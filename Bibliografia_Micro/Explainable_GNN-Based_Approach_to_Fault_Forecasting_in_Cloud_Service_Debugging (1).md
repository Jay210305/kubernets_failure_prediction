5640 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
Explainable GNN-Based Approach to Fault
Forecasting in Cloud Service Debugging
Dániel Unyi , Erno˝ Rigó , Bálint Gyires-Tóth , and Róbert Lovas
Abstract—Debugging cloud services is increasingly challeng- microservices. One of the greatest challenges in debugging is
ing due to their distributed, dynamic, and scalable nature. not just detecting failures, but understanding why they occur
Traditionalmethodsstruggletohandlelargestatespacesandthe
and which components are responsible. Debugging tools must
complex interactions between microservices, making it difficult
move beyond simple anomaly detection and provide inter-
todiagnosefailuresandidentifycriticalcomponents.Thispaper
presents a Graph Neural Network (GNN)-based approach that pretable insights that highlight the root causes of failures and
enhancescloudservicedebuggingbypredictingsystem-levelfault the most influential microservices affecting system reliability.
probabilities and providing interpretable insights into failure To ensure high availability and reliability, there is a critical
propagation. Our method models microservice interactions as
needforexplainablemethodsthatanalyze,predict,andclarify
graphs,wherefailurespropagateprobabilistically.UsingMarkov
cloudservicebehavior.Tobridgethisgap,ourworkintegrates
Decision Processes (MDPs), we simulate failure behaviors,
capturing the probabilistic dependencies that influence system failure propagation modeling with GNN-based explainability,
reliability.ThetrainedGNNnotonlypredictsfaultprobabilities which allows both fault probability estimation and critical
but also identifies the most failure-prone microservices and component identification within service meshes.
explains their impact. We evaluate our approach on various ser-
vicemeshstructures,includingfeature-enriched,tree-structured,
and general directed acyclic graph (DAG) architectures. Results
A. Cloud Computing With Reference Architecture and
indicate that our method is effective in the operational phase
of cloud services, enabling proactive debugging and targeted Service Mesh Concepts
optimization. This work represents a step toward more inter-
Cloud computing has transformed modern application
pretable, reliable, and maintainable cloud infrastructures.
architectures by enabling scalable, on-demand resource pro-
IndexTerms—Cloudcomputing,softwaredebugging,microser- visioning over the Internet. As cloud-native applications
vice architectures, deep learning, graph neural networks,
continue to expand, microservices architectures [1] have
explainable AI, fault prediction.
become the de facto standard for ensuring scalability, avail-
ability, and manageability. However, the heterogeneous and
distributed nature of microservices introduces challenges such
I. INTRODUCTION as efficient orchestration, secure communication, and observ-
CLOUD computing’s distributed, dynamic, and scalable ability. Managing these interactions becomes particularly
nature makes debugging cloud services increasingly difficult as the number of microservices grows, increasing
complex.Traditionaldebugging,monitoring,andtroubleshoot- the complexity of debugging and performance monitoring. To
ing methods struggle to capture the dependencies between address these issues, the service mesh paradigm has emerged
as a key solution.
Received 21 November 2024; revised 2 April 2025 and 21 June 2025; A service mesh is a dedicated infrastructure layer that
accepted20July2025.Dateofpublication25August2025;dateofcurrent
managesservice-to-servicecommunication,ensuringtranspar-
version 5 December 2025. The work reported in this paper, carried out
as a collaboration between HUN-REN SZTAKI and BME, has been partly ent, reliable, and secure interactions between microservices.
supported by the European Union project RRF-2.3.1-21-2022-00004 within It facilitates load balancing, service discovery, traffic manage-
the framework of the Artificial Intelligence National Laboratory. This work
ment, failure recovery, and monitoring, significantly reducing
waspartiallyfundedbytheNationalResearch,DevelopmentandInnovation
Office(NKFIH)underOTKAGrantAgreementNo.K132838.Thepresented the overhead associated with microservices orchestration. By
work of Róbert Lovas was also supported by the János Bolyai Research decouplingservicecommunicationfromapplicationlogic,ser-
Scholarship of the Hungarian Academy of Sciences. The associate editor
vice meshes simplify infrastructure management and enhance
coordinating the review of this article and approving it for publication was
F.Paganelli.(BálintGyires-TóthandRóbertLovascontributedequallytothis observability.Complementingthis,referencearchitectures[2],
work.)(Correspondingauthor:BálintGyires-Tóth.) [3], [4], [5], [6] serve as standardized blueprints for cloud
Dániel Unyi and Bálint Gyires-Tóth are with the Department of
service design, incorporating best practices, interoperabil-
Telecommunications and Artificial Intelligence, Faculty of Electrical
Engineering and Informatics, Budapest University of Technology and ity guidelines, and reliability principles to improve system
Economics, 1111 Budapest, Hungary (e-mail: unyi.daniel@tmit.bme.hu; resilience.
toth.b@tmit.bme.hu).
Leading service mesh implementations–Istio, Linkerd, and
Erno˝ Rigó and Róbert Lovas are with the Institute for Computer
Science and Control (SZTAKI), Hungarian Research Network (HUN- AWSAppMesh[7]–integratereferencearchitectureprinciples
REN), 1111 Budapest, Hungary, and also with the John von Neumann to facilitate microservice communication and management.
Faculty of Informatics, Óbuda University, 1034 Budapest, Hungary (e-mail:
For example, Istio provides advanced traffic management,
erno.rigo@sztaki.hun-ren.hu;robert.lovas@sztaki.hun-ren.hu).
DigitalObjectIdentifier10.1109/TNSM.2025.3602223 security policies, and telemetry collection, establishing a
(cid:2)c 2025TheAuthors. ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5641
Fig.1. Classificationofgeneraldistributeddebuggingmethodologies[8]extendedwithourplannedresultsinservicemeshenvironment(greybackground).
strong foundation for operational control and observability. instances, where failures may only manifest intermittently or
However, while these tools enhance visibility into service under specific operating conditions.
interactions, analyzing failure propagation across microser- Additionally, failures in service meshes are often difficult
vices remains a challenge, requiring additional techniques to to reproduce, making root cause analysis highly reactive
assess system reliability and performance. rather than proactive. Without effective replay mechanisms,
In summary, service meshes and reference architectures debugging relies on post-mortem analysis, where engineers
improve operational efficiency, security, and observability, must manually analyze logs and traces, often with limited
but effectively analyzing service behavior still requires addi- visibility into how failures emerged. This lack of systematic
tional tools that can track dependencies and evaluate system failure reproduction hinders efforts to anticipate and mitigate
performance under failure conditions. faults before they escalate.
B. Debugging Challenges C. Theoretical Background and Research Plan
Debugging service mesh architectures can be challenging Distributed debugging methodologies can be classified
due to their complexity and distributed nature [9]. A primary based on their support for global predicate specification and
issueisobservability,whichreferstoanalyzingsystembehav- detection, as well as their ability to identify root causes of
ior and inter-service communication. In practice, only partial software bugs in distributed systems [8]. Over time, these
observability is often possible due to factors such as closed- methodologies have evolved to address the limitations of
box (proprietary) services or probe effects, where monitoring previous approaches. Figure 1 summarizes these methods and
tools can influence system behavior. This incomplete view highlights our planned contributions in service mesh environ-
makes it difficult to determine which microservices contribute ments (grey background).
most to system failures and how faults propagate through the At the most basic level, interactive debugging extends
mesh. traditionalsequentialdebuggingtoremoteprocesses,allowing
Beyond observability, identifying and diagnosing faults real-time monitoring but lacking insight into inter-process
in large-scale service meshes is particularly challenging. interactions, making it unsuitable for distributed systems. To
Configuration errors, misrouted traffic, and performance bot- overcome this, the “Trace, replay and debugging” approach
tlenecks can cause latency spikes, service degradation, and (Figure 1, row 2) records selected execution traces to enable
system faults [10]. However, tracing these issues back to their deterministicreproductionoffaultybehaviorsundercontrolled
rootcauseisdifficultbecauseservicemeshesabstractcommu- conditions.
nication details, making failure propagation paths non-trivial Building on this, the “Integrated testing, active control
to reconstruct. Debugging inter-service failures is further anddebugging”(Figure 1,row3)introducesmechanismsthat
complicated by dynamic workloads and ephemeral service steerexecutionalongpredefinedcomputationpaths,improving

5642 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
Fig.2. Proposedframeworkfordebuggingcyclewithtoolsanddataflow.
reproducibility beyond passive observation. A more advanced method uses observed data to improve fault localization and
technique,“Predicatedetection,activecontrolanddebugging” guide debugging efforts.
(Figure 1,row4),allowsuserstodefinecorrectnessconditions Our approach builds on the service mesh paradigm, which
(predicates) that are continuously evaluated during execution, providesastructured,policy-drivenenvironmentformanaging
enhancing systematic failure detection. microservices.Servicemeshdescriptors,suchasthoseinIstio,
One of our previous works extended this methodology to define critical configurations for network traffic management
the deployment phase of orchestrated cloud services [11], (e.g., routing rules, load balancing), security policies (e.g.,
focusingonimprovingreliability(includingplatform-agnostic authentication, authorization), and observability features (e.g.,
behavior) in complex deployment strategies. This approach telemetry, logging). These descriptors allow fine-grained con-
proved useful in detecting timing or architecture-dependent troloverservicebehaviorwithoutmodifyingapplicationcode,
failures within deployment descriptions and orchestration makingthemanidealfoundationforourdebuggingframework
| steps. |     |     |     | (Figure | 2, “Service | Mesh Description”). |     |     |     |
| ------ | --- | --- | --- | ------- | ----------- | ------------------- | --- | --- | --- |
This research further narrows the scope to developing The “Predicate detection, active control, and debugging”
a smart steering mechanism within the “Smart Control, approach is embedded within the “Steering”-related compo-
Debugging, and Evaluation” paradigm (Figure 1, row 5). In nents of our framework (gray route in Figure 2). The ‘PRISM
ourpreviouswork[12],weappliedthePRISMsimulatorenvi- simulator environment with model checker’ detects suspicious
ronment with model checker, along with autoencoders, Long paths or nodes and labels them to steer debugging efforts
Short-Term Memory (LSTM) networks, and Graph Neural towardcriticalareas.Inourpreviouswork[12],wedeveloped
Networks (GNNs), to analyze system behavior. Extending asimplifiedservicemeshmodel,representingRESTfulservice
beyond this, in this paper we focus on leveraging GNNs for nodes as a dependency tree. This was extended into a REST
fault prediction and explainability to enhance debugging in modeling framework using a domain-specific language (DSL)
cloud service meshes. to define probabilistic service interactions, allowing the gen-
|     |     |     |     | eration of  | probabilistic | state       | machines for | each microservice |        |
| --- | --- | --- | --- | ----------- | ------------- | ----------- | ------------ | ----------------- | ------ |
|     |     |     |     | based on    | its strategy  | and network | connections. | Our               | PRISM- |
|     |     |     |     | based model | generator     | translates  | these DSL    | descriptions      | into   |
D. Proposed Debugging Framework Markov Decision Processes (MDPs) by generating module
|            |                  |                |            | descriptions | in PRISM | for all | nodes and their | dependencies. |     |
| ---------- | ---------------- | -------------- | ---------- | ------------ | -------- | ------- | --------------- | ------------- | --- |
| This paper | shifts the focus | from debugging | during the |              |          |         |                 |               |     |
deployment phase to debugging during operation, where Once validated, RESTful communication flows of arbitrary
failures often arise due to dynamic interactions between lengthcanbesimulated.Additionally,PRISMperformsformal
microservices. Our approach introduces explainability into verification, ensuring the model satisfies specified correctness
debugging, using Graph Neural Networks (GNNs) to not only properties using probabilistic model checking. This allows
|                      |                     |          |            | us to define | temporal | logic | properties and | systematically |     |
| -------------------- | ------------------- | -------- | ---------- | ------------ | -------- | ----- | -------------- | -------------- | --- |
| predict system-level | fault probabilities | but also | to provide |              |          |       |                |                |     |
interpretable insights into failure propagation and root causes analyze failure cases, identifying deadlocks, inconsistencies,
(see black route in Figure 2). Unlike deterministic replay- andfailureprobabilities[13](see‘Generated&labeledtraces’
| baseddebugging,whichreliesonreplicatingfailurestates,our |     |     |     | in Fig. 2). |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5643
In this paper, we propose a debugging framework that techniques. These studies highlight the importance of formal
integrates Graph Neural Networks (GNNs) within the methods in ensuring the robustness of RESTful systems.
‘Training’-related components (white route in Figure 2). Our Although formal methods provide strong guarantees, their
approach (see Section IV) addresses the challenge of debug- applicability to large-scale, dynamic service meshes is limited
ging complex service meshes by leveraging fault probability due to computational cost and reliance on predefined models.
prediction and GNN-based explainability to identify weak Inordertoaddresstheselimitations,data-drivenfaultdetection
components (see Section IV-C). Instead of relying solely on methods have emerged, using statistical analysis and machine
deterministicreplayorexhaustivemodelchecking,ourmethod learningtoimprovefaultdiagnosisandprediction.Thefollow-
learns from observed system behavior to prioritize high-risk ing subsections discuss both traditional and ML-based fault
execution paths and potential failure states. Key components detection approaches, with a particular focus on GNN-based
| include:      |       |         |            |              |               |       |           | methods        | for service | meshes.         |     |          |     |      |              |
| ------------- | ----- | ------- | ---------- | ------------ | ------------- | ----- | --------- | -------------- | ----------- | --------------- | --- | -------- | --- | ---- | ------------ |
| • Training    |       | a GNN   | to predict | system-level |               | fault | probabil- |                |             |                 |     |          |     |      |              |
| ities,        | using | service | mesh       | graphs       | where         | nodes | represent |                |             |                 |     |          |     |      |              |
|               |       |         |            |              |               |       |           | A. Traditional |             | Fault Detection |     | Methods  |     |      |              |
| microservices |       | and     | edges      | capture      | inter-service |       | interac-  |                |             |                 |     |          |     |      |              |
|               |       |         |            |              |               |       |           | Rule-based     |             | fault detection |     | methods, |     | such | as intrusion |
tions.
|     |     |     |     |     |     |     |     | and anomaly |     | detection | systems, | monitor |     | network | or host |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | -------- | ------- | --- | ------- | ------- |
• GNN-basedexplainabilitytoidentifycriticalcomponents,
|           |            |           |           |             |     |          |           | activity   | for deviations |           | from            | expected         | behavior |            | [19]. These |
| --------- | ---------- | --------- | --------- | ----------- | --- | -------- | --------- | ---------- | -------------- | --------- | --------------- | ---------------- | -------- | ---------- | ----------- |
| selecting |            | a minimal | but       | informative |     | subgraph | that pre- |            |                |           |                 |                  |          |            |             |
|           |            |           |           |             |     |          |           | methods    | rely           | on either | signature-based |                  |          | detection, | using       |
| serves    | predictive |           | accuracy. |             |     |          |           |            |                |           |                 |                  |          |            |             |
|           |            |           |           |             |     |          |           | predefined | anomaly        | patterns, |                 | or anomaly-based |          |            | detection,  |
•
| Automated |     | generation, |     | augmentation, |     | and | labeling of |     |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
identifyingstatisticaldeviationsfromnormalsystembehavior.
| training     | data        | using                                | the PRISM   |           | simulator/model |             | checker,      |                   |            |                |            |             |            |               |               |
| ------------ | ----------- | ------------------------------------ | ----------- | --------- | --------------- | ----------- | ------------- | ----------------- | ---------- | -------------- | ---------- | ----------- | ---------- | ------------- | ------------- |
|              |             |                                      |             |           |                 |             |               | Abbasi            | et al.     | [20] propose   | an         | anomaly     | detection  |               | system for    |
| whichallows  |             | theGNNtolearnfromprobabilisticexecu- |             |           |                 |             |               |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | cloud data        | centers    | that           | enhances   | fault       | resilience | through       | real-         |
| tion         | traces      | (white                               | route       | in Figure | 2, see          | also        | Section III). |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | time monitoring   |            | and behavioral |            | analysis.   |            |               |               |
| • Combining  |             | Markov                               | Decision    |           | Process         | (MDP)       | modeling      |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | Beyond            | anomaly    |                | detection, |             | automated  | testing       | and           |
| with         | GNN-based   |                                      | learning,   | where     | MDPs            | encode      | service       |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | resilience        | strategies | have           | been       | explored    | for        | service       | meshes.       |
| interaction  |             | dynamics,                            | and         | GNNs      | refine          | failure     | prediction    |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | Karn et           | al.        | [21] introduce |            | a framework |            | that          | monitors      |
| and          | debugging   |                                      | automation. |           |                 |             |               |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | microservice      |            | communication  |            | traces,     |            | using         | component     |
| The          | suspicious  | situations                           |             | detected  | by              | pre-trained | GNNs          |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | fault injectors   |            | to simulate    | delays,    |             | traffic    | restrictions, | and           |
| may realize  | ‘Smart      | steering’                            |             | (black    | route in        | Figure      | 2), allow-    |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | terminations.     |            | Their approach |            | detects     | faulty     | connections   | via           |
| ing cloud    | debugging   |                                      | tools [11], | [14]      | to proactively  |             | identify      |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | dashboards        | and        | mitigates      | issues     | through     | scaling,   |               | failover, and |
| and localize | failures.   |                                      | This        | process   | can bypass      |             | the PRISM     |                   |            |                |            |             |            |               |               |
|              |             |                                      |             |           |                 |             |               | circuit breakers, |            | offering       | a reactive |             | mechanism  |               | for service   |
| simulator    | environment |                                      | and         | model     | checker,        | as          | the trained   |                   |            |                |            |             |            |               |               |
reliability.
| GNN can           | directly |         | analyze       | service        | mesh  | descriptions. | Our          |                |          |                     |     |      |         |      |            |
| ----------------- | -------- | ------- | ------------- | -------------- | ----- | ------------- | ------------ | -------------- | -------- | ------------------- | --- | ---- | ------- | ---- | ---------- |
|                   |          |         |               |                |       |               |              | Formal         | modeling | techniques          |     | have | also    | been | applied to |
| experimental      |          | results | (see Sections |                | V and | VI)           | demonstrate  |                |          |                     |     |      |         |      |            |
|                   |          |         |               |                |       |               |              | fault analysis | in       | cloud environments. |     |      | Cao and | Niu  | [22] apply |
| the effectiveness |          | of      | GNN-based     | explainability |       |               | in detecting |                |          |                     |     |      |         |      |            |
higher-orderMarkovgraphstoanalyzeclouddeploymentsand
| critical | components |     | and operating | under | limited |     | observability |          |       |             |         |         |     |           |          |
| -------- | ---------- | --- | ------------- | ----- | ------- | --- | ------------- | -------- | ----- | ----------- | ------- | ------- | --- | --------- | -------- |
|          |            |     |               |       |         |     |               | big data | logs, | identifying | complex | failure |     | patterns. | However, |
conditions.
|     |     |     |     |     |     |     |     | their approach |         | lacks an | active   | control | mechanism |     | to steer the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | -------- | ------- | --------- | --- | ------------ |
|     |     |     |     |     |     |     |     | debugging      | process | toward   | critical | failure | states.   |     |              |
Pontilloetal.[23]proposeFERRARI,afailurereproduction
|     |     | II. | RELATEDWORKS |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toolthatgeneratestestcasesandanalyzesstacktracestoiden-
| With | the | increasing | complexity |     | of  | cloud | architec- |     |     |     |     |     |     |     |     |
| ---- | --- | ---------- | ---------- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tifyfaults.FERRARIincludesasimilarityscoringmechanism
| tures, maintaining |     | system | stability |     | and fault | detection | has |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | --------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toestimatehowcloselygeneratedtestcasesmatchrealfailure
| become | a critical | challenge. |     | Continuous | monitoring |     | collects |     |     |     |     |     |     |     |     |
| ------ | ---------- | ---------- | --- | ---------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
conditions.Whiletheirtoolaidsinfailurereproduction,itdoes
| logs on | memory | issues, | server |     | failures, | and | application |                 |     |           |          |     |           |       |     |
| ------- | ------ | ------- | ------ | --- | --------- | --- | ----------- | --------------- | --- | --------- | -------- | --- | --------- | ----- | --- |
|         |        |         |        |     |           |     |             | not incorporate |     | ML-guided | steering |     | as in our | work. |     |
performance[15],butthevastvolumeoflogsmakesitdifficult
| to promptly | isolate  | faults | and       | take    | proactive | measures | before        |            |          |       |       |           |     |         |     |
| ----------- | -------- | ------ | --------- | ------- | --------- | -------- | ------------- | ---------- | -------- | ----- | ----- | --------- | --- | ------- | --- |
|             |          |        |           |         |           |          |               | B. Machine | Learning | Based | Fault | Detection |     | Methods |     |
| system      | failures | occur. | Moreover, | failure | datasets  |          | are typically |            |          |       |       |           |     |         |     |
muchsmallerthancompletesystemlogs,makingfaultanalysis Machine learning-based fault detection methods generally
challenging. fall into supervised and unsupervised categories. Supervised
Farooq et al. define faults as abnormal conditions that models learn to distinguish between normal and faulty behav-
reduceoreliminateacomponent’sabilitytofunctioncorrectly, ior using labeled input-output pairs, making them effective
with failures emerging as their observable consequences [16]. when labeled data is available. In contrast, unsupervised
Identifying root causes before failures manifest is crucial for approaches detect anomalies by identifying deviations from
proactive debugging. normalpatternswithoutrequiringexplicitfaultlabels,allowing
Traditional formal verification methods have been applied them to adapt to previously unseen failure modes.
to analyze cloud architectures, particularly in service-oriented Zhang et al. [24] propose an online fault detection
environments. Zatout et al. [17] propose transaction modeling model for cloud systems using a support vector machine
for improving reliability in RESTful applications, while (SVM) with automated parameter tuning (SVM-Grid). Their
Souri et al. [18] review service composition verification approach improves fault prediction by selecting relevant

5644 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
TABLEI
COMPARISONOFSELECTEDRELATEDWORKS.(ML:MACHINELEARNING)
system attributes via Pearson correlation and principal com- context-based (graph-based) data representations. Their study
ponent analysis (PCA). While effective, it focuses on general demonstrates that graph-based representations significantly
cloud fault detection and does not explicitly model inter- enhance prediction accuracy by capturing the associativity of
service dependencies within service meshes. clientsandintegratingthemwithtraditionalmodels.However,
Zhou et al. [25] introduce MEPFL, a machine learning- their approach is concerned with SLA violations rather than
based method for latent error prediction and fault localization analyzingfailurepropagationoridentifyingstructurallycritical
in microservice applications. It leverages system trace logs to components in cloud services.
trainmodelsatboththetraceandmicroservicelevels,allowing Wu et al. [29] introduces MicroRCA, an attributed graph
real-time fault detection and classification. By analyzing exe- model to trace anomaly propagation across services and
cution traces and incorporating fault injection during training, machines in microservice architectures. It performs real-time
MEPFL improves failure diagnosis in dynamic production root cause localization by correlating application performance
environments. However, it primarily focuses on predicting symptomswithsystemresourceutilization.Whileeffectivefor
fault occurrences rather than modeling how failures propagate diagnosingperformanceissues,itsprimaryfocusisonlinking
within a service mesh. performance anomalies to resource bottlenecks, making it
Meng et al. [26] present a reinforcement learning approach complementary to our work.
to predict fault resilience behaviors in service meshes. Wang et al. [30] applies hierarchical graph neural networks
Their method optimizes service-level configurations that to discover intra-network and cross-network causal depen-
influence request-response behavior under failure conditions, dencies for fault localization. It combines topological causal
which enables adaptive fault resilience strategies across both discoverywithanExtremeValueTheory(EVT)-basedmethod
individual services and multi-service orchestrations. While to rank probable root causes. This approach is well-suited
effective for mitigating faults, this approach emphasizes pol- for analyzing multi-level causal interactions but does not
icy optimization rather than failure probability estimation or explicitly account for the role of service dependencies in fault
interpretable fault propagation modeling. propagation.
Rouf et al. [27] propose InstantOps, a multi-modal failure Gan et al. [31] introduce a trace-based root cause anal-
prediction and root cause analysis (RCA) framework that ysis system, Sleuth, for large-scale microservices, using an
integrates logs, metrics, traces, and microservices events. It unsupervised GNN to assess the causal impact of each span
constructs a dynamic service call flow graph, where traces in a trace. It clusters traces using a trace distance metric to
define the structure, while logs and resource metrics enrich reduce the data volume required for root cause localization,
node attributes. InstantOps applies GNNs to capture spatial with a strong emphasis on transferability across microservice
dependencies and Gated Recurrent Units (GRUs) to model applications.WhileSleuthfocusesonperformancedebugging,
temporal failure patterns, enabling proactive failure prediction our work provides a complementary perspective by learning
and precise root cause localization. Moreover, permutation an explicit failure propagation model and identifying critical
testingisusedtoassessnodeimportancewithinfailurepropa- subgraphs responsible for system faults.
gation chains. While InstantOps effectively fuses multi-modal Table Iprovides acomparative overview of selected related
observabilitydataandmodelsbothspatialandtemporalfailure worksaccordingto(i)thearchitecturalleveltheytarget,(ii)the
dynamics, it differs from our work, which explicitly learns overallapproachtheyapply,(iii)theprimarymethodsapplied,
a failure propagation model to identify critical subgraphs (iv) their main focus areas, and (v) the strategy used for fault
contributing to system faults. injection. This comparative analysis is partially informed by
the survey presented in [32].
Our previous work [12] introduced a preliminary GNN-
C. Graph Neural Network Based Fault Detection based fault prediction model for service meshes, leveraging
Maroudis et al. [28] investigate SLA violation prediction a simplified RESTful service model with a dependency tree
using GNNs, exploring time series, content-based, and structure. This model was integrated with a domain-specific

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5645
language (DSL) to define probabilistic service interactions, end-users these disruptions result in performance degradation
enablingthegenerationofprobabilisticstatemachinesforeach or - in severe cases - functional or data losses.
microservice.Faultpropagationdynamicswerecapturedusing Measurement efforts of cloud application quality aims to
Markov Decision Processes (MDPs), and the framework was quantify these properties. In cases of formal service agree-
validated using formal verification techniques. Even though ments, these quantitative metrics play a key role. Thresholds
thispreliminaryworkdemonstratedtheapplicabilityofGNNs for these metrics, including the acceptable rate of system
for failure prediction, it was limited to tree structured service faults are often established in a Service Level Agreement
meshes and lacked a dedicated explainability mechanism for (SLA) between the cloud service provider and the end-user.
identifying the most critical service components contributing This kind of service measurement was first employed in IP
to failures. networks [34]. The concept then was widely adopted by
Building on this foundation, our current work generalizes various sectors, including cloud applications [35].
the approach by extending the tree-structured service mesh Although transient errors or permanent disruptions that
model to feature-enriched, directed acyclic graph (DAG) ser- result in a performance degradation might play a major role
vice meshes. Unlike the earlier model, the new one supports in overall debugging of a cloud application, for the time of
node-level features such as failure probability (for leaf nodes) current research we are focusing on fatal service situations.
andretrycount(forintermediarynodes).Theseenhancements For this purpose service level is defined as the probability of
offeramorerealisticrepresentationofserviceinteractionsand fatal service disruption (system fault) observed by the end-
failure dependencies. user. Contrary to the common practice of representing service
Our updated approach integrates GNN-based explainability availabilityasthepercentageratioofacceptablemetricsvalues
to identify critical subgraphs and failure-prone microservices. over time (e.g., requests are answered 99.995% within a
Theidentifiedcriticalsubgraphsprovidehintsforactivesteer- specific period of time), we are representing fatal system
ing of a cloud debugger tool towards the suspicious situations disruption probability value (or in short, fault) as a standard
(component faults), allowing proactive fault localization and probability value (e.g., requests are failing with a probability
| mitigation. |                                |                        |     |     |     |     | of 0.005   | in the | observed      | simulation | window). |     |     |     |
| ----------- | ------------------------------ | ---------------------- | --- | --- | --- | --- | ---------- | ------ | ------------- | ---------- | -------- | --- | --- | --- |
| III.        | MODELLINGSERVICEMESHESFORCLOUD |                        |     |     |     |     |            |        |               |            |          |     |     |     |
|             |                                | REFERENCEARCHITECTURES |     |     |     |     | C. Service | Mesh   | Architectures |            |          |     |     |     |
A. Framework In order to generalize and refine our models further lever-
Current modelling efforts build upon our previous work aging on our previous achievements [12], we continued to
|          |                  |     |                |     |               |     | investigate | various | methods | of  | describing | cloud | use | cases. |
| -------- | ---------------- | --- | -------------- | --- | ------------- | --- | ----------- | ------- | ------- | --- | ---------- | ----- | --- | ------ |
| focusing | on probabilistic |     | model checking |     | applications, |     | more        |         |         |     |            |       |     |        |
specifically the PRISM model checker [13] is employed to Microservice-based architecture patterns, also known as ser-
|           |          |              |          |     |        |           | vice meshes,       | are | becoming | increasingly |     | popular | in modern |     |
| --------- | -------- | ------------ | -------- | --- | ------ | --------- | ------------------ | --- | -------- | ------------ | --- | ------- | --------- | --- |
| describe, | simulate | and formally | validate |     | models | expressed | as                 |     |          |              |     |         |           |     |
|           |          |              |          |     |        |           | cloud applications |     | [7].     |              |     |         |           |     |
| Markov    | decision | processes    | (MDPs).  |     |        |           |                    |     |          |              |     |         |           |     |
During further developments of the model, the PRISM Cloud applications were chosen to be modelled as a set
|          |         |           |          |             |     |            | of loosely | coupled | Web | services. | Intra-application |     | integration |     |
| -------- | ------- | --------- | -------- | ----------- | --- | ---------- | ---------- | ------- | --- | --------- | ----------------- | --- | ----------- | --- |
| language | is used | to define | parallel | composition |     | of modules |            |         |     |           |                   |     |             |     |
describing various behavioural patterns in different cloud is achieved by applying various services of the mesh service
application modules. These patterns are composed of vari- component. From these integration services, message inter-
|                   |     |         |      |         |                    |     | ception | and routing | is observed |     | to be most | feasible | to  | aid in |
| ----------------- | --- | ------- | ---- | ------- | ------------------ | --- | ------- | ----------- | ----------- | --- | ---------- | -------- | --- | ------ |
| ous communication |     | actions | also | serving | as synchronization |     |         |             |             |     |            |          |     |        |
points between the modules. Critical model parameters and simulation of RESTful cloud application services [36].
Ourpreviousmodellingeffortswereaimingtowardssimpli-
| various | features | of interests | are identified |     | by  | PRISM | labels |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | -------------- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
to aid tracking of behaviour changes in the cloud application. fied representation of a RESTful service model by organizing
Parametric generation of various experiments is based on application components by their dependency relationships
|           |      |         |                   |     |        |     | into a directed |     | acyclic | graph (DAG), | where | the | root | node |
| --------- | ---- | ------- | ----------------- | --- | ------ | --- | --------------- | --- | ------- | ------------ | ----- | --- | ---- | ---- |
| constants | that | provide | a straightforward |     | method | to  | adjust          |     |         |              |       |     |      |      |
behavioural properties of the simulated application context. R is representing the user facing service component of the
application.Inthemodel,Riscontinuouslytriggeringrequests
| Our work | has | gradually | shifted | from constrained |     | or  | uncon- |     |     |     |     |     |     |     |
| -------- | --- | --------- | ------- | ---------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
tointermediarynodesnandleafnodesm.Requestsarerouted
| strained | path simulation |     | applications | towards |     | formal | model |     |     |     |     |     |     |     |
| -------- | --------------- | --- | ------------ | ------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
checking against various properties described as probabilis- in a nondeterministic way from R through various number of
|            |          |         |              |     |         |      | intermediaries |     | (n) ultimately | arriving | to a | leaf m. |     |     |
| ---------- | -------- | ------- | ------------ | --- | ------- | ---- | -------------- | --- | -------------- | -------- | ---- | ------- | --- | --- |
| tic linear | temporal | logical | expressions, |     | such as | PCTL | [33].          |     |                |          |      |         |     |     |
Ultimately, these expressions were used to define end-user Two constants are introduced on the graph level to better
|     |     |     |     |     |     |     | describe | application | behaviour |     | P is | the probability |     | of  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --------- | --- | ---- | --------------- | --- | --- |
observable features of the simulated cloud application, most fail
|             |         |              |     |       |               |     | failure | of any | leaf node | (m), | while retries | is  | a parameter |     |
| ----------- | ------- | ------------ | --- | ----- | ------------- | --- | ------- | ------ | --------- | ---- | ------------- | --- | ----------- | --- |
| prominently | service | availability | or  | error | rate provided |     | by the  |        |           |      |               |     |             |     |
user interface. of intermediaries (n) representing number of request re-
transmissionattemptsbeforegivinguponanerror.Responses
|           |            |             |     |     |     |     | of the application |      | are originating |          | from leaf         | nodes | (m) | then  |
| --------- | ---------- | ----------- | --- | --- | --- | --- | ------------------ | ---- | --------------- | -------- | ----------------- | ----- | --- | ----- |
| B. Faults | in a Cloud | Application |     |     |     |     |                    |      |                 |          |                   |       |     |       |
|           |            |             |     |     |     |     | propagated         | back | through         | a series | of intermediaries |       | (n) | to be |
Errorsinacloudapplicationcanresultineithertransientor ultimatelyaggregatedatRenablingobservationofapplication
| permanentdisruptionoftheirservices.Fromtheperspectiveof |     |     |     |     |     |     | error rates. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |

5646 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
|     |     |     |     | Algorithm         | 1 Pseudocode | for | Dataset | Generation |     |     |
| --- | --- | --- | --- | ----------------- | ------------ | --- | ------- | ---------- | --- | --- |
|     |     |     |     | 1: for all        | cases do     |     |         |            |     |     |
|     |     |     |     | 2: D:=randomDAG(n |              |     | )       |            |     |     |
nodes
|     |     |     |     | G:=insertDFSEdges(D,p |                      |     |      | )   |     |     |
| --- | --- | --- | --- | --------------------- | -------------------- | --- | ---- | --- | --- | --- |
|     |     |     |     | 3:                    |                      |     | down |     |     |     |
|     |     |     |     | 4: for                | all subcases         | do  |      |     |     |     |
|     |     |     |     |                       | for all n in G.nodes |     | do   |     |     |     |
5:
isLeaf(n)
|     |     |     |     | 6:  | if             | then |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | ---- | --- | --- | --- | --- |
|     |     |     |     | 7:  | n.P :=random(p |      |     | ,p  | )   |     |
|     |     |     |     |     | fail           |      | min | max |     |     |
end if
8:
isInternal(n)
|     |     |     |     | 9:  | if                  |     | then |     |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | ---- | --- | --- | --- |
|     |     |     |     | 10: | n.retries:=random(r |     |      | ,r  | )   |     |
min max
|     |     |     |     | 11: | end if        |         |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | ------- | --- | --- | --- | --- |
|     |     |     |     | 12: | end for       |         |     |     |     |     |
|     |     |     |     |     | exportGEXF(id |         | ,G) |     |     |     |
|     |     |     |     | 13: |               | subcase |     |     |     |     |
S:=generatePAs(G)
14:
Fig.3. Simpleservicemeshapplicationtopology.
15: P:=generatePRISM(S)
path:=pathSimulation(P)
16:
exportPath(path)
17:
actions:=filterActions(path)
18:
exportActions(actions)
19:
20: fault:=checkFaultExpression(P)
|     |     |     |     |         | exportFault(id |         | ,fault) |     |     |     |
| --- | --- | --- | --- | ------- | -------------- | ------- | ------- | --- | --- | --- |
|     |     |     |     | 21:     |                | subcase |         |     |     |     |
|     |     |     |     | 22: end | for            |         |         |     |     |     |
exportStatistics(subcases)
23:
24: end for
25: exportStatistics(cases)
|     |     |     |     | model transitions                                  | measured  | from | the     | initial state | of “polling”. |     |
| --- | --- | --- | --- | -------------------------------------------------- | --------- | ---- | ------- | ------------- | ------------- | --- |
|     |     |     |     | AvailabilityoftheapplicationforagivenperiodoftimeT |           |      |         |               |               | can |
|     |     |     |     | also be considered                                 | a closely |      | related | property      | to P max.     |     |
Fig.4. Servicemeshapplicationtopologywithforwardedges-modification
ofgraphonFigure3. These enhancements further enhanced our simulation and
|     |     |     |     | training data | generation         | capabilities, |                | enabling | modelling   | of  |
| --- | --- | --- | --- | ------------- | ------------------ | ------------- | -------------- | -------- | ----------- | --- |
|     |     |     |     | RESTful       | cloud applications |               | with increased |          | complexity. | New |
Based on this approach, each user request is simulated node-level parameters enabled clustering of previous exper-
as a single chain of requests and responses along a path iments with subcases of topologically equivalent application
[R,n1 ,n2 ,...,n ,m], representing each complex request by models, but with distinct random values for P [m] and
|         | x                    |              |                 |             |     |     |     |     | fail |     |
| ------- | -------------------- | ------------ | --------------- | ----------- | --- | --- | --- | --- | ---- | --- |
| forming | a random depth-first | search (DFS) | path walk, com- | retries[n]. |     |     |     |     |      |     |
plete with occasional back-traces as instructed by the retries A generic algorithm for dataset generation is supplied as
parameter. Figure 3 illustrates a RESTful service mesh appli- pseudocode in Algorithm 1. Statements with export keywords
cation model based on a random DAG. represent records output as part of the dataset. Statements
In the course of our current work, model-level constants with generate and filter keywords represent custom Python
P and retries were further enhanced to become local codebytheauthors,generatePAs()isresponsibleforderiving
fail
properties of leaf m and intermediary n nodes, becoming probabilistic automatons (PAs) for nodes of a directed graph,
P [m] and retries[n] respectively. This approach then was generatePRISM() will then translate this PA representation
fail
further enhanced by conducting a breadth-first walk on the into PRISM source code. Statements with random keyword
DAG to group nodes by their distance d from the root node, annotate random data generation with uniform distribution.
thus forming node sets at different levels n of the DAG. Finally, pathSimulation and checkFaultExpression represent
d
New requests paths then were injected to the DAG in the external calls to the PRISM model checker.
form of edges (e) so that they only traverse forward the DAG, Algorithm 1 outlines a procedure for generating datasets
∀e (n ,n )|d1 < d2. Figure 4 illustrates the previous that simulate RESTful service mesh applications using
| new | d1 d2 |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RESTful service application model with injected forward directed acyclic graphs (DAGs) and stochastic modeling tools
edges. like probabilistic automatons (PAs) and the PRISM model
It is also possible to calculate the probability of an overall checker.Theprocessbeginswithiteratingoverdifferentappli-
application failure by checking the numerical value of the cationcases.Foreachcase,arandomDAG(D)isgeneratedto
expression P =?[F < TR ], where R is the representthearchitectureoftheapplication.Directededgesare
|     | max | failure | failure |     |     |     |     |     |     |     |
| --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
“failure” state of the root node (R) and T is the number of theninsertedintothisgraphtosimulatepotentialrequestpaths,

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5647
guided by a probability (p ) of establishing downward In this expression, x is the feature vector associated with
down i
connectionsthatrespectthehierarchicalstructureoftheDAG. node i, and N(i) represents th(cid:9)e set of neighboring nodes
Withineachsubcase,nodesinthegraphareclassifiedbased connectedtonodei.Thesymbol representsadifferentiable,
on their role: either as leaf nodes or intermediary nodes. Leaf permutation-invariant function (e.g., sum, mean, or max),
nodes, which handle end-user requests, are assigned a failure whileφandθdenotedifferentiablefunctions,oftenrealizedas
probability (P
fail
) generated randomly within defined bounds M(cid:9)ultilay(cid:10)erPerceptrons(MLPs).Inourstudy,wehaveadopted
((p min , p max )). Intermediary nodes are configured with a = , and have configured φ and θ as {Linear} →
parameter denoting the number of retry attempts in case of {PReLU}→{Linear}.
failures, also determined randomly ((r min , r max )).
The graph structure and its configurations are exported in B. GNN Training for Fault Prediction
GEXF format for interoperability and further analysis. The
To identify critical components within a service mesh,
procedural transformation then involves deriving probabilistic
it is essential to have a strong baseline GNN model for
automatonsforthegraphnodes,whicharesubsequentlytrans-
fault probability prediction. With a well-trained model, we
lated into the PRISM modeling language to facilitate formal
can assess how the removal of certain parts of the service
verification and model checking of the stochastic models. A
mesh affects the system-level fault probability: a significant
simulation of request paths is conducted, tracing the routes
decreaseindicatesthatthosepartsareweakcomponents,while
of requests across the service mesh to assess the pathways
a significant increase suggests that those parts play a crucial
utilized.
role in maintaining the service mesh’s performance.
Pathway data is exported for analysis, while actionable
Fault probability prediction is a graph-level regression task
eventswithinthesepathsarefilteredforfurtherinspectionand
in which each service mesh is represented as a graph, and the
exported separately. To ascertain the robustness of the sub-
target variable is the associated system-level fault probability.
cases, a formal check is performed for expressions indicating
Each node within the service mesh graph is characterized by
systemfaultsusingthePRISMmodelchecker,withtheresults
a single feature. For leaf nodes, this feature is the probability
recorded alongside the respective subcase identifiers.
of failure, while for intermediary nodes, it represents the
Thealgorithmconcludesbyaggregatingstatisticaldatafrom
number of request retransmission attempts before giving up
individual subcases and cases, exporting these statistics to
on an error. To facilitate modeling, we employed two distinct
serve as a comprehensive dataset that encapsulates the behav-
input channels: for leaves, the number of retries was set to
ior and properties of the simulated service mesh applications
0 since they lack descendants, while for intermediaries, the
under varied conditions.
probabilityoffailurewassetto0asthesenodesdonotdirectly
experiencefailures.Thisapproachensuresaconsistentfeature
representation.
IV. GRAPHNEURALNETWORKFORTHEDETECTIONOF
The dataset was randomly split into training, validation,
CRITICALCOMPONENTSINSERVICEMESHES
and test sets, comprising 80%, 10%, and 10% of the service
A. Graph Neural Networks
meshes,respectively.Ourobjectiveistolearnafunctionf that
Graph Neural Networks (GNNs) have become the most minimizes the mean squared error MSE(f(G),y) between the
commonmachinelearningmethodsforpredictivetaskswithin predictedsystem-levelfaultprobabilitiesf(G)andtheground-
the domain of real-world networks. In these networks, each truth system-level fault probabilities y for the input graphs
individual data point corresponds to a node, characterized G =(X,A).
not only by a feature vector x i but also an adjacency vector To achieve this, we use a standard graph neural network
a
i
that specifies its connections to all other nodes. These architecturecomposedofthefollowinglayers:{MPBlock}→
feature vectors are organized into a feature matrix denoted as {MPBlock} → {MPBlock} → {MPBlock} →
X ∈RN×F, while the adjacency vectors take the form of an {GlobalMeanPool} → {Linear} → {ReLU} → {Linear}
adjacency matrix A ∈ RN×N, where F and N respectively where each message passing block includes the follow-
denote the number of features and the number of nodes in the ing operations: {MessagePassing} → {BatchNorm} →
network. {PReLU}. The complete architecture is illustrated in
ThetasksaddressedbyGNNscanbecategorizedintonode- Figure 5.
level, link-level, and graph-level tasks, depending on whether We conducted meticulous hyperparameter tuning for our
the labels pertain to nodes, links, or entire graphs. Given the GNNmodel.Thedimensionalityofeachofthe4hiddenlayers
sparsity of real-world networks, it is noteworthy that only a weresetto32.Theneuralnetworkwastrainedfor200epochs
small number of entries in A contain non-zero values. To using mini-batches of 32 service meshes. Network parameters
effectively handle such sparse matrices, GNNs incorporate wereoptimizedusingtheAdamoptimizer[39]withalearning
so-called message passing layers [37], [38]. Message-passing rateof2e-4.Themeansquarederror(MSE)servedastheloss
layers are responsible for gathering information from neigh- function.Aftertraining,werestoredtheparametersofthebest
boring nodes. This process can be mathematically expressed performing model on the validation set.
as:
⎛ ⎞
C. GNN Training for Identifying Critical Components
(cid:4) (cid:5) (cid:6)
x (cid:2) =φ⎝ x , θ x ,x ⎠ After developing a highly accurate GNN model for fault
i i i j
j∈N(i) prediction, we turned our attention to understanding how

5648 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
|     |     |     |     |     |     |     | the | selected | nodes | are really |     | the critical | components |     | driving |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | --- | ------------ | ---------- | --- | ------- |
thefaultprediction:theyarenecessarybecauseremovingthem
significantlyimpactstheprediction,andsufficientbecausethe
|     |     |     |     |     |     |     | subgraph |     | alone can | replicate | the | original | prediction. |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | --------- | --- | -------- | ----------- | --- | --- |
TheexplainerandpredictorGNNsaretrainedinalternating
|     |     |     |     |     |     |     | steps. | In each          | iteration:                   |               |               |            |            |                   |             |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------------- | ---------------------------- | ------------- | ------------- | ---------- | ---------- | ----------------- | ----------- |
|     |     |     |     |     |     |     | •      | Predictor        | update:                      |               | The explainer |            | generates  | a                 | probability |
|     |     |     |     |     |     |     |        | distribution     |                              | p over        | the nodes     | of         | the graph. | A                 | node mask   |
|     |     |     |     |     |     |     |        | m is             | then sampled                 |               | by applying   |            | Bernoulli  | sampling          | to          |
|     |     |     |     |     |     |     |        | this probability |                              | distribution. |               | This       | mask       | defines           | a selected  |
|     |     |     |     |     |     |     |        | subgraph         | g                            | and its       | complementary |            |            | subgraph          | g¯. The     |
|     |     |     |     |     |     |     |        | predictor        | f istrainedtominimizethemean |               |               |            |            | squarederror      |             |
|     |     |     |     |     |     |     |        | (MSE)            | between                      | its           | predictions   | and        | the        | true system-level |             |
|     |     |     |     |     |     |     |        | fault            | probability                  | on            | both          | subgraphs: |            |                   |             |
Fig.5. TheproposedGNNarchitectureforfaultprobabilityprediction.
|     |     |     |     |     |     |     |     |     | L   | =MSE(f(g),y) |     | +MSE(f(g¯),y) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | --- | --- |
f
| specific parts | of the | service | mesh | influence | the | predicted |     |     |     |     |     |     |     |     |     |
| -------------- | ------ | ------- | ---- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Explainerupdate:Thepredictor,withitsupdatedparam-
system-level fault probability. In each network, our goal is eters, is evaluated on the subgraphs g and g¯ to compute
| to separate | the network | into     | two | complementary  |     | parts: one |     |             |     |               |      |           |           |       |           |
| ----------- | ----------- | -------- | --- | -------------- | --- | ---------- | --- | ----------- | --- | ------------- | ---- | --------- | --------- | ----- | --------- |
|             |             |          |     |                |     |            |     | the reward. |     | The explainer |      | s is then | optimized |       | using the |
| containing  | atmostB%of  | thenodes |     | and preserving |     | prediction |     |             |     |               |      |           |           |       |           |
|             |             |          |     |                |     |            |     | REINFORCE   |     | algorithm     | [43] | with      | the       | loss: |           |
accuracy(therelevantsubgraph),andonewheretheprediction
| accuracy degrades | significantly |     | (the | irrelevant | subgraph). | This |     |     |     |     |             |     |     |     |     |
| ----------------- | ------------- | --- | ---- | ---------- | ---------- | ---- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
|                   |               |     |      |            |            |      |     |     |     | L   | =R·BCE(p,m) |     |     |     |     |
way, the selected nodes are both necessary and sufficient for s
| the prediction. | Exhaustively    |     | searching | for     | such               | subnetworks |     |         |            |             |     |             |       |        |            |
| --------------- | --------------- | --- | --------- | ------- | ------------------ | ----------- | --- | ------- | ---------- | ----------- | --- | ----------- | ----- | ------ | ---------- |
|                 |                 |     |           |         |                    |             |     | where   | the reward | function    |     | R is        | based | on the | difference |
| by evaluating   | all possible    |     | node      | subsets | is computationally |             |     |         |            |             |     |             |       |        |            |
|                 |                 |     |           |         |                    |             |     | between | the        | predictor’s |     | performance |       | on the | selected   |
| infeasible,     | which motivates |     | the need  | for     | a learned          | masking     |     |         |            |             |     |             |       |        |            |
subgraphanditscomplementarysubgraph,withanadded
mechanism.
To address this challenge, we designed an explainability term that encourages sparsity in the selected nodes [42]:
algorithm that assigns importance scores to the nodes of (cid:5) (cid:6)
|     |     |     |     |     |     |     |     | =MSE(f(g¯),y) |     |     | −MSE(f(g),y) |     | +ReLU |     | μ −B |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------------ | --- | ----- | --- | ---- |
a network. Drawing inspiration from previous methods like R p
| L2X [40], | INVASE [41], | and | PGExplainer |     | [42], | our approach |     |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ----------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
μ
usesanexplainer neuralnetwork tocompute nodeimportance Here, p is the mean of the probability distribution p,
probabilitiesviagradientdescent.Basedontheseprobabilities, and B is the budget which controls the expected number
we can select the most important B% of the nodes in the of nodes selected by the explainer.
service mesh with respect to fault prediction, providing a The dataset was split into training, validation, and test sets
|                    |               |             |             |                |     |               | following |               | the same        | procedure  |      | used      | for fault | prediction, | and |
| ------------------ | ------------- | ----------- | ----------- | -------------- | --- | ------------- | --------- | ------------- | --------------- | ---------- | ---- | --------- | --------- | ----------- | --- |
| practical solution | to            | our problem |             | that minimizes |     | prediction    |           |               |                 |            |      |           |           |             |     |
| error.             |               |             |             |                |     |               | the       | same          | hyperparameters |            | were | retained. |           |             |     |
| Our algorithm,     | depicted      | in          | Figure      | 6, consists    |     | of two neural |           |               |                 |            |      |           |           |             |     |
| networks:          | an explainer  | GNN         | and         | a predictor    |     | GNN. The      |           |               |                 |            |      |           |           |             |     |
|                    |               |             |             |                |     |               | D.        | Computational |                 | Complexity |      |           |           |             |     |
| explainer          | GNN generates |             | a Bernoulli | distribution   |     | over the      |           |               |                 |            |      |           |           |             |     |
nodes of the service mesh, as illustrated in Figure 7. The Our approach is computationally efficient, as both the fault
probabilities assigned to each node reflect its significance in probability estimation and the explainability algorithm rely
shaping the fault prediction process. From this distribution, on Graph Neural Networks (GNNs). The key property of
we can sample a node mask that selects the most important GNNs is that they operate on sparse adjacency matrices,
nodes. This mask is then applied to both the adjacency enablingefficientstorageandcomputation.Thecomputational
matrix A and the feature matrix X through element-wise complexity of message-passing layers in GNNs is O(E),
multiplication,producingamaskedversionoftheinputgraph. where E is the number of edges in the graph. Since service
The predictor GNN, trained for fault prediction as described meshes typically have far fewer edges than the theoretical
O(N2)
in the previous subsection, evaluates three versions of the bound for dense graphs, this makes GNN-based fault
graph: the original unmasked graph G, the subgraph selected probability estimation scalable even for large-scale systems.
by the explainer after masking g, and its complementary Since our explainer network is implemented as another
g¯
subgraph (the nodes not selected by the explainer). If GNN that learns to generate node importance scores, its
the node mask captures the most relevant nodes within the complexity remainsthesameasthefaultprobabilitypredictor
service mesh, the predictor’s performance on the selected GNN. Its overhead comes from sampling node masks and
subgraphgshouldcloselyapproximateitsperformanceonthe computing the reward function, but these operations are
originalgraphG,whileitsperformanceonthecomplementary lightweight compared to the forward and backward passes of
g¯
| subgraph | should drop | significantly. |     | This | demonstrates | that | a GNN. |     |     |     |     |     |     |     |     |
| -------- | ----------- | -------------- | --- | ---- | ------------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5649
Fig.6. IllustrationoftrainingtheexplainerGNNforidentifyingcriticalcomponentsintheservicemesh.TheexplainerGNNgeneratesprobabilitiesfornode
masking,producingamaskthatselectsthemostimportantnodesforfaultprobabilityprediction.ThepredictorGNNthenevaluatestheselectedsubgraphg
anditscomplementaryg¯.Ifthemaskcapturesthemostrelevantnodes,thepredictor’sperformanceonthesubgraphgshouldcloselymatchitsperformance
on the original graph, while its performance on the complementary subgraph g¯ should drop significantly, confirming that the selected nodes are necessary
andsufficientfortheprediction.Themeanoftheprobabilities,µp,andthebudgetB(e.g.,B =33%meansone-thirdofthenodesareretained)controlthe
numberofnodesselected.
|         |               |                  |                        |         | A. Training       | Dataset     |                |               |                   |               |                |             |
| ------- | ------------- | ---------------- | ---------------------- | ------- | ----------------- | ----------- | -------------- | ------------- | ----------------- | ------------- | -------------- | ----------- |
|         |               |                  |                        |         | The generation    |             | of training    |               | datasets          | for           | the REST-based |             |
|         |               |                  |                        |         | approach          | involves    | constructing   |               | synthetic         | models        | that           | simulate    |
|         |               |                  |                        |         | complex           | cloud       | architectures  | characterized |                   | by            | a service      | mesh        |
|         |               |                  |                        |         | pattern.          | The RESTful | services       |               | are designed      |               | as nodes       | within a    |
|         |               |                  |                        |         | directed          | acyclic     | graph          | (DAG)         | structure,        | where         | the            | root node   |
|         |               |                  |                        |         | initiates         | requests    | that propagate |               | through           | intermediary  |                | nodes       |
|         |               |                  |                        |         | to leaf nodes.    |             | Intermediary   | nodes         | handle            | requests      |                | probabilis- |
|         |               |                  |                        |         | tically, relaying |             | them towards   |               | child nodes       | or            | providing      | direct      |
|         |               |                  |                        |         | responses.        | Leaf        | nodes finalize |               | interactions      | by            | returning      | HTTP        |
|         |               |                  |                        |         | status codes,     | either      | signifying     |               | successful        | operations    |                | (HTTP       |
|         |               |                  |                        |         | 2xx) or           | indicating  | server         | failures      | (HTTP             | 5xx),         | the            | latter of   |
|         |               |                  |                        |         | which triggers    |             | a defined      | retry         | mechanism.        | Each          | component’s    |             |
|         |               |                  |                        |         | operations        | and         | interactions   | are           | probabilistically |               | modulated,     |             |
|         |               |                  |                        |         | enabling          | varied      | simulations    | reflective    |                   | of real-world |                | scenarios.  |
| Fig. 7. | The explainer | network consists | of six message-passing | blocks, |                   |             |                |               |                   |               |                |             |
UtilizingthePythonprogramminglanguage,adomain-specific
followedbyasigmoidlayerthatgeneratesaprobabilitydistributionoverthe
nodes,reflectingtheirimportanceforfaultprobabilityprediction. language (DSL) was devised to model these interactions
|     |     |     |     |     | within the   | RESTful | framework. |     | This      | automation   |     | facilitates |
| --- | --- | --- | --- | --- | ------------ | ------- | ---------- | --- | --------- | ------------ | --- | ----------- |
|     |     |     |     |     | the creation | and     | execution  | of  | extensive | simulations, |     | with        |
V. EXPERIMENT1:FAULTPREDICTIONFORFEATURE
predefinedrangesforcriticalparameterssuchasthenumberof
ENRICHEDSERVICEMESHES itemsandbuffersizes,enhancingtherobustnessofthedataset.
|         |             |             |                 |        | The training | dataset | generation |     | method | and | the | volume of |
| ------- | ----------- | ----------- | --------------- | ------ | ------------ | ------- | ---------- | --- | ------ | --- | --- | --------- |
| In this | experiment, | we evaluate | the performance | of our |              |         |            |     |        |     |     |           |
GNN-based approach for fault prediction on two types of ser- generatedsamplesensurecomprehensivecoverageofpotential
vice meshes: tree-shaped service meshes and general directed statesandtransitions,therebyobviatingthenecessityfornoise
acyclicgraphs(DAGs).Faultpredictionservesasafoundation reduction. The framework’s methodological approach ensures
for identifying critical components within the service mesh, that the resultant dataset is both diverse and representative of
potentialreal-worldRESTfulserviceinteractions,significantly
asaccuratelypredictingsystemfaultprobabilitiesallowsusto
analyze the impact of removing specific nodes. Tree-shaped contributing to the accuracy and reliability of subsequent
meshes represent a simpler hierarchical topology, making it analyses and models.
|           |               |               |                 |      | The current |     | approach | prioritizes | computational |     |     | efficiency |
| --------- | ------------- | ------------- | --------------- | ---- | ----------- | --- | -------- | ----------- | ------------- | --- | --- | ---------- |
| easier to | trace service | dependencies, | whereas general | DAGs |             |     |          |             |               |     |     |            |
capture more complex, non-hierarchical relationships between andsimplifiesthesimulationofnetworkdynamicsbyfocusing
failurespredominantlyattheleafnodes.Thisdecisionensures
services,whereidentifyingcriticalcomponentsmightbemore
challenging. All experiments were repeated three times, and that the model remains scalable and manageable, particularly
allresultsreportedarethemeanandstandarddeviationacross whensimulatingextensiveservicemesheswithmultiplelayers
ofintermediatenodes.Byusingretrycountersatintermediary
| these three | runs. |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

5650 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
TABLEII
SAMPLEOFOBSERVABLEACTIONSIMULATIONRESULTS
Fig.8. Learningcurveforfaultprobabilitypredictionontree-shapedservice
meshes:validationR2 score(leftaxis)andvalidationMAEscore(rightaxis)
overepochs(mean±standarddeviationacross3runs).
• result: simulated HTTP result code for resp actions,
with values 2xx for normal responses, and 5xx for error
responses.
Based on the core model properties and node strategies
described in the previous section, the message patterns follow
a depth-first walk pattern with optional back-tracking. This
means that for any given pair of communicating nodes, the
following statements hold true:
• foreachreqactiontheremustbeatleastonerespaction,
more resp actions are allowed in case of errors
nodes,themodeleffectivelyemulatestherobustnessstrategies • for each req action at least one resp action is mandatory,
typical in contemporary cloud infrastructures, where fault
so requests are not queued
toleranceislargelyhandledthroughretriesandloadbalancing
At this phase of research, the total experimental dataset
rather than expecting individual intermediaries to manage
volume has exceeded 2.1 GB, including cloud architecture
failure. This abstraction aligns with industry practices, where
modelsin50casesfortree-shapedservicemeshesand10cases
resilienceisachievedthroughredundancyandfailovermecha-
for DAG-based service meshes, each with distinct topologies.
nisms, minimizing the need to simulate internal failures at all
Each tree-shaped case contains 50 subcases, and each DAG-
node levels within the architecture.
based case contains 10 subcases. The graphs in the dataset
Training datasets were generated based on the approach
consist of 25 RESTful nodes per service mesh. While the
described above. Several cases, each containing simulation
underlying graph structure remains the same within each
datasets, were generated for different architecture topologies
case, the node features–the number of retries for intermediary
(basedonrandomDAGs).Thesethenwereexpandedwithsets
nodesandtheprobabilityoffailureforleafnodes–varyacross
of sub-cases, each with random parameter values for P [m]
fail subcases, offering a diverse set of configurations for analysis.
andretries[n]followingauniformdistribution.Foreachcase,
The calculated system-level fault probabilities in the dataset
agraphdescriptioninGraphExchangeXMLFormat[44]was
range from a minimum of 0.0 to a maximum of 1.0, with a
augmented with these new node attributes.
median of 1.2e-5.
As internal state graph transition state simulations were
consideredlessimportantinthisphaseofresearch,theirlength
B. Fault Prediction Results on Tree-shaped Service Meshes
was reduced to 10.000 steps. To aid experiments focusing on
the external observable properties of the cloud applications, a Inthissubsection,wepresenttheresultsofourexperiments
newfilteredstatesimulationformatwasdevised,asillustrated ontree-shapedservicemeshes.Theseexperimentsdemonstrate
by Table II. This message simulation dataset consists of the the model’s ability to capture both the relationships between
following fields: nodes and their connections, as well as how variations in
• id: event identifier, the discrete timestamp of the logical node features and the overall mesh structure influence system
clock reliability.
• from:messagesourcenodeidentifierinformatX n where AsshowninFigure 8,thelearningcurveindicateseffective
is n is the node identifier training, with a consistent decrease in the MAE score and a
• to: message destination node identifier in format X n correspondingincreaseinthevalidationR2 scoreoverepochs.
• method: simulated HTTP method, only GET is imple- The best model on the validation set achieved a MAE of
mented at the time of writing 0.009±0.001onthetestset,demonstratingstronggeneraliza-
• action: simulated HTTP action, with values req for tion across diverse tree-shaped service mesh topologies. The
requests and resp for responses regression plot further highlights the close alignment between

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5651
Fig. 9. Test R2 score (left axis) and test MAE score (right axis) versus Fig.11. TestR2score(leftaxis)andtestMAE(rightaxis)versustrainingset
training set fraction for fault probability prediction on tree-shaped service fractionforfaultprobabilitypredictiononDAG-shapedservicemeshes.Error
meshes. Error bars represent mean ± standard deviation across 3 runs. bars represent mean ± standard deviation across 3 runs. Numerical labels
Numericallabelsindicatethemeanvalueateachpoint. indicatethemeanvalueateachpoint.
regression plot further confirms the close alignment between
predicted and actual system fault probabilities, with a test R2
score of 0.996±0.003 (Figure 15, subfigure (a))).
We further evaluated the model trained on DAG-shaped
service meshes by testing it on the tree-shaped service mesh
dataset to assess its ability to transfer across different topolo-
gies. The pretrained model achieved a test MAE score of
0.038±0.006 and a test R2 score of 0.938±0.014 on the
tree-shaped service mesh test set. These results, while slightly
lower than those of the model trained directly on tree-shaped
meshes,clearlydemonstratethemodel’scapacitytogeneralize
Fig.10. Learningcurveforfaultprobabilitypredictionontree-shapedservice effectively across different service mesh structures.
meshes:validationR2 score(leftaxis)andvalidationMAEscore(rightaxis) As in our experiments on tree-shaped service meshes,
overepochs(mean±standarddeviationacross3runs).
we explored the impact of varying the training set size on
the model’s performance. Figure 11 illustrates a clear trend:
predicted and actual system fault probabilities, with a test R2 increasing the training set size leads to a decreasing MAE
score of 0.992±0.005 (Figure 12, subfigure a)). score and an increasing R2 score on the test set, with both
metrics stabilizing at higher values. This consistency affirms
Additionally,weexaminedtheeffectofvaryingthetraining
our earlier conclusion that larger, more diverse datasets allow
setsizeonmodelperformance.AsshowninFigure 9,theplot
presents the test R2 score and test MAE score as functions of themodeltobettercapturetherelationshipswithintheservice
mesh topology.
the training set fraction. The figure shows that the test MAE
decreases consistently as the training set size increases, while
the test R2 score correspondingly improves and stabilizes at
D. Baseline Comparison
higher values. These results highlight the importance of using
To contextualize the performance of our GNN model and
a large and diverse dataset to enable the model to effectively
to isolate the contributions of nonlinear transformations and
capture the underlying dependencies within the service mesh.
messagepassing,weimplementedasystematicsetofbaseline
This is crucial for further analyses on identifying critical
models:
components within the network.
• LinReg: We bucketized the node feature values into five
buckets per feature by sorting the values and dividing
C. Fault Prediction Results on DAG-Shaped Service Meshes
them into equal-sized groups. The mean within each
In this subsection, we extend our experiments to DAG- bucketwascomputed,resultinginapermutation-invariant
shaped service meshes to evaluate the model’s ability to representation that is independent of node ordering and
generalize across more complex network topologies. robust to variations in graph size. A linear regression
As shown in Figure 10, the learning curve for DAG-shaped model was then fit to these aggregated features.
service meshes shows a pattern similar to that observed for • LinRegwithspectralembeddings:Sincelinearregression
tree-shaped meshes, with a consistent decrease in the MAE cannot capture the graph structure, we computed the
score and a corresponding increase in the validation R2 score spectral embedding of each graph, applied the same
over epochs. The best model on the validation set achieved a bucketization to the spectral coordinates, and concate-
test MAE of 0.009±0.002, indicating strong generalization nated these with the bucketized node features. A linear
across diverse DAG-shaped service mesh topologies. The regression model was fit to the combined features.

5652 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
TABLEIII
TESTSETMAEFORBASELINEMODELSANDTHEGNNONTREE-AND
DAG-SHAPEDSERVICEMESHES
• MLP:ThismodelusesthesamearchitectureastheGNN,
but with all message passing layers replaced by linear
layers.Permutationinvarianceispreservedthroughglobal Fig.13. R2andMAEScoresvs.Budget(ProportionofSelectedNodes):As
mean pooling, while the model loses the GNN’s ability the selection budget increases from 10% to 50%, the R2 score for selected
to capture node interactions through message passing. nodes remains consistently high (between 0.991 and 0.996), demonstrating
thatevensmallsubsetscapturemostofthepredictiveinformation.Incontrast,
• MLPwithspectralembeddings:Thesamearchitectureas theR2scoreforcomplementarynodessteadilydecreasesfrom0.306to0.048
above, but with spectral coordinates concatenated to the asmoreinformativenodesaremovedtotheselectedset.Similarly,theMAE
node features. This provides information about the graph scoreforselectednodesremainslow,whiletheMAEscoreforcomplementary
nodes increases, reinforcing the importance of the selected nodes in system
structure in the absence of message passing.
faultprobabilityprediction.
Table III presents the test set MAE for each model on
tree- and DAG-shaped service meshes. The linear regres-
sion models achieve limited accuracy, even when spectral
embeddings are included, showing their inability to capture B. Explainability Results on Tree-Shaped Service Meshes
complex interactions between nodes. The MLP baselines Inthissection,wepresenttheexplainabilityresultsfortree-
provide improvements, particularlywhen spectralembeddings shaped service meshes. Using the predictor GNN, we applied
are used, but still fall short of the GNN’s performance. our explainability algorithm to identify which nodes are most
These results highlight the critical role of message passing in influentialinpredictingsystemfaultsituations,discoveringthe
effectivelymodelingnodeinteractions.Atthesametime,they critical components of the networks.
illustrate the tradeoff between model complexity and inter- Figure 12 shows the regression results for the predictor
pretability, motivating the explainability method introduced in GNN on tree-shaped service meshes. The first plot (a) illus-
the next section. trates the predictions made using all nodes in the service
mesh, which align very closely with the actual system fault
probabilities, achieving an R2 score of 0.992±0.005 on the
test set. This result indicates the model’s strong predictive
VI. EXPERIMENT2:DETECTIONOFCRITICAL
performance when using the full set of nodes in the network.
COMPONENTSWITHGNNEXPLAINABILITY
Plot (b) demonstrates the predictions made using only the
In this experiment, we focus on our core objective: iden-
top 30% of nodes selected by the explainer network. Despite
tifying the critical components within service meshes using
reducing the input to a smaller subset, the model maintains
GNN explainability techniques. By applying an explainability strong performance, achieving an R2 score of 0.974±0.018.
method to a well-trained GNN model, we determine which
This is significant, as it confirms that these selected nodes
nodes (or subnetworks) have the most significant influence on
explain most of the variance in the predicted fault outcomes,
the system’s overall reliability. This allows us to detect both
effectivelyidentifyingthemasthemostimportantcomponents
weak points and essential nodes whose failure or underper-
for prediction. In contrast, plot (c) shows the predictions
formance could severely impact service quality. This deeper made on the complementary 70% of nodes, where the R2
insightiscrucialforimprovingservicerobustness,asitenables score drops to 0.104±0.042. This suggests that these nodes
targeted troubleshooting in the network’s most influential
provide minimal information about the fault outcomes, essen-
areas. Additionally, this understanding lays the groundwork
tially leading to a baseline mean prediction. The dramatic
for future work, where the cloud debugger system can be
drop in performance further reinforces the importance of the
steeredtowardpotentialfailurepoints,enablingmoreeffective
selected 30% of nodes in accurately predicting the network’s
remediation and resilience testing.
reliability.
These results show how well our explainability method
works, with the selected nodes being key to predicting fault
A. Training Dataset
outcomes accurately. The sharp drop between the predictive
For this experiment, we used the same datasets as in the power of the selected and unselected nodes affirms the power
faultpredictionexperiments,whichconsistofbothtree-shaped of our method in identifying key components that drive
and DAG-shaped service meshes. These datasets allow us network reliability.
to evaluate the model’s ability to detect critical components We further investigated how adjusting the selection budget,
across varying topologies and service configurations. i.e., the proportion of selected nodes, influences the model’s

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5653
Fig.12. Regressionplotsforfaultprobabilitypredictionontree-shapedservicemeshesusingthepredictorGNN:a)Predictionson100%ofthenodes,closely
alignedwiththegroundtruthvalues,achievinganR2
scoreof0.992,indicatingexcellentpredictiveperformance;b)Predictionsusingtheselected30%of
nodes(chosenbytheexplainernetwork),maintainingstrongperformancewithanR2
scoreof0.974,confirmingthatthesenodesarecriticalforpredicting
system-levelfaultprobabilitiesandcapturingmostofthevarianceinthesystem;c)Predictionsusingthecomplementary70%ofunselectednodes,withan
R2 scoreof0.104,demonstratingthatthesenodesprovidelittleinformationaboutthesystem-levelfaultprobabilities,essentiallyresultinginabaselinemean
prediction. This clearly demonstrates the algorithm’s success in identifying critical components, as the selected nodes retain most ofthe variance while the
unselectedonesprovideminimalpredictivevalue.
predictive performance. By varying the budget from 10% to In Figure 14 (b), we changed the example slightly by
R2
50%, clear patterns emerge in both the and MAE scores setting the failure probability of this critical leaf node next
for the selected and complementary node sets. As shown in to the root to 0.0. This leads to a significant change in the
Figure 13,theR2 scorefortheselectednodesremainsconsis- predicted system fault probability. Using the selected nodes,
tentlyhigh,between0.991and0.996,demonstratingthateven thepredictedsystemfaultprobabilitydropsto0.0becausethe
small subsets of nodes retain most of the critical information critical node no longer has a risk of failure. The predicted
requiredforaccuratefaultprediction.Incontrast,theR2
|     |     |     |     |     |     |     | score | system | fault probability |     | for | the unselected |     | nodes | stays the |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------------- | --- | --- | -------------- | --- | ----- | --------- |
for the complementary nodes steadily decreases from 0.306 same. This result is what we would expect and confirms that
at 10% budget to 0.048 at 50%, as increasingly informative the explainer works correctly.
nodes are moved to the selected set. A similar trend is seen InFigure 14(c),wemadeanotherslightchangebymoving
in the MAE scores: the error for the selected nodes remains the critical leaf node to a lower level in the service mesh,
low,between0.014and0.018,whilethecomplementarynodes attaching it to an intermediary node that can retry once after
exhibit rising errors, from 0.176 to 0.255. These findings a failure. This change affects how the explainer behaves: now
clearlyhighlightthestrengthofourexplainabilitymethod:the only this critical node gets selected. As we expected, the
selected nodes consistently concentrate the predictive power, predicted system fault probability drops to 0.01 due to the
whilethecomplementarynodescontributelittletothemodel’s recovery capability of the intermediary node, which can retry
| fault prediction | accuracy. |         |     |               |         |               |        | the request       | if a | failure | occurs. |            |         |        |     |
| ---------------- | --------- | ------- | --- | ------------- | ------- | ------------- | ------ | ----------------- | ---- | ------- | ------- | ---------- | ------- | ------ | --- |
| To demonstrate   |           | better  | how | our explainer | network |               | works, |                   |      |         |         |            |         |        |     |
| we show a        | simple    | example | in  | Figure 14     | (a). In | this example, |        |                   |      |         |         |            |         |        |     |
|                  |           |         |     |               |         |               |        | C. Explainability |      | Results | on      | DAG-Shaped | Service | Meshes |     |
nodesarecoloredbasedontheirselectionprobabilities,which
| show how | important | each | node | is for | predicting | the | fault |         |             |     |           |                    |     |          |     |
| -------- | --------- | ---- | ---- | ------ | ---------- | --- | ----- | ------- | ----------- | --- | --------- | ------------------ | --- | -------- | --- |
|          |           |      |      |        |            |     |       | In this | subsection, |     | we extend | our explainability |     | analysis | to  |
outcome. There is a leaf node next to the root with the DAG-shapedservicemeshes.Aswiththetree-shapedmeshes,
relatively high failure probability of 0.27 (marked in red). we used the predictor GNN and applied the explainability
| Since this | node is | close | to the | root and | has | a high | risk of |           |              |     |       |       |      |               |     |
| ---------- | ------- | ----- | ------ | -------- | --- | ------ | ------- | --------- | ------------ | --- | ----- | ----- | ---- | ------------- | --- |
|            |         |       |        |          |     |        |         | algorithm | to determine |     | which | nodes | were | most critical | for |
failure, it plays a key role in determining the overall system predicting the system fault outcomes.
fault probability. As a result, the ground truth system failure Figure 15 presents the regression results for the DAG-
| probability | is a high | value | of  | 0.93. Our | explainer | network |     |        |         |         |     |           |        |                 |     |
| ----------- | --------- | ----- | --- | --------- | --------- | ------- | --- | ------ | ------- | ------- | --- | --------- | ------ | --------------- | --- |
|             |           |       |     |           |           |         |     | shaped | service | meshes. | In  | plot (a), | we see | the predictions |     |
correctly identifies this node as important, assigning it a made using all nodes in the network. The predictor closely
| high selection | probability. |     | Using | only | the selected | nodes, | the |             |     |      |        |                      |     |           |     |
| -------------- | ------------ | --- | ----- | ---- | ------------ | ------ | --- | ----------- | --- | ---- | ------ | -------------------- | --- | --------- | --- |
|                |              |     |       |      |              |        |     | aligns with | the | true | system | fault probabilities, |     | achieving | an  |
model predicts that system fault probability is 0.94, which R2 score of 0.996±0.003, showing that the model performs
is very close to the actual value. In contrast, when the exceptionally well when considering the entire set of nodes.
predictorusesonlytheunselectednodes,thepredictedsystem
|     |     |     |     |     |     |     |     | Plot (b) | shows | the predictions |     | made | using | only the | top 30% |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------------- | --- | ---- | ----- | -------- | ------- |
fault probability is 0.02. This large difference shows that the of nodes identified by the explainer network. The model
unselected nodes cannot be used to determine the fault. Most R2 0.861±
|     |     |     |     |     |     |     |     | maintains | a strong | performance, |     | with | an  | score of |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------------ | --- | ---- | --- | -------- | --- |
oftheunselectednodesarestable,andtheleavesthatcouldfail 0.054, suggesting that these selected nodes capture most of
are far from the root, where intermediary nodes can mitigate the critical information for fault prediction. In contrast, plot
| if something | goes | wrong. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(c)showsthepredictionsmadeusingthecomplementary70%

5654 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
Fig.14. Demonstrationofexplainernetworkonaservicemesh.(a)Acriticalleafnodewithhigh0.27failureprobabilityneartherootleadstoapredicted
systemfaultprobabilityof0.94,closelymatchingthegroundtruthof0.93.(b)Settingthefailureprobabilityofthecriticalnodeto0.00reducesthepredicted
systemfaultprobabilityto0.00.(c)Movingthecriticalnodelowerinthetree,thepredictedsystemfaultprobabilitydropsto0.01duetotheintermediary
node’srecoveryability.
ofnodes.TheR2 scoreheredropsto0.072±0.086.Thissharp explainer may sometimes overlook sparse but highly informa-
decline highlights that these unselected nodes provide little to tivecomponents,andcouldbenefitfromfurtherfine-tuningor
nousefulinformationforpredictingthefaultoutcomes.These regularization to increase robustness.
resultsforDAG-shapedmeshesalignwellwiththosefromthe
tree-shaped meshes, which reinforces the effectiveness of our
explainability method in identifying the critical components
across different network structures. VII. DISCUSSIONANDCONCLUSION
However, in a small number of cases, we observe a Designing dependable and scalable cloud services requires
discrepancy where the predicted system fault probability is systematic tools to analyze complex behaviors and iden-
close to zero while the true probability is significantly higher. tify faults efficiently. While many existing approaches in
This typically occurs when the explainer masks a few critical the literature target specific aspects of fault detection–
nodes that have a disproportionately large influence on the such as networking faults, security breaches, or system-level
overall prediction. When these nodes are excluded from the anomalies–they often operate at a fixed abstraction level
selected subgraph, the model underestimates the system-level and lack generalizability across cloud environments. This
fault probability. These occasional failures suggest that the work contributes a unified and explainable approach to fault

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5655
Fig.15. RegressionplotsforfaultprobabilitypredictiononDAG-shapedservicemeshesusingthepredictorGNN:(a)Predictionson100%ofthenodes,
achievinganR2scoreof0.996,indicatingexcellentpredictiveperformance;(b)Predictionsusingtheselected30%ofnodes(chosenbytheexplainernetwork),
R2
achieving an score of 0.861, showing that these nodes capture most of the critical information for fault probability prediction; (c) Predictions using the
complementary70%ofnodes,achievinganR2 scoreof0.072,demonstratingthatthesenodesprovidelittletonovalueforpredictingfaultprobabilities.
forecasting in microservice-based cloud systems, using prob- (cid:4) OpenAI ChatGPT GPT-4, Scite Assistant: used to create
abilistic modeling and graph-based machine learning. a draft, which was completed, rewritten and enhanced by the
Our proposed method combines a formally verified sim- authors.The promptwas‘Youarearesearcher, produce high-
ulation environment with data-driven fault prediction and quality scientific text. Write a summary draft on the following
explainability. The use of the PRISM model checker enables topics: INPUT TEXT’ alike.
| us to simulate   |     | fault propagation |     | across   | a    | variety | of service |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------------- | --- | -------- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| mesh topologies, |     | generating        |     | training | data | without | requir-    |     |     |     |     |     |     |     |     |
REFERENCES
| ing deployment  |     | on live | infrastructure. |     | Starting | from    | simple   |                   |       |         |        |        |             |               |     |
| --------------- | --- | ------- | --------------- | --- | -------- | ------- | -------- | ----------------- | ----- | ------- | ------ | ------ | ----------- | ------------- | --- |
|                 |     |         |                 |     |          |         |          | [1] D. Jaramillo, | D. V. | Nguyen, | and R. | Smart, | “Leveraging | microservices |     |
| tree-structured |     | graphs  | and extending   |     | to       | general | DAGs, we |                   |       |         |        |        |             |               |     |
architecturebyusingdockertechnology,”inProc.SoutheastCon,2016,
| demonstrated | how | the | framework |     | scales | across | increasing |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --------- | --- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.1–5.
architectural complexity. [2] P.PääkkönenandD.Pakkala,“Referencearchitectureandclassification
oftechnologies,productsandservicesforbigdatasystems,”BigData
| Graph | Neural | Networks | allow | us  | to capture | both | structural |     |     |     |     |     |     |     |     |
| ----- | ------ | -------- | ----- | --- | ---------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Res.,vol.2,no.4,pp.166–186,Dec.2015.
and feature-based dependencies in microservice interactions, [3] A. C.Marosi et al., “Towardreference architectures: A cloud-agnostic
achieving accurate system-level fault probability predictions. dataanalyticsplatformempoweringautonomoussystems,”IEEEAccess,
Furthermore, by integrating an explainability mechanism, the vol.10,pp.60658–60673,2022.
|     |     |     |     |     |     |     |     | [4] “Microsoft | azure | documentation-reference |     |     | architectures.” |     | Accessed: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ----------------------- | --- | --- | --------------- | --- | --------- |
frameworkcanhighlightthemostfailure-pronemicroservices– Feb. 20, 2022. [Online]. Available: https://docs.microsoft.com/en-us/
guiding debugging efforts toward critical components and azure/architecture/browse/
[5] (OpenGroup,SanFrancisco,CA,USA).TheTOGAFStandard,Version
| improving | system-level |     | fault | understanding. |     |     |     |               |           |     |          |                 |     |            |          |
| --------- | ------------ | --- | ----- | -------------- | --- | --- | --- | ------------- | --------- | --- | -------- | --------------- | --- | ---------- | -------- |
|           |              |     |       |                |     |     |     | 9.2 Overview. | Accessed: |     | Feb. 12, | 2022. [Online]. |     | Available: | https:// |
Although the current evaluation is based on synthetic www.opengroup.org/togaf
datasets to ensure full control and formal validation, real- [6] (Hewlett Packard Enterprise, Spring, TX, USA). What is a Reference
|                     |     |            |       |           |          |      |            | Architecture?–Enterprise |            |     | it Definitions.                              | Accessed: |     | Feb. | 20, 2022. |
| ------------------- | --- | ---------- | ----- | --------- | -------- | ---- | ---------- | ------------------------ | ---------- | --- | -------------------------------------------- | --------- | --- | ---- | --------- |
| world applicability |     | remains    | a     | priority. | Future   | work | will focus |                          |            |     |                                              |           |     |      |           |
|                     |     |            |       |           |          |      |            | [Online].                | Available: |     | https://www.hpe.com/us/en/what-is/reference- |           |     |      |           |
| on integrating      |     | real-world | cloud | traces,   | adapting |      | to dynamic |                          |            |     |                                              |           |     |      |           |
architecture.html
|     |     |     |     |     |     |     |     | [7] W. Li, | Y. Lemieux, | J. Gao, | Z. Zhao, | and | Y. Han, | “Service | mesh: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------- | -------- | --- | ------- | -------- | ----- |
operationalenvironments,andextendingthemethodtobroader
|               |           |       |     |            |           |     |            | Challenges, | state     | of the                 | art, and | future | research   | opportunities,” | in    |
| ------------- | --------- | ----- | --- | ---------- | --------- | --- | ---------- | ----------- | --------- | ---------------------- | -------- | ------ | ---------- | --------------- | ----- |
| observability | contexts. |       |     |            |           |     |            |             |           |                        |          |        |            |                 |       |
|               |           |       |     |            |           |     |            | Proc.       | IEEE Int. | Conf. Service-Oriented |          |        | Syst. Eng. | (SOSE),         | 2019, |
| The dataset,  |           | code, | and | additional | materials |     | related to |             |           |                        |          |        |            |                 |       |
pp.122–1225.
this work are publicly available at: https://github.com/BME- [8] J. Cunha, J. Lourenco, and V. Duarte, Debugging of Parallel and
|     |     |     |     |     |     |     |     | Distributed | Programs. | Hauppauge, |     | NY, USA: | Nova | Sci. Publ., | 2001, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | --- | -------- | ---- | ----------- | ----- |
SmartLab/GNN-Fault-Forecasting
pp.101–136.
[9] X.Zhouetal.,“Faultanalysisanddebuggingofmicroservicesystems:
Industrialsurvey,benchmarksystem,andempiricalstudy,”IEEETrans.
Softw.Eng.,vol.47,no.2,pp.243–260,Feb.2021.
ACKNOWLEDGMENT [10] E. Aljoumah, F. Al-Mousawi, I. Ahmad, M. Al-Shammri, and Z. Al-
Jady,“SLAincloudcomputingarchitectures:Acomprehensivestudy,”
| On behalf | of  | the ‘MILAB |     | - SmartLab’ |     | cloud | project, the |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ----------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Int.J.GridDistrib.Comput,vol.8,no.5,pp.7–32,2015.
| authors    | are grateful |        | for the | possibility |             | to use    | HUN-REN |                                                                 |     |     |     |     |     |     |     |
| ---------- | ------------ | ------ | ------- | ----------- | ----------- | --------- | ------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|            |              |        |         |             |             |           |         | [11] B.Ligetfalvi,M.Emo˝di,J.Kovács,andR.Lovas,“Fundamentalsofa |     |     |     |     |     |     |     |
| Cloud [45] | which        | helped | us      | achieve     | the results | published | in      |                                                                 |     |     |     |     |     |     |     |
noveldebuggingmechanismfororchestratedcloudinfrastructureswith
|     |     |     |     |     |     |     |     | macrosteps | and active | control,” | Electronics, |     | vol. 10, | no. 24, | p. 3108, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ------------ | --- | -------- | ------- | -------- |
this paper.
2021.
| (cid:5) WordTune, |     | Grammarly, |     | OpenAI | ChatGPT | GPT-4: | gram- |                                                                  |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | ------ | ------- | ------ | ----- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |            |     |        |         |        |       | [12] R.Lovas,E.Rigó,D.Unyi,andB.Gyires-Tóth,“Experienceswithdeep |     |     |     |     |     |     |     |
mar enhancement. In case of ChatGPT, the prompt was ‘You learning enhanced steering mechanisms for debugging of fundamental
are a researcher, produce high-quality scientific text. Rewrite cloudservices,”IEEEAccess,vol.11,pp.26403–26418,2023.
|               |       |         |         |     |         |     |            | [13] M.Kwiatkowska,G.Norman,andD.Parker,“PRISM4.0:Verification |           |     |           |          |            |         |       |
| ------------- | ----- | ------- | ------- | --- | ------- | --- | ---------- | -------------------------------------------------------------- | --------- | --- | --------- | -------- | ---------- | ------- | ----- |
| the following |       | text to | improve | its | grammar | and | scientific |                                                                |           |     |           |          |            |         |       |
|               |       |         |         |     |         |     |            | of probabilistic                                               | real-time |     | systems,” | in Proc. | Int. Conf. | Comput. | Aided |
| language:     | INPUT | TEXT’   | alike.  |     |         |     |            | Verificat.,2011,pp.585–591.                                    |           |     |           |          |            |         |       |

5656 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.6,DECEMBER2025
[14] J. Kovács, B. Ligetfalvi, and R. Lovas, “Automated debugging mech- [38] M. M. Bronstein, J. Bruna, T. Cohen, and P. Velicˇkovic´, “Geometric
anisms for orchestrated cloud infrastructures with active control and deep learning: Grids, groups, graphs, geodesics, and gauges,” 2021,
| globalevaluation,”IEEEAccess,vol.12,pp.143193–143214,2024. |     |     |     |     |     |     |     | arXiv:2104.13478. |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
[15] G.Aceto,A.Botta,W.DeDonato,andA.Pescapè,“Cloudmonitoring: [39] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
Definitions, issues and future directions,” in Proc. IEEE 1st Int. Conf. 2014,arXiv:1412.6980.
CloudNetw.(CLOUDNET),2012,pp.63–67. [40] J.Chen,L.Song,M.Wainwright,andM.Jordan,“Learningtoexplain:
[16] S. U. Farooq, S. M. K. Quadri, and N. Ahmad, “Metrics, models and Aninformation-theoreticperspectiveonmodelinterpretation,”inProc.
measurements in software reliability,” in Proc. IEEE 10th Int. Symp. Int.Conf.Mach.Learn.,2018,pp.883–892.
Appl.Mach.Intell.Informat.(SAMI),2012,pp.441–449. [41] J. Yoon, J. Jordon, and M. van der Schaar, “INVASE: Instance-wise
[17] S.Zatout,M.S.Benabdelhafid,andM.Boufaida,“Formaltransaction variable selection using neural networks,” in Proc. Int. Conf. Learn.
modeling and verification foran adaptable Web service orchestration,” Represent.,2019,pp.1–24.
inProc.IEEEInt.Conf.Softw.Qual.,Rel.SecurityCompan.(QRS-C), [42] D. Luo et al., “Parameterized explainer for graph neural network,”
Jul.2018,pp.531–536. in Proc. 34th Conf. Neural Inf. Process. Syst., vol. 33, 2020,
[18] A. Souri, A. M. Rahmani, and N. J. Navimipour, “Formal verification pp.19620–19631.
approachesintheWebservicecomposition:Acomprehensiveanalysis [43] R.J.Williams,“Simplestatisticalgradient-followingalgorithmsforcon-
of the current challenges for future research,” Int. J. Commun. Syst., nectionist reinforcement learning,” Mach. Learn., vol. 8, pp.229–256,
| vol.31,no.17,2018,Art.no.e3808.[Online].Available:https://online |     |     |     |     |     |     |     | May1992. |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
ibrary.wiley.com/doi/pdf/10.1002/dac.3808 [44] “GEXF file format.” Accessed: Sep. 28, 2022. [Online]. Available:
| [19] M.Smara,M.Aliouat,A.-S.K.Pathan,andZ.Aliouat,“Acceptancetest |     |     |     |     |     |     |     | https://gexf.ne |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
forfaultdetectionincomponent-basedcloudcomputingandsystems,” [45] M. Héder et al., “The past, present and future of the ELKH cloud,”
FutureGener.Comput.Syst.,vol.70,pp.74–93,May2017. InformációsTársadalom(Inf.Soc.),vol.22,no.2,pp.128–137,2022.
[20] A.Abbasi,S.Band,M.A.A.Al-qaness,A.Abbasi,N.Al-Jallad,andA.
| Mosavi, | “Resource-aware |     | network | topology | management |     | framework,” |     |     |     |     |     |     |
| ------- | --------------- | --- | ------- | -------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ActaPolytechnicaHungarica,Feb.2020,tobepublished.
| [21] R. Raj | Karn, | R. Das, | D.  | Raj Pant, | J. Heikkonen, |     | and R. | Kanth, |     |     |     |     |     |
| ----------- | ----- | ------- | --- | --------- | ------------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
“Automatedtestingandresilienceofmicroservice’snetwork-linkusing
| istio | service | mesh,” in | Proc. | 31st Conf. | Open | Innov. | Assoc. (FRUCT), |     |     |     |     |     |     |
| ----- | ------- | --------- | ----- | ---------- | ---- | ------ | --------------- | --- | --- | --- | --- | --- | --- |
2022,pp.79–88.
| [22] Q. Cao    | and | H. Niu,       | “Higher-order | Markov   | graph | based          | bug | detection |     |     |     |     |     |
| -------------- | --- | ------------- | ------------- | -------- | ----- | -------------- | --- | --------- | --- | --- | --- | --- | --- |
| in cloud-based |     | deployments,” |               | in Proc. | IEEE  | Int. Perform., |     | Comput.,  |     |     |     |     |     |
Commun.Conf.(IPCCC),2022,pp.153–160.
| [23] V. Pontillo, |     | M. Vandercammen, |     | S.  | Verbelen, | and | C. De | Roover, |     |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | --------- | --- | ----- | ------- | --- | --- | --- | --- | --- |
“Ferrari:Failurereproductionthroughautomatictestcasegenerationand
| stack | trace analysis,” |     | in Proc. | 23rd | Belgium-Netherlands |     | Softw. | Evol. |     |     |     |     |     |
| ----- | ---------------- | --- | -------- | ---- | ------------------- | --- | ------ | ----- | --- | --- | --- | --- | --- |
Workshop,2024,pp.1–13.
|                |     |          |     |           |        |       |           |       | Dániel Unyi | is  | currently | pursuing | the Ph.D. |
| -------------- | --- | -------- | --- | --------- | ------ | ----- | --------- | ----- | ----------- | --- | --------- | -------- | --------- |
| [24] P. Zhang, | S.  | Shu, and | M.  | Zhou, “An | online | fault | detection | model |             |     |           |          |           |
andstrategiesbasedonSVM-gridinclouds,”IEEE/CAAJ.Automatica degree in computer engineering with the Budapest
|     |     |     |     |     |     |     |     |     | University | of Technology | and | Economics. | During |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ---------- | ------ |
Sinica,vol.5,no.2,pp.445–456,Mar.2018.
hisPh.D.,hehasearnedtopplacementsininterna-
| [25] X. | Zhou et | al., “Latent | error | prediction | and | fault | localization | for |             |         |               |     |                 |
| ------- | ------- | ------------ | ----- | ---------- | --- | ----- | ------------ | --- | ----------- | ------- | ------------- | --- | --------------- |
|         |         |              |       |            |     |       |              |     | tional data | science | competitions. | In  | addition to his |
microserviceapplicationsbylearningfromsystemtracelogs,”inProc.
|     |     |     |     |     |     |     |     |     | academic | work, he | is actively | involved | in several |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----------- | -------- | ---------- |
27thACMJointEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,2019,
pp.26–30. industry projects as a data scientist, primarily in
|               |     |             |            |             |              |                           |               |     | the financial | and         | forensic       | domains. | His research |
| ------------- | --- | ----------- | ---------- | ----------- | ------------ | ------------------------- | ------------- | --- | ------------- | ----------- | -------------- | -------- | ------------ |
| [26] F. Meng, | L.  | Jagadeesan, | and        | M. Thottan, | “Model-based |                           | reinforcement |     |               |             |                |          |              |
|               |     |             |            |             |              |                           |               |     | focuses on    | graph-based | representation |          | learning and |
| learning      | for | service     | mesh fault | resiliency  | in           | a Web application-level,” |               |     |               |             |                |          |              |
|               |     |             |            |             |              |                           |               |     | explainable   | AI, with    | a particular   | emphasis | on vari-     |
2021,arXiv:2110.13621.
[27] R.Roufetal.,“Instantops:Ajointapproachtosystemfailureprediction ousapplications.
androotcauseidentificationinmicroservicescloud-nativeapplications,”
inProc.15thACM/SPECInt.Conf.Perf.Eng.,2024,pp.119–129.
| [28] A.-C. | Maroudis, | T.          | Theodoropoulos, |        | J. Violos, | A.    | Leivadeas, | and       |     |     |     |     |     |
| ---------- | --------- | ----------- | --------------- | ------ | ---------- | ----- | ---------- | --------- | --- | --- | --- | --- | --- |
| K.         | Tserpes,  | “Leveraging | graph           | neural | networks   | for   | SLA        | violation |     |     |     |     |     |
| prediction | in        | cloud       | computing,”     | IEEE   | Trans.     | Netw. | Service    | Manag.,   |     |     |     |     |     |
vol.21,no.1,pp.605–620,Feb.2024.
| [29] L. Wu,  | J. Tordsson, |                | E. Elmroth, | and       | O. Kao,         | “Microrca: | Root     | cause |     |     |     |     |     |
| ------------ | ------------ | -------------- | ----------- | --------- | --------------- | ---------- | -------- | ----- | --- | --- | --- | --- | --- |
| localization |              | of performance |             | issues in | microservices,” |            | in Proc. | NOMS  |     |     |     |     |     |
IEEE/IFIPNetw.Oper.Manag.Symp.,2020,pp.1–9.
[30] D.Wangetal.,“Interdependentcausalnetworksforrootcauselocaliza-
tion,”inProc.29thACMSIGKDDConf.Knowl.DiscoveryDataMin.,
2023,pp.5051–5060.
| [31] Y. Gan, | G. Liu, | X.  | Zhang, | Q. Zhou, | J. Wu, | and J. Jiang, | “Sleuth: | A   |     |     |     |     |     |
| ------------ | ------- | --- | ------ | -------- | ------ | ------------- | -------- | --- | --- | --- | --- | --- | --- |
trace-basedrootcauseanalysissystemforlarge-scalemicroserviceswith Erno˝ Rigó received the M.Sc. degree in systems
graph neural networks,” in Proc. 28th ACM Int. Conf. Archit. Support engineering from the Budapest University of
Program.Lang.Oper.Syst.,2024,pp.324–337. TechnologyandEconomics.Heiscurrentlypursuing
[32] F. Asadova, G. Kertész, R. Lovas, and S. Szénási, “Fault detection in the Ph.D. degree with Óbuda University. He is
GPU-enabledcloudsystems–anoverview,”inProc.IEEE20thJubilee the Head of the Department of Network Security
WorldSymp.Appl.Mach.Intell.Informat.(SAMI),2022,pp.317–322. and Internet Technologies, Institute for Computer
[33] A. Bianco and L. de Alfaro, “Model checking of probabilistic and ScienceandControl(SZTAKI),HungarianResearch
nondeterministic systems,” in Proc. Int. Conf. Found. Softw. Technol. Network (HUN-REN). He is an Assistant Lecturer
Theor.Comput.Sci.,1995,pp.499–513. with the Institute for Cyber-Physical Systems,
[34] D. C. Verma, “Service level agreements on IP networks,” Proc. IEEE, John von Neumann Faculty of Informatics, Óbuda
vol.92,no.9,pp.1382–1388,2004. University. As an ISACA Certified Information
[35] P. Wieder, J. M. Butler, W. Theilmann, and R. Yahyapour, Service Systems Auditor (CISA) and ISC2 Certified Information Systems Security
LevelAgreementsforCloudComputing.NewYork,NY,USA:Springer. Professional(CISSP),hisPh.D.researchisfocusedonsecurityevaluationof
Nov.2011. dynamic cloud infrastructures. He is responsible for system design, imple-
[36] L. Richardson and S. Ruby, RESTful Web Services. Sebastopol, CA, mentation and day to day operation of the cloud research infrastructure of
USA:O’ReillyMedia,Inc.,2008. HUN-REN.Hiscloudandsecurityrelatedresearchachievementscontributeto
[37] M. Fey and J. E. Lenssen, “Fast graph representation learning with therecentlylaunchedartificialintelligenceandautonomoussystemsnational
| PyTorchgeometric,”2019,arXiv:1903.02428. |     |     |     |     |     |     |     | laboratories. |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |

UNYIetal.:EXPLAINABLEGNN-BASEDAPPROACHTOFAULTFORECASTING 5657
Bálint Gyires-Tóth received the Ph.D. degree RóbertLovasreceivedthePh.D.degreeininformat-
(with summa cum laude) in January 2014. He icsfromtheBudapestUniversityofTechnologyand
is an Associate Professor with BME. He con- Economics.HeistheDeputyDirectorofIT,Institute
ductsresearchonfundamentalandappliedmachine for Computer Science and Control (SZTAKI),
learning since 2007. With his leadership, the first HungarianResearchNetwork(HUN-REN).Heisa
Hungarian hidden Markov-model based Text-To- Habilitated Associate Professor and the Founder of
Speechsystemwasintroducedin2008.Sincethen, the Institute for Cyber-Physical Systems, John von
his primary research field is deep learning. He NeumannFacultyofInformatics,ÓbudaUniversity,
also participates in applied deep learning projects, and a member of the Committee on Information
including time series modeling, anomaly detection, Science with the Hungarian Academy of Sciences.
computer vision, and conversational AI. He was His research and development experience in wide
involved in various successful research and commercial projects. In 2017, rangeofapplicationfieldsofdistributedandparallelsystemshasbeengained
he was certified as a NVidia Deep Learning Institute Instructor and an in various global, EU, and national collaborations with academic organi-
UniversityAmbassador.HisAI-relatedresearchachievementscontributetothe zations, universities, and enterprises focusing on computational chemistry,
artificialintelligencesystemsnationallaboratory.Hismainresearchinterests numerical meteorological modelling, bioinformatics, agriculture, connected
aresequentialdatamodelingwithdeeplearning,self-supervisedlearning,and cars,andIndustry4.0.HehasbeencoordinatingEUFP7/H2020projects,and
deepreinforcementlearning. theHUN-RENCloudresearchinfrastructureofHUN-REN.Hislatestcloud,
bigdata,IoTandAI-relatedresearchachievementscontributetotherecently
launchedartificialintelligenceandautonomoussystemsnationallaboratories.