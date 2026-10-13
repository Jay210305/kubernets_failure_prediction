This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 1
Explainable GNN-based Approach to Fault
Forecasting in Cloud Service Debugging
Da´niel Unyi†, Erno˝ Rigo´∗, Ba´lint Gyires-To´th† and Ro´bert Lovas∗
†Department of Telecommunications and Artificial Intelligence, Faculty of Electrical Engineering and Informatics,
Budapest University of Technology and Economics, Mu˝egyetem rkp. 3., H-1111 Budapest, Hungary.
∗Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN)
Abstract—Debuggingcloudservicesisincreasinglychallenging propagation modeling with GNN-based explainability, which
due to their distributed, dynamic, and scalable nature. Tradi- allowsbothfaultprobabilityestimationandcriticalcomponent
tional methods struggle to handle large state spaces and the
identification within service meshes.
complex interactions between microservices, making it difficult
todiagnosefailuresandidentifycriticalcomponents.Thispaper
presents a Graph Neural Network (GNN)-based approach that
A. Cloud Computing with Reference Architecture and Service
enhancescloudservicedebuggingbypredictingsystem-levelfault
Mesh Concepts
probabilities and providing interpretable insights into failure
propagation. Our method models microservice interactions as Cloudcomputinghastransformedmodernapplicationarchi-
graphs,wherefailurespropagateprobabilistically.UsingMarkov
tectures by enabling scalable, on-demand resource provision-
Decision Processes (MDPs), we simulate failure behaviors, cap-
ing over the internet. As cloud-native applications continue
turingtheprobabilisticdependenciesthatinfluencesystemrelia-
bility. The trained GNN not only predicts fault probabilities but to expand, microservices architectures [1] have become the
also identifies the most failure-prone microservices and explains de facto standard for ensuring scalability, availability, and
theirimpact.Weevaluateourapproachonvariousservicemesh manageability. However, the heterogeneous and distributed
structures, including feature-enriched, tree-structured, and gen-
nature of microservices introduces challenges such as effi-
eraldirectedacyclicgraph(DAG)architectures.Resultsindicate
cient orchestration, secure communication, and observability.
that our method is effective in the operational phase of cloud
services,enablingproactivedebuggingandtargetedoptimization. Managing these interactions becomes particularly difficult as
This work represents a step toward more interpretable, reliable, thenumberofmicroservicesgrows,increasingthecomplexity
and maintainable cloud infrastructures. of debugging and performance monitoring. To address these
Index Terms—Cloud computing, Software debugging, Mi- issues, the service mesh paradigm has emerged as a key
croservice architectures, Deep learning, Graph neural networks, solution.
Explainable AI, Fault prediction Aservicemeshisadedicatedinfrastructurelayerthatman-
ages service-to-service communication, ensuring transparent,
I. INTRODUCTION reliable, and secure interactions between microservices. It
facilitates load balancing, service discovery, traffic manage-
Cloudcomputing’sdistributed,dynamic,andscalablenature
ment, failure recovery, and monitoring, significantly reducing
makes debugging cloud services increasingly complex. Tra-
the overhead associated with microservices orchestration. By
ditional debugging, monitoring, and troubleshooting methods
decouplingservicecommunicationfromapplicationlogic,ser-
struggle to capture the dependencies between microservices.
vice meshes simplify infrastructure management and enhance
One of the greatest challenges in debugging is not just de-
observability.Complementingthis,referencearchitectures[2]–
tecting failures, but understanding why they occur and which
[6] serve as standardized blueprints for cloud service design,
components are responsible. Debugging tools must move
incorporating best practices, interoperability guidelines, and
beyond simple anomaly detection and provide interpretable
reliability principles to improve system resilience.
insights that highlight the root causes of failures and the most
Leadingservicemeshimplementations—Istio,Linkerd,and
influentialmicroservicesaffectingsystemreliability.Toensure
AWS App Mesh [7]—integrate reference architecture princi-
high availability and reliability, there is a critical need for
ples to facilitate microservice communication and manage-
explainable methods that analyze, predict, and clarify cloud
ment. For example, Istio provides advanced traffic manage-
servicebehavior.Tobridgethisgap,ourworkintegratesfailure
ment, security policies, and telemetry collection, establishing
a strong foundation for operational control and observability.
R. Lovas and E. Rigo´ are with the Institute for Computer Science and
Control(SZTAKI),HungarianResearchNetwork(HUN-REN),andwiththe However, while these tools enhance visibility into service in-
JohnvonNeumannFacultyofInformatics,O´budaUniversity,Hungary,email: teractions, analyzing failure propagation across microservices
{robert.lovas,erno.rigo}@sztaki.hun-ren.hu
remains a challenge, requiring additional techniques to assess
D. Unyi and B. Gyires-To´th are with the Department of Telecom-
munications and Artifical Intelligence, Faculty of Electrical Engineer- system reliability and performance.
ing and Informatics, Budapest University of Technology and Economics, In summary, service meshes and reference architectures
email:{unyi.daniel,toth.b}@tmit.bme.hu
improve operational efficiency, security, and observability, but
B. Gyires-To´th and R. Lovas contributed equally to this work and share
seniorauthorship. effectively analyzing service behavior still requires additional
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 2
Fig.1. Classificationofgeneraldistributeddebuggingmethodologies[8]extendedwithourplannedresultsinservicemeshenvironment(greybackground).
tools that can track dependencies and evaluate system perfor- visibility into how failures emerged. This lack of systematic
mance under failure conditions. failure reproduction hinders efforts to anticipate and mitigate
faults before they escalate.
B. Debugging Challenges
C. Theoretical Background and Research Plan
Debugging service mesh architectures can be challenging
due to their complexity and distributed nature [9]. A primary Distributed debugging methodologies can be classified
issueisobservability,whichreferstoanalyzingsystembehav- based on their support for global predicate specification and
ior and inter-service communication. In practice, only partial detection, as well as their ability to identify root causes of
observabilityisoftenpossibleduetofactorssuchasblack-box software bugs in distributed systems [8]. Over time, these
(proprietary)servicesorprobeeffects,wheremonitoringtools methodologies have evolved to address the limitations of
can influence system behavior. This incomplete view makes it previous approaches. Figure 1 summarizes these methods and
difficult to determine which microservices contribute most to highlights our planned contributions in service mesh environ-
system failures and how faults propagate through the mesh. ments (grey background).
Beyond observability, identifying and diagnosing faults in At the most basic level, interactive debugging extends
large-scale service meshes is particularly challenging. Config- traditionalsequentialdebuggingtoremoteprocesses,allowing
uration errors, misrouted traffic, and performance bottlenecks real-time monitoring but lacking insight into inter-process
can cause latency spikes, service degradation, and system interactions, making it unsuitable for distributed systems. To
faults [10]. However, tracing these issues back to their root overcome this, the “Trace, replay and debugging” approach
cause is difficult because service meshes abstract communi- (Figure 1, row 2) records selected execution traces to enable
cation details, making failure propagation paths non-trivial to deterministicreproductionoffaultybehaviorsundercontrolled
reconstruct.Debugginginter-servicefailuresisfurthercompli- conditions.
cated by dynamic workloads and ephemeral service instances, Building on this, the “Integrated testing, active control and
where failures may only manifest intermittently or under debugging” (Figure 1, row 3) introduces mechanisms that
specific operating conditions. steerexecutionalongpredefinedcomputationpaths,improving
Additionally, failures in service meshes are often difficult reproducibility beyond passive observation. A more advanced
to reproduce, making root cause analysis highly reactive technique,“Predicatedetection,activecontrolanddebugging”
rather than proactive. Without effective replay mechanisms, (Figure1,row4),allowsuserstodefinecorrectnessconditions
debugging relies on post-mortem analysis, where engineers (predicates) that are continuously evaluated during execution,
must manually analyze logs and traces, often with limited enhancing systematic failure detection.
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 3
Fig.2. Proposedframeworkfordebuggingcyclewithtoolsanddataflow.
Oneofourpreviousworksextendedthismethodologytothe (e.g., routing rules, load balancing), security policies (e.g.,
deploymentphaseoforchestratedcloudservices[11],focusing authentication, authorization), and observability features (e.g.,
on improving reliability (including platform-agnostic behav- telemetry, logging). These descriptors allow fine-grained con-
ior) in complex deployment strategies. This approach proved troloverservicebehaviorwithoutmodifyingapplicationcode,
useful in detecting timing or architecture-dependent failures makingthemanidealfoundationforourdebuggingframework
within deployment descriptions and orchestration steps. (Figure 2, ”Service Mesh Description”).
| This           | research    | further  | narrows  | the       | scope              | to developing |            | a              |               |            |             |                        |          |           |            |
| -------------- | ----------- | -------- | -------- | --------- | ------------------ | ------------- | ---------- | -------------- | ------------- | ---------- | ----------- | ---------------------- | -------- | --------- | ---------- |
|                |             |          |          |           |                    |               |            | The “Predicate |               | detection, |             | active                 | control, | and       | debugging” |
| smart steering | mechanism   |          | within   | the       | ”Smart             | Control,      | Debug-     |                |               |            |             |                        |          |           |            |
|                |             |          |          |           |                    |               |            | approach       | is embedded   |            | within      | the “Steering”-related |          |           | compo-     |
| ging, and      | Evaluation” |          | paradigm | (Figure   |                    | 1, row        | 5). In our |                |               |            |             |                        |          |           |            |
|                |             |          |          |           |                    |               |            | nents of       | our framework |            | (gray       | route in               | Figure   | 2). The   | ‘PRISM     |
| previous       | work        | [12], we | applied  | the       | PRISM              | simulator     | envi-      |                |               |            |             |                        |          |           |            |
|                |             |          |          |           |                    |               |            | simulator      | environment   |            | with model  | checker’               |          | detects   | suspicious |
| ronment        | with model  | checker, |          | along     | with autoencoders, |               | Long       |                |               |            |             |                        |          |           |            |
|                |             |          |          |           |                    |               |            | paths or       | nodes         | and        | labels them | to                     | steer    | debugging | efforts    |
| Short-Term     | Memory      |          | (LSTM)   | networks, |                    | and Graph     | Neural     |                |               |            |             |                        |          |           |            |
towardcriticalareas.Inourpreviouswork[12],wedeveloped
| Networks | (GNNs), | to  | analyze | system | behavior. |     | Extending |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | ------- | ------ | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
asimplifiedservicemeshmodel,representingRESTfulservice
| beyond           | this, in | this paper         | we  | focus | on leveraging |           | GNNs for |           |                  |     |         |                 |          |                   |          |
| ---------------- | -------- | ------------------ | --- | ----- | ------------- | --------- | -------- | --------- | ---------------- | --- | ------- | --------------- | -------- | ----------------- | -------- |
|                  |          |                    |     |       |               |           |          | nodes as  | a dependency     |     | tree.   | This was        | extended | into              | a REST   |
| fault prediction |          | and explainability |     |       | to enhance    | debugging |          | in        |                  |     |         |                 |          |                   |          |
|                  |          |                    |     |       |               |           |          | modeling  | framework        |     | using a | domain-specific |          | language          | (DSL)    |
| cloud service    | meshes.  |                    |     |       |               |           |          |           |                  |     |         |                 |          |                   |          |
|                  |          |                    |     |       |               |           |          | to define | probabilistic    |     | service | interactions,   |          | allowing          | the gen- |
|                  |          |                    |     |       |               |           |          | eration   | of probabilistic |     | state   | machines        | for      | each microservice |          |
D. Proposed Debugging Framework based on its strategy and network connections. Our PRISM-
|      |              |     |       |      |           |        |         | based model | generator |           | translates | these  | DSL           | descriptions | into   |
| ---- | ------------ | --- | ----- | ---- | --------- | ------ | ------- | ----------- | --------- | --------- | ---------- | ------ | ------------- | ------------ | ------ |
| This | paper shifts | the | focus | from | debugging | during | the de- |             |           |           |            |        |               |              |        |
|      |              |     |       |      |           |        |         | Markov      | Decision  | Processes |            | (MDPs) | by generating |              | module |
ploymentphasetodebuggingduringoperation,wherefailures
|     |     |     |     |     |     |     |     | descriptions | in  | PRISM | for all | nodes | and their | dependencies. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ------- | ----- | --------- | ------------- | --- |
oftenariseduetodynamicinteractionsbetweenmicroservices.
|              |            |     |                |     |      |            |       | Once validated, |     | RESTful | communication |     |     | flows | of arbitrary |
| ------------ | ---------- | --- | -------------- | --- | ---- | ---------- | ----- | --------------- | --- | ------- | ------------- | --- | --- | ----- | ------------ |
| Our approach | introduces |     | explainability |     | into | debugging, | using |                 |     |         |               |     |     |       |              |
lengthcanbesimulated.Additionally,PRISMperformsformal
| Graph Neural | Networks      |     | (GNNs) | to      | not only | predict       | system- |               |          |     |           |           |           |     |             |
| ------------ | ------------- | --- | ------ | ------- | -------- | ------------- | ------- | ------------- | -------- | --- | --------- | --------- | --------- | --- | ----------- |
|              |               |     |        |         |          |               |         | verification, | ensuring |     | the model | satisfies | specified |     | correctness |
| level fault  | probabilities |     | but    | also to | provide  | interpretable | in-     |               |          |     |           |           |           |     |             |
sightsintofailurepropagationandrootcauses(seeblackroute properties using probabilistic model checking. This allows
|              |            |             |               |         |              |        |            | us to define |         | temporal | logic       | properties | and | systematically   |     |
| ------------ | ---------- | ----------- | ------------- | ------- | ------------ | ------ | ---------- | ------------ | ------- | -------- | ----------- | ---------- | --- | ---------------- | --- |
| in Figure    | 2). Unlike |             | deterministic |         | replay-based |        | debugging, |              |         |          |             |            |     |                  |     |
|              |            |             |               |         |              |        |            | analyze      | failure | cases,   | identifying | deadlocks, |     | inconsistencies, |     |
| which relies | on         | replicating | failure       | states, | our          | method | uses ob-   |              |         |          |             |            |     |                  |     |
andfailureprobabilities[13](see‘Generated&labeledtraces’
| served data | to improve |     | fault localization |     | and | guide | debugging |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------------------ | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
in Fig. 2).
efforts.
Our approach builds on the service mesh paradigm, which In this paper, we propose a debugging framework that inte-
providesastructured,policy-drivenenvironmentformanaging grates Graph Neural Networks (GNNs) within the ‘Training’-
microservices.Servicemeshdescriptors,suchasthoseinIstio, related components (white route in Figure 2). Our approach
define critical configurations for network traffic management (seeSectionIV)addressesthechallengeofdebuggingcomplex
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 4
service meshes by leveraging fault probability prediction and learningtoimprovefaultdiagnosisandprediction.Thefollow-
GNN-based explainability to identify weak components (see ing subsections discuss both traditional and ML-based fault
SectionIV-C).Insteadofrelyingsolelyondeterministicreplay detection approaches, with a particular focus on GNN-based
or exhaustive model checking, our method learns from ob- methods for service meshes.
| served system | behavior |         | to prioritize | high-risk    | execution |            | paths |                |       |                 |          |         |         |           |     |
| ------------- | -------- | ------- | ------------- | ------------ | --------- | ---------- | ----- | -------------- | ----- | --------------- | -------- | ------- | ------- | --------- | --- |
| and potential | failure  | states. | Key           | components   | include:  |            |       |                |       |                 |          |         |         |           |     |
|               |          |         |               |              |           |            |       | A. Traditional |       | Fault Detection |          | Methods |         |           |     |
| Training      | a        | GNN to  | predict       | system-level | fault     | probabili- |       |                |       |                 |          |         |         |           |     |
| •             |          |         |               |              |           |            |       | Rule-based     | fault | detection       | methods, |         | such as | intrusion | and |
ties,usingservicemeshgraphswherenodesrepresentmi- anomaly detection systems, monitor network or host activity
| croservices |     | and edges | capture | inter-service |     | interactions. |     |                |     |               |     |          |             |     |         |
| ----------- | --- | --------- | ------- | ------------- | --- | ------------- | --- | -------------- | --- | ------------- | --- | -------- | ----------- | --- | ------- |
|             |     |           |         |               |     |               |     | for deviations |     | from expected |     | behavior | [19]. These |     | methods |
GNN-basedexplainabilitytoidentifycriticalcomponents,
| •   |     |     |     |     |     |     |     | rely on | either | signature-based |     | detection, | using | predefined |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------------- | --- | ---------- | ----- | ---------- | --- |
selecting a minimal but informative subgraph that pre- anomaly patterns, or anomaly-based detection, identifying
| serves    | predictive | accuracy.   |           |                 |               |          |      |              |            |            |           |            |           |           |        |
| --------- | ---------- | ----------- | --------- | --------------- | ------------- | -------- | ---- | ------------ | ---------- | ---------- | --------- | ---------- | --------- | --------- | ------ |
|           |            |             |           |                 |               |          |      | statistical  | deviations | from       | normal    | system     | behavior. |           | Abbasi |
| Automated |            | generation, |           | augmentation,   | and           | labeling | of   |              |            |            |           |            |           |           |        |
| •         |            |             |           |                 |               |          |      | et al. [20]  | propose    | an         | anomaly   | detection  | system    | for       | cloud  |
| training  | data       | using       | the PRISM | simulator/model |               | checker, |      |              |            |            |           |            |           |           |        |
|           |            |             |           |                 |               |          |      | data centers | that       | enhances   | fault     | resilience | through   | real-time |        |
| which     | allows     | the         | GNN       | to learn from   | probabilistic |          | exe- |              |            |            |           |            |           |           |        |
|           |            |             |           |                 |               |          |      | monitoring   | and        | behavioral | analysis. |            |           |           |        |
cution traces (white route in Figure 2, see also Section Beyondanomalydetection,automatedtestingandresilience
III).
|             |           |        |           |             |             |            |         | strategies    | have      | been explored |       | for service | meshes.  |              | Karn et |
| ----------- | --------- | ------ | --------- | ----------- | ----------- | ---------- | ------- | ------------- | --------- | ------------- | ----- | ----------- | -------- | ------------ | ------- |
| Combining   |           | Markov | Decision  | Process     | (MDP)       | modeling   |         |               |           |               |       |             |          |              |         |
| •           |           |        |           |             |             |            |         | al. [21]      | introduce | a framework   |       | that        | monitors | microservice |         |
| with        | GNN-based |        | learning, | where       | MDPs encode |            | service |               |           |               |       |             |          |              |         |
|             |           |        |           |             |             |            |         | communication |           | traces,       | using | component   | fault    | injectors    | to      |
| interaction | dynamics, |        | and       | GNNs refine | failure     | prediction |         |               |           |               |       |             |          |              |         |
simulatedelays,trafficrestrictions,andterminations.Theirap-
and debugging automation. proachdetectsfaultyconnectionsviadashboardsandmitigates
Thesuspicioussituationsdetectedbypre-trainedGNNsmay
|     |     |     |     |     |     |     |     | issues through |     | scaling, | failover, | and circuit | breakers, |     | offering |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --------- | ----------- | --------- | --- | -------- |
realize ‘Smart steering’ (black route in Figure 2), allowing a reactive mechanism for service reliability.
| cloud debugging |     | tools | [11], [14] | to proactively |     | identify | and |        |          |            |     |      |           |         |     |
| --------------- | --- | ----- | ---------- | -------------- | --- | -------- | --- | ------ | -------- | ---------- | --- | ---- | --------- | ------- | --- |
|                 |     |       |            |                |     |          |     | Formal | modeling | techniques |     | have | also been | applied | to  |
localizefailures.ThisprocesscanbypassthePRISMsimulator fault analysis in cloud environments. Cao and Niu [22] apply
environment and model checker, as the trained GNN can higher-orderMarkovgraphstoanalyzeclouddeploymentsand
| directly analyze |     | service | mesh | descriptions. | Our | experimental |     |          |                   |     |         |         |           |          |     |
| ---------------- | --- | ------- | ---- | ------------- | --- | ------------ | --- | -------- | ----------------- | --- | ------- | ------- | --------- | -------- | --- |
|                  |     |         |      |               |     |              |     | big data | logs, identifying |     | complex | failure | patterns. | However, |     |
results (see Sections V and VI) demonstrate the effectiveness their approach lacks an active control mechanism to steer the
of GNN-based explainability in detecting critical components debugging process toward critical failure states.
and operating under limited observability conditions. Pontilloetal.[23]proposeFERRARI,afailurereproduction
toolthatgeneratestestcasesandanalyzesstacktracestoiden-
II. RELATEDWORKS tifyfaults.FERRARIincludesasimilarityscoringmechanism
toestimatehowcloselygeneratedtestcasesmatchrealfailure
Withtheincreasingcomplexityofcloudarchitectures,main-
conditions.Whiletheirtoolaidsinfailurereproduction,itdoes
tainingsystemstabilityandfaultdetectionhasbecomeacriti-
|     |     |     |     |     |     |     |     | not incorporate |     | ML-guided | steering | as  | in our work. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | -------- | --- | ------------ | --- | --- |
calchallenge.Continuousmonitoringcollectslogsonmemory
| issues, server  | failures, |         | and application |              | performance | [15], | but     |            |          |       |       |           |         |     |     |
| --------------- | --------- | ------- | --------------- | ------------ | ----------- | ----- | ------- | ---------- | -------- | ----- | ----- | --------- | ------- | --- | --- |
|                 |           |         |                 |              |             |       |         | B. Machine | Learning | Based | Fault | Detection | Methods |     |     |
| the vast volume |           | of logs | makes           | it difficult | to promptly |       | isolate |            |          |       |       |           |         |     |     |
faults and take proactive measures before system failures Machine learning-based fault detection methods generally
| occur. Moreover, |     | failure | datasets | are typically | much | smaller |     |           |            |     |              |     |             |            |     |
| ---------------- | --- | ------- | -------- | ------------- | ---- | ------- | --- | --------- | ---------- | --- | ------------ | --- | ----------- | ---------- | --- |
|                  |     |         |          |               |      |         |     | fall into | supervised | and | unsupervised |     | categories. | Supervised |     |
than complete system logs, making fault analysis challenging. models learn to distinguish between normal and faulty behav-
Farooq et al. define faults as abnormal conditions that ior using labeled input-output pairs, making them effective
reduceoreliminateacomponent’sabilitytofunctioncorrectly, when labeled data is available. In contrast, unsupervised
with failures emerging as their observable consequences [16]. approaches detect anomalies by identifying deviations from
| Identifying | root | causes | before | failures | manifest | is crucial | for |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------ | ------ | -------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
normalpatternswithoutrequiringexplicitfaultlabels,allowing
proactive debugging. them to adapt to previously unseen failure modes.
Traditional formal verification methods have been applied Zhang et al. [24] propose an online fault detection model
to analyze cloud architectures, particularly in service-oriented forcloudsystemsusingasupportvectormachine(SVM)with
environments. Zatout et al. [17] propose transaction modeling automated parameter tuning (SVM-Grid). Their approach im-
for improving reliability in RESTful applications, while Souri proves fault prediction by selecting relevant system attributes
et al. [18] review service composition verification techniques. via Pearson correlation and principal component analysis
These studies highlight the importance of formal methods in (PCA).Whileeffective,itfocusesongeneralcloudfaultdetec-
ensuring the robustness of RESTful systems. tion and does not explicitly model inter-service dependencies
Although formal methods provide strong guarantees, their within service meshes.
applicability to large-scale, dynamic service meshes is limited Zhou et al. [25] introduce MEPFL, a machine learning-
due to computational cost and reliance on predefined models. based method for latent error prediction and fault localization
Inordertoaddresstheselimitations,data-drivenfaultdetection in microservice applications. It leverages system trace logs to
methods have emerged, using statistical analysis and machine trainmodelsatboththetraceandmicroservicelevels,allowing
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 5
TABLEI
COMPARISONOFSELECTEDRELATEDWORKS.(ML:MACHINELEARNING)
reference architecturelevel approach appliedmethods focusarea faultinjection
Smara[19] component rule-based signature/anomalydetection componentsafety manual
Abbasi[20] networklevel rule-based behavioralanalysis networkanomalydetection manual
Karn[21] servicemesh automatedtesting faultinjection,rule-basedanalysis communicationreliability semi-automated
Cao&Niu[22] cloudservice stochasticmodel Higher-orderMarkovGraph faultanalysisincloudlogs N/A
Pontillo[23] servicemesh automatedtesting test-casegeneration,similarityscoring failurereproduction N/A
Zhang[24] system ML(supervised) SVM+PCA+Pearsoncorrelation generalfaultdetection N/A
Zhou[25] microservice-level ML(supervised) loganalysis,traceclassification latenterrorprediction semi-automated
Meng[26] servicemesh ML+RL reinforcementlearning,CTMC resiliencestrategyoptimization semi-automated
Rouf[27] servicemesh ML GNN+GRU+permutationtesting failureprediction+RCA N/A
Maroudis[28] client-servicenetwork GNN graph-basedSLAviolationprediction SLAprediction N/A
Wu[29] microservice-level GNN anomalytracing,rootcauselocalization performancediagnosis N/A
Wang[30] cross-networksystem GNN+EVT topologicalcausaldiscovery faultlocalization N/A
Gan[31] microservices unsup.GNN trace-levelrootcauseanalysis debugging N/A
Lovas[11],[12] multi-level ML,GNN autoencoder,LSTM,GNN,MDP genericdebugging automated
Thispaper servicemesh GNN+XAI MDP-basedfailuresimulation criticalcomponentidentification automated
real-time fault detection and classification. By analyzing exe- Wu et al. [29] introduces MicroRCA, an attributed graph
cution traces and incorporating fault injection during training, model to trace anomaly propagation across services and ma-
MEPFL improves failure diagnosis in dynamic production chines in microservice architectures. It performs real-time
environments. However, it primarily focuses on predicting root cause localization by correlating application performance
fault occurrences rather than modeling how failures propagate symptomswithsystemresourceutilization.Whileeffectivefor
within a service mesh. diagnosingperformanceissues,itsprimaryfocusisonlinking
Meng et al. [26] present a reinforcement learning approach performance anomalies to resource bottlenecks, making it
to predict fault resilience behaviors in service meshes. Their complementary to our work.
method optimizes service-level configurations that influence Wang et al. [30] applies hierarchical graph neural net-
request-response behavior under failure conditions, which en- works to discover intra-network and cross-network causal
ablesadaptivefaultresiliencestrategiesacrossbothindividual dependencies for fault localization. It combines topological
services and multi-service orchestrations. While effective for causal discovery with an Extreme Value Theory (EVT)-based
mitigating faults, this approach emphasizes policy optimiza- method to rank probable root causes. This approach is well-
tion rather than failure probability estimation or interpretable suited for analyzing multi-level causal interactions but does
fault propagation modeling. not explicitly account for the role of service dependencies in
Rouf et al. [27] propose InstantOps, a multi-modal failure fault propagation.
prediction and root cause analysis (RCA) framework that Gan et al. [31] introduce a trace-based root cause anal-
integrates logs, metrics, traces, and microservices events. It ysis system, Sleuth, for large-scale microservices, using an
constructs a dynamic service call flow graph, where traces unsupervised GNN to assess the causal impact of each span
define the structure, while logs and resource metrics enrich in a trace. It clusters traces using a trace distance metric to
node attributes. InstantOps applies GNNs to capture spatial reduce the data volume required for root cause localization,
dependencies and Gated Recurrent Units (GRUs) to model with a strong emphasis on transferability across microservice
temporal failure patterns, enabling proactive failure prediction applications.WhileSleuthfocusesonperformancedebugging,
and precise root cause localization. Moreover, permutation our work provides a complementary perspective by learning
testingisusedtoassessnodeimportancewithinfailurepropa- an explicit failure propagation model and identifying critical
gation chains. While InstantOps effectively fuses multi-modal subgraphs responsible for system faults.
observabilitydataandmodelsbothspatialandtemporalfailure Table I provides a comparative overview of selected related
dynamics, it differs from our work, which explicitly learns worksaccordingto(i)thearchitecturalleveltheytarget,(ii)the
a failure propagation model to identify critical subgraphs overallapproachtheyapply,(iii)theprimarymethodsapplied,
contributing to system faults. (iv) their main focus areas, and (v) the strategy used for fault
injection. This comparative analysis is partially informed by
the survey presented in [32].
C. Graph Neural Network Based Fault Detection
Our previous work [12] introduced a preliminary GNN-
Maroudis et al. [28] investigate SLA violation predic- based fault prediction model for service meshes, leveraging
tion using GNNs, exploring time series, content-based, and a simplified RESTful service model with a dependency tree
context-based (graph-based) data representations. Their study structure. This model was integrated with a domain-specific
demonstrates that graph-based representations significantly language (DSL) to define probabilistic service interactions,
enhance prediction accuracy by capturing the associativity of enablingthegenerationofprobabilisticstatemachinesforeach
clientsandintegratingthemwithtraditionalmodels.However, microservice.Faultpropagationdynamicswerecapturedusing
their approach is concerned with SLA violations rather than Markov Decision Processes (MDPs), and the framework was
analyzingfailurepropagationoridentifyingstructurallycritical validated using formal verification techniques. Even though
components in cloud services. thispreliminaryworkdemonstratedtheapplicabilityofGNNs
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 6
for failure prediction, it was limited to tree structured service betweenthecloudserviceproviderandtheend-user.Thiskind
meshes and lacked a dedicated explainability mechanism for of service measurement was first employed in IP networks
identifying the most critical service components contributing [34].Theconceptthenwaswidelyadoptedbyvarioussectors,
to failures. including cloud applications [35].
Building on this foundation, our current work generalizes Although transient errors or permanent disruptions that
the approach by extending the tree-structured service mesh result in a performance degradation might play a major role
model to feature-enriched, directed acyclic graph (DAG) ser- in overall debugging of a cloud application, for the time of
vice meshes. Unlike the earlier model, the new one supports current research we are focusing on fatal service situations.
node-level features such as failure probability (for leaf nodes) For this purpose service level is defined as the probability of
andretrycount(forintermediarynodes).Theseenhancements fatal service disruption (system fault) observed by the end-
offeramorerealisticrepresentationofserviceinteractionsand user. Contrary to the common practice of representing service
failure dependencies. availabilityasthepercentageratioofacceptablemetricsvalues
Our updated approach integrates GNN-based explainability over time (e.g., requests are answered 99.995% within a
to identify critical subgraphs and failure-prone microservices. specific period of time), we are representing fatal system
Theidentifiedcriticalsubgraphsprovidehintsforactivesteer- disruption probability value (or in short, fault) as a standard
ing of a cloud debugger tool towards the suspicious situations probability value (e.g., requests are failing with a probability
(component faults), allowing proactive fault localization and of 0.005 in the observed simulation window).
mitigation.
C. Service Mesh Architectures
III. MODELLINGSERVICEMESHESFORCLOUD In order to generalize and refine our models further lever-
REFERENCEARCHITECTURES aging on our previous achievements [12], we continued to
A. Framework investigate various methods of describing cloud use cases.
Microservice-based architecture patterns, also known as ser-
Current modelling efforts build upon our previous work
vice meshes, are becoming increasingly popular in modern
focusing on probabilistic model checking applications, more
cloud applications [36].
specifically the PRISM model checker [13] is employed to
Cloud applications were chosen to be modelled as a set
describe, simulate and formally validate models expressed as
of loosely coupled web services. Intra-application integration
Markov decision processes (MDPs).
is achieved by applying various services of the mesh service
During further developments of the model, the PRISM
component. From these integration services, message inter-
language is used to define parallel composition of modules
ception and routing is observed to be most feasible to aid in
describing various behavioural patterns in different cloud
simulation of RESTful cloud application services [37].
application modules. These patterns are composed of vari-
Ourpreviousmodellingeffortswereaimingtowardssimpli-
ous communication actions also serving as synchronization
fied representation of a RESTful service model by organizing
points between the modules. Critical model parameters and
applicationcomponentsbytheirdependencyrelationshipsinto
variousfeaturesofinterestsareidentifiedbyPRISMlabelsto
a directed acyclic graph (DAG), where the root node R
aid tracking of behaviour changes in the cloud application.
is representing the user facing service component of the
Parametric generation of various experiments is based on
application.Inthemodel,Riscontinuouslytriggeringrequests
constants that provide a straightforward method to adjust
tointermediarynodesnandleafnodesm.Requestsarerouted
behavioural properties of the simulated application context.
in a nondeterministic way from R through various number of
Our work has gradually shifted from constrained or uncon-
intermediaries (n) ultimately arriving to a leaf m.
strained path simulation applications towards formal model
Two constants are introduced on the graph level to better
checking against various properties described as probabilis-
describe application behaviour P is the probability of
tic linear temporal logical expressions, such as PCTL [33]. fail
failure of any leaf node (m), while retries is a parame-
Ultimately, these expressions were used to define end-user
ter of intermediaries (n) representing number of request re-
observable features of the simulated cloud application, most
transmissionattemptsbeforegivinguponanerror.Responses
prominently service availability or error rate provided by the
of the application are originating from leaf nodes (m) then
user interface.
propagated back through a series of intermediaries (n) to be
ultimatelyaggregatedatRenablingobservationofapplication
B. Faults in a Cloud Application
error rates.
Errorsinacloudapplicationcanresultineithertransientor Based on this approach, each user request is simulated
permanentdisruptionoftheirservices.Fromtheperspectiveof as a single chain of requests and responses along a path
end-users these disruptions result in performance degradation [R,n ,n ,...,n ,m], representing each complex request by
1 2 x
or - in severe cases - functional or data losses. forming a random depth-first search (DFS) path walk, com-
Measurement efforts of cloud application quality aims to plete with occasional back-traces as instructed by the retries
quantify these properties. In cases of formal service agree- parameter. Figure 3 illustrates a RESTful service mesh appli-
ments, these quantitative metrics play a key role. Thresholds cation model based on a random DAG.
forthesemetrics,includingtheacceptablerateofsystemfaults In the course of our current work, model-level constants
are often established in a Service Level Agreement (SLA) P and retries were further enhanced to become local
fail
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 7
|     |     |     |     |     |     |     | iments with | subcases |          | of topologically |     | equivalent | application |         |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | ---------------- | --- | ---------- | ----------- | ------- |
|     |     |     |     |     |     |     | models,     | but with | distinct | random           |     | values     | for P fail  | [m] and |
retries[n].
|     |     |     |     |     |     |     | A generic | algorithm |     | for dataset | generation |     | is supplied | as  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ----------- | ---------- | --- | ----------- | --- |
pseudocodeinAlgorithm1.Statementswithexportkeywords
representrecordsoutputaspartofthedataset.Statementswith
|     |     |     |     |     |     |     | generate        | and filter |               | keywords | represent | custom      | Python     | code     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------- | -------- | --------- | ----------- | ---------- | -------- |
|     |     |     |     |     |     |     | by the authors, |            | generatePAs() |          | is        | responsible | for        | deriving |
|     |     |     |     |     |     |     | probabilistic   | automatons |               | (PAs)    | for nodes | of          | a directed | graph,   |
generatePRISM()willthentranslatethisPArepresentation
|     |     |     |     |     |     |     | into PRISM      | source         | code.    | Statements |                      | with       | random        | keyword |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | -------- | ---------- | -------------------- | ---------- | ------------- | ------- |
|     |     |     |     |     |     |     | annotate        | random         | data     | generation | with                 | uniform    | distribution. |         |
|     |     |     |     |     |     |     | Finally,        | pathSimulation |          | and        | checkFaultExpression |            |               | rep-    |
|     |     |     |     |     |     |     | resent external |                | calls to | the PRISM  | model                | checker.   |               |         |
|     |     |     |     |     |     |     | Algorithm       | 1 pseudocode   |          | for        | dataset              | generation |               |         |
Fig.3. Simpleservicemeshapplicationtopology
|            |     |        |                  |     |                 |     | 1: for                   | all cases     | do  |     |       |     |     |     |
| ---------- | --- | ------ | ---------------- | --- | --------------- | --- | ------------------------ | ------------- | --- | --- | ----- | --- | --- | --- |
|            |     |        |                  |     |                 |     | D                        | :=randomDAG(n |     |     | )     |     |     |     |
|            |     |        |                  |     |                 |     | 2:                       |               |     |     | nodes |     |     |     |
| properties | of  | leaf m | and intermediary | n   | nodes, becoming |     |                          |               |     |     |       |     |     |     |
|            |     |        |                  |     |                 |     | 3: G:=insertDFSEdges(D,p |               |     |     |       | )   |     |     |
down
P [m] and retries[n] respectively. This approach then was for all subcases do
| fail    |          |               |                 |     |      |        | 4:  |         |      |         |     |     |     |     |
| ------- | -------- | ------------- | --------------- | --- | ---- | ------ | --- | ------- | ---- | ------- | --- | --- | --- | --- |
| further | enhanced | by conducting | a breadth-first |     | walk | on the |     |         |      |         |     |     |     |     |
|         |          |               |                 |     |      |        | 5:  | for all | n in | G.nodes | do  |     |     |     |
DAG to group nodes by their distance d from the root node, 6: if isLeaf(n) then
thus forming node sets at different levels n of the DAG. n.P :=random(p ,p )
|              |     |            |               |     | d       |        | 7:  |     | fail |     | min | max |     |     |
| ------------ | --- | ---------- | ------------- | --- | ------- | ------ | --- | --- | ---- | --- | --- | --- | --- | --- |
| New requests |     | paths then | were injected | to  | the DAG | in the |     |     |      |     |     |     |     |     |
|              |     |            |               |     |         |        | 8:  | end | if   |     |     |     |     |     |
formofedges(e)sothattheyonlytraverseforwardtheDAG, 9: if isInternal(n) then
| ∀e (n   | ,n      | )|d <       | d . Figure 4 | illustrates | the previous     |     |     |                     |     |     |     |        |       |     |
| ------- | ------- | ----------- | ------------ | ----------- | ---------------- | --- | --- | ------------------- | --- | --- | --- | ------ | ----- | --- |
| new     | d1 d2   | 1           | 2            |             |                  |     | 10: | n.retries:=random(r |     |     |     | min ,r | max ) |     |
| RESTful | service | application | model        | with        | injected forward |     | 11: | end                 | if  |     |     |        |       |     |
| edges.  |         |             |              |             |                  |     |     | end for             |     |     |     |        |       |     |
12:
|     |     |     |     |     |     |     | 13: | exportGEXF(id      |     | subcase | ,G) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 14: | S :=generatePAs(G) |     |         |     |     |     |     |
P :=generatePRISM(S)
15:
|     |     |     |     |     |     |     | 16: | path:=pathSimulation(P) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
exportPath(path)
17:
|     |     |     |     |     |     |     | 18: | actions:=filterActions(path) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 19: | exportActions(actions)       |     |     |     |     |     |     |
fault:=checkFaultExpression(P)
20:
|     |     |     |     |     |     |     | 21: | exportFault(id |     |     | ,fault) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------- | --- | --- | --- |
subcase
end for
22:
|     |     |     |     |     |     |     | 23: exportStatistics(subcases) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 24: end                        | for |     |     |     |     |     |     |
exportStatistics(cases)
25:
Algorithm1outlinesaprocedureforgeneratingdatasetsthat
|     |     |     |     |     |     |     | simulate | RESTful | service | mesh | applications |     | using | directed |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | ---- | ------------ | --- | ----- | -------- |
Fig.4. Servicemeshapplicationtopologywithforwardedges-modification
|     |     |     |     |     |     |     | acyclic | graphs | (DAGs) | and | stochastic | modeling | tools | like |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------ | --- | ---------- | -------- | ----- | ---- |
ofgraphonFigure3
probabilisticautomatons(PAs)andthePRISMmodelchecker.
|            |          |     |               |             |               |     | The process | begins |     | with iterating | over | different | application |     |
| ---------- | -------- | --- | ------------- | ----------- | ------------- | --- | ----------- | ------ | --- | -------------- | ---- | --------- | ----------- | --- |
| It is also | possible | to  | calculate the | probability | of an overall |     |             |        |     |                |      |           |             |     |
application failure by checking the numerical value of the cases. For each case, a random DAG (D) is generated to
P =?[F < TR ], R representthearchitectureoftheapplication.Directededgesare
| expression | max |     | failure | where | failure | is the |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | ------- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
“failure” state of the root node (R) and T is the number of theninsertedintothisgraphtosimulatepotentialrequestpaths,
model transitions measured from the initial state of “polling”. guided by a probability (p ) of establishing downward
down
connectionsthatrespectthehierarchicalstructureoftheDAG.
| Availability | of  | the application | for a | given | period of time | T   |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | ----- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
can also be considered a closely related property to P . Withineachsubcase,nodesinthegraphareclassifiedbased
max
These enhancements further enhanced our simulation and on their role: either as leaf nodes or intermediary nodes. Leaf
training data generation capabilities, enabling modelling of nodes, which handle end-user requests, are assigned a failure
RESTful cloud applications with increased complexity. New probability (P ) generated randomly within defined bounds
fail
node-level parameters enabled clustering of previous exper- ((p min , p max )). Intermediary nodes are configured with a
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 8
parameter denoting the number of retry attempts in case of
failures, also determined randomly ((r , r )).
min max
The graph structure and its configurations are exported in
GEXF format for interoperability and further analysis. The
procedural transformation then involves deriving probabilistic
automatonsforthegraphnodes,whicharesubsequentlytrans-
lated into the PRISM modeling language to facilitate formal
verification and model checking of the stochastic models. A
simulation of request paths is conducted, tracing the routes
of requests across the service mesh to assess the pathways
utilized.
Pathway data is exported for analysis, while actionable
events within these paths are filtered for further inspection
andexportedseparately.Toascertaintherobustnessofthesub-
cases, a formal check is performed for expressions indicating
Fig.5. TheproposedGNNarchitectureforfaultprobabilityprediction.
systemfaultsusingthePRISMmodelchecker,withtheresults
recorded alongside the respective subcase identifiers.
Thealgorithmconcludesbyaggregatingstatisticaldatafrom
B. GNN Training for Fault Prediction
individual subcases and cases, exporting these statistics to
serve as a comprehensive dataset that encapsulates the behav- To identify critical components within a service mesh,
ior and properties of the simulated service mesh applications it is essential to have a strong baseline GNN model for
under varied conditions. fault probability prediction. With a well-trained model, we
can assess how the removal of certain parts of the service
IV. GRAPHNEURALNETWORKFORTHEDETECTIONOF mesh affects the system-level fault probability: a significant
CRITICALCOMPONENTSINSERVICEMESHES decreaseindicatesthatthosepartsareweakcomponents,while
A. Graph Neural Networks a significant increase suggests that those parts play a crucial
role in maintaining the service mesh’s performance.
Graph Neural Networks (GNNs) have become the most
Fault probability prediction is a graph-level regression task
commonmachinelearningmethodsforpredictivetaskswithin
in which each service mesh is represented as a graph, and the
the domain of real-world networks. In these networks, each
target variable is the associated system-level fault probability.
individual data point corresponds to a node, characterized not
Each node within the service mesh graph is characterized by
only by a feature vector x but also an adjacency vector
i a single feature. For leaf nodes, this feature is the probability
a that specifies its connections to all other nodes. These
i of failure, while for intermediary nodes, it represents the
feature vectors are organized into a feature matrix denoted
number of request retransmission attempts before giving up
as X ∈ RN×F, while the adjacency vectors take the form of
on an error. To facilitate modeling, we employed two distinct
anadjacencymatrixA∈RN×N,whereF andN respectively
input channels: for leaves, the number of retries was set to
denote the number of features and the number of nodes in the
0 since they lack descendants, while for intermediaries, the
network.
probabilityoffailurewassetto0asthesenodesdonotdirectly
ThetasksaddressedbyGNNscanbecategorizedintonode-
experiencefailures.Thisapproachensuresaconsistentfeature
level, link-level, and graph-level tasks, depending on whether
representation.
the labels pertain to nodes, links, or entire graphs. Given the
The dataset was randomly split into training, validation,
sparsity of real-world networks, it is noteworthy that only a
and test sets, comprising 80%, 10%, and 10% of the service
small number of entries in A contain non-zero values. To
meshes,respectively.Ourobjectiveistolearnafunctionf that
effectivelyhandlesuchsparsematrices,GNNsincorporateso-
minimizes the mean squared error MSE(f(G),y) between the
calledmessagepassinglayers[38],[39].Message-passinglay-
predictedsystem-levelfaultprobabilitiesf(G)andtheground-
ersareresponsibleforgatheringinformationfromneighboring
truth system-level fault probabilities y for the input graphs
nodes. This process can be mathematically expressed as:
G =(X,A).
 
(cid:77) Toachievethis,weuseastandardgraphneuralnetworkar-
x′
i
=ϕx
i
, θ(x
i
,x
j
)
chitecture composed of the following layers: {MPBlock}→
j∈N(i) {MPBlock} → {MPBlock} → {MPBlock} →
In this expression, x is the feature vector associated with {GlobalMeanPool}→{Linear}→{ReLU}→{Linear}
i
node i, and N(i) represents the set of neighboring nodes where each message passing block includes the follow-
connected to node i. The symbol (cid:76) represents a differ- ing operations: {MessagePassing} → {BatchNorm} →
entiable, permutation-invariant function (e.g., sum, mean, or {PReLU}. The complete architecture is illustrated in Fig-
max), while ϕ and θ denote differentiable functions, often ure 5.
realized as Multilayer Perceptrons (MLPs). In our study, we We conducted meticulous hyperparameter tuning for our
(cid:76) (cid:80)
have adopted = , and have configured ϕ and θ as GNNmodel.Thedimensionalityofeachofthe4hiddenlayers
{Linear}→{PReLU}→{Linear}. weresetto32.Theneuralnetworkwastrainedfor200epochs
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 9
Fig.6. IllustrationoftrainingtheexplainerGNNforidentifyingcriticalcomponentsintheservicemesh.TheexplainerGNNgeneratesprobabilitiesfornode
masking,producingamaskthatselectsthemostimportantnodesforfaultprobabilityprediction.ThepredictorGNNthenevaluatestheselectedsubgraphg
anditscomplementaryg¯.Ifthemaskcapturesthemostrelevantnodes,thepredictor’sperformanceonthesubgraphg shouldcloselymatchitsperformance
g¯should
on the original graph, while its performance on the complementary subgraph drop significantly, confirming that the selected nodes are necessary
andsufficientfortheprediction.Themeanoftheprobabilities,µp,andthebudgetB(e.g.,B=33%meansone-thirdofthenodesareretained)controlthe
numberofnodesselected.
|     |     |     |     | way, the        | selected | nodes        | are both  | necessary | and      | sufficient      | for     |
| --- | --- | --- | --- | --------------- | -------- | ------------ | --------- | --------- | -------- | --------------- | ------- |
|     |     |     |     | the prediction. |          | Exhaustively | searching |           | for such | subnetworks     |         |
|     |     |     |     | by evaluating   |          | all possible | node      | subsets   | is       | computationally |         |
|     |     |     |     | infeasible,     | which    | motivates    | the       | need      | for a    | learned         | masking |
mechanism.
|     |     |     |     | To address |         | this challenge, |                 | we designed |          | an explainability |      |
| --- | --- | --- | --- | ---------- | ------- | --------------- | --------------- | ----------- | -------- | ----------------- | ---- |
|     |     |     |     | algorithm  | that    | assigns         | importance      | scores      |          | to the nodes      | of   |
|     |     |     |     | a network. | Drawing | inspiration     |                 | from        | previous | methods           | like |
|     |     |     |     | L2X [41],  | INVASE  | [42],           | and PGExplainer |             | [43],    | our approach      |      |
usesanexplainerneuralnetworktocomputenodeimportance
probabilitiesviagradientdescent.Basedontheseprobabilities,
|     |     |     |     | we can    | select   | the most     | important | B%                | of the    | nodes      | in the |
| --- | --- | --- | --- | --------- | -------- | ------------ | --------- | ----------------- | --------- | ---------- | ------ |
|     |     |     |     | service   | mesh     | with respect | to        | fault prediction, |           | providing  | a      |
|     |     |     |     | practical | solution | to our       | problem   | that              | minimizes | prediction |        |
error.
| Fig. 7. The explainer | network | consists of six message-passing | blocks, |     |     |     |     |     |     |     |     |
| --------------------- | ------- | ------------------------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
followed by a sigmoid layer that generates a probability distribution over Our algorithm, depicted in Figure 6, consists of two neural
thenodes,reflectingtheirimportanceforfaultprobabilityprediction. networks: an explainer GNN and a predictor GNN. The ex-
plainerGNNgeneratesaBernoullidistributionoverthenodes
oftheservicemesh,asillustratedinFigure7.Theprobabilities
| using mini-batches | of 32 service | meshes. Network | parameters |          |         |      |         |                  |     |            |     |
| ------------------ | ------------- | --------------- | ---------- | -------- | ------- | ---- | ------- | ---------------- | --- | ---------- | --- |
|                    |               |                 |            | assigned | to each | node | reflect | its significance |     | in shaping | the |
wereoptimizedusingtheAdamoptimizer[40]withalearning
faultpredictionprocess.Fromthisdistribution,wecansample
rateof2e-4.Themeansquarederror(MSE)servedastheloss
anodemaskthatselectsthemostimportantnodes.Thismask
function.Aftertraining,werestoredtheparametersofthebest
isthenappliedtoboththeadjacencymatrixAandthefeature
| performing model | on the validation | set. |     |        |           |              |     |                 |     |           |     |
| ---------------- | ----------------- | ---- | --- | ------ | --------- | ------------ | --- | --------------- | --- | --------- | --- |
|                  |                   |      |     | matrix | X through | element-wise |     | multiplication, |     | producing | a   |
maskedversionoftheinputgraph.ThepredictorGNN,trained
C. GNN Training for Identifying Critical Components for fault prediction as described in the previous subsection,
After developing a highly accurate GNN model for fault evaluates three versions of the graph: the original unmasked
prediction, we turned our attention to understanding how graph G, the subgraph selected by the explainer after masking
specific parts of the service mesh influence the predicted g, and its complementary subgraph g¯ (the nodes not selected
system-level fault probability. In each network, our goal is by the explainer). If the node mask captures the most relevant
to separate the network into two complementary parts: one nodes within the service mesh, the predictor’s performance
containingatmostB%ofthenodesandpreservingprediction on the selected subgraph g should closely approximate its
accuracy(therelevantsubgraph),andonewheretheprediction performance on the original graph G, while its performance
accuracy degrades significantly (the irrelevant subgraph). This on the complementary subgraph g¯ should drop significantly.
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 10
Thisdemonstratesthattheselectednodesarereallythecritical V. EXPERIMENT1:FAULTPREDICTIONFORFEATURE
components driving the fault prediction: they are necessary ENRICHEDSERVICEMESHES
| because removing |         | them significantly |          | impacts |     | the prediction, |     |           |             |     |             |            |                 |           |         |
| ---------------- | ------- | ------------------ | -------- | ------- | --- | --------------- | --- | --------- | ----------- | --- | ----------- | ---------- | --------------- | --------- | ------- |
|                  |         |                    |          |         |     |                 |     | In this   | experiment, |     | we evaluate |            | the performance |           | of our  |
| and sufficient   | because | the                | subgraph | alone   | can | replicate       | the |           |             |     |             |            |                 |           |         |
|                  |         |                    |          |         |     |                 |     | GNN-based | approach    |     | for fault   | prediction | on              | two types | of ser- |
original prediction.
|     |     |     |     |     |     |     |     | vice meshes: | tree-shaped |     | service | meshes | and | general | directed |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ------- | ------ | --- | ------- | -------- |
TheexplainerandpredictorGNNsaretrainedinalternating
acyclicgraphs(DAGs).Faultpredictionservesasafoundation
steps. In each iteration: for identifying critical components within the service mesh,
• Predictor update: The explainer generates a probability asaccuratelypredictingsystemfaultprobabilitiesallowsusto
distribution p over the nodes of the graph. A node mask analyze the impact of removing specific nodes. Tree-shaped
m is then sampled by applying Bernoulli sampling to meshes represent a simpler hierarchical topology, making it
this probability distribution. This mask defines a selected easier to trace service dependencies, whereas general DAGs
subgraph g and its complementary subgraph g¯. The capture more complex, non-hierarchical relationships between
predictorf istrainedtominimizethemeansquarederror services,whereidentifyingcriticalcomponentsmightbemore
(MSE) between its predictions and the true system-level challenging. All experiments were repeated three times, and
fault probability on both subgraphs: allresultsreportedarethemeanandstandarddeviationacross
|     |     |     |     |     |     |     |     | these three | runs. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
L =MSE(f(g),y)+MSE(f(g¯),y)
f
| Explainerupdate:Thepredictor,withitsupdatedparam- |     |     |     |     |     |     |     | A. Training | Dataset |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
•
eters, is evaluated on the subgraphs g and g¯ to compute The generation of training datasets for the REST-based
the reward. The explainer s is then optimized using the approach involves constructing synthetic models that simulate
REINFORCE algorithm [44] with the loss: complex cloud architectures characterized by a service mesh
|     |     |     |     |     |     |     |     | pattern. | The RESTful |     | services | are designed | as  | nodes | within a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | -------- | ------------ | --- | ----- | -------- |
L =R·BCE(p,m) directed acyclic graph (DAG) structure, where the root node
s
|       |            |          |     |          |     |                |     | initiates      | requests | that         | propagate | through | intermediary |     | nodes       |
| ----- | ---------- | -------- | --- | -------- | --- | -------------- | --- | -------------- | -------- | ------------ | --------- | ------- | ------------ | --- | ----------- |
| where | the reward | function | R   | is based | on  | the difference |     |                |          |              |           |         |              |     |             |
|       |            |          |     |          |     |                |     | to leaf nodes. |          | Intermediary | nodes     | handle  | requests     |     | probabilis- |
between the predictor’s performance on the selected sub- tically, relaying them towards child nodes or providing direct
| graph | and its | complementary |     | subgraph, |     | with an | added |            |      |       |          |              |     |           |      |
| ----- | ------- | ------------- | --- | --------- | --- | ------- | ----- | ---------- | ---- | ----- | -------- | ------------ | --- | --------- | ---- |
|       |         |               |     |           |     |         |       | responses. | Leaf | nodes | finalize | interactions | by  | returning | HTTP |
term that encourages sparsity in the selected nodes [43]: status codes, either signifying successful operations (HTTP
|                                   |          |      |        |             |     |              |     | 2xx) or        | indicating | server       | failures | (HTTP                 | 5xx), | the         | latter of |
| --------------------------------- | -------- | ---- | ------ | ----------- | --- | ------------ | --- | -------------- | ---------- | ------------ | -------- | --------------------- | ----- | ----------- | --------- |
| R=MSE(f(g¯),y)−MSE(f(g),y)+ReLU(µ |          |      |        |             |     |              | −B) |                |            |              |          |                       |       |             |           |
|                                   |          |      |        |             |     | p            |     | which triggers |            | a defined    | retry    | mechanism.            | Each  | component’s |           |
|                                   |          |      |        |             |     |              |     | operations     | and        | interactions |          | are probabilistically |       | modulated,  |           |
| Here,                             | µ is the | mean | of the | probability |     | distribution | p,  |                |            |              |          |                       |       |             |           |
p
|       |               |     |                |     |              |     |        | enabling | varied | simulations | reflective |     | of real-world |     | scenarios. |
| ----- | ------------- | --- | -------------- | --- | ------------ | --- | ------ | -------- | ------ | ----------- | ---------- | --- | ------------- | --- | ---------- |
| and B | is the budget |     | which controls |     | the expected |     | number |          |        |             |            |     |               |     |            |
UtilizingthePythonprogramminglanguage,adomain-specific
| of nodes | selected | by  | the explainer. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
language(DSL)wasdevisedtomodeltheseinteractionswithin
| The dataset | was | split into | training, | validation, |     | and test | sets |             |            |     |      |            |             |     |          |
| ----------- | --- | ---------- | --------- | ----------- | --- | -------- | ---- | ----------- | ---------- | --- | ---- | ---------- | ----------- | --- | -------- |
|             |     |            |           |             |     |          |      | the RESTful | framework. |     | This | automation | facilitates |     | the cre- |
following the same procedure used for fault prediction, and ation and execution of extensive simulations, with predefined
| the same hyperparameters |     |            | were retained. |     |     |     |     |              |              |            |            |                |        |        |           |
| ------------------------ | --- | ---------- | -------------- | --- | --- | --- | --- | ------------ | ------------ | ---------- | ---------- | -------------- | ------ | ------ | --------- |
|                          |     |            |                |     |     |     |     | ranges       | for critical | parameters |            | such           | as the | number | of items  |
|                          |     |            |                |     |     |     |     | and buffer   | sizes,       | enhancing  |            | the robustness |        | of the | dataset.  |
|                          |     |            |                |     |     |     |     | The training | dataset      |            | generation | method         | and    | the    | volume of |
| D. Computational         |     | Complexity |                |     |     |     |     |              |              |            |            |                |        |        |           |
generatedsamplesensurecomprehensivecoverageofpotential
Our approach is computationally efficient, as both the fault statesandtransitions,therebyobviatingthenecessityfornoise
probability estimation and the explainability algorithm rely reduction. The framework’s methodological approach ensures
on Graph Neural Networks (GNNs). The key property of that the resultant dataset is both diverse and representative of
| GNNs is | that they | operate | on  | sparse | adjacency | matrices, |     |     |     |     |     |     |     |     |     |
| ------- | --------- | ------- | --- | ------ | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
potentialreal-worldRESTfulserviceinteractions,significantly
enablingefficientstorageandcomputation.Thecomputational contributing to the accuracy and reliability of subsequent
complexityofmessage-passinglayersinGNNsisO(E),where analyses and models.
E is the number of edges in the graph. Since service meshes The current approach prioritizes computational efficiency
typicallyhavefarfeweredgesthanthetheoreticalO(N²)bound andsimplifiesthesimulationofnetworkdynamicsbyfocusing
for dense graphs, this makes GNN-based fault probability failurespredominantlyattheleafnodes.Thisdecisionensures
estimation scalable even for large-scale systems. that the model remains scalable and manageable, particularly
Since our explainer network is implemented as another whensimulatingextensiveservicemesheswithmultiplelayers
GNN that learns to generate node importance scores, its of intermediate nodes. By using retry counters at interme-
complexity remains the same as the fault probability pre- diary nodes, the model effectively emulates the robustness
dictor GNN. Its overhead comes from sampling node masks strategiestypicalincontemporarycloudinfrastructures,where
and computing the reward function, but these operations are fault tolerance is largely handled through retries and load
lightweight compared to the forward and backward passes of balancing rather than expecting individual intermediaries to
a GNN. managefailure.Thisabstractionalignswithindustrypractices,
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 11
TABLEII
SAMPLEOFOBSERVABLEACTIONSIMULATIONRESULTS
|     | id  | from | to method | action |     | result |     |                                                                       |     |     |     |     |     |     |     |
| --- | --- | ---- | --------- | ------ | --- | ------ | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   | X0   | X22 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     | 1   | X22  | X24 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     | 2   | X24  | X19 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     | 3   | X19  | X13 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     | 4   | X13  | X12 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     | 5   | X12  | X17 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     | 6   | X12  | X17 GET   | resp   |     | 2xx    |     |                                                                       |     |     |     |     |     |     |     |
|     | 7   | X13  | X12 GET   | resp   |     | 2xx    |     |                                                                       |     |     |     |     |     |     |     |
|     | 8   | X19  | X13 GET   | resp   |     | 2xx    |     |                                                                       |     |     |     |     |     |     |     |
|     | 9   | X24  | X19 GET   | resp   |     | 2xx    |     |                                                                       |     |     |     |     |     |     |     |
|     | 10  | X22  | X24 GET   | resp   |     | 2xx    |     |                                                                       |     |     |     |     |     |     |     |
|     | 11  | X0   | X22 GET   | resp   |     | 2xx    |     |                                                                       |     |     |     |     |     |     |     |
|     | 12  | X0   | X22 GET   | req    |     |        |     |                                                                       |     |     |     |     |     |     |     |
|     |     |      |           |        |     |        |     | Fig.8. Learningcurveforfaultprobabilitypredictionontree-shapedservice |     |     |     |     |     |     |     |
13 X22 X24 GET req meshes:validationR²score(leftaxis)andvalidationMAEscore(rightaxis)
14 X24 X5 GET req overepochs(mean±standarddeviationacross3runs).
|       | 15         | X24 | X5 GET           | resp       |     | 2xx          |     |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---------------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|       | 16         | X22 | X24 GET          | resp       |     | 2xx          |     |     |     |     |     |     |     |     |     |
|       | 17         | X0  | X22 GET          | resp       |     | 2xx          |     |     |     |     |     |     |     |     |     |
|       | 18         | X0  | X15 GET          | req        |     |              |     |     |     |     |     |     |     |     |     |
|       | 19         | X15 | X14 GET          | req        |     |              |     |     |     |     |     |     |     |     |     |
|       | 20         | X14 | X11 GET          | req        |     |              |     |     |     |     |     |     |     |     |     |
|       | 21         | X14 | X11 GET          | resp       |     | 2xx          |     |     |     |     |     |     |     |     |     |
|       | 22         | X15 | X14 GET          | resp       |     | 2xx          |     |     |     |     |     |     |     |     |     |
|       | 23         | X0  | X15 GET          | resp       |     | 2xx          |     |     |     |     |     |     |     |     |     |
|       | 24         | X0  | X23 GET          | req        |     |              |     |     |     |     |     |     |     |     |     |
|       | 25         | X0  | X23 GET          | resp       |     | 5xx          |     |     |     |     |     |     |     |     |     |
| where | resilience | is  | achieved through | redundancy |     | and failover |     |     |     |     |     |     |     |     |     |
mechanisms,minimizingtheneedtosimulateinternalfailures
| at all   | node levels | within | the architecture. |       |     |              |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | ------ | ----------------- | ----- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Training | datasets    |        | were generated    | based | on  | the approach |     |     |     |     |     |     |     |     |     |
described above. Several cases, each containing simulation Fig.9. TestR²score(leftaxis)andtestMAEscore(rightaxis)versustraining
datasets, were generated for different architecture topologies set fraction for fault probability prediction on tree-shaped service meshes.
Errorbarsrepresentmean±standarddeviationacross3runs.Numericallabels
(basedonrandomDAGs).Thesethenwereexpandedwithsets indicatethemeanvalueateachpoint.
| ofsub-cases,eachwithrandomparametervaluesforP |     |     |     |     |     |     | [m] |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fail
andretries[n]followingauniformdistribution.Foreachcase,
agraphdescriptioninGraphExchangeXMLFormat[45]was
augmented with these new node attributes. a depth-first walk pattern with optional back-tracking. This
|     |          |       |                  |       |             |     |      | means that | for any    | given | pair of | communicating |     | nodes, | the |
| --- | -------- | ----- | ---------------- | ----- | ----------- | --- | ---- | ---------- | ---------- | ----- | ------- | ------------- | --- | ------ | --- |
| As  | internal | state | graph transition | state | simulations |     | were |            |            |       |         |               |     |        |     |
|     |          |       |                  |       |             |     |      | following  | statements | hold  | true:   |               |     |        |     |
consideredlessimportantinthisphaseofresearch,theirlength
| was reduced |     | to 10.000 | steps. | To aid experiments |     | focusing | on  |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ------ | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• foreachreqactiontheremustbeatleastonerespaction,
| the external |     | observable | properties | of the | cloud | applications, | a   |      |              |     |         |         |     |        |     |
| ------------ | --- | ---------- | ---------- | ------ | ----- | ------------- | --- | ---- | ------------ | --- | ------- | ------- | --- | ------ | --- |
|              |     |            |            |        |       |               |     | more | resp actions | are | allowed | in case | of  | errors |     |
newfilteredstatesimulationformatwasdevised,asillustrated
|           |         |              |              |           |     |                |     | • foreachreq | actionatleastonerespactionismandatory, |            |     |       |              |     |         |
| --------- | ------- | ------------ | ------------ | --------- | --- | -------------- | --- | ------------ | -------------------------------------- | ---------- | --- | ----- | ------------ | --- | ------- |
| by Table  | II.     | This message | simulation   | dataset   |     | consists of    | the |              |                                        |            |     |       |              |     |         |
|           |         |              |              |           |     |                |     | so requests  | are                                    | not queued |     |       |              |     |         |
| following | fields: |              |              |           |     |                |     |              |                                        |            |     |       |              |     |         |
| • id:     | event   | identifier,  | the discrete | timestamp |     | of the logical |     |              |                                        |            |     |       |              |     |         |
|           |         |              |              |           |     |                |     | At this      | phase of                               | research,  | the | total | experimental |     | dataset |
clock
|     |     |     |     |     |     |     |     | volume | has exceeded | 2.1 | GB, | including | cloud | architecture |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | --------- | ----- | ------------ | --- |
• from: message source node identifier in format X n modelsin50casesfortree-shapedservicemeshesand10cases
| where | is  | n is the | node identifier |     |     |     |     |               |         |         |      |      |          |             |     |
| ----- | --- | -------- | --------------- | --- | --- | --- | --- | ------------- | ------- | ------- | ---- | ---- | -------- | ----------- | --- |
|       |     |          |                 |     |     |     |     | for DAG-based | service | meshes, | each | with | distinct | topologies. |     |
| to:   |     |          |                 |     |     | X   |     |               |         |         |      |      |          |             |     |
• message destination node identifier in format n Each tree-shaped case contains 50 subcases, and each DAG-
• method: simulated HTTP method, only GET is imple- based case contains 10 subcases. The graphs in the dataset
| mented |     | at the | time of writing |     |     |     |     |            |            |       |     |         |       |       |     |
| ------ | --- | ------ | --------------- | --- | --- | --- | --- | ---------- | ---------- | ----- | --- | ------- | ----- | ----- | --- |
|        |     |        |                 |     |     |     |     | consist of | 25 RESTful | nodes | per | service | mesh. | While | the |
• action: simulated HTTP action, with values req for underlyinggraphstructureremainsthesamewithineachcase,
| requests |     | and resp  | for responses |             |     |               |     |                                                        |              |        |     |            |     |              |     |
| -------- | --- | --------- | ------------- | ----------- | --- | ------------- | --- | ------------------------------------------------------ | ------------ | ------ | --- | ---------- | --- | ------------ | --- |
|          |     |           |               |             |     |               |     | the node                                               | features—the | number |     | of retries | for | intermediary |     |
| result:  |     | simulated | HTTP          | result code | for | resp actions, |     |                                                        |              |        |     |            |     |              |     |
| •        |     |           |               |             |     |               |     | nodesandtheprobabilityoffailureforleafnodes—varyacross |              |        |     |            |     |              |     |
with values 2xx for normal responses, and 5xx for error subcases, offering a diverse set of configurations for analysis.
responses
|     |     |     |     |     |     |     |     | The calculated | system-level |     | fault | probabilities |     | in the | dataset |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | ----- | ------------- | --- | ------ | ------- |
Based on the core model properties and node strategies range from a minimum of 0.0 to a maximum of 1.0, with a
| described | in  | the previous | section, | the message |     | patterns follow |     | median of | 1.2e-5. |     |     |     |     |     |     |
| --------- | --- | ------------ | -------- | ----------- | --- | --------------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 12
Fig.10. Learningcurveforfaultprobabilitypredictionontree-shapedservice Fig. 11. Test R² score (left axis) and test MAE (right axis) versus training
meshes:validationR²score(leftaxis)andvalidationMAEscore(rightaxis) set fraction for fault probability prediction on DAG-shaped service meshes.
overepochs(mean±standarddeviationacross3runs). Errorbarsrepresentmean±standarddeviationacross3runs.Numericallabels
indicatethemeanvalueateachpoint.
B. Fault Prediction Results on Tree-shaped Service Meshes
predicted and actual system fault probabilities, with a test R²
Inthissubsection,wepresenttheresultsofourexperiments
score of 0.996±0.003 (Figure 15, subfigure (a))).
ontree-shapedservicemeshes.Theseexperimentsdemonstrate
We further evaluated the model trained on DAG-shaped
the model’s ability to capture both the relationships between
service meshes by testing it on the tree-shaped service mesh
nodes and their connections, as well as how variations in
dataset to assess its ability to transfer across different topolo-
node features and the overall mesh structure influence system
gies. The pretrained model achieved a test MAE score of
reliability.
0.038±0.006 and a test R² score of 0.938±0.014 on the
AsshowninFigure8,thelearningcurveindicateseffective
tree-shaped service mesh test set. These results, while slightly
training, with a consistent decrease in the MAE score and a
lower than those of the model trained directly on tree-shaped
correspondingincreaseinthevalidationR²scoreoverepochs.
meshes,clearlydemonstratethemodel’scapacitytogeneralize
The best model on the validation set achieved a MAE of
effectively across different service mesh structures.
0.009±0.001onthetestset,demonstratingstronggeneraliza-
As in our experiments on tree-shaped service meshes,
tion across diverse tree-shaped service mesh topologies. The
we explored the impact of varying the training set size on
regression plot further highlights the close alignment between
the model’s performance. Figure 11 illustrates a clear trend:
predicted and actual system fault probabilities, with a test R²
increasing the training set size leads to a decreasing MAE
score of 0.992±0.005 (Figure 12, subfigure a)).
score and an increasing R² score on the test set, with both
Additionally,weexaminedtheeffectofvaryingthetraining
metrics stabilizing at higher values. This consistency affirms
setsizeonmodelperformance.AsshowninFigure9,theplot
our earlier conclusion that larger, more diverse datasets allow
presents the test R² score and test MAE score as functions of
themodeltobettercapturetherelationshipswithintheservice
the training set fraction. The figure shows that the test MAE
mesh topology.
decreases consistently as the training set size increases, while
the test R² score correspondingly improves and stabilizes at
higher values. These results highlight the importance of using D. Baseline Comparison
a large and diverse dataset to enable the model to effectively
To contextualize the performance of our GNN model and
capture the underlying dependencies within the service mesh.
to isolate the contributions of nonlinear transformations and
This is crucial for further analyses on identifying critical
messagepassing,weimplementedasystematicsetofbaseline
components within the network.
models:
• LinReg: We bucketized the node feature values into five
C. Fault Prediction Results on DAG-shaped Service Meshes
buckets per feature by sorting the values and dividing
In this subsection, we extend our experiments to DAG- them into equal-sized groups. The mean within each
shaped service meshes to evaluate the model’s ability to bucketwascomputed,resultinginapermutation-invariant
generalize across more complex network topologies. representation that is independent of node ordering and
As shown in Figure 10, the learning curve for DAG-shaped robust to variations in graph size. A linear regression
service meshes shows a pattern similar to that observed for model was then fit to these aggregated features.
tree-shaped meshes, with a consistent decrease in the MAE • LinReg with spectral embeddings: Since linear regres-
score and a corresponding increase in the validation R² score sion cannot capture the graph structure, we computed
over epochs. The best model on the validation set achieved a the spectral embedding of each graph, applied the same
test MAE of 0.009±0.002, indicating strong generalization bucketization to the spectral coordinates, and concate-
across diverse DAG-shaped service mesh topologies. The nated these with the bucketized node features. A linear
regression plot further confirms the close alignment between regression model was fit to the combined features.
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 13
TABLEIII B. Explainability Results on Tree-shaped Service Meshes
TESTSETMAEFORBASELINEMODELSANDTHEGNNONTREE-AND
DAG-SHAPEDSERVICEMESHES. Inthissection,wepresenttheexplainabilityresultsfortree-
shaped service meshes. Using the predictor GNN, we applied
Model TreeMAE DAGMAE
LinReg 0.218±0.004 0.130±0.017 our explainability algorithm to identify which nodes are most
LinRegwithspectralemb. 0.135±0.004 0.083±0.018 influentialinpredictingsystemfaultsituations,discoveringthe
MLP 0.177±0.001 0.127±0.020 critical components of the networks.
MLPwithspectralemb. 0.031±0.001 0.025±0.003
Figure 12 shows the regression results for the predictor
GNN 0.009±0.001 0.009±0.002
GNN on tree-shaped service meshes. The first plot (a) il-
lustrates the predictions made using all nodes in the service
• MLP:ThismodelusesthesamearchitectureastheGNN, mesh, which align very closely with the actual system fault
but with all message passing layers replaced by linear probabilities, achieving an R² score of 0.992±0.005 on the
layers.Permutationinvarianceispreservedthroughglobal test set. This result indicates the model’s strong predictive
mean pooling, while the model loses the GNN’s ability performance when using the full set of nodes in the network.
to capture node interactions through message passing. Plot (b) demonstrates the predictions made using only the
• MLP with spectral embeddings: The same architecture top 30% of nodes selected by the explainer network. Despite
as above, but with spectral coordinates concatenated to reducing the input to a smaller subset, the model maintains
the node features. This provides information about the strong performance, achieving an R² score of 0.974±0.018.
graph structure in the absence of message passing. This is significant, as it confirms that these selected nodes
explain most of the variance in the predicted fault outcomes,
Table III presents the test set MAE for each model on
effectivelyidentifyingthemasthemostimportantcomponents
tree- and DAG-shaped service meshes. The linear regression
forprediction.Incontrast,plot(c)showsthepredictionsmade
models achieve limited accuracy, even when spectral embed-
on the complementary 70% of nodes, where the R² score
dings are included, showing their inability to capture complex
dropsto0.104±0.042.Thissuggeststhatthesenodesprovide
interactions between nodes. The MLP baselines provide im-
minimal information about the fault outcomes, essentially
provements, particularly when spectral embeddings are used,
leading to a baseline mean prediction. The dramatic drop in
but still fall short of the GNN’s performance. These results
performance further reinforces the importance of the selected
highlight the critical role of message passing in effectively
30%ofnodesinaccuratelypredictingthenetwork’sreliability.
modeling node interactions. At the same time, they illustrate
These results show how well our explainability method
the tradeoff between model complexity and interpretability,
works, with the selected nodes being key to predicting fault
motivating the explainability method introduced in the next
outcomes accurately. The sharp drop between the predictive
section.
power of the selected and unselected nodes affirms the power
of our method in identifying key components that drive
VI. EXPERIMENT2:DETECTIONOFCRITICAL network reliability.
COMPONENTSWITHGNNEXPLAINABILITY We further investigated how adjusting the selection budget,
i.e., the proportion of selected nodes, influences the model’s
In this experiment, we focus on our core objective: iden-
predictive performance. By varying the budget from 10% to
tifying the critical components within service meshes using
50%, clear patterns emerge in both the R² and MAE scores
GNN explainability techniques. By applying an explainability
for the selected and complementary node sets. As shown in
method to a well-trained GNN model, we determine which
Figure 13, the R² score for the selected nodes remains consis-
nodes (or subnetworks) have the most significant influence
tentlyhigh,between0.991and0.996,demonstratingthateven
on the system’s overall reliability. This allows us to detect
small subsets of nodes retain most of the critical information
both weak points and essential nodes whose failure or un-
requiredforaccuratefaultprediction.Incontrast,theR²score
derperformance could severely impact service quality. This
for the complementary nodes steadily decreases from 0.306
deeper insight is crucial for improving service robustness,
at 10% budget to 0.048 at 50%, as increasingly informative
as it enables targeted troubleshooting in the network’s most
nodes are moved to the selected set. A similar trend is seen
influential areas. Additionally, this understanding lays the
in the MAE scores: the error for the selected nodes remains
groundworkforfuturework,wheretheclouddebuggersystem
low,between0.014and0.018,whilethecomplementarynodes
can be steered toward potential failure points, enabling more
exhibit rising errors, from 0.176 to 0.255. These findings
effective remediation and resilience testing.
clearlyhighlightthestrengthofourexplainabilitymethod:the
selected nodes consistently concentrate the predictive power,
whilethecomplementarynodescontributelittletothemodel’s
A. Training Dataset
fault prediction accuracy.
For this experiment, we used the same datasets as in the Todemonstratebetterhowourexplainernetworkworks,we
faultpredictionexperiments,whichconsistofbothtree-shaped showasimpleexampleinFigure14(a).Inthisexample,nodes
and DAG-shaped service meshes. These datasets allow us are colored based on their selection probabilities, which show
to evaluate the model’s ability to detect critical components how important each node is for predicting the fault outcome.
across varying topologies and service configurations. There is a leaf node next to the root with the relatively high
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 14
Fig.12. Regressionplotsforfaultprobabilitypredictionontree-shapedservicemeshesusingthepredictorGNN:a)Predictionson100%ofthenodes,closely
aligned with the ground truth values, achieving an R² score of 0.992, indicating excellent predictive performance; b) Predictions using the selected 30% of
nodes (chosen by the explainer network), maintaining strong performance with an R² score of 0.974, confirming that these nodes are critical for predicting
system-levelfaultprobabilitiesandcapturingmostofthevarianceinthesystem;c)Predictionsusingthecomplementary70%ofunselectednodes,withan
R²scoreof0.104,demonstratingthatthesenodesprovidelittleinformationaboutthesystem-levelfaultprobabilities,essentiallyresultinginabaselinemean
prediction. This clearly demonstrates the algorithm’s success in identifying critical components, as the selected nodes retain most of the variance while the
unselectedonesprovideminimalpredictivevalue.
|     |     |     |     |     | intermediary | nodes can mitigate        | if something           | goes wrong.      |        |
| --- | --- | --- | --- | --- | ------------ | ------------------------- | ---------------------- | ---------------- | ------ |
|     |     |     |     |     | In Figure    | 14 (b), we                | changed the            | example slightly | by     |
|     |     |     |     |     | setting the  | failure probability       | of this critical       | leaf node        | next   |
|     |     |     |     |     | to the root  | to 0.0. This              | leads to a significant | change           | in the |
|     |     |     |     |     | predicted    | system fault probability. | Using                  | the selected     | nodes, |
thepredictedsystemfaultprobabilitydropsto0.0becausethe
|     |     |     |     |     | critical node | no longer        | has a risk of failure. | The predicted |      |
| --- | --- | --- | --- | --- | ------------- | ---------------- | ---------------------- | ------------- | ---- |
|     |     |     |     |     | system fault  | probability      | for the unselected     | nodes stays   | the  |
|     |     |     |     |     | same. This    | result is what   | we would expect        | and confirms  | that |
|     |     |     |     |     | the explainer | works correctly. |                        |               |      |
InFigure14(c),wemadeanotherslightchangebymoving
|     |     |     |     |     | the critical | leaf node to          | a lower level in  | the service    | mesh, |
| --- | --- | --- | --- | --- | ------------ | --------------------- | ----------------- | -------------- | ----- |
|     |     |     |     |     | attaching    | it to an intermediary | node that         | can retry once | after |
|     |     |     |     |     | a failure.   | This change affects   | how the explainer | behaves:       | now   |
Fig.13. R²andMAEScoresvs.Budget(ProportionofSelectedNodes):As
the selection budget increases from 10% to 50%, the R² score for selected only this critical node gets selected. As we expected, the
| nodes remains | consistently | high (between 0.991 | and 0.996), | demonstrating |           |                          |       |             |        |
| ------------- | ------------ | ------------------- | ----------- | ------------- | --------- | ------------------------ | ----- | ----------- | ------ |
|               |              |                     |             |               | predicted | system fault probability | drops | to 0.01 due | to the |
thatevensmallsubsetscapturemostofthepredictiveinformation.Incontrast,
|     |     |     |     |     | recovery | capability of the | intermediary node, | which can | retry |
| --- | --- | --- | --- | --- | -------- | ----------------- | ------------------ | --------- | ----- |
theR²scoreforcomplementarynodessteadilydecreasesfrom0.306to0.048
|     |     |     |     |     | the request | if a failure occurs. |     |     |     |
| --- | --- | --- | --- | --- | ----------- | -------------------- | --- | --- | --- |
asmoreinformativenodesaremovedtotheselectedset.Similarly,theMAE
scoreforselectednodesremainslow,whiletheMAEscoreforcomplementary
| nodes increases, | reinforcing | the importance | of the selected nodes | in system |     |     |     |     |     |
| ---------------- | ----------- | -------------- | --------------------- | --------- | --- | --- | --- | --- | --- |
faultprobabilityprediction. C. Explainability Results on DAG-shaped Service Meshes
|     |     |     |     |     | In this | subsection, we | extend our explainability | analysis | to  |
| --- | --- | --- | --- | --- | ------- | -------------- | ------------------------- | -------- | --- |
DAG-shapedservicemeshes.Aswiththetree-shapedmeshes,
failure probability of 0.27 (marked in red). Since this node is we used the predictor GNN and applied the explainability
close to the root and has a high risk of failure, it plays a key algorithm to determine which nodes were most critical for
role in determining the overall system fault probability. As a predicting the system fault outcomes.
result, the ground truth system failure probability is a high Figure 15 presents the regression results for the DAG-
value of 0.93. Our explainer network correctly identifies this shaped service meshes. In plot (a), we see the predictions
node as important, assigning it a high selection probability. made using all nodes in the network. The predictor closely
Using only the selected nodes, the model predicts that system aligns with the true system fault probabilities, achieving an
fault probability is 0.94, which is very close to the actual R² score of 0.996±0.003, showing that the model performs
value.Incontrast,whenthepredictorusesonlytheunselected exceptionally well when considering the entire set of nodes.
nodes,thepredictedsystemfaultprobabilityis0.02.Thislarge Plot(b)showsthepredictionsmadeusingonlythetop30%of
difference shows that the unselected nodes cannot be used to nodes identified by the explainer network. The model main-
determine the fault. Most of the unselected nodes are stable, tainsastrongperformance,withanR²scoreof0.861±0.054,
and the leaves that could fail are far from the root, where suggestingthattheseselectednodescapturemostofthecritical
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 15
Fig.14. Demonstrationofexplainernetworkonaservicemesh.(a)Acriticalleafnodewithhigh0.27failureprobabilityneartherootleadstoapredicted
systemfaultprobabilityof0.94,closelymatchingthegroundtruthof0.93.(b)Settingthefailureprobabilityofthecriticalnodeto0.00reducesthepredicted
systemfaultprobabilityto0.00.(c)Movingthecriticalnodelowerinthetree,thepredictedsystemfaultprobabilitydropsto0.01duetotheintermediary
node’srecoveryability.
information for fault prediction. In contrast, plot (c) shows typically occurs when the explainer masks a few critical
the predictions made using the complementary 70% of nodes. nodes that have a disproportionately large influence on the
The R² score here drops to 0.072±0.086. This sharp decline overall prediction. When these nodes are excluded from the
highlights that these unselected nodes provide little to no selected subgraph, the model underestimates the system-level
useful information for predicting the fault outcomes. These fault probability. These occasional failures suggest that the
resultsforDAG-shapedmeshesalignwellwiththosefromthe explainer may sometimes overlook sparse but highly informa-
tree-shaped meshes, which reinforces the effectiveness of our tivecomponents,andcouldbenefitfromfurtherfine-tuningor
explainability method in identifying the critical components regularization to increase robustness.
across different network structures.
However,inasmallnumberofcases,weobserveadiscrep- VII. DISCUSSIONANDCONCLUSION
ancy where the predicted system fault probability is close to Designing dependable and scalable cloud services requires
zero while the true probability is significantly higher. This systematic tools to analyze complex behaviors and identify
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 16
Fig. 15. Regression plots for fault probability prediction on DAG-shaped service meshes using the predictor GNN: (a) Predictions on 100% of the nodes,
achievinganR²scoreof0.996,indicatingexcellentpredictiveperformance;(b)Predictionsusingtheselected30%ofnodes(chosenbytheexplainernetwork),
achieving an R² score of 0.861, showing that these nodes capture most of the critical information for fault probability prediction; (c) Predictions using the
complementary70%ofnodes,achievinganR²scoreof0.072,demonstratingthatthesenodesprovidelittletonovalueforpredictingfaultprobabilities.
faultsefficiently.Whilemanyexistingapproachesinthelitera- partly supported by the European Union project RRF-2.3.1-
turetargetspecificaspectsoffaultdetection—suchasnetwork- 21-2022-00004 within the framework of the Artificial Intel-
ing faults, security breaches, or system-level anomalies—they ligence National Laboratory. This work was partially funded
oftenoperateatafixedabstractionlevelandlackgeneralizabil- bytheNationalResearch,DevelopmentandInnovationOffice
ityacrosscloudenvironments.Thisworkcontributesaunified (NKFIH) under OTKA Grant Agreement No. K 132838. The
and explainable approach to fault forecasting in microservice- presented work of R. Lovas was also supported by the Ja´nos
based cloud systems, using probabilistic modeling and graph- Bolyai Research Scholarship of the Hungarian Academy of
based machine learning. Sciences.Onbehalfofthe‘MILAB-SmartLab’cloudproject,
wearegratefulforthepossibilitytouseHUN-RENCloud[46]
| Our proposed | method | combines |     | a formally |     | verified | sim- |     |     |     |     |     |     |     |
| ------------ | ------ | -------- | --- | ---------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ulation environment with data-driven fault prediction and which helped us achieve the results published in this paper.
explainability. The use of the PRISM model checker enables ⋄ WordTune, Grammarly, OpenAI ChatGPT GPT-4: gram-
us to simulate fault propagation across a variety of service mar enhancement. In case of ChatGPT, the prompt was ‘You
mesh topologies, generating training data without requiring are a researcher, produce high-quality scientific text. Rewrite
deployment on live infrastructure. Starting from simple tree- the following text to improve its grammar and scientific
structured graphs and extending to general DAGs, we demon- language: INPUT TEXT’ alike.
strated how the framework scales across increasing architec- ⋆ OpenAI ChatGPT GPT-4, Scite Assistant: used to create
|     |     |     |     |     |     |     |     | a draft, which | was completed, |     | rewritten | and enhanced |     | by the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --- | --------- | ------------ | --- | ------ |
tural complexity.
Graph Neural Networks allow us to capture both structural authors.Thepromptwas‘Youarearesearcher,producehigh-
|                   |     |              |     |              |     |               |     | quality scientific | text. | Write a summary |     | draft on | the following |     |
| ----------------- | --- | ------------ | --- | ------------ | --- | ------------- | --- | ------------------ | ----- | --------------- | --- | -------- | ------------- | --- |
| and feature-based |     | dependencies | in  | microservice |     | interactions, |     |                    |       |                 |     |          |               |     |
achieving accurate system-level fault probability predictions. topics: INPUT TEXT’ alike.
| Furthermore, | by integrating |     | an explainability |     | mechanism, |     | the |     |     |     |     |     |     |     |
| ------------ | -------------- | --- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| framework | can highlight |     | the most | failure-prone |     | microser- |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | -------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
vices—guiding debugging efforts toward critical components [1] David Jaramillo, Duy V Nguyen, and Robert Smart. Leveraging
and improving system-level fault understanding. microservicesarchitecturebyusingdockertechnology.InSoutheastCon
2016,pages1–5,2016.
Although the current evaluation is based on synthetic [2] Pekka Pa¨a¨kko¨nen and Daniel Pakkala. Reference architecture and
datasets to ensure full control and formal validation, real- classificationoftechnologies,productsandservicesforbigdatasystems.
BigDataRes.,2(4):166–186,dec2015.
| world applicability |            | remains | a priority. | Future   | work | will       | focus |                                                                      |     |     |     |     |     |        |
| ------------------- | ---------- | ------- | ----------- | -------- | ---- | ---------- | ----- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | ------ |
|                     |            |         |             |          |      |            |       | [3] AttilaCsabaMarosi,Ma´rkEmo˝di,AttilaFarkas,Ro´bertLovas,Richa´rd |     |     |     |     |     |        |
| on integrating      | real-world | cloud   | traces,     | adapting |      | to dynamic |       |                                                                      |     |     |     |     |     |        |
|                     |            |         |             |          |      |            |       | Beregi,GianfrancoPedone,Bala´zsNe´meth,andPe´terGa´spa´r.            |     |     |     |     |     | Toward |
operationalenvironments,andextendingthemethodtobroader reference architectures: A cloud-agnostic data analytics platform em-
|               |           |     |            |           |     |         |     | poweringautonomoussystems.                      |                     | IEEEAccess,10:60658–60673,2022. |           |                      |               |     |
| ------------- | --------- | --- | ---------- | --------- | --- | ------- | --- | ----------------------------------------------- | ------------------- | ------------------------------- | --------- | -------------------- | ------------- | --- |
| observability | contexts. |     |            |           |     |         |     |                                                 |                     |                                 |           |                      |               |     |
|               |           |     |            |           |     |         |     | [4] Microsoft                                   | azure documentation | -                               | reference | architectures.       | https://docs. |     |
| The dataset,  | code,     | and | additional | materials |     | related | to  |                                                 |                     |                                 |           |                      |               |     |
|               |           |     |            |           |     |         |     | microsoft.com/en-us/azure/architecture/browse/. |                     |                                 |           | Accessed:2022-02-20. |               |     |
this work are publicly available at: https://github.com/ [5] TheTOGAFStandard,Version9.2Overview. https://www.opengroup.
|     |     |     |     |     |     |     |     | org/togaf. | Accessed:2022-02-12. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------- | --- | --- | --- | --- | --- |
BME-SmartLab/GNN-Fault-Forecasting
|     |     |     |     |     |     |     |     | [6] Whatisareferencearchitecture?–enterpriseitdefinitions.https://www. |     |     |     |           |     |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --------- | --- | -------- |
|     |     |     |     |     |     |     |     | hpe.com/us/en/what-is/reference-architecture.html.                     |     |     |     | Accessed: |     | 2022-02- |
20.
ACKNOWLEDGMENT
|          |          |         |        |         |     |      |         | [7] Wubin | Li, Yves Lemieux, | Jing Gao,     | Zhuofeng    | Zhao,      | and Yanbo        | Han.   |
| -------- | -------- | ------- | ------ | ------- | --- | ---- | ------- | --------- | ----------------- | ------------- | ----------- | ---------- | ---------------- | ------ |
|          |          |         |        |         |     |      |         | Service   | mesh: Challenges, | state         | of the art, | and future | research         | oppor- |
| The work | reported | in this | paper, | carried | out | as a | collab- |           |                   |               |             |            |                  |        |
|          |          |         |        |         |     |      |         | tunities. | In 2019 IEEE      | International | Conference  | on         | Service-Oriented |        |
oration between HUN-REN SZTAKI and BME, has been SystemEngineering(SOSE),pages122–1225,2019.
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 17
[8] Jose Cunha, Joao Lourenco, and Vitor Duarte. Debugging of parallel [27] RaphaelRouf,MohammadrezaRasolroveicy,MarinLitoiu,SeemaNa-
and distributed programs, pages 101–136. Nova Science Publishers, gar, Prateeti Mohapatra, Pranjal Gupta, and Ian Watts. Instantops: A
2001. jointapproachtosystemfailurepredictionandrootcauseidentification
[9] XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,WenhaiLi,andDan in microservices cloud-native applications. In Proceedings of the
Ding. Faultanalysisanddebuggingofmicroservicesystems:Industrial 15thACM/SPECInternationalConferenceonPerformanceEngineering,
survey,benchmarksystem,andempiricalstudy. IEEETransactionson ICPE ’24, page 119–129, New York, NY, USA, 2024. Association for
SoftwareEngineering,47(2):243–260,2021. ComputingMachinery.
[10] EmanAljoumah,FajerAl-Mousawi,ImtiazAhmad,MahaAl-Shammri, [28] Angelos-Christos Maroudis, Theodoros Theodoropoulos, John Violos,
and Zahraa Al-Jady. Sla in cloud computing architectures: A compre- Aris Leivadeas, and Konstantinos Tserpes. Leveraging graph neural
hensivestudy. Int.J.GridDistrib.Comput,8(5):7–32,2015. networksforslaviolationpredictionincloudcomputing. IEEETrans-
[11] Bence Ligetfalvi, Ma´rk Emo˝di, Jo´zsef Kova´cs, and Ro´bert Lovas. actionsonNetworkandServiceManagement,2023.
Fundamentals of a novel debugging mechanism for orchestrated cloud [29] Li Wu, Johan Tordsson, Erik Elmroth, and Odej Kao. Microrca:
infrastructureswithmacrostepsandactivecontrol. Electronics,10(24), Root cause localization of performance issues in microservices. In
2021. NOMS 2020 - 2020 IEEE/IFIP Network Operations and Management
[12] Ro´bertLovas,Erno¨ Rigo´,Da´nielUnyi,andBa´lintGyires-To´th. Experi- Symposium,pages1–9,2020.
enceswithdeeplearningenhancedsteeringmechanismsfordebugging [30] Dongjie Wang, Zhengzhang Chen, Jingchao Ni, Liang Tong, Zheng
offundamentalcloudservices. IEEEAccess,11:26403–26418,2023. Wang, Yanjie Fu, and Haifeng Chen. Interdependent causal networks
[13] Marta Kwiatkowska, Gethin Norman, and David Parker. PRISM 4.0: for root cause localization. In Proceedings of the 29th ACM SIGKDD
Verification of Probabilistic Real-Time Systems. In Ganesh Gopalakr- ConferenceonKnowledgeDiscoveryandDataMining,KDD’23,page
ishnanandShazQadeer,editors,ComputerAidedVerification,volume 5051–5060, New York, NY, USA, 2023. Association for Computing
6806, pages 585–591. Springer Berlin Heidelberg, Berlin, Heidelberg, Machinery.
2011. [31] YuGan,GuiyangLiu,XinZhang,QiZhou,JieshengWu,andJiangwei
[14] Jo´zsef Kova´cs, Bence Ligetfalvi, and Ro´bert Lovas. Automated de- Jiang. Sleuth: A trace-based root cause analysis system for large-
bugging mechanisms for orchestrated cloud infrastructures with active scalemicroserviceswithgraphneuralnetworks. InProceedingsofthe
controlandglobalevaluation. IEEEAccess,12:143193–143214,2024. 28th ACM International Conference on Architectural Support for Pro-
[15] GiuseppeAceto,AlessioBotta,WalterDeDonato,andAntonioPescape`. grammingLanguagesandOperatingSystems,Volume4,ASPLOS’23,
Cloud monitoring: Definitions, issues and future directions. In 2012 page324–337,NewYork,NY,USA,2024.AssociationforComputing
IEEE1stInternationalConferenceonCloudNetworking(CLOUDNET), Machinery.
pages63–67.IEEE,2012. [32] FaridaAsadova,Ga´borKerte´sz,Ro´bertLovas,andSa´ndorSze´na´si.Fault
[16] SheikhUmarFarooq,SMKQuadri,andNesarAhmad.Metrics,models detection in gpu-enabled cloud systems – an overview. In 2022 IEEE
and measurements in software reliability. In 2012 IEEE 10th inter- 20th Jubilee World Symposium on Applied Machine Intelligence and
national symposium on applied machine intelligence and informatics Informatics(SAMI),pages000317–000322,2022.
(SAMI),pages441–449.IEEE,2012. [33] AndreaBiancoandLucadeAlfaro.Modelcheckingofprobabilisticand
[17] Sara Zatout, Maya Souilah Benabdelhafid, and Mahmoud Boufaida. nondeterministic systems. In International Conference on Foundations
Formal Transaction Modeling and Verification for an Adaptable Web ofSoftwareTechnologyandTheoreticalComputerScience,pages499–
Service Orchestration. In 2018 IEEE International Conference on 513.Springer,1995.
Software Quality, Reliability and Security Companion (QRS-C), pages [34] D.C.Verma. ServicelevelagreementsonIPnetworks. Proceedingsof
531–536,July2018. theIEEE,92(9):1382–1388,2004.
[18] Alireza Souri, Amir Masoud Rahmani, and Nima Jafari Navimipour. [35] Philipp Wieder, Joe M. Butler, Wolfgang Theilmann, and Ramin
Formal verification approaches in the web service composition: A Yahyapour. Service Level Agreements for Cloud Computing. Springer
comprehensive analysis of the current challenges for future research. Science&BusinessMedia,November2011.
International Journal of Communication Systems, 31(17):e3808, 2018. [36] Wubin Li, Yves Lemieux, Jing Gao, Zhuofeng Zhao, and Yanbo Han.
eprint:https://onlinelibrary.wiley.com/doi/pdf/10.1002/dac.3808. Service mesh: Challenges, state of the art, and future research oppor-
[19] MounyaSmara,MakhloufAliouat,Al-SakibKhanPathan,andZibouda tunities. In 2019 IEEE International Conference on Service-Oriented
Aliouat. Acceptance test for fault detection in component-based cloud SystemEngineering(SOSE),pages122–1225.IEEE,2019.
computingandsystems. FutureGenerationComputerSystems,70:74– [37] LeonardRichardsonandSamRuby. RESTfulWebServices. ”O’Reilly
93,2017. Media,Inc.”,2008.
[20] Aaqif Abbasi, Shahab Band, Mohammed A. A. Al-qaness, Almas [38] MatthiasFeyandJanEricLenssen. Fastgraphrepresentationlearning
Abbasi, Nahsat Al-Jallad, and Amir Mosavi. Resource-aware network withpytorchgeometric. arXivpreprintarXiv:1903.02428,2019.
topology management framework. Acta Polytechnica Hungarica, 02 [39] MichaelM.Bronstein,JoanBruna,TacoCohen,andPetarVelicˇkovic´.
2020. Geometricdeeplearning:Grids,groups,graphs,geodesics,andgauges.
[21] Rupesh Raj Karn, Rammi Das, Dibakar Raj Pant, Jukka Heikkonen, arXivpreprintarXiv:2104.13478,2021.
and Rajeev Kanth. Automated testing and resilience of microservice’s [40] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic
network-linkusingistioservicemesh.In202231stConferenceofOpen optimization. InarXivpreprintarXiv:1412.6980,2014.
InnovationsAssociation(FRUCT),pages79–88,2022. [41] JianboChen,LeSong,MartinWainwright,andMichaelJordan. Learn-
[22] Qing Cao and Haoran Niu. Higher-order markov graph based bug ingtoexplain:Aninformation-theoreticperspectiveonmodelinterpreta-
detection in cloud-based deployments. In 2022 IEEE International tion.InInternationalConferenceonMachineLearning,pages883–892.
Performance, Computing, and Communications Conference (IPCCC), PMLR,2018.
pages153–160,2022. [42] Jinsung Yoon, James Jordon, and Mihaela van der Schaar. Invase:
[23] Valeria Pontillo, Maarten Vandercammen, Sarah Verbelen, and Coen Instance-wisevariableselectionusingneuralnetworks. InInternational
De Roover. Ferrari: Failure reproduction through automatic test ConferenceonLearningRepresentations,2019.
case generation and stack trace analysis. In BENEVOL24: The 23rd [43] Dongsheng Luo, Wei Cheng, Dongkuan Xu, Wenchao Yu, Bo Zong,
Belgium-NetherlandsSoftwareEvolutionWorkshop,pages1–13.CEUR Haifeng Chen, and Xiang Zhang. Parameterized explainer for graph
Workshop Proceedings, 2024. BENEVOL 2024 : The 23rd Belgium- neuralnetwork.InAdvancesinNeuralInformationProcessingSystems,
Netherlands Software Evolution Workshop ; Conference date: 21-11- volume33,pages19620–19631,2020.
2024Through22-11-2024. [44] Ronald J. Williams. Simple statistical gradient-following algorithms
[24] PeiYun Zhang, Sheng Shu, and MengChu Zhou. An online fault forconnectionistreinforcementlearning. Machinelearning,8:229–256,
detectionmodelandstrategiesbasedonsvm-gridinclouds. IEEE/CAA 1992.
JournalofAutomaticaSinica,5(2):445–456,2018. [45] GEXFFileFormat. https://gexf.net/. [Online]Accessed28September
[25] Xiang Zhou, Xin Peng, Tao Xie, Jun Sun, Chao Ji, Dewei Liu, Qilin 2022.
Xiang,andChuanHe. Latenterrorpredictionandfaultlocalizationfor [46] Miha´ly He´der, Erno˝ Rigo´, Do´ra Medgyesi, Ro´bert Lovas, Szabolcs
microservice applications by learning from system trace logs. In 27th Tenczer, Ferenc To¨ro¨k, Attila Farkas, Ma´rk Emo˝di, Jo´zsef Kadlecsik,
ACMJointEuropeanSoftwareEngineeringConferenceandSymposium Gyo¨rgy Mezo˝, A´da´m Pinte´r, and Pe´ter Kacsuk. The Past, Present
ontheFoundationsofSoftwareEngineering,pages26–30,2019. andFutureoftheELKHCloud. Informa´cio´sTa´rsadalom(Information
[26] Fanfei Meng, Lalita Jagadeesan, and Marina Thottan. Model-based Society),XXII(2),2022.
reinforcement learning for service mesh fault resiliency in a web
application-level,2021.
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Transactions on Network and Service Management. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TNSM.2025.3602223
IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.XX,NO.XX,XXX2023 18
Da´nielUnyiisaPhDcandidateinComputerEngi-
neering at Budapest University of Technology and
Economics. His research focuses on graph-based
representation learning and explainable AI, with a
particularemphasisonvariousapplications.During
his PhD, he has earned top placements in interna-
tional data science competitions. In addition to his
academic work, he is actively involved in several
industryprojectsasadatascientist,primarilyinthe
financialandforensicdomains.
Erno¨ Rigo´ is the Head of the Department of
Network Security and Internet Technologies at the
Institute for Computer Science and Control (SZ-
TAKI), Hungarian Research Network (HUN-REN).
HereceivedhisMScdegreeinsystemsengineering
from the Budapest University of Technology and
Economics(BME).Heisanassistantlectureratthe
InstituteforCyber-PhysicalSystemsattheJohnvon
NeumannFacultyofInformatics,O´budaUniversity,
where he is also a PhD student. As an ISACA
Certified Information Systems Auditor (CISA) and
ISC2 Certified Information Systems Security Professional (CISSP), his PhD
research is focused on security evaluation of dynamic cloud infrastructures.
Heisresponsibleforsystemdesign,implementationanddaytodayoperation
of the Cloud research infrastructure of HUN-REN. His cloud and security
related research achievements contribute to the recently launched Artificial
IntelligenceandAutonomousSystemsNationalLaboratories.
Ba´lint Gyires-To´th is an associate professor at
BME. He conducts research on fundamental and
appliedmachinelearningsince2007.Withhislead-
ership, the first Hungarian hidden Markov-model
basedText-To-Speech(TTS)systemwasintroduced
in 2008. He obtained his PhD degree with summa
cumlaudeinJanuary2014.Sincethen,hisprimary
research field is deep learning. His main research
interests are sequential data modelling with deep
learning, self-supervised learning and deep rein-
forcement learning. He also participates in applied
deep learning projects, including time series modelling, anomaly detection,
computervisionandconversationalAI.Hewasinvolvedinvarioussuccessful
research and commercial projects. In 2017 he was certified as NVidia Deep
Learning Institute (DLI) Instructor and University Ambassador. His AI-
relatedresearchachievementscontributetotheArtificialIntelligenceSystems
NationalLaboratory.
Ro´bert Lovas is the deputy director of IT at
the Institute for Computer Science and Control
(SZTAKI), Hungarian Research Network (HUN-
REN). He received his PhD degree in Informatics
from the Budapest University of Technology and
Economics (BME). He is a habilitated associate
professorandthefounderoftheInstituteforCyber-
PhysicalSystemsattheJohnvonNeumannFaculty
of Informatics, O´buda University, and a member
of the Committee on Information Science at the
Hungarian Academy of Sciences. His research and
developmentexperienceinwiderangeofapplicationfieldsofdistributedand
parallelsystemshasbeengainedinvariousglobal,EUandnationalcollabo-
rationswithacademicorganizations,universities,andenterprisesfocusingon
computationalchemistry,numericalmeteorologicalmodelling,bioinformatics,
agriculture, connected cars, and Industry 4.0. He has been coordinating
EU FP7/H2020 projects, and the HUN-REN Cloud research infrastructure
of HUN-REN. His latest cloud, big data, IoT and AI-related research
achievements contribute to the recently launched Artificial Intelligence and
AutonomousSystemsNationalLaboratories.
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/