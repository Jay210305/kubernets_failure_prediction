# Agent entry point

This repository studies advance prediction of failures in a microservice application. Read [CONTEXT.md](CONTEXT.md) for the research workflow and [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md) for the current objective and boundaries.

## Routes

| Task | Open first |
| --- | --- |
| Map or update the system/change-impact map | `.agents/skills/icm-architect/SKILL.md`, then [map/CONTEXT.md](map/CONTEXT.md) |
| Trace code relationships or refresh the extracted code graph | installed `graphify` skill, then `graphify-out/` |
| Review prior work or add a paper | [docs/LITERATURE_MAP.md](docs/LITERATURE_MAP.md), then `.agents/skills/review-paper/SKILL.md` |
| Inspect telemetry or change extraction | [docs/BASELINE_AUDIT.md](docs/BASELINE_AUDIT.md), then `.agents/skills/audit-telemetry/SKILL.md` |
| Design a prediction experiment | [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md) and [docs/RESEARCH_PLAN.md](docs/RESEARCH_PLAN.md) |
| Follow the project phases and task to-dos | [docs/PROJECT_EXECUTION_PLAN.md](docs/PROJECT_EXECUTION_PLAN.md), then [docs/project-phases/CONTEXT.md](docs/project-phases/CONTEXT.md) |
| Set up the demo cluster | [README.md](README.md) and `google_boutique/kind-cluster.yaml` |
| Decide whether to delegate or use integrations | [docs/AGENT_WORKFLOW.md](docs/AGENT_WORKFLOW.md) |

## Research rules

- Treat the user-selected CNN–LSTM as the primary architecture to evaluate. A comparison model is a baseline, not a replacement without a documented decision.
- Never describe anomaly detection, fault localization, pod failure, and advance service failure prediction as the same task. State the target event, service, observation window, and lead time for each experiment.
- Verify telemetry values and labels before training. `baseline_run_01` is all zero and is not evidence that services were healthy.
- Split evaluation by time and failure episode before making overlapping windows. Keep preprocessing fit to the training split.
- Cite the exact paper or source file for research claims. Mark hypotheses and unverified implementation assumptions plainly.
- Preserve existing raw PDFs and baseline data. Record provenance for new datasets, fault injections, and derived artifacts.
- Read the relevant folder contract before changing its contents. Update the ICM map when a file's purpose, inputs, outputs, or first-order impacts change.
- Use the repo-local `icm-architect` skill for system mapping and change impact. Use the installed `graphify` skill for extracted code relationships. For a map task that involves both, use them together and keep graphify's code-only scope stated in [map/CONTEXT.md](map/CONTEXT.md).

Do not start cluster experiments, inject faults, publish artifacts, or connect external services as a side effect of documentation work.
