---
kind: paper-note
study_id: W001
source_pdf: "Bibliografia_Micro/A failure analysis framework to provide pure anomalous data using multi-source data of fault-sensitive microservices.pdf"
source_sha256: 055ad7ac81ff5db6025cc3035f2ad8907dbc8b6379963a148aef12296c967bdf
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [4, 5, 6, 8, 10, 11, 15]
research_task: detection
status: work-complete-awaiting-review
---

# A failure analysis framework to provide pure anomalous data using multi-source data of fault-sensitive microservices

**Citation:** Nan Fu et al.; 2025; The Journal of Systems and Software; 10.1016/j.jss.2025.112513. **Source:** [original PDF](<../../Bibliografia_Micro/A%20failure%20analysis%20framework%20to%20provide%20pure%20anomalous%20data%20using%20multi-source%20data%20of%20fault-sensitive%20microservices.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Current anomalous-data identification using fault-sensitive services; Transformer reconstruction alarms are detection, with no positive forecast lead/horizon established (pp. 4, 8).

## Data and method

Normal traces provide a call graph converted to a tree; the paper removes a frontend→shipping edge when a deeper frontend→checkout→shipping route exists (p. 5). Leaf nodes and cycle participants inform selection, but traces miss shared-storage interactions (p. 6). Metrics/traces align at minute timestamps into a time×service×feature tensor (p. 8).

Online Boutique has eleven services (ten targets excluding load generator); TrainTicket 41, on four cloud servers. Jaeger/cAdvisor/Istio collect observations; Chaos Mesh and HypnoFailpoint produce three-minute faults (p. 10). Independent episode totals are not extracted here.

## Evaluation and limits

Train/validation/test 7:1:2, with chronology and episode independence unknown (p. 10). Reported precision/recall/FPR are 97.16/97.85/3.10% Boutique and 85.17/80.54/8.78% TrainTicket (p. 11). Training noise and reconstruction threshold calibration matter (p. 15). TraceAnomaly appears among comparisons; complete baseline configuration is not extracted in this focused review. No reproduction.

## Relevance here

Transfer inference: retain original graph alongside any derived ordering/tree, and test feature/service selection inside training folds. Its minute resolution and ten-target choice do not automatically match this extractor's five-second/eleven-service schema. Forecast gains remain untested.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
