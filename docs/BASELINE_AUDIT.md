---
kind: data-audit
status: failed-data-readiness
checked: 2026-10-10
---

# Baseline and telemetry readiness audit

**Current verdict (2026-10-10): failed measurement readiness.** A new real workload capture contains nonzero/variable metrics with matching CSV/Parquet/masks, but source freshness fails the proposed protocol. See [the dated Phase 04 query and quality audit](telemetry/2026-10-10-phase04.md) for all 55 query pairs, source ages, provenance and repair actions. The original baseline remains unchanged and invalid.

## Historical baseline findings (2026-10-06)

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

## Re-measurement and implementation handoff (2026-10-10)

The old baseline was remeasured: 361 rows × 55 metrics, zero nonzero cells, matching CSV/Parquet and unchanged source hashes. The historical causal hypotheses above remain hypotheses about that old capture. The collector has since been repaired; its configurable default endpoint is 9090 and the actual capture used an explicit temporary 9095 forward. Follow [the current audit](telemetry/2026-10-10-phase04.md), [run contract](../google_boutique/runs/CONTEXT.md), [capture provenance template](_templates/capture-manifest.json), and [protocol](EXPERIMENT_PROTOCOL.md) before proceeding. Labels/training remain blocked by measurement freshness, missing request oracle/episodes and unverified historical availability/topology.
