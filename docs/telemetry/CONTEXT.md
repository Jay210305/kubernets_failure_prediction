---
kind: folder-contract
---

# Telemetry audit evidence

**Inputs:** versioned collector source, dated raw captures/manifests and cluster/workload observations.

**Process:** use the repo-local audit-telemetry skill; distinguish configured cadence from observed source timestamps, measured zero from absent series, and code defects from hypotheses about old captures. Preserve dated earlier conclusions.

**Outputs:** query-by-query audits, value/coverage/parity findings and readiness decisions. [BASELINE_AUDIT.md](../BASELINE_AUDIT.md) links the current verdict; run artifacts remain under [the run shelf](../../google_boutique/runs/CONTEXT.md).

**Human check:** accept evidence and repairs before labels or training. A report stating failure completes audit work; it does not pass the research gate.
