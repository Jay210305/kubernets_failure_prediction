---
kind: task-todo-index
status: work-complete-awaiting-review
---

# To-dos: Audit Prometheus queries

Complete these in order. Each item has its own evidence, output, and completion check. The [task summary](CONTEXT.md) states the task-level review gate.

1. [Verify Prometheus endpoint](todos/01-endpoint.md) — Endpoint finding in a dated query audit
2. [Inspect service and metric series](todos/02-series.md) — Query-by-query table in the audit
3. [Trace missingness through extraction](todos/03-alignment.md) — Root-cause and proposed repair section of the audit

Mark the task complete only after all items and its human check are reviewed.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
