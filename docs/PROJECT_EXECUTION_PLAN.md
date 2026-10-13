---
kind: project-execution-plan
status: planning-draft
checked: 2026-10-10
---

# Project execution plan

This is the entry point for the [phase, task, and to-do hierarchy](project-phases/CONTEXT.md). Each phase has a `CONTEXT.md`; each task has a short `CONTEXT.md`, a `TODO.md` index, and three focused Markdown to-dos under `todos/`. Each to-do states what to inspect, the exact work, its output, and a completion check. A checkbox describes future work until its evidence and human gate are reviewed.

## Alignment with existing repository documents

| Existing source | What it establishes | How the phase plan uses it |
| --- | --- | --- |
| [Root workflow](../CONTEXT.md) | Evidence/question → data readiness → experiment; the repeatable unit is a prediction experiment. | Phases 01–03 complete evidence/question, 04 completes data readiness, and 05–08 cover experiment and report. |
| [Agent rules](../AGENTS.md) | Service-level advance prediction, selected CNN–LSTM, evidence and split rules, source preservation. | These constraints apply to every task. |
| [Project scope](PROJECT_SCOPE.md) | Draft service-time prediction unit, possible targets, input structure, metrics, and exclusions. | Phase 03 resolves open event, lead, horizon, and layout choices. |
| [Literature map](LITERATURE_MAP.md) | Selected-paper overview and route to the corpus index and ranked queue. | Phase 01 records inventory and screening evidence; Phase 02 reviews selected PDFs and synthesizes findings. |
| [Research gates](RESEARCH_PLAN.md) | Five approval gates from evidence through CNN–LSTM. | Phase gates refine those five gates; they do not replace them. |
| [Baseline audit](BASELINE_AUDIT.md) | Existing capture has 0 nonzero metric cells; no labels or topology are verified. | Phase 04 must establish data readiness before phases 05–07 run. |
| [Agent workflow](AGENT_WORKFLOW.md) | Roles, local skills, and review handoffs. | Paper and telemetry tasks route through the named local skills; task folders do not authorize delegation. |

The comparison baselines are **specified model families** in `PROJECT_SCOPE.md`; no training results exist yet. The existing `baseline_run_01` is an invalid telemetry capture and is not a healthy baseline. No model implementation, labels, or verified service graph currently exists in the repository.

## Phases

| Phase | Main deliverable | Research gate |
| --- | --- | --- |
| [01 — Bibliography inventory and screening](project-phases/01-bibliography/CONTEXT.md) | Source index and reading queue | Gate 1: evidence and question |
| [02 — Evidence review and synthesis](project-phases/02-literature/CONTEXT.md) | Page-evidenced notes and thematic review | Gate 1 |
| [03 — Prediction contract and protocol](project-phases/03-protocol/CONTEXT.md) | Target, lead/horizon, inputs, splits, and metrics | Gate 1 |
| [04 — Telemetry readiness](project-phases/04-telemetry/CONTEXT.md) | Capture manifest and quality verdict | Gate 2: telemetry |
| [05 — Fault episodes and labels](project-phases/05-episodes-labels/CONTEXT.md) | Episode log and reproducible labels | Gate 3: episodes |
| [06 — Baseline evaluation](project-phases/06-baselines/CONTEXT.md) | Operational, tabular, temporal results | Gate 4: baselines |
| [07 — CNN–LSTM evaluation](project-phases/07-cnn-lstm/CONTEXT.md) | Primary-model comparison and sensitivity | Gate 5: CNN–LSTM |
| [08 — Final report and reproducibility](project-phases/08-report/CONTEXT.md) | Research report and run provenance | Final synthesis |

## Review logic

Start with the bibliography because the corpus is large: index and deduplicate PDFs first, screen unique works from targeted Markdown sections, then deep-review only papers that can change a named decision. Markdown extractions guide navigation; substantive claims and page numbers come from PDFs. `LITERATURE_MAP.md` remains navigation, `docs/papers/` holds compact evidence notes, and `docs/LITERATURE_SYNTHESIS.md` holds thematic conclusions.

The target, lead interval, and horizon remain draft while phases 01–02 gather evidence. Phase 03 proposes concrete definitions in [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md); human acceptance and target-signal verification are required before freeze and model evaluation. During later phases, split by chronology and fault episode before creating overlapping windows; fit preprocessing on training data only; compare the selected CNN–LSTM with the specified baseline families on the same held-out episodes.

**Current status:** Phases 01–02 execution is complete and awaits human review. [Phase 01 source checks](CORPUS_INDEX.md#execution-checks-and-review-handoff) and [Phase 02 notes/synthesis checks](LITERATURE_SYNTHESIS.md#execution-checks-and-review-handoff) record the evidence. Phase 02 covers all twenty queued studies at full/focused depth. Phase 03 has a concrete [protocol draft](EXPERIMENT_PROTOCOL.md), eight performed documentation actions and one event action pending signal verification. Phase 04 collector/quality tooling and its nine audit actions are performed; [real capture evidence](telemetry/2026-10-10-phase04.md) fails source freshness readiness and awaits human review. Phases 05–08 remain planned. Research Gate 1 remains open because human evidence/protocol acceptance and a verified target signal are pending. Gate 2 remains failed: the old capture is all zero, and new real measurements fail the proposed source freshness requirement. Research experiments begin only after the relevant gate and data prerequisites pass.
