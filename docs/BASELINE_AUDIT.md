---
kind: data-audit
status: failed-data-readiness
checked: 2026-10-06
---

# Initial baseline audit

## What is present

- `README.md` gives Windows commands for kind, Online Boutique, and Prometheus/Grafana. There is no checked-in cluster state or deployment verification.
- `google_boutique/extract_telemetry.py` requests CPU, memory, received/transmitted network bytes, and HTTP 5xx errors for 11 service names from Prometheus at `localhost:9095`, every five seconds. It writes CSV and Parquet, then builds 36-step windows.
- `google_boutique/baseline_run_01.csv` contains 361 timestamps from 2026-08-22 17:35:31.892595 to 18:05:31.892595 and 55 metric columns. A full numeric scan found **0 nonzero cells out of 19,855**. The Parquet file has the same 361 timestamps and 55 metric columns; its metric values also contain no nonzero cells. CSV and Parquet metric values and timestamps match after normalizing timestamp precision.

## Data-readiness verdict

**Failed.** All-zero metrics do not establish a healthy run or an observed failure. There are no failure labels, injected-fault records, workload records, or verified service topology in the repo. Model training or claimed prediction performance would be unsupported.

## Likely mechanisms to investigate, not confirmed causes

1. The README forwards Prometheus to `localhost:9090`, while the extractor queries `localhost:9095`.
2. The extractor joins Prometheus samples to a locally generated timestamp index by exact timestamp; differing offsets can leave joined values missing.
3. Missing or failed queries become zero, and the final fill replaces remaining gaps with zero. This hides unavailable telemetry.
4. The 5xx PromQL assumes a `http_requests_total` series with `namespace`, `pod`, and `status` labels; its availability must be checked. The `or vector(0)` clause also masks absent matches.

## Next evidence gate

Before another capture, record the live Prometheus URL, successful query count per feature and service, sample timestamps, pod/service label sets, actual NaN rate before filling, nonzero/variance counts, and a known workload interval. Preserve missingness separately from a measured zero. Confirm CSV/Parquet parity and write a capture manifest with cluster, scrape interval, query versions, start/end UTC times, and workload. Review this audit before labeling or training.
