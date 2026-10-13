ClusterComputing(2025)28:786
https://doi.org/10.1007/s10586-025-05437-3
(0123456789().,-volV)(0123456789,-().volV)
Performance prediction and resource adaptive adjustment for cloud-
| native  | microservices |         |     |     |     |     |     |     |
| ------- | ------------- | ------- | --- | --- | --- | --- | --- | --- |
| Peng1,2 | Hao1,2        | Chen1,2 |     |     |     |     |     |     |
| Yu      | • Jia         | • Yang  |     |     |     |     |     |     |
Received:26December2024/Revised:27April2025/Accepted:2May2025/Publishedonline:15September2025
(cid:2)TheAuthor(s),underexclusivelicencetoSpringerScience+BusinessMedia,LLC,partofSpringerNature2025
Abstract
Cloud-native architectures, characterized by loosely coupled microservices, enable the modular execution of specific
business functions, significantly accelerating software development and reducing update complexity. However, the exe-
cution of a single application often involves hundreds of interdependent microservice nodes, where complex invocation
topologiesanddynamicresourcedemandsmakeefficientresourceallocationacriticalchallenge.Toaddressthisissue,we
propose Convolutional Neural Network-based Prediction and Resource Adaptation Model (CPRAM), a novel framework
thatintegratesdeeplearningandreinforcementlearningtooptimizeresourceallocationincloud-nativeenvironments.The
key innovations of CPRAM are as follows: (1) We propose A CNN-based performance prediction model by analyzing
resource usage and response times, even with sparse or incomplete data. (2) We allocate CPU and memory via a Deep
Deterministic Policy Gradient (DDPG) based mechanism so as to maximize global resource utilization. We evaluate
CPRAMusingDeathStarBench,awidelyadopted cloud-nativemicroservices benchmark, anddeploy ourexperimentson
DockerSwarm.ExtensiveexperimentalresultsdemonstratethatCPRAMoutperformsstate-of-the-artbaselines,achieving
significantresourcesavingsofatleast22.8%inCPUand21.91%inmemoryutilizationwhileconsistentlymeetingend-to-
end QoS targets.
Keywords Cloud native (cid:2) Microservices (cid:2) Performance prediction(cid:2) Resource allocation (cid:2) Convolutional Neural Network(cid:2)
| Deep Deterministic | Policy | Gradient |     |     |     |     |     |     |
| ------------------ | ------ | -------- | --- | --- | --- | --- | --- | --- |
1 Introduction
|     |     |     | accelerating | the software     | development |                  | lifecycle | [2].   |
| --- | --- | --- | ------------ | ---------------- | ----------- | ---------------- | --------- | ------ |
|     |     |     | However,     | the fine-grained | nature      | of microservices |           | intro- |
Cloud-native architecture has emerged as a cutting-edge duces new challenges in ensuring end-to-end quality of
paradigm for developing highly automated, scalable, and service (QoS). A single user request, such as an e-com-
resilient applications. Unlike traditional monolithic cloud merce transaction or a streaming media service, often
systems, cloud-native architectures decompose complex involves hundreds of interdependent microservices, mak-
applications into modular, loosely coupled microservices ing it difficult to monitor and optimize the performance of
that communicate through lightweight protocols such as critical-path microservices in real time [3, 4].
message queues or remote invocations [1]. This architec- Existing research has made significant strides in
tural shift enables developers to deploy and update indi- addressing resource management challenges in cloud-na-
vidual functional modules independently, significantly tive environments. For instance, Bhardwaj et al. [5] pro-
|     |     |     | posed Cilantro, | a performance-aware |        | resource |                | allocation |
| --- | --- | --- | --------------- | ------------------- | ------ | -------- | -------------- | ---------- |
|     |     |     | framework       | that employs        | online | learning | to dynamically |            |
& JiaHao
|     |     |     | adjust resources | based | on real-time | performance |     | feedback. |
| --- | --- | --- | ---------------- | ----- | ------------ | ----------- | --- | --------- |
haojiaynu@qq.com
|     |     |     | Similarly, | Qiu et al. | [6] introduced |     | FIRM, a | machine |
| --- | --- | --- | ---------- | ---------- | -------------- | --- | ------- | ------- |
1 KeyLaboratoryofEducationInformatizationfor learning-based framework that predicts microservice per-
Nationalities,MinistryofEducation,YunnanNormal
|     |     |     | formance | and adapts | resources | to prevent | service-level |     |
| --- | --- | --- | -------- | ---------- | --------- | ---------- | ------------- | --- |
University,Kunming650500,China
|     |     |     | objective | (SLO) violations. | Guo | et  | al. [7] | developed |
| --- | --- | --- | --------- | ----------------- | --- | --- | ------- | --------- |
2 YunnanKeyLaboratoryofSmartEducation,YunnanNormal PARA,whichoptimizesresourceallocationbyconsidering
University,Kunming650500,China
123

| 786 Page2of19 |     |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:786 |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
dynamic resource demands and employs heuristic algo- management frameworks. While current solutions have
rithms to maximize long-term performance. Despite these made progress, they often fail to address the challenges
advancements, several limitations remain unresolved. posed by sparse data and global microservice interdepen-
First, existing approaches often require extensive man- dencies. CPRAM aims to bridge this gap by providing a
ual preprocessing of resource-related features before they robust, automated solution for performance prediction and
can be fed into machine learning models, increasing the resource allocation.
computational and memory overhead [8]. This is particu- Paper Organization: The remainder of this paper is
larly problematic for sparse features, such as CPU idle organized as follows. Section 2 reviews related work in
times, which are frequently zero in profiling data but resource management for cloud-native microservices.
require significant preprocessing effort. Second, most Section 3 presents the design and implementation of
resource management frameworks focus on individual CPRAM, including the CNN-based prediction model and
microservices, neglecting the global invocation relation- theDDPG-basedresourceallocationmechanism.Section 4
ships among interdependent microservices. This oversight describes the experimental setup and evaluates the perfor-
can lead to suboptimal resource allocation and degraded mance of CPRAM. Finally, Sect. 5 concludes the paper
end-to-end QoS [9]. and discusses future research directions.
| To address | these | challenges, |     | we propose | Convolutional |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | ----------- | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
NeuralNetwork-basedPredictionandResourceAdaptation
Model (CPRAM), a novel resource management frame- 2 Related work
| work that | leverages |     | deep learning |     | and reinforcement |     |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
learning to optimize resource allocation in cloud-native 2.1 The prediction of cloud-native microservice
| environments. | CPRAM |     | uses the | end-to-end | response | time |     |     |     |     |     |     |     |     |
| ------------- | ----- | --- | -------- | ---------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
as the primary QoS indicator and employs a two-stage Signiant efforts have been dedicated to the performance
approach: (1) a Convolutional Neural Network (CNN)- prediction of microservices to ensure the effectiveness of
based performance prediction model that accurately fore- follow-up resource allocation.
casts microservice performance even with sparse or For example, Rzadca et al. [12] proposed Autopilot, a
incomplete data, and (2) a Deep Deterministic Policy vertical andhorizontal algorithmscaler utilizedby Google
Gradient (DDPG)-based resource allocation mechanism for predicting resources. It leverages the optimized sliding
that dynamically adjusts CPU, memory, and I/O resources window algorithm and a reinforcement learning-based
to meet QoS requirements while maximizing global method to enhance system utilization. Guo et al. [7] pro-
resource utilization [10]. posed the PARA strategy, which took the service degrad-
The key contributions of this paper are as follows: ability, dynamic resource demand, the characteristics of
|            |            |          |                 |         |                 |          | MEC and    | cloud              | resource    | supply       | into      | consideration. |          | They   |
| ---------- | ---------- | -------- | --------------- | ------- | --------------- | -------- | ---------- | ------------------ | ----------- | ------------ | --------- | -------------- | -------- | ------ |
| • CPRAM    | Framework: |          | We              | propose | a novel         | resource |            |                    |             |              |           |                |          |        |
|            |            |          |                 |         |                 |          | analyzed   | the historical     |             | resource     | demand,   | and            | then     | estab- |
| management |            | model    | that integrates |         | CNN-based       | perfor-  |            |                    |             |              |           |                |          |        |
|            |            |          |                 |         |                 |          | lished an  | enhanced-heuristic |             |              | algorithm | based          | resource |        |
| mance      | prediction |          | with DDPG-based |         | resource        | alloca-  |            |                    |             |              |           |                |          |        |
|            |            |          |                 |         |                 |          | allocation | model              | aiming      | to maximize  |           | long-term      | perfor-  |        |
| tion,      | enabling   | accurate | performance     |         | forecasting     | and      |            |                    |             |              |           |                |          |        |
|            |            |          |                 |         |                 |          | mance.     | Zhang              | et al. [13] | proposed     | Sinan,    | a              | scalable | and    |
| dynamic    | resource   |          | adaptation      |         | in cloud-native |          |            |                    |             |              |           |                |          |        |
|            |            |          |                 |         |                 |          | QoS-aware  | interactive        |             | microservice |           | resource       | manager. |        |
environments.
|          |               |     |                |          |            |           | They first | used   | a set        | of scalable | and         | verified | machine   |     |
| -------- | ------------- | --- | -------------- | -------- | ---------- | --------- | ---------- | ------ | ------------ | ----------- | ----------- | -------- | --------- | --- |
| • Global | Optimization: |     | Unlike         | existing | approaches | that      |            |        |              |             |             |          |           |     |
|          |               |     |                |          |            |           | learning   | models | to determine |             | the impacts | from     | dependen- |     |
| focus    | on individual |     | microservices, |          | CPRAM      | considers |            |        |              |             |             |          |           |     |
ciesamongmicroservicesonperformance,andthenpredict
| the global | invocation |         | relationships |     | among      | microser-  |           |       |             |         |          |             |        |       |
| ---------- | ---------- | ------- | ------------- | --- | ---------- | ---------- | --------- | ----- | ----------- | ------- | -------- | ----------- | ------ | ----- |
|            |            |         |               |     |            |            | the QoS   | under | the current |         | resource | allocation. |        | Then, |
| vices,     | ensuring   | optimal | resource      |     | allocation | across the |           |       |             |         |          |             |        |       |
|            |            |         |               |     |            |            | resources | were  | allocated   | to each | layer    | in a        | manner | that  |
entire system.
|     |     |     |     |     |     |     | preserved | the end-to-end |     | application |     | delay. | Daniel | et al. |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ----------- | --- | ------ | ------ | ------ |
ExperimentalValidation:WeevaluateCPRAMusing
•
|                |              |            |                  |         |                 |            | [14] introduced |                  | the Clipper  | system,    | which     | implemented |               | a    |
| -------------- | ------------ | ---------- | ---------------- | ------- | --------------- | ---------- | --------------- | ---------------- | ------------ | ---------- | --------- | ----------- | ------------- | ---- |
| DeathStarBench |              | [11],      | a widely         | adopted | cloud-native    |            |                 |                  |              |            |           |             |               |      |
|                |              |            |                  |         |                 |            | dual-layer      | architecture     |              | consisting | of        | a model     | abstraction   |      |
| microservices  |              | benchmark, | and              | deploy  | our experiments |            |                 |                  |              |            |           |             |               |      |
|                |              |            |                  |         |                 |            | layer and       | a model          | selection    | layer,     | enabling  |             | unified       | man- |
| on Docker      |              | Swarm.     | Extensive        |         | experimental    | results    |                 |                  |              |            |           |             |               |      |
|                |              |            |                  |         |                 |            | agement         | and optimization |              | of         | multiple  | machine     | learning      |      |
| demonstrate    |              | the        | effectiveness    |         | and efficiency  | of         |                 |                  |              |            |           |             |               |      |
|                |              |            |                  |         |                 |            | models          | to support       | online       | model      | selection |             | and real-time |      |
| CPRAM          | in           | meeting    | QoS requirements |         | and             | optimizing |                 |                  |              |            |           |             |               |      |
|                |              |            |                  |         |                 |            | performance     | prediction.      |              | Christina  | et        | al. [15]    | proposed      | a    |
| resource       | utilization. |            |                  |         |                 |            |                 |                  |              |            |           |             |               |      |
|                |              |            |                  |         |                 |            | nature-inspired |                  | microservice |            | resource  | management  |               | and  |
ResearchMotivation:Themotivationbehindthiswork dynamic scheduling framework in cloud centers. In this
stems from the growing complexity of cloud-native appli- study, a predictive scheduling strategy for containerized
cations and the limitations of existing resource microservices was developed using the multiverse
123

ClusterComputing(2025)28:786 Page3of19 786
optimization algorithm, which effectively reduced the For example, Zhang et al. [20] proposed a lightweight
average response time and improved the efficiency of resource management system, Ursa, which used an ana-
resourceutilizationofthewholesystem.Rolandetal.[16] lytical model to decompose the end-to-end service level
used regression model to estimate resource usage and agreement (SLA) into each microservices, and then map-
performance of data-intensive applications based on pedtheseSLAstotheseparateresourceallocationsofeach
microservices, and then minimized CPU and memory microservice layer, so as to halt the corresponding execu-
reservation under QoS constraints with the formed linear tion when latency exceeded the layer-wise SLA promptly.
programming. Michel et al. [17] proposed a discrete event Wang et al. [21] introduced the Autothrottle framework,
simulatorforsimulatingandpredictingtheperformanceof which optimized microservice resource allocation for ser-
cloud-native microservice chains. Jeong et al. [18] pro- vicelevelobjectives(SLO)throughatwo-tiermanagement
posed the HiPerRM system, which utilized the SCINet structure. They utilized application-level learning con-
model to predict future workload and optimized container trollers to set performance targets, and then employed
resource management with reverse case normalization service-level heuristic controllers to adjust CPU allocation
technology. Sotirios et al. [19]proposed the Rusty system, dynamically. Luo et al. [22] proposed the Erms system,
which utilized the LSTM to predict resource and energy which utilizedthe piecewise linear featureof microservice
consumption with fine-grained performance counters, and delay, combined with global optimization and priority
demonstrated high prediction accuracy under various scheduling policies, and then optimized resource sharing
interference scenarios, enabling the management of run- and scheduling among microservices to reduce the proba-
time interference in multi-tenant systems. bility of SLA violation, so as to improve resource utiliza-
Current methods for microservice performance predic- tion and performance significantly. Chen et al. [23]
tion often rely on traditional machine learning techniques proposed a cloud running system, PARTIES. Through
or manual feature engineering, which suffer from several online monitoring and a resource partitioning mechanism,
limitations. Firstly, these approaches typically require PARTIES adjusted resource allocation to meet the QoS
extensive preprocessing of resource usage data, such as requirementsofco-scheduledworkloadsandmaximizethe
handling sparse features (e.g., CPU idle times that are throughput of servers dynamically. Guo et al. [24] pro-
frequently zero) or normalizing data, which increases posed the POBO framework, which combined pessimistic
computational overhead and complexity. Secondly, they and optimistic Bayesian optimization. They demonstrated
often fail to capture the intricate relationships and depen- the efficiency and accuracy of real microservice applica-
dencies among microservices, as they treat each node in tions through primal duality and penalty-based optimiza-
isolation rather than considering the global invocation tionmethods,whileensuringthemaximizationofSLAand
topology. In contrast, Convolutional Neural Networks resource efficiency. Ahyoung et al. [25] utilized genetic
(CNNs) offer significant advantages for microservice per- algorithms to simulate different resource allocation
formance prediction. CNNs can automatically extract schemes, and then optimized the resource adjustment for
meaningful patterns from raw data, eliminating the need container deployment in heterogeneous cloud environ-
for manual feature engineering. Their ability to process ments. Ataollah et al. [26] proposed SHOWAR, which
spatial and structural information, such as the invocation optimizedresource allocationandmicroservicescheduling
relationships among microservices, enables them to model through real-time monitoring of resource usage and per-
complex dependencies more effectively. Additionally, formance indicators. It combined vertical and horizontal
CNNsarerobusttosparseorincompletedata,makingthem algorithm scaling technology, leading to significant
well-suited for the dynamic and heterogeneous nature of improvements in resource utilization and system perfor-
cloud-nativeenvironments.ThesecapabilitiesallowCNNs mance. Piotr et al. [27] used machine learning methods to
to deliver more accurate and reliable performance predic- deal with the problem of overestimating resource utiliza-
tions,eveninscenarioswheretraditionalmethodsstruggle. tion of services using cloud computing, and gained great
practicabilitywhenplanningcloudresourcereservationfor
2.2 The resource adjustment for cloud-native network services. Reena et al. [28] combined the concepts
microservice of autonomic computing, linear regression and Bayesian
learningtoproposeaframeworkforprovidingresourcesin
The resource adjustment for the microservice node mainly anoptimalway,usingexistingpriorinformationtopredict
involves in monitoring, analyzing, and then adjusting resources. Antha et al. [29] proposed an adaptive
resourcessuchasCPU,memory,andI/Onetworkbasedon scheduling algorithm based on dynamic pricing of combi-
the real-time resource requirements, so as to optimize the natorialauctionallocationmechanism toimproveresource
task performance, reduce the cost of cloud servers, and utilizationandusersatisfactionthroughdynamicpricingof
then maintain the high availability and reliability. combinatorial auction.
123

786 Page4of19 ClusterComputing(2025)28:786
Current methods for microservice resource allocation this way, we can track the resource usage of every
often rely on heuristic rules or static optimization tech- microservice nodes in the non-interference state, and
niques, which exhibit several critical limitations. Firstly, whose performance (i.e., response time) is then collected
these approaches typically lack adaptability to dynamic by the distributed tracking system Jaeger.
resource demands, as they are designed based on fixed Next, the benchmark of Phoronix-Test-Suite is used to
thresholds or historical data, making them ineffective in simulate the interference from the perspective of CPU,
handling the highly variable workloads of cloud-native memory, I/O, and we use the above-mentioned method to
environments. Secondly, they often focus on optimizing collect the resource-performance data correspondingly.
individual microservices in isolation,neglecting the global Finally, the feature engineering method is adopted to
interdependencies and invocation relationships among conduct data pre-processing, so as to complete the per-
microservices, which can lead to suboptimal resource uti- formance tracking of microservice nodes under the cloud-
lizationanddegradedend-to-endperformance. Incontrast, native environment.
theDeepDeterministicPolicyGradient(DDPG)algorithm (2) The construction and prediction via CNN. The col-
offers significant advantages for microservice resource lected resource-performance tabular data is converted into
allocation.Asamodel-freereinforcementlearningmethod, grayscale images, which are the input of a CNN, and the
DDPG can dynamically adapt to changing workloads and keyresource-relatedfeaturesthencanbeextractedthrough
resource requirements in real time, ensuring optimal theoperationsofconvolutionandpooling,thuscompleting
resource allocation under varying conditions. Moreover, thetraining.BasedonCNN,wepredicttheperformanceof
DDPG is capable of learning global optimization policies microservice when given the resources.
by considering the interactions and dependencies among (3) DDPG-based resource allocation. According to the
microservices, enabling it to maximize system-wide prediction of CNNRPM, after obtaining the call depen-
resource efficiency while meeting quality of service (QoS) dencies among microservices, each of them is regarded as
targets. Its ability to handle continuous action spaces also an agent. Then, we adopt the Actor-Critic algorithm with
makes it particularly suitable for fine-grained resource the attention mechanism to train the DDPG in a decen-
adjustments,suchasallocatingCPUcores,memory,orI/O tralized way, and learn the best resource allocation strate-
bandwidth. These capabilities position DDPG as a power- giesunderdifferentworkloadstoensuretheQoSofend-to-
ful solution for addressing the complexities of resource end tasks at the same time.
management in cloud-native systems [33–36].
3.2 Data-preparation: track of cloud-native
microservices
3 The construction of CPRAM
Firstly,weneedtopreparethemodeltrainingdatafromall
In this chapter, we give the details of CPRAM-based of the microservice nodes, including the usage of CPU,
microserviceperformancepredictionandresourceadaptive memoryandotherresourcesunderthecriticalpath,aswell
adjustment in a cloud-native environment. We first intro- asthecorrespondingresponsetime.Then,inordertomake
ducetheoverallarchitectureofCPRAM,andthengivethe the trained CPRAM model more universal, we injected
data preparation process. Then, the CNNRPM-based artificial interference into each microservice node to sim-
resource prediction and DDPG-based resource allocation ulate the resource competition among different resources.
will be introduced respectively. The dataset is collected from the container engine
Docker and the benchmark DeathStarBench, which is an
3.1 The brief introduction of CPRAM open-source toolset for cloud-native environment that
builds six interactive and delay-sensitive services (such as
CPRAM, whose overall architecture is given in Fig. 1, social networking, video streaming, e-commerce, and
comprises three components, namely (1) the tracking of cluster control services) based on microservice architec-
cloud-nativemicroservices, (2)performancepredictionvia tures, and covers the current popular cloud and edge
CNN, and (3) DDPG-based resource allocation. applications. The data is collected in the following way.
(1) Track of cloud-native microservices. We deploy the First, we installed Docker on two physical hosts, and then
DeathStarBench test suite via Docker, a container man- deploy DeathStarBench, then the Linux profiling tool vm-
agement tool. Then, we use the Linux resource tracking stat1 is used to collect the resource usage of microservices
command vmstat to collect the resource usage of from each application at a given interval, including the
microservices at a given time interval. At the same time,
the Linux resource isolation mechanism Cgroup is used to 1 Vmstat: https://www.man7.org/linux/man-pages/man8/vmstat.8.
implement resource restrictions on each microservice. In html,2024/5/7.
123

| ClusterComputing(2025)28:786 |     |     |     |     |     |     |     |     |     |     |     | Page5of19 |     | 786 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
Fig.1 Modelarchitecture
Table1 Resourcecharacteristicsandperformancecollection
Resource-relatedfeatures
| Collectbyvmstat |     |     | Description |     |     |     | InitializedbyCgroups |     |     |     | Description |     |     |     |
| --------------- | --- | --- | ----------- | --- | --- | --- | -------------------- | --- | --- | --- | ----------- | --- | --- | --- |
Process procs.r/b Numberofrunningandwaitingprocesses CPU cpu.shares CPUallocationfor
| level |     |     |     |     |     |     |     |     |     |     | microservices |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
cpu.cfs_period_us
cpuset.cpus
CPUlevel cpu.us/sy/id/ CPUpercentageforuser,system,idleand Memory memory.limit_in_bytes Memoryallocationfor
|        |              | wa/st | I/Owait                           |     |     |     |     | memory.swappiness |     |     | microservices |     |     |     |
| ------ | ------------ | ----- | --------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | ------------- | --- | --- | --- |
| Memory | memory.swpd/ |       | Allocatedandswappedmemorycapacity |     |     |     |     |                   |     |     |               |     |     |     |
| level  |              | free  |                                   |     |     |     |     |                   |     |     |               |     |     |     |
memory.cache/
buff
swap.si/so
| I/Oblock | bi/bo |     | Readandwrittendatafromblockdevice |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
level
| System | system.in/cs |     | Numberofinterruptsandcontextswitchespersecond |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
level
CPU and memory usage, and I/O read/write rate. Next, injectedprogramisimplementedthroughthebenchmarkof
| Cgroups,2 |     |     |     |     |     |     | Phoronix-Test-Suite,4 |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
the physical resource isolation mechanism pro- whose details are given as follows:
| vided by | the Linux |     | kernel, is | used to | adjust | the resource |                 |     |               |     |     |          |              |     |
| -------- | --------- | --- | ---------- | ------- | ------ | ------------ | --------------- | --- | ------------- | --- | --- | -------- | ------------ | --- |
|          |           |     |            |         |        |              | • CPU-intensive |     | Interference. |     | We  | simulate | the competi- |     |
allocationofeachnode,andJaeger,3adistributedtracking
|     |     |     |     |     |     |     | tion | of CPU | by using | smallpt | from | the Phoronix-Test- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | -------- | ------- | ---- | ------------------ | --- | --- |
system,isusedtocollecttheresponsetimeofmicroservice
Suite.Thesmallptsimulatestheraytracingbyemitting
| nodes and | the   | call     | topology       | diagram | between             | microser- |             |     |         |          |               |        |              |     |
| --------- | ----- | -------- | -------------- | ------- | ------------------- | --------- | ----------- | --- | ------- | -------- | ------------- | ------ | ------------ | --- |
|           |       |          |                |         |                     |           | light       | and | tracing | its path | continuously, |        | as well      | as  |
| vices, so | as to | complete | the collection |         | of resource-perfor- |           |             |     |         |          |               |        |              |     |
|           |       |          |                |         |                     |           | interacting |     | with    | objects  | in the        | scene. | This process |     |
mancedataunderthenon-interferencestate.Thedetailsof
|               |           |           |          |                 |     |         | requires | a       | large | amount  | of computing | resources, |     | so it |
| ------------- | --------- | --------- | -------- | --------------- | --- | ------- | -------- | ------- | ----- | ------- | ------------ | ---------- | --- | ----- |
| data features | are       | shown     | in Table | 1.              |     |         |          |         |       |         |              |            |     |       |
|               |           |           |          |                 |     |         | can      | be used | to    | achieve | the          | preemption | of  | CPU   |
| Then,         | we inject | different | types    | of interference |     | on each |          |         |       |         |              |            |     |       |
resources.
| node to   | simulate | the                                                 | actual | competitive | scenarios. | This |                     |     |               |     |           |          |               |     |
| --------- | -------- | --------------------------------------------------- | ------ | ----------- | ---------- | ---- | ------------------- | --- | ------------- | --- | --------- | -------- | ------------- | --- |
|           |          |                                                     |        |             |            |      | • I/O-intensive     |     | Interference. |     | We use    | Tiobench | from          | the |
|           |          |                                                     |        |             |            |      | Phoronix-Test-Suite |     |               | to  | implement | I/O      | interference. |     |
| 2 Cgroup: |          | https://www.kernel.org/doc/html/latest/admin-guide/ |        |             |            |      |                     |     |               |     |           |          |               |     |
cgroup-v2.html,2024/5/7. 4 Phoronix-Test-Suite: https://www.phoronix-test-suite.com/,2024/5/
| 3 Jaeger:https://www.jaegertracing.io/,2024/5/7. |     |     |     |     |     |     | 7.  |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
123

| 786 Page6of19 |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:786 |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
Fig.2 Thetopologiesofsocialnetworkandmediaservice
Tiobenchcansimulateaseriesoffilesystemoperations, for the longest path from that particular child. It iterates
including read, write, and random access of the I/O throughallthechildnodesofthecurrentnode,andifeach
disks. child appears prior to the last returned child, the recursive
• Memory-intensive Interference. We write a script in search for the longest path continues from that child, ulti-
Linux system to achieve the preemption of memory mately returning the constructed longest path. By scruti-
| resources. |     | Firstly, | we create | a   | temporary | directory, |            |             |     |       |       |     |              |
| ---------- | --- | -------- | --------- | --- | --------- | ---------- | ---------- | ----------- | --- | ----- | ----- | --- | ------------ |
|            |     |          |           |     |           |            | nizing the | performance | of  | nodes | along | the | microservice |
which is mounted as a temporary memory-based file critical path (CP), we can identify the nodes causing end-
| system | tmpfs. | Then, | we specify |     | the size | of tmpfs, and |                   |     |                 |     |        |       |          |
| ------ | ------ | ----- | ---------- | --- | -------- | ------------- | ----------------- | --- | --------------- | --- | ------ | ----- | -------- |
|        |        |       |            |     |          |               | to-end violations |     | and accordingly |     | adjust | their | resource |
thenwritedatatotheblockfileunderthedirectory,thus allocation to guarantee end-to-end QoS.
| consuming |           | the system | memory   | resources. |           |           |                 |     |             |     |                  |     |     |
| --------- | --------- | ---------- | -------- | ---------- | --------- | --------- | --------------- | --- | ----------- | --- | ---------------- | --- | --- |
|           |           |            |          |            |           |           | 3.3 Performance |     | prediction: |     | the construction |     |     |
| Next,     | we delete | the        | outliers | and the    | duplicate | data, and |                 |     |             |     |                  |     |     |
|           |           |            |          |            |           |           | of CNN-based    |     | model       |     |                  |     |     |
thensmooththenoisefromthecollecteddatasetandfillin
| the missing | values, | so  | as to complete |     | the data | preparation. |     |     |     |     |     |     |     |
| ----------- | ------- | --- | -------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Wefirstgivethedefinitionsofthesymbolsinvolvedinthis
| For example, |     | the call | topologies |     | of social | network and |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ---------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
paper.
| mediaservicefromDeathStarBenchareillustratedinFig. |     |     |     |     |     | 2   |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Then, we the details for microservice tracking. Let V ¼fV 1 ;V 2 ;:::;V N g denote the set of N features
IntheexecutionhistorygraphG,thecriticalpath(CP)is collected by vmstat, where V ði21,2;:::;NÞ denotes the
i
defined as the path with the longest duration from the ith feature, including the number of running processes,
beginningtotheendoftheuserrequest,andthechangeof memory usage, and CPU usage, etc., and V is the jth
ij
theend-to-enddelayofanapplicationisusuallycausedby value of the ith feature ði21,2;:::;NÞ.
insufficient or excessive resources of one or more Let C ¼fC ;C ;:::;C g denote the set of cgroup
|     |     |     |     |     |     |     |     | 1   | 2   | M   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
microservicesonitsCP.Therefore,weneedtofirstidentify allocated features, where C ij is the jth value of the
the CP in the execution history graph. Then, resource ithði21,2;::::;M) feature.
predictioniscarriedoutonthemicroservicesonit,soasto Let T be each microservice node performance metric
accurately find out the microservices with resource allo- collected by jaeger, i.e., the response time of a
cation problems and make corresponding resource adjust- microservicenode.T i ði21,2;:::;tÞistheithvalueofT.
| ment. Algorithm   |           | 1 is            | a CP extraction |               | algorithm.  |              |           |                 |          |                          |                  |              |             |
| ----------------- | --------- | --------------- | --------------- | ------------- | ----------- | ------------ | --------- | --------------- | -------- | ------------------------ | ---------------- | ------------ | ----------- |
|                   |           |                 |                 |               |             |              | Based     | on the features | V;C      | and                      | the responsetime |              | T, we       |
| The critical      |           | path extraction |                 | algorithm     | is crafted  | to sys-      |           |                 |          |                          |                  |              |             |
|                   |           |                 |                 |               |             |              | construct | the CNN-based   |          | performance              |                  | prediction   | model,      |
| tematically       | identify  | the             | longest         | path          | (critical   | path) from a |           |                 |          |                          |                  |              |             |
|                   |           |                 |                 |               |             |              | which is  | divided         | into two | steps,                   | i.e.,            | transforming | the         |
| microservice      | execution |                 | history         | graph.        | The process | begins       |           |                 |          |                          |                  |              |             |
|                   |           |                 |                 |               |             |              | grayscale | image based     | on       | the resource-performance |                  |              | data,       |
| by initiatingfrom |           | the             | current node,   | initiatingthe |             | path, and    |           |                 |          |                          |                  |              |             |
|                   |           |                 |                 |               |             |              | and then  | constructing    | the      | CNN                      | model            | to           | predict the |
| including         | the       | current         | node within     | it.           | If the      | current node |           |                 |          |                          |                  |              |             |
responsetimeofthemicroservicesnodesunderthespecific
lackschildnodes,thepathterminates,andthecurrentpath
|              |             |          |          |           |             |          | resource allocation. |           | The details |               | are shown | in    | Fig. 3.       |
| ------------ | ----------- | -------- | -------- | --------- | ----------- | -------- | -------------------- | --------- | ----------- | ------------- | --------- | ----- | ------------- |
| is returned. | Conversely, |          | the      | algorithm | retrieves   | the last |                      |           |             |               |           |       |               |
|              |             |          |          |           |             |          | First, we            | transform | the         | grayscale     | image     | based | on the        |
| returned     | child       | node and | proceeds | with      | a recursive | search   |                      |           |             |               |           |       |               |
|              |             |          |          |           |             |          | resource-performance |           | data.       | Specifically, |           | for   | the resource- |
123

| ClusterComputing(2025)28:786          |        |                                         |     |     |     | Page7of19 | 786 |
| ------------------------------------- | ------ | --------------------------------------- | --- | --- | --- | --------- | --- |
| Algorithm1 Criticalpath(CP)extraction |        |                                         |     |     |     |           |     |
|                                       | Input: | : Microservice execution history graph  |     | ;   |     |           |     |
:currentNote
:currentNote.lastReturnChild
:currentNote.childNotes
:startNode
|     | Output: | CP # Critical Path        |     |     |     |     |     |
| --- | ------- | ------------------------- | --- | --- | --- | --- | --- |
|     | 1:      | functionLongestPath(G,cn) |     |     |     |     |     |
CP←∅
|     | 2:  | #Initializes an empty path set to store the longest path from CP.  |     |     |     |     |     |
| --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- |
CP.add(cn) #Add currentNode to the path.
3:
|     | 4:  | if == None then  |     |                                         |     |     |     |
| --- | --- | ---------------- | --- | --------------------------------------- | --- | --- | --- |
|     | 5:  | Return CP        |     |                                         |     |     |     |
|     | 6:  | else             |     |                                         |     |     |     |
|     | 7:  | lrc ←            | .   | ℎ # Get the last returned child of the  |     |     |     |
current node
8: CP.extend(LongestPath(G,lrc)) #Recursively extend the path with the longest
path from lrc
|     |     | each cn | Iterate over all child nodes cn |     |                 |     |     |
| --- | --- | ------- | ------------------------------- | --- | --------------- | --- | --- |
|     | 9:  | for     | in  do #                        |     | of the current  |     |     |
currentNode
10: ifcn.happensBefore(lrc) then #Check if the child node occurs before the last
returned child
|     |     | CP.extend(LongestPath(G,cn))  |     |                   | cn,                |     |     |
| --- | --- | ----------------------------- | --- | ----------------- | ------------------ | --- | --- |
|     | 11: |                               |     | # Starting  with  | call  LongestPath  |     |     |
recursively.
|     | 12: | end if                                                |     |     |     |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
|     | 13: | end for                                               |     |     |     |     |     |
|     | 14: | ReturnCP #Return critical path                        |     |     |     |     |     |
|     | 15: | functionFindCP(G):                                    |     |     |     |     |     |
|     | 16: | ← G.getStartNode() // Get the start node of the graph |     |     |     |     |     |
17: return LongestPath(G,  ) // Find and return the longest path starting from the
start node
Fig.3 CNNRPMmodeldiagram
123

| 786 Page8of19 |     |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:786 |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
performance samples, each of which has multiple feature layer executes convolution operations on the input data,
columnsandalabelcolumn,wherethefeaturecolumnsare employingcustomizedconvolutionkernelstoextractimage
the set of relevant resource features V captured by vmstat features.Theactivationlayeremploysanactivationfunction
and the set of resource allocation features C captured by to introduce nonlinear mapping, while the pooling layer
cgroup, and the label column is the corresponding perfor- reduces feature dimensions, often placed after the convolu-
mancemetricT.Then,wenormalizeeachresourcefeature tionallayertoyieldsmaller,refinedfeatures.Weiteratethe
from each sample into the range of [0,1], which will be convolution, activation, and pooling operations until con-
then mapped with the grayscale values in a predefined vergence,andtheresultingwell-trainedCNNisthenutilized
character set (where each character corresponds to a for accurate prediction of microservice node performance.
grayscale level). The processed characters are then drawn In this paper, the CNN is trained via back propagation
inablankimageusingimageprocessinglibrariesinatop- algorithm to optimize its parameters and the loss function
to-bottom, left-to-right order or some specific layout is shown in Eq. (1).
| strategytoensureeachfeatureiscorrectlypositionedintoa |     |     |     |     |     |     | 1   |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ð1Þ
| two-dimensional |     | matrix, | and | after performing |     | the neces- | L¼(cid:3) | T i lna i ; |     |     |     |     |     |
| --------------- | --- | ------- | --- | ---------------- | --- | ---------- | --------- | ----------- | --- | --- | --- | --- | --- |
n
| sary filling                | and              | alignment       | operations, |                            | a gray-scale | image |                          |               |            |         |                           |             |           |
| --------------------------- | ---------------- | --------------- | ----------- | -------------------------- | ------------ | ----- | ------------------------ | ------------- | ---------- | ------- | ------------------------- | ----------- | --------- |
|                             |                  |                 |             |                            |              |       | wherexdenotesthesample,T |               |            |         | denotesthecollectedtime,a |             |           |
| feature image               | is               | formed          | for each    | sample.                    |              |       |                          |               |            |         |                           |             |           |
|                             |                  |                 |             |                            |              |       | denotes                  | the predicted |            | output, | and                       | n denotes   | the total |
| Forexample,thestep(1)inFig. |                  |                 |             | 3illustratedtheprocessof   |              |       |                          |               |            |         |                           |             |           |
|                             |                  |                 |             |                            |              |       | number of                | samples.      | The        | loss    | function                  | measures    | the simi- |
| gray-scale                  | image            | transformation. |             | Assume                     | that there   | are N |                          |               |            |         |                           |             |           |
|                             |                  |                 |             |                            |              |       | larity between           |               | the actual |         | output                    | probability | and the   |
| samples                     | andeachofthemhas |                 |             | fourfeatures(i.e.,numberof |              |       |                          |               |            |         |                           |             |           |
|                             |                  |                 |             |                            |              |       | expected                 | ones, and     | the        | smaller | the value                 | of cross    | entropy,  |
CPU,memorycapacity,andI/Othroughput)andalabelcol-
| umnT |     |     |     |     |     |     | the closer | the two | probability |     | distributions | are. |     |
| ---- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | ------------- | ---- | --- |
i ,thenafter2Dembeddingofsample1,wecangenerate
|                       |     |     |                               |     |     |     | The specific |     | algorithm | of  | CNN-based |     | performance |
| --------------------- | --- | --- | ----------------------------- | --- | --- | --- | ------------ | --- | --------- | --- | --------- | --- | ----------- |
| agrayscaleimagenamedT |     |     | .jpg,i.e.,theimagewithperfor- |     |     |     |              |     |           |     |           |     |             |
1
manceT containsfourfeaturesatdifferentlocations. prediction is shown in Algorithm 2.
1
ForthetimecomplexityofAlgorithm2,weanalyzestep
| The | second | step involves |     | constructing | the | CNN and |     |     |     |     |     |     |     |
| --- | ------ | ------------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
subsequently forecasting the performance of microservice by step. For the FineTuneCNN(), it initializes and then
|             |             |     |          |             |     |            | fine-tunes | the CNN | model. | Assuming |     | the time | complexity |
| ----------- | ----------- | --- | -------- | ----------- | --- | ---------- | ---------- | ------- | ------ | -------- | --- | -------- | ---------- |
| nodes under | a specified |     | resource | allocation. | The | data input |            |         |        |          |     |          |            |
layer of CNN primarily pre-processes raw image data of FineTuneCNN() is OðCÞ, where C represents the com-
|         |            |      |         |          |                |     | plexityofthe | CNNmodel,which |     |     | typicallydependsonthe |     |     |
| ------- | ---------- | ---- | ------- | -------- | -------------- | --- | ------------ | -------------- | --- | --- | --------------------- | --- | --- |
| through | techniques | such | as mean | removal, | normalization, |     |              |                |     |     |                       |     |     |
and PCA/SVD dimensionality reduction. The convolution numberoflayers,thenumberofparameters,andthesizeof
thetrainingdata.TheouterloopiteratesoverthedatasetD
| Algorithm2 | CNNRPMconstruction |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Input:
|     |     |     |     |                                |     |     | ={  |           | }                  |     |     |     |     |
| --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --------- | ------------------ | --- | --- | --- | --- |
|     |     |     |     | Resource-performance data set  |     |     |     | (cid:638) | # n pieces of data |     |     |     |     |
FineTuneCNN()
|     |     | Output: |     | The Prediction of response time  |                             |                              |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | -------------------------------- | --------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 1:      |     | =FineTuneCNN()                   |                             | #CNNRPM model initialization |     |     |     |     |     |     |     |
|     |     | 2:      |     | for in                           | do:                         |                              |     |     |     |     |     |     |     |
|     |     | 3:      |     |                                  | = [] # Initialize an empty  |                              |     |     |     |     |     |     |     |
|     |     | 4:      |     | for                              | in                          | do:                          |     |     |     |     |     |     |     |
5: image[ .position] =  .value # Iterate over each cell of the table
data, filling its value into the corresponding image position.
|     |     | 6:  |     | end for |         |     |                                             |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | 7:  |     | =       | (image[ |     | .position]) # The CNNRPM model was used to  |     |     |     |     |     |     |
predict the response time
|     |     | 8:  |     | end for |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 9:  |     | return  |     |     |     |     |     |     |     |     |     |
123

ClusterComputing(2025)28:786 Page9of19 786
withndatapoints,sothetimecomplexityoftheouterloop • A¼fa ;a ;...;a;a ;...;a g indicates the action
1 2 i iþ1 n
is OðDÞ. The inner loop, iterating over m features of each space, which is the set of executable actions, where
data point D, has the time complexity of OðmÞ. For each a ¼{xcpu, xmemory, xio} indicates the i-th resource
i i i i i
data point, the F function is called to make a pre- allocation scheme on the microservice node.
cnnrpm
diction. Assuming the time complexity of the forward • Therewardisthefeedbackobtainedbytheenvironment
propagationoftheCNNmodelisOðFÞ,whereFrepresents basedontheactiontakenbythecurrentmicroservicenode
the computational complexity of the CNN model, which M,whichrepresentsthevalueobtainedaftermicroservice
i
typicallydependsontheinputdatadimensions,kernelsize, nodeM takingactiona inthecurrentstates .Thereare
i i;t i;t
number of layers, etc. Thus, combining the time com- two kinds of rewards: positive feedback and negative
plexityoftheabovesteps,thetotaltimecomplexitycanbe feedback. When the scheduled resources can meet the
expressed as OðCÞþOðnÞ(cid:4)ðOðmÞþOðFÞÞ. needsofmicroservicenodesandarelowerthanaspecific
threshold,therewardispositive.Otherwise,therewardis
3.4 Resource allocation: construction of DDPG- negative.Thegoalofmicroservicenodeistomaximizethe
based model rewardfunctiongiveninEq. (2):
R
i
¼ P1
j¼0
cjr
i;tþj
ð2Þ
This section first defines the resource allocation problem
for microservice nodes. Then, a method based on deep wherec(c(cid:2)½0,1(cid:5))isthediscountfactor,whichmeasuresthe
(cid:2) (cid:3)
reinforcement learning (DDPG) is adopted to coordinate extenttowhichfuturerewardsaffectcurrentactions.r x i;t
theallocationofeachtypeofresources,aimingtomeetthe istheimmediaterewardobtainedbythemicroservicenode
end-to-end QoS of the task, while improvingthe resources whenittakesactiona ,anditcanrepresenttheratioofthe
i;t
utilization of the whole system as much as possible. actual resource usage, whose calculation is given in
Eq. (3).
3.4.1 Problem definition in resource allocation model
ccpu cmemory cio
based on DDPG r (cid:2) x (cid:3) ¼a i;t þb i;t þc i;t ð3Þ
i;t xcpu xmemory xio
i;t i;t i;t
In this study, the resource allocation problem based on
where a, b and c represent the weight, and x represents
i;t
deep reinforcement learning is first modeled as a Markov
thesetofresourcequotasassignedtomicroservicenodeM
i
chain. In a cloud-native architecture, an application typi-
attimet,namely{xcpu,xmemory,xio}.Forexample,alarger
cally consists of multiple microservice nodes, each of i;t i;t i;t
ccpu=xcpu ratio indicates that the CPU resource allocation
which running a specific function. Assuming that an i;t i
share allocated to the microservice node is closer to the
application consisting of n microservice nodes, which can
actual demand. The reward function defines the value that
be represented as M ¼fM ;M ;M g where Mði2½1;n(cid:5)Þ
1 2 n i
if the resource allocation is proper.
represents the i-th one. The Markov model can be
expressed as the tupleo¼fS;A;R;Pg, where S represents • The status value s, action value a, reward value r of
t t t
the state space, A represents the action space, R represents each training and the status value s of the next
tþ1
the reward set, and P represents the state transition prob- moment are stored as a tuple:
ability.Thecurrentstates isaspecificvalueofstateSfor
i;t e ¼ðs;a;r;s Þ ð4Þ
t t t t tþ1
nodeM.Ateachtmoment,eachmicroservicenodeM will
i i
take corresponding actions a based on specific policies All training samples are stored in the experience buffer
i;t
according to its current states i;t , and then produce the next D, namely D¼fe 1 ;e 2 ...;e t g:
state s through the state transition probability func-
i;tþ1
(cid:2) (cid:3) 3.4.2 Construction of resource allocation model based
tionP s js ;a ;;a :S(cid:6)A!½0,1(cid:5), thus M receives
i;tþ1 i;t i;t n;t i
on DDPG
the instant rewards r through status and action functions.
i;t
The basic components of o¼fS;A;R;Pg are described in
TheresourceallocationmodelbasedonDDPGproposedin
detail below.
thispaperisshownintheFig. 4.Firstly,theActornetwork
• S¼fs ;s ;...;s;s ;...;s gindicatesthestatespace, capturestheobservationinformationthroughtheagentand
1 2 i iþ1 n
s ¼fccpu;cmemory;ciog indicates the resources allo- then uses deterministic strategy to get the corresponding
i;t i;t i;t i;t
cated for the i-th node at time t, where ccpu is the action. Second, the Critic network captures the action and
i;t
number of cores used by the CPU, and cmemory is the state information of all microservice nodes and evaluates
i;t
the output action of the Actor network.
memory capacity, and cio is the I/O throughput.
i;t In this paper, we adopt an architecture of dual neural
networktorealizetheDDPGalgorithm,whichcontainsthe
123

| 786 Page10of19 |     |     |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:786 |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
Fig.4 Resourceallocation
modeldiagrambasedonDDPG
policy functioninActor network andthe valuefunctionin Qlðs;aÞ¼E ½rðs;aÞþcQlðs
|     |     |     |     |     |     |     |     | t t | rt;stþ1(cid:8)E |     | t t | tþ1 | ;a tþ1 | Þ(cid:5) ð6Þ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ------ | ------------ |
Criticnetwork,namelyOnlinenetworkandTargetnetwork.
TheCriticnetworkusesthevaluefunctionQpðs;aÞtojudge wherea t ¼p h ðs i Þþe,erepresentstheexplorationnoiseon
|     |     |     |     |     |     |     |     | the behavioral | strategy. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | --- | --- | --- | --- |
theperformanceofActor,andthenguidewhoseactionsin
thenextstage.TheActorusesthepolicyfunctionptoupdate The network parameters are updated by minimizing the
meansquareerrorbetweenthecurrentQvalueandthetargetQ
| the value | method | of  | the strategy | p   | according | to  | the opti- |     |     |     |     |     |     |     |
| --------- | ------ | --- | ------------ | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
value,withhQastheupdateparameter.Theerrorfunctionis:
mizationresultofthevaluefunctionbytheCritic.InActor
networks,thepolicyfunctionp :S!Aisamappingfrom L(cid:2)hQ(cid:3) h(cid:4) Q(cid:2) ;atjhQ(cid:3) (cid:3)rðst;atÞþcQl(cid:2)stþ1;lðstþ1ÞjhQ(cid:3) 2(cid:5)i
|     |     |     |     | h   |     |     |     | ¼E st(cid:8)qb;at(cid:8)b;rt(cid:8)E |     |     | ðs t |     |     | Þ   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | ---- | --- | --- | --- |
thestatespacetotheactionspace,indicatingthattheagent
ð7Þ
| selectsactiona |     | inthestates,executestheactionandmoves |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                |     | t                                     | t   |     |     |     |     |     |     |     |     |     |     |     |
to the next state s with probability fðs;aÞ, while Then, by maintaining a parameterized Actor function
|     |     | tþ1 |     |     |     | t   | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lðsjhlÞ,
receiving the reward r from the environment feedback, this function guides the current policy by deter-
t
wherehisthetargetnetworkparameteroftheActor. ministically mapping the state to a particular action. The
Generally speaking, DDPG consists of four neural net- Actor update formula is as follows:
| w o r k s : | T a r ge t | net w o rk | i n A | c t o r n e tw | o r k, | O n l i n e | n e t w o r k | ,              |     |         |               |     |     |     |
| ----------- | ---------- | ---------- | ----- | -------------- | ------ | ----------- | ------------- | -------------- | --- | ------- | ------------- | --- | --- | --- |
|             |            |            |       |                |        |             |               |                | h   | (cid:2) | s;ajhQ(cid:3) |     | i   |     |
|             |            |            |       |                |        |             |               | r hlJ (cid:9)E |     | r hlQ   |               | j   |     |     |
Ta r g e t n e tw o rk i n C rit i c n e t w o r k a n d O n l i n e n e t w o r k . st(cid:8)qb s¼st;a¼lðstjhlÞ
| A c co rd i | n g t o | t h e c urr e | n t s t a t | ev al ue | , t h e On | li n e n | e tw o rk in |     |       |                       |     |            |     |     |
| ----------- | ------- | ------------- | ----------- | -------- | ---------- | -------- | ------------ | --- | ----- | --------------------- | --- | ---------- | --- | --- |
|             |         |               |             |          |            |          |              |     | h     | (cid:2) s;ajhQ(cid:3) |     |            |     | i   |
|             |         |               |             |          |            |          |              | ¼E  | r hlQ |                       | j   | r lðsjhlÞj |     | ð8Þ |
th e A c t o r n e t w o rk p r o v i d e s th e p o l i cy fu n c ti o n o f th e st(cid:8)qb s¼st;a¼lðstÞ hl s¼st
| current              | state, | the policy | function                        | p           | ðsÞ:S!A    |            | is a map- |                  |            |                |            |                 |     |             |
| -------------------- | ------ | ---------- | ------------------------------- | ----------- | ---------- | ---------- | --------- | ---------------- | ---------- | -------------- | ---------- | --------------- | --- | ----------- |
|                      |        |            |                                 | h           | i          |            |           |                  |            |                |            |                 |     |             |
|                      |        |            |                                 |             |            |            |           | where J          | represents | the            | state      | value function, | the | value of    |
| ping from            | state  | space      | to action                       | space,      | indicating |            | that the  |                  |            |                |            |                 |     |             |
|                      |        |            |                                 |             |            |            |           | which represents |            | the cumulative |            | expectation     | in  | each state  |
| agent selects        |        | action a   | in state                        | s, executes |            | the action | and       |                  |            |                |            |                 |     |             |
|                      |        |            | t                               | t           |            |            |           |                  |            |                |            |                 |     |             |
|                      |        |            |                                 |             |            |            |           | adjustment       | process.   |                |            |                 |     |             |
| movestothenextstates |        |            | tþ1 withprobabilityfðs;aÞ,while |             |            | t          | t         |                  |            |                |            |                 |     |             |
|                      |        |            |                                 |             |            |            |           | The target       | network    |                | parameters | x0 and          | h0  | are updated |
| receiving            | reward | r from     | environment                     |             | feedback.  |            |           |                  |            |                |            |                 |     |             |
t
|     |     |     |     |     |     |     |     | through soft | updating |     | to ensure | the parameters |     | can be |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | --------- | -------------- | --- | ------ |
TheOnlinenetworkintheCriticnetworkprovidestheQ
|                |     |         |           |     |        |         |        | updated slowly,      |     | thus improving |     | the stability | of  | learning: |
| -------------- | --- | ------- | --------- | --- | ------ | ------- | ------ | -------------------- | --- | -------------- | --- | ------------- | --- | --------- |
| value function |     | Q ðs;aÞ | according |     | to the | current | state— |                      |     |                |     |               |     |           |
|                |     | x t     | t         |     |        |         |        |                      |     |                |     |               |     |           |
|                |     |         |           |     |        |         |        | x0  exþð1(cid:3)eÞx0 |     |                |     |               |     | ð9Þ       |
actionoutputintheActornetwork,whichisusedtoevaluate
thecurrentpolicy.TheQvaluefunctionisdefinedasfollows.
|         |     |                                      |     |       |             |     |     | h0  ehþð1(cid:3)eÞh0 |     |     |     |     |     | ð10Þ |
| ------- | --- | ------------------------------------ | --- | ----- | ----------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | ---- |
| Q ðs ;a | Þ¼E |                                      |     | ½R js | ;a          |     |     |                      |     |     |     |     |     |      |
| x t     | t   | ri(cid:7)t;si[t(cid:8)E;ai[t(cid:8)p |     | t     | t t (cid:5) |     | ð5Þ |                      |     |     |     |     |     |      |
Basedontheaboveprocess,whenreceivingfeedbackthat
theend-to-endresponsetimeoftheCNNRPMmodelexceeds
| If the | Target | policy | is deterministic, |     | we  | can describe | it  |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ----------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
as the function l:S A, in order to increase the agent’s a specific threshold range, we first initialize the experience
bufferD,theActornetwork,andtheCriticnetwork.
| exploration | in  | the environment, |     | DDPG | adds | a   | Gaussian |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | ---- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
noise function to the behavior policy, and the Target net- Initializing the state at the beginning of each episodes,
work of the Critic network is used to estimate the Q-value the Actor network performs a specific action a={xcpu,
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
function of the state-action at the next moment: xmemory,xio}forincreasingtheamountofresourcessuchas
i i
123

ClusterComputing(2025)28:786 Page11of19 786
CPU, memory and I/O allocated, based on the state of the In the implementation of Algorithm 3, the resource
microservices node when the current actual amount of allocation model leveraging DDPG first establishes an
CPU, memory and I/O resources used Actor network,which determinesanaction Abased onthe
s ¼ (cid:6) ccpu;cmemory;cio(cid:7) . And the agent gets the corre- current environment state S. Subsequently, the network
i i i i
ccpu cmemory cio receivesthecorrespondingrewardRandobservesthenext
sponding reward rðxÞ¼a i þb i þc i and the next
n
i xc
i
pu
o
xm
i
emory xi
i
o stateS0.Next,aCriticnetworkisformulatedtoevaluatethe
state s ¼ ccpu ;cmemory;cio . The status value s, Actor’sstrategyandsteeractionsforthesubsequentphase.
i;tþ1 i;tþ1 i;tþ1 i;tþ1 t
The deterministic policy is employed to update the Critic
action value a, reward value r of each training and the
t t
network, aiming to maximize the Q value and reward.
status value s of the next moment are stored as a tuple
tþ1
Moreover,duringthetrainingoftheQnetwork,experience
e ¼ðs;a;r;s Þ, which will be put into the experience
t t t t tþ1
replay is utilized to break the correlation between data
buffer D. The above operations are repeated until the
samples, ensuring they adhere to an independent and
experience buffer D reaches the minimum sampling crite-
identical distribution. This approach reduces the variance
ria, and then N samples are randomly selected from D to
in parameter updates, enhances convergence speed, and
train the Actor network to update the parameters h of the
ultimately ensures a reasonable training duration.
policy function p and the Critic network. The specific
Lastly, we give an example including performance
resource allocation process based on DDPG is shown in
predictionandresourceallocationtobetterclarifyouridea
Algorithm 3.
(Fig. 5).
Algorithm3 DDPG-basedadaptiveresourceallocation
Input: Initialize the experience buffer , the Actor network, and the Critic network
Output: Resource allocation action
1: ← , ← # Initialize the target network weight parameters and
Initialize the experience buffer
2: for each episode=1 to do
3: Random noise initialization
4: Get the initial state value = , ,
5: fort = 1 to T do
6: ={ (cid:712) (cid:712) } # Perform action
7:
( )= + + #Get the rewards ( )
8: , = , , , , , # Gets the next state value ,
9: Save the tuple =( , , , ) to experience buffer
10: Multi-dimensional arrays ( , , , ) randomly sampling the number of batches
from
11: ( , )= , ~ , ~ [ | , ] # Online networkof Critic network
12: ( , )= , ~ [ ( , )+ ( , ))] # Target network of Critic
network
13: ( )= [( (( , | )− ( , )+ ( , ( )| )) )]# Minimize the loss
function to update the Critic network
14:
≈ ( , | )| # The Actor network is updated using
~ ,
policy gradients
15: ← +(1− ) # Update the target network parameters
16: = +(1− ) # Update the target network parameters
17: Get current status = , ,
18: = ( )+ ; # Execution action
19: end for
20: end for
21: Return ; # The resource adjustment plan is displayed
123

786 Page12of19 ClusterComputing(2025)28:786
Fig.5 AnexampleofCNNRPM-basedresourceallocation
Example Assume that the QoS-specified response time is
Next, set a = 0.5, b = 0.3, and c = 0.2 in Eq. (3), and
within the range of 1–5. When the response time is less
use this formula to calculate the reward values r corre-
than 1, the prediction result is 0, indicating that the allo-
sponding to the above three resource adjustment schemes.
cated resources are insufficient to meet the current task’s
The results are as follows:
requirements, and more resources need to be allocated.
Whenadoptingschemea ,thevaluesoftheelementsin
1
When the response time falls within the range of 1–5, the
s are c ¼8;c ¼1024MB;c ¼1GB, therefore,
i cpu memory I=O
predictionresultis1,indicatingthattheallocatedresources
the reward value is
meet the current task’s requirements, and the resource
r ¼0:5(cid:4)4þ0:3(cid:4) 512 þ0:2(cid:4)1¼0:6. When adopting
allocation is reasonable. When the response time exceeds 1 8 1024 1
scheme a , the values of the elements in s are
5, the prediction result is 2, indicating that excessive 2 i
c ¼10;c ¼1536MB;c ¼2GB, therefore, the
resources are allocated, leading to resource waste, and the cpu memory I=O
resource allocation needs to be adjusted appropriately. rewardvalueisr 2 ¼0:5(cid:4) 1 4 0 þ0:3(cid:4) 1 5 5 1 3 2 6 þ0:2(cid:4)1 2 ¼0:324.
Whenadoptingschemea ,thevaluesoftheelementsin s
3 i
WhentheresponsetimepredictedbyCNNRPMexceeds
isc ¼12;c ¼2048MB;c ¼3GB,therefore,the
cpu memory I=O
theQoS-specifiedrange,theDDPGstrategy isexecutedto
rewardvalueisr ¼0:5(cid:4) 4 þ0:3(cid:4) 512 þ0:2(cid:4)1¼0:336.
adaptively adjust the resources. 3 12 2048 3
Subsequently,setc = 0.7inEq. (6)andusethisformula
Assume that the resource allocation for this microser-
to calculate the target values of the value function for the
vice node is X ¼fx ¼4;x ¼512MB;x ¼
CPU memory I=O
above resource adjustment schemes. The results are as
1GBg. Based on the physical resources of the local server,
follows:
the adjustment ranges for each type of resource for the
microservicenodearedeterminedasfollows:x CPU 2½1,20(cid:5); Qðs;a 1 Þ¼0:6þ0:7(cid:4)0:6¼1:02
x memory 2½512MB;4096MB(cid:5), x I=O 2f1GB;4GBg. Three Qðs;a 2 Þ¼0:324þ0:7(cid:4)0:3¼0:534
resource adjustment schemes are proposed as follows: Qðs;a Þ¼0:336þ0:7(cid:4)0:3¼0:546
3
a ¼fc ¼8;c ¼1024MB;c ¼1GBg
1 cpu memory I=O Fromtheabovecalculations,itcanbeconcludedthatthe
a
2
¼fc
cpu
¼10;c
memory
¼1536MB;c
I=O
¼2GBg
value function Q is maximized when resource allocation
a 3 ¼fc cpu ¼12;c memory ¼2048MB;c I=O ¼3GBg scheme a 1 is adopted. Therefore, scheme 1 is ultimately
selected as the resource adjustment strategy.
123

| ClusterComputing(2025)28:786 |             |     |     |     |     |     |     |          |          |     |             |     | Page13of19 |     | 786 |
| ---------------------------- | ----------- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ----------- | --- | ---------- | --- | --- |
| 4                            | Experiments |     |     |     |     |     |     | 4.2 RQ1. | Resource |     | pPrediction |     | of CNNRPM  |     |     |
We conduct extensive experiments in response to the fol- Inthispart,FIRM,VIME(sl-only,semi-only,self-semi-sl)
lowing research questions (RQ): [30], Scarf [31], Regressor, Decision tree, XGboost, Ran-
|      |          |     |              |              |      |            |      | dom Forest       | and      | Naive_Bayes |                | are            | used as baselines. |           | Gen-    |
| ---- | -------- | --- | ------------ | ------------ | ---- | ---------- | ---- | ---------------- | -------- | ----------- | -------------- | -------------- | ------------------ | --------- | ------- |
| RQ1: | Compared |     | with other   | tabular      | data | prediction | mod- |                  |          |             |                |                |                    |           |         |
|      |          |     |              |              |      |            |      | erally speaking, |          | FIRM        | is a           | representative |                    | framework | for     |
|      | els,     | can | our proposed | CNNRPM       |      | predict    | the  |                  |          |             |                |                |                    |           |         |
|      |          |     |              |              |      |            |      | cloud-native     | resource |             | allocation,    | VIME           | and                | Scarf     | are two |
|      | response |     | time of      | microservice |      | nodes      | more |                  |          |             |                |                |                    |           |         |
|      |          |     |              |              |      |            |      | newly proposed   |          | deep        | learning-based |                | models             | for       | tabular |
effectively?
|     |     |     |     |     |     |     |     | data prediction, |     | while | the | others | are traditional |     | machine |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | --- | ------ | --------------- | --- | ------- |
RQ2: CantheresourceschedulingmodelbasedonDDPG
|     |          |     |              |             |     |          |      | learning | method. | The | details | are given | as follow: |     |     |
| --- | -------- | --- | ------------ | ----------- | --- | -------- | ---- | -------- | ------- | --- | ------- | --------- | ---------- | --- | --- |
|     | maximize |     | the resource | utilization |     | compared | with |          |         |     |         |           |            |     |     |
the other baselines? • FIRM, a representative framework to achieve the fine-
|     |              |     |       |     |     |     |     | grained    | resource   |        | management   |     | for microservice, |      | adopts |
| --- | ------------ | --- | ----- | --- | --- | --- | --- | ---------- | ---------- | ------ | ------------ | --- | ----------------- | ---- | ------ |
|     |              |     |       |     |     |     |     | SVM        | to predict |        | microservice |     | node performance. |      | The    |
| 4.1 | Experimental |     | setup |     |     |     |     |            |            |        |              |     |                   |      |        |
|     |              |     |       |     |     |     |     | parameter  |            | is     | set          | to  | learning          | rate | = 0.1, |
|     |              |     |       |     |     |     |     | batch_size |            | = 128. |              |     |                   |      |        |
Firstly,weappliedDockertodeployseverallight-weighted
|     |     |     |     |     |     |     |     | • VIME | (Value | Imputation |     | and | Mask | Estimation), | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ---------- | --- | --- | ---- | ------------ | --- |
containersontwophysicalhosts,whosedetailsaregivenin
|       |     |             |                  |     |              |     |     | semi-supervised |     |     | deep learning |     | framework, | comes | in  |
| ----- | --- | ----------- | ---------------- | --- | ------------ | --- | --- | --------------- | --- | --- | ------------- | --- | ---------- | ----- | --- |
| Table | 2,  | to simulate | the cloud-native |     | environment. |     | The |                 |     |     |               |     |            |       |     |
threeversions:sl-only,semi-only,andself-semi-sl.The
| kernel | version |     | for each | of the | container |     | is Linux |     |     |     |     |     |     |     |     |
| ------ | ------- | --- | -------- | ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
firstoneusesmulti-layerperceptron(MLP)fortraining,
| 5.10.102.1-microsoft-standard-WSL2, |       |        |                |     | and           | the | operating |            |         |        |                 |     |                 |     |          |
| ----------------------------------- | ----- | ------ | -------------- | --- | ------------- | --- | --------- | ---------- | ------- | ------ | --------------- | --- | --------------- | --- | -------- |
|                                     |       |        |                |     |               |     |           | the second |         | adopts | Semi-Supervised |     | Learning        | for | train-   |
| system                              | is    | Ubuntu | 20.04.5 LTS.   |     |               |     |           |            |         |        |                 |     |                 |     |          |
|                                     |       |        |                |     |               |     |           | ing,       | and the | last   | one combines    |     | self-supervised |     | learning |
|                                     | Then, | we run | Deathstarbench | as  | the real-time |     | applica-  |            |         |        |                 |     |                 |     |          |
andsemi-supervisedlearning.Theparametersaresetas
tions,andthenappliedthePhoronix-Test-Suitetosimulate
|             |          |             |                 |          |             |           |           | maxdepth         |           | = 3, learning-rate |                | =          | 0.1, batch_size |              | = 128.   |
| ----------- | -------- | ----------- | --------------- | -------- | ----------- | --------- | --------- | ---------------- | --------- | ------------------ | -------------- | ---------- | --------------- | ------------ | -------- |
| the         | resource | competition | from            | the      | perspective |           | of CPU,   |                  |           |                    |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | • Scarf          | (Scalable |                    | and Accurate   |            | Recurrent       | Forest),     | a        |
| memory,     |          | and I/O.    | At the same     | time,    | the         | processes | man-      |                  |           |                    |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | scalable         | and       | accurate           | recurrent      |            | forest model,   |              | captures |
| agement     |          | mechanism   | Cgroup          | are used | to          | alter     | resource  |                  |           |                    |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | the regularities |           | in                 | tabular        | data       | with the        | integration  | of       |
| allocation, |          | whose       | details are     | given    | in Table    | 3,        | the Linux |                  |           |                    |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | decision         | trees.    |                    | The parameters |            | are             | set as       | hidden   |
| profiling   |          | tool vmstat | and distributed |          | tracing     | system    | Jaeger    |                  |           |                    |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | layers           | = 8,      | batch_size         |                | = 128,     | corruption_rate |              | = 0.6,   |
| were        | used     | to collect  | data.           |          |             |           |           |                  |           |                    |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | learning-rate    |           | = 0.1.             |                |            |                 |              |          |
|             |          |             |                 |          |             |           |           | • DT             | (Decision | tree),             | a              | supervised | learning        | algorithm,   |          |
|             |          |             |                 |          |             |           |           | uses             | the idea  | of                 | classification |            | to build a      | mathematical |          |
Table2 Thedetailsofsimulationenvironment
|     |     |     |     |     | Physicalhost1 |     |     |     |     |     | Physicalhost2 |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
CPUtype 12thGenInte(R)Core(TM)i5-12500H 12thGenInte(R)Core(TM)i7-12700H
| CPUfrequency        |     |     |     |     | 3.2GHz   |     |     |     |     |     | 2.6GHz    |     |     |     |     |
| ------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
| Memorytype          |     |     |     |     | 16GBDDR5 |     |     |     |     |     | DDR4      |     |     |     |     |
| Memoryfrequency     |     |     |     |     | 6400MHz  |     |     |     |     |     | 3200MHz   |     |     |     |     |
| Harddisktype        |     |     |     |     | 512GBSSD |     |     |     |     |     | 1024GBSSD |     |     |     |     |
| Lastlevelcache(LLC) |     |     |     |     | 18MB     |     |     |     |     |     | 24MB      |     |     |     |     |
Table3 Thedetailsofdata
|     |     |     |     | Feature |     |     |     |     | Featurevalue |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
collection
|     |     |     |     | cpu.shares |     |     |     |     | 512M,1024M,2048M,3072M |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
cpu.cfs_period_us 100000us,150000us,200000us,500000us,1000000us
|     |     |     |     | cpu.cfs_quota_us      |     |     |     |     | -1us,100000us,200000us,400000us,500000us |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | cpuset.cpus           |     |     |     |     | 3,7,9,11,15,19                           |     |     |     |     |     |     |
|     |     |     |     | memory.limit_in_bytes |     |     |     |     | 512M,1024M,1536M,2048M,4096M             |     |     |     |     |     |     |
|     |     |     |     | memory.swappiness     |     |     |     |     | 10,20,30,40,50,60                        |     |     |     |     |     |     |
123

| 786 Page14of19 |     |     |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:786 |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
model according to the characteristics of data, so as to whether the differences observed in the experimental
achieve the goal of data screening and decision. resultsarestatisticallysignificantratherthanduetochance.
• XGBoostis an efficient gradient boosting decision tree The t-test is a commonly used parametric test method
algorithm,andtheparametersaresetasmax-depth = 5, suitable for comparing the mean differences between two
| learning_rate |     | = 0.1, | estimators | = 100. |     |     |     | sets of data. |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | ------ | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
• RF (A Random Forest), an ensemble learning method The experimental comparisons are given in Table 4,
that consists of multiple decision trees, whose param- where the bolded font represents the best performing
eters are set as max-depth = 5, maxfeature = 5, algorithm in the current metrics, and the underlined font
iteration = 100. indicatesthenextbestmethod.ItcanbeseenfromTable4
• NB (Naive Bayes) is a simple probabilistic classifier thattheCNNRPMhasachievedthebestperformanceinall
based on Bayes’ theorem, which assumes that features metrics, and its accuracy, recall rate and F1 score are all
are independent of each other, and then makes the higher than 99%, even up to 100%, which is significantly
model easy to implement and understand. higher than other algorithms, and can predict the response
|     |     |     |     |     |     |     |     | time of | microservice | nodes | more | accurately, |     | but with | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ----- | ---- | ----------- | --- | -------- | --- |
Asforthemetrics,weadoptAccuracy,Precision,Recall
|     |     |     |     |     |     |     |     | lower standard |     | deviation. | FIRM, | which | makes | predictions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ----- | ----- | ----- | ----------- | --- |
andF1scoretoverifythepredictioneffectivenessbasedon
directlybasedondatatables,hasaslightlyloweraccuracy,
CNNRPM.Thecalculationoftheabove-mentionedmetrics
|           |          |        |           |           |     |     |         | recall rate | and        | F1 score | than   | CNNRPM.   | XGboost  | came | in    |
| --------- | -------- | ------ | --------- | --------- | --- | --- | ------- | ----------- | ---------- | -------- | ------ | --------- | -------- | ---- | ----- |
| are given | in Eqs.  | (1–4). |           |           |     |     |         |             |            |          |        |           |          |      |       |
|           |          |        |           |           |     |     |         | second,     | with both  | its      | recall | rate and  | F1 score | of   | 0.98, |
| First,    | accuracy | is an  | important | indicator | of  | the | overall |             |            |          |        |           |          |      |       |
|           |          |        |           |           |     |     |         | slightly    | lower than | CNNRPM,  |        | but still | showing  | high | pre-  |
performanceofthemodel,whichrepresentstheproportion
|               |             |         |           |           |                    |        |       | dictive  | accuracy. | XGboost    |           | performs     | well          | thanks     | to its |
| ------------- | ----------- | ------- | --------- | --------- | ------------------ | ------ | ----- | -------- | --------- | ---------- | --------- | ------------ | ------------- | ---------- | ------ |
| of the number | of          | samples | correctly | predicted |                    | to the | total |          |           |            |           |              |               |            |        |
|               |             |         |           |           |                    |        |       | powerful | feature   | processing |           | capabilities | and           | integrated |        |
| number        | of samples. | The     | accuracy  |           | rate is calculated |        | as    |          |           |            |           |              |               |            |        |
|               |             |         |           |           |                    |        |       | learning | framework | for        | capturing | complex      | relationships |            | in     |
follows:
|     |     |         |     |         |     |     |     | data. However, |     | compared | with | CNNRPM, | XGboost |     | falls |
| --- | --- | ------- | --- | ------- | --- | --- | --- | -------------- | --- | -------- | ---- | ------- | ------- | --- | ----- |
|     |     | (cid:2) |     | (cid:3) |     |     |     |                |     |          |      |         |         |     |       |
N T actual ¼T pre slightly short in the following aspects: first of all,
| fðaccuracyÞ¼ |     |     |     |     |     |     | ð11Þ |                                                  |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|              |     | N   |     |     |     |     |      | CNNRPMadoptsCNNtoextracttabularfeaturesingreater |     |     |     |     |     |     |     |
total
|         |     |            |        |     |        |             |     | depth, and | then | handle | nonlinear | relationships |     |     | better. |
| ------- | --- | ---------- | ------ | --- | ------ | ----------- | --- | ---------- | ---- | ------ | --------- | ------------- | --- | --- | ------- |
| where T | is  | the ground | truth, | T   | is the | prediction, |     |            |      |        |           |               |     |     |         |
actual pre Secondly, CNNRPM has more balanced indicators, indi-
| (cid:2)     | (cid:3) |          |        |                |             |     |     |             |          |          |         |             |      |          |         |
| ----------- | ------- | -------- | ------ | -------------- | ----------- | --- | --- | ----------- | -------- | -------- | ------- | ----------- | ---- | -------- | ------- |
| N T actual  | ¼T pre  | ) is the | number | of correct     | prediction, |     | and |             |          |          |         |             |      |          |         |
|             |         |          |        |                |             |     |     | cating that | it has   | a strong | ability | to identify |      | positive | and     |
| N indicates | the     | number   | of     | total samples. |             |     |     |             |          |          |         |             |      |          |         |
| total       |         |          |        |                |             |     |     | negative    | samples, | while    | XGboost | may         | have | a        | certain |
Next,precisionisameasureoftheproportionofamodel
|                  |           |               |             |      |              |     |       | deviation | between        | the | accuracy  | rate and | the       | recall rate. | In    |
| ---------------- | --------- | ------------- | ----------- | ---- | ------------ | --- | ----- | --------- | -------------- | --- | --------- | -------- | --------- | ------------ | ----- |
| that is actually | positive  |               | in a sample | that | is predicted |     | to be |           |                |     |           |          |           |              |       |
|                  |           |               |             |      |              |     |       | addition, | all indicators |     | of CNNRPM |          | algorithm | are          | rela- |
| positive,        | which can | be calculated |             | by   | Eq. (12).    |     |       |           |                |     |           |          |           |              |       |
tivelybalanced,andallscoresreach99%,indicatingthatit
TP has a strong ability to identify positive and negative sam-
| fðprecisionÞ¼ |     |     |     |     |     |     | ð12Þ |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
TPþFP ples, and can better adapt to different data distributions.
|            |                   |          |              |            |                  |             |      | In conclusion,         |           | CNNRPM      | is             | the most   | effective | modelin      |        |
| ---------- | ----------------- | -------- | ------------ | ---------- | ---------------- | ----------- | ---- | ---------------------- | --------- | ----------- | -------------- | ---------- | --------- | ------------ | ------ |
| where, TP  | represents        | the      | number       | of         | samples          | that are    | true |                        |           |             |                |            |           |              |        |
|            |                   |          |              |            |                  |             |      | predicting             | resource  | performance |                | among      | all       | methods,     | and    |
| positive;  | FP is the         | false    | positive.    | The        | higher           | value       | of   |                        |           |             |                |            |           |              |        |
|            |                   |          |              |            |                  |             |      | its prediction         | accuracy, |             | stability,     | reasonable |           | model        | struc- |
| precision  | is, the better    | the      | prediction   |            | can be obtained. |             |      |                        |           |             |                |            |           |              |        |
|            |                   |          |              |            |                  |             |      | ture, interpretability |           | and         | generalization |            | ability   | are superior |        |
| The recall | rate              | measures | the          | proportion | of               | all samples |      |                        |           |             |                |            |           |              |        |
|            |                   |          |              |            |                  |             |      | to other               | methods.  |             |                |            |           |              |        |
| that are   | actually positive |          | be correctly |            | predicted        | to be       | pos- |                        |           |             |                |            |           |              |        |
itivebythemodel.Therecallrateiscalculatedasfollows:
|     |     |     |     |     |     |     |     | 4.3 RQ2.Comparative |     |     | test | of resource | allocation |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---- | ----------- | ---------- | --- | --- |
TP
| fðrecallÞ¼ |     |     |     |     |     |     | ð13Þ | model | based | on  | DDPG |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ---- | ----- | ----- | --- | ---- | --- | --- | --- | --- |
TPþFN
where, FN is the false negative, and the higher value of We now evaluate the ability of DDPG-based resource
recall is, the better the prediction effect can be got. adjustment to meet QoS while reducing resource
| Finally, | the F1 | score | is the | harmonic | average | of  | accu- | consumption. |     |     |     |     |     |     |     |
| -------- | ------ | ----- | ------ | -------- | ------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
racy and recall, which takes the accuracy and recall into TheparametersettingsfortrainingDDPGusingfeature-
account, and the calculation is given in Eq. 14. performance data are as follows: For the reward function
|     |     |     |     |     |     |     |     | shown in | Eq. | (3), the | parameters | are | set | as a | = 0.5, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ---------- | --- | --- | ---- | ------ |
2(cid:4)fðprecisionÞ(cid:4)fðrecallÞ
| F1¼ |     |     |     |     |     |     | ð14Þ |          |       |        |              |     |         |     |      |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ----- | ------ | ------------ | --- | ------- | --- | ---- |
|     |     |     |     |     |     |     |      | b = 0.3, | and c | = 0.2, | representing | the | weights | of  | CPU, |
fðprecisionÞþfðrecallÞ
|     |     |     |     |     |     |     |     | memory, | and | I/O resources |     | in the resource |     | scheduling |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------- | --- | --------------- | --- | ---------- | --- |
Toensurethecredibilityoftheexperimentalresults,we
|     |     |     |     |     |     |     |     | process | respectively. |     | Other | key parameters |     | include | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ----- | -------------- | --- | ------- | --- |
have incorporated t-tests into the evaluation to verify minibatch size of 64, a replay buffer capacity of 100, a
123

| ClusterComputing(2025)28:786 |     |     |     |     |     |     |     |     |     | Page15of19 | 786 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
Table4 Thecomparisonsofdifferentmetricswith95%confidenceintervals
|                    |     | Accuracy  |     | Precision |     |     | Recall    |     |     | F1score   |     |
| ------------------ | --- | --------- | --- | --------- | --- | --- | --------- | --- | --- | --------- | --- |
| Scarf              |     | 0.83±2.32 |     | 0.84±7.48 |     |     | 0.99±6.11 |     |     | 0.91±5.22 |     |
| VIME(sl-only)      |     | 0.64±3.22 |     | 0.73±4.56 |     |     | 0.64±4.23 |     |     | 0.67±4.61 |     |
| VIME(semi-only)    |     | 0.28±1.79 |     | 0.73±2.23 |     |     | 0.28±4.22 |     |     | 0.36±3.27 |     |
| VIME(self-semi-sl) |     | 0.57±1.78 |     | 0.71±3.46 |     |     | 0.57±3.56 |     |     | 0.62±3.56 |     |
| FIRM               |     | 0.96±2.99 |     | 0.95±2.56 |     |     | 0.96±2.89 |     |     | 0.95±3.52 |     |
| Regressor          |     | 0.94±2.74 |     | 0.09±2.68 |     |     | 0.01±3.45 |     |     | 0.05±2.74 |     |
| DecisionTree       |     | 0.98±2.78 |     | 0.96±6.45 |     |     | 0.96±4.12 |     |     | 0.96±2.75 |     |
| XGboost            |     | 0.99±2.25 |     | 0.99±2.23 |     |     | 0.98±5.31 |     |     | 0.98±2.71 |     |
| Random_forest      |     | 0.98±2.26 |     | 0.98±2.75 |     |     | 0.93±4.12 |     |     | 0.96±2.14 |     |
| Na¨ıve_bayes       |     | 0.47±1.79 |     | 0.47±2.25 |     |     | 0.62±3.21 |     |     | 0.55±1.12 |     |
| CNNRPM             |     | 1.00–1.76 |     | 0.99–1.74 |     |     | 0.99–2.17 |     |     | 0.99–1.12 |     |
Fig.6 NumberofCPUcores
allocatedbydifferentschemes
learningrateof0.003fortheActornetwork,alearningrate parameters to alpha = 0.5, episodes = 64, verbose = 1,
of0.03fortheCriticnetwork,andadiscountfactorforthe and timesteps = 4000.
reward value in each action step. The DDPG code is • A2C (Advantage Actor-Critic) algorithm is a deep
implemented in Python 3.0 and deployed on the PyTorch reinforcement learning algorithm based on policy
framework.BoththeActorandCriticnetworksconsistof4 gradient, which uses the Actor-Critic framework. In
fully connected layers, each containing 40 neurons. The this framework, the Actor is responsible for learning a
activation function between layers is ReLU(), while the policy, that is, the probability distribution of selected
final layer uses Tanh() as the activation function. actions in a given state; The Critic is responsible for
We compared DDPG with PPO[32], A2C, auto scaling learning a value function, that is, to estimate the value
and reservation, the first two are another representative of a state or state-action pair. Set the parameters to
deep reinforcement methods. alpha = 0, episodes = 64, verbose = 1, and
|     |     |     |     |     | timesteps | = 4000. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ------- | --- | --- | --- | --- | --- |
• PPO(ProximalPolicyOptimization)isareinforcement
|     |     |     |     |     | • Autoscaler | (AC) | refers | to the | dynamic | allocation | of  |
| --- | --- | --- | --- | --- | ------------ | ---- | ------ | ------ | ------- | ---------- | --- |
learningalgorithmbasedonpolicygradients.Itupdates
|              |                      |                       |     |     | computing     | resources  |               | according   | to the  | current    | demand  |
| ------------ | -------------------- | --------------------- | --- | --- | ------------- | ---------- | ------------- | ----------- | ------- | ---------- | ------- |
| the strategy | through near-end     | strategy optimization |     | to  |               |            |               |             |         |            |         |
|              |                      |                       |     |     | or load       | of the     | system.       | Other       | metrics | that       | provide |
| achieve      | stable and efficient | training results.     | Set | the |               |            |               |             |         |            |         |
|              |                      |                       |     |     | microservices |            | for algorithm | scaling     |         | decisions  | include |
|              |                      |                       |     |     | cloud         | monitoring |               | metrics and | CPU     | and memory |         |
123

786 Page16of19 ClusterComputing(2025)28:786
Fig.7 Memoryallocatedby
differentschemes
utilization. By analyzing these metrics, the algorithm functionestimationtoimprovepolicyperformancethrough
scaling algorithm can make informed decisions about multiple iterations and simplified objectives. PPO effec-
expanding or reducing resources. tively balances exploration and exploitation in resource
• The resource reservation (RE) ensures the quality of allocation but may not explore sufficiently in high-dimen-
critical services by reserving some resources for high- sional continuous action spaces, and its use of historical
priority needs. The algorithm evaluates the current dataisnotasefficientasDDPG.Statistically,DDPGsaves
resource situation and the forecast of future demand, 22.8% of CPU resources compared to PPO.
dynamically adjusts the reservation strategy, and aims The A2C enhances data collection efficiency by gath-
to achieve efficient and fair resource allocation. ering experience in parallel with multiple threads and uses
the advantage function for policy updates to reduce vari-
In order to understand the advantages of DDPG in
ance. While A2C excels in handling massively parallel
improving resource utilization, ten groups of data were
environments, it is primarily suited for discrete action
selected according to different amounts of CPU, memory
spaces, limiting its application to continuous action space
andI/Oresourcesofmicroservicenodes,andDDPG,PPO,
resource allocation. In contrast, the DDPG, with its deter-
A2C, automatic scaling and reservation algorithms were
ministic strategy and offline learning characteristics, is
used to allocate CPU cores and memory for each
more suitable for high-dimensional continuous action
microservice, as shown in Figs. 6 and 7.
space resource allocation, with a CPU utilization 24.52%
As illustrated in the Fig. 6, AC shows great resource
higher than A2C.
wastage compared to DDPG, allocating roughly twice as
Figure 7 reveals a detailed analysis of the memory
many CPU cores on average. This is mainly due to its
allocation by DDPG versus the baselines throughout the
failure to adapt to the dynamic resource demands of
entire testing. As depicted in Fig. 6, on average, DDPG
microservice nodes. RE can allocate CPU cores and
outperforms the PPO, A2C, AC, and RE by conserving
memory flexibly based on changing requirements, but it
21.91%, 29.27%, 55.43%, and 74.39% of memory
still results in noticeable waste compared to DDPG. The
resources, respectively, with a peak saving of up to
CPU utilization of the DDPG algorithm is 38.32% higher
80.82%.
than that of RE, primarily because it allocates resources
In summary, in comparison to PPO, A2C, algorithm
based on the last peak demand.
scaling, and reservation algorithms, DDPG demonstrates
Experimental results indicate that both the PPO and
superior capability in effectively allocating CPU and
A2C algorithmsoutperformACandREinCPUallocation
memory demonstrates superior capability in effectively
but are still slightly less effective than the DDPG algo-
allocating CPU and memory resources.
rithm. PPO constrains policy updates by clipping the
Furthermore, to verify if DDPG can improve resource
probability ratio to avoid instability from excessive
utilization while ensuring QoS, we further evaluated the
updates, combining strategy gradient methods with value
response time of microservice, and give details in Fig. 8.
123

| ClusterComputing(2025)28:786 |     |     |     |     |     |     |     |     |     |     |     | Page17of19 |     | 786 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
Fig.8 Theaverageresponse
timeofdifferentschemes
|     |     |     |     |     |     |     | effectively                | conserve  |             | the server’s     |                             | CPU           | and        | memory   |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --------- | ----------- | ---------------- | --------------------------- | ------------- | ---------- | -------- |
|     |     |     |     |     |     |     | resources.Therefore,inreal |           |             |                  | situations,usersshouldweigh |               |            |          |
|     |     |     |     |     |     |     | the relationship           |           | between     |                  | the allocation              |               | efficiency | of       |
|     |     |     |     |     |     |     | resources                  | and       | the time    | efficiency       | of                          | the           | allocation | algo-    |
|     |     |     |     |     |     |     | rithm to                   | make      | the optimal | choice.          |                             |               |            |          |
|     |     |     |     |     |     |     | 5 Conclusion               |           | and         | discussion       |                             |               |            |          |
|     |     |     |     |     |     |     | In this paper,             |           | we propose  | a                | CNN-based                   | adaptive      |            | resource |
|     |     |     |     |     |     |     | allocation                 | framework |             | for cloud-native |                             | architectures |            | that     |
Fig.9 Theaverageresponsetimeofdifferentschemes
|              |                                          |              |          |         |       |           | dynamically         | adjusts             | system       |        | resources   | including |              | CPU and |
| ------------ | ---------------------------------------- | ------------ | -------- | ------- | ----- | --------- | ------------------- | ------------------- | ------------ | ------ | ----------- | --------- | ------------ | ------- |
|              |                                          |              |          |         |       |           | memory              | of microservice     |              | nodes. | Extensive   |           | experimental |         |
| Figure       | 8showstheresponsetimeofmicroservicenodes |              |          |         |       |           |                     |                     |              |        |             |           |              |         |
|              |                                          |              |          |         |       |           | results demonstrate |                     | that         | our    | proposed    | method    | reduce       | CPU     |
| in different | schemes,                                 |              | and Fig. | 9 shows | the   | average   |                     |                     |              |        |             |           |              |         |
|              |                                          |              |          |         |       |           | consumption         |                     | by 22.8%     | and    | memory      | usage     | by           | 21.91%  |
| response     | time of                                  | microservice | nodes.   | When    | the   | response  |                     |                     |              |        |             |           |              |         |
|              |                                          |              |          |         |       |           | compared            | to state-of-the-art |              |        | baselines.  |           |              |         |
| time of      | microservice                             | nodes        | is lower | than    | 1 ms, | it proves |                     |                     |              |        |             |           |              |         |
|              |                                          |              |          |         |       |           | While               | CPRAM               | demonstrates |        | significant |           | improvements |         |
thattheallocatedmicroserviceresourcesaretoomanyand
inresourceallocationandQoSguaranteesforcloud-native
thereisawasteofresources.Whentheresponsetimeofthe
|                                |     |     |     |                    |     |     | microservices, |     | it is not | without | limitations. |     | Firstly,     | the |
| ------------------------------ | --- | --- | --- | ------------------ | --- | --- | -------------- | --- | --------- | ------- | ------------ | --- | ------------ | --- |
| microservicenodeisbetween1and5 |     |     |     | ms,itprovesthatthe |     |     |                |     |           |         |              |     |              |     |
|                                |     |     |     |                    |     |     | performance    | of  | CPRAM     | relies  | heavily      | on  | the accuracy | of  |
resourcesallocatedcanjustmeettheresourcerequirements
|                |                  |               |             |               |              |           | the CNN-based |            | prediction |            | model.       | Although     | CNNs           | are       |
| -------------- | ---------------- | ------------- | ----------- | ------------- | ------------ | --------- | ------------- | ---------- | ---------- | ---------- | ------------ | ------------ | -------------- | --------- |
| of the current | microservice     |               | node.       | When          | the response | time      |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | robust to     | sparse     | and        | incomplete | data,        | their        | effectiveness  |           |
| is greater     | than 5           | ms, it proves | that        | the resources |              | allocated |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | may degrade   |            | in highly  | dynamic    |              | environments |                | where     |
| to the         | microservice     | node          | are         | insufficient  | to           | meet the  |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | resource      | usage      | patterns   | change     | abruptly     | or           | unpredictably. |           |
| resource       | requirements     | of            | the current |               | node,        | and more  |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | Secondly,     | the        | DDPG-based |            | resource     | allocation   |                | mecha-    |
| resources      | need to          | be allocated  | to          | it.           |              |           |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | nism, while   | effective, |            | involves   | a relatively |              | high           | computa-  |
| From           | the experimental |               | results     | we can        | see that     | DDPG is   |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | tional cost   | during     | the        | training   | phase.       | This         | could          | limit its |
| not always     | optimal          | in            | terms of    | response      | time         | and the   |               |            |            |            |              |              |                |           |
|                |                  |               |             |               |              |           | applicability | in         | real-time  | scenarios  |              | where        | rapid          | decision- |
averageresponsetimeissecondonlytoPPO.Thisisdueto
makingiscritical.Althoughwehaveoptimizedthetraining
| the fact      | that DDPG | employs   | actor-critic, |     | a dual-network |           |           |          |            |     |              |            |            |     |
| ------------- | --------- | --------- | ------------- | --- | -------------- | --------- | --------- | -------- | ---------- | --- | ------------ | ---------- | ---------- | --- |
|               |           |           |               |     |                |           | process   | by using | techniques |     | such as      | experience | replay     | and |
| architecture, | which     | is higher | in complexity |     | than           | any other |           |          |            |     |              |            |            |     |
|               |           |           |               |     |                |           | minibatch | updates, | further    |     | improvements |            | are needed | to  |
methods.However,fromtheexperimentalresultspresented
|          |          |     |         |           |     |            | reduce   | the training | time      | and | computational |        | complexity.   |     |
| -------- | -------- | --- | ------- | --------- | --- | ---------- | -------- | ------------ | --------- | --- | ------------- | ------ | ------------- | --- |
| in Figs. | 6 and 7, | we  | can see | that DDPG |     | is able to |          |              |           |     |               |        |               |     |
|          |          |     |         |           |     |            | Thirdly, | CPRAM        | currently |     | focuses       | solely | on optimizing |     |
123

786 Page18of19 ClusterComputing(2025)28:786
latency as the primary QoS metric. While latency is a on Operating Systems Design and Implementation. 2020, USE-
critical factor in many cloud-native applications, other NIXAssociation.p.Article46.
7. Guo, Y., Liu, F., Xiao, N., et al.: PARA: Performability-aware
metrics such as throughput, energy consumption, and cost
resource allocation on the edges for cloud-native services. Int.
efficiency are also important in practical scenarios. J.Intell.Syst.37(11),8523–8547(2022)
For the future, we plan to explore multi-agent collabo- 8. Moghaddam, S.K., Buyya, R., Ramamohanarao, K.: Perfor-
rative learning to investigate how local decisions from mance-aware management of cloud resources: a taxonomy and
futuredirections.ACMComput.Surv.52(4),Article84(2019)
individual agents can be efficiently integrated to optimize
9. Liao,T.-L.,Peng,C.-Y.,Hou,Y.-Y.:Applicationofmulti-party
global resource allocation. Additionally, we will incorpo- computation and error correction with image enhancement and
rate online learning techniques to dynamically update the convolution neural networks based on cloud computing. IET
parameters of the reinforcement learning algorithm, ImageProc.17(6),1931–1950(2023)
10. Yang, J., Wang, Y., Li, Z.: Inverse order based optimization
enabling the framework to adapt to evolving software and
methodfortaskoffloadingandresourceallocationinmobileedge
hardware environments in real time. computing.Appl.SoftComput.116,108361(2022)
11. Gan,Y.,Zhang,Y.,Cheng,D.,etal.:Anopen-sourcebenchmark
suiteformicroservicesandtheirhardware-softwareimplications
forcloud&edgesystems.In:ProceedingsoftheTwenty-Fourth
Author contributions Yu Peng was responsible for proposing the
International Conference on Architectural Support for Program-
proposal,performingtheexperimentalvalidation,andthewritingpart
mingLanguagesandOperatingSystems.pp.3–18(2019)
of the paper. Jia Hao was responsible for proofreading. Yang Chen
12. Rzadca,K.,Findeisen, P.,Swiderski,J.,etal.:Autopilot: work-
wasresponsibleforwritingtheexperimentalpart,andJianhouGanis
load autoscaling at Google. In: Proceedings of the Fifteenth
responsibleforreviewingthefullpaper.
EuropeanConferenceonComputerSystems.pp.1–16(2020)
13. Zhang,Y.,Hua,W.,Zhou,Z.,etal.:Sinan:ML-basedandQoS-
Funding ThisworkissupportedbyYunnanInternationalJointR&D
aware resource management for cloud microservices. In: Pro-
Center of China-Laos-Thailand Educational Digitalization
ceedings of the 26th ACM International Conference on Archi-
(202203AP140006), Youth Project of Applied Basic Research Pro-
tectural Support for Programming Languages and Operating
gram of Yunnan Province (No. 202201AU070050), Key Project of
Systems.pp.167–181(2021)
Applied Basic Research Program of Yunnan Province (No.
14. Crankshaw,D.,Wang,X.,Zhou,G.,etal.:Clipperalow-latency
202201AS070021),TalentDevelopmentProgramforYunnan-Youth
onlinepredictionservingsystem.Comput.Sci.(2017)
TalentProject.
15. Joseph, C.T., Chandrasekaran, K.: Nature-inspired resource
management and dynamic rescheduling of microservices in
Data availability No datasets were generated or analysed during the
Clouddatacenters.Concurr.Comput.Pract.Exp.(2021).https://
currentstudy.
doi.org/10.1002/cpe.6290
16. Erdei, R., Toka, L.: Minimizing resource allocation for cloud-
Declarations nativemicroservices.J.Netw.Syst.Manage.31(2),35(2023)
17. Khan, T.M.G., Taheri, J., Al-Dulaimy, K.A.: PerfSim: a perfor-
mance simulator for cloud native microservice chains. IEEE
Conflictofinterest Theauthorsdeclarenocompetinginterests. Trans.CloudComput.11(2),1395–1413(2023)
18. Byeonghui, J., Jueun, J., Young-Sik, J.: Proactive resource
Ethicalapproval Notapplicable.
autoscalingschemebasedonSCINetforhigh-performancecloud
computing. IEEE Trans. Cloud Comput. 11(4), 3497–3509
(2023)
References 19. Masouros,D.,Xydis,S.,Soudris,D.:Rusty:runtimeinterference-
aware predictive monitoring for modern multi-tenant systems.
IEEETrans.ParallelDistrib.Syst.32(1),184–198(2021)
1. Kratzke, N., Quint, P.-C.: Understanding cloud-native applica-
20. Zhang, Y., Zhou, Z., Elnikety, S., Delimitrou, C.: Analytically-
tions after 10 years of cloud computing—a systematic mapping
driven resource management for cloud-native microservices.
study.J.Syst.Softw.126,1–16(2017)
Comput.Sci.(2024)
2. SotiriadisNathanCruzCoulsonSteliosandBessisNik:Adaptive
21. Wang,Z.,Li,P.,Liang,C.-J.M.,etal.:Autothrottle:apractical
microservice scaling for elastic applications. IEEE Internet
bi-level approach to resource management for SLO-targeted
ThingsJ.7(5),4195–4202(2020)
microservices.Comput.Sci.(2022)
3. Fu, K., Zhang, W., Chen, Q., et al.: Adaptive resource efficient
22. Shutian,L.,Chenyu,L.,Kejiang,Ye.,etal.:Optimizingresource
microservicedeploymentincloud-edgecontinuum.IEEETrans.
managementforsharedmicroservices:ascalablesystemdesign.
ParallelDistrib.Syst.33(8),1825–1840(2022)
ACMTrans.Comput.Syst.42(1–2),1–28(2024)
4. Chouliaras, S., Sotiriadis, S.: Real-time anomaly detection of
23. Chen, S., Delimitrou, C., and Mart´ınez, J.F.: PARTIES: QoS-
NoSQL systems based on resource usage monitoring. IEEE
aware resource partitioning for multiple interactive services. In:
Trans.Industr.Inf.16(9),6042–6049(2020)
Proceedings of the twenty-fourth international conference on
5. Bhardwaj, R., Kandasamy, K., Biswal, A., et al.: Cilantro: per-
architectural support for programming languages and operating
formance-aware resource allocation for general objectives via
systems.AssociationforComputingMachinery:Providence,RI,
onlinefeedback.In:USENIXSymposiumonOperatingSystems
USA.pp.107–120(2019)
DesignandImplementation.(2023)
24. Guo,H.,Cao,H.,He,J.,etal.:POBO:Safeandoptimalresource
6. Qiu,H.,Banerjee,S.S.,Jha,S.,etal.:FIRM:anintelligentfine-
management for cloud microservices. Perform. Evaluat. 162,
grained resource management framework for SLO-oriented
102376(2023)
microservices. In:Proceedingsofthe14thUSENIXConference
123

| ClusterComputing(2025)28:786 |     |     |     |     |     |     |     |     | Page19of19 |     | 786 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
25. Kim,A.,Lee,J.,Kim,M.:Resourcemanagementmodelbasedon
YuPengbornin2000,received
| cloud | computing | environment. |     | Int. | J. Distrib. | Sensor | Netw. |         |        |          |      |
| ----- | --------- | ------------ | --- | ---- | ----------- | ------ | ----- | ------- | ------ | -------- | ---- |
|       |           |              |     |      |             |        |       | her B.S | degree | from the | Guiz |
12(11),550147716676554(2016)
|             |      |              |     |         |              |     |           | hou Minzu | University. |     | Cur |
| ----------- | ---- | ------------ | --- | ------- | ------------ | --- | --------- | --------- | ----------- | --- | --- |
| 26. Baarzi, | A.F. | and Kesidis, | G.: | SHOWAR: | right-sizing |     | and effi- |           |             |     |     |
rently,sheisamasterstudentin
| cient     | scheduling | of microservices. |            | In:         | Proceedings |     | of the ACM |                 |        |        |         |
| --------- | ---------- | ----------------- | ---------- | ----------- | ----------- | --- | ---------- | --------------- | ------ | ------ | ------- |
|           |            |                   |            |             |             |     |            | the Information |        | School | of Sci- |
| Symposium | on         | Cloud             | Computing. | Association |             | for | Computing  |                 |        |        |         |
|           |            |                   |            |             |             |     |            | ence in         | Yunnan | Normal | Uni-    |
Machinery:Seattle,WA,USA.pp.427–441(2021)
|               |     |             |          |             |       |          |           | versity. | Her research    |     | interest |
| ------------- | --- | ----------- | -------- | ----------- | ----- | -------- | --------- | -------- | --------------- | --- | -------- |
| 27. Nawrocki, | P., | Grzywacz,   | M.,      | Sniezynski, | B.:   | Adaptive | resource  |          |                 |     |          |
|               |     |             |          |             |       |          |           | covers   | cloud computing |     | and      |
| planning      | for | cloud-based | services |             | using | machine  | learning. |          |                 |     |          |
edgecomputing.
J.ParallelDistrib.Comput.152,88–97(2021)
| 28. Panwar, | R., | Supriya, | M.: Dynamic |     | resource | provisioning | for |     |     |     |     |
| ----------- | --- | -------- | ----------- | --- | -------- | ------------ | --- | --- | --- | --- | --- |
service-basedcloudapplications:ABayesianlearningapproach.
J.ParallelDistrib.Comput.168,90–107(2022)
29. Kumar,R.A.,Kartheeban,K.:Resourceallocationusingdynamic
pricingauctionmechanismforsupportingemergencydemandsin
| cloud | computing. | J.  | Parallel | Distrib. | Comput. | 158, | 213–226 |     |     |     |     |
| ----- | ---------- | --- | -------- | -------- | ------- | ---- | ------- | --- | --- | --- | --- |
(2021)
JiaHaoreceivedtheMS.D.and
| 30. Yoon, | J., Zhang, | Y., | Jordon, | J., et | al.: VIME: | extending | the |     |     |     |     |
| --------- | ---------- | --- | ------- | ------ | ---------- | --------- | --- | --- | --- | --- | --- |
Ph.D.incomputersciencefrom
successofself-andsemi-supervisedlearningtotabulardomain.
|     |     |     |     |     |     |     |     | Wuhan | University | of Technol- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ----------- | --- |
In:NeuralInformationProcessingSystems(2020)
|            |            |     |          |         |        |                 |     | ogy and | Yunnan | University | in  |
| ---------- | ---------- | --- | -------- | ------- | ------ | --------------- | --- | ------- | ------ | ---------- | --- |
| 31. Bahri, | D., Jiang, | H., | Tay, Y., | et al.: | SCARF: | Self-Supervised |     |         |        |            |     |
2015and2020respectively.She
| Contrastive             | Learning |         | using Random  |     | Feature     | Corruption. | CoRR,  |              |            |           |       |
| ----------------------- | -------- | ------- | ------------- | --- | ----------- | ----------- | ------ | ------------ | ---------- | --------- | ----- |
|                         |          |         |               |     |             |             |        | is currently | a lecturer |           | and a |
| (2021).arxiv:2106.15147 |          |         |               |     |             |             |        | postdoctoral | research   | fellow    | in    |
| 32. Schulman,           | J.,      | Wolski, | F., Dhariwal, |     | P., et al., | Proximal    | Policy |              |            |           |       |
|                         |          |         |               |     |             |             |        | the Minister | of         | Education | at    |
OptimizationAlgorithms.ArXiv,(2017).arxiv:1707.06347.
|             |        |                |     |             |     |          |           | Yunnan    | Normal  | University,  |      |
| ----------- | ------ | -------------- | --- | ----------- | --- | -------- | --------- | --------- | ------- | ------------ | ---- |
| 33. Aslani, | A.,    | Ghobaei-Arani, |     | M.: Machine |     | learning | inference |           |         |              |      |
|             |        |                |     |             |     |          |           | Kunming,  | China.  | Her research |      |
| serving     | models | in serverless  |     | computing:  | a   | survey.  | Computing |           |         |              |      |
|             |        |                |     |             |     |          |           | interests | include | massive      | data |
107,47(2025).https://doi.org/10.1007/s00607-024-01377-9
analysis,uncertaintyinartificial
34. Ghorbian,M.,Ghobaei-Arani,M.,Esmaeili,L.:Asurveyonthe
|            |            |     |               |     |            |     |           | intelligence, | cloud | computing, |     |
| ---------- | ---------- | --- | ------------- | --- | ---------- | --- | --------- | ------------- | ----- | ---------- | --- |
| scheduling | mechanisms |     | in serverless |     | computing: | a   | taxonomy, |               |       |            |     |
andedgecomputing.
| challenges, | and | trends. | Clust. | Comput. | 27, | 5571–5610 | (2024). |     |     |     |     |
| ----------- | --- | ------- | ------ | ------- | --- | --------- | ------- | --- | --- | --- | --- |
https://doi.org/10.1007/s10586-023-04264-8
| 35. Ghorbian, | M.,           | Ghobaei-Arani, |     | M.: Function |         | offloading | approa- |          |           |        |       |
| ------------- | ------------- | -------------- | --- | ------------ | ------- | ---------- | ------- | -------- | --------- | ------ | ----- |
|               |               |                |     |              |         |            |         | Yang     | Chen born | in     | 1997, |
| ches          | in serverless | computing:     |     | a survey.    | Comput. | Electric.  | Eng.    |          |           |        |       |
|               |               |                |     |              |         |            |         | received | his B.S   | degree | from  |
120(1),109832(2024)
|            |         |            |        |     |        |       |         | the Southwest | Petroleum |     | Uni- |
| ---------- | ------- | ---------- | ------ | --- | ------ | ----- | ------- | ------------- | --------- | --- | ---- |
| 36. Anisha | kumari, | Bibhudatta | Sahoo, | and | Ranjan | Kumar | Behera. |               |           |     |      |
versity.Currently,heisamaster
| Mitigating | cold-start |     | delay | using     | warm-start | containers | in       |         |            |             |     |
| ---------- | ---------- | --- | ----- | --------- | ---------- | ---------- | -------- | ------- | ---------- | ----------- | --- |
|            |            |     |       |           |            |            |          | student | in the     | Information |     |
| serverless | platform.  | In  | 2022  | IEEE 19th | India      | Council    | Interna- |         |            |             |     |
|            |            |     |       |           |            |            |          | School  | of Science | in Yunnan   |     |
tionalConference(INDICON),pp.1–6.IEEE,2022.
NormalUniversity.Hisresearch
interestcoverscloudcomputing
Publisher’s Note Springer Nature remains neutral with regard to andedgecomputing.
jurisdictionalclaimsinpublishedmapsandinstitutionalaffiliations.
SpringerNatureoritslicensor(e.g.asocietyorotherpartner)holds
exclusiverightstothisarticleunderapublishingagreementwiththe
| author(s) | or other | rightsholder(s); |     | author | self-archiving |     | of the |     |     |     |     |
| --------- | -------- | ---------------- | --- | ------ | -------------- | --- | ------ | --- | --- | --- | --- |
acceptedmanuscriptversionofthisarticleissolelygovernedbythe
termsofsuchpublishingagreementandapplicablelaw.
123