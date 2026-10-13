---
kind: action-todo
status: work-complete-awaiting-review
---

# Preserve and identify artifacts

**Task:** [Capture representative telemetry](../CONTEXT.md)

**Inspect:** Captured files and existing baseline_run_01 files.

## Exact work

- [x] Compute file hashes, record row/time ranges and schema, verify raw and derived paths, and retain baseline_run_01 unchanged; note incomplete captures.

**Write:** Artifact section of capture manifest.

**Complete when:** A reviewer can distinguish old invalid baseline data from new capture data.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
