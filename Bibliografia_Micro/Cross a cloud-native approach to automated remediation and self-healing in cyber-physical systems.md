Johnphill et al. Cybersecurity (2026) 9:124 Cybersecurity
https://doi.org/10.1186/s42400-026-00549-8
RESEARCH Open Access
Cross: a cloud-native approach to automated
remediation and self-healing in cyber-physical
systems
Obinna Johnphill1, Ali Safaa Sadiq1* , Omprakash Kaiwartya1 and Mohammed Adam Taheir2
Abstract
Cyber-Physical Systems (CPS) operate in increasingly complex and security-critical environments where system
faults, misconfigurations, and cyberattacks can compromise safety, availability, and operational integrity. This paper
presents CROSS (Cross-platform Remediation and Observability Self-Healing System), a cloud-native, cross-platform
approach that extends the self-healing paradigm beyond anomaly detection to encompass autonomous, security-
aware remediation. Building upon the Log Intelligence and Self-Healing System (LISH) (Johnphill et al. 2023a), which
utilised CountVectorizer and Multinomial Naive Bayes (MNB) for log-based anomaly classification, CROSS introduces
a policy-driven remediation layer that executes context-specific recovery actions such as service restarts, system
updates, device reboots, and configuration enforcement across Android, Linux, macOS, and Windows. Prometheus-
based observability (Pai and Srinivas 2024) provides fine-grained telemetry on anomalies and remedial actions, ena-
bling continuous monitoring, auditability, and adaptive security governance. Experimental evaluation demonstrates
measurable reductions in mean time to recovery (MTTR) and improvements in anomaly containment and resilience
across heterogeneous CPS environments.
Although CROSS includes mechanisms that are applicable to cybersecurity scenarios, the present evaluation
focuses on operational anomalies rather than explicit attack-induced behaviours. Accordingly, its cybersecurity
relevance is framed as an architectural capability, with empirical security benchmarking identified as future
work. The proposed approach bridges the gap between anomaly detection and active cyber defence, embedding
explainable, automated remediation within the operational lifecycle of CPS.
Keywords Cyber-physical systems, Self-healing, Remediation, Anomaly detection, System resilience, Observability,
Cloud-native systems
Introduction
Cyber-Physical Systems (CPS) underpin critical national
infrastructure across sectors such as healthcare, trans-
portation, energy, and manufacturing. As these systems
become more interconnected and software-dependent,
*Correspondence: they inherit a growing range of vulnerabilities that expose
Ali Safaa Sadiq them to both accidental faults and deliberate cyberat-
ali.sadiq@ntu.ac.uk
1 Cyber Security Research Group (CSRG), Department of Computer tacks (Johnphill et al. 2023a; Loh and Thing 2023). The
Science, Nottingham Trent University, Clifton Lane, Nottingham NG11 convergence of operational technology (OT) and infor-
8NS, UK mation technology (IT) has expanded the attack surface,
2 Faculty of Technology Sciences, Zalingei University, Zalingei, Sudan
allowing misconfigurations or malware to cascade across
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this
licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

Johnphill et al. Cybersecurity (2026) 9:124 Page 2 of 24
interdependent subsystems, compromising safety and the framework with modern DevSecOps monitoring
availability. standards.
Traditional fault-tolerance mechanisms restore func- Although this study uses general-purpose operat-
tionality after benign faults but are often inadequate ing systems as representative CPS platforms, the archi-
against security-induced anomalies. Hence, the ability tecture and methodology are transferable to industrial
to autonomously detect, diagnose, and respond to inci- CPS contexts. The operating-system layer in controllers,
dents is essential for maintaining resilient CPS. Advances embedded devices, and production networks exhibits
in artificial intelligence (AI) and machine learning (ML) comparable behavioural patterns and failure signatures,
now enable adaptive fault management capable of oper- making OS-level anomaly classification a scalable proxy
ating with minimal human intervention (Cheng et al. for CPS-level diagnostics. CROSS therefore bridges con-
2023). These techniques allow CPS to identify deviations ventional IT observability with OT resilience, offering
from normal behaviour, classify anomalies, and initiate a unified pathway toward autonomous, cross-domain
corrective actions that preserve operational continuity self-healing.
even under hostile conditions. This research addresses two key questions: (1) Can
Self-healing systems have emerged as a promising para- a cross-platform self-healing system autonomously
digm for autonomously mitigating both technical faults detect and remediate both operational and security-
and security breaches. A self-healing CPS continuously related faults in real time using only preprocessed log
monitors operational telemetry, detects anomalies, and data? (2) How effectively can remediation be executed
performs automated recovery to maintain service qual- across heterogeneous environments under constraints
ity. However, many existing approaches employ static, such as missing tooling, sandboxed processes, or limited
pre-defined responses that are insufficient for dynamic, connectivity?
multi-platform environments (Vervaet 2021; Naqvi et al. From these, two hypotheses are proposed: (H1) A log-
2022). This rigidity limits responsiveness during unex- driven self-healing system can autonomously execute
pected faults or cyber incidents, highlighting the need OS-specific corrective actions with minimal human over-
for flexible, intelligent remediation strategies that operate sight while maintaining secure operational continuity.
seamlessly across diverse operating contexts. (H2) Platform-specific limitations (for example, unavail-
Recent developments in cloud computing, edge intelli- able systemd, PowerShell, or ADB) can be mitigated
gence, and container orchestration now make it feasible through simulation and fallback mechanisms to sustain
to execute remediation processes at scale. Cloud plat- uninterrupted remediation.
forms enable rapid deployment and telemetry analysis, This paper makes the following contributions:
while edge computing reduces latency by enabling local-
ised decision-making for time-sensitive applications such • CROSS Framework: A cloud-native, cross-platform
as autonomous vehicles and medical devices. By combin- self-healing system integrating log-based anomaly
ing these paradigms, self-healing CPS can detect anom- classification with automated, policy-driven remedia-
alies in near real time and respond promptly through tion.
distributed remediation workflows. This hybrid approach • Cyber-Resilience Orientation: Embeds security
not only improves recovery speed but also enhances awareness and autonomous defence within the reme-
resilience by ensuring isolated compromises do not esca- diation workflow.
late into systemic failures. • Integrated Observability: Provides fine-grained moni-
Building on this foundation, we introduce CROSS, toring and transparency through Prometheus metrics
the Cross-platform Remediation and Observability and Grafana (Siddiqui et al. 2023) dashboards.
Self-Healing System. CROSS extends our previous Log • Adaptive Fallback Logic: Introduces simulated reme-
Intelligence and Self-Healing (LISH) framework, which diation routines for constrained or tool-limited envi-
employed CountVectorizer and Multinomial Naïve Bayes ronments.
(MNB) to classify anomalies from multi-platform sys- • Scientific Evaluation: Demonstrates efficiency across
tem logs. While LISH focused on fault detection, CROSS four operating systems using metrics such as preci-
operationalises the post-detection phase by autono- sion, recall, MTTR, and resource impact.
mously executing platform-specific remedial actions
across Android, Linux, macOS, and Windows environ-
The remainder of this paper is structured as follows:
ments. In addition, CROSS integrates Prometheus-
Sect. 2 reviews recent work on self-healing and resil-
based observability to expose real-time telemetry of
ience in distributed CPS; Sect. 3 presents the CROSS
detected anomalies, remediation events, and system
architecture and operational workflow; Sect. 5
recovery outcomes. This facilitates auditability and aligns

J ohnphill et al. Cybersecurity (2026) 9:124 Page 3 of 24
describes implementation and evaluation; Sect. 6 capabilities including pod restart, health probing,
presents simulation results; Sect. 7 discusses impli- and automated service recovery (Cloud Native 2025).
cations; Sect. 8 concludes and outlines future direc- Shabariram et al. (2024) demonstrated how cloud deploy-
tions. ment strategies such as Blue-Green and Canary models
significantly reduce downtime and enhance reliability in
distributed applications. Similarly, Jhuang and Wu (2022)
Related work
applied Kubernetes load balancing to achieve seamless
Self-healing and resilience strategies have long been IP failover for VoIP services, ensuring high availability in
explored across critical domains such as power distribu- latency-sensitive contexts.
tion, cloud computing, and CPS. Early approaches pre- While these architectures automate recovery at the
dominantly addressed safety and fault tolerance rather infrastructure layer, they do not integrate intelligent
than cybersecurity, focusing on restoring service avail- fault reasoning or log-driven remediation. CROSS builds
ability after physical or software faults. However, with the upon these foundations by linking anomaly classifica-
increasing convergence of operational technology (OT) tion directly to OS-level corrective actions, extending
and information technology (IT), the boundary between traditional DevOps automation toward intelligent cyber
safety faults and cyber-induced anomalies has become resilience.
blurred, necessitating self-healing mechanisms capable of
addressing both. High availability, load balancing, and observability
Several studies have addressed resilience through
Fault tolerance and self‑healing in power and distributed
improved resource distribution and observability.
systems
Nugroho et al. (2023) developed a distributed Round-
In the context of power systems, fault detection and Robin load balancer for automatic proctoring systems,
recovery mechanisms have been well studied. Arefifar achieving a 22% reduction in response time and con-
et al. (2023) proposed a set of control actions, including sistent performance during failover. Malhotra et al.
grid reconfiguration, distributed generation (DG) man- (2023) further evaluated near-zero-downtime solutions
agement, load adjustment, and reactive power control, for enterprise systems, underscoring the importance of
to restore service after grid faults. Subsequent work by redundancy and clustering for service continuity.
Wang et al. (2019) optimised load restoration priori- More recent work has focused on observability and
ties to maximise service continuity under constrained continuous monitoring as complementary to self-healing.
resources. These self-healing control strategies empha- Siddiqui et al. (2023) and Akinbolaji et al. (2024) explored
sise fault isolation and load balancing to maintain reli- the integration of Prometheus and Grafana within
ability in safety-critical systems. DevOps pipelines to improve proactive detection and
Although these studies significantly contributed to response. Pai and Srinivas (2024) demonstrated that inte-
resilience in physical infrastructures, they primarily tar- grating multi-source observability tools enhances fault
get deterministic faults rather than adversarial or data- traceability and reduces mean time to recovery (MTTR).
driven anomalies. The absence of adaptive, data-centric These findings support CROSS’s design choice to embed
recovery approaches limits their effectiveness against Prometheus metrics directly into the remediation work-
cyber disruptions, where malicious interference can flow, enabling real-time feedback, auditing, and adaptive
mimic or exacerbate normal fault patterns. control.
Resilience in cloud‑native and containerised environments Cybersecurity‑oriented self‑healing and anomaly detection
Self-healing in cloud computing environments has Traditional self-healing frameworks often assume faults
evolved through automated failover, load balancing, and are benign. However, the increasing frequency of cyber-
container orchestration. Pakrijauskas and Mazeika (2022) attacks has prompted research into systems that can
examined the availability of stateful microservices during autonomously detect and respond to malicious activ-
failover, highlighting Kubernetes as a key enabler of auto- ity. Cheng et al. (2023) reviewed AI for IT Operations
mated recovery. Load balancing and database resilience (Cheng et al. 2023) (AIOps) and emphasised the role of
mechanisms, such as LABAREDA (Marinho et al. 2018) machine learning in identifying cyber anomalies in cloud
and Hihooi (Georgiou et al. 2019), further improved elas- platforms. Ali et al. (2025) presented an AI-powered
ticity and availability through predictive performance anomaly detection approach for proactive fault diagno-
modelling and replica routing. sis and self-healing, integrating ML-based detection with
Kubernetes has emerged as the de facto standard security-oriented response logic. Loh and Thing (2023)
for container orchestration, with built-in self-healing proposed mechanisms for enhancing CPS resilience

Johnphill et al. Cybersecurity (2026) 9:124 Page 4 of 24
through implicit guarantees against adversarial disrup- handlers: Android uses ADB to clear caches and reboot
tions, reinforcing the importance of combining security devices; Linux systems use package updates and service
and reliability. restarts; macOS performs simulated system updates and
Despite these advancements, few existing solutions service recoveries; Windows executes PowerShell-based
bridge detection and automated remediation in a unified maintenance scripts.
cross-platform system. Most frameworks either focus Metrics such as anomaly counts and remedial events
on predictive monitoring or rely on manual incident are exported to Prometheus and visualised in Grafana.
response. CROSS addresses this gap by coupling light- The system comprises five layers: data acquisition, feature
weight log-based anomaly detection with immediate, engineering, anomaly inference, threshold evaluation,
context-aware remediation actions. This makes it capable and remediation. Core principles include lightweight
of handling both operational faults and potential attack- anomaly detection, cross-platform adaptability, automa-
induced anomalies within a single adaptive architecture. tion through threshold logic, and full observability to
support transparency and auditability.
From LISH to CROSS: motivations for evolution Figure 2 outlines the CROSS workflow. After anomaly
The Log Intelligence and Self-Healing System (LISH) by classification, if error or warning thresholds are breached,
Johnphill et al. (2024) served as the foundation for this the system identifies the OS and selects an appropriate
work. LISH applied the CountVectorizer and MNB to remediation strategy. If the OS is unsupported, execution
classify system logs into normal, warning, and error cat- is gracefully skipped to avoid unnecessary system modifi-
egories across multiple platforms. While it achieved high cation. Supported platforms execute a defined remedia-
recall for anomaly detection, it lacked a mechanism to tion set, including:
execute remediation actions or provide runtime observa-
bility. CROSS extends LISH by introducing a remediation • System updates: Apply OS-specific patches and
layer that maps detected anomalies to platform-specific updates to fix vulnerabilities.
corrective actions, executed automatically via unified • Service restarts: Restart unresponsive services to
handlers. It integrates telemetry using Prometheus and restore normal operations.
Grafana, offering transparency and traceability; key • Disk clean-up: Remove temporary or obsolete files to
requirements for cyber-resilient architectures. recover storage.
By bridging detection and remediation, CROSS trans- • Resource reallocation: Free memory or CPU to opti-
forms passive fault monitoring into active cyber defence. mise responsiveness.
Its design reflects a broader shift in CPS research from
reliability-focused safety assurance toward intelligent, Platform-specific tools such as ADB (Android), sys-
autonomous resilience capable of addressing both faults temctl (Linux), PowerShell (Windows), or simulated
and attacks in real time. shell commands (macOS) are abstracted into an OS
registry, ensuring fault handling remains consistent
Design and operational workflow of the CROSS and explainable across environments. This architecture
framework decouples detection, decision-making, and execution,
promoting adaptive, reproducible, and scalable recovery
To enable intelligent fault tolerance across diverse com-
across cyber-physical systems.
puting platforms, we present CROSS, a unified self-
healing framework that builds upon our previous LISH
Methodology
system. It leverages preprocessed and labelled system
logs for machine learning-driven anomaly detection and This section formalises the methodology used to evaluate
integrates rule-based remediation logic and real-time the CROSS framework, defines key operational seman-
observability. CROSS supports Android, Linux, macOS, tics, and outlines the algorithms, datasets, and experi-
and Windows environments and uses predefined thresh- mental procedures applied to validate its performance
olds for errors and warnings to trigger platform-specific across heterogeneous platforms. The methodology also
actions, offering continuous insight into system health incorporates a cybersecurity dimension by examining
and automated recovery from faults. how CROSS responds to both benign system faults and
Figure 1 illustrates the CROSS architecture. Logs from simulated attack-induced anomalies.
heterogeneous platforms are preprocessed and vector-
ised using CountVectorizer, then classified via an MNB Terminology and formal definitions
model into normal, warning, or error states. Events Error and Warning Semantics. In the context of
exceeding threshold levels trigger the Remediation CROSS, a warning represents a recoverable anomaly,
Action Dispatcher, which maps to OS-specific recovery typically signalling system degradation or pre-fault

J ohnphill et al. Cybersecurity (2026) 9:124 Page 5 of 24
Fig. 1 Architectural overview of the CROSS framework, highlighting modular OS-specific execution paths and threshold-based remediation logic
Fig. 2 Threshold-based remediation workflow in CROSS, showing conditional execution of platform-specific recovery actions

Johnphill et al. Cybersecurity           (2026) 9:124  Page 6 of 24
conditions (for example, high CPU usage, temporary I/O  Evaluation setup and experimental design
delay), whereas an error corresponds to a critical failure  Preprocessed log datasets were obtained from Android,
or potential security violation requiring immediate reme- Linux, macOS, and Windows systems using the LISH
diation. This semantic distinction enables context-aware  preprocessing pipeline. Each log was labelled as nor-
responses  and  helps  prioritise  automated  corrective  mal,  warning,  or  error.  Additionally,  security-
actions. related anomalies, such as unauthorised access attempts,
Anomaly Definition. Let  L ℓ1 ,ℓ2 ,...,ℓn  represent  repeated authentication failures, and abnormal network
|     | ={  |     | }   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
α
a stream of log entries. An anomaly   is defined as any  activity, were injected to simulate cyberattack conditions.
M
entry  ℓi for which the model   estimates a probability  For each platform, the following steps were executed:
δ
| below a detection threshold  | :   |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1. Train the MNB classifier using preprocessed logs.
| P(ℓi M)<δ                                                 |     |     |     |     |            |           |                |     |          |          |
| --------------------------------------------------------- | --- | --- | --- | --- | ---------- | --------- | -------------- | --- | -------- | -------- |
| |                                                         |     |     |     | (1) |            |           |                |     |          |          |
|                                                           |     |     |     |     | 2. Stream  | incoming  | logs  through  |     | CROSS’s  | anomaly  |
| Here,  δ  defines the lower confidence bound distinguish- |     |     |     |     | detector.  |           |                |     |          |          |
3. Accumulate error and warning counts over a sliding
ing expected behaviour from anomalous activity. This
| probabilistic criterion accommodates both operational  |     |     |     |     | window.     |              |          |       |             |      |
| ------------------------------------------------------ | --- | --- | --- | --- | ----------- | ------------ | -------- | ----- | ----------- | ---- |
|                                                        |     |     |     |     | 4. Trigger  | remediation  | actions  | when  | thresholds  | are  |
faults and adversarial events.
breached.
Remediation Thresholds. Let E and W denote the
counts of errors and warnings in a given log window.  5. Record performance metrics and Prometheus telem-
etry.
CROSS triggers a remediation when:
| E >T e | or W >T w |     |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(2) Each experiment was executed ten times per platform to
| T   | T   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where  e  and  w  are  configurable  platform-specific  ensure statistical robustness. Mean values and standard
deviations were computed for recovery time, detection
thresholds. These values were empirically tuned for each
accuracy, and system overhead. Remedial actions were
| operating  system  | during  evaluation  | to  | minimise  | false  |     |     |     |     |     |     |
| ------------------ | ------------------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- |
executed either natively (for example, via systemctl,
positives while ensuring a timely response.
|                  |                |          | t              |     | adb,  or  | PowerShell)  | or  | in  simulated  | mode  | where  |
| ---------------- | -------------- | -------- | -------------- | --- | --------- | ------------ | --- | -------------- | ----- | ------ |
| Recovery  Time.  | The  recovery  | latency  | r  quantifies  |     |           |              |     |                |       |        |
responsiveness from anomaly detection to remediation  native tooling was unavailable.
Observability metrics, including anomaly rates, action
completion:
|       |     |     |     |     | frequencies,  | and  system  | health  | states,  | were  | exposed  |
| ----- | --- | --- | --- | --- | ------------- | ------------ | ------- | -------- | ----- | -------- |
| t t   | t   |     |     |     |               |              |         |          |       |          |
| r res | det |     |     |     |               |              |         |          |       |          |
= − (3) through  Prometheus  and  visualised  with  Grafana  for
| t                                                   |     |     |     | t    | temporal and comparative analysis. |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ---- | ---------------------------------- | --- | --- | --- | --- | --- |
| where  det is the anomaly detection timestamp, and  |     |     |     | res  |                                    |     |     |     |     |     |
t
| marks successful resolution. Lower  |     | r indicates improved  |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
resilience.
Comparative baseline analysis
|     |     |     |     |     | To  contextualise  | CROSS’s  | performance,  |     | two  baselines  |     |
| --- | --- | --- | --- | --- | ------------------ | -------- | ------------- | --- | --------------- | --- |
were implemented:
Feature engineering and model justification
CROSS leverages the CountVectorizer to transform
•  Rule-Based System: A static remediation engine map-
unstructured system logs into sparse bag-of-words repre-
sentations. This choice enables computational efficiency  ping specific log patterns to predefined shell com-
mands.
and high interpretability, essential for explainable self-
•  Manual Script Execution: Conventional administra-
healing systems. The MNB classifier was selected for its
proven robustness, low computational cost, and supe- tor-led corrective actions triggered upon manual log
inspection.
rior recall in log-based anomaly detection (Vervaet 2021;
Ali et al. 2025). In cybersecurity contexts, high recall
ensures that rare or emerging threats are more likely to  Metrics evaluated include precision, recall, Mean
be detected, even at the cost of slightly lower precision.
Time to Recovery (MTTR), CPU/memory overhead,
Alternative classifiers such as Support Vector Machines
|     |     |     |     |     | and  fallback  | activation  | rate.  | CROSS  | achieved  | a   |
| --- | --- | --- | --- | --- | -------------- | ----------- | ------ | ------ | --------- | --- |
(SVM) and Random Forests were evaluated during pre-
mean reduction in mean-time-to-recovery (MTTR)
liminary testing; however, these models exhibited higher
of 37% when compared against the manual script
latency and resource overhead, which made them less  baseline, demonstrating significant improvements in
suitable for real-time self-healing pipelines. MNB there-
recovery efficiency. Importantly, containerised isola-
fore offers an optimal balance between accuracy, speed,
tion ensured minimal system interference.
and explainability.

J ohnphill et al. Cybersecurity           (2026) 9:124  Page 7 of 24
Table 1 Comparative performance analysis of CROSS vs.  As detailed in Table 5, CROSS achieves the lowest
baseline methods mean MTTR (34.1 s) with modest CPU (9.2%) and RAM
| Metric | Manual scripts | Rule‑based CROSS  | (75.4 MB). |     |     |     |
| ------ | -------------- | ----------------- | ---------- | --- | --- | --- |
(proposed)
Remediation as a decision process
| MTTR (seconds) | 89.4 | 54.2 34.1 |     |     |     |     |
| -------------- | ---- | --------- | --- | --- | --- | --- |
The CROSS remediation process can be expressed as a
| Precision | 0.72 | 0.83 0.91 |                                               |     |     | s            |
| --------- | ---- | --------- | --------------------------------------------- | --- | --- | ------------ |
|           |      |           | discrete state–action transition system. Let  |     |     | t represent  |
| Recall    | 0.76 | 0.79 0.94 |                                               |     |     |              |
the system state at time t inferred from log classification.
| CPU Overhead (%)     | 11.3 | 8.7 9.2   |                       | a A                               |     |     |
| -------------------- | ---- | --------- | --------------------- | --------------------------------- | --- | --- |
|                      |      |           | A remediation action  | t  is executed to transition the  |     |     |
| Memory Overhead (MB) | 92.1 | 71.6 75.4 |                       | ∈                                 |     |     |
s t
|     |     |     | system to a new state  | 1:  |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --- |
+
|                                         |     |     | T(s ,a | s   |     |     |
| --------------------------------------- | --- | --- | ------ | --- | --- | --- |
|                                         |     |     | t t)   | t 1 |     |     |
|                                         |     |     | →      |     |     | (4) |
| Table 2 Features of the CROSS framework |     |     |        | +   |     |     |
This abstraction resembles a Markov Decision Process
| Feature | Description |     |                   |                      |                    |     |
| ------- | ----------- | --- | ----------------- | -------------------- | ------------------ | --- |
|         |             |     | (MDP),  allowing  | future  integration  | of  reinforcement  |     |
Log analysis Parses logs to detect anomalies. learning  for  adaptive  remediation.  Although  CROSS
Automated remediation Triggers corrective actions on threshold  currently uses deterministic threshold-based logic, the
breaches.
|     |     |     | MDP  representation  | provides  | a  theoretical  | founda- |
| --- | --- | --- | -------------------- | --------- | --------------- | ------- |
Containerisation Docker-based for reproducible deployment. tion for evolving toward self-learning, context-sensitive
| Cross-platform support | Handlers for Android, Linux, macOS,  |     |     |     |     |     |
| ---------------------- | ------------------------------------ | --- | --- | --- | --- | --- |
healing strategies. The methodological design ensures
and Windows.
reproducibility and balanced evaluation across security,
| Orchestration | Kubernetes-managed fault-tolerant deploy- |     |     |     |     |     |
| ------------- | ----------------------------------------- | --- | --- | --- | --- | --- |
ment. fault tolerance, and performance criteria. By combining
probabilistic detection, threshold-based remediation, and
| Observability | Exports Prometheus metrics, visualised  |     |     |     |     |     |
| ------------- | --------------------------------------- | --- | --- | --- | --- | --- |
multi-platform observability, CROSS offers a rigorous,
in Grafana.
extensible foundation for security-aware self-healing in
CPS.
Table 3 CROSS project file structure Implementation and system integration
The CROSS framework adopts a modular, cross-platform
| File/Directory | Description |     |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- | --- |
design for automating corrective actions across Android,
Core Python remediation logic
self-healing-trigger/ Linux, macOS, and Windows. As shown previously in
| dataset/ | Preprocessed logs for simulation |     |     |     |     |     |
| -------- | -------------------------------- | --- | --- | --- | --- | --- |
Figs. 1 and 2, the framework follows a layered architec-
Python package dependencies
requirements.txt ture that separates anomaly classification, threshold eval-
Dockerfile Docker configuration script uation, and remediation dispatch. The present section
Kubernetes manifest
deployment.yaml focuses only on concrete implementation aspects, how
Docker Compose orchestration file
docker-compose.yaml this architecture was realised, containerised, and evalu-
| prometheus.yml | Prometheus scraping rules |     |     |     |     |     |
| -------------- | ------------------------- | --- | --- | --- | --- | --- |
ated in practice, without re-stating the full design ration-
ale already detailed in Sect. 3.
|     |     |     | CROSS  is  implemented  | in  | Python  with  | a  central  |
| --- | --- | --- | ----------------------- | --- | ------------- | ----------- |
registry that maps OS types to remediation handlers
Tables 1 and 5 together provide a complete performance
using Python decorators, enabling dynamic dispatch
summary; Tables 1,2, 3 and 4 reports detection accuracy
and  recovery  effectiveness  (precision,  recall,  MTTR),  of  actions  tailored  to  each  environment.  Each  han-
dler abstracts native tools (for example, ADB, sys-
while Table 5 isolates runtime and resource efficiency
temctl, or PowerShell) behind a consistent interface
(CPU, RAM) under identical test conditions.
so that the remediation process remains explainable
Table 4 Examples from the static rule base (B2)
| Log template (normalised)          |     |     |     | Remediation action |           |     |
| ---------------------------------- | --- | --- | --- | ------------------ | --------- | --- |
| systemd: Failed to start <SERVICE> |     |     |     |                    | <SERVICE> |     |
systemctl restart
sshd: Authentication failed for <USER> Lock account for 5 min; rotate keys; trigger audit
docker: container <ID> exited (status != 0) <ID> and clear image cache
docker restart
nginx: upstream timed out Reload Nginx; increase upstream proxy_read_timeout
Windows: Service <NAME> terminated unexpectedly Restart service via PowerShell; reapply policy

Johnphill et al. Cybersecurity           (2026) 9:124  Page 8 of 24
Table 5 Overall execution time and resource usage (mean over  •  Android: Uses ADB for cache clearing and reboot.
| 10 runs; cf. Table 1) |     |     |     |     | Simulated if ADB is unavailable. |     |     |     |
| --------------------- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
Method MTTR (s) CPU Overhead  Memory  •  Linux: Executes updates, service restarts, and disk
(%) Overhead  clean-up. Falls back to simulated execution if sys-
(MB)
temctl is missing.
Manual scripts 89.4 11.3 92.1 •  macOS:  Performs  simulated  updates,  service
restarts, and clean-up.
| Rule-based | 54.2 | 8.7 | 71.6 |     |     |     |     |     |
| ---------- | ---- | --- | ---- | --- | --- | --- | --- | --- |
CROSS (proposed) 34.1 9.2 75.4 •  Windows: Uses PowerShell scripts for maintenance.
Falls back to simulated logic if needed.
Logs are structured into tabular form using Python and
evaluated against thresholds. If exceeded, remediation
and reproducible across systems. When native tools
is triggered (see Listing 1).
| are  unavailable,  | simulated  | execution  | is  invoked,  | as  |     |     |     |     |
| ------------------ | ---------- | ---------- | ------------- | --- | --- | --- | --- | --- |
explained earlier in Fig. 2.
Architecture overview
CROSS is implemented in Python with modular archi-
| tecture.     | A  central  registry  | maps    | OS  types    | to  their  |     |     |     |     |
| ------------ | --------------------- | ------- | ------------ | ---------- | --- | --- | --- | --- |
| remediation  | handlers  using       | Python  | decorators.  | This       |     |     |     |     |
enables dynamic dispatch of actions tailored to each
|     |     |     |     |     | Listing  1 Threshold  | Evaluation  | LogicDocker  | con- |
| --- | --- | --- | --- | --- | --------------------- | ----------- | ------------ | ---- |
environment:
tainerisation ensures consistency across environments.
Core Dockerfile features are shown in Listing 2.
Listing 2 Dockerfile for containerisation

J ohnphill et al. Cybersecurity (2026) 9:124 Page 9 of 24
CROSS is deployed on Kubernetes using the manifest • Resource utilisation (CPU, memory, network)
in Listing 3.
Results showed CROSS provides reliable, autonomous
remediation across all supported platforms. Com-
pared with manual methods and alternate frameworks,
CROSS improved recovery time and consistency.
Baselines and benchmark protocol
Baselines. We evaluate CROSS against two non-learn-
ing baselines:
• B1: Manual Scripts. System administrators inspect
logs and execute corrective scripts (service restarts,
cache/disk cleanup, configuration reloads) by hand.
This represents the conventional, non-automated
workflow.
• B2: Static Rule-Based Remediation. A determinis-
tic engine that maps log patterns to actions using a
hand-crafted ruleset. No statistical classification is
used.
Rule-base derivation (for B2). Rules were derived
from the same preprocessed log corpus used by CROSS
(see Data Availability; derived from Loghub (LOGPAI
2023; He et al. 2023) and our Zenodo release (Johnphill
and Sadiq 2024)). We extracted frequent error/warn-
ing templates and service names, then associated each
template with the most common successful corrective
action observed during pilot runs.
Listing 3 Kubernetes Deployment for the CROSS self-healing engine
1. Template mining: tokenise logs and keep lines
Platform‑specific integration highlights labelled warning/error; normalise dynamic fields
Development occurred on macOS Sequoia (M3 Pro (PIDs, IPs, timestamps) to placeholders; count tem-
chip, 18 GB RAM). The modular design enables struc- plate frequencies.
tured log ingestion and OS-specific remedial dispatch. 2. Trigger terms: retain templates containing service/
Python libraries used include: process tokens (for example, systemd, sshd,
docker, nginx, winlogon) and failure terms
• pandas for log processing (for example, failed, timeout, unreachable,
• subprocess, os for shell execution permission denied).
• prometheus_client, Flask, and werkzeug 3. Action mapping: map each template to one corrective
A
for exposing metrics action chosen from ={ restart service, reload con-
fig, clear cache, restart device, enforce policy, no-op .
}
4. Conflict resolution: if multiple actions match a tem-
Metrics including errors and remedial counts are
plate, pick the one with highest empirical success
pushed to Prometheus and displayed via Grafana.
rate during pilot runs; break ties with least-disruptive
CROSS performance evaluation action.
Performance was evaluated via simulations using pre-
Table 4 shows representative rules; the full list is in the
processed logs. Metrics included:
artefact.
• Execution latency for remedial actions
Implementation details. B2 performs regex match-
• Recovery time from error state to normal
ing over templates in priority order; the first match

Johnphill et al. Cybersecurity (2026) 9:124 Page 10 of 24
fires. Actions execute through OS-native interfaces usage, outperforming both the rule-based and manual
(systemctl/shell on Linux, PowerShell on Windows, baselines under identical experimental conditions.
adb on Android, and launchd/bash on macOS). Safety
guards include rate limiting and idempotent com-
mands. No ML inference is used in B2. Evaluation of attack‑induced anomalies and future work
Benchmark protocol. All methods consume the same While the present evaluation primarily focused on
preprocessed log stream. For CROSS, anomalies are operational anomalies such as service crashes, I/O bot-
detected with Multinomial Naïve Bayes (CountVec- tlenecks, and configuration errors, it did not explicitly
torizer features); remediation is triggered when error/ benchmark attack-induced anomalies. In CPS, mali-
T T
warning counts exceed thresholds e , w (Sect. 4). For cious activity, such as repeated authentication failures,
B2, the first matching rule emits an action; for B1, privilege escalation attempts, abnormal port scanning,
humans execute the equivalent action. or log tampering, can manifest as anomalies within
system logs. Although CROSS’s classifier was trained
• Datasets. Android, Linux, macOS, and Windows on generic fault data, its probabilistic structure allows
logs (split 80/20 by time where applicable); attack- extension toward identifying and remediating these
like patterns are discussed in Sect. 5.5. adversarial patterns.
10
• Runs. Each experiment is repeated per plat- Conceptually, the anomaly detection component can
×
form; we report mean ± stdev. be expanded to incorporate security-contextual log
• Metrics. Precision, recall (for anomaly detection); tokens (for example, “unauthorised”, “denied”, “mal-
Mean Time To Recovery (MTTR) from detection ware”, “connection refused”) to distinguish between
to resolution; CPU% and RAM (container-level). fault-induced and attack-induced anomalies. These
T T
• Parity controls. Identical thresholds ( e , w ) and would trigger remediation actions aligned with secu-
action catalogs across methods; identical host/con- rity protocols, such as service isolation, temporary user
tainer limits; cold-start between runs. lockout, or triggering audit policies. Future experi-
ments will integrate datasets such as Loghub (He et al.
Summary of differences. B2 reacts only to known pat- 2023; LOGPAI 2023) enriched with security event logs
terns and cannot generalise beyond its rule set; CROSS to simulate realistic intrusion scenarios.
generalises from feature space and selects actions via To strengthen CROSS’s resilience in adversarial con-
policy, yielding higher recall and faster MTTR in previ- texts, future research will focus on:
ously unseen conditions (see Table 1).
Experimental repetitions and statistical analysis. • Adversarial Robustness: Employing adversarial train-
Each experiment was executed 10 times per platform ing and ensemble detection to resist evasion and poi-
(Android, Linux, macOS, Windows) for each method soning attacks targeting log-based classifiers.
(Manual, Rule–Based, CROSS). For every run we (i) • Risk-Aware Action Selection: Integrating reinforce-
performed a fresh container start, (ii) cleared caches, ment learning for adaptive remediation that balances
and (iii) fixed the random seed for data splits and model system availability with security constraints.
initialisation to ensure repeatability. We report • Secure Execution Constraints: Implementing sand-
mean ± standard deviation across the 10 executions. boxed or privilege-restricted remediation processes
Mean Time To Recovery (MTTR) is measured from the to prevent exploitation of self-healing actions.
anomaly detection timestamp to the completion of the • Expanded Evaluation: Benchmarking CROSS using
remedial action using a monotonic wall-clock timer. hybrid datasets containing both operational and
Detection precision/recall are computed on the held-
out stream for each run and then averaged. Ninety-five
percent confidence intervals (CI) are provided where
space permits using the Student t-interval,
x ¯ ± t 0.975,n − 1 √ s n with n = 10 . Where applicable, we test Table 6 Summary of detected issues per system
differences against the strongest baseline using a two- System Errors detected Warnings
α 0.05
sided paired t-test ( ). detected
=
Runtime summary. Together with the comparative
Android 154,232 3,237
accuracy metrics in Table 1, the runtime and resource
Linux 415 4,198
measurements in Table 5 confirm CROSS’s overall effi-
macOS 16,661 370
ciency. It achieves the lowest mean MTTR (34.1 s) while
Windows 2,895 3,320
maintaining modest CPU (9.2%) and RAM (75.4 MB)

J ohnphill et al. Cybersecurity (2026) 9:124 Page 11 of 24
attack-induced anomalies, including data from intru- balanced mix, consistent with its broad use and heteroge-
sion detection systems and CPS honeypots. neous deployment environments.
Table 7 outlines the remediation steps taken. For
Through incorporating these extensions, CROSS can Android, CROSS used ADB-based commands to clear
evolve from an operational self-healing system into a app data and reboot the device. In Linux, it performed
cyber-resilient framework capable of autonomously updates and restarted SSH services, subject to contain-
detecting, classifying, and mitigating both faults erisation constraints. macOS and Windows relied on
and malicious activities across heterogeneous CPS simulated updates and service restarts due to tooling
environments. limitations. These adaptations confirmed CROSS’s ability
to autonomously handle varied faults, fall back gracefully
Simulation results when direct commands fail, and maintain observability
The simulation results are summarised in Tables 6 through structured logging. This confirms CROSS’s suit-
and 7. Table 6 presents the number of errors and warn- ability for dynamic, multi-OS environments where resil-
ings detected per system. These findings underscore the ience and autonomous recovery are essential.
need for system-specific remediation strategies across As Table 6 shows, Android produced the most errors,
Android, Linux, macOS, and Windows. To simulate real- while Linux recorded the highest warning count. These
istic conditions, high volumes of system logs, represent- distributions highlight the importance of adaptive fault-
ing faults such as service crashes, memory overflows, handling strategies tailored to each platform’s operational
app freezes, and incomplete updates, were preprocessed profile.
through the LISH pipeline for anomaly detection. The
CROSS engine ingested these logs and applied threshold- Remediation simulation across platforms
based logic to determine required actions. Figure 3 shows the initialisation phase of the CROSS self-
Each platform’s logs exhibited distinct behavioural healing engine. At runtime, the framework detects a pre-
traits. Android showed an exceptionally high error count, processed data directory and loads logs from Android,
indicating frequent app-level failures such as permis- Linux, macOS, and Windows platforms: Android_
sion issues or failed installs, characteristic of Android’s preprocessed.csv, Linux_preprocessed.csv,
fragmented runtime environments. Linux logs revealed Mac_preprocessed.csv, and Windows_preproc-
more warnings than errors, typically linked to early signs essed.csv. Each loading step is printed to the termi-
of degradation, outdated software, or recoverable ser- nal for traceability, confirming readiness for anomaly
vice issues. macOS logs showed relatively fewer issues detection.
overall, likely reflecting Apple’s tighter system controls This modular ingestion step supports extensibility
and standardised configurations. Windows presented a to new platforms without altering remediation logic,
Fig. 3 Initialisation of CROSS showing multi-platform preprocessed log loading

Johnphill et al. Cybersecurity           (2026) 9:124  Page 12 of 24
Fig. 4 Android remediation: ADB reset failed due to no device; fallback simulation applied
| Fig. 5 Linux remediation:  |  updates succeeded; SSH restart failed due to  |  absence |
| -------------------------- | ---------------------------------------------- | -------- |
|                            | apt systemd                                    |          |

J ohnphill et al. Cybersecurity (2026) 9:124 Page 13 of 24
Fig. 6 macOS remediation: simulated update, service restart, and clean-up actions
Fig. 7 Windows remediation: Simulated PowerShell update, service restart, and clean-up
Table 7 Remedial actions implemented for each system
System Remedial actions
Android Clear app data, reboot device. Simulated actions used if tools are unavailable.
Linux Apply updates, restart SSH, clean disk. Service restart simulated where unsupported.
macOS Simulated software update, service restart, and disk clean-up.
Windows Simulated update, service restart (IIS), and disk clean-up via PowerShell logic.
ensuring CROSS remains scalable and maintainable Figure 5 illustrates Linux remediation. CROSS initi-
across diverse systems. ates updates via apt, followed by an attempt to restart
Figure 4 shows Android remediation. Upon detect- SSH using systemctl. The service restart fails because
ing excessive errors, CROSS attempts adb shell pm systemd is not available in the container. CROSS logs
clear com.example.app. The command fails due the failure with command trace, demonstrating aware-
to no connected device. CROSS logs the failure and ness of runtime constraints.
simulates the command, followed by adb reboot, Figure 6 shows macOS simulation. CROSS simulates
preserving remediation flow and enabling post-hoc softwareupdate -i -a, apachectl restart,
review. and a disk clean-up, reflecting standard macOS admin

Johnphill et al. Cybersecurity (2026) 9:124 Page 14 of 24
routines. Though simulated, these steps demonstrate Hallur 2022; Akinbolaji et al. 2024; Pai and Srinivas
CROSS’s consistent remediation logic across systems. 2024).
Figure 7 shows Windows remediation. As PowerShell In addition to the Prometheus-Grafana stack currently
is unavailable in the container, CROSS simulates com- integrated within CROSS, further observability can be
mands: Install-WindowsUpdate -AcceptAll, achieved by incorporating emerging tools such as Loki
Restart-Service -Name ’W3SVC’, and Clean- for centralised log aggregation and HashiCorp Vault for
mgr /sagerun:1. These simulate update, service managing secure telemetry pipelines, as recommended
recovery, and disk maintenance. in recent observability studies (Akinbolaji et al. 2024; Pai
Figures 3 , 4, 5, 6 and 7 display terminal traces from and Srinivas 2024). These tools contribute enriched con-
CROSS running in a Dockerised simulation. The frame- text, support trace correlation, and provide secure access
work executes OS-specific remediation workflows based to system-level metrics, which are particularly impor-
on anomaly thresholds and adapts when native tools are tant in multi-tenant CPS environments or scenarios
unavailable. Observability and graceful fallback ensure involving sensitive infrastructure. Their inclusion would
reliability across diverse environments. strengthen traceability, enhance compliance, and support
Table 7 categorises system-specific actions applied by production-grade deployment of CROSS. The founda-
CROSS. Android and Windows relied on simulation due tional pillars of observability, logs, metrics, and traces,
to tooling limits, while Linux and macOS demonstrated play distinct yet complementary roles. Logs provide
partial native and simulated execution. These results vali- timestamped, immutable records of discrete events that
date CROSS’s adaptability across OS contexts. offer valuable context around system actions and failures.
Metrics represent quantitative measurements, such as
Evaluating observability of CROSS framework CPU usage, memory consumption, and request through-
CROSS integrates observability using Prometheus for put, which together reflect the real-time performance
metrics collection and Grafana for dashboard visualisa- characteristics of a system. Traces capture the end-to-
tion. Observability, particularly within Kubernetes and end journey of a request across multiple services within
distributed systems, refers to the ability to infer the inter- a distributed architecture, revealing critical insight into
nal state of a system solely from its external outputs. It inter-service communication paths and potential latency
goes beyond traditional monitoring by offering a richer, bottlenecks (Hallur 2022).
more structured method of understanding system behav- The implementation of observability in this self-healing
iour, leveraging primary telemetry signals, namely logs, system leverages a monitoring and visualisation stack
metrics, and traces, alongside auxiliary indicators such as built around Prometheus and Grafana. Prometheus is an
health checks. These signals operate in unison to deliver open-source monitoring system designed for time-series
comprehensive insight into application performance and data collection and analysis. Within the Kubernetes envi-
the operational state of the system (Siddiqui et al. 2023; ronment, it is configured to scrape metrics from pods,
Hallur 2022; Akinbolaji et al. 2024; Pai and Srinivas nodes, and internal components of the remediation
2024). Modern microservices architectures, cloud-native framework. These metrics encompass system resource
deployments, and complex distributed environments usage, application health indicators, and frequency of
present challenges that conventional monitoring tools observed errors (Siddiqui et al. 2023; Hallur 2022; Akin-
often struggle to overcome. Observability bridges this bolaji et al. 2024; Pai and Srinivas 2024).To visualise this
gap by providing a holistic perspective on system behav- data, Grafana is deployed alongside Prometheus, ena-
iour under real-world conditions. It enables engineering bling real-time and historical views through customisable
teams to proactively detect anomalies, trace problems to dashboards. This integration allows stakeholders to mon-
their root cause, and significantly reduce both the mean itor platform-specific error rates, CPU and memory utili-
time to detect (MTTD) and the mean time to resolve sation, remediation success ratios, and response latencies
(MTTR) faults within the system (Siddiqui et al. 2023; between error detection and recovery. Grafana’s intuitive
interface complements Prometheus by offering flexible
Fig. 8 CROSS monitoring output – total errors detected by system type

J ohnphill et al. Cybersecurity (2026) 9:124 Page 15 of 24
and interactive dashboards for operational insights. This Grafana for real-time visualisation. This monitoring
observability infrastructure ensures that the self-healing infrastructure enabled comprehensive evaluation of self-
system remains transparent, auditable, and continuously healing behaviours, system resource consumption, and
optimised. It supports not only runtime monitoring the responsiveness of corrective actions triggered by the
but also research-focused evaluation, enabling iterative framework across heterogeneous platforms, including
refinement of healing strategies based on empirical evi- Android, Mac, Linux, and Windows. The monitoring sys-
dence. Through this setup, operators and researchers gain tem collected a wide range of metrics essential for quan-
the necessary visibility to validate system performance, tifying the health and performance of the self-healing
identify bottlenecks, and improve the reliability of auto- platform. These included error and warning occurrences,
mated remediation mechanisms. resource usage profiles (for example, memory, CPU),
query execution latency, scrape duration, and configura-
Performance evaluation and metrics tion reload frequencies. Such metrics provide key indica-
To evaluate the performance and operational impact of tors of how the system performs under fault conditions
the CROSS framework, a robust observability stack was and the overhead introduced by continuous monitoring.
deployed using Prometheus for metric collection and
Fig. 9 CROSS monitoring output – total warnings detected by system type
Fig. 10 CROSS monitoring output – memory profile across system nodes
Fig. 11 CROSS monitoring output – processing time and memory usage

Johnphill et al. Cybersecurity (2026) 9:124 Page 16 of 24
Fig. 12 CROSS monitoring output – query execution durations across system nodes
Fig. 13 CROSS monitoring output – compaction activity over time
Figures 8 and 9 highlight the distribution of errors and thresholds or non-critical service evaluations to reduce
warnings across system types. Android systems reported false positives.
the highest number of errors (154,232), indicating sys- To measure the monitoring overhead, Figs. 14 and 15
temic instability, possibly due to fragmented OS ver- visualise scrape duration and reload activity over time.
sions and hardware variability. Linux, on the other hand, Prometheus exhibited consistent and low-latency scrape
registered the highest volume of warnings (4,198), likely durations across all targets, including the CROSS engine
attributable to verbose log generation and the nature of itself (denoted in dark red), which emitted lightweight,
system-level alerts. Mac and Windows reported fewer real-time metrics. The reload count remained stable, with
anomalies overall, suggesting more stable or tightly no reload failures, confirming the reliability of the con-
regulated environments. The significance of these met- figuration pipeline.
rics lies in their ability to inform adaptive, OS-specific Further evaluation of runtime behaviour is cap-
remedial strategies. For instance, systems with high error tured in Figs. 12 and 13. Query execution metrics,
rates may require frequent service restarts, cache clear- such as inner_eval_p99, prepare_time_p99,
ances, or system patching routines. Systems generat- and queue_time_p99, reflect how quickly the sys-
ing more warnings may benefit from adjusted detection tem could evaluate and respond to faults. Compaction

J ohnphill et al. Cybersecurity (2026) 9:124 Page 17 of 24
Fig. 14 CROSS monitoring output – scrape duration and monitoring overhead
Fig. 15 CROSS monitoring output – count of reloaded configurations during runtime
activity, vital for maintaining time-series database per- autonomous remediation illustrates a scalable and gen-
formance, showed regular triggering with zero failures, eralisable approach to resilient cyber-physical system
indicating data integrity was preserved under continuous management.
monitoring and write loads.
Figures 10 and 11 focus on system-level resource uti- Error and warning detection
lisation. Memory profiles across nodes revealed that Accurate interpretation of system anomalies is central
CROSS components maintained steady consumption, to the effectiveness of the CROSS framework. As shown
while processing time graphs showed bounded overhead earlier in Table 6 (Sect. 6), Android exhibited the highest
under load, confirming the framework’s ability to oper- number of critical error events, while Linux produced the
ate autonomously without compromising host system largest volume of warnings. These platform-specific dis-
performance. The collected metrics validate CROSS’s tributions underscore the importance of adaptive fault-
ability to perform lightweight, adaptive self-healing handling strategies. CROSS interprets such telemetry
without inducing measurable system strain. The combi- in real time through Prometheus metrics, enabling pro-
nation of detailed observability, fault classification, and portional, OS-aware remediation. For instance, systems

Johnphill et al. Cybersecurity (2026) 9:124 Page 18 of 24
with high error rates trigger deeper corrective routines Lastly, the insights gained from these metrics are instru-
such as service restarts or cache clearance, whereas those mental in guiding decisions around auto-scaling policies
with frequent warnings receive lightweight or deferred and optimising resource allocations within containerised
actions. This adaptive control prevents over-remediation deployments, thereby enhancing the system’s overall effi-
and reduces noise in stable environments. ciency and responsiveness.
The framework thereby calibrates its healing intensity The results highlight the stability and efficiency of the
according to observed fault behaviour, using thresholds CROSS framework under dynamic conditions, dem-
informed by historical results rather than static val- onstrating that system health can be preserved without
ues. Android environments, prone to frequent app-level overconsuming computational resources. This balance
instability, benefit from more aggressive interventions, is crucial to sustaining continuous fault detection and
while Linux and macOS adopt observability-led main- autonomous remediation in production environments.
tenance. Through this approach, CROSS maintains effi-
ciency and transparency across heterogeneous platforms Query performance and latency
without re-stating platform-specific metrics already dis-
Timely query execution is crucial for observability plat-
cussed earlier.
forms, especially within self-healing frameworks such
as CROSS, where metrics must be analysed and acted
Resource utilisation and processing time
upon without delay. In the CROSS system, query execu-
Resource usage is a critical performance indicator for
tion latency directly impacts the speed at which faults are
any autonomous system operating within real-time con-
diagnosed and remediation workflows are triggered.
straints. In the CROSS framework, Prometheus metrics
Figure 12 presents the execution durations for Pro-
are utilised to monitor CPU and memory consumption,
metheus queries, segmented into key performance
as well as processing durations, across its various com-
phases. The green line (labelled inner_eval_p99)
ponents. Figures 10 and 11 present visual representa-
represents the 99th percentile duration for the inner eval-
tions of these performance metrics. Figure 10 illustrates
uation of queries, which is typically the most compute-
the memory usage profile across monitored services
intensive stage. Spikes in this metric suggests increased
within the CROSS ecosystem. The observed variability in
system load or inefficient query execution. The orange
memory allocation reflects how components such as Pro-
line (prepare_time_p99) captures the time spent
metheus, the self-healing engine, and associated export-
preparing a query before execution; sustained elevated
ers dynamically respond to changing workloads. Periodic
values here indicate complexity in query parsing or label
spikes in memory usage often coincide with bursts of
matching. The blue line (queue_time_p99) reflects
anomaly detection activity or service reloads, providing
delays caused by queuing when multiple queries are
valuable insights into moments of operational strain. In
executed concurrently. The flatness of this line indicates
contrast, flat and stable memory usage trends suggest
minimal contention during the observed period. Lastly,
efficient memory handling, indicating the absence of
the red line (result_sort_p99) shows the duration
memory leaks or inflated services.
taken to sort query results, which remains close to zero
Figure 11 presents a combined visualisation that over-
and therefore contributes negligible post-processing
lays memory consumption with query execution latency,
overhead. The low values recorded across all dimensions
offering a more holistic view of system performance. This
confirm that the CROSS observability layer delivers near
pairing enables correlation analysis, such as identifying
real-time responsiveness. This is vital for sustaining the
whether increased memory pressure results in longer
fast feedback loops necessary to support autonomous
processing times. In some instances, steady execution
anomaly detection and prompt execution of remedial
durations despite rising memory footprints imply that
actions.
caching or buffering strategies are being applied effec-
tively. Conversely, if processing latency rises in tandem
with memory peaks, this signals the presence of resource Data integrity and write performance
contention or underlying performance bottlenecks. These CROSS relies on Prometheus as its metrics backend,
performance metrics serve several vital purposes. They which utilises a time-series database (TSDB) to per-
ensure that CROSS operates within acceptable resource sistently store telemetry data. It is essential that this
boundaries, particularly in constrained environments database maintains both consistency and integrity, par-
such as edge devices or cloud-based deployments. More- ticularly during periods of high ingestion when data
over, they assist in identifying and diagnosing perfor- volumes and write operations peak. Figure 13 visualises
mance regressions that could impair the system’s ability the compaction activity over time, a crucial aspect of
to detect anomalies and apply remedial actions promptly. Prometheus’s internal housekeeping processes. The blue

J ohnphill et al. Cybersecurity (2026) 9:124 Page 19 of 24
line (labelled triggered) represents the initiation of activity, which remains consistently efficient and exhibits
compaction events used to merge smaller time-series negligible performance impact. The dark red line (self-
segments. These events are vital for sustaining efficient healing) represents the CROSS remediation engine
disk I/O and maintaining fast query responses. The green itself, demonstrating minimal and stable scraping over-
line (compactions) tracks successfully completed head throughout the observation window. These results
compaction operations; the density of these markers collectively confirm that the CROSS monitoring stack
indicates that the system performs regular background introduces only lightweight overhead during normal
maintenance, contributing to TSDB stability. In contrast, operation, enabling real-time system introspection with-
the orange line (failed) monitors failed compaction out compromising performance or triggering cascading
attempts. Its complete absence during the observed time- delays in remediation logic.
frame suggests that the database experienced no write Figure 15 shows the frequency of configuration reloads
failures, demonstrating a robust and healthy storage layer during runtime. This reload pattern serves as an indica-
within the CROSS observability stack. These indicators tor of system dynamism and the stability of the observ-
affirm that Prometheus, as configured within CROSS, ability layer. The green line (labelled reloads) captures
maintains data integrity and write performance even successful configuration reload events, with the presence
under continuous monitoring loads, ensuring reliability of regular spikes suggesting either scheduled updates
of telemetry data for all subsequent anomaly detection or dynamic reconfiguration of monitored services.
and remediation tasks. The orange line (failures) remains consistently flat
These metrics verify that CROSS’s monitoring infra- throughout the observation period, confirming that no
structure is capable of handling sustained metric reload errors were encountered. Taken together, these
throughput without degradation. Compactions were exe- observations validate that CROSS maintains a low-
cuted consistently and successfully, which ensures time- overhead, high-performance observability setup. Scrape
series data remains queryable with minimal latency. durations remained stable and within acceptable opera-
tional thresholds, and configuration reloads occurred
predictably without disruption. This level of efficiency
Scraping and reload performance
within the telemetry pipeline is essential to ensuring that
Monitoring is a vital component of self-healing systems,
CROSS can autonomously detect anomalies and dispatch
providing real-time insights into system health, anom-
remediation actions reliably across complex, multi-plat-
aly frequency, and the outcomes of remediation efforts.
form CPS environments.
Within the CROSS framework (Cross-platform Remedia-
tion and Observability Self-Healing System), Prometheus Metric roles, relevance, and performance summary
plays a central role in continuously collecting and evalu-
Within the CROSS framework, specific observability
ating system-level metrics, including error logs, resource
metrics play a pivotal role in maintaining operational
usage, and operational signals. To evaluate the monitor-
efficiency and supporting autonomous remediation.
ing efficiency of CROSS, two primary metrics were ana-
Scrape duration measures the time Prometheus requires
lysed: scrape duration and reload count, as presented
to collect metrics from a target system. Extended or
in Figs. 14 and 15. These metrics quantify the overhead
inconsistent durations indicates underlying bottlenecks,
associated with ongoing data collection and configura-
high system load, or suboptimal target responsiveness.
tion reloads, both of which influence the responsiveness
Meanwhile, reload count monitors how frequently Pro-
and performance of the observability pipeline.
metheus reloads its configuration files. Elevated reload
Figure 14 illustrates the scrape durations across
frequencies can point to dynamic infrastructure changes,
various Prometheus targets. The green line (labelled
frequent service registrations, or potential misconfigura-
docker) reflects stable and low-latency metric scrap-
tions in scrape jobs. These metrics are critical for diag-
ing from Docker containers, suggesting reliable com-
nosing ingestion delays that could impair the timeliness
munication with containerised services. The orange line
of anomaly detection and subsequent remediation. They
(kube-state-metrics) captures metrics related to
also serve to assess the responsiveness and stability of
Kubernetes cluster state and displays moderate vari-
monitored components, inform resource scaling deci-
ability due to dynamic changes within the orchestration
sions, and guide adjustments to scrape intervals. Ulti-
environment. The blue line (node-exporter) cor-
mately, these indicators help to ensure the reliability of
responds to host-level metrics collection and reveals
the entire observability pipeline within CROSS.
higher-frequency oscillations, likely caused by fluctuating
The performance metrics collected during evalua-
resource activity on the host machine. The red line (pro-
tion offer important insights into system behaviour
metheus) tracks Prometheus’s internal self-monitoring
and optimisation priorities. Android exhibited the

Johnphill et al. Cybersecurity (2026) 9:124 Page 20 of 24
highest number of errors, highlighting the need for fur- system effectively managed variations in available tooling
ther refinement of remediation strategies tailored to the and operating constraints across platforms, particularly
platform’s instability. Linux, on the other hand, recorded those arising from containerisation, such as process ID
the greatest number of warnings, suggesting that more (PID) isolation and limited access to system toolchains.
sophisticated predictive analytics or threshold adjust- These operational conditions underscored the impor-
ments will be required to avoid excessive alerts. Query tance of robust fallback routines and precise error han-
latency remained minimal across all monitored compo- dling. CROSS addresses this by simulating executions
nents, confirming that real-time performance monitoring where necessary and maintaining comprehensive logging,
operates efficiently. Additionally, memory and CPU usage thereby ensuring that remediation attempts are traceable
were stable throughout, demonstrating that resource and continue even under less-than-ideal conditions.
management within the CROSS architecture is effective. In terms of strategic positioning, CROSS aligns with
Both scraping and configuration reloading processes per- emerging industry trends favouring autonomous, AI-
formed optimally, ensuring sustained system responsive- driven infrastructure. Its integration with standard
ness and minimal overhead in the telemetry pipeline. observability stacks, such as Prometheus and Grafana,
supports low-latency recovery loops and quantifi-
Discussion
able remediation metrics. Its lightweight classification
The CROSS framework addresses critical challenges in approach and threshold-triggered execution logic make
the design and deployment of self-healing systems, par- it particularly well-suited to resource-constrained envi-
ticularly within heterogeneous CPS environments. Unlike ronments, such as embedded or edge CPS deployments.
existing solutions that tend to focus on either detection Nonetheless, the framework has its limitations. Chief
or remediation within narrow operating boundaries, among these is the inability to invoke certain native
CROSS presents a holistic, platform-agnostic approach remediation tools within containerised environments, an
that fuses detection, remediation, and observability into issue stemming from restricted process control and privi-
a cohesive, modular architecture. It not only introduces lege boundaries. There may also be minor delays intro-
a practical and extensible design for autonomous reme- duced by log processing or orchestration overhead. These
diation but also raises the benchmark for cross-platform limitations are offset to a degree by the system’s modular
self-healing systems by combining fault detection, execu- design, transparent logging architecture, and OS-aware
tion logic, and system introspection within a lightweight, remediation logic. Future work may include the devel-
scalable solution. While CROSS currently leverages opment of native agents or elevated runtime modules to
lightweight probabilistic models for anomaly detec- bridge these gaps more effectively.
tion and employs threshold-based remediation, future
enhancements may draw on advances in AIOps (Artifi- Adaptive fallback logic and CPS‑relevant scenarios
cial Intelligence for IT Operations), as explored by Cheng
Adaptive fallback logic provides resilience in situa-
et al. (2023). Their review highlights the growing role of
tions where standard remediation routines cannot be
machine learning in cloud-native diagnostics, root cause
executed due to unavailable tooling, permission restric-
analysis, and intelligent automation; directions that align
tions, or degraded system states. Each remediation
closely with CROSS’s development roadmap, including
action is associated with one or more fallback alterna-
reinforcement learning or predictive models to support
tives, organised in a prioritised sequence. If an action
more context-aware remediation decisions. This sec-
fails, for example, due to missing binaries or command
tion critically evaluates the broader implications of the
rejection, the fallback is automatically attempted, ena-
framework, distinguishing it from existing solutions and
bling CROSS to maintain operational continuity. In
exploring its potential real-world applications.
CPS contexts, fallback logic is particularly valuable.
CROSS demonstrates considerable adaptability
For example, if a soft reset of a network service on
through its successful deployment of remediation logic
an industrial gateway fails, CROSS may revert to a
across Android, Linux, macOS, and Windows environ-
bounded interface reset, followed by a policy-defined
ments. This flexibility is achieved through the use of a
escalation such as transferring the affected node into
dynamic registry for OS-specific handlers, which sup-
a maintenance-safe state. Similarly, should an edge
ports extensibility by allowing additional platforms to be
controller fail to terminate an unresponsive process,
incorporated without restructuring the core logic. In this
CROSS may execute a container-level restart or, in
regard, CROSS outperforms other solutions that are typi-
highly constrained real-time environments, trigger a
cally bound to a single operating system or dependent on
supervisory watchdog rather than performing system-
rigid, static rule sets. Implementation testing revealed
wide restarts. These examples demonstrate that the
meaningful insights and challenges. For example, the
fallback logic extends beyond conventional IT-centric

J ohnphill et al. Cybersecurity (2026) 9:124 Page 21 of 24
remediation, enabling CPS-specific recovery behav- medical IoT hubs, or container-capable embedded Linux
iours such as industrial fail-safe mechanisms, Remote devices. Legacy PLCs and microcontroller-based systems
Terminal Unit (RTU) state reinitialisation, and Pro- are not target deployment points; instead, CROSS can
grammable Logic Controller (PLC)-supervised inhibi- function as a supervisory node augmenting such devices.
tion states. In these configurations, resource impact is confined to
the supervisory host, while CPS devices benefit indi-
rectly through reduced mean-time-to-recovery (MTTR),
Policy‑driven remediation improved anomaly visibility, and consistent remediation
CROSS employs a policy-driven remediation layer orchestration. This contextualisation clarifies that CROSS
that systematically maps detected anomalies to plat- complements a layered CPS architecture: lightweight
form-specific corrective actions. Policies are specified schemes such as LISH serve highly constrained environ-
declaratively using a lightweight rules format, allow- ments, whereas CROSS delivers comprehensive remedia-
ing operators to define conditions, triggers, and asso- tion on more capable nodes within the CPS hierarchy.
ciated remediation procedures without modifying CROSS exhibits significant potential for deployment
source code. A generic policy entry consists of: (i) an in mission-critical domains such as healthcare moni-
anomaly signature or label; (ii) contextual constraints toring, intelligent transport systems, smart grids, and
such as platform, severity, or resource thresholds; and industrial automation. Its observability model provides
(iii) a sequence of remediation actions with optional real-time insights into fault patterns, recovery latency,
escalation logic. At runtime, CROSS matches predicted and overall system health. This, in turn, strengthens post-
anomalies with the policy catalogue to determine an incident analysis, regulatory compliance, and operational
appropriate remediation plan. accountability-features that are vital for environments
Policies are evaluated in a context-aware manner: for where system reliability is non-negotiable. To deepen this
example, a high-CPU anomaly on Linux may trigger perspective, the following subsection critically reflects on
process throttling, whereas an equivalent anomaly on the limitations of using OS-level telemetry as an abstrac-
Android may invoke app-level restarts due to platform tion for CPS state, and how this impacts diagnosis and
constraints. Policy inheritance allows common remedia- remediation in control-dominated environments.
tion strategies to be specialised for individual OS fami- A limitation of the present study is that CROSS was
lies, ensuring consistency while enabling fine-grained not evaluated directly on physical CPS or OT devices
platform tailoring. To illustrate, a network-degradation such as PLCs, RTUs, or protection relays. The experi-
anomaly may trigger different sequences depending on ments relied on OS-level telemetry as a unifying abstrac-
execution context: (a) on a supervisory industrial gate- tion for demonstrating cross-platform anomaly detection
way, CROSS may restart affected services or reset net- and remediation. While this approach provides broad
work interfaces; (b) on a safety-critical device, policies generalisability across heterogeneous operating systems,
may restrict CROSS to non-intrusive diagnostics only, OS logs do not capture CPS-specific process deviations
deferring intrusive actions to a supervisory controller. or control-layer faults observable only through field-bus
This separation ensures that remediation remains aligned traffic, PLC logic traces, or real-time controller telem-
with operational and safety requirements across hetero- etry. OS-level signals should therefore be viewed as a
geneous CPS environments. foundational but incomplete proxy for CPS behaviour.
Future work will integrate cyber-physical system-native
Interpreting resource impact in representative CPS telemetry sources, including Distributed Network Pro-
hardware classes tocol (DNP3) and Modbus communication events, Open
The reported CPU and memory overheads must be Platform Communications Unified Architecture (OPC
interpreted in relation to the heterogeneous hardware UA) process variables, and PLC execution traces, to
found in CPS deployments. While CROSS was evaluated enable deeper and more realistic evaluation in industrial
on general-purpose computing platforms, many CPS environments.
nodes, including PLCs, RTUs, and embedded protection
devices-operate with significantly constrained resources Limitations of OS‑level telemetry as a proxy for CPS insight
and rely on real-time firmware rather than a full OS While OS-level telemetry provides a valuable and uni-
stack. form abstraction for cross-platform anomaly detec-
The observed overheads (typically under X% CPU and tion, its suitability as a proxy for CPS-specific process
Y MB memory) are therefore most appropriate for CPS anomalies has inherent limitations. In many operational
components with an IT-oriented architecture, such as technology (OT) domains, faults manifest not in the
industrial edge gateways, substation automation servers, general-purpose operating system but within specialised

Johnphill et al. Cybersecurity (2026) 9:124 Page 22 of 24
embedded subsystems. Examples include ladder-logic routines operate locally, eliminating any dependency
deviations in programmable logic controllers (PLCs), on external cloud services. Collectively, these deploy-
timing faults detectable only on field-bus networks (for ment modes extend the applicability of CROSS to legacy,
example, Modbus, CAN, Profibus), or domain-specific safety-critical, and infrastructure-constrained cyber-
measurements observed within real-time controllers and physical system environments.
remote terminal units (RTUs). Key Contributions. To clearly summarise its nov-
Such anomalies may not propagate to the host operat- elty and impact, CROSS delivers the following core
ing system and therefore remain invisible to generic OS contributions:
logs. CROSS addresses this by treating OS-level signals
as a baseline source of behavioural deviation rather than • First cloud-native, cross-platform remediation frame-
a complete view of CPS health. This design enables broad work: Enables automated recovery across Android,
deployability but does not replace the need for specialised Linux, macOS, and Windows, triggered via machine
telemetry in safety- or mission-critical environments. learning-based log classification.
Future extensions could incorporate heterogeneous log • Integrated observability with remediation: Pro-
sources such as PLC execution traces, DNP3 traffic sum- metheus and Grafana integration allows real-time
maries, or OPC-UA telemetry, enabling a multi-layered inspection of errors, recovery events, and healing
view that unifies OS and control-layer anomalies. This metrics.
hybrid approach would enhance diagnostic richness, par- • Simulated fallback execution: Ensures continuity
ticularly for faults arising at the physical–digital bound- by simulating remediation steps when native tools
ary where OS-level signals alone are insufficient. (for example, ADB or PowerShell) are unavailable in
restricted environments.
Deployment considerations for real‑time, deterministic, • Modular and extensible architecture: A registry-
and air‑gapped CPS driven design allows easy addition of new platforms
Cyber-physical system deployments frequently oper- and remediation handlers without altering the core
ate under stringent constraints related to timing, deter- system.
minism, and connectivity. Systems such as industrial • Validated against baselines: Demonstrates superior
protection relays, aerospace control units, and medical MTTR, precision, and recall compared to manual
devices often enforce fixed execution cycles, bounded scripts and rule-based systems.
timing jitter, and, in some domains, strictly air-gapped
operational modes. The cloud-native design of CROSS
does not inherently require wide-area network connec- Conclusion and future work
tivity; instead, its components can be deployed entirely
Although CROSS integrates anomaly detection
on premises or within isolated edge clusters using light-
mechanisms that are applicable to cybersecurity
weight, locally managed Kubernetes container orches-
contexts, the present evaluation focuses primarily on
tration distributions, such as K3s, a compact Kubernetes
operational anomalies rather than explicit attack-
implementation designed for resource-constrained and
induced behaviours. As such, the cybersecurity
edge environments, and MicroK8s, a self-contained
contribution is framed as an architectural capabil-
Kubernetes platform optimised for local, offline, and
ity rather than an empirically benchmarked claim.
air-gapped deployments. These configurations preserve
Evaluating CROSS using intrusion-specific datasets
equivalent functionality to cloud-connected deployments
is identified as an important direction for future
while remaining compatible with security-sensitive CPS
work.
settings.
Real-time scheduling constraints are accommodated This study introduced CROSS, the Cross-platform
by executing anomaly detection and remediation tasks as Remediation and Observability Self-Healing System,
background processes with bounded resource footprints, as a novel framework for autonomous fault recovery in
thereby ensuring minimal interference with time-critical cyber-physical systems. Through lightweight log-based
control workloads. Where strict real-time determinism anomaly detection, containerised deployment using
is required, CROSS can be configured to execute reme- Docker, scalable orchestration via Kubernetes, and an
diation actions only within predefined safe execution observability layer powered by Prometheus and Grafana,
windows or to defer intrusive actions to higher-level CROSS achieves a balanced combination of adaptability,
supervisory nodes. In fully air-gapped environments, transparency, and performance. Unlike many existing
all telemetry storage, policy management, and inference self-healing solutions confined to specific platforms or

J ohnphill et al. Cybersecurity (2026) 9:124 Page 23 of 24
toolchains, CROSS dynamically adjusts its remediation Acknowledgements
The authors would like to acknowledge the support provided by the Cyber
logic to suit Android, Linux, macOS, and Windows envi-
Security Research Group (CSRG), Department of Computer Science, Notting-
ronments, maintaining operational continuity even in ham Trent University.
constrained or hybrid execution contexts.
Author contributions
Beyond its practical feasibility, CROSS makes a broader
Conceptualisation: O.J. and A.S.S.; Methodology: O.J.; Software: O.J.; Validation:
research contribution by bridging theoretical models of O.J., A.S.S., and O.K.; Analysis: O.J. and A.S.S.; Resources: A.S.S., O.K., and M.A.;
fault tolerance with deployable, real-world self-healing Data curation: O.J.; Writing - original draft: O.J.; Writing - review and editing:
O.J., A.S.S., O.K., and M.A.; Visualisation: O.J.; Supervision: A.S.S. and O.K. All
mechanisms. It executes corrective actions autonomously
authors read and approved the final manuscript.
while emitting verifiable telemetry, thereby strengthening
both system resilience and auditability. The framework Funding
This research received no external funding.
demonstrates that explainable log-driven learning can
underpin secure, cross-platform self-healing architec- Data availability
tures suitable for industrial CPS domains such as smart The source code of the CROSS framework is openly available on GitHub ([30]):
https:// github. com/ obinn ajohn phill/ self- heali ng- remed ial- actio ns (accessed
grids, healthcare monitoring, and intelligent transport.
on 19 April 2025). The preprocessed dataset, including raw logs, extracted
features, and processed data derived from the publicly available Loghub
Integrated roadmap for future work repository curated by LOGPAI ([26, 27]), is available on Zenodo ([28]): https://
doi. org/ 10. 5281/ zenodo. 15249 598 (accessed on 19 April 2025).
Future research will extend CROSS along several comple-
mentary directions:
Declarations
• Adversarial Robustness and Security Context: Incor- Ethics approval
porate adversarial training and ensemble detection Not applicable.
to resist evasion and poisoning attacks targeting log-
Consent for publication
based classifiers, enabling the framework to distin- Not applicable.
guish operational faults from malicious anomalies.
Competing interests
• Reinforcement-Learning-Driven Remediation: Model
The authors declare that they have no Competing interests.
remediation as a Markov Decision Process (MDP)
where adaptive policies learn optimal corrective
Received: 6 November 2025 Accepted: 11 January 2026
actions from feedback, balancing availability with
security risk.
• Predictive and Time-Series Analytics: Employ super-
vised and temporal learning models for proactive
References
fault prediction and pre-emptive remediation before Akinbolaji TJ, Nzeako G, Akokodaripon D, Aderoju AV (2024) Proactive monitor-
service degradation occurs. ing and security in cloud infrastructure: leveraging tools like prometheus,
grafana, and hashicorp vault. World J Adv Eng Technol Sci 13(2):74–89
• Secure and Auditable Execution: Introduce sand-
Ali T, Iqbal R, Ansari NM, Tariq T, Rafique AA (2025) Ai-powered anomaly detec-
boxed or privilege-restricted healing agents and tion in software logs: a machine learning approach for proactive fault
explore blockchain-based audit trails to enhance diagnosis and self-healing systems. Spectr Eng Sci 3(3):302–322
Arefifar SA, Alam MS, Hamadi A (2023) A review on self-healing in mod-
the trustworthiness and verifiability of remediation
ern power distribution systems. J Mod Power Syst Clean Energy
actions. 11(6):1719–1733
• Edge-Cloud Hybrid Architecture: Distribute detection Cheng Y, Zhang W, Shen H, Tang C (2023) AI for IT operations (AIOps) on cloud
platforms: reviews, opportunities and challenges
and remediation across computing tiers, latency-sen-
Cloud native computing foundation: CNCF. Accessed 2 Jan 2025 (2025).
sitive operations at the edge and orchestration in the https:// www. cncf. io/
cloud, to support large-scale CPS deployments. Georgiou MA, Paphitis A, Sirivianos M, Herodotou H (2019) Towards auto-
scaling existing transactional databases with strong consistency. In: Proc.
• Human-in-the-Loop Interfaces: Develop operator
IEEE 35th ICDE Workshops (ICDEW), pp. 107–112
dashboards that allow manual override, validation, Hallur J (2022) From monitoring to observability: enhancing system reliability
and contextual decision support, blending autonomy and team productivity. Int J Sci Res(IJSR) 13(10):602–606
He P, Zhu J, Zheng S, Li Z, Lyu MR (2023) Loghub: a large collection of system
with expert insight.
log datasets for ai-driven log analytics. In: Proc. IEEE ISSRE, pp. 1–11 IEEE.
https:// github. com/ logpai/ loghub
These directions aim to evolve CROSS from an opera- Jhuang C, Wu Q (2022) Container-based voip failover design on kubernetes
overlay networks. In: Proc. CSCI, pp. 1317–1322
tionally self-healing engine into a fully cyber-resilient,
Johnphill O, Sadiq AS, Kaiwartya O (2024) Preprocessed log dataset for cross-
explainable, and trustworthy ecosystem for heterogene- platform remedial actions in cyber-physical systems. https:// doi. org/ 10.
ous CPS. The framework thus establishes a foundation 5281/ zenodo. 152495 98
Johnphill O, Sadiq AS, Kaiwartya O, Aljaidi M (2024) An intelligent approach
for scalable, intelligent, and transparent self-healing
to automated operating systems log analysis for enhanced security.
infrastructures across both IT and OT domains. Information 15:657

Johnphill et al. Cybersecurity (2026) 9:124 Page 24 of 24
Johnphill O, Sadiq AS, Pillai P, Taheir MA, Kaiwartya O (2023) Self-healing in
cyber-physical systems using machine learning: a critical analysis of
theories and tools. Futur Internet 15(7):244
LOGPAI: Loghub: a large collection of system log datasets for AI-driven log
analytics (2023). https:// github. com/ logpai/ loghub
Loh R, Thing VLL (2023) Enhancing cyber-resilience in self-healing cyber-
physical systems with implicit guarantees. In: Proc. IEEE International
Conference on Cyber Security and Resilience (CSR), pp. 359–366
Malhotra A, Elsayed A, Torres R, Venkatraman S (2023) Evaluate solutions for
achieving high availability or near zero downtime for cloud native enter-
prise applications. IEEE Access 11:85384–85394
Marinho CSS, Moreira LO, Coutinho EF, Costa Filho JS, Sousa FRC, Machado JC
(2018) Labareda: a predictive and elastic load balancing service for cloud-
replicated databases. J Inf Data Manag 9(1):94–106
Naqvi S, Ahmed T, Ullah M (2022) On evaluating self-adaptive and self-healing
systems using chaos engineering. In: Proc. IEEE international conference
on autonomic computing and self-organizing systems (ACSOS), pp. 1–10
Nugroho MA, Abdurohman M, Erfianto B (2023) Increasing automatic proctor-
ing system performance using distributed round-robin load balancer. In:
Proc. IEEE IAICT, pp. 377–382
Pai K, Srinivas BK (2024) Enhanced visibility for real-time monitoring and alert-
ing in kubernetes by integrating prometheus, grafana, loki, and alerta. Int
J Sci Res Eng Manag IJSREM 8(6):1–5
Pakrijauskas K, Mazeika D (2022) Investigation of stateful microservice avail-
ability during failover. In: Proc. 8th International Conference on Control,
Decision and Information Technologies (CoDIT), pp. 286–290
Shabariram CP, Vrinda S, Srivastan S, Manimeghalai R (2024) Case study based
investigation on self-healing cloud deployments for edge-based software
development. In: Proc. ICSSEECC, pp. 85–90
Siddiqui I, Pandey A, Jain S, Kothadia H, Agrawal R, Chankhore N (2023) Com-
prehensive monitoring and observability with jenkins and grafana. In:
Proc. ISMSIT, pp. 1–5
Vervaet A (2021) Monilog: An automated log-based anomaly detection system
for cloud computing infrastructures. In: Proc. IEEE 37th international
conference on data engineering (ICDE), pp. 2739–2743
Wang Y, Xu Y, He J, Liu C, Schneider KP, Hong M, Ton DT (2019) Coordinating
multiple sources for service restoration to enhance resilience of distribu-
tion systems. IEEE Trans Smart Grid 10(5):5781–5793
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.