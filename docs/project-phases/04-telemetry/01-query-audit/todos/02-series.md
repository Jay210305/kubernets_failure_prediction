---
kind: action-todo
status: work-complete-awaiting-review
---

# Inspect service and metric series

**Task:** [Audit Prometheus queries](../CONTEXT.md)

**Inspect:** Five extractor queries across eleven services and live Prometheus metadata when available.

## Exact work

- [x] For every service-feature pair record query, HTTP response, matched series, label sets, sample count, timestamps, nonzero range, and query failures; inspect 5xx metric name/status labels.

**Write:** Query-by-query table in the audit.

**Complete when:** Missing series are visible rather than converted into apparent zeros.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
