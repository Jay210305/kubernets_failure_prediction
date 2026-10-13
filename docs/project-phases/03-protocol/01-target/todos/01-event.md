---
kind: action-todo
status: in-progress-awaiting-signal-verification
---

# Choose measurable service event

**Task:** [Define the target event](../CONTEXT.md)

**Inspect:** docs/PROJECT_SCOPE.md, literature synthesis, and available telemetry signals.

## Exact work

- [ ] Compare candidate service unavailable, sustained 5xx, and Kubernetes state events; choose one primary target and justify operational meaning and observability; define service set and event threshold/duration.

**Write:** Target definition in docs/PROJECT_SCOPE.md and docs/EXPERIMENT_PROTOCOL.md.

**Complete when:** The event is service-level and can be recognized from a verified signal.

Draft outputs and source limitations are recorded below. Checked boxes record documentation work, not human acceptance or verified runtime measurements.

## Draft execution evidence

**Prepared:** 2026-10-10. [Experiment protocol](../../../../EXPERIMENT_PROTOCOL.md), section 2, and [scope](../../../../PROJECT_SCOPE.md). See the protocol action record for exact source assumptions, proposed settings and prerequisites. **Human review:** pending.

The candidate comparison, user-selected target, proposed service registry and measurable oracle definition are prepared. This action remains unchecked because its completion condition requires a **verified service-level signal**, and none exists in the current capture. Phase 04 must validate the oracle before this action or Gate 1 can pass; no event is inferred from the all-zero data.
