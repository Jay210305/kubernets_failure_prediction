---
kind: paper-note
study_id: W049
source_pdf: "Bibliografia_Micro/Multilayered_Fault_Detection_and_Localization_With_Transformer_for_Microservice_Systems.pdf"
source_sha256: cb062f3e70cb6e05e537e79dcc51f4b6039b623f7ca5951379f81bb9552e86e4
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [4, 5, 9, 10, 13]
research_task: detection
status: work-complete-awaiting-review
---

# Multilayered Fault Detection and Localization With Transformer for Microservice Systems

**Citation:** Jingyu Wang et al.; 2024; IEEE Transactions on Reliability; 10.1109/TR.2024.3356717. **Source:** [original PDF](<../../Bibliografia_Micro/Multilayered_Fault_Detection_and_Localization_With_Transformer_for_Microservice_Systems.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

TAD reconstructs current container metrics; traces and metric rankings localize service/resource causes. Separate container anomaly, service cause and host/metric outcomes; no future service lead/horizon is established (pp. 4–5). Default window length is five observations, not five minutes (p. 10).

## Data and method

Temporal attention and container attention encode dependencies; BFS/KDE trace latency processing and multifactor metric ranking localize causes (pp. 4–5, 10). SMD spans five weeks; AIOps2020 has 81 anomalous cases over 22 days with five-minute injections. SockShop on three-node Kubernetes has 102 five-minute faults, minimum 30-minute separation, over seven days, with Locust/ChaosBlade/Prometheus (p. 9).

## Evaluation and limits

Training min/max normalize inputs explicitly (p. 10). Exact chronological/episode split is not extracted in this focused layer review. Detection metrics: precision, recall, F1, ROC-AUC and AP; localization: PR@k/MAP/F1. MicroRCA/MonitorRank are localization comparisons; classic and temporal models form detection comparisons (pp. 9–10). Granger's linear/no-hidden-variable assumptions limit the causal score (p. 13). Numeric table results are not imported; no reproduction.

## Relevance here

Record pod→service→host placement and distinguish observation from target layer. Attention across containers is a spatial hypothesis, not validation of a CNN service grid. Training-only scaling is directly supported; lead-time evaluation still needs the project's own protocol.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
