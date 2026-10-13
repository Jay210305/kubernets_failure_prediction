---
kind: paper-note
study_id: W004
source_pdf: "Bibliografia_Micro/A Survey of AIOps Methods for Failure Management.pdf"
source_sha256: 7ba221f5cfa77d459f8f269967efa3e84b0069ad940e782f4064848ebdced2c2
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [1, 8, 9, 17, 22, 28, 34]
research_task: survey
status: work-complete-awaiting-review
---

# A Survey of AIOps Methods for Failure Management

**Citation:** Paolo Notaro et al.; 2021; ACM Transactions on Intelligent Systems and Technology; 10.1145/3483424. **Source:** [original PDF](<../../Bibliografia_Micro/A%20Survey%20of%20AIOps%20Methods%20for%20Failure%20Management.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Failure management taxonomy: prevention/prediction are proactive; detection, root-cause analysis and remediation are reactive according to intervention time (p. 9). Lead time is event time minus prediction time; warning time must fit inside available lead for action (p. 17). The survey does not choose this project's history or horizon.

## Data and method

Reviews 100 failure-management solutions with five categories and fourteen subcategories (p. 1). Prediction timing, detection, fault localization/diagnosis and remediation are treated separately (pp. 17, 22, 28, 34). It is secondary evidence, without one shared dataset, label source or predictive split.

## Evaluation and limits

Precision/FPR depend on operating point and different denominators (p. 8); component localization and causal diagnosis differ (p. 28). Numeric cross-study results cannot become a paired forecast comparison. Independent episode totals, a unified baseline and service lead distribution are not applicable. No reproduction.

## Relevance here

Use the taxonomy to label the literature and to define a useful operational warning interval in Phase 03. Transfer inference: select minimum lead from the response action and evaluate first alerts before onset. Detection/localization and mitigation remain separate tasks.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
