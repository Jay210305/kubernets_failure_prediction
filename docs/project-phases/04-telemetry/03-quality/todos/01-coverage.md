---
kind: action-todo
status: work-complete-awaiting-review
---

# Measure coverage and timing

**Task:** [Judge data readiness](../CONTEXT.md)

**Inspect:** Completed capture and manifest.

## Exact work

- [x] Calculate expected versus observed samples per service-feature, missingness before imputation, query failures, timestamp alignment and drift, and workload overlap.

**Write:** Coverage table in dated data-quality report.

**Complete when:** Every required feature has measured coverage and timing evidence.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
