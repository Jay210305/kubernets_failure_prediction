---
kind: paper-note
study_id: W068
source_pdf: "Bibliografia_Micro/To Split or to Merge Exploring Multi-modal Data Flexibly for Failure Classification in Microservices.pdf"
source_sha256: e058bfa06bc3a910072862be46b03fd80261e259b2c5bd0c085ceb68a78c1280
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [4, 5, 8, 9, 10]
research_task: detection
status: work-complete-awaiting-review
---

# To Split or to Merge? Exploring Multi-modal Data Flexibly for Failure Classification in Microservices

**Citation:** Xiuhong Tan et al.; 2025; Internetware 2025; 10.1145/3755881.3755891. **Source:** [original PDF](<../../Bibliografia_Micro/To%20Split%20or%20to%20Merge%20Exploring%20Multi-modal%20Data%20Flexibly%20for%20Failure%20Classification%20in%20Microservices.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Failure-type classification from logs/metrics/traces around an existing failure. Observation window w is associated with failure time t; it does not establish positive advance service lead/horizon (p. 5). Hardware/software/network categories may be refined according to available labels.

## Data and method

AgileMFC uses Transformer expert representations with modality/shared gates and a classifier (pp. 8–10). GAIA has ten instances/five injected types; TrainTicket 27 active instances/three types and SocialNetwork twelve/three types. Table 2 counts raw modality observations, not independent episodes (p. 8). Cloud19, LogCluster, CloudRCA and DiagFusion are baselines; experiments repeat five times (p. 8).

## Evaluation and limits

Earlier data train and later data test by temporal precedence; exact ratios, episode separation and purge are unknown at this depth (p. 8). Weighted F1 is .939 GAIA, .728 TrainTicket and .701 SocialNetwork (p. 9); these are failure classification results. Modality weights and dataset size affect transfer; ablations vary gates, CNN features and classifiers (pp. 9–10). No reproduction.

## Relevance here

Keep root fault type, affected instances and observed service outcome separate in episode logs. Transfer inference: modality ablations may test useful context, but metrics-first CNN–LSTM remains primary. Raw record totals cannot justify episode-level confidence intervals.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
