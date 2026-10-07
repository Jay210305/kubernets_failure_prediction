---
kind: agent-workflow
status: active
---

# Agent workflow and integrations

The root [AGENTS.md](../AGENTS.md) is the short routing contract. [CONTEXT.md](../CONTEXT.md) defines the research gates. Use the ICM map for human-maintained scope and change impact; use graphify for extracted code relationships. Do not infer deployment or scientific validity from either map.

The structure follows the [ICM architect method](https://github.com/RinDig/icm-architect/blob/main/SKILL.md): small entry files, explicit folder contracts, and source-linked maps. Keep it proportional to this small repository.

## Repo-local skills

| Skill | Trigger | Output |
| --- | --- | --- |
| `.agents/skills/icm-architect/SKILL.md` | Map the repository or update change impact | Source-linked ICM catalog, kept in `map/CONTEXT.md`; use graphify beside it for extracted code relationships. |
| `.agents/skills/review-paper/SKILL.md` | Add or revise a claim from a PDF in `Bibliografia_Micro/` | One evidence note based on the paper note template, with page references and task classification. |
| `.agents/skills/audit-telemetry/SKILL.md` | Inspect a capture, extraction script, or data quality claim | A data quality report and a pass/fail readiness verdict. |

Use the repo-local **icm-architect** skill for the human-maintained map and the installed **graphify** skill for code relationships; read both for mapping work. Use **pdf** when figures, tables, or page layout matter. Repo-local skills travel with the repository. No plugin is needed to read local PDFs or run local code.

## Specialist subagent roles, when parallel work is useful

These are proposed task briefs, not running agents. Delegate only independent, bounded work with a named output file; the main agent checks source citations and integrates results.

| Role | Bounded task | Handoff |
| --- | --- | --- |
| Literature screener | Read a disjoint set of PDFs and classify prediction, detection, localization, and remediation separately. | Paper notes and citation/page evidence; no synthesis claim without cross-check. |
| Telemetry auditor | Inspect query results, schema, missingness, timing, and capture provenance. | Quality report with counts and specific failing queries. |
| Experiment reviewer | Audit label timing, split leakage, metrics, and baseline comparability after protocols exist. | Findings tied to exact run IDs and files. |
| Topology mapper | Derive service dependencies from verified manifests/traces after deployment evidence exists. | Versioned adjacency/layout artifact and evidence source. |

Do not parallelize changes to the same dataset or experiment report. A subagent may recommend a model or fault definition but does not silently change the approved protocol.

## Plugins

The **GitHub** integration is connected for this project. It can inspect the [public repository](https://github.com/Jay210305/kubernets_failure_prediction), issues, pull requests, and CI. Repository metadata reports default branch `main`; a read-only check on 2026-10-06 found no open issues or open pull requests. Recheck live state before using it for a later task. Local Git and files remain sufficient for the current research baseline. Other integrations should be added only when a concrete external data source or collaboration workflow needs them; no cloud connector is required for the local PDFs.
