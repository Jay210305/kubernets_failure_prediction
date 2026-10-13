---
kind: paper-note
study_id: W033
source_pdf: "Bibliografia_Micro/InstantOps_ A Joint Approach to System Failure Prediction and Root Cause Identification in Microservices Cloud-Native.pdf"
source_sha256: 758f2c9ef0f68b883ae76a390aad905cc2239a60b448d0c443e3e8d3e21734d0
reviewed_on: 2026-10-10
review_depth: full
reviewed_pages: [1, 4, 5, 6, 7, 8, 9, 10]
research_task: prediction
status: work-complete-awaiting-review
---

# InstantOps: A Joint Approach to System Failure Prediction and Root Cause Identification in Microservices Cloud-Native Applications

**Citation:** Raphael Rouf et al.; 2024; ICPE '24; 10.1145/3629526.3645047. **Source:** [original PDF](<../../Bibliografia_Micro/InstantOps_%20A%20Joint%20Approach%20to%20System%20Failure%20Prediction%20and%20Root%20Cause%20Identification%20in%20Microservices%20Cloud-Native.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** full decision review of target, methods, evaluation and limits; references/appendices not exhaustively audited. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

System-level failure in the next time bin t+1; nodes represent services, but the forecast target is the application. Per-minute aggregation is described on pp. 4, 7–8. Fixed observation-history length and a strictly positive minimum warning interval are unknown; example lags t−2 and t−5 do not fix a history length (p. 8). Root-cause ranking is a separate output (pp. 8–10).

The failure definition changes within the PDF: p. 4 says application crash or over 99% HTTP 500 responses; p. 8 uses 99.9% error responses, such as 503, during one minute. Preserve both definitions as an unresolved protocol inconsistency.

## Data and method

GNN/GCN plus GRU learns service interactions and time dependence. Traces provide caller/callee relations; edges reflect interaction counts, while the GCN description also uses a binary adjacency (pp. 4–6). Logs, CPU/memory, disk/network I/O, request status/latency and Kubernetes events are inputs (p. 6, Table 1).

MicroSS/GAIA has ten services, two databases and five hosts with annotated injected system/service faults. TrainTicket has 41 services and injected/code/resource/network faults. QoTD has eight services on OpenShift with Chaos Mesh CPU, memory and DNS faults; Instana, LogDNA and a minute-level event script collect observations (p. 7). Table 2 reports 419,959 MicroSS, 24,492 TrainTicket and 450,000 QoTD samples; independent episode counts are unknown (p. 8).

Neural comparisons are GNN+LSTM, GNN, GTN, GTN+LSTM and GTN+GRU. JLT combines JumpStarter, LogAnomaly and TraceAnomaly; AnoFusion is another multimodal detection comparator (pp. 8–9). Detection comparator scores do not establish an identical advance-warning protocol.

## Evaluation and limits

Table 2 explicitly labels train/test counts as 84,026/335,933 for MicroSS, 5,085/19,337 for TrainTicket and 90,000/360,000 for QoTD. This is approximately 20% training and 80% testing as printed, not the reverse. Chronology, episode grouping and window purge are unknown (p. 8; table visually checked).

Table 3 reports forecast F1 of .98 MicroSS, .98 TrainTicket and .96 QoTD (p. 9; visually checked). The abstract instead reports .97 for TrainTicket (p. 1). Localization tables measure ranks/top-k accuracy, not forecast lead time; prose and Table 5 also disagree on some application ranks (p. 9). Scaling is described over all data points without establishing training-only fitting (p. 4). Labeling, minute granularity and benchmark scale limit transfer (p. 10). No project reproduction or verified operational false-alert/first-alert distribution exists.

## Relevance here

Closest reviewed spatiotemporal forecast comparison, but its system target, multimodal inputs and unresolved SLA/split details prevent importing its score as a service-forecast benchmark. Transfer inference: audit Kubernetes/status features for availability before decision time, and require matched targets/splits for a graph baseline. Evaluate the selected CNN–LSTM under the project contract; this note does not replace it.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
