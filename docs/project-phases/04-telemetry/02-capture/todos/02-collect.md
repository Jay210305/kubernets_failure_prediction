---
kind: action-todo
status: work-complete-awaiting-review
---

# Collect workload and telemetry

**Task:** [Capture representative telemetry](../CONTEXT.md)

**Inspect:** Verified endpoint/queries, manifest, and workload procedure.

## Exact work

- [x] Run only when the data-readiness phase is authorized; record actual workload interval and export raw query responses plus derived CSV/Parquet; preserve source values and missingness indicators.

**Write:** Dated capture files and completed manifest.

**Complete when:** The manifest names the exact workload and data files produced.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
