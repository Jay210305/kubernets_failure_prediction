---
kind: paper-note
study_id: W059
source_pdf: "Bibliografia_Micro/Resilient Microservice Applications, by Design, and without the Chaos.pdf"
source_sha256: 121a8645b60409d1427628980a4084d0d3fa949632c60347a54438531c97fa3a
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [9, 10, 11, 12, 78, 80, 173]
research_task: other
status: work-complete-awaiting-review
---

# Resilient Microservice Applications, by Design, and without the Chaos

**Citation:** Christopher S. Meiklejohn; 2024; Carnegie Mellon University doctoral thesis; Unknown. **Source:** [original PDF](<../../Bibliografia_Micro/Resilient%20Microservice%20Applications%2C%20by%20Design%2C%20and%20without%20the%20Chaos.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Service-level Fault Injection Testing (SFIT) finds resilience bugs during development using functional tests; it is not online forecasting. Lead/history/horizon and predictive splits are not applicable (pp. 78, 80, 173). This is a focused chapter review, not a full review of the 213-page thesis.

## Data and method

A fault configuration maps RPC signatures/payloads to fault specifications. SFIT begins with a fault-free reference execution, records concrete executions with Distributed Execution Indexes, and schedules/reexecutes abstract fault cases until the configured failure space is exhausted (pp. 78–80). Contents route to corpus and industrial Foodly evaluations (pp. 9–12); their numeric results are not extracted here.

## Evaluation and limits

Coverage is relative to supplied tests and fault configuration, not all possible production failures. The conclusion reports development-time industrial resilience findings (p. 173). ML labels, benchmark scores, split ratios and forecast episode counts are not applicable/not extracted. No reproduction.

## Relevance here

Transfer inference: retain deterministic request/test identity, a normal control and a fault recipe for each episode. Controlled test outcomes need a separate operational service-failure definition to become forecast labels. Do not claim exhaustive real-world fault coverage.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
