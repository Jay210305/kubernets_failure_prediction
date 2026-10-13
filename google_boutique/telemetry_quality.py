"""Audit saved captures; never infer health from absent or constant telemetry."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


def quality_report(directory):
    directory = Path(directory)
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    snapshot = directory / f"quality-source-{code_hash[:12]}.py"
    if not snapshot.exists():
        snapshot.write_bytes(Path(__file__).read_bytes())
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("capture_status") == "in-progress":
        raise ValueError("Incomplete capture: no final artifact-hashed manifest")
    frame = pd.read_parquet(directory / "values.parquet")
    csv = pd.read_csv(directory / "values.csv", index_col=0)
    csv.index = pd.to_datetime(csv.index, utc=True)
    mask = pd.read_parquet(directory / "observed.parquet")
    csv_mask = pd.read_csv(directory / "observed.csv", index_col=0)
    csv_mask.index = pd.to_datetime(csv_mask.index, utc=True)
    sources = pd.read_parquet(directory / "source_times.parquet")
    artifacts = []
    for item in manifest["artifacts"]:
        path = directory / item["path"]
        # Reject traversal in an untrusted manifest.
        if not path.resolve().is_relative_to(directory.resolve()):
            raise ValueError("Artifact path escapes capture directory")
        valid = path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
        artifacts.append({"path": item["path"], "hash_matches": valid})
    evidence_checks = []
    for item in manifest.get("provenance", {}).get("evidence_artifacts", []):
        path = Path(item["path"])
        if not path.resolve().is_relative_to(Path.cwd().resolve()):
            raise ValueError("External evidence escapes the current project directory")
        evidence_checks.append({"path": item["path"], "hash_matches": path.is_file() and
                                hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]})
    schema = list(frame.columns) == manifest["columns"] == list(csv.columns)
    parity = (schema and frame.index.equals(csv.index) and
              np.allclose(frame.to_numpy(), csv.to_numpy(), rtol=1e-12, atol=1e-12, equal_nan=True))
    mask_parity = mask.index.equals(csv_mask.index) and mask.equals(csv_mask)
    mask_consistent = mask.equals(frame.notna())
    expected = pd.date_range(manifest["start_utc"], manifest["end_utc"],
                             freq=f'{manifest["query_step_seconds"]}s', name="timestamp")
    timing = frame.index.equals(expected)
    # pandas indexes may store microseconds or nanoseconds; timestamp() is unit-independent.
    endpoint = pd.Series([stamp.timestamp() for stamp in frame.index], index=frame.index)
    records = []
    for query in manifest["queries"]:
        column = query["column"]
        values = frame[column]
        observed = values.dropna()
        ages = endpoint - sources[column]
        fresh = (ages.ge(0) & ages.le(10)) & values.notna()
        errors = [query.get(k) for k in ["error", "source_time_error", "series_error"] if query.get(k)]
        coverage = float(values.notna().mean()) if len(values) else 0.0
        fresh_coverage = float(fresh.mean()) if len(values) else 0.0
        varying = observed.nunique() > 1
        nonzero = int(observed.ne(0).sum())
        reasons = []
        if errors: reasons.append("query/source/metadata errors")
        if coverage < .95: reasons.append("coverage below 95%")
        if fresh_coverage < .95: reasons.append("fresh coverage below 95% (10s maximum age)")
        if observed.lt(0).any(): reasons.append("negative nonnegative metric")
        if not nonzero: reasons.append("no observed nonzero measurement")
        if not varying: reasons.append("constant series; workload evidence insufficient")
        if query.get("off_grid") or query.get("duplicate_timestamps") or query.get("invalid_values"):
            reasons.append("range alignment/duplicate/nonfinite samples")
        if query.get("warnings"): reasons.append("Prometheus warnings require review")
        if query.get("source_time_diagnostics", {}).get("error") or query.get("error"):
            reasons.append("unexpected query shape")
        records.append({"column": column, "required": query["required"], "expected": len(expected),
                        "observed": int(values.notna().sum()), "coverage": coverage,
                        "missing": int(values.isna().sum()), "nonzero": nonzero,
                        "distinct": int(observed.nunique()),
                        "min": float(observed.min()) if len(observed) else None,
                        "max": float(observed.max()) if len(observed) else None,
                        "maximum_source_age_s": float(ages.max()) if ages.notna().any() else None,
                        "fresh_coverage": fresh_coverage, "query_failures": errors,
                        "verdict": "pass" if not reasons else "fail", "reasons": reasons})
    workload = manifest.get("provenance", {}).get("workload", {})
    try:
        wstart, wend = pd.Timestamp(workload["verified_start_utc"]), pd.Timestamp(workload["verified_end_utc"])
        workload_overlap = bool(wstart.tzinfo and wend.tzinfo and wstart <= expected[0] and wend >= expected[-1]
                                and workload.get("evidence_paths"))
    except (KeyError, ValueError, IndexError):
        workload_overlap = False
    failures = [r["column"] for r in records if r["required"] and r["verdict"] != "pass"]
    integrity = all(a["hash_matches"] for a in artifacts)
    evidence_integrity = bool(evidence_checks) and all(a["hash_matches"] for a in evidence_checks)
    passed = not failures and parity and mask_parity and mask_consistent and timing and integrity and evidence_integrity and workload_overlap
    report = {"capture": directory.name, "measurement_readiness": "pass-awaiting-human-review" if passed else "fail",
              "quality_code_sha256": code_hash, "quality_source_snapshot": snapshot.name,
              "training_readiness": "not-ready: missing event oracle/episodes, topology acceptance and historical availability",
              "rows": len(frame), "columns": len(frame.columns), "csv_parquet_parity": bool(parity),
              "mask_parity": bool(mask_parity), "mask_consistent": bool(mask_consistent),
              "utc_grid_matches": bool(timing), "artifact_integrity": integrity,
              "provenance_integrity": evidence_integrity, "evidence_artifacts": evidence_checks,
              "workload_covers_capture": workload_overlap, "failed_required_columns": failures,
              "series": records, "artifacts": artifacts,
              "limits": ["Query evaluation timestamps are not scrape timestamps; source ages are reported separately.",
                         "Retrospective receipt times do not prove historical inference availability.",
                         "Clock synchronization and replica/network aggregation still require review."]}
    (directory / "quality.json").write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
    lines = ["# Capture quality report", "", f'**Measurement verdict:** {report["measurement_readiness"]}.',
             f'**Training:** {report["training_readiness"]}.', "",
             f"Rows: {len(frame)}; CSV/Parquet parity: {parity}; observed-mask parity: {mask_parity}; hashes: {integrity}; UTC grid: {timing}; workload overlap: {workload_overlap}.", "",
             "| Series | Required | Observed / expected | Nonzero | Distinct | Fresh coverage | Verdict / reasons |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for item in records:
        lines.append(f'| {item["column"]} | {item["required"]} | {item["observed"]}/{item["expected"]} | {item["nonzero"]} | {item["distinct"]} | {item["fresh_coverage"]:.1%} | {item["verdict"]}: {"; ".join(item["reasons"])} |')
    lines += ["", "## Limits", ""] + [f"- {v}" for v in report["limits"]]
    (directory / "QUALITY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture_dir")
    args = parser.parse_args()
    result = quality_report(args.capture_dir)
    print(json.dumps({k: result[k] for k in ["measurement_readiness", "rows", "csv_parquet_parity",
                                             "failed_required_columns"]}))
    raise SystemExit(0 if result["measurement_readiness"] == "pass-awaiting-human-review" else 2)
