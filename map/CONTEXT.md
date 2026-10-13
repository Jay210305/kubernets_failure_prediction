---
kind: system-map
source_revision: 32db139
checked: 2026-10-10
---

# ICM system map

Maintain this file using [the repo-local ICM skill](../.agents/skills/icm-architect/SKILL.md). It maps **what exists and what a change touches**. It complements the generated graph in `../graphify-out/`: ICM routes an agent through intent and first-order impact; graphify records relationships extracted from code. The refreshed graph covers only `google_boutique/extract_telemetry.py`, `telemetry_capture.py` and `telemetry_quality.py`; graph source locations are relative to `google_boutique/`. It is not a map of the 81 PDFs or the deployed cluster.

**Inputs:** the source files named below, their current Git state, and the research contract. **Process:** verify file purpose, actual data flow, and first-order impacts against those sources. **Output:** this map and the linked graphify artifacts. **Human check:** confirm the universe/status labels and any proposed change impact before using the map to plan edits.

## Objects and status

| Object | Source of truth | Universe | Meaning and first-order impact |
| --- | --- | --- | --- |
| Project goal | `docs/PROJECT_SCOPE.md` | live | Research question, target definitions, success criteria. Changes affect labels and evaluation. |
| Execution navigation | `docs/PROJECT_EXECUTION_PLAN.md`, `docs/project-phases/` | live as navigation; later phases planned | Phase/task/to-do route and links to execution evidence. Phases 01–02 record completed execution with human review pending; Phase 03 has eight performed documentation actions and one target-signal verification pending; Phase 04 has implemented collector/quality tooling and nine performed audit actions with measurement readiness failed. Changes affect handoffs and planned outputs. |
| Local demo setup | `README.md`, `google_boutique/kind-cluster.yaml`, `google_boutique/runs/*-evidence/` | documented configuration; dated deployment evidence exists | Three Ready kind nodes, demo pods and existing workload observed during Phase 04; this snapshot does not prove future runtime state. Changes affect capture provenance. |
| Telemetry collector | `google_boutique/extract_telemetry.py`, `telemetry_capture.py` | implemented; live capture performed | Explicit UTC bounds/column order, five audited features (four primary), NaN/masks, raw/source/receipt evidence, hashed manifests, safe CLI and explicit-column tensor helper. Changes affect capture schema and future causal model inputs. |
| Telemetry quality | `google_boutique/telemetry_quality.py`, `docs/telemetry/2026-10-10-phase04.md` | implemented; measurement readiness failed | Per-pair coverage/freshness/value/parity/hash/workload audit; all 44 required pairs fail source freshness. Changes affect Gate 2 and future label/training eligibility. |
| Dated captures | `google_boutique/runs/CONTEXT.md`, `phase04-20261011T021200Z-audited/` | present; diagnostic measurement only | Real workload values plus preserved failures/absence and provenance. Historical extraction receipt times do not establish online availability; this is not training-ready data. |
| Baseline capture | `google_boutique/baseline_run_01.csv`, `.parquet` | present, invalid as measurement | 361 timestamps × 55 metric columns, all metric values zero. Never train on it as a healthy baseline. |
| Paper corpus | `Bibliografia_Micro/*.pdf` | reference | 81 files, 75 distinct hashes. Changes affect evidence map, not running code. |
| Corpus index | `docs/CORPUS_INDEX.md` | live as completed Phase 01 output awaiting review | Source inventory, citation/edition decisions, first-pass screen, reading queue, and dated execution checks derived from the PDFs. Changes affect Phase 01 review and the Phase 02 paper review route. |
| Paper evidence notes | `docs/papers/CONTEXT.md`, `docs/papers/W*.md` | live as Phase 02 outputs awaiting review | Twenty source/page/hash-backed notes, with declared full/focused depth. Interpretation changes affect synthesis and protocol choices. |
| Literature synthesis | `docs/LITERATURE_SYNTHESIS.md` | live as Phase 02 output awaiting review | Keyed evidence matrix, seven decision themes, bounded gap and unresolved choices. Changes affect evidence review and Phase 03 protocol. |
| Experiment protocol | `docs/EXPERIMENT_PROTOCOL.md` | proposed; review and signal verification pending | Service-event oracle, four-feature/ten-output schema, timing, split support, comparators and alert rules. Changes affect future collectors, labels, tensor construction, training and scoring; no protocol implementation exists. |
| CNN–LSTM | `docs/PROJECT_SCOPE.md` | proposed | Architecture selected for research; no model implementation exists yet. |
| Failure labels and topology | `docs/EXPERIMENT_PROTOCOL.md`, `docs/RESEARCH_PLAN.md` | missing as measured artifacts; definitions proposed | Required before supervised prediction; no verified oracle operations, event log or service graph exists. Protocol layout v0 is an explicit assumption. |

## Actual movement

`Prometheus range/series/source-time APIs → raw evidence + UTC value/mask tables → CSV/Parquet + hashed manifest → quality report` is implemented by the telemetry collector/quality modules, accessed through `google_boutique/extract_telemetry.py`. The tensor helper explicitly maps columns and retains NaN; it is not run automatically and callers must split/filter before creating windows. The deployment instructions in `README.md` describe a separate manual movement from kind cluster creation to monitoring; Phase 04 used the existing deployment, not a new setup. No checked-in path currently connects windows to labels, training, forecasts, or actions.

## Change impact routes

- **PromQL, timing, or missing-value handling** → inspect extractor, CSV schema, [docs/BASELINE_AUDIT.md](../docs/BASELINE_AUDIT.md), [dated telemetry audit](../docs/telemetry/2026-10-10-phase04.md), capture/quality modules, manifests, and any later experiment using that data.
- **Service set or ordering** → inspect extractor, topology definition when created, window tensor shape, and model checkpoint compatibility.
- **Fault definition or lead time** → inspect [docs/PROJECT_SCOPE.md](../docs/PROJECT_SCOPE.md), [proposed protocol](../docs/EXPERIMENT_PROTOCOL.md), future label generation, split support/confirmation, and all evaluation claims.
- **Paper interpretation** → inspect the specific PDF, [docs/CORPUS_INDEX.md](../docs/CORPUS_INDEX.md), its [review handoff](../docs/CORPUS_INDEX.md#execution-checks-and-review-handoff), and [docs/LITERATURE_MAP.md](../docs/LITERATURE_MAP.md). Follow [paper notes](../docs/papers/CONTEXT.md) and [synthesis](../docs/LITERATURE_SYNTHESIS.md) before changing protocol implications. The paper note must distinguish its actual task from this project's task.
- **Phase or task ownership** → inspect [docs/PROJECT_EXECUTION_PLAN.md](../docs/PROJECT_EXECUTION_PLAN.md), the relevant phase/task `CONTEXT.md`, and its `TODO.md`; revise the canonical scope, audit, or protocol only when its facts change.

The map cites existing sources; it is not a second implementation specification. Recheck the cited file before editing. Query `graphify-out/graph.json` for code relationships after refreshing its code-only extraction when Python changes. [Source hashes](../graphify-out/telemetry-source-hashes.json) identify the local uncommitted source versions; commit identity alone is insufficient.
