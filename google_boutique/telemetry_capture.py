"""Capture Prometheus evidence without filling missing measurements."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.metadata
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd
import requests

PROMETHEUS_URL = "http://localhost:9090"
NAMESPACE = "demo-app"
STEP = "5s"
QUERY_VERSION = "cadvisor-eth0-missing-preserving-v2"
SERVICES = ["frontend", "cartservice", "productcatalogservice", "currencyservice",
            "paymentservice", "shippingservice", "emailservice", "checkoutservice",
            "recommendationservice", "adservice", "redis-cart"]
PRIMARY_FEATURES = ["cpu_usage", "memory_usage", "network_rx", "network_tx"]
FEATURES = PRIMARY_FEATURES + ["http_errors"]
UNITS = dict(zip(FEATURES, ["cores", "bytes", "bytes/second", "bytes/second", "requests/second"]))


def utc(value):
    value = pd.Timestamp(value)
    if value.tzinfo is None:
        raise ValueError("Timestamps must have an explicit timezone; use UTC/Z.")
    return value.tz_convert("UTC")


def source_selectors(namespace=NAMESPACE):
    ns = json.dumps(namespace)
    base = f'namespace={ns},pod=~"{{service}}-.*",job="kubelet",metrics_path="/metrics/cadvisor"'
    return {
        "cpu_usage": f'container_cpu_usage_seconds_total{{{{{base},container!="",container!="POD"}}}}',
        "memory_usage": f'container_memory_working_set_bytes{{{{{base},container!="",container!="POD"}}}}',
        "network_rx": f'container_network_receive_bytes_total{{{{{base},interface="eth0"}}}}',
        "network_tx": f'container_network_transmit_bytes_total{{{{{base},interface="eth0"}}}}',
        "http_errors": f'http_requests_total{{{{namespace={ns},pod=~"{{service}}-.*",status=~"5.."}}}}',
    }


def metric_queries(namespace=NAMESPACE):
    return {k: f'sum({v})' if k == "memory_usage" else f'sum(rate({v}[30s]))'
            for k, v in source_selectors(namespace).items()}


METRIC_QUERIES = metric_queries()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False), encoding="utf-8")


def api_record(url, endpoint, params=None, timeout=10):
    """Preserve HTTP/body/API errors, warnings and receipt time, not apparent zeros."""
    record = {"url": url.rstrip("/") + endpoint, "params": params or {},
              "requested_at": dt.datetime.now(dt.timezone.utc).isoformat(), "http_status": None}
    try:
        response = requests.get(record["url"], params=params, timeout=timeout)
        record["http_status"] = response.status_code
        record["body"] = response.text
        response.raise_for_status()
        payload = response.json()
        record["payload"] = payload
        if payload.get("status") != "success":
            raise ValueError(f'Prometheus API status {payload.get("status")}: {payload.get("error")}')
    except (requests.RequestException, ValueError) as exc:
        record["error"] = str(exc)
    record["received_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return record


def range_values(record, grid):
    """Require a single aggregate and a timestamp on the requested UTC grid."""
    values = pd.Series(np.nan, index=grid, dtype=float)
    diagnostics = {"matched_series": 0, "returned_samples": 0, "off_grid": 0,
                   "duplicate_timestamps": 0, "invalid_values": 0}
    if "error" in record:
        return values, diagnostics
    payload = record.get("payload", {})
    if payload.get("data", {}).get("resultType") != "matrix":
        diagnostics["error"] = "Expected range matrix"
        return values, diagnostics
    result = payload.get("data", {}).get("result", [])
    diagnostics["matched_series"] = len(result)
    if len(result) != 1:
        if result:
            diagnostics["error"] = "Expected exactly one aggregate series"
        return values, diagnostics
    seen = set()
    for timestamp, raw in result[0].get("values", []):
        diagnostics["returned_samples"] += 1
        stamp = pd.Timestamp(float(timestamp), unit="s", tz="UTC")
        nearest = grid.get_indexer([stamp], method="nearest", tolerance=pd.Timedelta(milliseconds=1))[0]
        if nearest < 0:
            diagnostics["off_grid"] += 1
            continue
        if nearest in seen:
            diagnostics["duplicate_timestamps"] += 1
            values.iloc[nearest] = np.nan
            continue
        seen.add(nearest)
        try:
            number = float(raw)
            if not math.isfinite(number):
                raise ValueError("Nonfinite sample")
            values.iloc[nearest] = number
        except (ValueError, TypeError):
            diagnostics["invalid_values"] += 1
    return values, diagnostics


def capture(start, end, output_dir, *, prometheus_url=PROMETHEUS_URL,
            namespace=NAMESPACE, step=STEP, provenance=None):
    # Fail before creating an incomplete run if the selected runtime lacks Parquet.
    from pandas.io.parquet import get_engine
    get_engine("auto")
    start, end = utc(start), utc(end)
    if start >= end or end > pd.Timestamp.now(tz="UTC"):
        raise ValueError("Require start < end <= current time")
    if not re.fullmatch(r"[1-9][0-9]*s", step):
        raise ValueError("step must be a positive integer number of seconds")
    seconds = int(step[:-1])
    if any(int(v.timestamp()) % seconds or v.microsecond or v.nanosecond for v in [start, end]):
        raise ValueError("Bounds must be aligned to whole UTC step boundaries")
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=False)
    raw_dir = destination / "raw"
    raw_dir.mkdir()
    (destination / "collector-source.py").write_bytes(Path(__file__).read_bytes())
    save_json(destination / "manifest.json", {
        "capture_status": "in-progress", "format_version": 2, "query_version": QUERY_VERSION,
        "start_utc": start.isoformat(), "end_utc": end.isoformat(),
        "prometheus_url": prometheus_url, "namespace": namespace,
        "provenance": provenance or {},
        "note": "Incomplete until replaced by the final artifact-hashed manifest."})
    grid = pd.date_range(start, end, freq=step, name="timestamp")
    values = pd.DataFrame(index=grid)
    source_times = pd.DataFrame(index=grid)
    arrivals = pd.DataFrame(index=grid)
    audits = []
    queries, selectors = metric_queries(namespace), source_selectors(namespace)
    for service in SERVICES:
        for feature, template in queries.items():
            column = f"{service}_{feature}"
            # Registry IDs contain only DNS letters/digits/hyphens, which need no regex escaping.
            # re.escape('redis-cart') would insert an invalid PromQL string escape '\-'.
            query = template.format(service=service)
            selector = selectors[feature].format(service=service)
            params = {"query": query, "start": start.timestamp(), "end": end.timestamp(), "step": step}
            record = api_record(prometheus_url, "/api/v1/query_range", params)
            save_json(raw_dir / f"{column}.json", record)
            series, diag = range_values(record, grid)
            # Timestamp is evaluated on the source selector, before aggregation/rate hides it.
            stamp_record = api_record(prometheus_url, "/api/v1/query_range",
                                      {**params, "query": f"min(timestamp({selector}))"})
            save_json(raw_dir / f"{column}.source-time.json", stamp_record)
            stamps, stamp_diag = range_values(stamp_record, grid)
            metadata = api_record(prometheus_url, "/api/v1/series",
                                  {"match[]": selector, "start": start.timestamp(), "end": end.timestamp()})
            save_json(raw_dir / f"{column}.series.json", metadata)
            values[column] = series
            source_times[column] = stamps
            available = max(record["received_at"], stamp_record["received_at"])
            arrivals[column] = pd.Series(available, index=grid).where(series.notna() & stamps.notna())
            audits.append({"service": service, "feature": feature, "column": column,
                           "required": feature in PRIMARY_FEATURES, "unit": UNITS[feature],
                           "query": query, "selector": selector, "http_status": record["http_status"],
                           "error": record.get("error"), "warnings": record.get("payload", {}).get("warnings", []),
                           "source_time_error": stamp_record.get("error"),
                           "series_error": metadata.get("error"),
                           "labels": metadata.get("payload", {}).get("data", []),
                           "source_time_diagnostics": stamp_diag, **diag})
    observed = values.notna()
    values.to_csv(destination / "values.csv")
    values.to_parquet(destination / "values.parquet")
    observed.to_csv(destination / "observed.csv")
    observed.to_parquet(destination / "observed.parquet")
    source_times.to_parquet(destination / "source_times.parquet")
    arrivals.to_parquet(destination / "available_at.parquet")
    for name, endpoint in {"buildinfo": "/api/v1/status/buildinfo", "targets": "/api/v1/targets",
                           "config": "/api/v1/status/config"}.items():
        save_json(raw_dir / f"prometheus-{name}.json", api_record(prometheus_url, endpoint))
    manifest = {"format_version": 2, "capture_status": "complete", "query_version": QUERY_VERSION, "capture_mode": "retrospective-query-range",
                "prometheus_url": prometheus_url, "namespace": namespace, "start_utc": start.isoformat(),
                "end_utc": end.isoformat(), "query_step_seconds": seconds, "row_count": len(grid),
                "services": SERVICES, "features": FEATURES, "primary_features": PRIMARY_FEATURES,
                "columns": list(values.columns), "queries": audits, "provenance": provenance or {},
                "availability_note": "Receipt times belong to this extraction, not historical online availability.",
                "source_revision": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                                  text=True).stdout.strip(),
                "collector_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "dependencies": {name: importlib.metadata.version(name) for name in ["numpy", "pandas", "requests", "pyarrow"]},
                "artifacts": []}
    for file in sorted(destination.rglob("*")):
        if file.is_file() and file.name != "manifest.json":
            manifest["artifacts"].append({"path": file.relative_to(destination).as_posix(),
                                           "bytes": file.stat().st_size,
                                           "sha256": hashlib.sha256(file.read_bytes()).hexdigest()})
    save_json(destination / "manifest.json", manifest)
    return values, manifest


def query_prometheus_range(query, start_ts, end_ts, step=STEP):
    """Legacy list API: raises for failed requests; an empty result stays empty."""
    record = api_record(PROMETHEUS_URL, "/api/v1/query_range",
                        {"query": query, "start": start_ts, "end": end_ts, "step": step})
    if "error" in record:
        raise RuntimeError(record["error"])
    result = record["payload"].get("data", {}).get("result", [])
    if len(result) > 1:
        raise ValueError("Expected one aggregate series")
    return result[0].get("values", []) if result else []


def extract_dataset(start_time, end_time, output_filename="dataset_raw", **kwargs):
    """Compatibility entry: output_filename now names a NEW capture directory."""
    return capture(start_time, end_time, output_filename, **kwargs)[0]


def build_spatiotemporal_tensor(df, window_size=36, *, features=None):
    """Explicit-column value windows; retain NaN; split before calling this helper."""
    features = PRIMARY_FEATURES if features is None else list(features)
    if window_size < 1 or not features or len(features) != len(set(features)):
        raise ValueError("Require positive window_size and unique, nonempty features")
    columns = [f"{s}_{f}" for s in SERVICES for f in features]
    if not df.columns.is_unique or any(c not in df for c in columns):
        raise ValueError("Missing or duplicate schema columns")
    if not isinstance(df.index, pd.DatetimeIndex) or df.index.tz is None or not df.index.is_unique:
        raise ValueError("Require unique timezone-aware UTC timestamps")
    if str(df.index.tz) != "UTC" or not df.index.is_monotonic_increasing:
        raise ValueError("Require sorted UTC index")
    if len(df) > 1 and not (df.index.to_series().diff().dropna() == pd.Timedelta(seconds=5)).all():
        raise ValueError("Windows cannot cross gaps; this schema uses five-second cadence")
    array = df.loc[:, columns].to_numpy(dtype=float).reshape(len(df), len(SERVICES), len(features))
    count = max(0, len(df) - window_size + 1)
    if not count:
        return np.empty((0, window_size, len(SERVICES), len(features)), dtype=float)
    return np.stack([array[i:i + window_size] for i in range(count)])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True, help="UTC ISO timestamp aligned to five seconds")
    parser.add_argument("--end", required=True)
    parser.add_argument("--output-dir", required=True, help="Must not already exist")
    parser.add_argument("--prometheus-url", default=PROMETHEUS_URL)
    parser.add_argument("--namespace", default=NAMESPACE)
    parser.add_argument("--provenance", required=True, help="JSON with cluster/config/workload evidence")
    args = parser.parse_args()
    provenance = json.loads(Path(args.provenance).read_text(encoding="utf-8"))
    if "REQUIRED:" in json.dumps(provenance):
        parser.error("Fill the provenance template from actual evidence before capture")
    for key in ["cluster_context", "cluster_config_revision", "workload", "scrape_interval_evidence"]:
        if not provenance.get(key):
            parser.error(f"Provenance requires {key}")
    try:
        work = provenance["workload"]
        utc(work["verified_start_utc"])
        utc(work["verified_end_utc"])
        if not work.get("evidence_paths"):
            raise ValueError("Missing workload evidence paths")
    except (KeyError, ValueError, TypeError) as exc:
        parser.error(f"Workload UTC interval/evidence required: {exc}")
    _, manifest = capture(args.start, args.end, args.output_dir, prometheus_url=args.prometheus_url,
                          namespace=args.namespace, provenance=provenance)
    print(json.dumps({"capture": args.output_dir, "rows": manifest["row_count"],
                      "query_pairs": len(manifest["queries"])}))


if __name__ == "__main__":
    main()
