---
kind: paper-note
study_id: W019
source_pdf: "Bibliografia_Micro/Can We Trust Auto-Mitigation_ Improving Cloud Failure Prediction with Uncertain Positive Learning.pdf"
source_sha256: 658d8709431a800d4b0bb1d41bad19791d4d52cf3368ba96d6c8909be5580abd
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [1, 3, 6, 8, 10]
research_task: prediction
status: work-complete-awaiting-review
---

# Can We Trust Auto-Mitigation? Improving Cloud Failure Prediction with Uncertain Positive Learning

**Citation:** Haozhe Li et al.; Unknown; Unknown; Unknown. **Source:** [original PDF](<../../Bibliografia_Micro/Can%20We%20Trust%20Auto-Mitigation_%20Improving%20Cloud%20Failure%20Prediction%20with%20Uncertain%20Positive%20Learning.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Disk/node failure prediction under automatic mitigation, with uncertain positive outcomes when intervention prevents observing a failure. Hardware/node unit, not service availability. Numeric history and lead/horizon are not extracted in this focused label review (pp. 1, 3). Publication year/venue remain unknown; file creation time is not a publication date.

## Data and method

Alibaba/Backblaze disks and industrial Azure node data; SMART, node metrics/counters and events (pp. 3, 6). UPTAKE modifies risk/loss for uncertain positives using a positive prior derived from validation precision. RNN, LSTM, Transformer and TCNN are base models (p. 6). Complete sample/episode totals are not extracted here.

## Evaluation and limits

Sequential updating stages compare an offline ground-truth oracle and online updating using only certain labels; validation F1 selects checkpoints (p. 6). Precision/recall/F1 evaluate prediction; node deployment and prior sensitivity are discussed (pp. 8, 10). Exact split ratios, purge and numeric gains are not extracted; no reproduction. The oracle uses labels unavailable after real mitigation.

## Relevance here

Transfer inference: preserve intervention time and censored/unknown outcomes rather than labeling every averted incident healthy. This becomes relevant if future Boutique experiments intervene automatically; UPTAKE is not yet required by a passive forecast experiment.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
