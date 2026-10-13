This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
1
A Comprehensive Benchmark and Empirical Study
of Trace Anomaly Detection
Yongqian Sun, Member, IEEE, Minyi Shao, Xiaohui Nie Member, IEEE, Kaiwen Yang, Xingda Li, Bowen Hao,
Shenglin Zhang, Member, IEEE, Changhua Pei, Dongbiao He, Yanbiao Li, Dan Pei, Senior Member, IEEE
Abstract—ThegrowingcomplexityofmodernInternetapplica- userexperience.Itenablesthereal-timeidentificationofissues
tions and the widespread use of microservice architectures have within the service interaction network, facilitating the prompt
amplifiedtheneedforefficienttraceanomalydetectiontomain-
localizationandresolutionoffaultsandtherebypreventingser-
tain system stability. Despite the fact that many trace anomaly
vice interruptions or performance degradation [4]. Moreover,
detectionalgorithmshavebeenproposedtoidentifyabnormalbe-
haviors, a comprehensive evaluation of these methods is lacking, tracing request propagation paths is essential for enhancing
whichmakesitdifficultfordeveloperstochoosethemostsuitable system observability and maintainability. Developers can gain
algorithm for real-world applications. To address this gap, we a comprehensive understanding of service interaction patterns
present TADBench, a comprehensive and extensible benchmark
by monitoring the dependencies and sequences of service
for trace anomaly detection. TADBench consolidates diverse
calls, which allows them to optimize service performance and
publicly available trace datasets and algorithms into a unified
repository, standardizes data formats, and incorporates manual improve system stability [5] [6]. Furthermore, historical trace
anomaly labels. To ensure reproducibility and fair comparisons, analysis can reveal long-term performance trends and abnor-
we propose a modular evaluation framework supporting end- mal patterns, offering crucial insights for system optimization
to-end model assessment. Additionally, we provide practical
andfuturearchitecturalimprovements[7].Thus,effectivetrace
guidanceforalgorithmselectionbasedonspecificdataattributes
anomaly detection technologies are vital for comprehensively
by evaluating their performance across datasets with different
characteristics, thereby effectively bridging the gap between understanding system states and ensuring the stable operation
academicresearchandindustrialdeployment.Tothebestofour and efficient management of microservice systems.
knowledge,thisisthefirstcomprehensiveempiricalstudyoftrace Nowadays, many trace anomaly detection algorithms have
anomaly detection algorithms. Our findings aim to facilitate the
been developed to swiftly identify potential abnormal behav-
adoption of these methods in production environments, offering
iors. Despite extensive research in this field, comprehensive
actionable insights for developers and researchers.
public benchmarks for evaluating these algorithms remain
Index Terms—Trace anomaly detection, Empirical study.
largely unavailable. This gap can be attributed to several
challenges:
I. INTRODUCTION (1) Data availability. Although many anomaly detection
algorithms and trace datasets have been open-sourced, pre-
IN recent years, the rapid development of modern Internet
vious efforts have failed to systematically consolidate these
applications,accompaniedbytheexpansionofbusinessop-
valuable resources. This lack of integration makes it difficult
erations,hasledtoasignificantincreaseinsystemcomplexity.
for researchers to access datasets and tools efficiently, as
Microservice architecture [1] has emerged as the preferred
well as to conduct meaningful comparisons and validations
architectural choice for many Internet applications due to its
of existing methods. Besides, existing trace datasets generally
well-documented advantages in scalability, flexibility, main-
lack well-defined anomaly labels, limiting their utility and the
tainability, and efficient resource use [2] [3]. This architecture
accuracy of anomaly detection models. Inconsistency in data
enables developers and engineers to independently develop,
formatsalsomakesdataprocessingandanalysismoredifficult,
deploy and update services, greatly boosting development
further complicating subsequent research efforts.
efficiency andsystem responsiveness [1]. However,the highly
(2) Absence of standardized evaluation framework. In-
modular and distributed structure also poses challenges in
consistent data preprocessing methods, inaccurate algorithm
system monitoring and management.
implementations, and the lack of unified testing pipelines
Toensurethesmoothoperationandefficientmanagementof
contributetoreproducibilityproblems.Inadditiontomakingit
microservicesystems,traceanomalydetectionservesasanin-
challenging to compare algorithms equitably, these drawbacks
dispensabletoolformaintainingservicequalityandenhancing
impede innovation by directing researchers’ focus away from
developing novel approaches and into redundant implementa-
Yongqian Sun, Minyi Shao, Kaiwen Yang, Xingda Li, Bowen Hao, and
ShenglinZhangarewiththeCollegeofSoftware,NankaiUniversity,Tianjin tion tasks.
300071,China(e-mail:sunyongqian@nankai.edu.cn,{2120230754,2112122, (3)Difficultyinalgorithmadoptionfordifferentapplica-
2210352,2120230749}@mail.nankai.edu.cn,zhangsl@nankai.edu.cn).
tions.Whileseveralalgorithmsmayperformbetterindifferent
Xiaohui Nie, Changhua Pei, Dongbiao He, and Yanbiao Li are with
Computer Network Information Center (CNIC), Chinese Academy of Sci- scenarios,itisstilldifficultforoperationspersonneltoquickly
ences (CAS), Beijing 100083, China (e-mail: xhnie, chpei@cnic.cn, her- identify the optimal algorithm for real-world production en-
bertt12@gmail.com,lybmath@cnic.cn).(correspondingauthor:XiaohuiNie.)
vironments. Limited empirical analysis and recommendation
DanPeiiswiththeDepartmentofComputerScienceandTechnology,Ts-
inghuaUniversity,Beijing100084,China(e-mail:peidan@tsinghua.edu.cn.) strategies further exacerbate the difficulties in selecting and
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore. Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
2
applying anomaly detection algorithms, which may lower the enabling systems to be more modular, scalable, flexible, and
effectiveness of troubleshooting. durable. In this architecture, an application is composed of
To tackle these challenges, we propose TADBench, a com- a collection of loosely coupled services, each responsible
prehensiveandextensiblebenchmarkfortraceanomalydetec- for a specific business function. These services communi-
tion.TADBenchmakesdiversepubliclyavailabletracedatasets cate with each other through lightweight protocols and are
and algorithms into a unified repository with standard data independently deployable, allowing for rapid iteration and
formats and accurate anomaly labels. For Challenge 1: We fault isolation. However, as the number of services grows,
collect, organize, and make a publicly available repository trackingandmanagingtheirinteractionsbecomesincreasingly
containing trace datasets and anomaly detection algorithms. complex. This is where distributed tracing plays a crucial
This repository provides researchers with the necessary re- role. As illustrated in Fig. 1, a microservice system typically
sourcesforin-depthstudyandcomprehensivecomparisons.In consistsofthreelayers:theservicelayer,wheremicroservices
addition,westandardizetheformatsofavailabletracedatasets like ts-travel-service and ts-ticketinfo-service function; the
and provide anomaly labels based on human feedback. These containerlayer,whichprovidesruntimeenvironmentsforthese
enhancementssignificantlyimprovethedatasets’usabilityand services, ensuring resource isolation and scalability; and the
ensure greater accuracy for future analysis. For Challenge 2: server layer, where the containers are hosted on physical or
| In response | to      | the lack of     | a standardized |           | evaluation | frame-        | virtual machines. |     |     |     |     |     |
| ----------- | ------- | --------------- | -------------- | --------- | ---------- | ------------- | ----------------- | --- | --- | --- | --- | --- |
| work, we    | develop | a comprehensive |                | framework |            | that includes |                   |     |     |     |     |     |
Distributedtracingrecordstheflowofrequestsastheyprop-
trace collection, trace preprocessing, model adaptation, and agatethroughdifferentsystemcomponents,givinginsightinto
model evaluation. This enables thorough empirical assess- how microservices interact with one another. By tracing each
ments of diverse algorithms across multiple datasets, ensur- request’s path across different services, it becomes possible
ing reproducibility and promoting robust comparative studies. to understand not only the performance attributes of distinct
| For Challenge |     | 3: Based | on extensive |     | experimental | results, |          |                |              |     |              |          |
| ------------- | --- | -------- | ------------ | --- | ------------ | -------- | -------- | -------------- | ------------ | --- | ------------ | -------- |
|               |     |          |              |     |              |          | services | but also their | dependencies | and | interactions | with one |
we propose tailored recommendation strategies for selecting another. Common distributed tracing systems mainly include
anomaly detection algorithms. These strategies account for Jaeger [8], Zipkin [9], and SkyWalking [10], all of which
theuniquecharacteristicsofvarioustracedatasetsandprovide adhere to the OpenTracing [11] specification. OpenTracing
practicalguidanceforselectingthemostappropriatealgorithm defines two core components: traces and spans. Traces serve
| for specific | scenarios. |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
asessentialtoolsfordescribingtheexecutionpathsofrequests
The key contributions of this paper can be summarized as and play a pivotal role in comprehending and evaluating
follows: systembehavior.Conceptually,atracecanberepresentedasa
(1) Public Benchmark. We establish an open-source repos- directedacyclicgraph(DAG)thatencapsulatesalltheservices
itory containing trace data and algorithms and offer and operations involved in processing a request, along with
| a unified |     | and standardized |     | benchmark |     | for evaluating |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
theirtemporaldependencies,therebyprovidingaholisticview
| trace | anomaly | detection | algorithms. |     | The | open-source | of system | behavior. |     |     |     |     |
| ----- | ------- | --------- | ----------- | --- | --- | ----------- | --------- | --------- | --- | --- | --- | --- |
data repository has a total size of 3.6 GB, containing An example of trace is shown in Fig. 1. The illustrated
approximately 1.04 million traces. Our code is available trace comprises seven spans, with each span representing a
at https://github.com/nkalgo/TADBench.git. specific service call. Each trace is uniquely identified by its
| (2) Accurate |     | Data Labeling. | We  | standardize |     | available trace |           |               |          |           |     |              |
| ------------ | --- | -------------- | --- | ----------- | --- | --------------- | --------- | ------------- | -------- | --------- | --- | ------------ |
|              |     |                |     |             |     |                 | own trace | ID, providing | a global | reference | for | tracking the |
datasets and provide manually labeled anomaly annota- entire execution flow. Meanwhile, each individual span in the
tions, improving the datasets’ quality and applicability. trace captures detailed call-related information, including the
Around210,000tracesarelabeledasstructuralanomalies traceID,auniquespanID,andtheparentspanID.Theparent
or latency anomalies. span ID establishes hierarchical relationships among spans,
(3) Empirical Study. In response to the question of whether thusconstructingthestructureoftheentiretrace.Furthermore,
a universally effective trace anomaly detection algo- spans typically record time-related information such as the
rithmexists,weconductacomprehensiveandsystematic start time and duration, as well as the service name, specific
| empirical   |     | study of trace    | anomaly |              | detection | algorithms,    |           |           |              |     |     |     |
| ----------- | --- | ----------------- | ------- | ------------ | --------- | -------------- | --------- | --------- | ------------ | --- | --- | --- |
|             |     |                   |         |              |           |                | operation | name, and | status code. |     |     |     |
| analyzing   |     | their performance |         | across       | several   | datasets and   |           |           |              |     |     |     |
| identifying |     | their strengths   | and     | limitations. |           | To the best of |           |           |              |     |     |     |
B. Trace Anomalies
| our | knowledge, | this | is the | first comprehensive |     | empirical |     |     |     |     |     |     |
| --- | ---------- | ---- | ------ | ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
study in this area. Trace data is primarily utilized for system operation and
(4) Algorithm Recommendation Strategies. We propose maintenance, supporting tasks such as fault diagnosis, root
data-driven recommendation strategies for selecting the cause analysis, and system visualization. Among these tasks,
most suitable anomaly detection algorithms based on trace anomaly detection is of particular importance. Generally
trace characteristics and operational requirements. speaking,traceanomaliescanbecategorizedintotwoprimary
types:
|     |     | II. BACKGROUND |     |     |     |     |         |            |         |           |       |          |
| --- | --- | -------------- | --- | --- | --- | --- | ------- | ---------- | ------- | --------- | ----- | -------- |
|     |     |                |     |     |     |     | Latency | Anomalies. | Latency | anomalies | occur | when the |
A. Trace Structure
|     |     |     |     |     |     |     | execution | time of an | operation | exceeds | its normal | range, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------- | ------- | ---------- | ------ |
Microservice architecture has fundamentally transformed which can be detected when spans exhibit abnormally long
the way modern applications are developed and operated, durations.Typically,suchanomaliesnotonlyimpactthetarget
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
3
|     |     |     |     |     |     |     |     |                |     | Fig.           | 2: Latency |          | Anomaly     |         |          |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | ---------- | -------- | ----------- | ------- | -------- |
|     |     |     |     |     |     |     |     | logic failures |     | (e.g., circuit |            | breakers | redirecting | traffic | to unin- |
tendedornon-redundantservices),ordependencymismatches
|     |     |     |     |     |     |     |     | (e.g., API | version | upgradation |     | without | backward |     | compatibil- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | ------- | -------- | --- | ----------- |
ity).Thesebusiness-relatedconfigurationordeploymentissues
|     |     |     |     |     |     |     |     | can inadvertently |     | cause | services | to  | interact | with | incorrect or |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----- | -------- | --- | -------- | ---- | ------------ |
unexpectedcounterparts,therebyintroducinganomaliesinthe
|     |     |     |     |     |     |     |     | expected        | trace.   |         |           |             |      |             |            |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ------- | --------- | ----------- | ---- | ----------- | ---------- |
|     |     |     |     |     |     |     |     | Missing         | calls    | refer   | to        | cases where |      | an expected | service    |
|     |     |     |     |     |     |     |     | or operation    | is       | absent, | like      | Service     | E is | missing     | in Fig. 4. |
|     |     |     |     |     |     |     |     | These anomalies |          | may     | be caused | not         | only | by system   | failures   |
|     |     |     |     |     |     |     |     | or network      | latency, |         | but more  | critically  |      | by business | process    |
incompleteness.Forinstance,aworkflowstepmaybeskipped
|     |     |     |     |     |     |     |     | due to | unmet | preconditions |     | such | as data | validation | failures, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------------- | --- | ---- | ------- | ---------- | --------- |
Fig. 1: Microservice System and Trace authorizationdenials,orbusinessruleviolations.Additionally,
|     |     |     |     |     |     |     |     | service | outages, | communication |     |     | timeouts, | or misconfigured |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------------- | --- | --- | --------- | ---------------- | --- |
routing(suchasincorrectserviceaddresses,unpublishedAPIs,
|               |       |           |           |         |         |             |          | or authentication |         | failures) |      | can also | interrupt | the normal   | flow, |
| ------------- | ----- | --------- | --------- | ------- | ------- | ----------- | -------- | ----------------- | ------- | --------- | ---- | -------- | --------- | ------------ | ----- |
| service but   | can   | also have | cascading |         | effects | on its      | upstream |                   |         |           |      |          |           |              |       |
|               |       |           |           |         |         |             |          | preventing        | certain | calls     | from | being    | made.     | Furthermore, | oper- |
| dependencies, | which | may       | impair    | overall | system  | performance |          |                   |         |           |      |          |           |              |       |
and have a negative impact on user experience. For instance, ationaldecisionssuchastemporaryservicedisruptionsduring
|          |        |        |            |      |           |     |            | deployments |     | may lead | to  | the absence |     | of expected | service |
| -------- | ------ | ------ | ---------- | ---- | --------- | --- | ---------- | ----------- | --- | -------- | --- | ----------- | --- | ----------- | ------- |
| Spans 0, | 1, and | 2 have | abnormally | high | latencies |     | of 237 ms, |             |     |          |     |             |     |             |         |
235 ms, and 230 ms, respectively, as illustrated in Fig. 2. interactions in the trace.
|             |     |             |     |         |           |     |         | Moreover, |     | call order | errors | occur | when | the sequence | of  |
| ----------- | --- | ----------- | --- | ------- | --------- | --- | ------- | --------- | --- | ---------- | ------ | ----- | ---- | ------------ | --- |
| The reasons |     | for causing |     | latency | anomalies | may | include |           |     |            |        |       |      |              |     |
performance bottlenecks, resource contention, and network service invocations deviates from the expected order. For
|     |     |     |     |     |     |     |     | example, | in Fig. | 5,  | Service | F mistakenly |     | invokes | Service E, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | ------- | ------------ | --- | ------- | ---------- |
delays.Forexample,abottleneckwithinaservice’sprocessing
|                    |     |          |         |     |           |     |        | whereas | it should | have | been | Service | B   | invoking | Service E. |
| ------------------ | --- | -------- | ------- | --- | --------- | --- | ------ | ------- | --------- | ---- | ---- | ------- | --- | -------- | ---------- |
| (e.g., inefficient |     | database | queries | or  | excessive | CPU | usage) |         |           |      |      |         |     |          |            |
directlyextendstheexecutiontimeofthecorrespondingspan. Such errors often stem not merely from race conditions in
asynchronoussystems,butmorespecificallyfromconcurrency
Similarly,contentionforlimitedresources(e.g.,memory,disk
I/O,orthreadpoolcapacity)increasesoperationwaitingtimes, control issues in event-driven architectures where events are
|     |     |     |     |     |     |     |     | processed | in  | improper | sequences, |     | violating | logical | depen- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ---------- | --- | --------- | ------- | ------ |
therebyamplifyingservicelatency.Inaddition,anomalousnet-
|                  |     |           |        |      |               |     |         | dencies | between | services. | Moreover, |     | version | incompatibilities |     |
| ---------------- | --- | --------- | ------ | ---- | ------------- | --- | ------- | ------- | ------- | --------- | --------- | --- | ------- | ----------------- | --- |
| work conditions, |     | including | packet | loss | or congestion |     | between |         |         |           |           |     |         |                   |     |
microservices, introduce transmission delays in requests and between microservices can induce unintended temporal se-
quencingofoperations,whichoftenmaterializesasobservable
| responses, | further | prolongs | trace | latency | beyond |     | its normal |     |     |     |     |     |     |     |     |
| ---------- | ------- | -------- | ----- | ------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
statistical range. These issues are reflected in trace data as structural anomalies in the trace.
| abnormally          | prolonged     |            | durations          | of specific   |            | spans,      | leading    | to  |      |               |     |         |              |     |     |
| ------------------- | ------------- | ---------- | ------------------ | ------------- | ---------- | ----------- | ---------- | --- | ---- | ------------- | --- | ------- | ------------ | --- | --- |
| service-level       | latency       | that       | exceeds            | the           | normal     | statistical | range.     |     |      |               |     |         |              |     |     |
| Structural          | Anomalies.    |            | Deviations         |               | from       | expected    | service    |     |      |               |     |         |              |     |     |
| invocation          | sequences     | inside     |                    | a trace       | are known  | as          | structural |     |      |               |     |         |              |     |     |
| anomalies.          | These         | deviations |                    | may include   | unexpected |             | service    |     |      |               |     |         |              |     |     |
| calls, missing      | calls,        | and        | call               | order errors. |            |             |            |     |      |               |     |         |              |     |     |
| Unexpected          |               | service    | calls occur        | when          | a service  | or          | operation  |     |      |               |     |         |              |     |     |
| is invoked          | unexpectedly, |            | as shown           | in            | Fig. 3,    | where       | Service    | B   |      |               |     |         |              |     |     |
| incorrectly         | invokes       | Service    | G                  | instead       | of Service | E.          | This type  |     |      |               |     |         |              |     |     |
|                     |               |            |                    |               |            |             |            |     | Fig. | 3: Structural |     | Anomaly | (unexpected) |     |     |
| of anomaly          | may           | result     | from configuration |               | drift      | (e.g.,      | outdated   |     |      |               |     |         |              |     |     |
| service registries) |               | leading    | to                 | incorrect     | routing    | rules,      | fallback   |     |      |               |     |         |              |     |     |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
4
|     |     | normal       | trace patterns. | It                | uses | a Service | Trace    | Vector    | (STV)      |
| --- | --- | ------------ | --------------- | ----------------- | ---- | --------- | -------- | --------- | ---------- |
|     |     | to represent | data,           | with              | each | dimension | denoting |           | a distinct |
|     |     | call path    | and             | the corresponding |      | response  | time     | indicated | by         |
its value.
|     |     | CRISP.        | Adopting | the   | same         | anomaly | detection |               | model as |
| --- | --- | ------------- | -------- | ----- | ------------ | ------- | --------- | ------------- | -------- |
|     |     | TraceAnomaly, |          | CRISP | [16] encodes |         | traces    | by extracting | the      |
criticalpathusingarecursivealgorithm.ItconstructsaService
|                    |                   | Critical        | Path Vector  | (SCPV)            |                | by subtracting |               | the durations | of         |
| ------------------ | ----------------- | --------------- | ------------ | ----------------- | -------------- | -------------- | ------------- | ------------- | ---------- |
|                    |                   | child spans     | when         | recording         | spans          | on             | the critical  | path.         |            |
| Fig. 4: Structural | Anomaly (missing) |                 |              |                   |                |                |               |               |            |
|                    |                   | TraceVAE.       |              | Using             | Graph-VAE      |                | architectures |               | [17]–[19], |
|                    |                   | TraceVAE        | [20]         | separately        | models         |                | structural    | and           | temporal   |
|                    |                   | features        | via a        | structure         | VAE            | and a time     | VAE.          | Additionally, |            |
|                    |                   | TraceVAE        | incorporates |                   | Graph          | Attention      | Networks      |               | (GATs)     |
|                    |                   | [21] to capture |              | correlations      | among          | nodes          | in            | the trace     | graphs.    |
|                    |                   | GTrace.         | By           | combining         | graph-wise     |                | and           | node-wise     | VAE        |
|                    |                   | models,         | GTrace       | [12] reconstructs |                | both           | structural    | and           | latency    |
|                    |                   | features        | of trace     | graphs.           | To             | enhance        | detection     | efficiency,   | it         |
|                    |                   | groups traces   | with         | the same          | substructures. |                | Moreover,     |               | GTrace     |
adoptsTree-LSTM[22]togeneratesharedencodingsforiden-
|                    |                        | tical sub-tree | structures, |             | further | supporting                 |                 | its substructure- |       |
| ------------------ | ---------------------- | -------------- | ----------- | ----------- | ------- | -------------------------- | --------------- | ----------------- | ----- |
|                    |                        | based grouping |             | strategy.   |         |                            |                 |                   |       |
| Fig. 5: Structural | Anomaly (out-of-order) | 2)             |             | Algorithms: |         |                            |                 |                   |       |
|                    |                        | GNN-based      |             |             |         | Inthiscategory,GraphNeural |                 |                   |       |
|                    |                        | Networks       | (GNNs)      | [23],       | [24]    | serve as                   | the foundation. |                   | These |
modelsexcelatcapturingstructuralandrelationalinformation
| C. Trace Anomaly Detection | Algorithms |     |     |     |     |     |     |     |     |
| -------------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
in trace graphs.
Manyalgorithmsfortraceanomalydetectionexhibitunique PUTraceAD. As a semi-supervised anomaly detection
design principles and robust performance under specific con- method, PUTraceAD [25] trains a model based on GATs and
ditions. Traditionally, algorithms in this domain have been the nnPU [26] algorithm using a limited amount of labeled
categorized into statistic-based and model-based approaches abnormal traces. Notably, when generating graph represen-
[12]. However, as deep learning has become more and more tations for traces, PUTraceAD uses WordPiece [27] and a
popular, an increasing number of algorithms now employ pre-trained BERT model [28] to generate 768-dimensional
deep learning models, rendering the traditional classification embeddings for service and operation names while creating
inadequateforcapturingthecomplexityanddiversityofstate- graph representations for traces.
of-the-art trace anomaly detection techniques. To address this TraceCRL. Following the GraphCL (Graph Contrastive
limitation, we propose a classification based on underlying Learning with Augmentations) framework [29], TraceCRL
architectures, providing a more precise and systematic frame- [30] leverages contrastive learning and graph neural networks
work. Accordingly, we divide these algorithms into three to learn effective trace representations. Initially, it utilizes
main categories: VAE-based, GNN-based, and LSTM-based DeepWalk [31] to generate vector representations for each
algorithms, which represent the dominant design paradigms operation.Comparedtootheralgorithmsthatonlyuseduration
in the field. An overview of this classification is presented in as the temporal feature for each invocation, TraceCRL incor-
Fig. 6. Except for PUTraceAD, which is a semi supervised porates more detailed temporal features, such as the quantile
learning algorithm, all others in Fig. 6 are unsupervised. of the invocation’s start time and the proportion of the local
|     |     | execution     | time.     | By employing |          | One-Class |               | SVM    | [32] as a |
| --- | --- | ------------- | --------- | ------------ | -------- | --------- | ------------- | ------ | --------- |
|     |     | subsequent    | detection | model,       |          | TraceCRL  | is            | widely | used for  |
|     |     | anomaly       | detection | tasks.       |          |           |               |        |           |
|     |     | 3) LSTM-based |           | Algorithms:  |          | Long      | Short-Term    |        | Memory    |
|     |     | (LSTM)        | networks  | [33]         | are used | in        | this category |        | to model  |
sequentialdependenciesanddetectbothlatencyandstructural
|     |     | anomalies | in traces. |     |     |     |     |     |     |
| --- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
Fig. 6: Algorithm Overview Multimodal LSTM. Multimodal LSTM [34] combines
|     |     | temporal | and | structural | features | into | a joint | representation. |     |
| --- | --- | -------- | --- | ---------- | -------- | ---- | ------- | --------------- | --- |
1) VAE-based Algorithms: Variational Autoencoders Each span is encoded using a vector with one-hot call path
(VAEs) [13] serve as the core model for this category. encoding and normalized duration. Rare calls are excluded to
These methods aim to reconstruct normal patterns in trace reduce noise and maintain consistency. LSTM networks are
data, leveraging the learned latent representations to identify applied to model the sequential relationships.
anomalies. In summary, a wide range of trace anomaly detection
TraceAnomaly. TraceAnomaly [14] employs deep varia- algorithms have been developed in recent years, each with
tional Bayesian networks with posterior flow [15] to model uniquedesignmodels.Selectinganappropriatedetectionalgo-
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
5
|     |     |     |     |     |     | Fig. | 7: Evaluation | Framework |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
rithm for real-world applications remains a critical challenge. field names, the number of fields, and the units of values. In
This paper aims to address this issue by conducting a com- previousexperiments,researchersoftenhadtopreprocesseach
prehensive evaluation of various algorithms under different datasetseparatelytomeettheformatrequirementsofdifferent
conditions. Through extensive experiments, we systematically algorithms. When new datasets emerged, adapting them to
analyze their performance, highlight their advantages and variousalgorithmswastime-consumingandseverelyhindered
drawbacks, and provide recommendations for the most effec- experimental progress. Furthermore, there were significant
tive selection strategy. difficulties in comparing the features of various datasets or
|     |     |      |                |     |     |     |     | combining | them. |     |     |     |     |     |
| --- | --- | ---- | -------------- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- |
|     |     | III. | TADBenchDESIGN |     |     |     |     |           |       |     |     |     |     |     |
Tosystematicallyevaluatetheperformanceoftraceanomaly
| detection        | algorithms,     | we             | propose       | an        | evaluation  |              | framework   |          |            |           |       |         |                      |     |
| ---------------- | --------------- | -------------- | ------------- | --------- | ----------- | ------------ | ----------- | -------- | ---------- | --------- | ----- | ------- | -------------------- | --- |
| depicted         | in Fig.         | 7, which       | consists      | of        | four        | main stages: | trace       |          |            |           |       |         |                      |     |
| collection,      | trace           | preprocessing, |               | model     | adaptation, |              | and model   |          |            |           |       |         |                      |     |
| evaluation.      | First,          | we collect     | the           | available | trace       | data,        | followed    |          |            |           |       |         |                      |     |
| by preprocessing |                 | to standardize |               | the       | data        | format.      | Next, the   |          |            |           |       |         |                      |     |
|                  |                 |                |               |           |             |              |             | (a) Data | Format for | GAIA      | (b)   | Data    | Format for AIOps2022 |     |
| algorithms       | needs           | to ensure      | proper        | data      | format      | adaptation   |             | to       |            |           |       |         |                      |     |
|                  |                 |                |               |           |             |              |             |          | Fig. 8:    | Different | Trace | Formats |                      |     |
| receive          | and process     | the            | pre-processed |           | data        | for          | evaluation. |          |            |           |       |         |                      |     |
| Finally,         | the performance |                | of different  |           | algorithms  | is           | evaluated   |          |            |           |       |         |                      |     |
based on the experimental results. To address these challenges, we propose a standardized
|            |          |            |         |          |          |     |          | format consisting | of          | two primary | classes: |          | Trace and Span, | as     |
| ---------- | -------- | ---------- | ------- | -------- | -------- | --- | -------- | ----------------- | ----------- | ----------- | -------- | -------- | --------------- | ------ |
| A. Dataset | Overview | and        | Unified | Format   |          |     |          |                   |             |             |          |          |                 |        |
|            |          |            |         |          |          |     |          | demonstrated      | in Fig.     | 9.          |          |          |                 |        |
| In this    | study,   | we conduct | an      | in-depth | analysis | of  | multiple |                   |             |             |          |          |                 |        |
|            |          |            |         |          |          |     |          | • Trace           | Class. Each | trace       | is       | uniquely | identified      | by its |
datasets, including TrainTicket [35], [36], GAIA (Generic trace id and contains fields such as root span (denoting
AIOps Atlas) [37], AIOps2020 [38], AIOps2022 [39] and the start of the trace) and span count (denoting the total
| AIOps2023. | These | datasets | are | generally | based | on  | the Open- |        |            |     |         |      |                   |     |
| ---------- | ----- | -------- | --- | --------- | ----- | --- | --------- | ------ | ---------- | --- | ------- | ---- | ----------------- | --- |
|            |       |          |     |           |       |     |           | number | of spans). | The | anomaly | type | field categorizes |     |
Tracing format mentioned in Section II-A. anomalies into four types: 0 (normal), 1 (only latency
• TrainTicket: The TrainTicket dataset, sourced from the anomaly), 2 (only structural anomaly), and 3 (both la-
open-source data in the PUTraceAD [25] paper, is gen- tency and structural anomalies). Additionally, the source
erated through fault injection in the microservice system field denotes the data source.
TrainTicket. • Span Class. Each span records detailed call information,
GAIA: GAIA, dedicated to anomaly detection, log anal- including trace id, span id, parent span id, and chil-
•
ysis, and fault localization, is derived from CloudWise dren span id, which collectively construct the trace tree.
microservice simulation system. Eachspanalsocontainstimeinformation(start timeand
AIOps2020, AIOps2022 and AIOps2023: The duration), service and operation details (service name
•
AIOps2020, AIOps2022, and AIOps2023 datasets and operation name), anomaly labels (anomaly) and sta-
originate from the CCF International AIOps Challenge tus information (status code). The latency and structure
held in 2020, 2022, and 2023 respectively. AIOps2020 fields further specify latency and structural anomaly,
originates from a real-world production microservice whiletheextrafieldcapturesadditionalcontextualdetails.
| system, | while | AIOps2022 |     | and | AIOps2023 |     | simulate |              |        |            |     |      |               |     |
| ------- | ----- | --------- | --- | --- | --------- | --- | -------- | ------------ | ------ | ---------- | --- | ---- | ------------- | --- |
|         |       |           |     |     |           |     |          | This unified | format | eliminates | the | need | to preprocess | raw |
anomalies through fault injection. dataforeachalgorithmseparately.Instead,wemerelyconvert
However, the specific details in different datasets may the data into this unified format, and then adapt the format
vary, as exemplified by the GAIA and AIOps2022 datasets to various algorithms. Consequently, each new dataset in any
shown in Fig. 8a and Fig. 8b, respectively. These differences formatcanbecompatiblewithanyalgorithmwithouttheneed
encompass various aspects, including the meaning of fields, for extra data preprocessing once it has been converted to
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
6
|     |     |     |     |     |     | TABLE | I: Dataset | Characteristics |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
AverageTraceDepth AverageSpanNumbers Granularity ServiceScale AverageServiceNumber OperationScale AverageOperationNumber
|             |     |     |     | perTrace |     |           |     |            | perTrace    |          |             |           |         | perTrace      |     |
| ----------- | --- | --- | --- | -------- | --- | --------- | --- | ---------- | ----------- | -------- | ----------- | --------- | ------- | ------------- | --- |
| TrainTicket | 3.3 |     |     | 39.0     |     | Operation |     | 29         |             | 5.9      |             | 64        |         | 7.6           |     |
| GAIA        | 4.7 |     |     | 9.3      |     | Service   |     | 10         |             | 6.4      |             | -         |         | -             |     |
| AIOps2020   | 5.5 |     |     | 23.1     |     | Service   |     | 10         |             | 7.8      |             | -         |         | -             |     |
| AIOps2022   | 4.2 |     |     | 21.7     |     | Operation |     | 40         |             | 6.9      |             | 29        |         | 11.6          |     |
| AIOps2023   | 3.8 |     |     | 14.5     |     | Service   |     | 37         |             | 1.3      |             | -         |         | -             |     |
|             |     |     |     |          |     |           |     |            | TABLE       | II:      | Dataset     | Anomaly   | Ratio   |               |     |
|             |     |     |     |          |     |           |     |            |             |          | Total       | Structure | Latency |               |     |
|             |     |     |     |          |     |           |     |            | TrainTicket |          | 32.9%       | 26.7%     | 28.5%   |               |     |
|             |     |     |     |          |     |           |     |            | GAIA        |          | 49.9%       | 21.8%     | 29.9%   |               |     |
|             |     |     |     |          |     |           |     |            | AIOps2020   |          | 21.8%       | 3.5%      | 21.5%   |               |     |
|             |     |     |     |          |     |           |     |            | AIOps2022   |          | 36.3%       | 4.0%      | 35.9%   |               |     |
|             |     |     |     |          |     |           |     |            | AIOps2023   |          | 53.6%       | 39.0%     | 24.0%   |               |     |
|             |     |     |     |          |     |           |     | B. Dataset | Labeling    |          |             |           |         |               |     |
|             |     |     |     |          |     |           |     | Despite    | being       | publicly | accessible, |           | the     | five datasets | are |
generallycollectedsystematicallywithoutspecificlabels.Con-
sequently,researcherscannotdirectlydistinguishbetweennor-
|     |     |         |         |        |     |     |     | mal and          | abnormal   | traces          | in these     | datasets,   | posing       |              | challenges |
| --- | --- | ------- | ------- | ------ | --- | --- | --- | ---------------- | ---------- | --------------- | ------------ | ----------- | ------------ | ------------ | ---------- |
|     |     |         |         |        |     |     |     | for further      | analysis   | and             | application. | Without     |              | proper       | labeling,  |
|     |     |         |         |        |     |     |     | it is impossible |            | to successfully |              | validate    | the          | performance  | of         |
|     |     |         |         |        |     |     |     | anomaly          | detection  | algorithms.     |              | Therefore,  |              | recognizing  | that       |
|     |     |         |         |        |     |     |     | trace anomalies  |            | are generally   |              | categorized |              | into latency | and        |
|     |     |         |         |        |     |     |     | structural       | anomalies, | we              | develop      | the         | labeling     | process      | shown      |
|     |     |         |         |        |     |     |     | in Fig.          | 10.        |                 |              |             |              |              |            |
|     |     |         |         |        |     |     |     | These            | datasets   | usually         | contain      | fault       | microservice |              | infor-     |
|     |     |         |         |        |     |     |     | mation           | and fault  | occurrence      | time.        | Using       | this         | critical     | data,      |
|     |     |         |         |        |     |     |     | we divide        | the        | traces into     | two          | categories: | normal       |              | traces and |
|     |     | Fig. 9: | Unified | Format |     |     |     |                  |            |                 |              |             |              |              |            |
fault-injectedtraces.Forlatencyanomalydetection,weassess
|               |                            |                 |                  |                    |              |                |           | whether               | the latency   | of each             | service     | in           | a fault-injected |                | trace     |
| ------------- | -------------------------- | --------------- | ---------------- | ------------------ | ------------ | -------------- | --------- | --------------------- | ------------- | ------------------- | ----------- | ------------ | ---------------- | -------------- | --------- |
|               |                            |                 |                  |                    |              |                |           | falls within          | the           | normal              | range.      | As discussed |                  | in Section     | II-B,     |
| the unified   | format.                    | Besides,        | this             | unified            | format       | supports       |           | a                     |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | some business-related |               | anomalies—such      |             |              | as               | performance    | bot-      |
| systematic    | comparison                 | of              | datasets,        | enabling           |              | operators      | to gain   |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | tlenecks,             | resource      | contention,         |             | and network  |                  | delays—produce |           |
| deeper        | insight into               | system          | behavior,        | and                | facilitating |                | efficient |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | detectable            | latency       | distribution        | shifts      | in           | trace            | data. To       | enhance   |
| anomaly       | diagnosis                  | and resolution. |                  |                    |              |                |           |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | accuracy,             | we            | group services      | based       | on           | their            | shared         | calling   |
| To evaluate   | the                        | differences     | between          |                    | the          | five datasets, |           | we                    |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | paths from            | the           | root service,       |             | rather       | than relying     |                | solely on |
| examine       | their respective           |                 | characteristics, |                    | with         | the results    | sum-      |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | service               | names.        | Next, we            | use a       | Gaussian     | distribution     |                | to model  |
| marized       | in Table I.                | Key features    |                  | are systematically |              |                | compared  |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | the service           | latency       | distribution        |             | in normal    | traces.          | Specifically,  |           |
| in the table, | with                       | particular      | attention        |                    | paid         | to differences |           | in                    |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | let µ and             | σ denote      | the                 | mean        | and standard |                  | deviation      | of the    |
| average       | trace depth                | (ranging        | from             | 3.3                | to 5.5),     | average        | span      |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | latency               | distribution, | respectively.       |             | A            | service          | latency        | L in a    |
| numbers       | per trace                  | (ranging        | from             | 9.3                | to 39.0),    | monitoring     |           |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           | fault-injected        |               | trace is considered |             | abnormal     | if               | it satisfies:  |           |
| granularity   | (service/operation-level), |                 |                  |                    | service      | scale          | (ranging  |                       |               |                     |             |              |                  |                |           |
| from 10       | to 40), average            |                 | service          | numbers            | per          | trace          | (ranging  |                       |               |                     |             |              |                  |                |           |
|               |                            |                 |                  |                    |              |                |           |                       |               | L∈/                 | [µ−3σ,µ+3σ] |              |                  |                | (1)       |
| from 1.3      | to 7.8),                   | operation       | scale            | (ranging           |              | from 29        | to 64),   |                       |               |                     |             |              |                  |                |           |
and average operation numbers per trace (ranging from 7.6 following the 3-sigma rule, which assumes that 99.73% of
to 11.6). Notably, TrainTicket has the highest operation scale normallydistributeddatafallswithinthreestandarddeviations
(64), while AIOps2022 contains the most services (40). Ad- of the mean. We employ the 3-sigma rule because it is a
ditionally, GAIA, AIOps2020 and AIOps2023 lack operation- statistically robust and widely accepted method for detecting
level metrics. rare, extreme deviations from an established normal pattern
TableIIsummarizestheanomalyratiosforthefivedatasets [14]. If such an anomaly is detected, both the service and the
across three categories: total, structure, and latency. The total trace are labeled as latency anomalies.
anomaly ratios range from 21.8% (AIOps2020) to 53.6% Forstructuralanomalydetection,wecomparethestructural
(AIOps2023). For structural anomalies, the ratios range from differences between faulty and normal traces. Initially, we
3.5% (AIOps2020) and 39.0% (AIOps2023). For latency collect all patterns and their frequencies from normal traces.
anomalies,theratiosrangefrom21.5%(AIOps2020)to35.9% Then, for each fault-injected trace, we examine if its structure
(AIOps2022). exists in the normal dataset. If the structure is rare or absent,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
7
|     |     |     |     |     |     | Fig. 10: | Trace | Labeling Process |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | ---------------- | --- | --- | --- |
we apply the Jaccard similarity to identify the most similar for extra adaptation or modification. More importantly, it
patternfromthenormaltraces.TheJaccardsimilaritybetween facilitates fair and consistent comparisons. The SDK also
two traces T and P is defined as: serves as a scalable and extensible foundation for future
research,enablingrapidprototyping,algorithmbenchmarking,
|S(T)∩S(P)|
J(T,P)= (2) and collaborative development in the field of trace anomaly
|                     |     |      | |S(T)∪S(P)| |            |             |         |        | detection. |     |     |     |
| ------------------- | --- | ---- | ----------- | ---------- | ----------- | ------- | ------ | ---------- | --- | --- | --- |
| where S(T)          | and | S(P) | denote      | the set    | of services | in      | traces | T          |     |     |     |
| and P respectively. |     | We   | then        | select the | most        | similar | normal |            |     |     |     |
pattern through:
P∗
|     |     | =argmaxJ(T,P |     |     | i ) |     | (3) |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Pi∈P
| where P    | is the | collection   | of         | normal      | trace | patterns. | Sub-     |     |     |     |     |
| ---------- | ------ | ------------ | ---------- | ----------- | ----- | --------- | -------- | --- | --- | --- | --- |
| sequently, | we     | perform      | a detailed | examination |       | by        | manually |     |     |     |     |
| comparing  | the    | faulty trace | T          | with the    | most  | similar   | normal   |     |     |     |     |
patternP∗.Thetraceisfinallylabeledasastructuralanomaly
ifthiscomparisonconfirmsthepresenceofdeviationssuchas
| missing       | calls,   | unexpected           | service      | calls,         | or call | order            | errors.   |     |                    |     |     |
| ------------- | -------- | -------------------- | ------------ | -------------- | ------- | ---------------- | --------- | --- | ------------------ | --- | --- |
| C. Algorithm  |          | Adaption             |              |                |         |                  |           |     |                    |     |     |
| In general,   |          | different algorithms |              | often          | call    | for specific     | trace     |     |                    |     |     |
| formats       | in their | architecture.        | In           | prior studies, |         | researchers      | who       |     |                    |     |     |
| intended      | to use   | open-source          | algorithm    |                | code    | had to implement |           |     |                    |     |     |
|               |          |                      |              |                |         |                  |           |     | Fig. 11: Algorithm | SDK |     |
| additional    | data     | preprocessing        |              | steps          | to meet | the              | algorithm |     |                    |     |     |
| requirements, |          | which incurred       | considerable |                | time    | overhead.        | To        |     |                    |     |     |
| address       | this,    | our work             | have         | standardized   |         | the data         | format,   |     |                    |     |     |
allowingustosimplyaddcodetoeachalgorithm’simplemen- D. Evaluation Metrics
tation that converts the unified format into the specific format In this study, we utilize several evaluation metrics to
required by the algorithm. As a result, when a new dataset measure the performance of the anomaly detection models,
|          |            |          |            |     |     |            |         | including Precision, | Recall, F1-score, | Accuracy, | and Time |
| -------- | ---------- | -------- | ---------- | --- | --- | ---------- | ------- | -------------------- | ----------------- | --------- | -------- |
| needs to | be applied | to these | algorithms |     | for | detection, | it only |                      |                   |           |          |
needs to be converted to the standardized format now, which Consumption. These metrics evaluate both the effectiveness
will then be automatically compatible with all algorithms, and efficiency of the trace anomaly detection algorithms.
eliminatingtheneedforcumbersomeformatadjustments.The They are defined as follows, where TP refers to the number
open-source code we have released already incorporates this of anomalous traces accurately detected as anomalies, FP
functionality. refers to the number of normal traces mistakenly detected as
In addition, to ensure the standardization, modularity, and anomalies, FN refers to the number of anomalous traces that
extensibility of algorithm evaluation, we construct an algo- fail to be identified as such, and TN refers to the number of
rithm Software Development Kit (SDK), as illustrated in the normal traces correctly detected as normal.
Fig. 11. By requiring each algorithm to inherit from the Precision: the proportion of real anomalous traces over
•
| common | abstract | base | class, | we standardize |     | the format | of  |                   |                   |           |           |
| ------ | -------- | ---- | ------ | -------------- | --- | ---------- | --- | ----------------- | ----------------- | --------- | --------- |
|        |          |      |        |                |     |            |     | all the predicted | anomalous traces, | which can | be calcu- |
inputs and outputs across different algorithms. This design lated using the following formula:
| not only | simplifies | the | integration | of  | new | algorithms | into |     |     |     |     |
| -------- | ---------- | --- | ----------- | --- | --- | ---------- | ---- | --- | --- | --- | --- |
TP
|                |     |          |          |         |     |        |          |     | Precision= |     | (4) |
| -------------- | --- | -------- | -------- | ------- | --- | ------ | -------- | --- | ---------- | --- | --- |
| the evaluation |     | pipeline | but also | reduces | the | effort | required |     |            |     |     |
TP+FP
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
8
Recall:theproportionofpredictedanomaloustracesover IV. EVALUATION
•
| all the | real anomalous |          | traces, which | can | be calculated |           |          |            |       |        |            |     |             |
| ------- | -------------- | -------- | ------------- | --- | ------------- | --------- | -------- | ---------- | ----- | ------ | ---------- | --- | ----------- |
|         |                |          |               |     |               | In this   | section, | we         | focus | on the | evaluation | to  | address the |
| using   | the following  | formula: |               |     |               |           |          |            |       |        |            |     |             |
|         |                |          |               |     |               | following | research | questions: |       |        |            |     |             |
TP • RQ1: Is there an algorithm that consistently outperforms
|     |     | Recall= |       |     | (5) |        |        |     |           |     |     |     |     |
| --- | --- | ------- | ----- | --- | --- | ------ | ------ | --- | --------- | --- | --- | --- | --- |
|     |     |         | TP+FN |     |     | others | across | all | datasets? |     |     |     |     |
• RQ2:Howwelldothealgorithmsperformacrossvarious
| • F1-score: | the harmonic      |     | mean of   | the precision | and recall, |         |             |        |        |     |           |      |            |
| ----------- | ----------------- | --- | --------- | ------------- | ----------- | ------- | ----------- | ------ | ------ | --- | --------- | ---- | ---------- |
|             |                   |     |           |               |             | dataset | conditions? |        |        |     |           |      |            |
| which       | can be calculated |     | using the | following     | formula:    |         |             |        |        |     |           |      |            |
|             |                   |     |           |               |             | RQ3:    | How         | can we | choose | the | algorithm | that | works best |
•
Precision×Recall
|     |             |     |     |     |     | for | a certain | dataset? |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- |
|     | F1-score=2× |     |     |     | (6) |     |           |          |     |     |     |     |     |
Precision+Recall
| Accuracy: | the proportion |     | of correctly |     | predicted traces | A. Experimental |     | Setup |     |     |     |     |     |
| --------- | -------------- | --- | ------------ | --- | ---------------- | --------------- | --- | ----- | --- | --- | --- | --- | --- |
•
| over | all the traces, | which | can | be calculated | using the |     |     |     |     |     |     |     |     |
| ---- | --------------- | ----- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Afterperforminganomalylabelsoneachofthefivedatasets
| following | formula: |     |     |     |     |            |              |           |       |             |     |           |             |
| --------- | -------- | --- | --- | --- | --- | ---------- | ------------ | --------- | ----- | ----------- | --- | --------- | ----------- |
|           |          |     |     |     |     | including  | TrainTicket, |           | GAIA, | AIOps2020,  |     | AIOps2022 | and         |
|           |          |     |     |     |     | AIOps2023, | we           | evaluated | the   | performance |     | of the    | trace-based |
TP+TN
|     | Accuracy= |     |     |     | (7) |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TP+TN+FP+FN anomalydetectionalgorithmsonthesedatasetsseparately.For
|             |              |     |             |     |                  | each dataset, | we     | divided   | the    | normal | traces       | into | a training set |
| ----------- | ------------ | --- | ----------- | --- | ---------------- | ------------- | ------ | --------- | ------ | ------ | ------------ | ---- | -------------- |
| • Time      | Consumption: | A   | key metric  | for | assessing model  |               |        |           |        |        |              |      |                |
|             |              |     |             |     |                  | and a test    | set in | a 2:1     | ratio, | while  | all abnormal |      | traces were    |
| efficiency, | particularly | in  | large-scale | or  | real-time appli- |               |        |           |        |        |              |      |                |
|             |              |     |             |     |                  | included      | in the | test set. |        |        |              |      |                |
cations. This is quantified by the time required for the During experiments, we generally use default hyperparam-
| training | and testing | phases. |     |     |     |            |     |               |     |         |           |     |           |
| -------- | ----------- | ------- | --- | --- | --- | ---------- | --- | ------------- | --- | ------- | --------- | --- | --------- |
|          |             |         |     |     |     | eters from | the | corresponding |     | anomaly | detection |     | algorithm |
papers.Ifthetrainingordetectionperformanceonaparticular
|     |     |     |     |     |     | dataset is | suboptimal, |     | hyperparameters |     | are       | adjusted | to opti-    |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------------- | --- | --------- | -------- | ----------- |
|     |     |     |     |     |     | mize the   | results.    | All | experiments     | are | performed |          | on a server |
configuredwithtwoIntel(R)Xeon(R)Gold5416SCPUs,376
|     |     |     |     |     |     | GB of RAM,       |                | and seven    | NVIDIA    |              | RTX A6000   |              | GPUs, each |
| --- | --- | --- | --- | --- | --- | ---------------- | -------------- | ------------ | --------- | ------------ | ----------- | ------------ | ---------- |
|     |     |     |     |     |     | with 48          | GB of          | GPU memory.  |           |              |             |              |            |
|     |     |     |     |     |     | B. Overall       | Performance    |              | (RQ1)     |              |             |              |            |
|     |     |     |     |     |     | Table            | III summarizes |              | the       | overall      | performance |              | of various |
|     |     |     |     |     |     | algorithms       | across         | datasets,    |           | and Fig.     | 13          | presents     | a radar    |
|     |     |     |     |     |     | chart comparing  |                | the          | F1-scores | achieved     |             | by different | algo-      |
|     |     |     |     |     |     | rithms on        | various        | datasets.    |           | The findings |             | reveal       | that no    |
|     |     |     |     |     |     | single algorithm |                | consistently |           | outperforms  |             | others       | across all |
|     |     |     |     |     |     | datasets.        | Specifically,  |              | GTrace    | [12]         | achieves    | optimal      | perfor-    |
Fig. 12: Trace Anomaly Detection Algorithm Leaderboard mancewithF1-scoresof99.4%and71.8%ontheTrainTicket
|              |             |     |     |     |     | and AIOps2020   |      | datasets    | respectively. |        | TraceVAE    |     | [20] demon-   |
| ------------ | ----------- | --- | --- | --- | --- | --------------- | ---- | ----------- | ------------- | ------ | ----------- | --- | ------------- |
|              |             |     |     |     |     | strates leading |      | performance |               | on the | GAIA        | and | AIOps2022     |
|              |             |     |     |     |     | datasets        | with | F1-scores   | of            | 90.9%  | and 78.9%   |     | respectively, |
| E. Algorithm | Leaderboard |     |     |     |     |                 |      |             |               |        |             |     |               |
|              |             |     |     |     |     | while PUTraceAD |      | [25]        | achieves      |        | the highest |     | F1-score of   |
Toprovideaclearerandmorecomprehensivecomparisonof 74.7% on the AIOps2023 dataset. These results highlight that
trace anomaly detection algorithms, we design and implement the effectiveness of each algorithm is influenced by dataset
a dedicated leaderboard, as illustrated in Fig. 12. This leader- characteristics. GTrace’s innovative strategy of “predicting
board systematically displays the performance of different latency with structure” proves effective in part datasets, while
algorithmsondifferentdatasets.Specifically,itreportsasetof TraceVAE’s integration of GNNs and VAEs addresses com-
keyevaluationmetrics—includingprecision,recall,F1-score, plex data characteristics. PUTraceAD’s semi-supervised ar-
accuracy,andtimeconsumption—acrossthreerepresentative chitecture demonstrates unique advantages on the AIOps2023
anomaly types: total anomalies, structural anomalies, and dataset containing 53.6% anomalies.
latency anomalies. Moreover, the leaderboard supports inter- To evaluate the algorithms’ performance in detecting dif-
active functionality, allowing users to dynamically sort results ferent types of anomalies, we calculate the F1-scores for
based on any chosen metric. This design enables researchers both structural and latency anomalies. This analysis does
toexplorealgorithms’strengthsandweaknessesfrommultiple not take into account the dataset differences, as detailed in
dimensions. By offering a unified and visually accessible Table IV. TraceVAE achieves a structural anomaly detection
platform for comprehensive performance comparison, this F1-score of 96.8%, highlighting the exceptional performance
leaderboard not only facilitates the identification of state-of- of its Structure VAE module. The model’s GNN encoder
the-art methods but also encourages further improvement in explicitlycapturestopologicaldependencieswithintracedata,
trace anomaly detection research. significantly enhancing its structural modeling capabilities. In
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
9
|     |     |     | TABLE       |     | III: Overall | Performance | (F1: F1-score; | ACC: | Accuracy) |           |     |     |           |     |
| --- | --- | --- | ----------- | --- | ------------ | ----------- | -------------- | ---- | --------- | --------- | --- | --- | --------- | --- |
|     |     |     | TrainTicket |     |              | GAIA        | AIOps2020      |      |           | AIOps2022 |     |     | AIOps2023 |     |
F1 (%) ACC (%) F1 (%) ACC (%) F1 (%) ACC (%) F1 (%) ACC (%) F1 (%) ACC (%)
Multimodal LSTM 68.5 73.7 89.8 70.7 54.5 41.6 59.2 51.4 64.4 80.5
TraceAnomaly 62.6 82.1 46.3 65.3 56.8 77.9 58.5 78.7 55.4 82.9
| CRISP     |     | 62.5 |     | 82.0 | 44.5 | 64.1 | 57.0         | 78.0            | 58.1            |                 | 78.5         | 66.4          |                | 87.2        |
| --------- | --- | ---- | --- | ---- | ---- | ---- | ------------ | --------------- | --------------- | --------------- | ------------ | ------------- | -------------- | ----------- |
| PUTraceAD |     | 95.4 |     | 98.9 | 68.6 | 84.8 | 48.3         | 78.6            | 68.1            |                 | 88.1         | 74.7          |                | 95.5        |
| TraceCRL  |     | 55.6 |     | 50.9 | 75.0 | 73.9 | 53.0         | 40.8            | 53.2            |                 | 36.2         | 44.2          |                | 57.4        |
| TraceVAE  |     | 97.3 |     | 98.2 | 90.9 | 91.1 | 57.1         | 72.7            | 78.9            |                 | 86.7         | 74.0          |                | 90.0        |
| GTrace    |     | 99.4 |     | 80.3 | 70.9 | 64.5 | 71.8         | 81.9            | 76.5            |                 | 93.8         | 70.3          |                | 87.6        |
|           |     |      |     |      |      |      | performance, | we              | then reclassify |                 | the          | combined      | data           | based on    |
|           |     |      |     |      |      |      | specific     | feature         | values,         | thereby         | establishing |               | different      | subsets     |
|           |     |      |     |      |      |      | where data   | with            | similar         | characteristics |              | are           | clustered      | together.   |
|           |     |      |     |      |      |      | These newly  | constructed     |                 | datasets        | are          | subsequently  |                | applied to  |
|           |     |      |     |      |      |      | evaluate     | the performance |                 | of different    |              | algorithms.   |                | The results |
|           |     |      |     |      |      |      | indicate     | that these      | data            | characteristics |              | significantly |                | influence   |
|           |     |      |     |      |      |      | algorithm    | performance:    |                 |                 |              |               |                |             |
|           |     |      |     |      |      |      | Trace        | Depth.          | Fig. 14         | clearly         | illustrates  |               | that different | al-         |
|           |     |      |     |      |      |      | gorithms     | excel           | at different    | trace           | depths.      | Specifically, |                | when        |
|           |     |      |     |      |      |      | trace depth  | is ≤            | 3, TraceVAE     |                 | achieves     | the           | highest        | F1-score    |
|           |     |      |     |      |      |      | of 92.2%,    | slightly        | outperforming   |                 | PUTraceAD    |               | (91.6%)        | and         |
|           |     |      |     |      |      |      | GTrace       | (91.4%).        | Both GTrace     |                 | and TraceVAE |               | show           | distinct    |
|           |     |      |     |      |      |      | performance  | advantages      |                 | as trace        | depth        | increases.    |                | Notably,    |
|           |     |      |     |      |      |      | when the     | trace           | depth           | is more         | than         | 6, TraceVAE   |                | signif-     |
|           |     |      |     |      |      |      | icantly      | outperforms     | other           | algorithms,     |              |               | reaching       | an F1-      |
Fig. 13: F1-score Comparison Across Datasets score of 82.3%, while GTrace drops to 66.5%. This suggests
|     |     |     |     |     |     |     | that many | anomaly | detection |     | methods | are | capable | of effec- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | --- | ------- | --- | ------- | --------- |
tivelyhandlingrelativelysimpletraceswithshallowinvocation
contrast, GTrace achieves a latency anomaly detection F1- paths. However, when trace depth grows, the complexity of
scoreof78.2%,primarilyduetoitsfocusonmodelinglatency invocationlogicandmulti-layerserviceinteractionsincreases,
features at the span level, unlike other algorithms that operate resultinginwiderfaultpropagationandmorenoticeablevaria-
solely at the trace level. This span-level modeling allows tionsinalgorithmperformance.Insuchscenarios,TraceVAE’s
|     |     |     |     |     |     |     | dual-variable | graph | variational |     | autoencoder |     | [17]–[19] | appears |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ----------- | --- | ----------- | --- | --------- | ------- |
GTracetocapturefine-grainedlatencyvariationswithintraces,
leading to more precise anomaly detection that might be better equipped to capture long-range dependencies and con-
overlooked by trace-level approaches. Furthermore, this table textual information. Meanwhile, GTrace shows its strength in
indicatesthatcurrentlatencydetectionmethodsstillhaveroom moderate-depth situations, and PUTraceAD remains competi-
for improvement, making it a promising direction for future tive for traces with small depth.
research.
| TABLE | IV: Algorithm | Performance |     | under | Different | Anomaly |     |     |     |     |     |     |     |     |
| ----- | ------------- | ----------- | --- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Types
|                |                |             |         | Structure       | Latency |                   |     |     |     |     |     |     |     |     |
| -------------- | -------------- | ----------- | ------- | --------------- | ------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                | MultimodalLSTM |             |         | 76.5%           | 62.2%   |                   |     |     |     |     |     |     |     |     |
|                | TraceAnomaly   |             |         | 57.7%           | 56.0%   |                   |     |     |     |     |     |     |     |     |
|                | CRISP          |             |         | 55.8%           | 56.2%   |                   |     |     |     |     |     |     |     |     |
|                | PUTraceAD      |             |         | 89.1%           | 61.7%   |                   |     |     |     |     |     |     |     |     |
|                | TraceCRL       |             |         | 65.9%           | 53.7%   |                   |     |     |     |     |     |     |     |     |
|                | TraceVAE       |             |         | 96.8%           | 76.4%   |                   |     |     |     |     |     |     |     |     |
|                | GTrace         |             |         | 95.6%           | 78.2%   |                   |     |     |     |     |     |     |     |     |
| C. Performance | on             | Various     | Data    | Characteristics |         | (RQ2)             |     |     |     |     |     |     |     |     |
| In order       | to thoroughly  |             | analyze | the             | impact  | of data char-     |     |     |     |     |     |     |     |     |
| acteristics    | on the         | performance |         | of trace        | anomaly | detection         |     |     |     |     |     |     |     |     |
| algorithms,    | we first       | combine     |         | data            | from    | the five distinct |     |     |     |     |     |     |     |     |
datasets into a single, comprehensive dataset. This aggregated Fig.14:AlgorithmPerformanceunderDifferentTraceDepths
| dataset | serves as | a unified | foundation |     | for | further analysis. |     |     |     |     |     |     |     |     |
| ------- | --------- | --------- | ---------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
To better understand how different features affect algorithm Span Count. As shown in Fig. 15, GTrace achieves
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
10
| the highest    | F1-score     |            | for         | traces    | with       | 1-5 spans   | (99.7%),    |       |     |     |     |     |     |     |
| -------------- | ------------ | ---------- | ----------- | --------- | ---------- | ----------- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
| 11-30 spans    |              | (70.7%),   | and         | more      | than       | 30 spans    | (60.8%),    |       |     |     |     |     |     |     |
| demonstrating  |              | its robust | performance |           | across     | both        | simple      | and   |     |     |     |     |     |     |
| highly complex |              | traces.    | In          | contrast, | TraceVAE   |             | excels      | at 6- |     |     |     |     |     |     |
| 10 spans,      | attaining    |            | an F1-score |           | of 74.2%,  | which       | suggests    |       |     |     |     |     |     |     |
| that its       | architecture | is         | well-suited |           | to traces  | of moderate |             | com-  |     |     |     |     |     |     |
| plexity.       | Notably,     | both       | TraceVAE    |           | (99.4%)    | and         | PUTraceAD   |       |     |     |     |     |     |     |
| (99.1%)        | also         | approach   | 99%         | at        | 1-5 spans, | indicating  |             | that  |     |     |     |     |     |     |
| simple         | traces       | can be     | effectively |           | handled    | by          | a variety   | of    |     |     |     |     |     |     |
| methods.       | Moreover,    |            | CRISP       | exhibits  | a          | unique      | performance |       |     |     |     |     |     |     |
trend:itimprovessteadilywithincreasingspancount,starting
| from 24.3%   | for           | traces      | with         | 1–5     | spans        | and reaching  |           | 59.3%              |             |     |       |           |      |        |
| ------------ | ------------- | ----------- | ------------ | ------- | ------------ | ------------- | --------- | ------------------ | ----------- | --- | ----- | --------- | ---- | ------ |
| when the     | span          | count       | exceeds      | 30.     | Meanwhile,   | other         | methods,  |                    |             |     |       |           |      |        |
| such as      | Multimodal    |             | LSTM         | [34]    | and TraceCRL |               | [30],     | exhibit            |             |     |       |           |      |        |
| moderate     | performance   |             | but          | do not  | outperform   |               | the       | optimal            |             |     |       |           |      |        |
| algorithm    | in any        | particular  |              | range.  | The          | span count    | of        | a trace            |             |     |       |           |      |        |
| reflects     | both          | the breadth | and          | depth   | of           | its execution |           | logic,             |             |     |       |           |      |        |
|              |               |             |              |         |              |               |           | Fig. 15: Algorithm | Performance |     | under | Different | Span | Counts |
| encompassing |               | horizontal  | service      |         | calls at     | the same      | level     | and                |             |     |       |           |      |        |
| vertical,    | multi-layered |             | interactions |         | across       | different     | services. |                    |             |     |       |           |      |        |
| Traces with  | more          | spans       | often        | involve | more         | frequent      |           | service            |             |     |       |           |      |        |
otheranomalydetectionmethodssuchasPUTraceAD,CRISP,
| calls, denser      | data         | interactions, |          | and         | greater  | opportunities      |              | for           |                    |              |            |               |                |           |
| ------------------ | ------------ | ------------- | -------- | ----------- | -------- | ------------------ | ------------ | ------------- | ------------------ | ------------ | ---------- | ------------- | -------------- | --------- |
|                    |              |               |          |             |          |                    |              | and TraceCRL  | show               | relatively   | limited    | adaptability, |                | and their |
| fault propagation. |              | GTrace’s      |          | Tree-LSTM   |          | [22], specifically |              | de-           |                    |              |            |               |                |           |
|                    |              |               |          |             |          |                    |              | inability to  | consistently       | model        | detailed   | inter-service |                | interac-  |
| signed for         | tree         | structures,   |          | effectively | captures |                    | dependencies |               |                    |              |            |               |                |           |
|                    |              |               |          |             |          |                    |              | tions hinders | their              | performance, | especially |               | as system      | scale     |
| between            | parent-child |               | nodes,   | aligning    | well     | with               | typical      | trace         |                    |              |            |               |                |           |
|                    |              |               |          |             |          |                    |              | increases.    | These observations |              | underscore |               | the importance | of        |
| structures.        | However,     |               | although | TraceVAE    |          | achieves           | outstanding  |               |                    |              |            |               |                |           |
capturingnuancedinteractionsacrossmultipleservices,which
| results for   | traces     | with | a medium |            | or small | number    | of   | spans,      |              |         |           |     |                |       |
| ------------- | ---------- | ---- | -------- | ---------- | -------- | --------- | ---- | ----------- | ------------ | ------- | --------- | --- | -------------- | ----- |
|               |            |      |          |            |          |           |      | is critical | for accurate | anomaly | detection |     | in large-scale | trace |
| its detection | capability |      | may      | be limited | by       | its fixed | span | count       |              |         |           |     |                |       |
data.
| requirement, | determined |       | by         | a predefined |             | max node | count. | A       |     |     |     |     |     |     |
| ------------ | ---------- | ----- | ---------- | ------------ | ----------- | -------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
| small max    | node       | count | constrains |              | the model’s | ability  |        | to deal |     |     |     |     |     |     |
withhighlycomplextracesinvolvingalargenumberofspans.
| Meanwhile,   | CRISP      | [16] | becomes |     | more  | competitive   | at  | higher   |     |     |     |     |     |     |
| ------------ | ---------- | ---- | ------- | --- | ----- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| span counts, | suggesting |      | that    | its | focus | on extracting |     | critical |     |     |     |     |     |     |
pathsiswell-suitedforscenariosrequiringalotofinvocation.
| In contrast,  | methods     |          | like PUTraceAD |             | and        | Multimodal |               | LSTM    |     |     |     |     |     |     |
| ------------- | ----------- | -------- | -------------- | ----------- | ---------- | ---------- | ------------- | ------- | --- | --- | --- | --- | --- | --- |
| maintain      | high        | accuracy | for            | relatively  | simple     | traces     | but           | show    |     |     |     |     |     |     |
| diminished    | performance |          | as             | trace       | complexity | grows,     |               | due to  |     |     |     |     |     |     |
| their limited | capacity    |          | for modeling   |             | long-range |            | dependencies. |         |     |     |     |     |     |     |
| For traces    | with        | high     | span           | counts,     | approaches |            | capable       | of      |     |     |     |     |     |     |
| capturing     | extensive   |          | dependencies,  |             | like       | GTrace,    | are expected  |         |     |     |     |     |     |     |
| to yield      | better      | anomaly  | detection      |             | results.   |            |               |         |     |     |     |     |     |     |
| Service       | Count.      | Fig.     | 16             | illustrates | that       | for traces |               | with 1- |     |     |     |     |     |     |
| 4 services,   | TraceVAE    |          | achieves       | the         | highest    | F1-score   | (89.7%),      |         |     |     |     |     |     |     |
| followed      | by GTrace   |          | (83.5%)        | and         | Multimodal | LSTM       | (78.3%).      |         |     |     |     |     |     |     |
| Similarly,    | TraceVAE    |          | maintains      | its         | dominance  | at         | 5-8 services  |         |     |     |     |     |     |     |
| with an       | F1-score    | of       | 67.9%,         | while       | GTrace     | and        | Multimodal    |         |     |     |     |     |     |     |
LSTM are still competitive at 57.7% and 57.0%, respec- Fig. 16: Algorithm Performance under Different Service
| tively. However, |             | when | the       | number | of       | services | exceeds | 8, Counts |     |     |     |     |     |     |
| ---------------- | ----------- | ---- | --------- | ------ | -------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
| GTrace           | outperforms |      | the other |        | methods, | reaching |         | 68.1%,    |     |     |     |     |     |     |
whereasTraceAnomalytrailsbehindat59.6%.Asthenumber Anomaly Ratio. According to Fig. 17, GTrace achieves
of services in a trace increases, fault diagnosis becomes the highest F1-score (68.7%) when the anomaly ratio is
more challenging. These results suggest that TraceVAE is 0%, whereas TraceVAE leads at 0.5% (69.1%). For 1%,
particularly effective in relatively simple service topologies, GTrace again outperforms other methods at 61.8%, but when
wheremodelingkeyservice-to-serviceinteractionscancapture the anomaly ratio reaches 3%, TraceVAE stands out
most of the anomaly-relevant information. However, GTrace with 56.6%. Other algorithms, including Multimodal LSTM,
demonstrates better performance for traces with more ser- TraceAnomaly, and CRISP, exhibit moderate performance
vices.ThisisprimarilyattributedtoGTrace’sNode-wiseVAE acrossallanomalylevels.Notably,PUTraceADlosesdetection
encoder, which leverages the service name field to capture capability for 0% or 0.5% but achieves 41.9% at 1% and
each service’s impact on overall trace latency. In contrast, 55.0% at 3%. This is consistent with its positive-unlabeled
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
11
learningparadigm,whichreliesonthepresenceofasufficient The results reveal notable differences in time efficiency
number of positive (abnormal) samples to perform effective among the algorithms. Multimodal LSTM demonstrates the
training. PUTraceAD’s detection performance deteriorates in lowest training overhead, owing to its approach of indepen-
the absence of sufficient anomalies to direct the optimization dentlymodelingtemporalandstructuralfeatureswithLSTMs.
process. Additionally, Since abnormal traces account for ap- This architecture simplifies the learning process and leads to
proximately 1% of total traces [40] in real-world production superior training efficiency compared to other models with
environments, GTrace’s robustness at this ratio is particularly more complex graph-based encoders or latent variable mech-
noteworthy. However, as the anomaly ratio further increases, anisms. Conversely, TraceVAE requires a significant amount
unlikemethodssuchasGTracethatusenegativelog-likelihood of training time, which reflects the computational complexity
(NLL) directly as anomaly scores, TraceVAE’s techniques, ofitsdual-variablegraphvariationalautoencoderarchitecture,
including Bernoulli & Categorical Scaling, Node Count Nor- evenifithasdemonstratedoutstandingdetectionperformance
malization, and Gaussian Std-Limit [20], reduce entropy gaps inpriorexperiments.Themodel’strainingcostmayhinderits
effectively , mitigate the negative impact of noise, and enable real-time adaptability or deployment in resource-constrained
more accurate differentiation between normal and anomalous environments.Similarly,TraceCRLexhibitsconsiderabletime
traces. This findings underscore the importance of designing consumptionduringtracerepresentationgeneration,evenwith
models that can handle increased noise effectively, ensuring GPU acceleration. The model’s reliance on contrastive learn-
reliable anomaly identification even in highly contaminated ing frameworks, involving large numbers of positive and neg-
datasets. ative sample pairs, results in high computational complexity.
Notably,GTraceachievesremarkabledetectionspeed,primar-
|     |     |     |     |     |     |     |     | ily attributed |       | to its       | caching | techniques      |     | and trace         | grouping |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ------------ | ------- | --------------- | --- | ----------------- | -------- |
|     |     |     |     |     |     |     |     | strategies,    | which | allow        | shared  | representations |     | and               | precom-  |
|     |     |     |     |     |     |     |     | puted features |       | to be reused |         | across similar  |     | trace structures. | By       |
avoidingredundantcomputation,GTraceeffectivelyminimizes
|     |     |     |     |     |     |     |     | time consumption |     | during | detection |     | phases, | making | it suitable |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | --------- | --- | ------- | ------ | ----------- |
forreal-timeanomalydetectionscenarioswhereresponsetime
is critical.
|      |               |     |             |     |       |           |         | E. Recommended |             | Algorithms    |              | (RQ3)            |               |                |             |
| ---- | ------------- | --- | ----------- | --- | ----- | --------- | ------- | -------------- | ----------- | ------------- | ------------ | ---------------- | ------------- | -------------- | ----------- |
|      |               |     |             |     |       |           |         | In previous    |             | experiments,  |              | we evaluated     |               | the            | performance |
|      |               |     |             |     |       |           |         | of various     | algorithms  |               | on datasets  |                  | characterized |                | by distinct |
|      |               |     |             |     |       |           |         | individual     | features,   | primarily     |              | focusing         | on            | the impact     | of sin-     |
|      |               |     |             |     |       |           |         | gle features   | on          | detection     | performance. |                  | However,      |                | real-world  |
|      |               |     |             |     |       |           |         | datasets       | typically   | exhibit       | multiple     |                  | coexisting    | features,      | ne-         |
|      |               |     |             |     |       |           |         | cessitating    | a more      | comprehensive |              |                  | evaluation.   | To             | bridge this |
|      |               |     |             |     |       |           |         | gap and        | approximate |               | more         | realistic        | application   | scenarios,     | we          |
|      |               |     |             |     |       |           |         | extend our     | analysis    | by            | employing    |                  | a decision    | tree           | model [41]  |
| Fig. | 17: Algorithm |     | Performance |     | under | Different | Anomaly |                |             |               |              |                  |               |                |             |
|      |               |     |             |     |       |           |         | to integrate   | multiple    |               | dataset      | characteristics, |               | as illustrated | in          |
Ratios
|     |     |     |     |     |     |     |     | Fig. 18.    | The | results | demonstrate |     | that when | the  | proportion |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ----------- | --- | --------- | ---- | ---------- |
|     |     |     |     |     |     |     |     | of abnormal |     | data in | the dataset |     | exceeds   | 10%, | the semi-  |
supervisedanomalydetectionmethodPUTraceADispreferred
D. Efficiency analysis of different algorithms due to its ability to effectively utilize anomaly information.
|           |          |     |           |             |          |               |              | For datasets  | with | lower    | anomaly |            | proportions, | the | choice of  |
| --------- | -------- | --- | --------- | ----------- | -------- | ------------- | ------------ | ------------- | ---- | -------- | ------- | ---------- | ------------ | --- | ---------- |
| To        | evaluate | the | detection | efficiency  |          | of various    | algorithms,  |               |      |          |         |            |              |     |            |
|           |          |     |           |             |          |               |              | the algorithm |      | depends  | on      | additional | factors.     | If  | the number |
| we        | measure  | the | time      | consumption | during   | the           | training and |               |      |          |         |            |              |     |            |
|           |          |     |           |             |          |               |              | of spans      | in a | trace is | ≤ 5 or  | > 30,      | we recommend |     | GTrace,    |
| detection | phases   |     | using     | the same    | dataset. | Specifically, | 51,386       |               |      |          |         |            |              |     |            |
traces are randomly sampled from the TrainTicket dataset as benefiting from its Tree-LSTM architecture that handles both
|         |          |           |           |          |               |          |             | shallow         | and complex |          | hierarchical |           | structures | efficiently. | For          |
| ------- | -------- | --------- | --------- | -------- | ------------- | -------- | ----------- | --------------- | ----------- | -------- | ------------ | --------- | ---------- | ------------ | ------------ |
| the     | training | set,      | while     | the test | set comprises | 51,309   | normal      |                 |             |          |              |           |            |              |              |
|         |          |           |           |          |               |          |             | traces with     | 6–10        | spans,   | the          | selection | depends    |              | on the trace |
| traces  | and      | 25,197    | anomalous |          | traces.       | The time | consumption |                 |             |          |              |           |            |              |              |
|         |          |           |           |          |               |          |             | depth: TraceVAE |             | performs | better       | for       | traces     | with         | a depth of 3 |
| details | are      | presented | in        | Table V. |               |          |             |                 |             |          |              |           |            |              |              |
orless,whereasGTraceismoreeffectivefordeepertracesdue
TABLEV:TrainingTimeandDetectingSpeedingofDifferent to its ability to capture long-range dependencies. For traces
Algorithms with spans ranging from 11 to 30, TraceVAE is preferable
|     |                |     |     |              |      |                |     | when the | anomaly | proportion  |     | is ≤    | 1% or | > 3%; | otherwise, |
| --- | -------------- | --- | --- | ------------ | ---- | -------------- | --- | -------- | ------- | ----------- | --- | ------- | ----- | ----- | ---------- |
|     | Algorithm      |     |     | TrainingTime |      | DetectingSpeed |     |          |         |             |     |         |       |       |            |
|     |                |     |     |              |      |                |     | GTrace   | remains | the optimal |     | choice. |       |       |            |
|     | MultimodalLSTM |     |     |              | 419s | 4500traces/s   |     |          |         |             |     |         |       |       |            |
TraceAnomaly 3422s 107traces/s This hierarchical decision-making framework provides a
CRISP 3827s 107traces/s systematicandpracticalstrategyforselectingthemostsuitable
|     | TraceCRL  |     |     |     | 13176s | 700traces/s |     |         |           |           |     |        |         |            |         |
| --- | --------- | --- | --- | --- | ------ | ----------- | --- | ------- | --------- | --------- | --- | ------ | ------- | ---------- | ------- |
|     |           |     |     |     |        |             |     | anomaly | detection | algorithm |     | across | diverse | real-world | scenar- |
|     | PUTraceAD |     |     |     | 1715s  | 548traces/s |     |         |           |           |     |        |         |            |         |
ios,effectivelyaccountingfortheinterplayofmultipledataset
|     | TraceVAE |     |     |     | 23497s | 257traces/s   |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | GTrace   |     |     |     | 1641s  | 10211traces/s |     |     |     |     |     |     |     |     |     |
characteristics.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
12
|     |     |     |     |     |     | when higher | detection |         | efficiency  | is        | the primary | goal,               | GTrace      |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ------- | ----------- | --------- | ----------- | ------------------- | ----------- |
|     |     |     |     |     |     | is the most | suitable  | option. |             |           |             |                     |             |
|     |     |     |     |     |     | Future      | Research  |         | Directions. | Despite   |             | the progress        | made        |
|     |     |     |     |     |     | by existing | trace     | anomaly |             | detection | algorithms, |                     | our empiri- |
|     |     |     |     |     |     | cal results | reveal    | current | limitations |           | and         | future optimization |             |
directions.
|     |     |     |     |     |     | Towards |     | fine-grained |     | span-level | anomaly |     | detection. |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | --- | ---------- | ------- | --- | ---------- |
•
Manyanomalydetectionalgorithms[14],[16],[20],[25],
|     |     |     |     |     |     | [34] | operate | primarily |     | at the | trace | level, | labeling an |
| --- | --- | --- | --- | --- | --- | ---- | ------- | --------- | --- | ------ | ----- | ------ | ----------- |
Fig.18:Adecisiontreebasedonmultipledatasets’character-
|     |     |     |     |     |     | entire | trace | as  | normal | or abnormal. |     | This trace-centric |     |
| --- | --- | --- | --- | --- | --- | ------ | ----- | --- | ------ | ------------ | --- | ------------------ | --- |
istics
|     |     |     |     |     |     | approach |        | is insufficient |               | for | detailed | diagnosis. | Future    |
| --- | --- | --- | --- | --- | --- | -------- | ------ | --------------- | ------------- | --- | -------- | ---------- | --------- |
|     |     |     |     |     |     | work     | should | focus           | on optimizing |     | the      | capability | for span- |
leveldetection,whichisessentialforrootcauseanalysis.
V. THREATSTOVALIDITY
|     |     |     |     |     |     | • Building |     | upon | the strengths |     | of prior | methods. | Re- |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ------------- | --- | -------- | -------- | --- |
Algorithms.Theprimarythreattovalidityinthisempirical searchers should aim to adopt effective design elements
study lies in the models’ configuration. By default, we utilize from existing work while minimizing architectural con-
the hyperparameter settings given in the original publications straints that may negatively impact model performance.
for the corresponding algorithm and conduct each experiment For example, TraceVAE’s use of a fixed span count per
at least three times. However, when suboptimal results are trace leads to performance degradation on traces with
observedoncertaindatasets,adjustmentsaremadetoimprove high span counts, which should be avoided in future
detectionperformance.Whileusingdefaulthyperparametersis
|     |     |     |     |     |     | designs. | Building |     | upon | established | methodologies |     | while |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ---- | ----------- | ------------- | --- | ----- |
apracticalapproach,fine-tuningthemtoalignwiththeunique addressing their limitations, future anomaly detection
characteristics of each dataset may result in better detection methodscanintegratetheentropygapreductionstrategies
outcomes. pioneeredinTraceVAE.Specifically,thisinvolvesimple-
Datasets. The external threat to validity stems from the menting Bernoulli & Categorical Scaling for structural
| datasets used | in the evaluation. |     | Although | five distinct | datasets |         |     |                 |     |      |       |               |     |
| ------------- | ------------------ | --- | -------- | ------------- | -------- | ------- | --- | --------------- | --- | ---- | ----- | ------------- | --- |
|               |                    |     |          |               |          | anomaly |     | identification, |     | Node | Count | Normalization | for |
were employed to assess algorithm performance, their data dimensional consistency, and Gaussian Std-Limit thresh-
features may not comprehensively reflect the wide range of olding for latency anomalies. These techniques are to
real-world scenarios. Each dataset has unique characteristics be synergistically combined with the hierarchical graph
and inherent limitations, potentially failing to capture the encoding architecture of GTrace, which separates global
| full diversity | and complexity | of  | data encountered |     | in practical |           |     |          |      |            |     |         |            |
| -------------- | -------------- | --- | ---------------- | --- | ------------ | --------- | --- | -------- | ---- | ---------- | --- | ------- | ---------- |
|                |                |     |                  |     |              | structure |     | modeling | from | node-level |     | feature | processing |
applications. To overcome this restriction, we will focus on throughitsinnovativedispatchinglayer.Furthermore,the
collecting more datasets from a broader range of scenarios entire system can leverage GTrace’s optimized caching
and domains in the future. strategy that utilizes dynamic programming and LRU-
|     |     |     |     |     |     | cached | trees | to  | enable | batched | processing |     | of merged |
| --- | --- | --- | --- | --- | --- | ------ | ----- | --- | ------ | ------- | ---------- | --- | --------- |
VI. DISCUSSIONANDFUTUREDIRECTIONS subgraphs,therebyenhancingoverallefficiencyandscal-
ability.
Thissectionbuildsupontheempiricalfindingsandprovides
adeeperexplorationoftheinsightsgainedfrombenchmarking
|               |                       |     |          |         |           |     |     |     | VII. CONCLUSION |     |     |     |     |
| ------------- | --------------------- | --- | -------- | ------- | --------- | --- | --- | --- | --------------- | --- | --- | --- | --- |
| trace anomaly | detection algorithms. |     | We first | discuss | the data- |     |     |     |                 |     |     |     |     |
driven strategy required for selecting an optimal existing This paper presents a comprehensive empirical study on
algorithm. Following this, we address the current limitations anomaly detection algorithms used in distributed tracing sys-
observed in anomaly detection methodologies and outline tems, addressing critical challenges in selecting and applying
promising research directions. suitable models for real-world scenarios. By systematically
Insights for Existing Algorithm Selection. Our extensive evaluating multiple state-of-the-art algorithms across diverse
evaluation demonstrates that the most architecturally complex datasets, we provide an in-depth analysis of their respective
or recently published method is not necessarily the most strengths and limitations under varying data characteristics,
effectiveacrossallscenarios.Theeffectivenessofanalgorithm including trace depth, span count, service count, and anomaly
is deeply intertwined with the characteristics of trace data. ratio.Thelabeleddatasetsandalgorithmimplementationhave
Therefore,toselectthemostappropriatemethodforaspecific been made publicly available. Future studies can seamlessly
scenario,practitionersfirstneedtoconductathoroughanalysis apply these models to new datasets by simply converting the
of their production trace data, considering factors like span data into our standardized format, eliminating the need for
count, service count, trace depth, and anomaly ratio, and additional format-specific preprocessing for each model. This
then follow our recommended strategy. For example, we not only supports experiment reproducibility but also signif-
recommend PUTraceAD for data with high anomaly ratios. icantly facilitates future research in trace anomaly detection.
For traces with a large number of spans or a large number of Furthermore,weofferpracticalguidanceforselectingsuitable
services, GTrace is the preferred choice. Conversely, for trace algorithmsbasedondifferentdatacharacteristics,bridgingthe
data with shallow depth, we suggest TraceVAE. Additionally, gap between academic research and industrial applications.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
13
| To the best | of our knowledge, |     | this is | the first | comprehensive |     |          |            |       |               |                |            |         |            |        |
| ----------- | ----------------- | --- | ------- | --------- | ------------- | --- | -------- | ---------- | ----- | ------------- | -------------- | ---------- | ------- | ---------- | ------ |
|             |                   |     |         |           |               |     | [19] M.  | Simonovsky | and   | N. Komodakis, |                | “Graphvae: | Towards | generation |        |
|             |                   |     |         |           |               |     | of small | graphs     | using | variational   | autoencoders,” |            | in      | Artificial | Neural |
empiricalstudyontraceanomalydetection,providingvaluable
NetworksandMachineLearning–ICANN2018:27thInternationalCon-
| insights to | guide both | research | and practical |     | deployment. |     |                           |         |            |        |                           |         |           |         |       |
| ----------- | ---------- | -------- | ------------- | --- | ----------- | --- | ------------------------- | ------- | ---------- | ------ | ------------------------- | ------- | --------- | ------- | ----- |
|             |            |          |               |     |             |     | ference                   | on      | Artificial | Neural | Networks,                 | Rhodes, | Greece,   | October | 4-7,  |
|             |            |          |               |     |             |     | 2018,Proceedings,PartI27. |         |            |        | Springer,2018,pp.412–422. |         |           |         |       |
|             |            |          |               |     |             |     | [20] Z.                   | Xie, H. | Xu, W.     | Chen,  | W. Li,                    | H.      | Jiang, L. | Su, H.  | Wang, |
REFERENCES and D. Pei, “Unsupervised anomaly detection on microservice traces
|     |     |     |     |     |     |     | through | graph | vae,” | in Proceedings |     | of the | ACM | Web Conference |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----- | -------------- | --- | ------ | --- | -------------- | --- |
[1] M.Villamizar,O.Garce´s,H.Castro,M.Verano,L.Salamanca,R.Casal-
|     |     |     |     |     |     |     | 2023, | ser. | WWW | ’23. | New York, | NY, | USA: | Association | for |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | ---- | --------- | --- | ---- | ----------- | --- |
las,andS.Gil,“Evaluatingthemonolithicandthemicroservicearchi-
|         |                   |     |              |        |         |              | Computing |     | Machinery, | 2023, | p.  | 2874–2884. | [Online]. | Available: |     |
| ------- | ----------------- | --- | ------------ | ------ | ------- | ------------ | --------- | --- | ---------- | ----- | --- | ---------- | --------- | ---------- | --- |
| tecture | pattern to deploy | web | applications | in the | cloud,” | in 2015 10th |           |     |            |       |     |            |           |            |     |
https://doi.org/10.1145/3543507.3583215
ComputingColombianConference(10CCC),2015,pp.583–590. [21] P. Velicˇkovic´, G. Cucurull, A. Casanova, A. Romero, P. Lio`, and
[2] N. Dragoni, S. Giallorenzo, A. L. Lafuente, M. Mazzara, F. Montesi, Y. Bengio, “Graph attention networks,” in International Conference
| R. Mustafin,   | and | L. Safina, | “Microservices: |          | Yesterday, | today,       |     |          |                  |     |       |           |     |            |        |
| -------------- | --- | ---------- | --------------- | -------- | ---------- | ------------ | --- | -------- | ---------------- | --- | ----- | --------- | --- | ---------- | ------ |
|                |     |            |                 |          |            |              | on  | Learning | Representations, |     | 2018. | [Online]. |     | Available: | https: |
| and tomorrow,” | in  | Present    | and Ulterior    | Software |            | Engineering, |     |          |                  |     |       |           |     |            |        |
//openreview.net/forum?id=rJXMpikCZ
| M. Mazzara | and B. | Meyer, | Eds. | Cham, | Switzerland: | Springer |                                                              |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | ---- | ----- | ------------ | -------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|            |        |        |      |       |              |          | [22] M.Ahmed,M.R.Samee,andR.E.Mercer,“Improvingtree-lstmwith |     |     |     |     |     |     |     |     |
International Publishing, 2017, pp. 195–216. [Online]. Available: treeattention,”in2019IEEE13thInternationalConferenceonSemantic
https://doi.org/10.48550/arXiv.1606.04036 Computing(ICSC),2019,pp.247–254.
| [3] P. Jamshidi, | C. Pahl, | N. C. Mendonc¸a, |     | J. Lewis, | and S. | Tilkov, “Mi- |         |              |     |       |                  |     |            |                |     |
| ---------------- | -------- | ---------------- | --- | --------- | ------ | ------------ | ------- | ------------ | --- | ----- | ---------------- | --- | ---------- | -------------- | --- |
|                  |          |                  |     |           |        |              | [23] W. | L. Hamilton, | R.  | Ying, | and J. Leskovec, |     | “Inductive | representation |     |
croservices:Thejourneysofarandchallengesahead,”IEEESoftware,
|     |     |     |     |     |     |     | learning | on  | large graphs,” |     | in Proceedings |     | of the | 31st International |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | -------------- | --- | ------ | ------------------ | --- |
vol.35,no.3,pp.24–35,2018. Conference on Neural Information Processing Systems,
ser. NIPS’17.
[4] P.Liu,H.Xu,Q.Ouyang,R.Jiao,Z.Chen,S.Zhang,J.Yang,L.Mo, RedHook,NY,USA:CurranAssociatesInc.,2017,p.1025–1035.
J.Zeng,W.Xue,andD.Pei,“Unsuperviseddetectionofmicroservice [24] M. Zhang, Z. Cui, M. Neumann, and Y. Chen, “An end-to-end deep
traceanomaliesthroughservice-leveldeepbayesiannetworks,”in2020
|     |     |     |     |     |     |     | learning | architecture |     | for graph | classification,” |     | in Proceedings |     | of the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --------- | ---------------- | --- | -------------- | --- | ------ |
IEEE31stInternationalSymposiumonSoftwareReliabilityEngineering
AAAIconferenceonartificialintelligence,vol.32,no.1,2018.
(ISSRE),Oct2020,pp.48–58. [25] K.Zhang,C.Zhang,X.Peng,andC.Sha,“Putracead:Traceanomaly
[5] J. Kaldor et al., “Canopy: An end-to-end performance tracing and detection with partial labels based on gnn and pu learning,” in 2022
analysis system,” in Proceedings of the 26th Symposium on Operating IEEE33rdInternationalSymposiumonSoftwareReliabilityEngineering
SystemsPrinciples,2017.
(ISSRE),2022,pp.239–250.
[6] X.Guo,X.Peng,H.Wang,W.Li,H.Jiang,D.Ding,T.Xie,andL.Su,
|     |     |     |     |     |     |     | [26] R. Kiryo, | G.  | Niu, | M. C. | du Plessis, | and | M. Sugiyama, | “Positive- |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ----- | ----------- | --- | ------------ | ---------- | --- |
“Graph-basedtraceanalysisformicroservicearchitectureunderstanding unlabeled learning with non-negative risk estimator,” in Proceedings
andproblemdiagnosis,”inProceedingsofthe28thACMJointMeeting ofthe31stInternationalConferenceonNeuralInformationProcessing
onEuropeanSoftwareEngineeringConferenceandSymposiumonthe Systems,ser.NIPS’17. RedHook,NY,USA:CurranAssociatesInc.,
| FoundationsofSoftwareEngineering,ser.ESEC/FSE2020. |     |     |     |     |     | NewYork, |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2017,p.1674–1684.
NY,USA:AssociationforComputingMachinery,2020,p.1387–1397.
|     |     |     |     |     |     |     | [27] M. | Schuster | and K. | Nakajima, | “Japanese | and | korean | voice search,” | in  |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --------- | --------- | --- | ------ | -------------- | --- |
[Online].Available:https://doi.org/10.1145/3368089.3417066 2012 IEEE International Conference on Acoustics, Speech and Signal
[7] C. Zhang, X. Peng, C. Sha, K. Zhang, Z. Fu, X. Wu, Q. Lin, and Processing(ICASSP),2012,pp.5149–5152.
D.Zhang,“Deeptralog:Trace-logcombinedmicroserviceanomalyde- [28] T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi,
| tection       | through graph-based |     | deep learning,”      | in  | 2022 IEEE/ACM | 44th      |            |         |        |          |               |         |             |           |           |
| ------------- | ------------------- | --- | -------------------- | --- | ------------- | --------- | ---------- | ------- | ------ | -------- | ------------- | ------- | ----------- | --------- | --------- |
|               |                     |     |                      |     |               |           | P. Cistac, | T.      | Rault, | R. Louf, | M. Funtowicz, |         | J. Davison, | S.        | Shleifer, |
| International | Conference          | on  | Software Engineering |     | (ICSE),       | 2022, pp. |            |         |        |          |               |         |             |           |           |
|               |                     |     |                      |     |               |           | P. von     | Platen, | C.     | Ma, Y.   | Jernite,      | J. Plu, | C.          | Xu, T. Le | Scao,     |
623–634. S. Gugger, M. Drame, Q. Lhoest, and A. Rush, “Transformers: State-
[8] Jaegertracing.io, “Jaeger,” [Online]. Available: https://www. of-the-art natural language processing,” in Proceedings of the 2020
jaegertracing.io/. Conference on Empirical Methods in Natural Language Processing:
[9] Twitter,“Zipkin,”[Online].Available:https://zipkin.io/.
|     |     |     |     |     |     |     | System | Demonstrations, |     | Q.  | Liu and | D. Schlangen, |     | Eds. | Online: |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | --- | ------- | ------------- | --- | ---- | ------- |
[10] Skywalking.apache.org,“Apacheskywalking,”[Online].Available:http:
|     |     |     |     |     |     |     | Association |     | for Computational |     | Linguistics, |     | Oct. | 2020, pp. | 38–45. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------------- | --- | ------------ | --- | ---- | --------- | ------ |
//skywalking.apache.org/. [Online].Available:https://aclanthology.org/2020.emnlp-demos.6
[11] Opentracing.io, “Opentracing,” [Online]. Available: http://opentracing. [29] Y.You,T.Chen,Y.Sui,T.Chen,Z.Wang,andY.Shen,“Graphcon-
io/. trastive learning with augmentations,” Advances in neural information
[12] Z. Xie, C. Pei, W. Li, H. Jiang, L. Su, J. Li, G. Xie, and D. Pei, processingsystems,vol.33,pp.5812–5823,2020.
“Frompoint-wisetogroup-wise:Afastandaccuratemicroservicetrace
|     |     |     |     |     |     |     | [30] C. Zhang, | X.  | Peng, | T. Zhou, | C. Sha, | Z. Yan, | Y. Chen, | and H. | Yang, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | -------- | ------- | ------- | -------- | ------ | ----- |
anomaly detection approach,” in Proceedings of the 31st ACM Joint “Tracecrl: contrastive representation learning for microservice trace
European Software Engineering Conference and Symposium on the analysis,” in Proceedings of the 30th ACM Joint European Software
FoundationsofSoftwareEngineering,ser.ESEC/FSE2023. NewYork, EngineeringConferenceandSymposiumontheFoundationsofSoftware
NY,USA:AssociationforComputingMachinery,2023,p.1739–1749.
|     |     |     |     |     |     |     | Engineering,ser.ESEC/FSE2022. |     |     |     |     | NewYork,NY,USA:Association |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
[Online].Available:https://doi.org/10.1145/3611643.3613861 for Computing Machinery, 2022, p. 1221–1232. [Online]. Available:
[13] D. P. Kingma, “Auto-encoding variational bayes,” arXiv preprint https://doi.org/10.1145/3540250.3549146
arXiv:1312.6114,2013. [31] B. Perozzi, R. Al-Rfou, and S. Skiena, “Deepwalk: online learning
[14] P.Liu,H.Xu,Q.Ouyang,R.Jiao,Z.Chen,S.Zhang,J.Yang,L.Mo, of social representations,” in Proceedings of the 20th ACM SIGKDD
J.Zeng,W.Xue,andD.Pei,“Unsuperviseddetectionofmicroservice International Conference on Knowledge Discovery and Data Mining,
traceanomaliesthroughservice-leveldeepbayesiannetworks,”in2020 ser. KDD ’14. New York, NY, USA: Association for Computing
IEEE31stInternationalSymposiumonSoftwareReliabilityEngineering Machinery, 2014, p. 701–710. [Online]. Available: https://doi.org/10.
| (ISSRE),2020,pp.48–58. |     |     |     |     |     |     | 1145/2623330.2623732 |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[15] D. Rezende and S. Mohamed, “Variational inference with normalizing [32] B. Scho¨lkopf, R. C. Williamson, A. Smola, J. Shawe-Taylor,
flows,”inInternationalconferenceonmachinelearning.
|     |     |     |     |     |     | PMLR,2015, | and | J. Platt, | “Support | vector | method | for | novelty | detection,” | in  |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | -------- | ------ | ------ | --- | ------- | ----------- | --- |
pp.1530–1538. Advances in Neural Information Processing Systems, S. Solla,
[16] Z. Zhang, M. K. Ramanathan, P. Raj, A. Parwal, T. Sherwood, and T. Leen, and K. Mu¨ller, Eds., vol. 12. MIT Press, 1999.
M.Chabbi,“CRISP:CriticalpathanalysisofLarge-Scalemicroservice [Online]. Available: https://proceedings.neurips.cc/paper files/paper/
architectures,”in2022USENIXAnnualTechnicalConference(USENIX 1999/file/8725fb777f25776ffa9076e44fcfd776-Paper.pdf
ATC22).
Carlsbad,CA:USENIXAssociation,Jul.2022,pp.655–672. [33] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
[17] Y. Kwon, J. Yoo, Y.-S. Choi, W.-J. Son, D. Lee, and S. Kang, Computation, vol. 9, no. 8, pp. 1735–1780, 11 1997. [Online].
“Efficientlearningofnon-autoregressivegraphvariationalautoencoders Available:https://doi.org/10.1162/neco.1997.9.8.1735
for molecular graph generation,” Journal of Cheminformatics, vol. 11, [34] S. Nedelkoski, J. Cardoso, and O. Kao, “Anomaly detection from
no. 1, p. 70, 2019. [Online]. Available: https://doi.org/10.1186/ system tracing data using multimodal deep learning,” in 2019 IEEE
s13321-019-0396-x 12th International Conference on Cloud Computing (CLOUD), 2019,
| [18] J.Mitton,H.M.Senn,K.Wynne,andR.Murray-Smith,“Agraphvae |     |     |     |     |     |     | pp.179–186. |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
andgraphtransformerapproachtogeneratingmoleculargraphs,”arXiv [35] X. Zhou, X. Peng, T. Xie, J. Sun, C. Ji, W. Li, and D. Ding, “Fault
preprintarXiv:2104.04345,2021. analysis and debugging of microservice systems: Industrial survey,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Services Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TSC.2025.3622122
14
benchmarksystem,andempiricalstudy,”IEEETransactionsonSoftware Bowen Hao received the B.E. degree in software
Engineering,vol.47,no.2,pp.243–260,2021. engineeringfromNankaiUniversity,Tianjin,China,
[36] X. Zhou, X. Peng, T. Xie, J. Sun, C. Xu, C. Ji, and W. Zhao, in 2023. He is currently working toward M.E. de-
“Benchmarking microservice systems for software engineering greewiththeDepartmentofSoftwareEngineering,
research,” in Proceedings of the 40th International Conference Nankai University. His research interests include
on Software Engineering: Companion Proceeedings, ser. ICSE ’18. LLMforAIOpsandsoftwareengineering.
| New York, | NY, USA: | Association | for | Computing | Machinery, |     | 2018, p. |     |     |     |     |     |     |
| --------- | -------- | ----------- | --- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
323–324.[Online].Available:https://doi.org/10.1145/3183440.3194991
| [37] CloudWise, | “GAIA,” | [Online]. |     | Available: | https://github.com/ |     |     |     |     |     |     |     |     |
| --------------- | ------- | --------- | --- | ---------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
CloudWise-OpenSource/GAIA-DataSet,2021.
| [38] NetManAIOps, | “AIOps | Challenge |     | 2020 Data,” | [Online]. | Available: |     |     |     |     |     |     |     |
| ----------------- | ------ | --------- | --- | ----------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
https://github.com/NetManAIOps/AIOps-Challenge-2020-Data,2020.
| [39] Google Cloud | Platform, | “Online | Boutique,” |     | [Online]. | Available: | https: |     |     |     |     |     |     |
| ----------------- | --------- | ------- | ---------- | --- | --------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
ShenglinZhangreceivedB.S.innetworkengineer-
//github.com/GoogleCloudPlatform/microservices-demo. ingfromtheSchoolofComputerScienceandTech-
[40] S. Zhang, Z. Pan, H. Liu, P. Jin, Y. Sun, Q. Ouyang, J. Wang, nology,XidianUniversity,Xi’an,China,in2012and
X. Jia, Y. Zhang, H. Yang, Y. Zou, and D. Pei, “Efficient and robust Ph.D.incomputersciencefromTsinghuaUniversity,
traceanomalydetectionforlarge-scalemicroservicesystems,”in2023
Beijing,China,in2017.Heiscurrentlyanassociate
IEEE34thInternationalSymposiumonSoftwareReliabilityEngineering
professorwiththeCollegeofSoftware,NankaiUni-
(ISSRE),2023,pp.69–79. versity,Tianjin,China.Hiscurrentresearchinterests
[41] L.Breiman,J.Friedman,R.A.Olshen,andC.J.Stone,Classification include failure detection, diagnosis and prediction
| and Regression | Trees, |         |     |       |         |               |     |                       |     |     |     |     |     |
| -------------- | ------ | ------- | --- | ----- | ------- | ------------- | --- | --------------------- | --- | --- | --- | --- | --- |
|                |        | 1st ed. | New | York: | Chapman | and Hall/CRC, |     | forservicemanagement. |     |     |     |     |     |
1984,eBookPublished19October2017.
YongqianSunreceivedtheB.S.degreeinstatistical
specialty from Northwestern Polytechnical Univer- Changhua Pei received the B.E. and Ph.D. in
sity, Xi’an, China, in 2012, and Ph.D. in computer computersciencefromtheDepartmentofComputer
science from Tsinghua University, Beijing, China, Science and Technology, Tsinghua University in
in 2018. He is currently an assistant professor in 2012and2017,respectively.Heiscurrentlyanasso-
theCollegeofSoftware,NankaiUniversity,Tianjin, ciateprofessorwiththeComputerNetworkInforma-
China.Hisresearchinterestsincludeanomalydetec-
|     |     |     |     |     |     |     |     | tion | Center (CNIC), | Chinese | Academy | of Sciences |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ------- | ------- | ----------- | --- |
tion and root cause localization in service manage- (CAS),Beijing,China.Hisresearchinterestsinclude
|     |     | ment.      |          |     |             |     |          | AIOpsandAIforNetworking. |     |     |     |     |     |
| --- | --- | ---------- | -------- | --- | ----------- | --- | -------- | ------------------------ | --- | --- | --- | --- | --- |
|     |     | Minyi Shao | received | the | B.E. degree | in  | software |                          |     |     |     |     |     |
engineeringfromNankaiUniversity,Tianjin,China,
|     |     | in 2023. | She is currently |     | working | toward | the M.E. |          |     |          |         |           |      |
| --- | --- | -------- | ---------------- | --- | ------- | ------ | -------- | -------- | --- | -------- | ------- | --------- | ---- |
|     |     |          |                  |     |         |        |          | Dongbiao | He  | received | the PhD | degree in | com- |
degree with the Department of Software Engineer- puterscienceandtechnologyfromTsinghuaUniver-
ing, Nankai University. Her research interests in- sity, Beijing, China in 2019. His research interests
cludeAIOpsandanomalydetectioninserviceman- include networking and edge computing systems.
|     |     | agement. |     |     |     |     |     | He received  | his      | B.E. degree | from         | Jilin University, |        |
| --- | --- | -------- | --- | --- | --- | --- | --- | ------------ | -------- | ----------- | ------------ | ----------------- | ------ |
|     |     |          |     |     |     |     |     | China,       | in 2013. | He is       | an associate | professor         | at     |
|     |     |          |     |     |     |     |     | the Computer |          | Network     | Information  | Center            | of the |
ChineseAcademyofSciences.
|     |     | Xiaohui | Nie received   | the  | B.E. degree | in computer |        |     |     |     |     |     |     |
| --- | --- | ------- | -------------- | ---- | ----------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
|     |     | science | and technology | from | Jilin       | University, | Jilin, |     |     |     |     |     |     |
China,in2013,andPh.D.incomputersciencefrom
Tsinghua University, Beijing, China, in 2019. He YanbiaoLireceivedtheB.S.degreeinmathematics
|     |     |              |              |     |           |          |      | from | Hunan University, |     | Changsha, | China, in | 2009, |
| --- | --- | ------------ | ------------ | --- | --------- | -------- | ---- | ---- | ----------------- | --- | --------- | --------- | ----- |
|     |     | is currently | an associate |     | professor | with the | Com- |      |                   |     |           |           |       |
puterNetworkInformationCenter(CNIC),Chinese and Ph.D. in computer science from Hunan Uni-
AcademyofSciences(CAS),Beijing,China.Hisre- versity, Changsha, China, in 2016. He is currently
searchinterestsincludeAIOpsandInternetSecurity. a professor with the Computer Network Informa-
|     |     |     |     |     |     |     |     | tion | Center (CNIC), | Chinese | Academy | of  | Science |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ------- | ------- | --- | ------- |
(CAS),Beijing,China.Hisresearchinterestsinclude
efficientandreliablerouting,andsatellitenetwork.
|     |     | Kaiwen | Yang receivedtheB.E.degreeinsoftware |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
engineeringfromNankaiUniversity,Tianjin,China,
|     |     | in 2025.          | She is currently |     | working     | toward    | the M.E. |     |          |     |          |             |     |
| --- | --- | ----------------- | ---------------- | --- | ----------- | --------- | -------- | --- | -------- | --- | -------- | ----------- | --- |
|     |     | degree with       | the Department   |     | of Software | Engineer- |          |     |          |     |          |             |     |
|     |     | ing, Nankai       | University.      | Her | research    | interests | in-      |     |          |     |          |             |     |
|     |     | cludeAIOpsandLLM. |                  |     |             |           |          | Dan | Pei      |     |          |             |     |
|     |     |                   |                  |     |             |           |          |     | received | the | B.E. and | M.S. degree | in  |
computersciencefromtheDepartmentofComputer
|     |     |     |     |     |     |     |     | Science     | and Technology, |               | Tsinghua       | University   | in      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ------------- | -------------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | 1997        | and 2000,       | respectively, | and            | the Ph.D.    | degree  |
|     |     |     |     |     |     |     |     | in computer | science         | from          | the Computer   |              | Science |
|     |     |     |     |     |     |     |     | Department, | University      |               | of California, | Los          | Ange-   |
|     |     |     |     |     |     |     |     | les (UCLA)  | in              | 2005. He      | is currently   | an associate |         |
XingdaLiHeiscurrentlyworkingtowardtheB.E.
|     |     |             |                |     |             |           |     | professor       | in the | Department | of          | Computer     | Science |
| --- | --- | ----------- | -------------- | --- | ----------- | --------- | --- | --------------- | ------ | ---------- | ----------- | ------------ | ------- |
|     |     | degree with | the Department |     | of Software | Engineer- |     |                 |        |            |             |              |         |
|     |     |             |                |     |             |           |     | and Technology, |        | Tsinghua   | University. | His research |         |
ing,NankaiUniversity.Hisresearchinterestsinclude
|     |     |     |     |     |     |     |     | interests | include | network | and service | management |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | ----------- | ---------- | --- |
anomalydetectionandrootcauselocalization. ingeneral.HeisanIEEEandACMseniormember.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:37:56 UTC from IEEE Xplore.  Restrictions apply.
© 2025 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.