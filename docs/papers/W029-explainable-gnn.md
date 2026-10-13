---
kind: paper-note
study_id: W029
source_pdf: "Bibliografia_Micro/Explainable_GNN-Based_Approach_to_Fault_Forecasting_in_Cloud_Service_Debugging (1).pdf"
source_sha256: ee37977d54ab3a3d4568765374feb9d7984e2fdcd7323cfb426537c2255c10c6
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [6, 7, 8, 9, 10, 11, 12, 13, 15]
research_task: other
status: work-complete-awaiting-review
---

# Explainable GNN-Based Approach to Fault Forecasting in Cloud Service Debugging

**Citation:** Dániel Unyi et al.; 2025; IEEE Transactions on Network and Service Management; 10.1109/TNSM.2025.3602223. **Source:** [original PDF](<../../Bibliografia_Micro/Explainable_GNN-Based_Approach_to_Fault_Forecasting_in_Cloud_Service_Debugging%20%281%29.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Graph-level regression of simulated system disruption probability, rather than telemetry forecasting for a future named-service event. PRISM evaluates Pmax=?[F<T Rfailure]; T is simulation steps, not an observed wall-clock warning interval (pp. 6–8). No telemetry observation history or service warning lead is established.

## Data and method

Directed service meshes forward requests; leaf failure probabilities and intermediate retry counts parameterize probabilistic automata. PRISM supplies labels. Two node-feature channels contain failure probability and retries, with zeros for inapplicable nodes. Four message-passing blocks (32 hidden units), global mean pooling and a linear readout predict probability (pp. 6–8).

Tree cases use 50 topologies with 50 parameter variants each; DAG cases use ten topologies with ten variants, with 25 REST nodes in the described experiments (p. 11). These cases are simulations, not observed fault episodes. Linear regression and MLP, with/without spectral features, are baselines (pp. 12–13). Explanation masks identify influential simulated nodes (p. 9).

## Evaluation and limits

Random 80/10/10 train/validation/test service-mesh split; MSE selects the best validation checkpoint, 200 epochs and batch size 32 (p. 8). Experiments have three runs (p. 10). Reported tree MAE is .009±.001, R² .992±.005; DAG MAE .009±.002, R² .996±.003. A DAG-trained model tested on trees reports MAE .038±.006 and R² .938±.014 (pp. 11–12).

Whether parameter variants of the same topology are grouped across splits is unknown. This limits interpretation as unseen-topology generalization; it is not proof of actual leakage. Sparse informative leaves challenge explanations (p. 15). Focused review of model, simulation and evaluation; no reproduction.

## Relevance here

Supports an explicit directed graph representation and testing generalization to different graphs. Transfer inference: preserve the actual Boutique graph and compare spatial assumptions. Simulation probability MAE cannot serve as a benchmark for lead-time failure alerts. This note uses the published edition; the corpus index groups the other same-DOI manuscript as an edition of this work.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
