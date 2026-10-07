---
name: review-paper
description: Use when adding or revising evidence from a PDF in this project's Bibliografia_Micro corpus for the microservice failure-prediction study.
---

# Review a research paper

Read `docs/PROJECT_SCOPE.md` and `docs/LITERATURE_MAP.md` only as needed to understand the current research question. Open the named PDF itself. Start with abstract and conclusion, then inspect methods, data, and evaluation before making claims about results or transferability.

Copy `docs/_templates/paper-note.md` into a clearly named note under `docs/papers/` when a durable review is requested. Keep the original PDF path and page numbers for each substantive claim. Mark review depth accurately. Classify the paper's task as advance prediction, current anomaly detection, fault localization, mitigation, or another category; keep target unit and time horizon explicit.

Record dataset and fault provenance, modalities, model, comparison methods, split strategy, metrics, and limitations. If any are absent or unread, say so. Separate the paper's reported results from what this project has reproduced. Update `docs/LITERATURE_MAP.md` with a brief link to the note, avoiding a second copy of its details.
