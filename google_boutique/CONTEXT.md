---
kind: folder-contract
status: data-readiness-failed
---

# Demo and telemetry shelf

**Inputs:** `kind-cluster.yaml`, the live environment when explicitly inspected, `extract_telemetry.py`, and its captures. **Process:** deploy or capture only when requested; audit each query and dataset before modeling. **Outputs:** capture files and a linked quality audit in `../docs/BASELINE_AUDIT.md`. **Human check:** verify environment, workload, data coverage, and failure-event provenance before declaring a capture usable.

The present `baseline_run_01` CSV/Parquet pair is all zero. The README describes cluster setup; it does not prove a currently running deployment.

Phase 04 collector/quality implementation is accessed through `extract_telemetry.py`; `telemetry_capture.py` owns extraction/provenance and `telemetry_quality.py` owns saved-capture audits. [Run contract](runs/CONTEXT.md) and [dated audit](../docs/telemetry/2026-10-10-phase04.md) record actual deployment/workload evidence and failed freshness readiness. Four primary features and optional HTTP-error diagnostics are explicit; label-oracle/model implementation remains separate.
