This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
IEEETRANSACTIONSONSERVICESCOMPUTING 1
SynScale: Spatiotemporal Collaborative Autoscaling
for Microservices in Edge-Clouds
Haogang Tong, Chunyang Meng, Shijie Song, Maolin Pan, Yang Yu*
Abstract—Edge-cloudenvironmentsconstituteaheterogeneous limitations of centralized cloud architectures. The synthesis
computing paradigm that integrates resource-constrained edge of these approaches, known as edge-cloud computing, strate-
serverswithhigh-performancecloudservers.Whilemicroservices
gically leverages the strengths of both paradigms, offering
have revolutionized large-scale applications development by en-
a hybrid solution that balances the proximity and real-time
hancingscalabilityandflexibility,achievingefficientmicroservice
autoscaling—the dynamic adjustment of instances to maintain processingcapabilitiesofedgedeviceswiththescalabilityand
qualityofservice(QoS)andmeetservice-levelagreements(SLA) extensive resources of cloud infrastructure.
targets—remainschallenginginsuchenvironments.Mostexisting Concurrently, the field of software engineering has wit-
autoscalingtechniquesrelyonmetricforecastingandcentralized
nessed a significant architectural evolution with the rise of
orper-nodecontrol,causingthemtooverlooktemporalevolution
microservices. This approach deconstructs monolithic appli-
and server relationships and resulting in unstable and weakly
coordinated scaling. To address these challenges, we present cations into smaller, independently deployable services, of-
SynScale, a distributed collaborative autoscaling framework fering enhanced modularity, scalability, and maintainability
that strengthens both temporal sensitivity and structural coor- [3]. The adoption of microservices has been facilitated by
dination. SynScale introduces a spatiotemporal representation
advancementsincontainerizationtechnologiessuchasDocker,
module that couples a temporal attention network with a multi-
orchestration platforms like Kubernetes, and serverless com-
graph convolutional model. The temporal component distills
behavioral trends from recent observations to ensure coherent putingframeworks.Thesetechnologieshavecollectivelyrede-
responsestotime-varyingdynamics,whilethespatialcomponent fined the landscape of software deployment and management.
performs relational reasoning over explicitly modeled inter- The convergence of edge-cloud computing and microservices
server correlations to yield structure-aware representations that
architectures has given rise to novel deployment strategies,
support effective cross-node coordination. These spatiotemporal
where microservice instances are distributed across the edge-
embeddings are then used within a multi-agent reinforcement
learning paradigm, enabling distributed agents to generate cloud continuum [4], [5]. This approach aims to optimize
context-awarescalingdecisionsthatalignlocaladaptabilitywith request response times by leveraging on-site processing ca-
system-wide efficiency. Experimental evaluations against state- pabilities.
of-the-art autoscaling techniques show that SynScale reduces
To accommodate the fluctuating request arrival rates in
average response time by 59.32%, SLA violations by 85.71%,
edge-cloud environments, the dynamic deployment of mi-
and P95 latency by 73.2%, while also lowering resource cost. It
further improves scaling stability—reflected by lower instance- croserviceinstancesacrossheterogeneousservers(i.e.,servers
time and longer instance lifetimes—and maintains lightweight, with varying computational, memory, and storage capacities)
scale-stable runtime overhead, ensuring practical deployability is essential. This process, known as microservice autoscaling,
in heterogeneous edge-cloud environments.
adapts to the time-varying workload demands. However, the
Index Terms—Microservice Autoscaling, Edge-cloud Environ- challengesposedbygeographicallyuneventrafficpatternsand
ment, Quality of Service, Service-Level Agreements, Graph the inherent resource heterogeneity across servers make the
Convolutional Network, Multi-Agent Reinforcement Learning.
application of traditional autoscaling methods increasingly in-
adequate. The following analysis delves into these challenges
I. INTRODUCTION in more detail.
Challenge 1: Scaling Under Spatiotemporal Dynamics
Inrecentyears,theproliferationofInternetofThings(IoT)
and System Heterogeneity. Edge-cloud environments are
devices and latency-sensitive applications has precipitated a
inherently dynamic and heterogeneous. On one hand, user
paradigm shift in distributed computing architectures [1].
mobility and regional activity patterns introduce spatiotem-
Traditionalcloudcomputingmodels,whileofferingsubstantial
poral workload fluctuations that result in server-specific and
computational power, often fall short in meeting the stringent
time-varyingresourcedemands.Ontheotherhand,thediverse
latency requirements imposed by these emerging use cases
resource capacities and deployment conditions across edge
[2]. This limitation has catalyzed the ascendance of edge
and cloud servers further compound this complexity, creating
computing as a complementary paradigm. Edge computing,
a highly non-uniform operational landscape. To substanti-
by bringing computational resources closer to data sources
ate this, we analyze the Shanghai Telecom dataset [6]–[8],
and end-users, presents a compelling solution to the inherent
which includes millions of records from over 9,000 mobile
Haogang Tong, Chunyang Meng, Shijie Song are with the School of users across 3,000+ base stations. Our analysis reveals clear
Computer Science and Engineering, Sun Yat-sen University, Guangzhou, temporal variations and geographical disparities in request
China (email:{tonghg,mengchy3,songshj6}@mail2.sysu.edu.cn). Yang Yu
intensity, confirming that each server faces unique, evolving
and Maolin Pan are professors at the School of Software Engineering, Sun
Yat-senUniversity,Zhuhai,China(email:{panml,yuy}@mail.sysu.edu.cn). load patterns.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     | 2   |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Most existing autoscaling approaches [9]–[11] focus on trend-awarecontextualrepresentationsfromhistoricalob-
forecasting individual metrics such as workload or resource servations, enabling the policy to perceive evolving be-
utilization to trigger proactive scaling. While effective for havioral patterns and make temporally consistent scaling
short-termadjustments,theseprediction-drivendesignsignore decisions, while the spatial component performs graph-
the evolving temporal interplay between system states and based relational reasoning over explicitly modeled inter-
scaling decisions, leading to context-insensitive and unstable server relationships to yield structure-aware representa-
adaptation.Theyalsoremainheavilydata-dependent,requiring tions that enhance distributed coordination.
largevolumesofaccuratetrainingdatatogeneratereliablepre- Wedevelopadistributedcollaborativeautoscalingframe-
•
dictions, and their forecast-oriented modeling fails to capture work in which multiple agents jointly optimize scaling
the multi-faceted dynamics of autoscaling. As a result, these policies to balance local adaptability and global QoS
limitations confine autoscalers to narrow, prediction-oriented objectives. This design effectively leverages system het-
adaptation, preventing them from leveraging historical cues erogeneity and improves computational efficiency and
| and system-wide |     | dynamics | to  | make | trend-aware | and | tempo- | scalability. |     |     |     |     |     |     |
| --------------- | --- | -------- | --- | ---- | ----------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- |
rally consistent decisions under continuously changing condi- We construct realistic, geographically distributed work-
•
tions. Meanwhile, traditional rule-based approaches [12]–[14] loads using real-world data and conduct comprehensive
are inherently inflexible—either relying on globally defined empirical evaluations against state-of-the-art methods.
thresholds that ignore local conditions, or requiring per-server Our results demonstrate substantial improvements in re-
configurationsthatarelabor-intensiveandpoorlycoordinated. sponse time, SLA adherence, and resource efficiency,
Even reinforcement learning (RL)-based methods [15]–[18] reinforcing the effectiveness and scalability of our ap-
| often adopt   | monolithic    |           | control     | structures | that               | encode | system-    | proach.    |      |     |             |     |     |     |
| ------------- | ------------- | --------- | ----------- | ---------- | ------------------ | ------ | ---------- | ---------- | ---- | --- | ----------- | --- | --- | --- |
| wide states   | but           | lack the  | granularity | to         | reflect individual |        | server     |            |      |     |             |     |     |     |
|               |               |           |             |            |                    |        |            |            |      | II. | RELATEDWORK |     |     |     |
| dynamics.     | As            | a result, | these       | approaches | struggle           |        | to deliver |            |      |     |             |     |     |     |
|               |               |           |             |            |                    |        |            | A. Related | Work |     |             |     |     |     |
| fine-grained, | context-aware |           | scaling     | decisions  |                    | under  | dynamic,   |            |      |     |             |     |     |     |
heterogeneous conditions. The domain of microservice autoscaling has witnessed
Challenge 2: Lack of Coordination Across Distributed significant research momentum in recent years. This section
Resources. Beyond the need for local adaptability, effective presents a comprehensive review of microservice autoscaling
| autoscaling | in  | edge-cloud | environments |     | also | demands | coor- |                      |     |      |                         |     |             |     |
| ----------- | --- | ---------- | ------------ | --- | ---- | ------- | ----- | -------------------- | --- | ---- | ----------------------- | --- | ----------- | --- |
|             |     |            |              |     |      |         |       | studies, categorized |     | into | distinct methodological |     | approaches. |     |
dination across geographically distributed and functionally Rule-based autoscaling methods [19]–[29] rely on pre-
interdependent servers. Microservices are often deployed as defined thresholds for scaling decisions based on monitored
collaborative service chains, where multiple instances interact resource metrics. These methods are favored for their sim-
across servers to fulfill a single request. Their performance plicity and low computational overhead, making them suit-
| is thus not | solely | determined |     | by individual |     | server | capacity, |          |                      |     |               |     |          |      |
| ----------- | ------ | ---------- | --- | ------------- | --- | ------ | --------- | -------- | -------------------- | --- | ------------- | --- | -------- | ---- |
|             |        |            |     |               |     |        |           | able for | resource-constrained |     | environments. |     | However, | they |
but by the efficiency of inter-server cooperation—including are inherently limited by their static nature, often failing
proximity, placement, and traffic migration. to adapt to dynamic and unpredictable environments. Pre-
| However, | most | existing | methods |     | [15], | [16], [18] | treat |                     |     |         |           |           |         |     |
| -------- | ---- | -------- | ------- | --- | ----- | ---------- | ----- | ------------------- | --- | ------- | --------- | --------- | ------- | --- |
|          |      |          |         |     |       |            |       | dictive autoscaling |     | methods | [9]–[11], | [30]–[33] | attempt | to  |
servers as independent units and rely solely on local perfor- mitigate the reactivity limitations of rule-based methods by
mance metrics such as CPU or memory usage. These metrics forecasting future resource demands based on historical data.
provide no insight into the structural relationships between While these methods can reduce scaling latency and improve
servers, such as functional similarity, communication affinity, performance,theyaredata-dependent,requiringlargevolumes
| or migration | tendencies. |     | Consequently, |     | scaling | decisions | are |             |          |      |             |          |              |     |
| ------------ | ----------- | --- | ------------- | --- | ------- | --------- | --- | ----------- | -------- | ---- | ----------- | -------- | ------------ | --- |
|              |             |     |               |     |         |           |     | of accurate | training | data | to generate | reliable | predictions. |     |
made in isolation, leading to redundant actions, cross-server Furthermore, their time modeling remains inherently forecast-
bottlenecks, and underutilized synergy potential. Without ex- oriented—treating temporal information merely as input fea-
plicit modeling and utilization of inter-server correlations, turesforvalueprediction—thusfailingtocapturetheevolving
current approaches fail to achieve collaborative efficiency in behavioralcontextthatlinkspastsystemchangeswithscaling
| distributed | autoscaling. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
behavior.Asaresult,theylacktemporalawarenessindecision
Contribution. To address the above limitations and realize making, often leading to inconsistent or short-sighted scaling
coordinated, temporally consistent autoscaling, we make the under continuously changing conditions. Both rule-based and
following contributions: predictive methods fail to leverage inter-server dependencies,
We establish a structured modeling approach for diverse making them unsuitable for collaborative scaling across dis-
•
| inter-server |     | relationships |     | by explicitly |     | defining | hetero- |          |               |     |     |     |     |     |
| ------------ | --- | ------------- | --- | ------------- | --- | -------- | ------- | -------- | ------------- | --- | --- | --- | --- | --- |
|              |     |               |     |               |     |          |         | tributed | environments. |     |     |     |     |     |
geneous correlations across multiple resource attributes. Machine learning (ML)-based methods [28], [34]–[39]
This enables a more precise and adaptive representa- have been employed to dynamically adjust scaling actions
tion of inter-server dependencies, facilitating informed by learning from historical data and identifying patterns in
decision-making and cooperative resource allocation in resource utilization. These methods can adapt to a broader
distributed environments. rangeofscenarios,buttheyareheavilyreliantonlargedatasets
• Wedesignaspatiotemporalrepresentationlearningmech- and accurate labeling, which can be difficult to obtain in
anism that integrates a temporal attention network with complex, heterogeneous systems. Moreover, the generaliza-
multi-graphconvolution.Thetemporalcomponentdistills tion capabilities of these models are often limited, especially
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     |     |     | 3   |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a) 0:00-6:00 (b) 6:00-12:00 (c) 12:00-18:00 (d) 18:00-24:00 (e) the total volume of requests
|     |     | Fig. | 1: Time-Varying | and | Geographically | Unevenly | Distributed | Workload |     |     |     |     |
| --- | --- | ---- | --------------- | --- | -------------- | -------- | ----------- | -------- | --- | --- | --- | --- |
when encountering novel environments or workload shifts Rule- and prediction-based methods [9], [48], [49] typically
not present in the training data. Despite these challenges, operate on statically configured, globally tuned thresholds
ML-based methods have shown promise in offering scenario- (e.g., CPU utilization or queue length). Such one-size-fits-all
specific autoscaling solutions tailored to observed conditions. heuristics lack the flexibility to accommodate server-specific
Reinforcement learning (RL)-based approaches [16]– variations, resulting in limited contextual precision and re-
[18], [40]–[46] represent a significant departure from rule- duced responsiveness in dynamic environments. (ii) Central-
based and predictive methods by continuously learning and ized RL approaches [16], [17], [40], [50] encode system-wide
optimizingpoliciesthroughinteractionswiththeenvironment. information into a monolithic global state representation and
These methods are well-suited for dynamic environments learn a unified policy for all servers. This design (a) suffers
where data is sparse and workloads are highly variable. How- from scalability issues due to exponential state-space growth
ever, monolithic policy models used in most RL approaches as server count increases, (b) tightly couples the learned
tend to overlook the heterogeneity of individual servers and policy to a fixed environment size, and (c) fails to account
inter-server synergies, often leading to inefficient scaling ac- for heterogeneity across servers, leading to uniform decisions
tions and increased computational overhead. thatareill-suitedfordistributed,diverseconditions.Moreover,
| Recently, | a few studies | have | explored | the integration | of  |             |             |               |     |           |          |      |
| --------- | ------------- | ---- | -------- | --------------- | --- | ----------- | ----------- | ------------- | --- | --------- | -------- | ---- |
|           |               |      |          |                 |     | the lack of | an explicit | collaboration |     | mechanism | prevents | such |
graphconvolutionalnetworks(GCNs)intoRL-basedautoscal- methodsfromexploitingthecomplementarycapacitiesofedge
| ing to capture | service | dependencies |     | [15], [47]. | These ap- | nodes. |     |     |     |     |     |     |
| -------------- | ------- | ------------ | --- | ----------- | --------- | ------ | --- | --- | --- | --- | --- | --- |
proaches enhance the feature representation of system states These limitations motivate a shift toward decentralized
by incorporating structural information among microservices. yet collaborative autoscaling—exemplified by our proposed
Whilepromising,suchmethodstypicallyassumestaticservice
|     |     |     |     |     |     | SynScale—which |     | learns server-specific |     | scaling | policies | that |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------------- | --- | ------- | -------- | ---- |
interaction graphs or topology-based adjacency, and often arelocallyadaptivewhilesupportinglightweightcoordination
failtomodelserver-levelcollaborativerelationshipsexplicitly, across the system.
limiting their ability to fully exploit cross-server synergies in Insight 2: Beyond Isolated Scaling: Graph-Based Re-
heterogeneous environments. lational Modeling for Collaborative Autoscaling. A fun-
|     |     |     |     |     |     | damental | limitation | of existing | autoscaling |     | methods | is their |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ----------- | ----------- | --- | ------- | -------- |
B. Key Insights narrow-scope decision-making, which primarily relies on per-
|         |               |             |     |           |            | server resource |     | utilization metrics | while | neglecting | the | struc- |
| ------- | ------------- | ----------- | --- | --------- | ---------- | --------------- | --- | ------------------- | ----- | ---------- | --- | ------ |
| Through | comprehensive | experiments |     | (Sec. V), | we further |                 |     |                     |       |            |     |        |
analyze and reveal the limitations of existing approaches tured relationships among servers. Many traditional methods,
regarding the challenges previously outlined. To clearly dis- such as rule-based autoscalers (e.g., Kubernetes Horizontal
tinguish our approach from these methods, we summarize our Pod Autoscaler (HPA) [51]), make scaling decisions based
key insights as follows. solely on predefined thresholds, treating each server in isola-
tionwithoutconsideringcross-serverinteractions.Meanwhile,
| Insight | 1: One Policy | Does | Not | Fit All—Rethinking |     |     |     |     |     |     |     |     |
| ------- | ------------- | ---- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
AutoscalingforHeterogeneousEdgeServers.Inedge-cloud reinforcementlearning(RL)-basedapproaches[18],[40]opti-
environments, geographically distributed servers experience mize scaling policies through global decision-making, encod-
highlydynamicandserver-specificconditions.Analysisofthe ing system states in a monolithic fashion. While differing in
Shanghai Telecom trace [6]–[8]—millions of requests from theirdecision-makingscope,bothapproachesfailtoexplicitly
|              |        |        |               |       |          | model inter-server |     | relationships, | resulting |     | in uncoordinated |     |
| ------------ | ------ | ------ | ------------- | ----- | -------- | ------------------ | --- | -------------- | --------- | --- | ---------------- | --- |
| 9 000+ users | across | 3 000+ | base stations | (BSs) | over six |                    |     |                |           |     |                  |     |
months—shows that, after partitioning each day into four scaling actions and inefficient resource utilization. Without
equal intervals, the spatial distribution of hot (high-load) and a structured understanding of how servers influence each
warm(low-load)BSsshiftsmarkedly(Fig.1a-d).Bothrequest other,thesemethodssufferfrominefficientresourceallocation,
volume(Fig.1e)andgeographicalconcentrationfluctuateover increased scaling overhead, and degraded application perfor-
| time, leading | to evolving | and | asymmetric | scaling | demands | mance. |     |     |     |     |     |     |
| ------------- | ----------- | --- | ---------- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
across servers. A more effective autoscaling mechanism must therefore
Existing autoscaling techniques do not satisfy the dual movebeyondisolatedormonolithicdecision-makingtowarda
requirement of local adaptability and global coordination. (i) relational perspective—one that captures how servers interact,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
IEEETRANSACTIONSONSERVICESCOMPUTING 4
complement each other, and collectively shape system behav- Neighborhood. Spatial proximity is a critical factor in de-
ior. Incorporating such relational structure enables autoscalers terminingwhichserversarelikelytobenefitfromcollaborative
to reason collaboratively across distributed nodes rather than scaling. To model this, we define a binary adjacency matrix
reacting to local signals alone. This perspective forms the A =[a ]|V| , where each element a indicates whether
neigh ij i,j=1 ij
conceptual foundation for our subsequent design, where we server v and server v are geographically adjacent:
i j
leverage structured inter-server relationships to support coor-
(cid:40)
dinated and scalable autoscaling decisions. 1, if v and v are adjacent
a = i j (1)
ij
0, otherwise
III. PROBLEMFORMULATIONANDSYSTEMDESIGN
A. System Model This matrix captures the spatial layout of the system, re-
vealing which server pairs are in close geographic prox-
We consider a distributed edge-cloud environment where
imity. Such relationships are particularly valuable in edge-
user requests are served by microservices deployed across ge-
cloud scenarios, where servers within the same proximity
ographicallydistributed,resource-heterogeneousservers.Each
can coordinate their scaling actions more effectively, reducing
microservice may run multiple instances, and a request may
communication overhead and end-to-end latency. Proximity-
invoke a dependency chain spanning several servers. The
basedcollaboration ensuresthatscalingdecisions arecontext-
key notations used throughout this paper are summarized in
aware and responsive to physical deployment characteristics,
Table I.
thereby improving real-time performance.
Heterogeneity in such environments arises from both the
Functional similarity. Besides proximity, the functional
networkanddevicelayers[52].Networkheterogeneityappears
suitability of servers for specific workloads is also critical.
in two forms [53]: edge-to-edge variations in bandwidth and
Different servers may be optimized for different types of
propagation delay among edge nodes, and edge-to-cloud dis-
tasks, such as compute-intensive or memory-bound tasks.
crepanciesbetweenlow-latencyintra-edgelocalareanetworks
To quantify the functional similarity between servers, we
(LANs) and the higher-latency backhaul links to the cloud.
define a Point of Interest (POI) vector for each server, which
Device heterogeneity comprises variations in both resource
includes attributes such as its geographical location, resource
capacities (e.g., CPU, memory, storage) and computational
availability (CPU cores, memory, storage), and current load
capabilities, the latter reflected in differences in processing
metrics. The POI vector is updated continuously at runtime to
speedscausedbyvariationsinhardwarearchitecture,operating
reflect the dynamic state of the server. The cosine similarity
systems, and system-level optimizations [54].
between two servers’ POI vectors is calculated to measure
The edge-cloud environment is modeled as a Directed
Acyclic Graph (DAG), denoted as G = (V,A), where V their functional similarity:
E
istheserversetwhichconsistsofasetofheterogeneousedge p ·p
devices and a cloud data center, and A = {A neigh ,A poi ,T} a˜ ij = ∥p i ∥∥p j ∥ (2)
i j
is the set of inter-server correlations introduced in this paper.
The resource capabilities of each server v ∈V are quantified where p and p are the POI vectors for servers v and v ,
i i j i j
in terms of CPU, memory, storage volume, denoted as Wcpu, respectively. Since the POI features are non-negative, a˜ lies
i ij
Wmem, Wdisk, respectively. within [0,1]. To construct an adjacency matrix applicable to
i i
graph convolution, we further binarize the similarity matrix
TABLE I: Notations and Descriptions using a threshold τ :
poi
Symbol Description (cid:40)
1, if a˜ ≥τ ,
ij poi
V Setofservers a = (3)
ij
A Setofadjacencymatricesforservercorrelations 0, otherwise.
Wcpu NumberofCPUcoresonservers
i
Wmem Memorycapacityofservers
i We collect these pairwise similarities into a matrix A =
Wdisk Storagevolumeofservers poi
M i Setofmicroservices [a ij ]| i V ,j | =1 ,whichrepresentsthefunctionalsimilarityadjacency
E Callrelationshipsamongmicroservices among all servers. This measure reflects the similarity in
△ m,m′ Theamountofdatatransferredfrommicroservicemtom′ operational characteristics between servers and is updated
F Thefunctionalitysetoftheconsideredapplication
wcpu NumberofCPUcoresrequiredtodeployservicei continuously to track state changes. Incorporating functional
i
w i mem Amountofmemoryrequiredtodeployservicei similarity helps align scaling decisions with each server’s
wdisk Amountofstoragerequiredtodeployservicei
i capabilities and current conditions. Here, the threshold is set
αm(t) Workloadofeachinstanceofservicem
λm Processingrateofaninstanceofservicem to τ poi =0.6 in our implementation.
Traffic connectivity. User mobility across servers is a
1) CorrelationsofServers: Tocapturetheinter-serversyn- key factor influencing workload distribution in edge-cloud
ergies in edge-cloud environments, we propose and formalize environments. As users move between servers over time,
three types of server correlations: neighborhood, functional they form dynamic patterns of spatial and temporal flows.
similarity, and traffic connectivity. These correlations are vital To capture these spatiotemporal relationships, we define a
for optimizing collaborative autoscaling decisions by consid- traffic connectivity matrix T, which tracks whether there is
ering the structural dependencies between servers. significant traffic flow between two servers. If the traffic flow
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
IEEETRANSACTIONSONSERVICESCOMPUTING 5
ð betweenserversv andv exceedsathresholdτ =20,the The routing probability is defined as:
ij i j
connection between them is considered substantial:
(cid:40) (cid:89)
|fi|
T = 1, if ð ij ≥τ (4) P(f i ,l)= P(m j ,v j ) (6)
ij 0, if ð <τ j=1
ij
where P(m ,v ) denotes the probability that microservice
Thismatrixhelpsmodeltrafficdependenciesbetweenservers, j j
m is handled by a server v . Assuming round-robin load
identifying pairs of servers that frequently experience traffic j j
balancing, this probability is proportional to the number of
flows from each other. By identifying these connections, the
instances of m deployed on v :
autoscaling algorithm can proactively prepare instances on j j
servers with strong traffic connectivity, ensuring that they are n (t)
P(m,v )=
m,vj
(7)
readytohandletheincomingdemandandminimizinglatency. j (cid:80)|V|
n (t)
2) Microservice-Based Application: Modern applications k=1 m,vk
are increasingly structured as microservices to enhance mod- where n (t) is the number of m’s instances on v .
m,vj j
ularity, scalability, and independent deployment. We for- The overall path-level response time T (t) is composed
l,fi
mallyrepresentamicroservice-basedapplicationasadirected of four components: transmission delay, propagation delay,
acyclic graph (DAG), denoted by G M = (M,E), where M queuing delay, and execution delay, formally expressed as:
is the set of microservices (nodes), and E ⊆M×M denotes
the set of directed inter-service dependencies (edges). For any T l,fi (t)=T l t , r f a i ns(t)+T l p ,f r i op(t)+T f q i ueue(t)+T f e i xec(t) (8)
two microservices m,m′ ∈ M, a directed edge ⟨m,m′⟩ ∈ E
Each term captures a different stage of end-to-end request
implies that m′ depends on the output produced by m during
processing.
execution. The parameter △ captures the volume of data
m,m′
The transmission delay accounts for the time needed to
transmitted from m to m′ during execution.
transfer intermediate data between dependent microservices
Each application supports a set of functionalities, denoted
hostedondifferentservers.Fortwoconsecutivemicroservices
byF.Followingpriorwork[13],wemodeleachfunctionality
m →m deployedonv andv respectively,thetransmission
f ∈F as a sequence of microservices that must be executed i j i j
i delay is defined as:
in a predefined order, i.e., f = ⟨m ,...,m ⟩, where |f |
i 1 |fi| i
denotesthenumberofmicroservicesinvolved.Thisformalism △
Ttrans (t)= mi,mj (9)
enables the system to associate functionality-specific request l,mi,mj B(v ,v )
i j
flows with subgraphs of the overall microservice DAG.
where △ is the data volume to be transmitted and
Microservices are executed through their deployed in- mi,mj
B(v ,v )isthebandwidthbetweentheservers.Ifv =v ,the
stances, each corresponding to a lightweight container hosted i j i j
delay is considered negligible. Aggregating over the service
on a server. The deployment of an instance consumes server
chain, the total transmission delay becomes:
resources including CPU, memory, and storage. For each
microservice m, we denote its per-instance resource demands
by 3 w ) m c R pu e , qu w e m m st em Re , s a p n o d ns w e m di T s i k m , e r : esp U e s c e t r iv s e r ly e . quest different func- T l t , r f a i ns(t)=
|f (cid:88)i|−1
T l t , r m a j n , s mj+1 (t) (10)
j=1
tionalities provided by the application, each typically com-
Next, the propagation delay captures the time for signals to
posed of a sequence of interdependent microservices. We
traversethephysicaldistancebetweenservers.Foreachpairof
denote such a functionality by f = ⟨m ,...,m ⟩, where
i 1 |fi|
consecutive servers v and v on the path, the propagation
m represents the j-th microservice in the chain. Given the j j+1
j delay is denoted by Tprop (t), and the cumulative delay
geographicdistributionofusersinanedge-cloudenvironment, vj,vj+1,fi
over the full path is:
requests are first received by the base station nearest to
the user, then routed to one or more nearby servers for
|l|−1
(cid:88)
processing.Forthesamefunctionality,requestsmaybeserved Tprop(t)= Tprop (t) (11)
bydifferentcombinationsofserversdependingonlocationand
l,fi vj,vj+1,fi
j=1
load balancing, thus forming distinct processing paths.
Following data transmission and propagation, the request
We define a path l=⟨v ,...,v ⟩, where each v indicates
1 |fi| j
is enqueued and executed on the target instance. To capture
the server executing microservice m of functionality f . The
j i
this, we adopt the standard M/M/1 queuing model. For a
expected response time T (t) for functionality f in time slot
fi i
microservice m, the combined queuing and execution delay
t is the weighted sum over all feasible paths:
is given by:
|V| |V|
(cid:88) (cid:88) α (t) 1
T fi (t)= ... P(f i ,l)T l,fi (t) (5) T
m
queue(t)+T
m
exec(t)=
λ (λ
m
−α (t))
+
(λ )
(12)
v1=1 v|fi|=1
(cid:124)
m m
(cid:123)(cid:122)
m
(cid:125) (cid:124)(cid:123)
m
(cid:122)(cid:125)
queue execution
where P(f ,l) is the probability that a request for f is
i i
processed along path l, and T (t) is the corresponding whereα (t)denotesthearrivalrateofrequestsattheinstance,
l,fi m
response time along that path. and λ represents the processing rate, measured in requests
m
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
IEEETRANSACTIONSONSERVICESCOMPUTING 6
per second (RPS). Summing over all microservices along the IV. ALGORITHMDESIGN
functionality chain, we obtain:
This section presents the design of SynScale, with the
overall architecture illustrated in Fig. 2. The subsequent sub-
Tqueue(t)+Texec(t)= (cid:88)
|fi|
Tqueue(t)+Texec(t) (13) sections provide detailed descriptions of its components and
fi fi mj mj
their underlying design principles.
j=1
Finally, the overall expected application response time is
A. Spatiotemporal Representation Module
obtained by aggregating over all functionalities, weighted by
Thissubsectionintroducesthespatiotemporalrepresentation
their request distribution:
module,whichcombinesatemporalattentionmechanismwith
|F| amulti-graphconvolutionalnetworkbasedonChebyshevcon-
(cid:88)
Tapp(t)= P(f i ,t)T fi (t) (14) volution (ChebConv) [55]. As illustrated in parts B and A of
i=1 Fig.2,thesecomponentsjointlyprocesshistoricalobservations
whereP(f ,t)denotestheprobabilityoffunctionalityf being and multi-relational server graphs to produce spatiotemporal
i i
requested at time t, calculated as: representations used in subsequent policy learning.
1) Temporal Attention Network: The input to this module
(cid:80)|V|
α (t) is the historical observation sequence X =x ,...,x , where
P(f ,t)= k=1 fi,vk (15) 1 W
i (cid:80)|F| (cid:80)|V|
α (t)
each x
t
includes server states, executed actions, and applica-
j=1 k=1 fj,vk tion response at time t. We set W =5 in our implementation.
with α (t) denoting the request volume for functionality To extract informative temporal features, we adopt a temporal
fi,vk
f at server v . attention mechanism that learns to focus on key historical
i k
points by dynamically assigning attention weights along the
temporal dimension:
B. Problem Formulation

A =softmax(Θσ(X X +b)) (17)
Thegoalofmicroserviceautoscalinginedge-cloudenviron-
 att 1 2
X =W (XTW ) (18)
ments is to ensure application-level QoS, typically reflected 1 2 1
by low response latency and stable system performance. X 2 =XTW 3 T (19)
Giventheheterogeneityandresourceconstraintsofdistributed
Here,Θ,W ,W ,W arelearnableparameters,andσisanon-
1 2 3
servers, we aim to minimize the average response time of the
linearactivation.TheresultingattentionweightsA highlight
att
applicationbydeterminingatime-varyingdeploymentstrategy
temporally salient points that correlate scaling actions with
for microservice instances while satisfying multi-dimensional
their outcomes. The output H is obtained by aggregating
temp
resource constraints and ensuring request serviceability. For-
weighted inputs:
mally, the problem is defined as:
H =A X (20)
temp att
This temporal encoding captures the dynamic evolution of
T
1 (cid:88) system behavior and its correlation with past scaling actions,
min lim Tapp(t), m∈M, v ∈V, t∈Z+
nm,v(t)T→∞T
t=1
allowing the policy to internalize performance trends.
(16a) 2) Multi-graph Network: The input to this module in-
s.t. (cid:88) n (t)≥1, ∀m∈M (16b) cludes the current server states and a set of explicitly defined
m,v graphs A = {A ,A ,T} that capture spatial proximity,
v∈V neigh poi
functional similarity, and traffic connectivity, respectively, as
(cid:88)
n (t)wr ≤Wr, ∀v ∈V, ∀r ∈R (16c) described in §III-A1. These graphs form a unified multi-
m,v m v
relational server topology G = (V,A), where each server
m∈M E
is a vertex.
α (t)>λ , ∀m∈M (16d)
m m We perform Chebyshev spectral convolution over each
graph in parallel. The results are concatenated across the
In the above, n (t) denotes the number of instances of
m,v feature dimension to form an enriched representation that
service m deployed on server v at time t, and Z+ represents
encodes multi-faceted inter-server relationships:
the set of positive integers. Equation 16a defines the objective
of minimizing long-term average application response time K
Tapp(t) across all services and servers. Constraint 16b en- H(l) =||| τ A = | 1 σ( (cid:88) T k (Aˆ τ )H(l−1)Θ(l)) (21)
sures service availability by requiring at least one instance of k=0
each microservice to be deployed. Constraint 16c compactly where σ is the activation function (i.e., ReLU), T (x) de-
k
enforces the per-server limits on CPU, memory, and disk notes the Chebyshev polynomials that are recursively defined
resources, where r ∈ R indexes these resource types and as T (x) = 2xT (x) − T (x), with T (x) = 1 and
k k−1 k−2 0
wr and Wr denote the corresponding per-instance demand T (x) = x. K is the order of the Chebyshev convolution,
m v 1
and server capacity. Finally, 16d ensures system stability by which determines the range of neighbors (up to K-hop)
enforcing that the processing rate of each service exceeds its consideredduringtheconvolution.A ∈Arepresentstheτ-th
τ
arrival rate. adjacency matrix in A. Aˆ τ =D˜− 2 1A˜ τ D˜−1 2 is the normalized
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

IEEETRANSACTIONSONSERVICESCOMPUTING 7
Integrate paire-wise correlations Capture server synergies
between servers with state with graph convolution
on multiple graphs
Neighborhood
GCN
State Func. similarity
GCN
Connectivity
GCN
Time
Historical data
TimeAtt
This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
Environment Execute scaling actions Part C.1Execution
Part A Actor
Actions
Spatial contextual information network
capturing the server synergies
across different correlations
Application
Update
Part C.2
Critic Estimated
Spatiotemporal network reward
Edge server Users information
Dense Block
Service instance Request
···
Cloud server Concatenation Temporal contextual information
Reward function Part B capturing the critical historical data Training Update
Environment-provided reward
Fig. 2: Algorithm Overview
adjacent matrix, where A˜ = A +I and D˜ is a diagonal Foreachserverv ,theactorπ receivesaserver-centricob-
τ τ i i
matrix with D˜ = (cid:80) A˜ . H(l−1) represents the feature servation.AsshowninFig.3,thisobservationconsistsoftwo
ii j τij
matrix from the previous layer, which for the first layer is the components.Thefirstisthelocalextendedstates˜ =(s ,X ),
i i i
initialserverstates.Θ(l) isthelearnableparameters.||denotes where s denotes the current state of server v —capturing its
i i
the concatenation operator. This process is repeated over two resource condition and workload-related characteristics—and
layers,andthefinaloutputH capturesserver-awarefeatures X is its historical observation sequence used by the temporal
spat i
enriched with multi-relational context. attention module. The second component is the set of states
3) Spatiotemporal Fusion: The temporal and spatial em- from other servers, denoted as {s j :j ∈N i }, where N i is the
beddings are concatenated along the feature axis: selected neighborhood used by the multi-graph convolution
to construct spatial relational features. The receptive field
H final =H temp ||H spat (22) size k i = |N i | can be flexibly configured depending on
deployment needs. We denote the entire input compactly
Thisspatiotemporalembeddingispassedtothescalingpolicy
as o = (s˜,{s : j ∈ N }). As the policy operates in
i i j i
network, enabling it to reason over both historical dynamics
a distributed manner and its network design depends only
and structural synergies. The fusion of temporal attention and
on this per-server observation rather than the global system
graph-based structural encoding ensures that the policy not
state, changes in the number of servers do not affect the
only reacts to real-time conditions, but also aligns with the
dimensionality of s ; only modifications to the local state
i
long-term collaborative potential of the edge-cloud system.
space itself would require retraining. Given o , the actor π
i i
produces a probability distribution π (a|o ) over the discrete
i i
B. Distributed Collaborative Autoscaling autoscaling actions in the action space A={−2,−1,0,1,2},
where each action specifies a step-wise adjustment to the
To realize adaptive and collaborative autoscaling in dis-
numberofmicroserviceinstancesonserverv .Theagentthen
i
tributed environments, we instantiate our framework with
selects the most probable action a for execution.
i
Multi-Agent Proximal Policy Optimization (MAPPO) [56]
During centralized training, the value network V receives
under the Centralized Training and Decentralized Execution ϕ
a global representation of the system. Let z denote the global
(CTDE) paradigm [57]. This setup allows agents deployed
state constructed by concatenating the observations of all
on each server to make scaling decisions independently while
agents. Given z, the critic outputs a scalar that estimates the
being trained cooperatively, enabling the system to integrate
expected long-term return associated with the current joint
server-specific conditions with system-wide coordination.
condition of the system. This global evaluation reflects how
SynScale trains two neural networks parameterized by θ
desirabletheoverallsystemstateisandprovidestraining-time
and ϕ: an actor network π for action selection and a value
θ
guidance for improving the shared policy toward cooperative
network V for global state evaluation. Depending on the
ϕ
behavior.
application, these networks can either be shared among all
agents when their state–action spaces are homogeneous, or Becauseautoscalingisacooperativecontroltask,allagents
instantiated independently with arbitrary architectures when sharethesamerewardsignal.Inthiswork,weadoptparameter
heterogeneous behavior is required. sharing under a homogeneous state–action definition. Prior
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 8   |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
studies [56], [58] have shown that sharing policy parameters where a represents the possible actions that can be taken by
across homogeneous agents can improve learning efficiency the policy π θ in state o t .
and overall policy performance. Consequently, each agent Update. The policy and value function are updated itera-
| employs | an     | actor and    | a critic | that      | share the | same      | parameter |        |         |            |          |               |     |         |      |
| ------- | ------ | ------------ | -------- | --------- | --------- | --------- | --------- | ------ | ------- | ---------- | -------- | ------------- | --- | ------- | ---- |
|         |        |              |          |           |           |           |           | tively | via     | stochastic | gradient | ascent:       |     |         |      |
| sets θ  | and ϕ. | In addition, | we       | configure | the       | receptive | field     | to     |         |            |          |               |     |         |      |
|         |        |              |          |           |           |           |           |        | policy: | θ ←θ+η     |          | (∇ LCLIP(θ)+c | ∇   | S[π ]), | (28) |
be global, meaning that the actor’s observation o consists of π θ t 2 θ θ
i
LVF(ϕ)
the local extended state s˜ i together with the states of all other value: ϕ←ϕ−η v c 1 ∇ ϕ t (29)
| servers   | (i.e.,     | {s :j        | ∈V \{i}}). |          |        |            |             |           |      |               |                                         |     |     |     | ··· |
| --------- | ---------- | ------------ | ---------- | -------- | ------ | ---------- | ----------- | --------- | ---- | ------------- | --------------------------------------- | --- | --- | --- | --- |
|           |            | j            |            |          |        |            |             | Here,η    | andη |               | arethelearningratesforthepolicyandvalue |     |     |     |     |
|           |            |              |            |          |        |            |             |           | π    | v             |                                         |     |     |     | ··· |
| Training. |            | The training |            | phase    | of the | autoscaler | involves    |           |      |               |                                         |     |     |     | ··· |
|           |            |              |            |          |        |            |             | networks, |      | respectively. |                                         |     |     |     |     |
| jointly   | optimizing | the          | policy     | function | π and  | the        | value func- |           |      |               |                                         |     |     |     |     |
θ
| tion V | via stochastic |     | gradient | ascent. | The | policy | is updated |     |     |     |     |     |     |     |     |
| ------ | -------------- | --- | -------- | ------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ϕ
toimprovedecisionqualityandmaintainexplorationcapacity,
| while | the value | function | estimates |     | expected | returns | to support |     |     |     |     |     |     |     |     |
| ----- | --------- | -------- | --------- | --- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
advantage computation and cooperative learning. At each Exe c u tion
· · ·
| iteration, | we  | minimize | a composite |     | loss: |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(θ,ϕ)=Eˆ
| L     |            | [−LCLIP(θ)+c |           |     | LVF(ϕ)−c | S[π    | ]] (23)      |     |     | ··· |     | ··· |     | ··· |     |
| ----- | ---------- | ------------ | --------- | --- | -------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|       | t          | t            | t         | 1   | t        | 2      | θ            |     |     |     |     |     |     |     |     |
| where | Eˆ denotes | the          | empirical |     | average  | over a | finite batch |     |     |     |     |     |     |     |     |
t
···
| of samples, |     | and c 1 ,c | 2 are | coefficient | hyperparameters. |     | The |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | ----- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
firstterm,LCLIP(θ),representstheclippedsurrogateobjective,
t
defined as: Fig. 3: Overview of the centralized training and decentralized
execution.
| LCLIP(θ)=Eˆ |     | [min(p | (θ)Aˆ | ,clip(p | (θ),1−ϵ,1+ϵ)Aˆ |     | )] (24) |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ----- | ------- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |     | t      | t     | t       | t              |     | t       |     |     |     |     |     |     |     |     |
πθ(at|ot)
| wherep | t (θ)= |         | denotestheratioofactionprobabil- |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------ | ------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |        | π θ ( a | t| ot )                          |     |     |     |     |     |     |     |     |     |     |     |     |
ities wh ich qua n tiolfid e s h o w the probability of selecting action C. Computational Complexity Analysis
a t has changed between the old policy π θold and the current The computational complexity of the temporal attention
policy π based on the same state o . The clipping operation, network is dominated by Eq. 17, with a complexity of
|     | θ   |     |     |     | t   |     |     |      |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ϵ,  |     |     |     |     |     | Θ(T3 | +T2 |     |     |     |     |     |     |
parameterized by constrains the policy update, mitigating ·N), where T is the time window size and N
the risk of excessively large policy deviations that could lead is the number of servers. For the multi-graph convolution, the
to performance collapse. Here, Aˆ denotes the generalized complexity primarily stems from Eq. 21, which involves a
t
|     |     |     |     |     |     |     |     |     |     |     |     |     | Aˆ H(l−1), |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
advantage estimate (GAE) [59], a standard technique for sparse-dense matrix multiplication of τ resulting in
reducing variance in policy gradient estimation. To further acomplexityofΘ(|E|·F·C).Here,|E|denotesthenumberof
stabilize learning, we normalize the advantages using the edgesbetweenservers(i.e.,theircorrelations),whileC andF
PopArt method [60]. representtheinputandoutputfeaturedimensions,respectively.
The second term in the composite loss, LVF(ϕ), represents The actor network comprises m parallel fully connected sub-
t
the squared-error loss for the value function: networks, each corresponding to a microservice, where m is
thenumberofmicroservices.Eachsubnetworkconsistsoftwo
|     |     |     |     | (cid:104) |     | (cid:105) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LVF(ϕ)=Eˆ (V (z )−y(t))2 . (25) fullyconnectedlayersthattakethespatiotemporalinformation
|     |     |     | t   | ϕ   | t   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheassociatedserverasinputandoutputan|A|-dimensional
The target value y(t) is computed as y(t)=r t +γV ϕ (z t+1 ), action probability distribution, where |A| is the number of
| and r | is the | environment |     | reward | given | by the | autoscaling |     |     |     |     |     |     |     |     |
| ----- | ------ | ----------- | --- | ------ | ----- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
t possible actions. Considering the parallel computation across
reward function m sub-networks, the total complexity of the actor network is
|     |     |     |     |     |     |     |     | Θ(d·h+h·|A|), |     |     | with d | and h being the | input | dimension | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------ | --------------- | ----- | --------- | --- |
|M|
(cid:88)
|     |     | r =δ(SLA−res |     | )−β |     | n (t), | (26) | hidden | layer | size, | respectively. |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | ------ | ---- | ------ | ----- | ----- | ------------- | --- | --- | --- | --- |
|     |     | t            |     | t   |     | i      |      |        |       |       |               |     |     |     |     |
i=1
|      |              |     |                   |     |            |     |         |     |     | TABLE | II: | System Parameters |     |     |     |
| ---- | ------------ | --- | ----------------- | --- | ---------- | --- | ------- | --- | --- | ----- | --- | ----------------- | --- | --- | --- |
| with | SLA denoting |     | the response-time |     | threshold, |     | res the |     |     |       |     |                   |     |     |     |
t
measured application response time, and n (t) the number Parameter Description Value
i
of instances of microservice i. The coefficients are set to Wcpu NumberofCPUcores 8–100
i
δ = 0.6 and β = 0.4 to balance SLA compliance against Wmem Memorysize 16–64GB
i
resource consumption, and γ is the standard discount factor. W d is k S t o ra g e vo l u m e 120–1 0 2 4GB
ic p u
|           |        |     |       |         |                |     |          |     | w       |     | Requ               | ir e d C P U c o r e count |     |         | 1 – 4 |
| --------- | ------ | --- | ----- | ------- | -------------- | --- | -------- | --- | ------- | --- | ------------------ | -------------------------- | --- | ------- | ----- |
| This term | trains | the | value | network | to approximate |     | expected |     | wm i em |     |                    |                            |     |         |       |
|           |        |     |       |         |                |     |          |     | i       |     | Requiredmemorysize |                            |     | 0.5–4GB |       |
returns, supporting stable advantage estimation. wdisk Requiredstoragevolume 0.5–8GB
i
|             |       |             |          |            |                |      |          | B          | (vi,vj) |     | Bandwidthbetweenedgenodes    |     |     | 1±0.2Gbps  |     |
| ----------- | ----- | ----------- | -------- | ---------- | -------------- | ---- | -------- | ---------- | ------- | --- | ---------------------------- | --- | --- | ---------- | --- |
| The         | final | term, S[π   | θ ], is  | an entropy | bonus          | that | promotes | edge-edge  |         |     |                              |     |     |            |     |
|             |       |             |          |            |                |      |          | B          | (vi,vj) |     | Bandwidthbetweenedgeandcloud |     |     | 150±20Mbps |     |
| exploration | by    | maintaining |          | policy     | stochasticity: |      |          | edge-cloud |         |     |                              |     |     |            |     |
|             |       |             |          |            |                |      |          |            | λm      |     | Processingrateofaninstance   |     |     | 40–80RPS   |     |
|             |       |             | (cid:88) |            |                |      |          |            | △mi,mj  |     | Thevolumeoftransferreddata   |     |     | 100–2000KB |     |
|             | S[π   | ](s )=−     |          | π (a|o     | )logπ          | (a|o | ) (27)   |            |         |     |                              |     |     |            |     |
|             |       | θ t         |          | θ          | t              | θ    | t        |            |         |     |                              |     |     |            |     |
a
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 9   |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V. EVALUATION negligible latency. This result demonstrates that SynScale can
A. Experiment Setup be efficiently trained with modest computational resources
|                 |     |     |           |      |            |             | while | maintaining |     | fast execution |     | during | deployment. |     |     |
| --------------- | --- | --- | --------- | ---- | ---------- | ----------- | ----- | ----------- | --- | -------------- | --- | ------ | ----------- | --- | --- |
| All experiments |     | are | conducted | in a | simulation | environment |       |             |     |                |     |        |             |     |     |
using Python 3.9 on macOS equipped with an Apple M1 TABLE III: Algorithm Parameters
| Pro chipset | and | 16 GB | RAM. | The system | model | parameters |     |           |     |     |             |     |     |       |     |
| ----------- | --- | ----- | ---- | ---------- | ----- | ---------- | --- | --------- | --- | --- | ----------- | --- | --- | ----- | --- |
|             |     |       |      |            |       |            |     | Parameter |     |     | Description |     |     | Value |     |
describedinSectionIII-Aandthealgorithm-specifichyperpa-
rametersaresummarizedinTableIIandTableIII,respectively. c1 Valuelosscoefficient 1
Resource attributes (CPU, memory, and storage) are defined c2 Entropycoefficient 0.01
|          |          |          |       |         |      |              |     |     | ϵ   |     | Clippingcoefficient |     |     | 0.2  |     |
| -------- | -------- | -------- | ----- | ------- | ---- | ------------ | --- | --- | --- | --- | ------------------- | --- | --- | ---- | --- |
| for edge | servers, | assuming | cloud | servers | have | unrestricted |     |     |     |     |                     |     |     |      |     |
|          |          |          |       |         |      |              |     |     | γ   |     | Discountfactor      |     |     | 0.99 |     |
capacity. To avoid excessive autoscaling that may degrade ηπ Learningrateforactornetwork 0.0005
|           |     |                  |          |     |           |                |     |     | ηv  | Learningrateforcriticnetwork |     |     |     | 0.0005 |     |
| --------- | --- | ---------------- | -------- | --- | --------- | -------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------ | --- |
| QoS [61], | the | autoscaling      | interval | is  | set to 30 | seconds.       |     |     |     |                              |     |     |     |        |     |
| Workload  |     | and application. |          | We  | construct | geographically |     |     |     |                              |     |     |     |        |     |
distributed workloads using the Shanghai Telecom trace [6]– Comparison baselines. For comparison, we select three
representativeautoscalingalgorithms:ProScale[9],HRA[40],
[8],whichcontainsoversixmonthsofInternetaccessrecords
from 9,481 mobile users across 3,233 base stations, along and AWS algorithm [21]. These methods encompass a range
|             |             |      |           |      |          |                | of       | scaling | strategies, | from     | rule-based, |         | prediction-driven |     | ap-     |
| ----------- | ----------- | ---- | --------- | ---- | -------- | -------------- | -------- | ------- | ----------- | -------- | ----------- | ------- | ----------------- | --- | ------- |
| with server | location    | data | derived   | from | latitude | and longitude. |          |         |             |          |             |         |                   |     |         |
|             |             |      |           |      |          |                | proaches | to      | adaptive    | learning |             | models, | providing         | a   | compre- |
| To simulate | application |      | requests, | we   | assume   | that each user |          |         |             |          |             |         |                   |     |         |
initiates one request per second during their active sessions, hensive baseline for evaluating our proposed framework.
|         |            |        |         |      |         |                 |     | ProScale | [9]: | This | predictive | method | adjusts | the | number |
| ------- | ---------- | ------ | ------- | ---- | ------- | --------------- | --- | -------- | ---- | ---- | ---------- | ------ | ------- | --- | ------ |
| thereby | converting | access | records | into | request | traces. For the | •   |          |      |      |            |        |         |     |        |
applicationscenario,weadoptavideoprocessing(VP)service of service instances based on predicted workloads using
|            |     |                |     |          |      |                |     | a heuristic | algorithm. |     | While | ProScale |     | offers | a simple |
| ---------- | --- | -------------- | --- | -------- | ---- | -------------- | --- | ----------- | ---------- | --- | ----- | -------- | --- | ------ | -------- |
| comprising | 12  | microservices, |     | obtained | from | [62], with its |     |             |            |     |       |          |     |        |          |
architecture illustrated in Fig. 4. and intuitive approach, it relies on predefined rules and
|     |     |     |     |     |     |     |     | thresholds, | making        |     | it inflexible |     | to dynamic | and          | hetero- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | ------------- | --- | ---------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | geneous     | environments. |     | Moreover,     |     | it lacks   | coordination |         |
HD
Encode across servers, resulting in inefficient scaling decisions
|     |       |     |           |     |       |         |     | in distributed |     | systems. |     |     |     |     |     |
| --- | ----- | --- | --------- | --- | ----- | ------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- |
|     | Video |     | Thumbnail |     | Count | Combine |     |                |     |          |     |     |     |     |     |
Track generation Segments Tracks • HRA[40]:Areinforcementlearning-basedapproachthat
|         |          |     |        |     |     |        |     | enhances | training | efficiency      |     | by        | modeling | environmental |          |
| ------- | -------- | --- | ------ | --- | --- | ------ | --- | -------- | -------- | --------------- | --- | --------- | -------- | ------------- | -------- |
| Data    | Audio    |     | SD     |     |     |        |     |          |          |                 |     |           |          |               |          |
|         |          |     |        |     |     | Notify |     | dynamics | and      | utilizes        | DRL | agents    | to       | make scaling  | de-      |
| Collect | Track    |     | Encode |     |     |        |     |          |          |                 |     |           |          |               |          |
|         |          |     |        |     |     |        |     | cisions  | from     | low-dimensional |     | features. |          | While it      | exhibits |
|         | Metadata |     | Data   |     |     | Video  |     |          |          |                 |     |           |          |               |          |
Traack Analysis Classify improved learning performance compared to traditional
Fig. 4: Video Processing Application Architecture with 12 DRL approaches, HRA still adopts a centralized policy
Microservices structure and overlooks the distinct operational contexts
|     |     |     |     |     |     |     |     | of individual |                | servers, | leading | to             | limited | scalability | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | -------- | ------- | -------------- | ------- | ----------- | ---- |
|     |     |     |     |     |     |     |     | insufficient  | responsiveness |          |         | in large-scale |         | distributed | sys- |
tems.
|     |     |     |     |     |     |     | •   | AWS           | algorithm | [21]:        | A widely       |             | adopted     | threshold-based  |           |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ------------ | -------------- | ----------- | ----------- | ---------------- | --------- |
|     |     |     |     |     |     |     |     | mechanism     | used      | in           | major          | platforms.  | In          | our experiments, |           |
|     |     |     |     |     |     |     |     | we follow     | its       | standard     | configuration, |             | where       | scaling          | deci-     |
|     |     |     |     |     |     |     |     | sions are     | triggered |              | when CPU       | utilization |             | exceeds          | a fixed   |
|     |     |     |     |     |     |     |     | threshold.    | Despite   |              | its industrial |             | maturity    | and              | minimal   |
|     |     |     |     |     |     |     |     | computational |           | overhead,    |                | AWS-style   | autoscaling |                  | lacks     |
|     |     |     |     |     |     |     |     | adaptability  | and       | fine-grained |                | control,    | as          | it relies        | on static |
|     |     |     |     |     |     |     |     | policies      | and       | narrow-scope |                | indicators  | that        | are insufficient |           |
torespondtodynamic,heterogeneousruntimeconditions.
|     |     |     |     |     |     |     | Metrics. |     | To evaluate |     | the | performance |     | of the | proposed |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | --- | ----------- | --- | ------ | -------- |
framework,weadoptthefollowingwidelyrecognizedmetrics:
|              |             |          |         |             |                |            | (1)      | Average  | Response    |                 | Time   | (ART):     | The    | average       | end-to- |
| ------------ | ----------- | -------- | ------- | ----------- | -------------- | ---------- | -------- | -------- | ----------- | --------------- | ------ | ---------- | ------ | ------------- | ------- |
|              |             |          |         |             |                |            | end      | latency  | experienced |                 | by all | requests   | during | an evaluation |         |
| Fig.         | 5: Training | reward   |         | convergence | of             | SynScale.  |          |          |             |                 |        |            |        |               |         |
|              |             |          |         |             |                |            | episode, | measured |             | in milliseconds |        | (ms):      |        |               |         |
| Training     | Cost.       | We       | further | report      | the training   | efficiency |          |          |             |                 |        | N          |        |               |         |
|              |             |          |         |             |                |            |          |          |             |                 |        | 1 (cid:88) |        |               |         |
|              |             |          |         |             |                |            |          |          |             | ART=            |        | T          | ,      |               | (30)    |
| of SynScale. |             | As shown | in Fig. | 5,          | the normalized | training   |          |          |             |                 |        |            | i      |               |         |
N
reward steadily increases and converges after approximately i=1
500 episodes. The entire offline training phase for the eight- where N is the total number of processed requests and T
i
serversetupcompleteswithinabout1hours.Suchtrainingcost denotes the response time of the i-th request.
isacceptablesinceitisperformedonlyonceoffline,whilethe (2) SLA Violation Rate: In this work, we define a latency-
subsequent inference process for autoscaling decisions incurs centric service-level agreement (SLA), consistent with com-
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
IEEETRANSACTIONSONSERVICESCOMPUTING 10
mon practice in autoscaling literature [11], [40]. An SLA The set of all observed lifetimes L = {ℓ ,ℓ ,...,ℓ } yields
1 2 K
violation occurs when a request’s response time exceeds a the following statistics:
predefined threshold τ SLA =80ms. The SLA violation rate is 1 (cid:88)
AIL= ℓ. (36)
then defined as:
K
ℓ∈L
N
SLA Violation Rate= 1 (cid:88) I(T >τ ), (31) Here, AIL represents the average lifetime (reported in min-
N i SLA utes).AhigherAILindicatesthatinstancestendtostayactive
i=1
for longer periods, implying more stable and less oscillatory
where I(·) is the indicator function that returns 1 if the
scaling with reduced cold-start overheads. Conversely, shorter
condition is true and 0 otherwise. This metric quantifies the
lifetimes correspond to frequent scale-in/out cycles, reflecting
proportion of requests failing to meet the latency-based SLA
more volatile behavior.
objective.
(3)95thPercentileLatency(P95):Tocapturethetaillatency B. Experiment Results and Analysis
that critically impacts user experience, we compute the 95th
Thissectionpresentsandanalyzesourexperimentalresults.
percentile of the response time distribution:
To ensure reproducibility and statistical significance, each
experimentwasrepeated10times,andwereporttheaveraged
P95=min{t|F (t)≥0.95}, (32)
T
results.Allalgorithmsweretrainedunderidenticalconditions,
where F (t) denotes the empirical cumulative distribution withtheenvironmentconsistingof8servers,including1cloud
T
function (CDF) of request response times. A lower P95 value server and 7 edge servers. To comprehensively evaluate our
indicates tighter latency control under bursty workloads and proposedmethod,wedesignedthreesetsofexperiments,each
reduced performance jitter. addressing a specific validation aspect:
(4) Resource Cost. We define the resource cost as the 1) Effectiveness validation: Comparative analysis of the
average number of active microservice instances across all performance of different autoscaling algorithms.
servers over the evaluation period, reflecting the mean level 2) Ablation study: Analysis of individual module contri-
of resource utilization. Formally, butions to the autoscaling performance in our approach.
3) Overheadanalysis:Comparisonofoverheadacrossdif-
T
1 (cid:88) (cid:88) (cid:88) ferent algorithms under environments of varying scales.
Cost= n (t), (33)
T m,v Notethattheexperimentalsetupsforthefirsttwoexperiments
t=1m∈Mv∈V
were conducted with environments of the same scale as the
where n (t) denotes the number of running instances of
m,v training environment.
servicemonserverv attimeslott,andT isthetotalnumber Effectiveness validation. This experiment evaluates the
of autoscaling intervals. A lower value of Cost indicates more overall effectiveness of SynScale under dynamic, heteroge-
efficient average resource usage while maintaining service- neous workloads. As shown in Fig. 6(a), SynScale achieves
level performance. the lowest and most stable response time throughout the
(5) Instance-Time (IT). Since cloud providers typically autoscalingprocess.ThekerneldensitydistributioninFig.6(c)
charge according to the runtime of active instances, we quan- further confirms its tight latency profile, with most requests
tifythetotalaccumulateduptimeofallmicroserviceinstances concentrated in the low-latency region and significantly fewer
during an evaluation horizon T as long-tail outliers. Across all metrics (Fig. 6(b)), SynScale
consistently outperforms state-of-the-art methods, reducing
T
(cid:88) (cid:88) (cid:88)
IT= n (t)·∆t, (34) averageresponsetimeby59.32%,SLAviolationsby85.71%,
m,v
and P95 latency by 73.2%, while lowering resource cost by
t=1m∈Mv∈V
14.46%. It also achieves 42.77% lower instance-time and
where n (t) denotes the number of running instances of
m,v 54.5% longer instance lifetime, indicating more stable scaling
servicemonserverv attimeslott,and∆tistheautoscaling
with fewer oscillatory scale-in/out cycles.
interval (30 s in our experiments). The instance-time (IT)
ThesuperiorityofSynScalestemsfromitsabilitytocouple
metric thus represents the total runtime accumulated by all
temporal consistency with structure-aware coordination. The
instances, serving as a direct measure of temporal resource
temporal module captures how past actions influence current
consumption. IT is reported in hours, where lower values
performance, enabling trend-aligned scaling rather than short-
indicate lower overall runtime cost.
sightedreactions.Meanwhile,thespatialmoduleleveragesex-
(6) Average Instance Lifetime (AIL). While IT reflects the
plicitlymodeledinter-serversynergiestoformstructure-aware
total uptime cost, it does not reveal how frequently instances
representations, allowing each agent to make locally adaptive
are created and terminated. To assess scaling stability, we
yet globally coherent decisions. This joint spatiotemporal
define the average instance lifetime as the mean duration that
awarenessenablesSynScaletoprovisionresourcesproactively
an instance remains active before being terminated. Formally,
where needed while avoiding redundant scaling across the
let ℓ denote the lifetime of the k-th instance, measured as
k system, leading to both improved QoS and reduced cost.
the elapsed time between its start time t(k) and termination
start Compared with SynScale, existing methods reveal clear
time t( en k d ): structurallimitations.Rule-basedautoscalers—typifiedbysys-
ℓ =(t(k)−t(k))·∆t. (35) temssuchasAWS—dependonstaticallyconfiguredthresholds
k end start
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     | 11  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SynScale HRA AWS ProScale SLA ART (ms) Cost (Instances) IT (hours) SynScale HRA AWS ProScale
|     |     |     |     | P95 Latency (ms) | SLA Violations (%) |     | AIL (minutes) |          |     |     |
| --- | --- | --- | --- | ---------------- | ------------------ | --- | ------------- | -------- | --- | --- |
|     |     |     |     | 175              |                    |     |               | 120 0.12 |     |     |
100
| 200                |     |     |                        | 150 |     |     |     |                                              |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
| )sm( emiT esnopseR |     |     | )sm( ycnetaL 59P / TRA |     |     |     |     | 100 0.10                                     |     |     |
|                    |     |     |                        |     |     |     |     | )%( snoitaloiV / tsoC 80 )nim( LIA / )rh( TI |     |     |
125
| 150 |     |     |     |     |     |     |     | 80 0.08    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
|     |     |     |     | 100 |     |     |     | 60 ytisneD |     |     |
|     |     |     |     |     |     |     |     | 60 0.06    |     |     |
| 100 |     |     |     | 75  |     |     |     |            |     |     |
40
|     |     |     |     | 50  |     |     |     | 40 0.04  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
| 50  |     |     |     |     |     |     |     | 20 0.02  |     |     |
|     |     |     |     | 25  |     |     |     | 20       |     |     |
|     |     |     |     | 0   |     |     |     | 0 0 0.00 |     |     |
0 20 40 60 80 100 SynScale HRA AWS ProScale 0 50 100 150 200 250
|     | Timeline |     |     |     | Approaches |     |     |     | Response Time (ms) |     |
| --- | -------- | --- | --- | --- | ---------- | --- | --- | --- | ------------------ | --- |
(a) Autoscaling Process (b) Result Comparison (c) Kernel Density Estimate
|     |     |     | Fig. 6: Performance |       | Comparison   | Across | Different | Algorithms |     |     |
| --- | --- | --- | ------------------- | ----- | ------------ | ------ | --------- | ---------- | --- | --- |
|     |     |     |                     | TABLE | IV: Ablation | Study  | Results   |            |     |     |
Metric FullModel(Exp.1) w/oTemporal(Exp.2) w/oSpatial(Exp.3) w/oSpatiotemporal(Exp.4)
| ART(ms)          |     | 22.3±6.28  |     |     | 35.32±4.31 |     | 42.33±10.32 |     | 48.08±12.48 |     |
| ---------------- | --- | ---------- | --- | --- | ---------- | --- | ----------- | --- | ----------- | --- |
| P95Latency(ms)   |     | 27.72±2.13 |     |     | 82.4±14    |     | 70.28±19    |     | 91.22±6.29  |     |
| Cost(Instances)  |     | 90.67±4.2  |     |     | 99.82±1.37 |     | 106.18±4.22 |     | 128.34±7.6  |     |
| SLAViolations(%) |     | 2.2±0.9    |     |     | 11.3±2.9   |     | 13.6±5.6    |     | 18±3.8      |     |
| IT(hours)        |     | 75.56±0.83 |     |     | 80.28±2.05 |     | 91.38±1.1   |     | 104.89±0.98 |     |
| AIL(minutes)     |     | 39.72±0.53 |     |     | 35.5±0.9   |     | 37.02±1.04  |     | 29.93±0.87  |     |
and narrow-scope indicators, which cannot reflect evolving Experiment 4 removes both the spatial and temporal mod-
workload trends or cross-server interactions. This rigidity ules. This combined ablation yields the poorest performance,
leadstodelayedorexcessivescalingactionsandconsequently confirmingthatrelationallyinformedspatiotemporalmodeling
higher latency and violation rates under dynamic conditions. is central to SynScale’s ability to achieve effective collabora-
Prediction-driven approaches (e.g., ProScale) improve reac- tive autoscaling under dynamic and heterogeneous conditions.
| tivity but rely | on one-dimensional |     | forecasts | and | predefined |          |     |                         |                  |      |
| --------------- | ------------------ | --- | --------- | --- | ---------- | -------- | --- | ----------------------- | ---------------- | ---- |
|                 |                    |     |           |     |            | Overhead |     | analysis. In edge-cloud | scenarios, where | edge |
heuristics, making them sensitive to prediction errors and devices often operate under tight latency and resource con-
unstable when workload patterns shift. Centralized RL meth- straints,theruntimeoverheadintroducedbyautoscalingstrate-
ods such as HRA are more adaptive yet still encode the gies is a critical factor for practical deployment. We evaluate
environment through a monolithic global policy, limiting their the overhead of each method in terms of the time (ms) and
ability to capture server-specific heterogeneity and hindering memory usage (MB) required to complete a one-shot scaling
distributed coordination. These design constraints fundamen- decision under environments of varying scale (i.e., different
tally restrict their capability to sustain low latency and stable numbers of servers). Since the goal of this experiment is to
scaling in heterogeneous edge-cloud settings. measure inference-time overhead rather than policy perfor-
Ablation study. To assess the contribution of each core mance,wedirectlyexecutethetrainedmodelonenvironments
component in SynScale, we conducted a series of ablation with different numbers of servers without retraining. The
experiments, with results reported in Table IV. The complete forward computation—including the multi-graph convolution
modelconsistentlyoutperformsallablatedvariantsacrosskey in Eq. (23) and the shared actor network—is fully compatible
performance metrics, underscoring the importance of each withvaryingenvironmentsizes,makingthissetupappropriate
module. forisolatingtheimpactofsystemscaleoncomputationalcost.
Experiment 2 removes the temporal-awareness module, The results are summarized in Table V.
which leverages historical observations to uncover the causal As system size increases, most methods show rising over-
impact of recent scaling actions on system performance. head due to the need to process more complex system in-
Without this capability, the system cannot accurately model formation. AWS, which employs a simple threshold-based
thedelayedeffectsofpriordecisions,leadingtolessinformed trigger without structural or historical reasoning, maintains
policies and degraded responsiveness—particularly evident in low overhead but lacks adaptability and struggles to meet
elevated P95 latency, which reflects poor temporal stability. QoS under dynamic workloads. ProScale incurs significantly
Experiment3disablesthespatialmodule,whichimplements higher overhead because it must evaluate heuristic rules over
structured representation learning over explicitly modeled both the service dependency graph and all candidate servers
server relationships using graph convolution. This module en- when making scaling decisions. HRA, relying on a cen-
ablescontext-awarerefinementofserverstatesbypropagating tralized RL formulation, performs policy inference over a
relational information across distributed nodes. Its removal high-dimensional global state, causing inference latency and
undermines cross-server awareness and collaboration, leading memory usage to grow rapidly as the server count increases.
toinefficientresourceutilizationandincreasedSLAviolations. In contrast, SynScale maintains a lightweight and slowly
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
IEEETRANSACTIONSONSERVICESCOMPUTING 12
TABLE V: Overhead Comparison
Exp.ID Scale Metric SynScale ProScale AWS HRA
Exec.Time(ms) 2.85±1.02 9.44±3.62 2.21±1.29 12.95±9.13
1 8
Memory(MB) 0.50±1.34 0.27±0.42 0.40±0.96 0.63±1.40
Exec.Time(ms) 3.64±0.97 13.27±0.70 2.86±0.28 17.91±0.61
2 15
Memory(MB) 0.62±1.36 0.27±0.48 0.49±0.97 0.65±1.45
Exec.Time(ms) 13.59±8.42 41.42±2.40 14.49±1.33 50.70±1.39
3 50
Memory(MB) 1.21±1.82 0.56±0.77 1.00±1.36 0.93±1.65
Exec.Time(ms) 17.26±0.86 57.27±3.26 17.71±1.76 70.73±1.36
4 70
Memory(MB) 3.04±4.51 0.53±1.21 1.06±1.46 1.26±1.89
Exec.Time(ms) 32.21±1.75 82.36±6.72 26.78±3.63 102.72±2.34
5 100
Memory(MB) 7.52±9.22 1.06±1.40 0.99±1.74 1.65±2.08
increasing overhead. Its distributed design ensures that each Transferability limitation. We adopt parameter sharing
agent reasons over localized information rather than a global across agents, so the learned policy can be directly executed
systemstate,yieldingnearlylinearinferencecost—2.85ms→ in environments with different numbers of servers. However,
32.21 ms from 8 to 100 servers (≈0.32 ms/server), compared transfer becomes limited because the structural features in
withHRA(≈0.98ms/server)andProScale(≈0.79ms/server). SynScale are extracted using a spectral GCN, whose filters
The slight upward trend originates from computing graph- depend on the eigenstructure of the training-time graphs
based relational representations via the multi-graph convolu- and therefore exhibit limited transfer when the topology
tion in Eq. 21. However, the correlation matrices are typically or server relationships differ substantially. In addition, the
sparse—enabling efficient sparse operations (§IV-C)—and the policy network is tied to a fixed per-server state space, so
aggregation neighborhood can be flexibly constrained, so the any change in the state definition would require redesigning
receptivefielddoesnothavetogrowwiththefullsystemsize. the input representation and retraining the model, although
ThesefactorskeepSynScale’sscale-relatedoverheadmoderate such state definitions are typically stable in real deployments.
and predictable, offering a favorable overhead-performance Environment-level transferability remains a broader challenge
balancesuitableforlarge-scale,latency-sensitivedeployments. for autoscaling systems operating across heterogeneous envi-
ronments, and we plan to design autoscaling algorithms that
VI. DISCUSSIONANDLIMITATIONS better support such environment transfer in future work.
Feasibility discussion. Our overhead evaluation shows that
the proposed method incurs minimal delay and resource con- VII. CONCLUSION
sumption, exerting negligible impact on autoscaling perfor- This paper presented SynScale, a distributed collabora-
mance. The framework supports both distributed and central- tive autoscaling framework for microservices in heteroge-
ized deployment, enabling flexible integration across hetero- neous edge-cloud environments. By explicitly modeling inter-
geneous environments. When edge servers have sufficient ca- server relationships and integrating spatiotemporal represen-
pacity, local deployment allows parallel, server-side decision- tation learning with multi-agent reinforcement learning, Syn-
making. In resource-limited scenarios, the policy can be cen- Scale enables locally adaptive yet globally coordinated scal-
trally executed on a cloud server, with node-level metrics ing decisions across distributed servers. Experimental results
collected through high-performance monitoring systems (e.g., demonstrate that SynScale consistently outperforms existing
Prometheus[63]).Althoughcentralizeddeploymentintroduces autoscaling approaches in terms of response latency, SLA
synchronization overhead, its magnitude is largely determined compliance,andresourceefficiency.Moreover,theframework
by the monitoring infrastructure, and modern tools generally maintains stable and lightweight runtime overhead across
keep this overhead within acceptable bounds. different system scales, indicating its practicality for large-
Correlation modeling limitation. A current limitation of scaledeployments.Theseresultshighlightthatspatiotemporal
our framework lies in its reliance on manually constructed correlation-aware and distributed scaling paradigms can pro-
inter-server relationships to represent collaborative synergies. videaprincipledfoundationforautoscalingsystemsoperating
While effective in our setting, such predefined structures may in large-scale edge-cloud infrastructures.
miss latent or evolving dependencies, especially in large,
dynamic, or previously unseen environments. Moreover, new
VIII. ACKNOWLEDGEMENTS
deploymentscenariosmayrequireadditionalefforttoadaptor
redesign these relational models, introducing manual tuning. This work is Supported by the National Natural Sci-
Tomitigatethislimitation,futureworkwillexploreautomated ence Foundation of China(NSFC) under Grant No.92582202,
approaches for inferring inter-server relationships, such as and the NSFC-Guangdong Joint Fund Project under Grant
unsupervised or self-organizing techniques. No.U20A6003.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 13  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
|     |     |     |     |     |     |     |     | knowledge-driven |     | evolutionary |     | algorithm,” | Complex & | Intelligent | Sys- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ----------- | --------- | ----------- | ---- |
tems,vol.7,pp.1153–1171,2021.
[1] Y.Chiang,Y.Zhang,H.Luo,T.-Y.Chen,G.-H.Chen,H.-T.Chen,Y.- [23] S.Xie,J.Wang,B.Li,Z.Zhang,D.Li,andP.C.Hung,“Pbscaler:A
J. Wang, H.-Y. Wei, and C.-T. Chou, “Management and orchestration bottleneck-aware autoscaling framework for microservice-based appli-
ofedgecomputingforiot:Acomprehensivesurvey,”IEEEInternetof cations,”IEEETransactionsonServicesComputing,2024.
ThingsJournal,2023. [24] D. Balla, C. Simon, and M. Maliosz, “Adaptive scaling of kubernetes
pods,”inNOMS2020-2020IEEE/IFIPNetworkOperationsandMan-
| [2] A. Sarah, | G.  | Nencioni, | and M. | M. I. Khan, | “Resource |     | allocation | in  |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ------ | ----------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
multi-access edge computing for 5g-and-beyond networks,” Computer agementSymposium. IEEE,2020,pp.1–5.
Networks,vol.227,p.109720,2023. [25] E.CasalicchioandV.Perciballi,“Auto-scalingofcontainers:Theimpact
[3] ”CNCF”.(2021).[Online].Available:https://www.cncf.io/ of relative and absolute metrics,” in 2017 IEEE 2nd International
[4] AWS, “Hybrid cloud with aws,” 2022, [Online]. [Online]. Available: Workshops on Foundations and Applications of Self* Systems (FAS*
W). IEEE,2017,pp.207–214.
https://aws.amazon.com/hybrid/
|             |     |           |     |            |      |     |              | [26] M. R. | Hossen | and M. | A. Islam, | “A lightweight | workload-aware |     | mi- |
| ----------- | --- | --------- | --- | ---------- | ---- | --- | ------------ | ---------- | ------ | ------ | --------- | -------------- | -------------- | --- | --- |
| [5] Google, |     | “Building |     | enterprise | edge |     | applications |            |        |        |           |                |                |     |     |
with google cloud,” 2022, [Online]. [On- croservicesautoscalingwithqosassurance,”learning,vol.12,pp.17–
| line]. | Available: | https://cloud.google.com/blog/topics/hybrid-cloud/ |     |     |     |     |     | 19,2022. |     |     |     |     |     |     |     |
| ------ | ---------- | -------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
google-cloud-tools-to-manage-your-enterprise-edge-apps [27] L.BaresiandG.Quattrocchi,“Asimulation-basedcomparisonbetween
|                                                             |          |      |                 |        |           |       |             | industrial                                          | autoscaling |     | solutions | and cocos | for cloud | applications,” | in    |
| ----------------------------------------------------------- | -------- | ---- | --------------- | ------ | --------- | ----- | ----------- | --------------------------------------------------- | ----------- | --- | --------- | --------- | --------- | -------------- | ----- |
| [6] Y. Guo,                                                 | S. Wang, | A.   | Zhou, J.        | Xu, J. | Yuan, and | C.-H. | Hsu, “User  |                                                     |             |     |           |           |           |                |       |
|                                                             |          |      |                 |        |           |       |             | 2020IEEEInternationalConferenceonWebServices(ICWS). |             |     |           |           |           |                | IEEE, |
| allocation-aware                                            |          | edge | cloud placement |        | in mobile | edge  | computing,” |                                                     |             |     |           |           |           |                |       |
| Software:PracticeandExperience,vol.50,no.5,pp.489–502,2020. |          |      |                 |        |           |       |             | 2020,pp.94–101.                                     |             |     |           |           |           |                |       |
[7] S. Wang, Y. Guo, N. Zhang, P. Yang, A. Zhou, and X. Shen, “Delay- [28] A.F.BaarziandG.Kesidis,“Showar:Right-sizingandefficientschedul-
ingofmicroservices,”inProceedingsoftheACMSymposiumonCloud
| aware | microservice | coordination |     | in mobile | edge | computing: | A rein- |     |     |     |     |     |     |     |     |
| ----- | ------------ | ------------ | --- | --------- | ---- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Computing,2021,pp.427–441.
forcementlearningapproach,”IEEETransactionsonMobileComputing,
|     |     |     |     |     |     |     |     | [29] M.Mekki,N.Toumi,andA.Ksentini,“Microservicesconfigurationsand |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
vol.20,no.3,pp.939–951,2019.
|            |          |     |         |          |               |     |             | the impact | on  | the performance |     | in cloud native | environments,” |     | in 2022 |
| ---------- | -------- | --- | ------- | -------- | ------------- | --- | ----------- | ---------- | --- | --------------- | --- | --------------- | -------------- | --- | ------- |
| [8] Y. Li, | A. Zhou, | X.  | Ma, and | S. Wang, | “Profit-aware |     | edge server |            |     |                 |     |                 |                |     |         |
placement,”IEEEInternetofThingsJournal,vol.9,no.1,pp.55–67, IEEE 47th Conference on Local Computer Networks (LCN). IEEE,
2022,pp.239–244.
2021.
|                          |            |           |             |            |                  |        |              | [30] Y. Guo,                                                       | J. Ge,     | P. Guo,        | Y. Chai, | T. Li, M.  | Shi, Y. Tu,       | and J.     | Ouyang, |
| ------------------------ | ---------- | --------- | ----------- | ---------- | ---------------- | ------ | ------------ | ------------------------------------------------------------------ | ---------- | -------------- | -------- | ---------- | ----------------- | ---------- | ------- |
| [9] K. Cheng,            | S.         | Zhang,    | C. Tu,      | X. Shi, Z. | Yin, S.          | Lu, Y. | Liang, and   |                                                                    |            |                |          |            |                   |            |         |
|                          |            |           |             |            |                  |        |              | “Pass:                                                             | Predictive | auto-scaling   |          | system for | large-scale       | enterprise | web     |
| Q. Gu,                   | “Proscale: | Proactive | autoscaling |            | for microservice |        | with time-   |                                                                    |            |                |          |            |                   |            |         |
|                          |            |           |             |            |                  |        |              | applications,”                                                     |            | in Proceedings | of       | the ACM    | on Web Conference |            | 2024,   |
| varying                  | workload   | at        | the edge,”  | IEEE       | Transactions     | on     | Parallel and |                                                                    |            |                |          |            |                   |            |         |
| DistributedSystems,2023. |            |           |             |            |                  |        |              | 2024,pp.2747–2758.                                                 |            |                |          |            |                   |            |         |
|                          |            |           |             |            |                  |        |              | [31] H.YuanandS.Liao,“Atimeseries-basedapproachtoelastickubernetes |            |                |          |            |                   |            |         |
[10] C.Meng,S.Song,H.Tong,M.Pan,andY.Yu,“Deepscaler:Holistic
scaling,”Electronics,vol.13,no.2,p.285,2024.
autoscalingformicroservicesbasedonspatiotemporalgnnwithadaptive
|       |            |         |      |          |               |            |     | [32] S.K.Mondal,X.Wu,H.M.D.Kabir,H.-N.Dai,K.Ni,H.Yuan,and |     |     |     |     |     |     |     |
| ----- | ---------- | ------- | ---- | -------- | ------------- | ---------- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| graph | learning,” | in 2023 | 38th | IEEE/ACM | International | Conference |     | on                                                        |     |     |     |     |     |     |     |
T.Wang,“Towardoptimalloadpredictionandcustomizableautoscaling
| AutomatedSoftwareEngineering(ASE). |     |     |     |     | IEEE,2023,pp.53–65. |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
schemeforkubernetes,”Mathematics,vol.11,no.12,p.2675,2023.
[11] S.Zhang,T.Wu,M.Pan,C.Zhang,andY.Yu,“A-sarsa:Apredictive [33] L.Ju,P.Singh,andS.Toor,“Proactiveautoscalingforedgecomputing
| container | auto-scaling |     | algorithm | based on | reinforcement |     | learning,” | in  |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --------- | -------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
systemswithkubernetes,”inProceedingsofthe14thIEEE/ACMInter-
| 2020IEEEInternationalConferenceonWebServices(ICWS). |     |     |     |     |     |     | IEEE, |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
nationalConferenceonUtilityandCloudComputingCompanion,2021,
2020,pp.489–497.
pp.1–8.
[12] K.Cheng,S.Zhang,M.Liu,Y.Gu,L.Wei,H.Cheng,K.Liu,Y.Song,
|     |     |     |     |     |     |     |     | [34] Y. Song, | C.  | Li, K. Zhuang, | T.  | Ma, and T. | Wo, “An automatic |     | scaling |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ---------- | ----------------- | --- | ------- |
X. Shi, A. Zhu et al., “Geoscale: Microservice autoscaling with cost systemforonlineapplicationwithmicroservicesarchitecture,”in2022
| budget | in geo-distributed |     | edge | clouds,” IEEE | Transactions |     | on Parallel |                                                        |     |     |     |     |     |     |       |
| ------ | ------------------ | --- | ---- | ------------- | ------------ | --- | ----------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- |
|        |                    |     |      |               |              |     |             | IEEEInternationalConferenceonJointCloudComputing(JCC). |     |     |     |     |     |     | IEEE, |
andDistributedSystems,vol.35,no.4,pp.646–662,2024.
2022,pp.73–78.
| [13] X. He, | Z. Tu, | M. Wagner, | X.  | Xu, and | Z. Wang, | “Online | deployment |                                                                   |     |     |     |     |     |     |     |
| ----------- | ------ | ---------- | --- | ------- | -------- | ------- | ---------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|             |        |            |     |         |          |         |            | [35] Y.Li,H.Zhang,W.Tian,andH.Ma,“Jointoptimizationofauto-scaling |     |     |     |     |     |     |     |
algorithmsformicroservicesystemswithcomplexdependencies,”IEEE
andadaptiveserviceplacementinedgecomputing,”in2021IEEE27th
TransactionsonCloudComputing,vol.11,no.2,pp.1746–1763,2022. InternationalConferenceonParallelandDistributedSystems(ICPADS).
[14] J.Tong,M.Wei,M.Pan,andY.Yu,“Aholisticauto-scalingalgorithm IEEE,2021,pp.923–930.
| for multi-service                                   |     | applications | based | on balanced |     | queuing | network,” | in                                                           |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | ------------ | ----- | ----------- | --- | ------- | --------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                                                     |     |              |       |             |     |         |           | [36] Y.Zhang,W.Hua,Z.Zhou,G.E.Suh,andC.Delimitrou,“Sinan:Ml- |     |     |     |     |     |     |     |
| 2021IEEEInternationalConferenceonWebServices(ICWS). |     |              |       |             |     |         | IEEE,     |                                                              |     |     |     |     |     |     |     |
basedandqos-awareresourcemanagementforcloudmicroservices,”in
2021,pp.531–540. Proceedingsofthe26thACMinternationalconferenceonarchitectural
[15] W. Lv, P. Yang, T. Zheng, C. Lin, Z. Wang, M. Deng, and Q. Wang, support for programming languages and operating systems, 2021, pp.
| “Graph | reinforcement |     | learning-based | dependency-aware |     |     | microservice | 167–181. |     |     |     |     |     |     |     |
| ------ | ------------- | --- | -------------- | ---------------- | --- | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
deploymentinedgecomputing,”IEEEInternetofThingsJournal,2023.
|     |     |     |     |     |     |     |     | [37] X. Li, | J. Zhou, | X. Wei, | D. Li, | Z. Qian, | J. Wu, X. | Qin, and | S. Lu, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------- | ------ | -------- | --------- | -------- | ------ |
[16] C.Wang,B.Jia,H.Yu,X.Li,X.Wang,andT.Taleb,“Deepreinforce-
“Topology-awareschedulingframeworkformicroserviceapplicationsin
ment learning for dependency-aware microservice deployment in edge cloud,”IEEETransactionsonParallelandDistributedSystems,vol.34,
computing,”inGLOBECOM2022-2022IEEEGlobalCommunications no.5,pp.1635–1649,2023.
Conference. IEEE,2022,pp.5141–5146. [38] G.Yu,P.Chen,andZ.Zheng,“Microscaler:Cost-effectivescalingfor
[17] K.Fu,W.Zhang,Q.Chen,D.Zeng,X.Peng,W.Zheng,andM.Guo,
microserviceapplicationsinthecloudwithanonlinelearningapproach,”
| “Qos-aware | and | resource | efficient | microservice |     | deployment | in cloud- |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --------- | ------------ | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEETransactionsonCloudComputing,vol.10,no.2,pp.1100–1116,
| edgecontinuum,”in2021IEEEInternationalParallelandDistributed |     |     |     |     |     |     |     | 2020. |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ProcessingSymposium(IPDPS). IEEE,2021,pp.932–941. [39] H.Yang,Q.Chen,M.Riaz,Z.Luan,L.Tang,andJ.Mars,“Powerchief:
[18] L. Chen, Y. Xu, Z. Lu, J. Wu, K. Gai, P. C. Hung, and M. Qiu, Intelligent power allocation for multi-stage applications to improve
“Iot microservice deployment in edge-cloud hybrid environment using responsivenessonpowerconstrainedcmp,”inProceedingsofthe44th
reinforcementlearning,”IEEEInternetofThingsJournal,vol.8,no.16,
|                      |     |     |     |     |     |     |     | Annual   | International |     | Symposium | on Computer | Architecture, | 2017, | pp. |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --------- | ----------- | ------------- | ----- | --- |
| pp.12610–12622,2020. |     |     |     |     |     |     |     | 133–146. |               |     |           |             |               |       |     |
[19] L.A.Vayghan,M.A.Saied,M.Toeroe,andF.Khendek,“Akubernetes [40] C. Meng, J. Tong, M. Pan, and Y. Yu, “Hra: An intelligent holistic
controller for managing the availability of elastic microservice based resourceautoscalingframeworkformulti-serviceapplications,”in2022
stateful applications,” Journal of Systems and Software, vol. 175, p. IEEEInternationalConferenceonWebServices(ICWS). IEEE,2022,
110924,2021.
pp.129–139.
[20] S.N.Srirama,M.Adhikari,andS.Paul,“Applicationdeploymentusing [41] K.Fu,W.Zhang,Q.Chen,D.Zeng,andM.Guo,“Adaptiveresource
containers with auto-scaling for microservices in cloud environment,” efficient microservice deployment in cloud-edge continuum,” IEEE
Journal of Network and Computer Applications, vol. 160, p. 102629, Transactions on Parallel and Distributed Systems, vol. 33, no. 8, pp.
| 2020.       |        |      |         |          |           |     |           | 1825–1840,2021.                                                 |     |     |     |     |     |     |     |
| ----------- | ------ | ---- | ------- | -------- | --------- | --- | --------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| [21] (2025) | Amazon | Auto | Scaling | Service. | Accessed: | Aug | 10, 2025. |                                                                 |     |     |     |     |     |     |     |
|             |        |      |         |          |           |     |           | [42] Z.Yang,P.Nguyen,H.Jin,andK.Nahrstedt,“Miras:Model-basedre- |     |     |     |     |     |     |     |
[Online].Available:http://aws.amazon.com/autoscaling/ inforcementlearningformicroserviceresourceallocationoverscientific
[22] W. Ma, R. Wang, Y. Gu, Q. Meng, H. Huang, S. Deng, and workflows,”in2019IEEE39thinternationalconferenceondistributed
Y. Wu, “Multi-objective microservice deployment optimization via a computingsystems(ICDCS). IEEE,2019,pp.122–132.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2026.3672566
| IEEETRANSACTIONSONSERVICESCOMPUTING |     |     |     |     |     |     |     |     |     |     |     | 14  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[43] W. Lv, Q. Wang, P. Yang, Y. Ding, B. Yi, Z. Wang, and C. Lin, HaogangTongreceivedhisM.S.degreefromBei-
“Microservicedeploymentinedgecomputingbasedondeepqlearning,” jing University of Posts and Telecommunications
IEEETransactionsonParallelandDistributedSystems,vol.33,no.11, (BUPT),China,in2020.HeispursuingaPh.D.de-
pp.2968–2978,2022. greewiththeSchoolofComputerScience,SunYat-
[44] D.Garg,N.C.Narendra,andS.Tesfatsion,“Heuristicandreinforcement senUniversity(SYSU),China.Hisresearchfocuses
learning algorithms for dynamic service placement on mobile edge onmicroservicesschedulingindistributedsystems,
cloud,”arXivpreprintarXiv:2111.00240,2021. latency-sensitive task orchestration for edge com-
[45] X.Tian,H.Meng,Y.Shen,J.Zhang,Y.Chen,andY.Li,“Dynamicmi- puting,andIoT-drivenintelligentsystems.Hiswork
croservicedeploymentandoffloadingforthings-edge-cloudcomputing,” wasawardedtheACMSIGSOFTDistinguishedPa-
| IEEEInternetofThingsJournal,2024. |     |     |     |     |     |     |     | perAward. |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
[46] K.Gasmi,K.Abassi,L.Romdhani,andO.Debauche,“Reinforcement
learning-basedapproachformicroservices-basedapplicationplacement
| in edge               | environment,” |             | in 2023                 | IEEE Symposium |            | on Computers     | and    |          |      |          |            |             |
| --------------------- | ------------- | ----------- | ----------------------- | -------------- | ---------- | ---------------- | ------ | -------- | ---- | -------- | ---------- | ----------- |
| Communications(ISCC). |               |             | IEEE,2023,pp.1098–1103. |                |            |                  |        |          |      |          |            |             |
| [47] S. Chen,         | Q. Yuan,      | J. Li,      | H. He,                  | S. Li, X.      | Jiang, and | J. Yang,         | “Graph |          |      |          |            |             |
| neural                | network       | aided       | deep reinforcement      |                | learning   | for microservice |        |          |      |          |            |             |
| deployment            | in            | cooperative | edge                    | computing,”    | IEEE       | Transactions     | on     |          |      |          |            |             |
|                       |               |             |                         |                |            |                  |        | Chunyang | Meng | received | his master | degree from |
ServicesComputing,2024.
|     |     |     |     |     |     |     |     | Beijing University |     | of Posts | and Telecommunica- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | ------------------ | --- |
[48] S.HorovitzandY.Arian,“Efficientcloudauto-scalingwithslaobjective
tions,China,in2020.HeisnowaPh.D.studentat
usingq-learning,”in2018IEEE6thInternationalConferenceonFuture School of Computer Science and Engineering with
InternetofThingsandCloud(FiCloud).
IEEE,2018,pp.85–92. SunYat-SenUniversity,China.Hiscurrentresearch
| [49] G. Yu, | P. Chen, | and Z. | Zheng, | “Microscaler: | Automatic |     | scaling for |     |     |     |     |     |
| ----------- | -------- | ------ | ------ | ------------- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
areasincludedistributedsystem,servicescomputing,
| microservices |     | with an | online learning | approach,” | in  | 2019 | IEEE Inter- |     |     |     |     |     |
| ------------- | --- | ------- | --------------- | ---------- | --- | ---- | ----------- | --- | --- | --- | --- | --- |
andAIdrivenoperations.Hewasarecipientofthe
| nationalConferenceonWebServices(ICWS). |     |     |     |     | IEEE,2019,pp.68–75. |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
ACMSIGSOFTDistinguishedPaperAwardatASE
[50] X. Jie, T. Liu, H. Gao, C. Cao, P. Wang, and W. Tong, “A dqn-based 2023 and the Best Student Paper Award at ICWS
| approach | for | online service | placement | in  | mobile edge | computing,” | in  |     |     |     |     |     |
| -------- | --- | -------------- | --------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- |
2022.
| Collaborative                                 |                   | Computing: | Networking, | Applications   |     | and Worksharing: |           |     |     |     |     |     |
| --------------------------------------------- | ----------------- | ---------- | ----------- | -------------- | --- | ---------------- | --------- | --- | --- | --- | --- | --- |
| 16th                                          | EAI International |            | Conference, | CollaborateCom |     | 2020,            | Shanghai, |     |     |     |     |     |
| China,October16–18,2020,Proceedings,PartII16. |                   |            |             |                |     | Springer,2021,   |           |     |     |     |     |     |
pp.169–183.
[51] T.-T.Nguyen,Y.-J.Yeom,T.Kim,D.-H.Park,andS.Kim,“Horizon-
| tal pod | autoscaling | in  | kubernetes | for elastic | container | orchestration,” |     |     |     |     |     |     |
| ------- | ----------- | --- | ---------- | ----------- | --------- | --------------- | --- | --- | --- | --- | --- | --- |
Sensors,vol.20,no.16,p.4621,2020.
|     |     |     |     |     |     |     |     | Shijie Song | received | his bachelor’s |     | degree from |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------------- | --- | ----------- |
[52] W.Shi,J.Cao,Q.Zhang,Y.Li,andL.Xu,“Edgecomputing:Visionand
|     |     |     |     |     |     |     |     | Jinan University, |     | China, in | 2022. He | is currently a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | -------- | -------------- |
challenges,”IEEEinternetofthingsjournal,vol.3,no.5,pp.637–646,
| 2016. |     |     |     |     |     |     |     | master’sstudentattheSchoolofComputerScience |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
[53] Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, “A survey andEngineering,SunYat-SenUniversity,China.His
|           |      |            |     |               |     |               |      | current research | areas | include | distributed | systems, |
| --------- | ---- | ---------- | --- | ------------- | --- | ------------- | ---- | ---------------- | ----- | ------- | ----------- | -------- |
| on mobile | edge | computing: | The | communication |     | perspective,” | IEEE |                  |       |         |             |          |
servicescomputing,andserverlessfunctions.Hewas
| communications |     | surveys | & tutorials, | vol. | 19, no. | 4, pp. | 2322–2358, |             |        |             |     |               |
| -------------- | --- | ------- | ------------ | ---- | ------- | ------ | ---------- | ----------- | ------ | ----------- | --- | ------------- |
|                |     |         |              |      |         |        |            | a recipient | of the | ACM SIGSOFT |     | Distinguished |
2017.
[54] S.Deng,Z.Xiang,J.Taheri,M.A.Khoshkholghi,J.Yin,A.Y.Zomaya, PaperAwardatASE2023andhasapaperaccepted
andS.Dustdar,“Optimalapplicationdeploymentinresourceconstrained atICWS2024.
| distributed | edges,” | IEEE | transactions | on  | mobile | computing, | vol. 20, |     |     |     |     |     |
| ----------- | ------- | ---- | ------------ | --- | ------ | ---------- | -------- | --- | --- | --- | --- | --- |
no.5,pp.1907–1923,2020.
[55] M.Defferrard,X.Bresson,andP.Vandergheynst,“Convolutionalneural
| networks | on graphs | with | fast localized | spectral | filtering,” |     | Advances in |     |     |     |     |     |
| -------- | --------- | ---- | -------------- | -------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- |
neuralinformationprocessingsystems,vol.29,2016.
[56] C.Yu,A.Velu,E.Vinitsky,J.Gao,Y.Wang,A.Bayen,andY.Wu,“The
surprising effectiveness of ppo in cooperative multi-agent games,” Ad- Maolin Pan received the B.S. degree from the
vancesinNeuralInformationProcessingSystems,vol.35,pp.24611–
|             |     |     |     |     |     |     |     | Huazhong       | University | of Science | and       | Technology   |
| ----------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | ---------- | --------- | ------------ |
| 24624,2022. |     |     |     |     |     |     |     | (HUST), Wuhan, |            | China, in  | 1988, and | the M.S. de- |
[57] R.Lowe,Y.I.Wu,A.Tamar,J.Harb,O.PieterAbbeel,andI.Mordatch, greefromHUST,in1991,andthePh.D.degreefrom
“Multi-agent actor-critic for mixed cooperative-competitive environ- SunYat-senUniversity(SYSU),Guangzhou,China,
ments,” Advances in neural information processing systems, vol. 30, in2017.HeiscurrentlyalecturerwiththeSchoolof
2017.
SoftwareEngineering,SYSU.Hisresearchinterests
[58] F. Christianos, G. Papoudakis, M. A. Rahman, and S. V. Albrecht, include BPM and workflow technical, cloud native
“Scaling multi-agent reinforcement learning with selective parameter computing.
| sharing,” | in International |     | Conference | on Machine |     | Learning. | PMLR, |     |     |     |     |     |
| --------- | ---------------- | --- | ---------- | ---------- | --- | --------- | ----- | --- | --- | --- | --- | --- |
2021,pp.1989–1998.
| [59] J. Schulman, |     | P. Moritz, | S. Levine, | M. Jordan, | and | P. Abbeel, | “High- |     |     |     |     |     |
| ----------------- | --- | ---------- | ---------- | ---------- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
dimensionalcontinuouscontrolusinggeneralizedadvantageestimation,”
arXivpreprintarXiv:1506.02438,2015.
| [60] H. P. | Van Hasselt, | A.  | Guez, M. | Hessel, | V. Mnih, | and | D. Silver, |     |     |     |     |     |
| ---------- | ------------ | --- | -------- | ------- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
“Learningvaluesacrossmanyordersofmagnitude,”Advancesinneural
informationprocessingsystems,vol.29,2016. Yang Yu received the bachelor’s and master’s de-
[61] M. Abdullah, W. Iqbal, J. L. Berral, J. Polo, and D. Carrera, “Burst- grees in computer science from Huazhong Univer-
|              |            |             |            |               |                 |        |            | sity of Science | and       | Technology | (HUST),     | Wuhan,     |
| ------------ | ---------- | ----------- | ---------- | ------------- | --------------- | ------ | ---------- | --------------- | --------- | ---------- | ----------- | ---------- |
| aware        | predictive | autoscaling | for        | containerized | microservices,” |        | IEEE       |                 |           |            |             |            |
|              |            |             |            |               |                 |        |            | China, and      | the Ph.D. | degree     | in computer | science    |
| Transactions | on         | Services    | Computing, | vol.          | 15, no.         | 3, pp. | 1448–1460, |                 |           |            |             |            |
|              |            |             |            |               |                 |        |            | from Sun        | Yat-sen   | University | (SYSU),     | Guangzhou, |
2020.
[62] Q.Huang,P.Ang,P.Knowles,T.Nykiel,I.Tverdokhlib,A.Yajurvedi, China,in1988,1991,and2007,respectively.Heis
P. Dapolito IV, X. Yan, M. Bykov, C. Liang et al., “Sve: Distributed currently a Full Professor with the School of Data
|     |     |     |     |     |     |     |     | and Computer | Science | and | the School | of Software |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ---------- | ----------- |
videoprocessingatfacebookscale,”inProceedingsofthe26thSympo-
|     |     |     |     |     |     |     |     | Engineering, | Sun | Yat-sen University. |     | His research |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------- | --- | ------------ |
siumonOperatingSystemsPrinciples,2017,pp.87–103.
interestsincludeworkflow/BPM,servicecomputing,
| [63] Prometheus, | “An | open-source | monitoring |     | system | with a | dimensional |     |     |     |     |     |
| ---------------- | --- | ----------- | ---------- | --- | ------ | ------ | ----------- | --- | --- | --- | --- | --- |
data model, flexible query language, efficient time series database cloudcomputing,andsoftwareengineering.Heisa
DistinguishedMemberofCCFandamemberofACM.
| and | modern | alerting | approach.” | 2025. | [Online]. | Available: | https: |     |     |     |     |     |
| --- | ------ | -------- | ---------- | ----- | --------- | ---------- | ------ | --- | --- | --- | --- | --- |
//prometheus.io/
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:08:26 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.