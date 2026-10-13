---
kind: paper-note
study_id: W064
source_pdf: "Bibliografia_Micro/ServiceAnomaly_ An anomaly detection approach in microservices using distributed traces and profiling metrics.pdf"
source_sha256: 37a7e968c715f4a051ddc068e995cab1ce23ff3e728f33ad047ffff3ec484a9e
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [4, 6, 8, 9, 10, 12, 13, 14, 17]
research_task: detection
status: work-complete-awaiting-review
---

# ServiceAnomaly: An anomaly detection approach in microservices using distributed traces and profiling metrics

**Citation:** Mahsa Panahandeh et al.; 2024; The Journal of Systems and Software; 10.1016/j.jss.2023.111917. **Source:** [original PDF](<../../Bibliografia_Micro/ServiceAnomaly_%20An%20anomaly%20detection%20approach%20in%20microservices%20using%20distributed%20traces%20and%20profiling%20metrics.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Current anomaly detection from trace paths and profiling metrics; no future forecast lead/horizon is established (pp. 4, 8–10). Observation units combine paths and service relationships.

## Data and method

Context Propagation Graph unions normal trace trees into a DAG; edges follow span parent/child-of/follows-from relations. The same logical service can be distinguished by path context. Duration, request/response sizes, queue time, latency and throughput annotate relationships; correlation/NMI and SVR model metric dependence (pp. 4, 6, 8–10).

TeaStore has six services; TrainTicket has 32 logical services plus 24 database pods. Load-test normal traces establish a reference, with host CPU/disk and service delay/HTTP/timeout/hang faults in evaluation. TeaStore has over 3,000 traces/9,160 metric rows; TrainTicket over 5,000/5,410 (pp. 12–13).

## Evaluation and limits

Normal reference plus fault-test design; precise chronology/purge is unknown at this focused depth. Reported detection F1 reaches 85% TeaStore and 86% TrainTicket; evaluated anomalous trace sets are small (15/32 respectively, p. 14). Missing paths may hide faults (p. 17). Baseline configurations and independent episode counts are not fully extracted in this focused graph review. No reproduction.

## Relevance here

Trace-derived caller/callee edges are a plausible Boutique topology source, conditional on actual trace coverage and stable service identity. Preserve full graph and any derived DAG separately; path duplication affects node meaning. Detection F1 is not a forecast comparator score.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
