---
kind: action-todo
status: planned
---

# Calculate service-level alert metrics

**Task:** [Report baseline performance](../CONTEXT.md)

**Inspect:** Held-out predictions, labels, split manifest, and metric definitions.

## Exact work

- [ ] For each service compute confusion counts, precision, recall, PR-AUC when defined, and false alerts per hour at validation-selected threshold; state denominator and missing-positive cases.

**Write:** Per-service table in baseline evaluation report.

**Complete when:** Numbers can be recomputed from prediction and label files.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
