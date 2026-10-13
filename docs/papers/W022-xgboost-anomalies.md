---
kind: paper-note
study_id: W022
source_pdf: "Bibliografia_Micro/Classification_of_Anomalies_in_Microservices_Using_an_XGBoost-Based_Approach_With_Data_Balancing_and_Hyperparameter_Tuning.pdf"
source_sha256: e96cd7ca82c7e04c7491babece919283ab1d15d6617c5eb19fcd61677b64d8e3
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [4, 5, 6, 7, 8, 9]
research_task: detection
status: work-complete-awaiting-review
---

# Classification of Anomalies in Microservices Using an XGBoost-Based Approach With Data Balancing and Hyperparameter Tuning

**Citation:** Luís M. Barata et al.; 2025; IEEE Open Journal of the Computer Society; 10.1109/OJCS.2025.3622532. **Source:** [original PDF](<../../Bibliografia_Micro/Classification_of_Anomalies_in_Microservices_Using_an_XGBoost-Based_Approach_With_Data_Balancing_and_Hyperparameter_Tuning.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

TraceRCA trace-latency anomaly classification; no positive forecast history/lead/horizon is established. Extreme latency is labeled using mean+3 standard deviations, approximately 494.520 ms, on a full dataset of 85,561,389 traces (pp. 6–7).

## Data and method

ADMXGB combines cleaning/scaling, thresholding, SMOTE/undersampling/SMOTEENN and XGBoost tuning by grid, random search or Hyperopt; ten-fold training CV selects F1 (pp. 4–5, 7). Baselines include LightGBM, XGBoost, autoencoders, Isolation Forest, decision trees and Gaussian Naive Bayes (p. 9). Labels are latency-derived; independent service-failure episode counts are unknown.

## Evaluation and limits

Algorithm 2 specifies train/validation/test 70/20/10 and ten-fold training CV, with final fitting on train+validation. Its prose says test is protected from filtering/balancing, but also says Algorithm 2 receives data already scaled/balanced by Algorithm 1. Order/fit scope is therefore ambiguous; chronology and episode grouping are unknown (p. 5). The reported maximum F1 99.97% belongs to this classification/tuning setting (p. 9), not a service forecast. No reproduction.

## Relevance here

Supports a newly trained tabular baseline family. Transfer inference: fit resampling/scaling and label thresholds in training folds and preserve deployment class prevalence in evaluation. A contemporaneous latency feature may reveal its own latency-derived label; predecision availability needs explicit audit.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
