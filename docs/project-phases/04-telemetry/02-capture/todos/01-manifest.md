---
kind: action-todo
status: work-complete-awaiting-review
---

# Prepare capture provenance

**Task:** [Capture representative telemetry](../CONTEXT.md)

**Inspect:** Reviewed query audit and intended Online Boutique workload.

## Exact work

- [x] Define manifest fields for cluster/config revision, Prometheus URL, scrape interval, query version, UTC bounds, service/pod labels, workload generator and interval, and raw/derived paths.

**Write:** Dated capture manifest template.

**Complete when:** A run cannot begin without knowing what evidence must be saved.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
