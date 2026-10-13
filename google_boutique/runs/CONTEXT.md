---
kind: folder-contract
status: measurement-readiness-failed
---

# Telemetry capture runs

**Inputs:** explicit UTC bounds, local Prometheus endpoint, namespace, versioned queries, cluster/pod/node metadata and observed workload provenance.

**Process:** use `../extract_telemetry.py` with the existing project environment. Capture into a new directory, retain raw API responses/errors, NaN values, measured-value masks, source timestamps and retrospective receipt times. Run `../telemetry_quality.py` for a dated saved-artifact audit. Interrupted attempts stay identifiable and preserved; no fault injection, labels or training occurs here.

**Outputs:** capture `manifest.json`, raw JSON, CSV/Parquet values/masks, source/arrival metadata and quality reports. Sibling `*-evidence/` directories hold saved cluster/workload/config evidence; manifests record their hashes and paths. Failed attempts are references for diagnosis, not healthy/training data.

**Human check:** accept per-series coverage, actual cadence/freshness, correct aggregation, workload support and provenance before declaring measurement ready. Retrospective query receipt times do not establish historical inference availability. The [dated audit](../../docs/telemetry/2026-10-10-phase04.md) records the canonical run and remaining limitations.
