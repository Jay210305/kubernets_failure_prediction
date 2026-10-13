---
kind: workspace-contract
status: setup
---

# Research workspace

The repeatable unit of work is a **prediction experiment**: a defined fault event and lead time, a versioned telemetry slice, labels, a model, and an evaluation report. The current work stops before training because the available baseline telemetry is invalid for measurement.

## Sequence

1. **Evidence and question** — read `Bibliografia_Micro/` through [docs/LITERATURE_MAP.md](docs/LITERATURE_MAP.md); specify the target, horizon, and comparison baselines in [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md).
2. **Data readiness** — collect and audit metrics, topology, workload, and fault events. Use [docs/BASELINE_AUDIT.md](docs/BASELINE_AUDIT.md) as the current checkpoint.
3. **Experiment** — only after a usable labeled dataset exists, train chronological baselines and the CNN–LSTM, then report service-level and episode-level results. [docs/RESEARCH_PLAN.md](docs/RESEARCH_PLAN.md) defines the gates.

Stable references live in `docs/`, `.agents/skills/`, and `map/`. Existing run artifacts live under `google_boutique/`; raw papers remain in `Bibliografia_Micro/`. The source files stay in place. Derived experiment outputs should get their own dated run directory when that stage begins.

The work is decomposed into numbered phases, task summaries, and to-dos in [docs/PROJECT_EXECUTION_PLAN.md](docs/PROJECT_EXECUTION_PLAN.md). That navigation refines the sequence above; [docs/RESEARCH_PLAN.md](docs/RESEARCH_PLAN.md) remains the canonical gate list.

For each step, an agent reads only its contract, the linked sources, and its working input. A human reviews the resulting question, data audit, or experiment report before it becomes the next step's premise. The presence of an output file records progress; an unreviewed output is still a draft.

| Step | Working input | Output | Human check |
| --- | --- | --- | --- |
| Evidence and question | Named PDFs and current scope | Paper notes and finalized prediction contract | Claims have page evidence; target and horizon match the intended operational action. |
| Data readiness | Extractor, capture files, live query evidence if requested | Dated quality audit and capture manifest | Nonzero/coverage checks and fault provenance support the data claim. |
| Experiment | Reviewed protocol and labeled episodes | Reproducible run report | Split integrity, comparator fairness, lead time, and false alert rate are acceptable. |
