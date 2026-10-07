---
kind: folder-contract
status: data-readiness-failed
---

# Demo and telemetry shelf

**Inputs:** `kind-cluster.yaml`, the live environment when explicitly inspected, `extract_telemetry.py`, and its captures. **Process:** deploy or capture only when requested; audit each query and dataset before modeling. **Outputs:** capture files and a linked quality audit in `../docs/BASELINE_AUDIT.md`. **Human check:** verify environment, workload, data coverage, and failure-event provenance before declaring a capture usable.

The present `baseline_run_01` CSV/Parquet pair is all zero. The README describes cluster setup; it does not prove a currently running deployment.
