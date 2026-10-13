---
kind: folder-contract
---

# Research documentation shelf

**Inputs:** the user-approved research aim, current repository files, and named papers. **Process:** keep the single authoritative scope, baseline audit, research gates, literature map, and agent workflow here; navigate the staged work through [PROJECT_EXECUTION_PLAN.md](PROJECT_EXECUTION_PLAN.md) and [project-phases/CONTEXT.md](project-phases/CONTEXT.md). **Outputs:** reviewed Markdown documents and paper notes made from `_templates/paper-note.md`. **Human check:** accept target definitions, data-readiness verdicts, and interpretation of prior work before an experiment depends on them.

Do not copy raw PDFs or captured datasets into this folder. Link to their existing homes. Treat `LITERATURE_MAP.md` as navigation and individual paper notes as the evidence home for detailed claims.

`project-phases/` contains phase and task contracts, task-level `TODO.md` indexes, and individual action files in each task's `todos/` folder. Its planned deliverable paths are proposals until the corresponding outputs are created and reviewed.

Completed evidence outputs awaiting review: [corpus index](CORPUS_INDEX.md), [paper-note shelf](papers/CONTEXT.md), and [literature synthesis](LITERATURE_SYNTHESIS.md). The map owns navigation; notes own PDF claims; synthesis owns cross-paper decisions. Changes to a source interpretation flow through note → synthesis → proposed Phase 03 protocol.

[EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) now owns the proposed target/timing, feature/tensor schema, split rules, model selection and alert metrics. It is an unaccepted draft with target-signal verification pending. Interpretation changes flow from paper note → synthesis → protocol revision; implementation must wait for the relevant research gates.

[Telemetry audits](telemetry/CONTEXT.md) now own the dated query/quality evidence and repair handoff; raw/derived run artifacts remain in `google_boutique/runs/`. Phase 04 implemented measurement tooling and recorded a failing freshness verdict; no human gate is passed by the audit alone.
