---
kind: task-contract
status: work-complete-awaiting-review
---

# Audit Prometheus queries

**Purpose:** Audit Prometheus queries within [Telemetry readiness](../CONTEXT.md).

**Inputs:** docs/BASELINE_AUDIT.md, .agents/skills/audit-telemetry/SKILL.md, google_boutique/extract_telemetry.py.

**Expected output:** dated query audit linked from docs/BASELINE_AUDIT.md.

**Work:** Follow the [to-do index](TODO.md), then its three linked action files. Each action file names evidence, output, and a completion check.

**Human check:** A query-by-query audit distinguishes measured zero from missing data.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
