---
kind: paper-note
study_id: W056
source_pdf: "Bibliografia_Micro/Performance prediction and resource adaptive adjustment for cloud-native microservices.pdf"
source_sha256: 9801085becf602481237bd434ba5cc07285e8c4ef7899a0f78e992d66b935757
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [4, 5, 6, 7, 8, 13, 14, 17]
research_task: other
status: work-complete-awaiting-review
---

# Performance prediction and resource adaptive adjustment for cloud-native microservices

**Citation:** Yu Peng et al.; 2025; Cluster Computing; 10.1007/s10586-025-05437-3. **Source:** [original PDF](<../../Bibliografia_Micro/Performance%20prediction%20and%20resource%20adaptive%20adjustment%20for%20cloud-native%20microservices.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

CNNRPM predicts response-time/performance under a resource allocation; DDPG adjusts resources. It does not define a future binary service-failure event with positive lead/horizon (pp. 8, 13, 17).

## Data and method

DeathStarBench on two physical hosts with Docker/Ubuntu/WSL2. vmstat resource features and Cgroups allocation settings pair with Jaeger response time/topology; CPU, I/O and tmpfs-memory interference supply measurements (pp. 5–6, 13). Critical paths guide resource decisions. Tabular resource/allocation samples become grayscale images with a chosen feature layout, then CNN input (pp. 6–8). Sample counts and temporal history are not extracted.

FIRM, VIME, Scarf, decision tree, XGBoost, RF and Naive Bayes appear in performance comparisons; DDPG policy comparisons concern resource allocation (pp. 13–14, 17).

## Evaluation and limits

Accuracy/precision/recall/F1 are reported for the performance task; precise response-time label binning and chronological episode split are unknown at this focused depth (p. 14). Resource savings trade against response time; DDPG is not always the best response-time policy (p. 17). No numeric forecast result or reproduction is asserted.

## Relevance here

A CNN's tabular/image layout must be justified; placing values next to each other does not establish service topology. Transfer inference: test service-order sensitivity and compare temporal-only/tabular models on this project's own forecast labels. Resource control remains outside current scope.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
