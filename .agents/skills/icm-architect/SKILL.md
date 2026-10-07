---
name: icm-architect
description: Design any process, idea, problem, or body of knowledge into an ICM workspace, or restructure an existing folder, repo, or vault to make it walkable for agents.
---

# ICM Architect

Use this skill to maintain the repository's human-readable system map alongside graphify's extracted code graph. ICM records what the project concepts are, how the actual workflows move, and what a change affects. Graphify records relationships it extracts from code. Keep the ICM map source-linked and graphify's scope explicit.

## Project mapping route

For this repository, read `map/CONTEXT.md` and `docs/PROJECT_SCOPE.md` first. Keep `map/CONTEXT.md` as the catalog of objects, status (`live`, `leftover`, `ghost`, or `missing`), source of truth, real data movement, and first-order change impact. Do not duplicate the project scope or rewrite graphify output by hand.

Before changing the map, inventory the relevant files and classify them as catalog, contract, factory/reference, product/output, or dead. Do not move or delete project files during a mapping pass. Verify claims against source files, cite paths, and mark uncertain or missing pieces explicitly. Preserve distinctions between documented configuration and verified runtime state.

If the system map grows beyond a single useful catalog, follow [the system-map method](references/system-map.md) and add only real object cards, processes, and impact routes. Keep each folder's `CONTEXT.md` explicit about inputs, process, outputs, and human review. Use numbered folders only for stages with a real order. Keep stable templates separate from experiment outputs.

## Graphify relationship

Use the `graphify` skill when the task asks for code relationships or when Python source changes make the extracted graph stale. For this repository, graphify's current scan covers only `google_boutique/extract_telemetry.py`; do not describe it as covering papers, cluster state, or the whole research process. After graphify runs, update this map only when its verified source-backed findings change the project catalog or impact routes.

## Walk test

- From root `AGENTS.md`, an agent can reach this skill, the map, and graphify report quickly.
- A cold reader can identify what is implemented, proposed, missing, or invalid from `map/CONTEXT.md` plus one cited source.
- Every claim about runtime behavior points to evidence; intended README behavior is not deployment evidence.
- Any new map artifact names its inputs, process, outputs, and human check.
- Links resolve, and no stable fact is copied into multiple documents without a canonical home.

## Upstream source

This project-local skill is based on [RinDig/icm-architect](https://github.com/RinDig/icm-architect/blob/main/SKILL.md). Review upstream when revising this local copy.
