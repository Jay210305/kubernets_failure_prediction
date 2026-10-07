---
kind: system-map
source_revision: 32db139
checked: 2026-10-06
---

# ICM system map

Maintain this file using [the repo-local ICM skill](../.agents/skills/icm-architect/SKILL.md). It maps **what exists and what a change touches**. It complements the generated graph in `../graphify-out/`: ICM routes an agent through intent and first-order impact; graphify records relationships extracted from code. The graph currently covers only `google_boutique/extract_telemetry.py`; graph source locations are relative to `google_boutique/`. It is not a map of the 81 PDFs or the deployed cluster.

**Inputs:** the source files named below, their current Git state, and the research contract. **Process:** verify file purpose, actual data flow, and first-order impacts against those sources. **Output:** this map and the linked graphify artifacts. **Human check:** confirm the universe/status labels and any proposed change impact before using the map to plan edits.

## Objects and status

| Object | Source of truth | Universe | Meaning and first-order impact |
| --- | --- | --- | --- |
| Project goal | `docs/PROJECT_SCOPE.md` | live | Research question, target definitions, success criteria. Changes affect labels and evaluation. |
| Local demo setup | `README.md`, `google_boutique/kind-cluster.yaml` | live as documentation/configuration | Describes kind, Online Boutique, Prometheus, Grafana. Changes affect collection instructions; deployment state is unverified. |
| Telemetry extractor | `google_boutique/extract_telemetry.py` | live but unvalidated | PromQL, service order, five features, export, and sliding windows. Changes affect dataset schema and model input. |
| Baseline capture | `google_boutique/baseline_run_01.csv`, `.parquet` | present, invalid as measurement | 361 timestamps × 55 metric columns, all metric values zero. Never train on it as a healthy baseline. |
| Paper corpus | `Bibliografia_Micro/*.pdf` | reference | 81 files, 75 distinct hashes. Changes affect evidence map, not running code. |
| CNN–LSTM | `docs/PROJECT_SCOPE.md` | proposed | Architecture selected for research; no model implementation exists yet. |
| Failure labels and topology | `docs/RESEARCH_PLAN.md` | missing | Required before supervised prediction; no verified event log or service graph is in the repo. |

## Actual movement

`Prometheus query_range → service × metric table → CSV/Parquet → sliding window tensor` is implemented in `google_boutique/extract_telemetry.py`. The deployment instructions in `README.md` describe a separate manual movement from kind cluster creation to monitoring. No checked-in path currently connects windows to labels, training, forecasts, or actions.

## Change impact routes

- **PromQL, timing, or missing-value handling** → inspect extractor, CSV schema, [docs/BASELINE_AUDIT.md](../docs/BASELINE_AUDIT.md), and any later experiment using that data.
- **Service set or ordering** → inspect extractor, topology definition when created, window tensor shape, and model checkpoint compatibility.
- **Fault definition or lead time** → inspect [docs/PROJECT_SCOPE.md](../docs/PROJECT_SCOPE.md), label generation, split boundaries, and all evaluation claims.
- **Paper interpretation** → inspect the specific PDF and [docs/LITERATURE_MAP.md](../docs/LITERATURE_MAP.md). The paper note must distinguish its actual task from this project's task.

The map cites existing sources; it is not a second implementation specification. Recheck the cited file before editing. Query `graphify-out/graph.json` for code relationships after refreshing its code-only extraction when Python changes.
