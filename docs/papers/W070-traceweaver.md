---
kind: paper-note
study_id: W070
source_pdf: "Bibliografia_Micro/TraceWeaver_ Distributed Request Tracing for Microservices Without Application Modification.pdf"
source_sha256: 72bb9eaadf5abdd2fad442b90ee9355d8ac6b4d6717c7eb0836f6edbb7f82a73
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [6, 9, 10, 11]
research_task: other
status: work-complete-awaiting-review
---

# TraceWeaver: Distributed Request Tracing for Microservices Without Application Modification

**Citation:** Sachin Ashok et al.; 2024; ACM SIGCOMM '24; 10.1145/3651890.3672254. **Source:** [original PDF](<../../Bibliografia_Micro/TraceWeaver_%20Distributed%20Request%20Tracing%20for%20Microservices%20Without%20Application%20Modification.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Reconstructs distributed request traces without application modification; output is request paths/spans, not future failure risk. Forecast history/lead/horizon are not applicable (pp. 6, 9).

## Data and method

eBPF syscall timestamps, caller/callee observations and constrained timing/GMM optimization match spans. Call graph and dependency order are supplied by operators or learned with isolated test requests and artificial network delays; application changes require refreshing them (pp. 6, 9). gRPC/HPACK state and unencrypted traffic assumptions constrain recovery (p. 9).

HotelReservation (six services), Media (14), a Node.js demo (seven) and Alibaba traces are evaluated against Jaeger ground truth and methods including WAP5, vPath/DeepFlow and FCFS (pp. 10–11).

## Evaluation and limits

Load/caching/asynchronous scenarios test trace reconstruction rather than a forecast train/test split (pp. 10–11). Numeric recovery metrics and counts are not extracted in this focused prerequisites review; predictive labels/episodes are not applicable. No reproduction.

## Relevance here

Potential topology source after checking kernel, protocol, encryption and coverage locally. “No application modification” still requires operational assumptions and dependency discovery. Prefer a verifiable trace source already supported by the demo; feasibility is unverified.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
