---
kind: paper-note
study_id: W045
source_pdf: "Bibliografia_Micro/MicroFI_Non-Intrusive_and_Prioritized_Request-Level_Fault_Injection_for_Microservice_Applications.pdf"
source_sha256: eb942dd5f184dc5a623544af2fde1f436b9b235f3a55708f2c76b7e18bb28b17
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [5, 6, 10, 11, 15, 16, 17]
research_task: other
status: work-complete-awaiting-review
---

# MicroFI: Non-Intrusive and Prioritized Request-Level Fault Injection for Microservice Applications

**Citation:** Hongyang Chen et al.; 2024; IEEE Transactions on Dependable and Secure Computing; 10.1109/TDSC.2024.3363902. **Source:** [original PDF](<../../Bibliografia_Micro/MicroFI_Non-Intrusive_and_Prioritized_Request-Level_Fault_Injection_for_Microservice_Applications.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Request-level fault injection and resilience testing, not a predictive model. Selected requests/business functions define blast radius; forecast history/lead/horizon and predictive split are not applicable (pp. 5–6).

## Data and method

Traces yield API call graphs; logical fault solutions and prioritization select request faults (p. 5). Python/Kubernetes/Istio/Z3 implementation uses an OpenTelemetry/OpenTracing request marker, request-matching attributes and Istio Delay/Abort recipes with probability and HTTP status (p. 10). Jaeger/Elasticsearch stores traces (p. 11).

HotelReservation, HipsterShop and TrainTicket, with one to three replicas, compare service-level ChaosBlade, API-level Istio and request-level Gremlin/3MileBeach across nine blast-radius groups (p. 11). Testing outcomes are failed business functions and injection efficiency; independent forecast episodes/labels are not supplied (p. 15).

## Evaluation and limits

Prioritization compares R-rules and IntelliFT*; overhead measurements use three-minute intervals repeated five times (pp. 15–16). Numeric overhead is not extracted here. Delay/Abort support does not determine resource-exhaustion intensity; environment/standard adaptation is required (p. 17). No forecast metric or reproduction.

## Relevance here

Transfer inference: log recipe, matched request, injector start/end, workload, affected service and observed outcome separately. Injection onset is not service-failure onset. Boutique compatibility depends on its installed mesh/instrumentation, which is unverified; do not deploy this tool as a side effect of review.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
