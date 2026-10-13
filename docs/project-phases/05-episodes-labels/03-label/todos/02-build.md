---
kind: action-todo
status: planned
---

# Build service-time labels

**Task:** [Generate forecast labels](../CONTEXT.md)

**Inspect:** Verified episode log and quality-approved telemetry timeline.

## Exact work

- [ ] For each eligible service/time decision point, compute the label and link any positive to episode ID; preserve missingness and label version; exclude ambiguous intervals.

**Write:** Versioned labeled dataset and manifest.

**Complete when:** Every positive row traces to a verified onset and every input is at or before t.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
