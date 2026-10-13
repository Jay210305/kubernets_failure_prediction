4884 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
TraceDAE: Trace-Based Anomaly Detection in
Microservice Systems via Dual Autoencoder
Junjun Li , Shi Ying, Tiangang Li , and Xiangbo Tian
Abstract—Microservice systems have become a popular archi- lossesforDiDiexceeding10millionorders,withatransaction
tecture for modern Web applications owing to their scalability, volume of approximately ¥400 million [6]. Consequently,
modularity, and maintainability. However, with the increasing
anomaly detection and root cause localization of microservice
complexityandsizeofthesesystems,anomalydetectionemerges
systemsareofgreatsignificance.Theynotonlyhelpusreport
asacriticaltask.Inthispaper,weintroduceTraceDAE,atrace-
based anomaly detection approach in microservice systems. The system faults accurately but also provide valuable guidance
approach initially constructs a Service Trace Graph (STG) to for subsequent fault analysis.
depict service invocation relationships and performance metrics, Anomaly detection and root cause localization in microser-
subsequentlyintroducingadualautoencoderframework.Inthis
vicesystemshavegarneredsignificantattentionovertheyears
framework, the structure autoencoder employs Graph Attention
[7], [8], [9], [10], [11]. Currently, most anomaly detection
Networks (GAT) to analyze the structure, while the attribute
autoencoder leverages the Long Short-Term Memory Network methods primarily concentrate on logs and metrics [12], [13],
(LSTM)forprocessingtimeseriesdata.Thisapproachiscapable [14], which often make it difficult to accurately determine
ofeffectivelyidentifyingServiceResponseAbnormalandService the type of anomaly and support subsequent root cause
Invocation Abnormal. Moreover, the final experimental results
localization. However, in microservice systems, there are
ondatasetsshowthatTraceDAEisanefficientanomalydetection
multipletypesofdatasources,amongwhichtracedatacarries
approachwhichoutperformstheSOTA(StateofTheArts)trace-
based anomaly detection methods with F1-scores of 0.970 and rich attribute information [15]. Among existing trace-based
0.925, respectively. approaches, a common practice is to convert trace data into
numeric vectors, which enables the application of machine
Index Terms—Microservice systems, anomaly detection, trace
analysis, dual autoencoder. learning techniques. Some approaches, notably [16] and [17],
perform analysis by defining features such as the frequency
of different business operations. Other approaches emphasize
I. INTRODUCTION thestructuralfeaturesoftheinvocationpaths,transformingthe
MICROSERVICE systems have become a popular archi- metric data on these paths into vectors.
tecture for modern Web applications attributable to Unfortunately, most existing trace-based approaches ignore
their scalability, modularity, and ease of maintenance [1], [2], therichdetailedinformationcarriedbytracedata.Westrongly
[3]. These architectures decompose services into diminutive, believe that fully utilizing the detailed information is crucial
independently deployable services that communicate over the for achieving more accurate anomaly detection and finer root
network, thereby offering complete application functionality. cause localization [18].
Even though a lot of efforts are devoted to quality assurance In this paper, we propose TraceDAE, an anomaly detection
of microservice systems, owing to their increasing size and method based on trace data in microservice systems. This
complexity, microservice systems often seem fragile and the method is based on trace data and uses metric data as
risk of system failures increases gradually [4], [5]. Once a built-in attributes to construct a Service Trace Graph (STG).
failureoccurs,itmayprecipitateservicedisruption,potentially STG not only reflects the invocation relationship between
causing significant financial losses to the organization and services but also incorporates performance metrics for each
undermining user satisfaction. For instance, on the evening invocation. Based on STG, we design two integrated autoen-
of November 27, 2023, a system failure at DiDi lasted for coders: structure autoencoder and attribute autoencoder, each
nearly 12 hours, causing a large number of users unable focusing on specific aspects of the trace data. The structure
to locate and take taxis. This malfunction resulted in direct autoencoder analyzes the structural information of the STGs
through Graph Attention Networks (GAT) to capture the
Received 29 April 2024; revised 20 September 2024; accepted 23 dependencies between services. The attribute autoencoder, on
June 2025. Date of publication 26 June 2025; date of current version
the other hand, employs Long Short-Term Memory Network
7 October 2025. This work was supported by the National Natural Science
Foundation Project of China under Grants 62472329, 62072342, and (LSTM) to process time-series data to identify anomalous
61672392,andbytheNationalKeyResearchandDevelopmentPlanProject changes in performance metrics over time. By integrating
of China under Grant 2022YFB3304300. The associate editor coordinating
the loss values of these dual autoencoders, TraceDAE can
the review of this article and approving it for publication was M. F. Zhani.
(Correspondingauthor:ShiYing.) effectively identify anomaly traces and their anomaly types
TheauthorsarewiththeSchoolofComputerScience,WuhanUniversity, in a microservice system. For the anomaly trace data, we
Wuhan 430072, China (e-mail: lijunjun@whu.edu.cn; shiying@whu.edu.cn;
compute the anomaly score for each microservice to locate
tiangangli@whu.edu.cn;tianxiangbo@whu.edu.cn).
DigitalObjectIdentifier10.1109/TNSM.2025.3583213 the root cause of the anomaly traces. We conducted extensive
1932-4537©2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligence
andsimilartechnologies. Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4885
experiments to compare the performance of six SOTA(State them as semantic vectors and then detects the semantic
of The Arts) trace anomaly detection methods based on items by Transformer’s classification model, which captures
Train-Ticket[19],anopen-sourcemicroservicebenchmark,as contextualinformationfromlogsequences.Heetal.proposed
well as a large-scale Internet service provider’s production amethodTopoMAD[22]foranomalyanalysisdetectionusing
microservice system. The experimental results show that the spatiotemporal deep learning. The method collects data such
TraceDAE performs excellently in F1-scores, reaching 0.970 as CPU, memory, disk, and network metrics from containers
and 0.925 respectively, which are 0.235 and 0.11 higher than to capture temporal and spatial dependencies. The method
the highest scores of the baseline method. Our contribution utilizes graph neural networks to extract spatial features and
can be summarized as follows: LSTM networks to extract temporal features. Zhang et al.
1. We propose a Service Trace Graph (STG) construction proposed a time series anomaly detection model TFAD [23]
method. It integrates trace and metrics into a graph to rep- based on time-frequency analysis, which incorporates time
resent microservices and their invocations, thus providing a series decomposition and data expansion mechanism in the
comprehensive view of system operations and interactions. time-frequency architecture to improve the performance and
2. We design a dual autoencoder architecture that com- interpretability of anomaly detection. Yang et al. proposed
bines structure autoencoder and attribute autoencoder, and MicroMILTS [24], a microservice fault localization method
utilizes Graph Attention Network (GAT) and Long Short based on mutual information and LSTM autoencoder, which
Term Memory Network (LSTM) to capture structural and uses the BIRCH clustering algorithm to analyze performance
attribute features of trace data, respectively. In this way, we metrics associated with microservice anomalies for anomaly
can effectively detect response time anomalies and invocation detection. Although these methods have good performance
path anomalies in microservice invocations. in anomaly detection for microservices, most of them
3. We design and implement TraceDAE and conduct ignore the trace data that is related to the invocation
extensive experiments using two different datasets. The information that can react to more microservice system
| experimental    | results   | show    | that our      | approach |       | performs well | interactions. |     |     |     |     |     |     |     |
| --------------- | --------- | ------- | ------------- | -------- | ----- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| in microservice | trace     | anomaly | detection,    |          | with  | average F1-   |               |     |     |     |     |     |     |     |
| scores of       | 0.970 and | 0.925   | respectively, |          | which | are 0.235 and |               |     |     |     |     |     |     |     |
0.119 higher than the most advanced methods on average. B. Anomaly Detection Based on Traces
The remainder of this paper is organized as follows. With the emergence of trace data in microservice systems,
Section II provides the related work. Section III further some research work has been conducted to perform anomaly
introduces some basic concepts and the problem definition. detection based on trace data. Early research converted traces
Section IV presents our approach. Section V discusses the into numerical vectors and then used machine learning tech-
experimental setup and presents the results of our evaluations. niques for anomaly detection. Las-Casas et al. proposed a
Section VI concludes the paper, summarizing key contribu- method [16] based on execution graph clustering for the
tions and suggesting avenues for future research. overhead and storage requirements of traces, which can
|     |     |     |     |     |     |     | bias the | requested | traces, | and | improve | the | storage | problem |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------- | --- | ------- | --- | ------- | ------- |
II. RELATEDWORK of storing the diversity of traces in infrequent patterns.
|                  |             |         |                 |         |           |              | Fu et al.       | constructed  |              | a finite  | state         | automaton        | FSA         | [25]      |
| ---------------- | ----------- | ------- | --------------- | ------- | --------- | ------------ | --------------- | ------------ | ------------ | --------- | ------------- | ---------------- | ----------- | --------- |
| Anomaly          | detection   | in      | microservice    | systems | is        | an important |                 |              |              |           |               |                  |             |           |
|                  |             |         |                 |         |           |              | to learn        | the time     | distribution |           | and           | detect anomalies |             | k-sigma   |
| research         | field [20], | [21].   | Many related    |         | research  | works have   |                 |              |              |           |               |                  |             |           |
|                  |             |         |                 |         |           |              | based on        | trace        | data. The    | above     | methods       | only             | encode      | trace     |
| been proposed.   | Depending   |         | on the          | type of | data and  | techniques   |                 |              |              |           |               |                  |             |           |
|                  |             |         |                 |         |           |              | data as         | a numerical  |              | value,    | without       | utilizing        | the         | complex   |
| used, these      | works       | can be  | categorized     | into    | different | classes.     |                 |              |              |           |               |                  |             |           |
|                  |             |         |                 |         |           |              | structural      | information  |              | of trace. | Nedelkoski    |                  | et al.      | proposed  |
| In this section, | we          | provide | a comprehensive |         | review    | of related   |                 |              |              |           |               |                  |             |           |
|                  |             |         |                 |         |           |              | Multimodal-LSTM |              | [26],        | a         | deep learning |                  | model based | on        |
| works and        | discuss     | them    | in detail.      |         |           |              |                 |              |              |           |               |                  |             |           |
|                  |             |         |                 |         |           |              | time series     | learning,    | which        | uses      | LSTM          | networks         | to          | construct |
|                  |             |         |                 |         |           |              | a multimodal    | architecture |              | to        | detect        | microservice     | anomalies   |           |
A. Anomaly Detection Based on Logs and Metrics using structural features of response time and trace. Liu et al.
Some of the early-stage anomaly detection methods were proposed TraceAnamoly [27], a trace anomaly detection
based on logs and performance metrics. Meng et al. proposed method based on a deep Bayesian network that encodes
LogAnomaly [12], a framework for modeling a log stream traces as STVs and uses VAE to detect anomalous traces.
as a natural language sequence. Utilizing template2vec to Zhang et al. proposed CRISP [28], which represents traces
extract the semantic information hidden in log templates, as STV(Service Trace Vector) and detects trace anomalies
LogAnomaly can detect both sequential and quantitative log through VAE reconstruction. These methods encode trace as
anomalies. Li et al. proposed SwissLog [13], a deep learning- a vector, which although utilizing the structural information
based anomaly detection model. This model introduces a of trace, still do not fully exploit the potential of the complex
log parser that combines semantic embedding and tempo- attribute information carried by trace.
ral embedding to train a unified attention-based BiLSTM In recent years, several research works have focused on the
model for solving problems caused by log order changes structural properties of traces, transforming them into tree or
and log time interval changes. Zhang et al. proposed graph structures. Deep learning algorithms have been used to
NeuralLog [14], a log anomaly detection method without learn the call characteristics between traces in depth to enable
parsing. The method extracts raw log messages to represent anomaly detection.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore.  Restrictions apply.

4886 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
Meng et al. [29] and Wang et al. [30] proposed a method each service s interacts with others through network
i
to detect microservice anomalies by comparing execution calls. These interactions generate trace data, which
traces, which calculates trace anomalies by tree edit distance can be represented as a sequence of traces T =
and detects response time anomalies by principal component {(t1 ,s1 ,s2 ,x1 ),(t2 ,s2 ,s2 ,x2 ),...,(t
i
,s
i
,s
j
,x
i
)}, where t
i
analysis. TraceLingo [31] and DeepTraLog [32] use LSTM denotes the timestamp of the ith interaction, s ,s signifies
i j
and GNN methods, respectively, to capture the tree structure the microservice s invoking the microservice s , and x
i j i
in the trace to obtain an accurate representation of the trace. represents a high-dimensional vector capturing the features
TraceLingo requires supervised training, while DeepTraLog extracted from that interaction, including but not limited to
uses additional logging data. TraceVAE [33] encodes traces the source and target services and response times.
as graph structures and proposes a solution for graph VAE. To illustrate this with an example, consider a simple
Zhang et al. proposed a comparative representation learning e-commerce microservice system where the user authentica-
method,TraceCRL[34],whichrepresentstracedataasagraph tion service s1 calls the user profile service s2 to retrieve
structure,andmakessimilartracescloserintherepresentation user details. This interaction would be logged as a trace like
space through representation learning for more accurate and (t1 ,s1 ,s2 ,x1 ), where t1 is the timestamp of the request, and
efficient anomaly detection and fault diagnosis. x1 could include features like the response time of the user
Although these methods fully consider the structural profile service, the size of the response, and the success or
information of trace, they do not integrate the attribute failure status of the interaction.
information of trace to comprehensively achieve anomaly Our core goal is to design and develop a model TraceDAE
detection and further analyze the types of anomalies in the for identifying anomalous trace T in microservice systems S.
results of anomaly detection. Here, an anomaly is characterized as a significant deviation
from the normal mode of operation of a microservice system,
C. Root Cause Localization Based on Traces indicativeofapotentialproblemorfailure.Forinstance,ifthe
response time of a service, such as the payment processing
Tracedescribestheinvocationrelationshipsbetweenservices
service in an e-commerce system, suddenly increases beyond
in a microservice system, which provides an important basis
its typical range, this could signal an issue such as network
for fault root cause localization methods. Liu et al. proposed
latency, resource exhaustion, or a software bug. TraceDAE
a microservice system root cause of failure localization
aims to detect such deviations automatically, helping to main-
method MicroHECL [35], which analyzes potential anomaly
tain the system’s reliability and performance.
propagation chains based on service invocation graphs and
In order to better represent the invocation relationship
rankscandidateserviceinstancesbasedoncorrelationanalysis
between services, TraceDAE constructs the trace data T as a
todiscoverarankedsequenceofpotentiallyfaultymicroservice
Service Trace Graph STG = {V, E, X}, where V represents
instances. Yu et al. proposed MicroRank [36], a root-cause
the set of services involved in the trace acting as nodes
localizationmethodbasedontheextended-spectrumtechnique,
in the graph, E denotes the service invocations, acting as
which identifies the root cause of a fault by pre-training
edges connecting the nodes, and X denotes the latency and
features in normal and abnormal trace data. Zhou et al.
performance metrics generated when the service is invoked,
proposed an approach MEPFL [17] for fault localization
which is also referred to as the service attribute matrix. The
in microservice applications, which predicts potential faults
STG is formally a graph with M nodes, each associated with
by analyzing the trace logs of the application. Lin et al.
an N - dimensional attribute vector, where N represents the
proposedanapproachMicroScope[37]forfaultlocalizationin
number of features used to characterize the interactions.
microservice applications, which uses directed acyclic graphs
Intheanomalydetectionphase,TraceDAEencodestheSTG
to represent dependencies between microservices. Li et al.
by a dual autoencoder, then computes its reconstruction loss
proposed TraceRCA [38], which uses unsupervised machine
functionvalue.Moreformally,weaimtolearnalossfunction
learningtodetectvariousmetricsoverthesameperiodinatrace
L : T (cid:2)−→ y ∈ R, to classify the sample T based on the
toidentifyanomaloustraces.Foranomaloustraces,TraceRCA i i i
threshold λ:
calculates a suspicion score by passing in and outputting the (cid:2)
numberoftracesofanomalouscallsandranksallmicroservices. y = 1, ifL(T i )≥λ (1)
Although these methods utilize trace structure for root cause i 0, otherwise
localization, they do not take full advantage of the feature
where y denotes the label of sample trace T , with 0 being
information contained in the traces. i i
the normal class and 1 being the anomalous class.
For abnormal traces, in more detail, we classify them into
III. PROBLEMDEFINITION
two categories based on their different characteristics Service
In this section, we outline the service invocation relation- Response Abnormal and Service Invocation Abnormal.
ships in microservice systems and provide a formal definition • ServiceResponseAbnormal:Itmeansthatthedurationof
of the trace exception detection problem for microservice the response to a user request deviates significantly from
systems. Table I enumerates the relevant notations and their the normal value, either being too long or abnormally
descriptions, providing a basis for the subsequent discussion. short. This may occur, for example, when an application
We define the microservice system as an interconnected faces resource constraints due to a large number of
network of services S = {s1 ,s2 ,...,s
N
}, where requests or irregular resource utilization patterns.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4887
TABLEI
COMMONLYUSEDNOTATIONS
Fig.1. TheoverviewofTraceDAEworkflow.
• Service Invocation Abnormal: It denotes a significant Graph STG to represent the relationship of microservice
| change | in the execution | path | of a trace. This | may occur | invocations. |     |     |     |
| ------ | ---------------- | ---- | ---------------- | --------- | ------------ | --- | --- | --- |
when there are noticeable deviations in the sequence • Step3:Noisereducing.Tosanitizethedatasetandelimi-
of microservice invocations. For instance, errors within nateunwantednoise,weemploydensity-basedDBSCAN
certain microservices, such as network disruptions, can clustering [39]. This technique effectively filters out out-
result in the interruption of user requests, leading to liers, ensuring the accuracy and reliability of subsequent
| changes | in the expected | invocation | path. |     | analysis. |     |     |     |
| ------- | --------------- | ---------- | ----- | --- | --------- | --- | --- | --- |
By categorizing anomalies in this way, we can more • Step 4: Training model. During the training phase, the
precisely diagnose the root cause of potential issues in model learns to extract relevant features from different
microservice systems, leading to more targeted and effective data modalities and encode their interactions effectively.
troubleshooting. It then uses attention mechanisms to assign weights to
differentfeaturesbasedontheirrelevanceandimportance
|     |     |              |     |     | for detecting      | anomalies. |               |              |
| --- | --- | ------------ | --- | --- | ------------------ | ---------- | ------------- | ------------ |
|     |     | IV. APPROACH |     |     |                    |            |               |              |
|     |     |              |     |     | • Step 5: Abnormal | detection. | For each STG, | we calculate |
A. Overview
|     |     |     |     |     | an anomaly | score. If | this score surpasses | a predefined |
| --- | --- | --- | --- | --- | ---------- | --------- | -------------------- | ------------ |
In this section, we present the TraceDAE, a trace-based threshold γ, the STG is marked as an outlier, indicating
anomaly detection method in microservice systems via dual potential abnormalities.
autoencoders, which can efficiently detect trace anomalies. • Step6:Rootcauselocalization.ForeachabnormalSTG,
Figure 1illustratestheoverallworkflowofthemethod,which we compute anomaly scores for each node. The node
can be concluded by several steps as follows: with the highest anomaly score among thetop k nodes is
• Step 1: Collecting origin data. microservice systems identified as the likely root microservice responsible for
| generate    | a continuous | stream      | of raw data,   | encompassing   | the anomaly.    |     |     |     |
| ----------- | ------------ | ----------- | -------------- | -------------- | --------------- | --- | --- | --- |
| trace and   | metric       | data. The   | trace data     | describes the  |                 |     |     |     |
| invocation  | dependencies | between     | microservices, | and the        |                 |     |     |     |
|             |              |             |                |                | B. Building STG |     |     |     |
| metric data | is the       | performance | indicator      | data generated |                 |     |     |     |
during the service invocation. Microservice systems accurately reflect their operational
• Step 2: Building STG. Based on the collected trace status through various types of raw data. As shown in
and metric data, we construct them as a Service Trace Fig. 2, we propose a method to convert service invocation
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore.  Restrictions apply.

4888 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
Algorithm 1 Constructing the Service Trace Graph (STG)
Input: Trace data T, containing trace records; each trace
recordconsistsofserviceinvocationswithSpanID,Trace
ID, and temporal performance data CPU Mem Time.;
Output: STG = (V, E);
1: Initialize an empty graph STG =(V,E)
2: for each trace record r in T do
3: Initialize an empty list nodesList ← []
4: for each service invocation s in r do
Fig.2. TheoverviewofbuildingtheServiceTraceGraph(STG). 5: Extract or generate unique Span ID for service
invocation s
6: Extract temporal performance data associated with s
relationships in the microservice system into a unified graph 7: if Span ID of s is not in V then
representation called the Service Trace Graph (STG). This is 8: Create a new node v with Span ID as identifier
a crucial step for effectively applying TraceDAE to anomaly 9: Attach temporal performance data to v
detection. The STG is designed to capture the complex inter- 10: Add v to the graph STG
actions and dependencies between microservices, including 11: end if
both the invocation relationships and the performance metrics 12: Append v to nodesList
of the services, which are essential for subsequent analysis 13: end for
and processing. The following section provides a detailed 14: for each consecutive pair of nodes (v source ,v target ) in
explanation about how to build a STG: nodesList do
1) CollectingTraceData.Foramicroservicesystem,there 15: if edge (v source ,v target ) is not in E then
are hundreds of microservices. We collect trace data 16: Create a new directed edge e from v source to
andtemporalperformancedatageneratedduringservice v target
invocation and store them in a temporal database. 17: Add e to the graph STG
2) Preprocessing Trace Data. For the collected trace data, 18: end if
we normalize the data to ensure consistency. When a 19: end for
service generates trace data in different formats, we 20: end for
preprocess it to ensure that each user request generates 21: return STG.
auniqueTraceId,andeachserviceinvocationgenerates
a unique Span ID.
3) Constructing STG Nodes. For each trace record, we traditional graph representation learning techniques such as
construct the unique Span ID generated by the service TraceCRL [34] utilizing DeepWalk [40] traversal operations
invocationasanodeintheSTG.Differentfromprevious on dependency graphs, TraceDAE introduces an innovative
approache TraceCRL [34], where nodes represent ser- treebasedgraphconstructionalgorithmspecificallyoptimized
vice operations, in our STG, nodes represent entire for the STG construction process. This Algorithm 1 not only
services. Moreover, the temporal performance data gen- significantly improves the generation efficiency and quality
erated by the service invocation is attached as attributes of STG, but also further highlights the unique advantages
of the node, which include metrics such as timestamp, and innovative significance of STG in anomaly detection and
average response time, CPU usage, and memory usage. analysis of microservice systems.
This structure allows the STG to encapsulate a richer
set of information compared to traditional operation
C. TraceDAE
invocation graphs.
4) ConstructingSTGEdges.Foreachtracerecord,wecon- The TraceDAE model is an unsupervised joint learning
struct service invocation dependencies from the source framework designed to address the problem of trace anomaly
service node to the target service node as edges in the detection in microservice systems. As shown in Fig. 3,
STG. In contrast to the edges in TraceCRL’s operation TraceDAE achieves a comprehensive analysis of microservice
invocation graph [34], which also encodes operation tracedatabyfusingtwocorecomponents,thestructureautoen-
states and predefined attributes, our STG focuses on coderandtheattributeautoencoder.Thestructureautoencoder
representing the invocation relationships at the service captures the structural information in the microservice system
level,withtheassociatedperformancemetricsembedded through the graph autoencoder (GAE). The attribute autoen-
within the nodes rather than the edges. coder focuses on processing temporal data, i.e., changes in
TraceDAE has made significant breakthroughs in handling attributes, through the LSTM autoencoder (LSTM-AE). By
service invocation relationships in microservice systems with integrating the loss values of these two components as the
its unique four core steps. These steps cleverly transform anomaly score, the TraceDAE model is able to accurately
the originally intricate invocation relationships into a clear detect trace response times and invocation path anomalies.
and structured form, thereby constructing a unified service Next, we describe in detail the design of these two autoen-
trace graph (STG) as the core graph representation. Unlike coders and how they are integrated into a unified model.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4889
Fig.3. ThearchitectureofTraceDAE.
1) Structure Autoencoder: The core of a structure autoen- where N represents the set of neighbors for the node h
i i
coder lies in leveraging attention mechanisms to learn the provided by the adjacency matrix A. The final embedded
structuralrelationshipsbetweenservicenodesandtheirneigh- representation Z for node h is then derived by aggregating
i i
bors, aiming to capture effective structural patterns. This the representations of its neighbors, obtained by weighting
model comprehends the contextual surroundings of a service based on the learned significant weights as follows:
(cid:9)
node within the entire microservice architecture. By adopting
an attention mechanism, the structure autoencoder evaluates Z i V = (γ i,k ×h (cid:6) k ) (6)
the relative significance among nodes and their neighbors,
k∈Ni
facilitating the learning of impactful structural patterns. The structured autoencoder concludes with a structure
To enhance the dimensionality of node features, the struc- decoder that uses the embedded representations ZV as inputs
ture autoencoder initially transforms the originally observed to reconstruct the original node network structure. The recon-
node attribute X into a lower-dimensional latent representa- struction is achieved through:
tion, denoted by Z (cid:3)V. This transformation is defined as: (cid:4) (cid:5) (cid:4) (cid:5)
A ˆ =σ ZV(ZV)T =sigmoid ZV(ZV)T (7)
Z (cid:3)V =σ(XW x +b x ) (2)
where sigmoid(·) denotes the sigmoid activation function.
where σ(·) represents an activation function, such as ReLU This step utilizes the inner product between pairs of node
or Tanh. Here, W x ∈ RM×D and b x ∈ RD are the weight embeddings to estimate the probability of a link existing
matrix and bias vector learned by the encoder, M and D are between two nodes:
the dimensionalities of X and Z
(cid:3)V,
respectively.
(cid:4) (cid:5) (cid:4) (cid:5)
After performing the transformation, we treat Z (cid:3)V as p A ˆ i,j =1|Z i V,Z j V =sigmoid Z i V(Z j V)T (8)
a graph attention layer with node eigenvalues of Z (cid:3)V =
{Z (cid:3) 1 V,Z (cid:3) 2 V,...,Z (cid:3) N V}, where N is the number of nodes. We of T th h e e n s e t t r w uc o t r u k r , e fa a c u i t l o it e a n t c in o g de th r e ca re n co le n a s r t n ru t c h t e ion str o u f c t t h u e ra n l e p tw at o te r r k n ’ s s
perform a shared attention mechanism on the nodes, employ-
topology based on the learned embeddings. By integrating
ing graph attention layers to aggregate representations from
attention mechanisms, the autoencoder not only captures
neighboring nodes:
(cid:4) (cid:5) the direct relationships between nodes but also effectively
e i,j =attn Z (cid:3) i V,Z (cid:3) j V (3) learns from the overall structure of the microservice system,
enhancing its ability to model complex networks.
where e i,j denotes the importance weight of the node V i 2) Attribute Autoencoder: The attribute encoder focuses
relativetonodeV .Thefunctionattn(·)signifiesaweightthat on analyzing the attribute information in service requests
j
isuniformlyappliedacrossallnodes.Here,weuseLeakyReLU and responses, such as the duration of the request. Using
function. Consequently, e i,j can be described as follows: the LSTM-AE model, the attribute encoder can effectively
(cid:2) (cid:4) (cid:2) (cid:5) (cid:6)(cid:4) capture dependency relationships in time series data to learn
ei,j =attn Z (cid:3) i V,Z (cid:3) j V =LeakyReLU αT WZ (cid:3) i V||WZ (cid:3) j V (4) dynamic patterns of service behavior. Compared to traditional
RecurrentNeuralNetworks(RNNs),LSTMcanperformbetter
whereα∈RD andW ∈R D 2 ×D representtheneuralnetwork in processing longer sequences thanks to their ability to
weights that parameterize the attention mechanism, shared maintain two states: the cell state (c t ) and the hidden state
across all nodes. The operator || denotes concatenation. Then, (h t ), for the current input (X t ) and the previous hidden state
softmax is used to normalize the neighboring nodes of the (h t−1 ). The forward propagation in an LSTM cell with a
central node: forget gate involves the following equations:
(cid:6) (cid:7) (cid:6) (cid:7)
γ i,j =softmax (cid:6) e i,j (cid:7) = (cid:8)
k∈
e
N
xp
i e
e
x
i
p
,j(cid:6)
e i,k
(cid:7) (5) Fo
I
r
n
g
p
e
u
t
t
g
g
a
a
te
te
:
:
f t
i t
=
=
σ
σ
g
g (
W
W
f
i
X
X
t
t
+
+
U
U
f
i
h
h
t
t
−
−
1
1
+
+
b
b
f
i )
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

4890 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
Output gate : o t =σ g (W o X t + U o h t−1 + b o ) N 2) and O (MD + NM), respectively, where N is the number
Cell input : (cid:3)c t =σ c (W c X t + U c h t−1 + b c ) of nodes, E is the number of edges, M is the dimension of
attributes, and D is the dimension of embeddings.
Cell state update : c t =f t (cid:7)c t−1 +i t (cid:7)(cid:3)c t
Hidden state update : h t =o t (cid:7)σ h (c t ) (9) D. Anomaly Detection
Here, we designate d and h as the number of input features
In the anomaly detection component, we use the learned
and the number of hidden units, respectively the operator (cid:7)
joint representation from the multi-modal learning stage to
theHadamardproduct.Thevectorsi t ,f t ,o t aretheactivations detectanomaliesinrealtime.Wemonitorthesystem’sbehav-
fortheinput,forget,andoutputgates,respectively.Theweight
iorusingreal-timedatainputsandcompareitwiththelearned
matrices W f,i,o,c ∈ Rh×d and recurrent weights U f,i,o,c ∈ normal behavior represented by the joint representation. Any
Rh×h are learned during training. The bias vectors b f,i,o,c ∈ deviations from the learned normal behavior indicate an
Rh are used for each gate and cell state update. The LSTM exception to the prescribed specifications of this template.
unit receives an input vector x t ∈ Rd. The initial values for Given the significant changes in communication modes
the cell and hidden states are set to c0 = 0 and h0 = 0, during different application stages (including rise, run, and
respectively. During the computation process, σ g represents fall stages), our approach responds by dynamically adjust-
the sigmoid activation function, σ c and σ h refer to the ing strategies. Specifically, we recalculate the threshold and
hyperbolic tangent function. optimize the anomaly detection parameters based on the
In the attribute encoder, we employ the LSTM-AE model specificstagewearecurrentlyin.Takingtheupgradephaseas
to encode the monitored microservice feature attribute time anexample,therearesignificantdifferencesincommunication
seriesdataX,(includingrequestresponsetime,CPUusageand frequency and types between microservices compared to the
memory usage) into an attribute embedding hidden layer ZX, runtime phase. Therefore, we adjust the time window settings
whichisveryimportantforTraceDAE.Inthedecodingphase, and thresholds immediately when detecting phase transitions
the attribute decoder fuses the node embedding ZA and the toensurethatthemodelcanflexiblyrespondtothesedynamic
attribute embedding ZX learned by the structure autoencoder, changes.
which is used as the input for decoding the original node In addition, our approach deeply considers the differences
attributes: between microservices. For microservices that assume differ-
(cid:4) (cid:5)
X ˆ =ZV ZA T (10) entroles(e.g.,front-endservices,businesslogichandlers,and
back-endservices),werecognizethattheyeachexhibitunique
3) Joint Optimizing: The outputs of the structure autoen- communication patterns. To improve the accuracy of anomaly
coder and the attribute autoencoder are jointly optimized by detection, we adopt customized aggregation and anomaly
integrating them into a unified model. This integration is detection methods for each type of microservice. In partic-
achieved through the calculation of the reconstruction loss ular, for microservices with extremely short lifecycles (e.g.,
score, which evaluates the model’s capacity to rebuild the processing a single request in milliseconds) [41], traditional
structuralandattributeinformationofagivennodeaccurately. detection methods are challenged by a limited observation
To emphasize the importance of different features, we assign window. To address this problem, we introduce aggregated
weights to the reconstruction losses associated with them. metrics and historical pattern analysis based on microservice
The primary aim of TraceDAE’s training is to reduce the types to effectively capture and identify anomalous behaviors
reconstructionlossesrelatedtoboththenetworktopologyand even in short-lived instances. At the same time, we flexibly
the node attributes: adjust the monitoring frequency according to the expected
(cid:10)(cid:4) (cid:5) (cid:10) (cid:10)(cid:4) (cid:5) (cid:10)
L=α (cid:10) (cid:10) A−A ˆ (cid:7)θ (cid:10) (cid:10) 2 +(1−α) (cid:10) (cid:10) X −X ˆ (cid:7)η (cid:10) (cid:10) 2 (11) lifetimeofthemicroservicestoensuremoreefficientanomaly
detection within the limited lifecycle.
F F
where α denotes the parameter that adjusts the balance Finally,wecalculatetheanomalyscoreforeachtraceusing
the final loss value formula:
between structure and attribute reconstruction. The symbol
(cid:7) denotes the Hadamard product. The variables η and θ Anomaly Score(x )= x i −μ x (13)
are defined to penalize the reconstruction error of non-zero i σ
x
elements more heavily, compensating for the presence of
where x i is the current data poi(cid:2)nt, μ x is the mean of the
missing edges or a θ tt i r , i j b = ute (cid:2) s 1 θ in , , o i e f t m A h p e i i r , r j w ic = i a s l e 0 datasets: d d a ev ta ia p ti o o i n n , ts c , a c lc a u lc la u t l e a d te a d s a σ s x μ = x = (cid:2) i∈N i∈ N ( N x N i − xi μ , x) σ 2 x . is the standard
η i,j = (cid:2) 1 η , , i o f t X he i r ,j w = ise 0 (12) σ x T r h e e pr t e h s r e e n s t ho t l h d e γ me is an de a fi nd ned sta a n s da μ rd x + dev 3 i σ a x ti , on w , h r e e r s e pe μ c x tiv a e n ly d ,
of historical data. A trace is labeled as an anomaly if its
In these definitions, both η and θ are greater than 1, anomaly score exceeds γ. We establish a time window to
indicatingtheadditionalpenaltiesappliedtothereconstruction compute the mean and standard deviation based on historical
of non-zero elements due to missing edges or attributes. data during that time period. Setting the time window too
In TraceDAE, the computational complexity of the struc- small can result in too many false anomalies, while setting it
turalautoencoderandattributeautoencoderareO(ND+ED+ too large will prevent the detection of anomalies. Based on
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4891
business experience, we set the time window to 30 minutes, service instances. We utilize cAdvisor2 and OpenTelemetry3
which can be manually adjusted during runtime. to collect performance metrics and trace data, respectively.
Prometheus4 is used for the persistent storage of collected
data, ensuring that all metrics and traces can be efficiently
E. Root Cause Localization
queried and analyzed over time. In addition, to simulate real
When an anomaly is detected, TraceDAE analyzes the
user requests and workloads, we use Locust5 to set specific
abnormal trace for the root cause. Each node within the
userbehaviorscriptsandrequestfrequenciestogeneratetraffic
trace represented as N , is scrutinized for deviations from
i patterns that are close to real-world scenarios. To obtain a
normal behavior, focusing on both its structural and attribute
comprehensive sample of anomalies, we inject various types
characteristics. The anomaly score S for node N is defined
i i of faults into the train ticket system. As shown in Table III,
based on the observation that abnormal nodes differ from the
these faults include scenarios such as high CPU utilization,
majority in terms of structure or attributes. We quantify the
memory leaks, network congestion, and pod crash loops.
reconstruction error from both the network structure and node
Over the two hours, we collected 242,259 traces, including
attribute perspectives:
both normal operations and fault-injected scenarios, leading
(cid:7)(cid:2) (cid:4) (cid:7) (cid:7)(cid:2) (cid:4) (cid:7)
S =α (cid:7) (cid:7) A −Aˆ (cid:2)θ (cid:7) (cid:7) 2 +(1−α) (cid:7) (cid:7) X −Xˆ (cid:2)η (cid:7) (cid:7) 2 (14) to the construction of 200 distinct fault conditions across four
i i i F i i F categories. Of these, 26,751 traces (approximately 11.04%)
where A and X represent the actual network structure were impacted by faults. Notably, 11 of these conditions
i i
and node attributes, respectively, while A and X denote are designed to emulate complex, multi-root cause faults,
i i
their predicted values based on the model. The symbols reflectingtheintricatenatureofreal-worldsystemfailures.The
θ and η are weights applied to the network structure and fault conditions are distributed as follows: 1.99% is related
node attributes, respectively. The parameter α balances the to high CPU usage, 2.54% is related to memory leaks, and
importancebetweenstructuralandattributediscrepancies,and 4.77% is related to network abnormalities, all of which can
the Frobenius norm ((cid:8)·(cid:8) ) measures the magnitude of these lead to abnormal service responses. Additionally, 3.48% are
F
discrepancies. relatedtopodabnormalities,whichcancauseabnormalservice
Based on the calculated anomaly scores, TraceDAE identi- invocation. The average depth of trace data is 6.3 spans,
fies and ranks the nodes with the highest deviations, labeling providing rich contextual information for each operation.
the top-k as anomalous. It further correlates these anomalous For ease of reference, we refer to the Train-Ticket dataset
nodes with their corresponding microservices using the trace as D1.
featurematrix,thushighlightingthetopkmicroserviceslikely 2) Online Microservice System Dataset D2: Dataset D2
responsible for the anomalies. This methodology allows for originates from an operational e-commerce microservice
systematic identification and analysis of anomalies within system. To ensure the accuracy and reliability of the data,
complex microservice architectures, aiding in swift and accu- we specifically invite professional operators to annotate the
rate troubleshooting. traces in the dataset and to conduct a thorough classification
of anomaly types. As a result of their efforts, we collect a
total of 1,136,825 trace records. The average depth of trace
V. EVALUATION
recordsis6.8spans.Amongthese,17,041traces(representing
A. Dataset 1.50%ofthetotaldataset)areidentifiedasfaulty.Thesefaulty
In this study, we evaluate the anomaly detection effective- tracesarefurthersubdividedintotwotypes:ServiceResponse
nessofTraceDAEwithdatasetsgeneratedbytwomicroservice Abnormal and Service Response Abnormal. However, due to
systems. The first dataset, D1, comes from Train-Ticket,1 a the sensitivity of the information contained in the dataset,
widely used open source microservice benchmarking system. including commercial confidentiality and user privacy, direct
The second dataset, D2, is derived from the production public access to the dataset is limited. We are exploring ways
microservice system of a large Internet company, which toprovideaccesstosanitizedversionsofthedatasetstoprotect
includes several data sources such as system metrics, user user privacy and comply with confidentiality agreements.
behaviorlogs,andtransactiondata.Thedetailsofthedatasets
are provided in Table II, which includes the number of
microservice instances, the number of failures that occurred B. Experiment Setup
in the microservice instances, and the total number of trace We have implemented the TraceDAE using a combination
records in each dataset. of transformer-based attention mechanisms and LSTM-based
1) Train-Ticket Dataset D1: We deploy the microservice memory networks. By integrating the advantages of both and
system to generate the Train-Ticket dataset. The system is fully exploiting their interactions, we are able to provide a
deployed on a Kubernetes cluster of four servers, which more comprehensive and in-depth representation of system
consistsofthreeworkernodesrunningtheapplicationservices behavior. The TraceDAE model has been constructed and
and a master node responsible for coordinating cluster activ-
ities and resource allocation, each equipped with a 12-core
2https://github.com/google/cadvisor
2.4 GHzCPUand12GBRAM,capableofdeployingmultiple 3https://opentelemetry.io
4https://prometheus.io
1https://github.com/FudanSELab/train-ticket 5https://locust.io
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

4892 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
TABLEII
THEDETAILSOFDATASETS
TABLEIII
THETYPESOFFAULTINJECTIONANDDETAILED
trainedwithinthePyTorchframework.Thesource6 ispublicly • F1-score: the harmonic mean of precision and recall,
available. providing a balance between the two metrics, which can
To optimize the TraceDAE model, we employ the Adam be calculated as: F1−score =2× Precision×Recall.
Precision+Recall
optimizer, chosen for its adaptive learning rate capabilities, To evaluate the precision of TraceDAE in root cause
making it well-suited for our complex data. The learning rate localization, we use the common evaluation metric Top-k
issetto0.001,balancingspeedandaccuracy,andabatchsize accuracy (A@k).
of 32 is found optimal for our GPU memory constraints. We • Top-k Accuracy (A@k): This metric measures the like-
set the number of epochs to 100 and use early stopping if the lihood that the actual root causes are among the top-k
validation loss does not improve for 10 consecutive epochs. identified candidates. For our evaluation, we select k
The embedding dimension of the two datasets is set to 128, values of 1, 2, and 3 to cover a range of scenarios.
and the parameters (α, η, θ) are set to (0.1, 5, 40) and (0.1, Based on the above metrics, we can evaluate the effec-
3, 10). The experiments are conducted on a high-performance tiveness of TraceDAE and comparative baseline SOTA(State
computer equipped with NVIDIA GeForce RTX 4050 Laptop of The Arts) methods in anomaly detection and root cause
GPU, which accelerates the speed of model training. localization in microservice systems.
C. Performance Metrics
D. Baseline Methods
To evaluate the performance of our approach, we use three
common evaluation metrics for anomaly detection: precision, TocomprehensivelyevaluatetheperformanceofTraceDAE
recall,andF1-score.Traceanomalydetectionisapproachedas in anomaly detection, we compare it against six SOTA trace
a binary classification task for each trace, where the F1-score anomaly detection methods, including the latest deep learning
servesasacriticalmetricforevaluatingperformance.TheF1- and machine learning-based methods, as well as solutions
scoreisderivedfromthecountsoftruepositivesamples(TP), designed specifically for microservice systems.
false positive samples (FP), and false negative samples (FN) • FSA[25].Usesafinite-stateautomatontocaptureinvoca-
produced by the model tasked with identifying failures. In tiondependenciesandtimeconsumptions,flaggingtraces
addition,weexpandourevaluationbyincorporatingadditional as anomalous if rejected by the FSA. This approach is a
metricssuchasROC-AUCandpreciserecallcurvestooffera classical method widely recognized for its effectiveness
more comprehensive assessment of TraceDAE’s effectiveness. in trace anomaly detection.
Toevaluatetheefficiencyofourmethod,weusetrainingtime • MultimodalTrace[26].Organizesmicroservicesandtheir
and inference time as efficiency evaluation metrics. time consumptions in sequences modeled using LSTM-
• Precision: the proportion of true positive predictions VAE. This method optimizes node anomaly scores
amongallpositivepredictionsmadebythemodel.,which uniquely, aiming for maximization rather than aggrega-
can be calculated as: Precision = TP . tion.
TP+FP
• Recall: the proportion of true positive predictions among • TraceAnomaly [27]. Traces are encoded into vectors,
all actual positive instances, which can be calculated as: where each dimension represents the time consumption
Recall = TP . of a specific “path”. Negative Log Likelihoods (NLLs)
TP+FN
areemployedasanomalyscores,providingaquantitative
6https://github.com/hellolijj/traceDAE.git measure of deviation from expected behavior.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4893
TABLEIV
THEEFFECTSOFTRACEDAEINCOMPARISONWITHBASELINEMETHODSONTWODATASETS
• DeepTraLog[32].Thecomplexcallingstructurebetween
traces and time of service logs is processed by the Deep
SVDDmodelforunifiedanomalydetection.Atthesame
time, it provides a user feedback mechanism to enable
dynamic adjustment of weights over time.
• TraceCRL [34]. It employs a representation learn-
ing approach that combines contrastive learning with
graph neural networks to incorporate graph-structured
information into downstream trace analysis tasks.
Fig.4. TheROCCurveofTraceDAEincomparisonwithbaselinemethods
• TraceVAE [33]. The approach utilizes a novel model
ontwodatasets.
to identify anomalies in traces. It captures the trace
characteristics using a dual-variable graph VAE model
and detects anomalies through NLL. Additionally, it optimal F1-score as presented in Table IV. Using these met-
incorporates techniques aimed at minimizing the entropy rics, we compare the performance of TraceDAE against five
gap. baselineapproachesacrosstwodatasets.Theresultsshowcase
In implementing the Multimodal-Trace method, we employ thesuperiorperformanceofTraceDAEindetectinganomalies
two LSTM networks to process the input data and equally within microservice systems, evidenced by its high precision
distributed the weights of the two loss functions, setting each (0.971),recall(0.935),andF1-score(0.953).Comparedtothe
weightto0.5,toensurethenetworkcouldadequatelylearnthe best-performing baseline method, TraceDAE achieves higher
multifaceted characteristics of traces during training. For the optimal F1-score by 17.9% and 10.7% on the respective
TraceAnomalymethod,wesetthedimensionalityofthelatent datasets, further confirming its effectiveness in the field of
variable z to 10, which aids in capturing the deep structures microservice anomaly detection.
and anomaly patterns within trace data. Considering that the Among the evaluated methods, TraceAnomaly and
original design of DeepTraLog requires processing both log MultimodalTrace exhibit relatively weaker performance in
and trace data, and our current dataset contains only trace terms of F1-score, primarily due to their reliance only
information, we substitute the event vector inputs from the on trace data of microservice systems (Trace data mainly
originalmethodwiththefeaturematrixofTPGtoadapttoour focuses on the service invocation relationships and service
data characteristics and fully leverage DeepTraLog’s potential response time indicators), while ignoring key performance
in trace anomaly detection. For the TraceVAE method, we set monitoring metrics in microservice systems, such as CPU
theparameterK =5torepresentthestructuralvariableZ,and usage and memory usage, which are essential for identifying
K = 10 to represent the time variable Z2. These adjustments abnormalresourceusage.Incontrast,FSAdemonstratesstable
areaimedatensuringallmethodscanoperateintheiroptimal and moderate performance across all datasets but requires
state on the same dataset, thus allowing for a fair comparison extensive parameter adjustments for each target microservice
of their anomaly detection performance. system.TraceCRL,despiteitsslightlyinferiorabilitytodetect
To evaluate the precision of TraceDAE in root cause call structure anomalies, surpassed TraceAnomaly in overall
localization, we compare it with three recently proposed performance. DeepTraLog benefits from its deep SVDD
methods: MEPFL [17], TraceAnomaly [19], MicroRank [36], learning rule feature representation and amine hyperspheres
and TraceRCA [38]. We describe the parameter settings for in preprocessing all datasets, achieving a good performance.
all methods to ensure a fair comparison. For MicroRank, we TraceVAE has achieved good performance because it can
set the damping factor d to 0.85 and maintain the preference effectively detect structural anomalies in Trace, but it cannot
vectorweightϕtodefaultvalue0.5.Similarly,forTraceRCA,
effectively detect a small number of attribute anomalies.
we utilize the recommended default values for parameters In addition, we also use precision-recall curves to compare
δ ad ,δ fs and δ spt which are 1, 0.1 and 0.1, respectively. the anomaly detection capabilities of all methods. The area
under the curve (AUC) demonstrates the ability of different
E. Result
methods to identify anomalies. The larger the AUC value, the
Toevaluatetheperformanceofanomalydetectionmethods, higher the accuracy of this method. As shown in Figure 4,
we compute and compare the average precision, recall, and TraceDAE performs well on all datasets.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

4894 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
TABLEV
THEACCURACYOFROOTCAUSELOCALIZATIONINCOMPARISON
WITHDIFFERENTMETHODS
Besidesanomalydetection,wealsocomparetheaccuracyof
TraceDAEinrootcauselocalizationwiththebaselinemethods
| of two | datasets, | as shown |     | in Table | V. We | observe | that the |     |     |     |     |     |     |     |     |
| ------ | --------- | -------- | --- | -------- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
accuracyofTraceDAEinrootcauselocalizationisbetterthan
| the baseline | method. |     | Notably, | TraceDAE |     | exhibits | exceptional |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | -------- | -------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
performanceinprecisionatthetoprank(A@1),whichreflects Parametersensitivityexperimentresultsaboutα.
Fig.5.
| its robust    | capability |               | to accurately |              | locate       | root cause    | of the   |             |              |      |                 |     |            |     |         |
| ------------- | ---------- | ------------- | ------------- | ------------ | ------------ | ------------- | -------- | ----------- | ------------ | ---- | --------------- | --- | ---------- | --- | ------- |
| primary       | anomalous  | microservice. |               |              |              |               |          |             |              |      |                 |     |            |     |         |
| Additionally, |            | we evaluated  |               | the training |              | and inference | effi-    |             |              |      |                 |     |            |     |         |
|               |            |               |               |              |              |               |          | compared    | to using     | STV. | This experiment |     | emphasizes |     | the key |
| ciency        | of each    | method.       | TraceDAE      |              | demonstrated |               | superior |             |              |      |                 |     |            |     |         |
|               |            |               |               |              |              |               |          | role of STG | in TraceDAE. |      |                 |     |            |     |         |
performance, with detailed timings presented in Table VI. In addition, we evaluated the impact of the noise reducing
| MulitmodaleTrace |     | and | TraceCRL |     | exhibited | relatively | brief |          |          |       |      |          |           |           |     |
| ---------------- | --- | --- | -------- | --- | --------- | ---------- | ----- | -------- | -------- | ----- | ---- | -------- | --------- | --------- | --- |
|                  |     |     |          |     |           |            |       | step. As | shown in | Table | VII, | removing | the noise | reduction |     |
trainingtimesof20msand24.6msforthedatasetA,and7.8ms step (w/o DBSCAN) resulted in lower precision and recall,
and 23.4ms for the dataset B, due to their efficient handling suggestingthatthenoisereductionstepiscriticalforminimiz-
ofsequencedata.TraceAnomaly,whichtransformstracesinto
|     |     |     |     |     |     |     |     | ing false | alarms by | preventing |     | the model | from | learning | from |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | --------- | ---- | -------- | ---- |
Structured Trace Vectors (STVs) for the detection of response anomalous trajectory patterns.
timeandcallpathanomalies,hastrainingtimesof49.2msand
|     |     |     |     |     |     |     |     | Finally, | we explore |     | the impact | of each | autoencoder |     | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---------- | ------- | ----------- | --- | --- |
42.4ms for the respective datasets. Its inference times s are removing the Structure-AE and Attribute-AE modules from
at 19.2ms and 17.4ms, indicating a more resource-intensive TraceDAE,respectively.Table VIIIpresentsthebestF1-scores
| approach. | DeepTraLog, |     | which | processes |     | a significant | amount |             |          |          |     |        |         |            |     |
| --------- | ----------- | --- | ----- | --------- | --- | ------------- | ------ | ----------- | -------- | -------- | --- | ------ | ------- | ---------- | --- |
|           |             |     |       |           |     |               |        | for service | response | abnormal |     | (SRA), | service | invocation |     |
of simulated log information, exhibited the longest training abnormal (SIA), and overall abnormal for two approaches
| times of | 158.5ms | and | 135.1ms, | respectively. |     | Other | methods |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | -------- | ------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
acrosstwodatasets.Experimentalresultsindicateasignificant
such as FSA and TraceVAE also showed varying degrees of decrease in SRA performance upon the removal of Attribute-
efficiency.FSA’strainingtimeisnotavailable,butithadoneof AE, and a notable reduction in SIA performance upon the
| the shortest | inference |     | times | s of 0.9ms | and | 0.7ms. | TraceVAE |         |                  |     |      |               |     |      |      |
| ------------ | --------- | --- | ----- | ---------- | --- | ------ | -------- | ------- | ---------------- | --- | ---- | ------------- | --- | ---- | ---- |
|              |           |     |       |            |     |        |          | removal | of Structure-AE. |     | This | suggests that | the | LSTM | com- |
required43.1ms and30.4ms fortraining,withinference times ponent of Attribute-AE excels at detecting response time
| s of 8.2ms  | and | 7.6ms. | TraceDAE |            | introduced |         | the Service |                 |              |            |     |                      |         |           |         |
| ----------- | --- | ------ | -------- | ---------- | ---------- | ------- | ----------- | --------------- | ------------ | ---------- | --- | -------------------- | ------- | --------- | ------- |
|             |     |        |          |            |            |         |             | and other       | performance  | anomalies, |     | while                | the GAT | component |         |
| Trace Graph |     | (STG)  | method   | to present |            | service | trace. This |                 |              |            |     |                      |         |           |         |
|             |     |        |          |            |            |         |             | of Structure-AE | demonstrates |            |     | a higher sensitivity |         | to        | service |
method significantly reduced the time required, making it the invocation path anomalies. The combined usage of Attribute-
shortesttrainingtimeofallmethods,requiringonly6.1msand
|             |         |          |            |     |               |       |            | AE and        | Attribute-AE | enhances       |     | the overall | anomaly | detection     |     |
| ----------- | ------- | -------- | ---------- | --- | ------------- | ----- | ---------- | ------------- | ------------ | -------------- | --- | ----------- | ------- | ------------- | --- |
| 4.3ms for   | two     | separate | datasets.  | Its | inference     | times | s are also | capability.   |              |                |     |             |         |               |     |
| minimal,    | at just | 0.6ms    | and 0.5ms, |     | respectively. |       |            |               |              |                |     |             |         |               |     |
|             |         |          |            |     |               |       |            | G. Parametric | Analysis     |                |     |             |         |               |     |
| F. Ablation | Study   |          |            |     |               |       |            |               |              |                |     |             |         |               |     |
|             |         |          |            |     |               |       |            | In this       | section,     | we investigate |     | the impact  | of      | the parameter |     |
In this section, we evaluated the impact of various compo- α on the average optimal F1-score of TraceDAE. The results
nentswithinourproposedTraceDAEmodelbysystematically fromtheparametersensitivityexperimentspresentedinFig. 5
α
replacing or disabling specific modules. reveal that when is set to 0 or 1, relying only on Attribute-
Initially, in order to explore the impact brought by AE or Structure-AE results in a decrease in performance,
the STG module, we replace the STG in TraceDAE which highlights the synergistic role of Attribute-AE and
withtheSTV(ServiceTraceVector)inTraceDAE.Theresults Structure-AE in trace-based anomaly detection in microser-
of the experiment are shown in Table VII, where the method vice systems. As α increases from 0.0 to 1.0, we observe
α
using STV shows a decrease in both precision and recall, that the average F1-score of TraceDAE peaks when set
which indicates that STG outperforms STV in extracting to 0.1. Further increasing α affects the selection of the
relevant features from the trace data. Meanwhile, the exper- anomaly score threshold, resulting in a performance degrada-
iment also shows that the execution time of using STV is tion. Consequently, we set α to 0.1.
significantly longer than TraceDAE, which further proves that In the experimental process of anomaly detection, the
γ
theusingofSTGhashigherefficiencyinprocessingtracedata threshold parameter has a significant impact on the
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore.  Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4895
TABLEVI
THETRAININGANDINFERENCETIMEOFTRACEDAEINCOMPARISONWITHBASELINEMETHODSONTWODATASETS
TABLEVII
THEEFFECTSOFTRACEDAEINCOMPARISONWITHDIFFERENTALTERNATIVEMODELONTWODATASETS
TABLEVIII
| THEEFFECTSOFTRACEDAEINCOMPARISONWITHDIFFERENT |     |     |     |     |     |     |     |     |     | VI. CONCLUSION |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
ALTERNATIVEAEONTWODATASETS
|     |     |     |     |     |     |     | In this         | paper,    | we         | propose   | a novel       | approach,        |     | TraceDAE,    |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ---------- | --------- | ------------- | ---------------- | --- | ------------ |
|     |     |     |     |     |     |     | for trace-based |           | anomaly    | detection |               | in microservice  |     | systems.     |
|     |     |     |     |     |     |     | By constructing |           | a service  | trace     | graph         | (STG),           | we  | effectively  |
|     |     |     |     |     |     |     | illustrate      | service   | invocation |           | relationships |                  | and | performance  |
|     |     |     |     |     |     |     | metrics.        | Utilizing | the        | STG,      | we have       | designed         | a   | dual autoen- |
|     |     |     |     |     |     |     | coder framework |           | to         | jointly   | model         | the interactions |     | between      |
differentdatasourcesusingtheattentionmechanismtocapture
|     |     |     |     |     |     |     | complementary |         | information    |           | between  | different          | data | sources.    |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | -------------- | --------- | -------- | ------------------ | ---- | ----------- |
|     |     |     |     |     |     |     | Experimental  | results |                | show that | the      | STG representation |      | makes       |
|     |     |     |     |     |     |     | our approach  |         | more efficient |           | in model | training           |      | and anomaly |
detection,andthedualautoencoderframeworkmakesTraceDAE
|     |     |     |     |     |     |     | effective        | for anomaly |                 | detection    | and     | root cause       | localization. |             |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | --------------- | ------------ | ------- | ---------------- | ------------- | ----------- |
|     |     |     |     |     |     |     | In the           | future,     | we              | will         | explore | the relationship |               | between     |
|     |     |     |     |     |     |     | multimodal       | data        | from            | microservice |         | systems          | to            | efficiently |
|     |     |     |     |     |     |     | detect anomalies |             | in microservice |              | systems |                  | and locate    | the root    |
|     |     |     |     |     |     |     | cause of         | failures.   |                 |              |         |                  |               |             |
ACKNOWLEDGMENT
|     |     |     |     |     |     |     | The authors |     | would | like   | to thank | engineers   |     | such as Kai  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------ | -------- | ----------- | --- | ------------ |
|     |     |     |     |     |     |     | Shi from    | the | Cloud | Native | team     | of AliCloud |     | Inc. for the |
enlighteningdiscussionsandexchangesprovidedtothispaper.
ParametersensitivityexperimentresultsaboutγT They also thank the anonymous reviewers for providing
| Fig.6. |     |     |     |     | .   |     |            |          |        |             |     |              |          |     |
| ------ | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | ----------- | --- | ------------ | -------- | --- |
|        |     |     |     |     |     |     | valuable   | feedback | and    | suggestions |     | that greatly | improved | the |
|        |     |     |     |     |     |     | quality of | this     | paper. |             |     |              |          |     |
performanceofthedetectionresults.Thethresholdγisdefined
REFERENCES
| μ +      | 3σ        |       | μ      | σ           |                  |     |             |     |            |          |     |         |       |                |
| -------- | --------- | ----- | ------ | ----------- | ---------------- | --- | ----------- | --- | ---------- | -------- | --- | ------- | ----- | -------------- |
| as x     | x         | where | x and  | x represent | the average      | and |             |     |            |          |     |         |       |                |
|          |           |       |        |             |                  |     | [1] Z. Liu, | N.  | Japkowicz, | R. Wang, | Y.  | Cai, D. | Tang, | and X. Cai, “A |
| standard | deviation | of    | a time | window γ    | T, respectively. | To  |             |     |            |          |     |         |       |                |
statisticalpatternbasedfeatureextractionmethodonsystemcalltraces
| determine                             | the | optimal | value | of γ, we | designed a series | of  |     |         |             |      |        |           |           |            |
| ------------------------------------- | --- | ------- | ----- | -------- | ----------------- | --- | --- | ------- | ----------- | ---- | ------ | --------- | --------- | ---------- |
|                                       |     |         |       |          |                   |     | for | anomaly | detection,” | Inf. | Softw. | Technol., | vol. 126, | Oct. 2020, |
| parameterexperimentsforthetimewindowγ |     |         |       |          | T.Asshownin       |     |     |         |             |      |        |           |           |            |
Art.no.106348.
|            |              |     |         |               |                   |     | [2] N. Singh | et  | al., “Load | balancing | and | service | discovery | using docker |
| ---------- | ------------ | --- | ------- | ------------- | ----------------- | --- | ------------ | --- | ---------- | --------- | --- | ------- | --------- | ------------ |
| Fig 6, the | experimental |     | results | indicate that | as γ T increases, |     |              |     |            |           |     |         |           |              |
swarmformicroservicebasedbigdataapplications,”J.CloudComput.-
|     |     |     |     |     | γ T | = 30 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
the detection accuracy gradually improves. At Adv.Syst.Appl.,vol.12,no.1,p.4,Jul.2023.
minutes,theF1-scorereacheditshighestvalue.Therefore,this [3] J. Diaz-De-Arcaya, A. I. Torre-Bastida, G. Zarate, R. Minon, and
|                 |            |       |         |        |                   |     | A. Almeida,                         |     | “A joint | study      | of the | challenges, | opportunities, | and         |
| --------------- | ---------- | ----- | ------- | ------ | ----------------- | --- | ----------------------------------- | --- | -------- | ---------- | ------ | ----------- | -------------- | ----------- |
| article selects | γ          | T =30 | minutes | as the | optimal threshold | for |                                     |     |          |            |        |             |                |             |
|                 |            |       |         |        |                   |     | Roadmap                             | of  | MLOps    | and AIOps: | A      | systematic  | survey,”       | ACM Comput. |
| anomaly         | detection. |       |         |        |                   |     | Surv.,vol.56,no.4,pp.1–30,Apr.2024. |     |          |            |        |             |                |             |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore.  Restrictions apply.

4896 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.22,NO.5,OCTOBER2025
[4] P. Jamshidi, C. Pahl, N. C. Mendonca, J. Lewis, and S. Tilkov, [27] P. Liu et al., “Unsupervised detection of microservice trace anomalies
“Microservices:Thejourneysofarandchallengesahead,”IEEESoftw., throughservice-leveldeepBayesiannetworks,”inProc.IEEE31stInt.
vol.35,no.3,pp.24–35,May/Jun.2018. Symp.Softw.Rel.Eng.(ISSRE),2020,pp.48–58.
[5] C. Lee, T. Yang, Z. Chen, Y. Su, and M. R. Lyu, “Eadro: An end- [28] Z. Zhang, M. K. Ramanathan, P. Raj, A. Parwal, T. Sherwood, and
to-end troubleshooting framework for microservices on multi-source M.Chabbi,“{CRISP}:Criticalpathanalysisof{large-scale}microser-
data,” in Proc. IEEE/ACM 45TH Int. Conf. Softw. Eng. (ICSE), 2023, vicearchitectures,”inProc.USENIXAnnu.Tech.Conf.(USENIXATC),
pp.1750–1762. 2022,pp.655–672.
[6] F.Zanettin.“Didisystemglitchlasts12hours,withcompanyapologiz- [29] L.Meng,F.Ji,Y.Sun,andT.Wang,“Detectinganomaliesinmicroser-
ing for service breakdown.” 2023. [Online]. Available: https://english. vices with execution trace comparison,” Future Gener. Comput. Syst.,
visitbeijing.com.cn/article/4FZquTLvAMl vol.116,pp.291–301,Mar.2021.
[7] J. Soldani and A. Brogi, “Anomaly detection and failure root cause [30] T. Wang, W. Zhang, J. Xu, and Z. Gu, “Workflow-aware automatic
analysis in (micro) service-based cloud applications: A survey,” ACM faultdiagnosisformicroservice-basedapplicationswithstatistics,”IEEE
Comput.Surv.,vol.55,no.3,pp.1–39,Apr.2023. Trans.Netw.ServiceManag.,vol.17,no.4,pp.2350–2363,Dec.2020.
[8] G. Yu, P. Chen, Y. Li, H. Chen, X. Li, and Z. Zheng, “Nezha: [31] Y. Xu et al., “TraceLingo: Trace representation and learning for
Interpretable fine-grained root causes analysis for microservices on performanceissuediagnosisincloudservices,”inProc.IEEE/ACMInt.
multi-modal observability data,” in Proc. 31ST ACM Joint Meeting WorkshopCloudIntell.(CloudIntell.),2021,pp.37–40.
Eur. Softw. Eng. Conf. Symp. Found. Softw. Eng. (ESEC/FSE), 2023, [32] C. Zhang et al., “DeepTraLog: Trace-log combined microservice
pp.553–565. anomaly detection through graph-based deep learning,” in Proc.
[9] S. Zhang et al., “Robust failure diagnosis of microservice system ACM/IEEE44thInt.Conf.Softw.Eng.(ICSE),2022,pp.623–634.
throughmultimodaldata,”IEEETrans.ServicesComput.,vol.16,no.6, [33] Z. Xie et al., “Unsupervised anomaly detection on microservice traces
pp.3851–3864,Nov./Dec.2023. throughgraphVAE,”inProc.ACMWebConf.,2023,pp.2874–2884.
[10] K.Zhang,C.Zhang,X.Peng,andC.Sha,“PUTraceAD:Traceanomaly [34] C. Zhang et al., “TraceCRL: Contrastive representation learning for
detectionwithpartiallabelsbasedonGNNandPUlearning,”inProc. microservice trace analysis,” in Proc. 30th ACM Joint Meeting Eur.
IEEE33RDInt.Symp.Softw.Reliab.Eng.(ISSRE),2022,pp.239–250. Softw. Eng. Conf. Symp. Found. Softw. Eng. (ESEC/FSE), 2022,
[11] Z. Xie et al., “From point-wise to group-wise: A fast and accu- pp.1221–1232.
rate microservice trace anomaly detection approach,” in Proc. 31ST [35] D. Liu et al., “MicroHECL: High-efficient root cause localization in
ACM Joint Meeting Eur. Softw. Eng. Conf. Symp. Found. Softw. Eng. large-scale microservice systems,” in Proc. IEEE/ACM 43rd Int. Conf.
(ESEC/FSE),2023,pp.1739–1749. Softw.Eng.Softw.Eng.Pract.(ICSE-SEIP),2021,pp.338–347.
[12] W.Mengetal.,“Loganomaly:Unsuperviseddetectionofsequentialand [36] G. Yu et al., “MicroRank: End-to-end latency issue localization with
quantitative anomalies in unstructured logs,” in Proc. 28th Int. Joint extendedspectrumanalysisinMicroserviceenvironments,”inProc.Web
Conf.Artif.Intell.(IJCAI),2019,pp.4739–4745. Conf.,2021,pp.3087–3098.
[13] X.Li,P.Chen,L.Jing,Z.He,andG.Yu,“SwissLog:Robustandunified [37] J.Lin,P.Chen,andZ.Zheng,“Microscope:Pinpointperformanceissues
deeplearningbasedloganomalydetectionfordiversefaults,”inProc. with causal graphs in micro-service environments,” in Proc. 16th Int.
IEEE31stInt.Symp.Softw.Rel.Eng.(ISSRE),2020,pp.92–103. Conf.Service-OrientedComput.(ICSOC),2018,pp.3–20.
[14] C. Zhang, X. Wang, H. Zhang, H. Zhang, and P. Han, “Log sequence [38] Z.Lietal.,“Practicalrootcauselocalizationformicroservicesystems
anomaly detection based on local information extraction and globally via trace analysis,” in Proc. IEEE/ACM 29th Int. Symp. Qual. Service
sparsetransformermodel,”IEEETrans.Netw.ServiceManage.,vol.18, (IWQOS),2021,pp.1–10.
no.4,pp.4119–4133,Dec.2021. [39] M.Ester,H.-P.Kriegel,J.Sander,andX.Xu,“Adensity-basedalgorithm
[15] J. Chen et al., “TraceGra: A trace-based anomaly detection for fordiscoveringclustersinlargespatialdatabaseswithnoise,”inProc.
microservice using graph deep learning,” Comput. Commun., vol. 204, Nat.Conf.Aritif.Intell.,1999,pp.226–231.
pp.109–117,Apr.2023. [40] B.Perozzi,R.Al-Rfou,andS.Skiena,“DeepWalk:Onlinelearningof
[16] P.Las-Casas,J.Mace,D.Guedes,andR.Fonseca,“Weightedsampling socialrepresentations,”inProc.20thACMSIGKDDInt.Conf.Knowl.
ofexecutiontraces:Capturingmoreneedlesandlesshay,”inProc.ACM Discov.DataMin.,2014,pp.701–710.[Online].Available:https://doi.
SoCC,2018,pp.326–332. org/10.1145/2623330.2623732
[17] X. Zhou et al., “Latent error prediction and fault localization for [41] M. M. Ghorbani, F. F. Moghaddam, M. Zhang, M. Pourzandi,
microserviceapplicationsbylearningfromsystemtracelogs,”inProc. K.K.Nguyen,andM.Cheriet,“Malchain:Virtualapplicationbehaviour
27thACMESEC/FSE,2019,pp.683–694. profiling by aggregated microservice data exchange graph,” in Proc.
[18] H. Fan, F. Zhang, and Z. Li, “Anomalydae: Dual autoencoder for IEEE Int. Conf. Cloud Comput. Technol. Sci. (CloudCom), 2020,
anomaly detection on attributed networks,” in Proc. IEEE Int. Conf. pp.41–48.
Acoust.,Speech,SignalProcess.,2020,pp.5685–5689.
[19] X.Zhouetal.,“Faultanalysisanddebuggingofmicroservicesystems:
Industrialsurvey,benchmarksystem,andempiricalstudy,”IEEETrans.
Softw.Eng.,vol.47,no.2,pp.243–260,Feb.2021.
Junjun Li received the B.S. degree in network
[20] S.Zhangetal.,“Efficientandrobusttraceanomalydetectionforlarge-
engineering from the School of information
scalemicroservicesystems,”inProc.IEEE34thInt.Symp.Softw.Reliab.
and electronic engineering, Zhejiang Gongshang
Eng.(ISSRE),2023,pp.69–79.
University, Hangzhou, China, in 2018, and the
[21] J. Huang, Y. Yang, H. Yu, J. Li, and X. Zheng, “Twin graph-based
master’s degree in software engineering from the
anomaly detection via attentive multi-modal learning for microservice
SchoolofSoftwareTechnology,ZhejiangUniversity,
system,”inProc.38thIEEE/ACMInt.Conf.Autom.Softw.Eng.(ASE),
Hangzhou, in 2020. He is currently pursuing the
2023,pp.66–78.
Ph.D.degreewiththeSchoolofComputerScience,
[22] Z.Heetal.,“Aspatiotemporaldeeplearningapproachforunsupervised
Wuhan University. His research interests include
anomalydetectionincloudsystems,”IEEETrans.NeuralNetw.Learn.
anomaly detection and root cause localization in
Syst.,vol.34,no.4,pp.1705–1719,Apr.2023.
microservicesystems.
[23] C.Zhang,T.Zhou,Q.Wen,andL.Sun,“TFAD:Adecompositiontime
seriesanomalydetectionarchitecturewithtime-frequencyanalysis,”in
Proc. 31ST ACM Int. Conf. Inf. Knowl. Manage. (CIKM), 2022,
pp.2497–2507.
[24] L. Yang, J. Li, K. Shi, S. Yang, Q. Yang, and J. Sun, “MicroMILTS: Shi Ying is currently a Professor with the School
Fault location for microservices based mutual information and LSTM ofComputerScience,WuhanUniversity,China.His
autoencoder,” in Proc. 23rd Asia-Pac. Netw. Oper. Manag. Symp. mainresearchinterestsincludesoftwareengineering,
(APNOMS),2022,pp.73–78. intelligent operation and maintenance management,
[25] Q. Fu, J. G. Lou, Y. Wang, and J. Li, “Execution anomaly detection cloud computing and cloud service software, and
in distributed systems through unstructured log analysis,” in Proc. 9th artificialintelligence.
IEEEInt.Conf.DataMin.,2009,pp.149–158.
[26] S.Nedelkoski,J.Cardoso,andO.Kao,“Anomalydetectionfromsystem
tracing data using multimodal deep learning,” in Proc. IEEE 12th Int.
Conf.CloudComput.(CLOUD),2019,pp.179–186.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.

LIetal.:TraceDAE:TRACE-BASEDANOMALYDETECTIONINMICROSERVICESYSTEMS 4897
TiangangLiiscurrentlypursuingthePh.D.degree XiangboTianiscurrentlypursuingthePh.D.degree
with the School of Computer, Wuhan University, with the School of Computer, Wuhan University,
China.Hisresearchinterestsincludecloudcomput- China. His research interests include cloud com-
ing,softwareengineering,andresourcemanagement puting, software engineering, causal learning, and
andreinforcementlearning. representationlearning.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:36 UTC from IEEE Xplore. Restrictions apply.