---
kind: action-todo
status: work-complete-awaiting-review
---

# Fix observation and forecast timing

**Task:** [Define the target event](../CONTEXT.md)

**Inspect:** Selected event, data cadence, and intended operator response.

## Exact work

- [x] Specify decision time t, input history and cadence, minimum lead_min, forecast horizon, and event interval (t + lead_min, t + horizon]; explain how onset and alert time are recorded.

**Write:** Timing contract in docs/EXPERIMENT_PROTOCOL.md.

**Complete when:** A reviewer can label a service-time sample without using future inputs.

Draft outputs and source limitations are recorded below. Checked boxes record documentation work, not human acceptance or verified runtime measurements.

## Draft execution evidence

**Prepared:** 2026-10-10. [Experiment protocol](../../../../EXPERIMENT_PROTOCOL.md), section 3, and [scope](../../../../PROJECT_SCOPE.md). See the protocol action record for exact source assumptions, proposed settings and prerequisites. **Human review:** pending.
