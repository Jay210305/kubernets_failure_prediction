---
kind: action-todo
status: work-complete-awaiting-review
---

# Trace missingness through extraction

**Task:** [Audit Prometheus queries](../CONTEXT.md)

**Inspect:** Extractor timestamp construction, merge logic, zero-fill behavior, and baseline audit.

## Exact work

- [x] Compare Prometheus sample times with generated index times; identify where exact joins or fallbacks lose samples; propose changes that preserve missingness and real zeros distinctly.

**Write:** Root-cause and proposed repair section of the audit.

**Complete when:** Confirmed causes cite query or code evidence; unsupported causes stay hypotheses.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
