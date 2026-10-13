Received17March2025,accepted11April2025,dateofpublication17April2025,dateofcurrentversion30April2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3562125
Observability in Microservices: An In-Depth
Exploration of Frameworks, Challenges, and
Deployment Paradigms
UMMAYFASEEHA 1,2,(Member,IEEE),HASSANJAMILSYED 3,FAHADSAMAD 4,
SEHARZEHRA 1,ANDHAMZAAHMED1
1DepartmentofComputerScience,NationalUniversityofComputerandEmergingSciences(FAST),Karachi75030,Pakistan
2DepartmentofComputerScienceandSoftwareEngineering,JinnahUniversityforWomen,Karachi74600,Pakistan
3AsiaPacificUniversityofTechnologyandInnovation(APU),KualaLumpur57000,Malaysia
4DepartmentofCyberSecurity,NationalUniversityofComputerandEmergingSciences(FAST),Karachi75030,Pakistan
Correspondingauthor:HassanJamilSyed(hassan.jamil@apu.edu.my)
ThisworkwassupportedbyAsiaPacificUniversityofTechnologyandInnovation(APU),KualaLumpur,Malaysia.
ABSTRACT The widespread adoption of microservices-based architectures in native cloud systems
has amplified the need for robust observability strategies to ensure system reliability and performance.
Microservices,whileenablingscalabilityandflexibility,introducecomplexitiessuchasdistributedfailure
points,performancebottlenecks,andresourcemismanagement.Thispaperprovidesacomprehensivereview
ofstate-of-the-artobservabilityframeworksandtoolsdesignedformicroservicesarchitecture.Itfocuseson
key aspects of observability at the system, service, and network levels, utilizing logs, traces, and metrics
as core data sources. A thematic taxonomy is proposed, classifying the diverse approaches to monitoring
microservices based on implementation paradigms, deployment platforms, and architecture patterns. The
studycomparesexistingsolutionsintermsoftheircapabilities,limitations,andeffectivenessinaddressing
observability challenges in cloud, edge, and fog environments. Furthermore, open research issues are
identified, and practical recommendations are provided to optimize observability in complex, distributed
microservices ecosystems. This work aims to serve as a valuable resource for system architects, DevOps
engineers, and researchers striving to enhance the reliability and performance of modern cloud-native
systems.
INDEX TERMS Microservicesobservability,cloud-basedmicroservices,systemreliability,containerized
computingenvironments,real-timeperformancemonitoring.
I. INTRODUCTION reliability and performance of microservices-based cloud-
The rapid shift of IT infrastructure towards distributed, native systems in increasingly complex environments [2],
complex, and dynamic systems, driven by the increasing [3].Microservicesareawidelyuseddistributedplatform[4],
number of data sources, highlights the growing need [5], with well-known use cases of companies shifting from
for effective observability. Managing resources in such monolithictomicroservicesarchitectureincludingAmazon,
decentralized systems requires advanced tools to address Netflix,Uber,andEtsy[6],[7],[8].Containersarethecorner-
challenges like distributed failures and resource inefficien- stoneofmicroservicesarchitecturebyencasingapplications
cies [1]. The integration of edge and cloud computing and their dependencies into flexible and portable modules.
plays a key role in improving observability by offering They enable isolation, ensuring each microservice operates
real-time monitoring, better system visibility, and more independently while facilitating portability across diverse
efficient management. These advancements help ensure the environments. Containers streamline scalability, resource
efficiency, and version management, supporting continuous
The associate editor coordinating the review of this manuscript and deployment and integration pipelines. With fault isolation
approvingitforpublicationwasRenatoFerrero . and support for DevOps practices, containers empower
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 72011

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
| organizations         |         | to build, deploy, | and        | scale         | microservices |            |     |     |     |     |     |
| --------------------- | ------- | ----------------- | ---------- | ------------- | ------------- | ---------- | --- | --- | --- | --- | --- |
| effectively,          | driving | agility and       | innovation |               | in modern     | cloud-     |     |     |     |     |     |
| native architectures. |         | Microservices     |            | architectures |               | consist of |     |     |     |     |     |
multiplesmall,independentlydeployableserviceshousedin
| containers,      | each | assigned a    | specific  | task  | [9]. The          | number |     |     |     |     |     |
| ---------------- | ---- | ------------- | --------- | ----- | ----------------- | ------ | --- | --- | --- | --- | --- |
| of microservices |      | can vary      | depending | on    | the application’s |        |     |     |     |     |     |
| complexity       | and  | requirements. | These     | small | services          | are    |     |     |     |     |     |
easilydeployableandhighlymultilingual,offeringexcellent
reliabilityandperformanceindistributedandscalableinfras-
tructures[10].Withtheincreasingadoptionofmicroservices FIGURE1. Observabilitycomponentsinmicroservicesarchitectures.
inthecurrentenvironment,computationalcomplexitieswill
rise,potentiallyleadingtosystemperformancedegradation,
service failures, and mismanagement in allocating desired analyzingthenetworkconnections’communicationpatterns,
resources [11], [12]. Real-time active observability and performance metrics, and security aspects between indi-
management of microservices architectures enhance the vidual microservices [30]. This observability better detects
system’sreliabilityandperformance[13],[14].Observability communication issues such as network bottlenecks, high
is based on three main elements as illustrated in fig 1 logs, latency, and congestion, facilitating timely troubleshooting
traces,andmetrics[15],[16].Logsarethesimpletext-based and remediation. Monitoring network traffic and metrics
files containing records of system events and errors [17], can identify performance anomalies, and resources can be
[18], which is a fundamental part of the observability of optimized to ensure scalability and reliability [31]. Addi-
the complex distributed architecture. However, it generates tionally, network-level observability is critical in enhancing
a massive amount of data. Traces are integrated within the security by identifying and alleviating possible threats.
complexsystemtoidentifybottlenecks,end-to-endvisibility Integration with logging and monitoring systems offers a
of the request, and faulty application components without comprehensive view of the application’s behavior, allowing
necessarily identifying the cause of the failure [10], [19]. effectivetroubleshootingandrootcauseanalysis.
Thesemetricshelpgaugeproblemseverity,providevisibility, Edge computing introduces unique observability chal-
|     |     |     |     |     |     |     | lenges due | to its distributed | nature, limited | resources, | and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --------------- | ---------- | --- |
andtriggeralertsincaseofunusualsystemperformance[20],
[21]. With the growing prevalence of microservices in low-latency requirements. Unlike cloud computing, which
modern applications, effectively understanding and mon- benefits from centralized resources and mature monitoring
itoring the diverse range of logs they produce can be tools, edge computing disperses resources across nodes,
challenging [22], [23]. For troubleshooting in case of any including edge devices, fog nodes, and centralized cloud
|     |     |     |     |     |     |     | servers [32]. | This distributed | architecture | necessitates | spe- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------------- | ------------ | ------------ | ---- |
failure,establishingatracebetweentheselogsiscrucial[24].
Insuchsystems,diverselevelsofobservabilityarenecessary cializedobservabilitysolutionstomaintainsystemreliability
to gain deeper insights; among these layers, three primary and efficiency while optimizing resource-constrained edge
levelsofobservabilityhavebeenthefocusofmostresearch devices[33],[34],[35],[36],[37].
efforts: system level, service level, and network level, each Service-level observability takes precedence in edge
|             |     |                  |     |        |                 |     | environments | due to | the frequent | workload shifts | and |
| ----------- | --- | ---------------- | --- | ------ | --------------- | --- | ------------ | ------ | ------------ | --------------- | --- |
| emphasizing | a   | distinct element | of  | health | and performance |     |              |        |              |                 |     |
[25],[26],[27]. real-time processing demands [38], [39]. Services deployed
System level observability ensures the actual applica- on edge nodes often migrate between nodes to adapt to
tion health and the performance of the system, including changing workloads, emphasizing the need for granular
communication of the components using API gateway, performance monitoring to ensure minimal latency [40].
Real-timeobservabilitytoolsmustaccountforthesedynamic
| load balancers, |     | and network | traffic | information, |     | which |     |     |     |     |     |
| --------------- | --- | ----------- | ------- | ------------ | --- | ----- | --- | --- | --- | --- | --- |
depend upon the collected data, for instance, logs, metrics, behaviorstosupportcriticalapplicationssuchasIoTdevices
and traces [28]. This level of observability is needed to andedgeanalytics[41].
evaluate the system’s resilience, scalability, and responsive- Fog computing, as an intermediary layer between edge
ness for smooth communication and interaction between andcloud,addsfurthercomplexitybyrequiringobservability
acrossheterogeneousenvironmentswithdiverseworkloads.
| services. | Conversely, | Service | level | observability |     | focuses on |     |     |     |     |     |
| --------- | ----------- | ------- | ----- | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
monitoring individual microservices, which includes their Monitoringserviceperformanceacrossfognodesintroduces
performance, health, and behavior aspects such as response challenges in managing resource utilization and identi-
times, error rates, and resource usage. The primary goal fying bottlenecks [42]. Specialized tools are needed to
is to ensure that each microservice operates appropriately address these complexities, offering insights into communi-
andefficiently,meetingitsspecifiedservicelevelobjectives cation patterns, performance metrics, and potential security
(SLOs). This is crucial for identifying issues or fine-tuning threats[43].Thesetoolsmustintegrateseamlesslyacrossthe
system components [29]. In microservices-based applica- edge-fog-cloudcontinuumtoprovideaunifiedobservability
| tions, network-level |     | observability |     | includes | monitoring | and | framework. |     |     |               |     |
| -------------------- | --- | ------------- | --- | -------- | ---------- | --- | ---------- | --- | --- | ------------- | --- |
| 72012                |     |               |     |          |            |     |            |     |     | VOLUME13,2025 |     |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
With minimal performance overhead, eBPF emerges as frameworks. ii) It proposes a thematic taxonomy to classify
an ideal observability tool for distributed systems, allowing theexistingliteratureintodistinctcategories.iii)Theresearch
real-timeinsightbetweenedgedevices,fognodes,andcloud methodology section clarifies the main objective of the
infrastructure [44], [45], [46]. Its ability to operate directly research and paper selection method. iv) It analyzes current
within the Linux kernel makes it particularly well-suited solutionsbasedonthisproposedtaxonomy.v)Comparative
forheterogeneousenvironments.Itenablestheexecutionof Analysis of State-of-the-Art Microservices Observability
one’s applications at various places in the kernel, such as Solutions, vi) Evaluation of Microservices Observability
network sockets or system calls, without requiring changes Solutions: Tools, Features, and Performance Metrics, and
to the kernel source code. This allows the behavior of the vii)Lastly,ithighlightsopenresearchissuesandchallenges
kerneltobetailoreddynamicallyandflexiblyandistherefore in microservices observability, offering future guidance for
considered one of the significant improvements [47] in the researchersinthefield.
way,thekernelworkswithuser-definedcode.Thetoolsbeing
used today for the monitoring and visualization of different
II. RELATEDWORK
aspects from a user-space level, for example, Grafana, This section highlights surveys related to various aspects of
Prometheus, BCC, and others [48], use different methods microservices, discussing the contributions, limitations, and
to gather and analyze data from the various layers that motivationoftheresearchersbehindthisstudy.
comprise the software stack, such as applications, services,
andoperatingsystemmetrics.Incontrast,eBPFrunswithin
A. CONTRIBUTIONSANDLIMITATIONSOFTHEEXISTING
theruntimeoftheLinuxkernelrightoutofthebox,enabling
LITERATURE
the execution of custom programs inside the kernel. This
An overview of existing research reveals significant con-
allows for tracing, monitoring, and interaction with events
tributions and notable gaps in the field of microservice
andactivitiesoccurringinthekernel[49].
observability. Usman et al. [56] conducted a survey on
In this paper, we comprehensively surveyed state-of-the-
observability solutions, but their study was confined to
art solutions for microservices observability. Our survey
edge environments, addressing the challenges of distributed
standsoutbypresentingadetailedtaxonomythatcategorizes
edge infrastructures. Kosińska et al. [27] conducted a
variousaspectsofobservability,includingmonitoringparam-
systematic mapping of cloud-native observability based on
eters, implementation paradigms, deployment platforms,
studies from 2018 to 2022, providing valuable insights but
tools, and architecture patterns. This provides a robust
potentiallymissing thelatest trends.Li etal. [16]presented
comparative analysis of state-of-the-art solutions, offering
an industrial survey on microservice tracing, emphasizing
bothqualitativeandquantitativeevaluations,whichprovidea
challenges faced by developers, though its narrow focus on
nuancedunderstandingofvariousobservabilitytools.Unlike
specific practices limit generalizability. Parmar et al. [57]
variousmonitoringframeworksbasedondomainsotherthan
analyzedobservabilitydesignpatternsandtools,focusingon
microservices, such as in the article [50] the researchers
adaptability to project needs, while Li et al. [58] reviewed
Muvskardin et al. focused on observing the agent’s perfor-
quality attributes of microservice architectures, identifying
mance in terms of its decision making and adaptability in
critical factors but overlooking emerging trends. Velepucha
partially observable environments, Min et al [51] offered
and Flores [59] compared microservices’ principles and
smart grid observability using stochastic machine learning-
patternswithmonolithicarchitectures,offeringatheoretical
based approach. In addition, Wu et al. [52], have analyzed
perspective. Lastly, Zhang et al. [60] provided an extensive
thestructureandcommunicationpatternsoftheIoTnetwork
survey on microservice system failure diagnosis, discussing
betweennodes(vertices)toidentifykeyvulnerabilities,inthe
key frameworks and concepts but lacking a focus on recent
article [53], the authors have analyzed the observability of
practicaldevelopments.Collectively,thisliteratureprovides
trafficflowandsensornetworkswithinthecontextofthe6G
valuable insights but reveals limitations in scope and depth,
enabled Internet of Vehicles (IoV). While [54] Congetal.
highlighting the need for a more comprehensive analysis,
addressed critical observability in discrete event systems
asundertakeninthisresearchstudy.Collectively,thestudies
using labeled Petri nets, commonly used in manufacturing,
summarized in table 1 provide valuable insights but reveal
telecommunications, traffic and computer networks, and
limitations in scope and depth, highlighting the need for a
Akbarietal.[55]monitoredandanalyzedresourceutilization
morecomprehensiveanalysis,asundertakeninthisresearch
and energy efficiency in mobile networks 5G and Beyond
study.
5G (B5G), which focus on other areas than microservices
such as IoT security, machine learning and deep learning
environment, 6G (IoV), or sustainability in B5G networks. B. RESEARCHMOTIVATION
Inaddition,weidentifyopenresearchchallengesandissues The motivation for our research comes from the growing
that effectively guide future research directions. The main complexity and importance of observability in modern
contributions of this paper are as follows: i) It surveys microservices architecture [61], [62], [63]. In today’s inter-
state-of-the-art observability solutions for microservices, connected systems, where many small services operate
providingdetailedtechnicalandpracticalinsightsintothese independently, understanding how they interact is crucial.
VOLUME13,2025 72013

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
TABLE1. Summaryofobservabilitydomains,contributions,andshortcomingsofeachsurveypaper.
Observability tools allow us to gain deep insights into to systematically classify existing frameworks and tools.
theseinteractions,whichisessentialformaintainingsystem This taxonomyis designedto address thelack ofstructured
reliabilityandperformance.Astechnologyevolves,therole classifications in the field, enabling a clear understanding
of observability in preventing system failures and ensuring of the functionalities and applicability of each framework.
smoothoperationbecomesevenmorecritical.Thisinspired Furthermore,thestudyoffersacomparativeanalysisofthese
ustoexplorehowobservabilityframeworkscancontributeto frameworks,providinginsightsintotheirrolesinimproving
theefficiencyandstabilityofmicroservices. systemreliabilityandperformance.Bydeliveringactionable
Thesechallengesmakeourcontributiononmicroservices’ insights, this work aims to contribute to the advancement
observability unique with its holistic taxonomy: we classify of observability practices within increasingly complex and
all of the concerns related to observability—monitoring dynamicmicroservicesenvironments.
| parameters,   | implementation |              | paradigms,  |     | deployment | plat-    |     |     |     |     |     |     |
| ------------- | -------------- | ------------ | ----------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| forms, tools, | and            | architecture | patterns—in |     | a highly   | detailed |     |     |     |     |     |     |
B. DATACOLLECTIONPROCESS
| manner. | Our study | provides | a   | qualitative | and | quantitative |          |      |           |            |         |             |
| ------- | --------- | -------- | --- | ----------- | --- | ------------ | -------- | ---- | --------- | ---------- | ------- | ----------- |
|         |           |          |     |             |     |              | Searches | were | conducted | using IEEE | Xplore, | ACM Digital |
comparisonofstate-of-the-artsolutionsforputtingdifferent
|               |       |      |             |     |              |        | Library, | and Google | Scholar, | utilizing |     | targeted keywords |
| ------------- | ----- | ---- | ----------- | --- | ------------ | ------ | -------- | ---------- | -------- | --------- | --- | ----------------- |
| observability | tools | into | perspective |     | with nuanced | under- |          |            |          |           |     |                   |
suchas:
| standing. | It also | focuses | on  | very | recent advancements, |     |     |     |     |     |     |     |
| --------- | ------- | ------- | --- | ---- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
identifiesopenresearchissues,andchallengesfutureresearch
• Observabilityinmicroservices
directions. The completeness of this practically explorative • Containerizedenvironments
| survey of | the observability |     | frameworks |     | make | the survey |     |     |     |     |     |     |
| --------- | ----------------- | --- | ---------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
• MicroservicesPerformanceMonitoringinKubernetes
somewhat different from other studies that may give more • ObservabilityinCloud-NativeApplications
| generalized | insights | or  | have quite | limited | temporal | scopes, |     |     |     |     |     |     |
| ----------- | -------- | --- | ---------- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
further underlining the importance of addressing these Additionally,industry-standardtoolssuchasOpenTeleme-
|     |     |     |     |     |     |     | try, Prometheus, |     | and Grafana | were | selected | due to their |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ---- | -------- | ------------ |
emergingcomplexities.
|                          |       |                  |           |               |               |        | widespread                | adoption. | The | collected   | data            | informed the |
| ------------------------ | ----- | ---------------- | --------- | ------------- | ------------- | ------ | ------------------------- | --------- | --- | ----------- | --------------- | ------------ |
|                          |       |                  |           |               |               |        | thematic                  | taxonomy  | and | facilitated | the comparative | analysis     |
| III. RESEARCHMETHODOLOGY |       |                  |           |               |               |        | ofobservabilitysolutions. |           |     |             |                 |              |
| To effectively           |       | analyze          | the state | of            | observability | frame- |                           |           |     |             |                 |              |
| works and                | tools | in microservices |           | architectures | deployed      | on     |                           |           |     |             |                 |              |
C. SELECTIONOFOBSERVABILITYFRAMEWORKSAND
| containerized | environments, |          | a         | structured | methodology | was        |       |     |     |     |     |     |
| ------------- | ------------- | -------- | --------- | ---------- | ----------- | ---------- | ----- | --- | --- | --- | --- | --- |
| essential.    | This          | approach | considers |            | the added   | complexity | TOOLS |     |     |     |     |     |
introduced by these systems and aims to generate new The selection process prioritized frameworks proposed by
insights into their mechanisms concerning observability. researchers and the tools used within these frameworks,
The methodology highlights the development of a thematic ensuringrelevance tomicroservices andcontainerizedenvi-
|          |                 |     |          |     |                       |     | ronments. | Industry-standard |     | solutions | such | as Prometheus, |
| -------- | --------------- | --- | -------- | --- | --------------------- | --- | --------- | ----------------- | --- | --------- | ---- | -------------- |
| taxonomy | and comparative |     | analysis |     | as key contributions, |     |           |                   |     |           |      |                |
ensuringthefindingsofferactionablescientificvalue. Loki,andJaegerwereincluded,alongwithtoolsdesignedfor
|     |     |     |     |     |     |     | containerized | computing |     | environments | to  | address emerging |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ------------ | --- | ---------------- |
challenges.Theevaluationfocusedonthreekeyobservability
A. RESEARCHOBJECTIVE
features:
Thisstudyprovidesacomprehensivereviewofobservability
frameworksandtoolstailoredforcontainerizedenvironments • Metricscollection
targeting microservice architecture. A primary contribution • Distributedtracing
of this work is the development of a thematic taxonomy • Logaggregations
| 72014 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
These criteria provided comprehensive insights into each solutions;(v)DeploymentEnvironment,identifyingtheenvi-
framework’s role in enabling observability within microser- ronmentslikeKubernetesorDocker;(vi)MonitoringTools,
vicesarchitectures. which lists the specific tools and technologies employed;
|     |     |     |     |     |     | and (vii) | Architecture |     | Pattern, | describing |     | the structural |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | -------- | ---------- | --- | -------------- | --- |
D. INCLUSIONANDEXCLUSIONCRITERIA design of the monitoring solutions. This comprehensive
The following criteria guided the selection of studies and framework,depictedinfig2,aidsinsystematicallyanalyzing
|     |     |     |     |     |     | and comparing |     | different | observability |     | solutions | within | the |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------------- | --- | --------- | ------ | --- |
frameworks:
| InclusionCriteria: |          |     |               |            |     | microservicesecosystem. |     |     |     |     |     |     |     |
| ------------------ | -------- | --- | ------------- | ---------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| • Studies          | focusing | on  | observability | frameworks | for |                         |     |     |     |     |     |     |     |
microservicesincontainerizedenvironments. A. PURPOSEOFMONITORING
|            |     |                  |                |     |             | In the case | of microservices |     | observability, |     | monitoring |     | is an |
| ---------- | --- | ---------------- | -------------- | --- | ----------- | ----------- | ---------------- | --- | -------------- | --- | ---------- | --- | ----- |
| • Research |     | addressing tools | and techniques |     | for metrics |             |                  |     |                |     |            |     |       |
essentialapproachformakingdistributedsystemsrobustand
collection,distributedtracing,andlogaggregation.
|          |            |              |     |             |          | powerful. | Monitoring | shall | include   | anything |              | from     | perfor- |
| -------- | ---------- | ------------ | --- | ----------- | -------- | --------- | ---------- | ----- | --------- | -------- | ------------ | -------- | ------- |
| • Papers | presenting | quantitative | or  | comparative | analyses |           |            |       |           |          |              |          |         |
|          |            |              |     |             |          | mance to  | detection  | and   | diagnosis | of       | any failure, | anomaly, |         |
ofobservabilitysolutions.
Frameworksproposedordesignedbytheresearcherfor andoverallhealthassessmentofapplications.Thisproactive
•
|     |     |     |     |     |     | way helps | an  | organization | identify | issues, | solve | them | in  |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | -------- | ------- | ----- | ---- | --- |
containerizedcomputingenvironments.
theshortesttime,optimizeresources,andenhanceresilience
ExclusionCriteria:
|     |     |     |     |     |     | and flexibility |     | in microservices |     | architecture. |     | Each of | these |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | --- | ------------- | --- | ------- | ----- |
• Studies focusing exclusively on traditional monolithic categoriesisexploredindividually.
architectures.
| Research |     | limited to container | orchestration |     | without |                        |     |     |     |     |     |     |     |
| -------- | --- | -------------------- | ------------- | --- | ------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| •        |     |                      |               |     |         | 1) PERFORMANCEANALYSIS |     |     |     |     |     |     |     |
addressingobservability. Performance analysis deals with the continuous monitoring
| • Outdated |     | studies (published | before | 2019) | unless they |                  |     |          |       |             |          |     |        |
| ---------- | --- | ------------------ | ------ | ----- | ----------- | ---------------- | --- | -------- | ----- | ----------- | -------- | --- | ------ |
|            |     |                    |        |       |             | of the different |     | metrics, | which | may include | response |     | times, |
introducefoundationalconcepts. throughput, and service availability. This is generally done
• Solutionsthatdonotsupportcloud-nativearchitectures tounderstandhowmicroservicesprocessrequeststhatcome
ordistributedenvironments.
|     |     |     |     |     |     | their way       | and the | work  | processing | management. |     | Response |        |
| --- | --- | --- | --- | --- | --- | --------------- | ------- | ----- | ---------- | ----------- | --- | -------- | ------ |
|     |     |     |     |     |     | time monitoring |         | gives | an insight | into        | how | much     | time a |
E. TAXONOMYDEVELOPMENT
|     |     |     |     |     |     | service takes | to  | process | requests | and provide |     | results. | Faster |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ----------- | --- | -------- | ------ |
The thematic taxonomy was created by grouping the tools response times normally mean that things are working well
and frameworks observed based on their key features. and users are having a superior experience. By monitoring
Itconsideredfactorssuchasthepurposeofmonitoring(e.g., these times, an organization can observe which services are
performance analysis, issue detection, root cause analysis), performing slowly and thus need optimization. Throughput
| monitoring | parameters | (e.g., | logs, metrics, |     | traces), and |             |        |         |      |           |           |     |        |
| ---------- | ---------- | ------ | -------------- | --- | ------------ | ----------- | ------ | ------- | ---- | --------- | --------- | --- | ------ |
|            |            |        |                |     |              | defines the | amount | of work | that | a service | completes |     | within |
monitoring levels (e.g., network, system, or service level). a given period, such as the number of requests processed
The taxonomy also included various deployment platforms every second. This metric is important in terms of judging
like cloud, fog, and edge, as well as architectural patterns microservicesontheircapacityandefficiency.Highthrough-
(e.g., service mesh, event-driven) and monitoring tools putmeansthataservicecanprocessmanyrequestswithout
| (e.g., Prometheus, |     | Grafana, | OpenTelemetry). |     | This process |            |       |                 |     |       |      |             |     |
| ------------------ | --- | -------- | --------------- | --- | ------------ | ---------- | ----- | --------------- | --- | ----- | ---- | ----------- | --- |
|                    |     |          |                 |     |              | hindrance, | while | low throughputs |     | might | echo | bottlenecks |     |
involved a thorough analysis and comparison of different or resource limitations. Furthermore, by monitoring service
toolsandframeworkstoensureacomprehensiveandcoherent availability, one is assured that services will be available
classificationsystem. and accessible at the time needed. High availability is
|     |     |     |     |     |     | significantly | important | toretain |     | users’ | trust andsatisfaction |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --------- | -------- | --- | ------ | --------------------- | --- | --- |
withserviceproviders.Thetrackingofdowntimesandhalting
IV. TAXONOMYOFMICROSERVICESOBSERVABILITY
In this section, we introduce a thematic taxonomy that ofservicesshouldprovokeanyorganizationintobeingmore
organizes existing solutions for observability in microser- reliable and avoiding such scenarios. Performance analysis
vices by drawing on common parameters identified in willlettheorganizationunderstandtheperformancetrends,
the literature. A visual classification of these solutions detect anomalies, and understand how changes affect the
is presented in fig 2, highlighting several key factors performanceofservices.Thisenablesongoingimprovement
essential for understanding their diverse applications. This andoptimizationofmicroservices.
classificationincludes:(i)ThepurposeofMonitoring,which
definesthemainobjectivessuchasperformanceassessment 2) FAILUREROOTCAUSEANALYSIS
orfaultdetection;(ii)MonitoringParameters,focusingonthe Rootcausefailureanalysisinvolvesthein-depthinvestigation
specific metrics and data collected; (iii) Monitoring Scope, of errors, exceptions, and events leading to a particular
which differentiates between various operational layers like failure.Itsmainaimistoestablishtherootcauseofaproblem
infrastructure and application; (iv) Implementation Layers, sothatitdoesnotrecuragaininthefuture.Anorganization
detailing the approaches used in deploying monitoring canseektoknowwhereandwhyacertainfailurehappened
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 72015 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
FIGURE2. Thematictaxonomyofmicroservicesobservability.
by gathering logs recording the occurrences of errors and sudden use of 90% could be identified as an anomaly.
exceptions. These logs provide wonderful information on Common statistical techniques include the calculation of z-
the nature of the error, the components involved, and the scores,whichmeasurethenumberofstandarddeviationsan
context under which the issue occurred. Understanding the observation is away from the mean, and moving averages,
eventsequenceleadingtofailureiscriticalinlocatingtheroot smoothing out short-term fluctuations to show longer-term
cause.Eventcorrelationallowsforthetracingofinteractions trends.
and dependence among microservices so one can see how The detection of anomalies with machine learning algo-
a problem in one part of the system might have caused rithmsismuchfiner.Thiscanbeachievedbylearningfrom
failures somewhere else. To that effect, there is usually a the data over time and hence increasing the accuracy of the
technique known as distributed tracing, which helps with anomaliesidentified.Itoftenmakesuseofvarioustechniques
thevisualizationofflowsofrequestsbetweenmicroservices. such as clustering, classification, and neural networks.
The evaluation of impacts brought about by such failures Clusteringalgorithms,forexample,k-means,clustersimilar
presents priorities of fixes in terms of severity and extent datapointsandidentifyoutliersthatdonotfitintoanycluster.
ofusersimpacted.Byidentifyingwhatservicesorusersare Anomaly detection is carried out by training classification
impacted,anorganizationisbettersettofocusresourceson algorithmssuchasdecisiontreesorsupportvectormachines
resolving the most critical issues first. The ultimate goal of onlabeleddatatoidentifytypicalbehaviorversusabnormal
a root cause analysis shall be recommending prevention for behavior. Of all, neural networks, especially deep learning
a similar focus of failures likely to occur in time to come. models, are quite efficient at handling complex and high-
Thekindofsolutionprovidedmaybeabugfix,improvement dimensional data, which proves very effective to pick up
in error handling, or enhancement of general robustness on minor or sophisticated anomalies that may get missed by
microservices.Organizedhandlingoftherootcausecanhelp simplermethods.
an organization increase the reliability and stability of its Apart from the usual techniques, another method of
systems. performinganomalydetectioninvolvesthreshold-basednoti-
fications. This involves setting limits for some metrics,
3) ANOMALYDETECTION threshold-based approaches, and triggering an alert in the
Anomaly detection is the process of finding patterns that caseofabreachofthatlimit.Thisapproachisstraightforward
areatypicalofnormal/usualsystembehavior,hencepointing and works well if the system’s normal behavior is very
to problems in the system. Such problems include security stable, but it could be less useful in dynamic environments
breaches or malfunctioning of the systems. Approaches where normal behavior changes frequently. This may lead
towardsanomalydetectionincludemachinelearning,statisti- to too many false positives when using this method in
calmethods,andthreshold-basedalertingsystems.Statistical such scenarios or missed anomalies. Setting a threshold on
methods of anomaly detection work in ways that include a network volume, for instance, can quickly flag possible
looking at past data to define what normal looks or problems,likeaDDoSattack.
feels like. By knowing these trending patterns, the system Theadvantageofanomalydetectionisthatitprovidesearly
can flag those anomalies that fall out of that trend. For warning of potential entry point issues. By identifying such
example,ifaserver’sCPUnormallyrangesbetween20-40%, anomaliesinatimelyway,organizationscantakecorrective
72016 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
| stepsbeforeissuesspiraloutofcontrol,therebyminimizing |     |     |     |     |     |     |     | 2) METRICS |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
downtimeandcurtailingrisks.
|     |     |     |     |     |     |     |     | Metrics     | provide | insights       | into  | the performance |        | and resource |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------------- | ----- | --------------- | ------ | ------------ |
|     |     |     |     |     |     |     |     | utilization | of      | microservices. | These | can             | be CPU | utilization, |
4) OVERALLAPPLICATIONHEALTH memory usage, and network throughput or traditional
Overallstatusanalysisofasystembeginswithhealthchecks application-level metrics such as active users or several
and ends with resource utilization, including dependency processed transactions per second. Such monitoring of
| checks. | This will | ensure | comprehensive |     | optimization |     | of all |         |         |                  |     |             |        |         |
| ------- | --------- | ------ | ------------- | --- | ------------ | --- | ------ | ------- | ------- | ---------------- | --- | ----------- | ------ | ------- |
|         |           |        |               |     |              |     |        | metrics | enables | the organization |     | to perceive | system | health, |
themicroserviceswithinthesystem.Theseareperiodictests performancetrends,andanomaliesthatmayindicateimpend-
to ensure the proper functioning of any given microservice. ingproblemsoroptimizationopportunities.Themetricsare
Checksforthestatusofdifferentcomponents,whichinclude aggregated over time and can be visualized through graphs
databases, APIs, and third-party services, are conducted. and dashboards to proactively analyze performance and do
| These would |     | include, | for example, |     | ping | tests | that send |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------------ | --- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
capacityplanning.
| simple requests |        | to services | to   | see if | they      | are available, | and       |     |     |     |     |     |     |     |
| --------------- | ------ | ----------- | ---- | ------ | --------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| custom          | health | endpoints   | like | health | or status | that           | report on |     |     |     |     |     |     |     |
3) TRACES
the health status of a service. The checks on dependencies Traces capture detailed information about every request
| check for | the           | health and | availability |             | of      | all those | external |          |             |           |         |                 |     |              |
| --------- | ------------- | ---------- | ------------ | ----------- | ------- | --------- | -------- | -------- | ----------- | --------- | ------- | --------------- | --- | ------------ |
|           |               |            |              |             |         |           |          | crossing | the system, | capturing |         | each involved   |     | microservice |
| services  | and resources |            | the          | application | depends |           | on. Such |          |             |           |         |                 |     |              |
|           |               |            |              |             |         |           |          | in turn. | Tracing     | should    | provide | a fine-granular |     | view of      |
checks are meant to ascertain that all the dependencies are request processing, including latency measurements and
up,reachable,andperformingwell.Examplesofthisinclude
dependenciesbetweenmicroservices.Onlythencananorga-
| database | reachability |     | and responsiveness, |     |     | as well | as the |          |         |        |             |             |     |             |
| -------- | ------------ | --- | ------------------- | --- | --- | ------- | ------ | -------- | ------- | ------ | ----------- | ----------- | --- | ----------- |
|          |              |     |                     |     |     |         |        | nization | analyze | traces | to identify | performance |     | bottlenecks |
availabilityandresponsetimesofAPIs.Resourceutilization
|     |     |     |     |     |     |     |     | and optimize |     | request paths | to  | improve | responsiveness | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | ------- | -------------- | --- |
reviewsfocusonmonitoringCPU,memory,diskspace,and
|     |     |     |     |     |     |     |     | microservices |     | overall. Especially |     | in large | modern | complex |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------- | --- | -------- | ------ | ------- |
network bandwidth usage. This helps identify bottlenecks distributed systems, traces become particularly important
| and potential |     | problems | caused | by  | resource | shortages. | For |                |     |        |             |         |     |            |
| ------------- | --- | -------- | ------ | --- | -------- | ---------- | --- | -------------- | --- | ------ | ----------- | ------- | --- | ---------- |
|               |     |          |        |     |          |            |     | when knowledge |     | of the | interaction | between |     | components |
example,CPUusageismonitoredtopreventanyservicefrom
|             |     |            |            |     |        |     |            | provides    | a means | of diagnosing |         | issues | and heading | toward    |
| ----------- | --- | ---------- | ---------- | --- | ------ | --- | ---------- | ----------- | ------- | ------------- | ------- | ------ | ----------- | --------- |
| overloading | the | processor. | Similarly, |     | memory | is  | checked to |             |         |               |         |        |             |           |
|             |     |            |            |     |        |     |            | resolution. | Tracing | will          | further | enable | root cause  | analysis, |
avoidleaksandensureefficientusage,diskspaceistracked
|     |     |     |     |     |     |     |     | performance | optimization, |     | and | troubleshooting |     | by adding |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --- | --------------- | --- | --------- |
topreventrunningoutofstorage,andnetworkbandwidthis visibilitytorequestflowsandservicedependencies.
| monitored | to maintain |     | smooth | communication |     | between | ser- |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------ | ------------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
vices.Theprimarygoalofassessinganapplication’soverall
C. MONITORINGSCOPE
| health is     | to ensure | that        | microservices |        | function |     | efficiently. |                |     |                  |     |                   |     |            |
| ------------- | --------- | ----------- | ------------- | ------ | -------- | --- | ------------ | -------------- | --- | ---------------- | --- | ----------------- | --- | ---------- |
|               |           |             |               |        |          |     |              | In the context |     | of observability |     | in microservices, |     | monitoring |
| This involves |           | identifying | and           | fixing | issues   |     | proactively  |                |     |                  |     |                   |     |            |
requireatmultiplelevelstoensurecomprehensiveinsightinto
beforetheyaffectusers,guaranteeingahighlyavailableand
thebehaviorandperformanceofthesystem.
| performance-driven |          | system. |       | It ensures    | seamless |        | interaction |     |     |     |     |     |     |     |
| ------------------ | -------- | ------- | ----- | ------------- | -------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| between            | services | and     | their | dependencies, |          | avoids | resource    |     |     |     |     |     |     |     |
1) NETWORKLEVEL
exhaustion,andpromotesoptimalresourceutilization.
|     |     |     |     |     |     |     |     | This will | monitor | the              | interaction | between |         | the involved |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------------- | ----------- | ------- | ------- | ------------ |
|     |     |     |     |     |     |     |     | services, | how     | one microservice |             | sends   | data to | another, and |
B. MONITORINGPARAMETERS
|                   |     |               |     |             |     |       |          | so forth. | It also | identifies | any | potential | failure | points that |
| ----------------- | --- | ------------- | --- | ----------- | --- | ----- | -------- | --------- | ------- | ---------- | --- | --------- | ------- | ----------- |
| The microservices |     | observability |     | parameters: |     | logs, | metrics, |           |         |            |     |           |         |             |
and traces are essential for understanding the performance, may lead to breaking this communication chain. You are
|           |     |           |             |     |          |      |          | able to | see how | much | traffic | goes between |     | services with |
| --------- | --- | --------- | ----------- | --- | -------- | ---- | -------- | ------- | ------- | ---- | ------- | ------------ | --- | ------------- |
| behavior, | and | health of | distributed |     | systems. | Each | of these |         |         |      |         |              |     |               |
elements provides unique insights, helping manage and the help of the traffic patterns. Latency refers to how long
optimizethemicroservicesarchitectureeffectively. datatakestotravelbetweenservices.Itisanotherimportant
|     |     |     |     |     |     |     |     | metric that | helps | locate | delays | or bottlenecks. |     | Investigating |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | ------ | --------------- | --- | ------------- |
1) LOGS network issues, such as lost packets or failed connections,
canbedonebymonitoringtherateofcommunicationerrors.
Logsincludetextdatageneratedbymicroservices,recording
Inaddition,networkthroughputmonitoringensuresthatdata
| various | events, | the occurrence |     | of  | error messages, |     | transac- |     |     |     |     |     |     |     |
| ------- | ------- | -------------- | --- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tions, and changes in system status. The result from log throughput occurs at an acceptable rate, which is critical
|          |          |                 |     |     |               |     |        | for the | overall | performance |     | of the system. | That | level of |
| -------- | -------- | --------------- | --- | --- | ------------- | --- | ------ | ------- | ------- | ----------- | --- | -------------- | ---- | -------- |
| analysis | provides | a much-valuable |     |     | understanding |     | of the |         |         |             |     |                |      |          |
point where things went wrong, timelines showing what monitoringiskeytoensuringthenetworksupportsseamless
operationofmicroservices.
| happened  | to lead        | to failure, |     | and such     | request | flows      | among  |     |     |     |     |     |     |     |
| --------- | -------------- | ----------- | --- | ------------ | ------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| different | microservices. |             | The | logs provide |         | an ordered | record |     |     |     |     |     |     |     |
of activities that help to identify the root cause of system 2) SYSTEMLEVEL
events. Therefore, they are useful in detecting anomalies in System-levelmonitoringisfocusedontheunderlyinginfras-
the system, diagnosing problems, and many other activities tructure whether it is physical servers or virtual machines.
criticalforensuringsystemreliability. The performance here flows directly into the reception
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 72017 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
of the microservices. CPU load provides insight into the right near the end user. This decentralized approach helps
extentofprocessingpowerbeingutilized,therebyindicating reduce latency and improve application responsiveness by
potentialresourceoverloading.DiskI/Omonitoringassesses processing data closer to its origin. In fog computing,
the rate at which data is read from or written to the disk, intermediate nodes handle tasks like data aggregation and
whichisparticularlycriticalforservicesthatrelyheavilyon initial processing, which helps reduce bandwidth usage and
stored data for their operations. Monitoring memory usage lessentheloadoncentralservers.Thismodelisparticularly
isessential,asinsufficientmemorycansignificantlydegrade effectiveforreal-timeapplications,suchasIoTdevicesand
service performance and, in many cases, lead to complete edgeanalytics,wherequickdataprocessingisessential.
systemfailure.Onlybycloselymonitoringthesesystem-level
metrics is it possible to keep issues at bay before they start 3) EDGE
impacting microservices performance, hence maintaining a Edgecomputingbringscomputationanddatastoragecloser
stableandefficientinfrastructure. to the source of the data, like within IoT devices or
sensors.Processingtaskslocallyratherthansendingdatato
3) SERVICESLEVEL centralservers,significantlycutsdownonlatency,improving
Ontheserviceslevel,monitoringisfocusedontheapplication responsiveness. This method is ideal for applications that
layer, essentially the performance and behavior of each require fast data processing and high bandwidth, such as
microservice. This form of monitoring is very crucial in autonomous vehicles and industrial control systems. Addi-
handling the general performance of the application. All tionally, edge computing reduces the need for continuous
the services put up will be closely watching error rates data transmission to central servers, saving bandwidth and
so that a bug or failure can be quickly detected very fast. boostingoverallefficiency.
Besides,responsetimesaregoingtobeimportanttomonitor Inadditiontodeploymentlayers(cloud,fog,edge),observ-
because they show at what speed a service is capable of abilitytoolscanalsobecategorizedbasedontheirimplemen-
processing requests and thereby directly influence the user tation paradigms. Open standard tools like Prometheus and
experience.Moreover,transactionvolumesneedtobetracked OpenTelemetryareknownfortheirflexibilityandabilityto
tounderstandtheloadoneachserviceanditsgreaterabilityto operateacrossdiverseenvironments.Incontrast,proprietary
dealwithrisingdemand.Thisisdonebylookingatthevalues toolssuchasDatadogandAWSCloudWatchofferseamless
of these metrics, hence giving important information on the integrationbutarelimitedtospecificvendors.However,the
performance of each microservice that leads to proactive tools are further discussed under the heading monitoring
management for the smooth and effective running of the tools.
wholeapplication.Thismonitoringlevelisimportantinterms
of maintaining a reliable, highly performing microservices E. DEPLOYMENTENVIRONMENT
architecture. Microservicescanbedeployedusingvariousplatforms,each
tailored to meet specific operational needs and enhance the
D. IMPLEMENTATIONLAYERS managementofcontainerizedapplications.Inthissubsection,
Microservicescanbeimplementedinvariousenvironments, we examine a set of widely recognized monitoring tools
each offering unique advantages and catering to specific for microservices-based architectures, identified through an
requirements. extensivereviewoftheliterature.
1) CLOUD 1) DOCKERSWARM
Theimplementationofmicroservicesoncloudinfrastructure Docker Swarm serves as a native clustering system for
brings significant advantages, such as scalable resources, Docker, effectively transforming a group of Docker hosts
high reliability, and extensive geographical coverage. Plat- intoasingular,cohesivevirtualhost.Keymonitoringaspects
formslikeAWS,Azure,andGoogleCloudofferon-demand should include the status of nodes, containers, and services
resourcesthatadjusttoworkloadfluctuations,enablingappli- withintheswarm.Thisplatformisparticularlyadvantageous
cationstohandlepeakdemandsefficientlywithoutrequiring for simplified orchestration, native integration with Docker
substantialupfrontinvestmentsinhardware.Furthermore,the environments,andstreamlinedscalabilityofapplications.
cloud’s distributed architecture boosts service reliability by
spreadingresourcesacrossmultipledatacenters,reducingthe 2) KUBERNETES
riskofdowntime.Forapplicationswithglobalaudiencesor Kubernetes excels in managing and dynamically scaling
variabledemands,thecloud’seffectiveresourcemanagement microservices,usingconfigurationsthatmeticulouslydefine
andsimplifieddeploymentprocessmakeitahighlybeneficial the desired operational state of applications. Monitoring
choice. effortsforKubernetesshouldfocusonassessingpodstatus,
cluster resource allocation, and orchestration behaviors.
2) FOG This platform is renowned for its robustness in handling
Fog computing extends cloud computing by bringing more complexapplications,extensivecommunitysupport,andits
computational resources closer to the edge of the network, capability to ensure continuous availability and resilience.
72018 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
traces,andlogs.Foundedin2010,Datadogoffersextensive
automationandmonitoringcapabilitiesacrosscloudservices,
servers, databases, tools, and services. The tool is known
foritsreal-timeperformancedashboardsandscalableinfras-
tructure monitoring that can handle vast amounts of data
and applications. Airbnb and Netflix leverage Datadog for
their comprehensive monitoring capabilities that integrate
seamlesslywiththeircomplexcloudenvironments.
3) GRAFANA
Grafana is an open-source platform for monitoring and
observability,knownforitssophisticatedvisualizationcapa-
bilities. Launched in 2014, it works seamlessly with a
FIGURE3. Kubernetescluster. variety of databases, including Prometheus, MySQL, and
Elasticsearch,todisplaydatathroughcomprehensivegraphs,
charts,andalerts.However,Toaccesstheadvancedfeatures
The architecture of a Kubernetes cluster is shown in
of Grafana Enterprise, an Enterprise license activation
fig 3, comprising a master node and various worker nodes.
is required. Grafana allows users to create customized
The master node, containing components such as the API
dashboards according to their monitoring needs. Uber and
server, scheduler, controller manager, and etcd, manages
eBay use Grafana for its powerful visualization capabilities
the cluster’s overall state and scheduling of workloads. The
tomonitortheirvastoperationsandtohelpwiththeanalysis
worker nodes, equipped with kubelet and kube-proxy, are
oftheirmetricsandlogs.
responsible for running the containerized applications and
maintaining network communication. The API server acts
4) ZIPKIN
as the central management interface, while etcd serves as
Zipkinisadistributedtracingsystemthatcollectsandman-
the key-value store for all cluster data. Together, these
agestimingdatatodiagnoselatencyissuesinmicroservices
components ensure efficient and consistent operation of
architectures, facilitating both data collection and retrieval.
containerizedapplicationswithintheKubernetescluster.
Originating from Twitter and based on the Google Dapper
paper, Zipkin provides crucial insights into application per-
F. MONITORINGTOOLS
formanceandissuesrelatedtocomplexdistributedsystems.
In this subsection, we examined a set of widely recognized
Twitter and major financial institutions like Credit Karma
monitoringtoolsformicroservices-basedarchitectures,iden-
deploy Zipkin to trace transactions through their distributed
tified through an extensive review of the literature. These
servicesanddiagnoselatencyissueseffectively.
toolswereselectedbasedontheirfrequentimplementationby
researchersandindustrypractitioners,aswellastheirproven
effectivenessinenhancingobservability,maintainingsystem 5) WEAVESCOPE
health, and ensuring uninterrupted services. They address Weave Scope is an open-source tool specifically designed
criticalaspectssuchaslogging,tracing,metrics. for monitoring, visualizing, and managing Docker and
Kubernetes containers. It automatically generates a map
1) PROMETHEUS of your processes, containers, and hosts, allowing you
Prometheus is an open-source monitoring solution devel- to understand, monitor, and control your applications and
oped by SoundCloud in 2012. It’s designed for reliability containersdirectlyfromyourbrowser.
and scalability, primarily handling multi-dimensional data
collection and querying. It has a strong ecosystem and 6) LOKI
integrateswithvariousservicediscoveryoptionswhileusing Loki,createdbyGrafanaLabs,isahorizontallyscalablelog
atime-seriesdatabaseforstoringitsdata.Prometheusgathers aggregation system that can expand across multiple servers
metrics from monitored targets by polling HTTP endpoints to manage large data volumes. It ensures high availability,
onthesetargets.Oneofitscorefeaturesisapowerfulquery soitremainsoperationalevenifsomepartsfail,andsupports
languagecalledPromQL.GitLabandRedHatareamongthe multiple tenants, enabling different users or organizations
major users of Prometheus. They utilize it to monitor their to share the system without overlapping data. Launched
infrastructureandensuretheirsystemsoperateefficientlyand in 2018 and inspired by Prometheus, Loki is designed to
reliably. be cost-effective and user-friendly. Instead of indexing the
full content of log entries like traditional systems, Loki
2) DATADOG indexeslogsbasedontheirlabels.Thislabel-basedindexing
Datadog is a SaaS-based monitoring and analytics platform reduces storage needs and processing demands, making
thatprovidesfull-stackobservabilitybyintegratingmetrics, log management more economical and efficient. This tool
VOLUME13,2025 72019

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
simplifies searching and retrieving logs, minimizing system maintaining the reliability and efficiency of microservices
performanceandcostimpacts. environments.
7) OpenTelemetry G. ARCHITECTUREPATTERN
OpenTelemetry is an observability framework for cloud- Architecturepatternsplayacrucialroleinenablingeffective
native software, providing APIs and libraries to collect observability in microservices. Observability, in the con-
distributedtracesandmetricsfromapplications.ItisaCloud text of microservices, involves the ability to monitor and
NativeComputingFoundation(CNCF)projectthatemerged understand the state and behavior of services, which helps
fromthemergingofOpenCensusandOpenTracingprojects. in identifying issues, optimizing performance, and ensuring
OpenTelemetry aims to make telemetry data (metrics, logs, reliability.
and traces) a built-in feature of cloud-native software
applications.
1) APIGATEWAY
TheAPIGatewayisamanaginglayerthatactsasthesingle
8) BPFTrace point of entry for external clients into the microservices
BPFTrace is a high-level tracing tool for Linux based on ecosystem.Thispatternisdesignedtoaddressthecomplexity
BPF,theBerkeleyPacketFilter.Itwasdevelopedasamore ofhavingmultipleendpointsbyprovidingaunifiedinterface
accessibleinterfacefordynamictracinginLinux,providinga to clients. The gateway routes incoming requests to the
powerfulandflexiblewaytoobserveandmodifythebehavior appropriate microservices while also handling cross-cutting
ofrunningLinuxsystems.BPFTraceisespeciallyusefulfor concerns such as authentication, authorization, and rate
analyzing performance issues and troubleshooting system limiting.Additionally,itcanaggregateresultsfrommultiple
calls and events. Facebook and Netflix use BPFTrace for microservices into a single response to simplify the client
dynamictracingintheirLinuxenvironmentstoanalyzeand experience. The use of an API Gateway can facilitate the
debugperformanceissuesinreal-time. management of endpoints, especially in large systems with
numerousmicroservices,anditcanbepivotalinorchestrating
microservices’ interactions and optimizing communication
9) ISTIO
Istio is a comprehensive service mesh that significantly flows.
enhances the monitoring of microservices by facilitating
detailed insights and control over complex microservices 2) EVENT-DRIVEN
architectures. It automatically collects telemetry data such In an event-driven architecture, microservices communicate
as metrics, logs, and traces through sidecar proxies, which with each other using events. This pattern promotes a high
integrate seamlessly with each service. This enables Istio level of decoupling as services do not send requests to
to provide real-time traffic management, service graphs, each other directly but instead produce and consume events
and observability without modifying the microservices asynchronously. Events are typically emitted as a result of
themselves. Additionally, Istio supports integrations with a service performing a task, such as updating a database or
populartoolslikePrometheus,Grafana,andJaeger,offering processingauseraction.Otherserviceslistentotheseevents
advancedcapabilitiesfordashboardvisualization,distributed and react accordingly, which allows for a responsive and
tracing,andanomalydetection.Thisrobustfeaturesetallows flexiblesystemthatcaneasilyadapttochanges.Thispattern
for effective monitoring, alerting, and operational visibility, is especially beneficial in dynamic environments where
making Istio an invaluable tool for managing distributed services need to scale independently and remain resilient to
microservicesenvironments. thefailuresofothers.
10) JAEGER 3) SERVICEMESH
Jaeger is an open-source distributed tracing tool that excels A service mesh introduces a transparent layer of infrastruc-
in monitoring microservices by providing deep insights ture dedicated to managing service-to-service communica-
into the interactions and performance of complex service tion in a microservices architecture. It effectively abstracts
architectures. It enables detailed tracking of requests across thecomplexityoftheseinteractionsbyprovidingadistributed
services, helping to identify bottlenecks, optimize perfor- networking layer that has a broad understanding of the
mance, and conduct effective root cause analysis. Jaeger’s architecture and can control communication. This pattern
integration with other monitoring and observability tools facilitates features like service discovery, load balancing,
like Prometheus, Grafana, and service meshes such as Istio encryption, observability, and traceability without requiring
enhances its capability to offer comprehensive visibility changes to the individual services. A service mesh employs
without the need for invasive code modifications. With its sidecarproxiesthataccompanyeachservice,takingrespon-
user-friendlywebUI,Jaegerfacilitatesthevisualizationand sibility for inter-service communications, which allows
analysis of traces, making it easier for teams to understand developers to focus on the business logic within individual
service dependencies and data flow, which are critical for servicesratherthantheintricaciesofnetworkmanagement.
72020 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
TABLE2. Comparisonofobservabilitytools[64].
This taxonomy of microservices observability is struc- A. STATE-OF-THE-ARTMICROSERVICESOBSERVABILITY
| tured into | six interrelated |     | categories, | each | serving | distinct |     |     |     |     |     |     |     |     |
| ---------- | ---------------- | --- | ----------- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
SOLUTIONS
monitoring objectives. The Purpose of Monitoring includes This subsection highlights recently published research
performance analysis, failure root cause analysis, anomaly works and presents a comprehensive review of state-of-the-
detection, and overall application health, which all aim to art microservices observability solutions. In recent years,
ensure system reliability and efficiency. These purposes are observability has become a critical focus in microservices
| supported | by specific | Monitoring |     | Parameters, | such | as logs |     |     |     |     |     |     |     |     |
| --------- | ----------- | ---------- | --- | ----------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
architectureduetothecomplexityintroducedbydistributed
for understanding system events, metrics for performance systems. Modern research emphasizes the necessity of
evaluation, and traces for tracking requests across services. observability in ensuring service reliability, performance
| Monitoring | occurs | at different |     | Levels, including |     | the net- |             |     |           |                  |     |        |     |         |
| ---------- | ------ | ------------ | --- | ----------------- | --- | -------- | ----------- | --- | --------- | ---------------- | --- | ------ | --- | ------- |
|            |        |              |     |                   |     |          | monitoring, | and | effective | troubleshooting. |     | Recent |     | studies |
work, system, and services layers, each offering insights have focused on advanced techniques for tracing, logging,
into various aspects of the microservices architecture. The andmetricscollectiontoenhancevisibilityandunderstand-
Implementation Paradigm covers deployment environments ingofmicroservicesenvironments.
| like cloud,   | fog, | and edge,     | influencing | how        | monitoring | tools      |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------------- | ----------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| are deployed. | The  | Microservices |             | Deployment |            | Platforms, |     |     |     |     |     |     |     |     |
1) MDF(MODELDRIVENFRAMEWORK)
| such as   | Kubernetes | or Docker |             | Swarm, integrate |           | with these |            |      |               |     |              |             |     |     |
| --------- | ---------- | --------- | ----------- | ---------------- | --------- | ---------- | ---------- | ---- | ------------- | --- | ------------ | ----------- | --- | --- |
|           |            |           |             |                  |           |            | Fè et al., | [65] | proposed      | a   | model-driven | methodology |     | to  |
| paradigms | to manage  | and       | orchestrate |                  | services. | Finally,   |            |      |               |     |              |             |     |     |
|           |            |           |             |                  |           |            | evaluate   | the  | dependability |     | and energy   | consumption |     | of  |
variousMonitoringToolslikePrometheus,Loki,andGrafana
|                |               |                 |     |                     |          |            | Kubernetes-based  |            | cloud     | fog    | systems.     | The proposed    |           | model  |
| -------------- | ------------- | --------------- | --- | ------------------- | -------- | ---------- | ----------------- | ---------- | --------- | ------ | ------------ | --------------- | --------- | ------ |
| provide        | the technical | capability      |     | to observe          | and      | manage     |                   |            |           |        |              |                 |           |        |
|                |               |                 |     |                     |          |            | uses a            | stochastic | approach  |        | to predict   | system          | behavior, |        |
| microservices, |               | while specific  |     | Architecture        | Patterns | like       |                   |            |           |        |              |                 |           |        |
|                |               |                 |     |                     |          |            | with a particular |            | focus     | on the | performance  |                 | of cloud  | and    |
| service        | mesh and      | API gateways    |     | ensure that         | the      | monitoring |                   |            |           |        |              |                 |           |        |
|                |               |                 |     |                     |          |            | fog computing     |            | layers    | under  | different    | configurations. |           | The    |
| frameworks     | are           | well-integrated |     | with the underlying |          | service    |                   |            |           |        |              |                 |           |        |
|                |               |                 |     |                     |          |            | proposed          | system     | monitored | system | availability |                 | and       | energy |
architecture.
|     |     |     |     |     |     |     | consumption, |     | with a | significant | finding | demonstrating |     | a   |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ----------- | ------- | ------------- | --- | --- |
22.33%increaseinsystemavailabilityandaminimal1.33%
|     |     |     |     |     |     |     | increase | in energy | consumption. |     | This | model | offers a | struc- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------ | --- | ---- | ----- | -------- | ------ |
V. REVIEWANDCOMPARATIVEANALYSISOF
STATE-OF-ARTMICROSERVICESOBSERVABILITY turedapproachtoanalyzingandcomparingthedependability
SOLUTIONS of different systems and serves as a guide to optimize
The section consists of two parts. The first part offers a source allocation. The proposed methodology involves
detailed review of the state-of-the-art microservices observ- empirical validation through rigorous testing in controlled
ability solutions, highlighting the most recently published environments to ensure accurate dependability and power
researchfindings.Inthesecondpart,acomparativeanalysis consumption assessments, contributing to enhanced system
ofthesesolutionsisprovidedbasedonthethematictaxonomy performance and sustainability in cloud fog computing
| definedinsectionIV. |     |     |     |     |     |     | environments. |     |     |     |     |     |     |       |
| ------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME13,2025       |     |     |     |     |     |     |               |     |     |     |     |     |     | 72021 |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
2) METROFUNNEL degradation over the cloud infrastructure. The proposed
systemisbasedonthemachinelearningmodel,isdeployed
| Cinque | et al., [66] | proposed |     | a monitoring |     | system | for |     |     |     |     |     |     |     |
| ------ | ------------ | -------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
microservicesusingeventlogscombinedwithpassiveblack over the virtual machine that can monitor the traces data
box tracing to capture data like resource usage and opera- for the fine-grain analysis of the system and predict the
tional statistics essential for maintaining service continuity. microservices performance degradation 100s to 200s ahead
Theproposedmethod,MetroFunnel,enhancestroubleshoot- of it happens. The accuracy of the proposed system is 90%
anditsF1scoreis0.7withminimaloverheads.
| ing by automatically |               | generating         |        | detailed  | execution |             | traces |           |                  |     |      |          |     |             |
| -------------------- | ------------- | ------------------ | ------ | --------- | --------- | ----------- | ------ | --------- | ---------------- | --- | ---- | -------- | --- | ----------- |
| without modifying    |               | the microservices, |        | making    |           | it suitable | for    |           |                  |     |      |          |     |             |
| complex              | environments. |                    | Tested | in Docker | and       | Kubernetes  |        | 6) BbMA   |                  |     |      |          |     |             |
|                      |               |                    |        |           |           |             |        | Brondolin | and Santambrogio |     | [70] | proposed |     | an approach |
setups,MetroFunnelsupportsefficientproblem-solvingwith
minimalperformanceanddataoverhead,provinganeffective for microservices monitoring at runtime with less overhead
usingeBPFtechnology.Thisapproachisintegratedwiththe
| tool for | operational | transparency |     | and | troubleshooting |     | in  |     |     |     |     |     |     |     |
| -------- | ----------- | ------------ | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
existingtoolSysdigforCPU,memory,networkIOmetrics,
microservicesarchitectures.
|     |     |     |     |     |     |     |     | Weave scope | for | CPU usage | and | network | connections, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | --- | ------- | ------------ | --- |
PrometheusforAPIs,time-seriesdatabase,andvisualization
3) MOA(MODERNOBSERVABILITYAPPROACH)
interface.
Tzanettisetal.,[67]focusedonenhancingtheobservability
| and management |                   | of distributed |     | applications, |     | particularly |          |          |     |     |     |     |     |     |
| -------------- | ----------------- | -------------- | --- | ------------- | --- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- |
|                |                   |                |     |               |     |              |          | 7) NEZHA |     |     |     |     |     |     |
| those based    | on microservices, |                |     | by addressing |     | the          | disjoint |          |     |     |     |     |     |     |
nature of information provided by existing frameworks Yu et al., [71] proposed an observability framework for
|     |     |     |     |     |     |     |     | the root cause | analyses |     | of the microservices-based |     |     | system. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | -------------------------- | --- | --- | ------- |
andcloudcomputingorchestrationplatforms.Theproposed
methodology integrates various observability signals such The collected data was multi-modal and contained the
as metrics, logs, and distributed tracing mechanisms from heterogeneousdataoflogs,traces,andmetricsattheservices
|          |             |            |     |     |        |         |      | level and | inner | services | level, | and the | varied | data into a |
| -------- | ----------- | ---------- | --- | --- | ------ | ------- | ---- | --------- | ----- | -------- | ------ | ------- | ------ | ----------- |
| multiple | open-source | frameworks |     | to  | form a | unified | view |           |       |          |        |         |        |             |
that facilitates performance issue insights and root cause homogeneous form for further analyses to better address
|           |               |     |                 |     |         |     |         | the root | cause in | case | of service, | failure. | This | approach |
| --------- | ------------- | --- | --------------- | --- | ------- | --- | ------- | -------- | -------- | ---- | ----------- | -------- | ---- | -------- |
| analysis. | This approach |     | is demonstrated |     | through |     | a pilot |          |          |      |             |          |      |          |
implementation involving the stress testing of a proof-of- mainlyfocusesonanomalydetection,however,thesuggested
concept microservices-based application, which validated approach is unable to detect certain byzantine errors, such
|                 |     |                |     |      |         |        |     | as providing | the | user with | an  | irrational | result. | Since the |
| --------------- | --- | -------------- | --- | ---- | ------- | ------ | --- | ------------ | --- | --------- | --- | ---------- | ------- | --------- |
| the methodology |     | by identifying |     | main | latency | causes | and |              |     |           |     |            |         |           |
enhancing the application’s behavior understanding under proposedapproachcanprocessmulti-modaldataandidentify
abroaderrangeoffaultbehaviors,itoutperformsallbaseline
differentconditions.Theresultsconfirmedtheeffectiveness
|             |        |          |     |           |        |     |      | techniques | at the | service | level | with high | accuracy | (97% at |
| ----------- | ------ | -------- | --- | --------- | ------ | --- | ---- | ---------- | ------ | ------- | ----- | --------- | -------- | ------- |
| of the data | fusion | approach | in  | providing | deeper | and | more |            |        |         |       |           |          |         |
actionable observability of distributed applications, thereby both top 3 and top 5 and 90% at top 1), making it the most
effectivetoolavailable.
| supporting | better | management |     | and troubleshooting |     | of  | these |     |     |     |     |     |     |     |
| ---------- | ------ | ---------- | --- | ------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
systems.
|     |     |     |     |     |     |     |     | 8) KUNERVA |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
4) AET(APPROACHFOREXPLAINABILITYAND LeeandNam[72]proposedaframeworkbasedonnetwork
TRACEABILITY) policy generation to avoid security attacks occurring due
|     |     |     |     |     |     |     |     | to misconfiguration. |     | They | applied | Cilium | Hubble | for the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ---- | ------- | ------ | ------ | ------- |
Pierre-JeanandZdun[68]proposedamethodtoanalyzeand
recover the architecture of complex microservices systems, network monitoring to collect the logs that contain less
focusing on security, explainability, and traceability. The data on source and destination pods’ name and their port
approach consists of three main steps: abstracting tree numbers. They collected logs related to the system using
structures, exploring using generic detectors, and scanning eBPF and LSM from various Levels from 3-7 and found
|     |     |     |     |     |     |     |     | policies. | Except | for the | log collector, |     | which | operated with |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------- | -------------- | --- | ----- | ------------- |
tocreatealinearviewthatoutlinesthesystem’sarchitecture.
ThestudytestedthismethodonthePiggymetricsapplication, the microservice containers on different machines, every
showing that it could accurately identify the architecture component of the proposed system was configured on the
maincomputer.Throughoutthetests,theylookedforpolicies
| components | and | security | annotations |     | found | in  | manual |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
analyses. This demonstrates the method’s precision and every10secondsandmonitoredtheCPUandmemoryusage
ability to link findings to specific code locations. However, everyfiveminutes.
| the study                                                | also revealed |     | some | challenges | in  | detecting | all |         |     |     |     |     |     |     |
| -------------------------------------------------------- | ------------- | --- | ---- | ---------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| securityfeaturesduetotheirscatterednatureacrossdifferent |               |     |      |            |     |           |     | 9) CdOF |     |     |     |     |     |     |
codesections,pointingoutopportunitiesforfurtherrefining Ranjithaetal.,[73]proposedaframeworkfortheobservabil-
thedetectorsandenhancingtheoverallapproach. ity of the microservices at the network and host domain for
betterperformanceevaluationandanalysisoftheactualcause
5) SuanMing of the microservices failure. Multiple domain observability
Grohmann, et al., [69] proposed a framework to predict providesthefinegrainend-to-endfromthesendertothehost
the root cause analyses of the microservices performance observability of the system. The observability framework is
| 72022 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
based on eBPF while imposing less overheads of 2.6% of approximately2.5%ofthetotalCPUandmemoryavailable
CPU usage. This system correlates the internal application onthehardware.Despitethislowoverhead,itdemonstrates
traffic(withinpodspaces)withthebroaderexternalnetwork rapid troubleshooting and resolution of diverse operational
activities (across the physical network IP space) for the issues arising from varied observability data. The frame-
precise identification and diagnosis of the sources and work is mostly based on existing open-access tools like
reasonsfornetworkperformanceissues. Prometheus,Grafana,Telegraf,andothers.
10) AdOB 13) OESS
Monteiro et al., [74] proposed an observability approach Alanezi and Mishra [77] design, implement, and evaluate
basedongametheoryastatisticalapproachforforensic-ready the performance of a microservices-oriented architecture
microservices systems to investigate efficiently in case of for an edge server. It further illustrates its practicality
anysecuritybreachandperformancefailures.Theresearcher by building comprehensive IoT applications from start to
collects logs, traces, and metrics while considering the finish. According to the research, monitoring is a crucial
user (malicious or legitimate) and microservices as game component of the microservices architecture. The system
players, and collects the data in case of unusual activities includes a Microservices Registry that tracks the status of
done by the malicious user as defined in the game theory eachmicroservices,determiningwhichareactiveandwhich
strategies and maintains the related log. The findings show are not. This information is sent to the Orchestrator, which
that adaptive observability outperforms observability by a uses it to create launch configurations for new services
significantmargin,itimprovesdetectionratesby26.97%to or applications. The Orchestrator’s configurations are then
42.50%insamplingobservabilityandby3.1%to38.96%in sent to the Main Controller, which launches the appropriate
fullobservability. ApplicationControllerforthenewapplicationandprovides
the client with the necessary port number. This architecture
11) eBPFM heavily utilizes Docker for containerization, enabling the
Wustrich et al. [75] proposed an eBPF-based matcher virtualization of each microservices and allowing for com-
that monitors and logs the communication patterns of prehensiveperformanceevaluation,includingthemonitoring
applications, linking network traffic with their respective ofinter-microservicescommunication.
applications. eBPF matcher collects the data related to the
ingress and egress packets containing packet information, 14) MSM
associated process ID, and thread group and matches them Zdun et al. [78] addressed the challenges of microservices
withtheirspecificapplicationtoidentifyamaliciousnetwork architecture for security, considering the size, complexity,
flow. For this purpose, the researchers deployed a botnet to and continuous evolution of these systems. This method
performanintrusion,andtheproposedtoolmaintainedlogs employed three commonly used security strategies: secure
and successfully identified the botnet’s abnormal activity. communication, identity management, and observability.
Moreover, the researchers gathered relevant data while They emphasized the importance of three key observability
minimizingdataredundancy,whichsignificantlyreducedthe techniquesinmicroservicesarchitecture:Logging,monitor-
overheadoftheeBPF-basedmatcher. ing, and tracing. Logging records system events to identify
defectsandconductauditsforeachmicroservice.Monitoring
12) DESK involves the use of metrics to assess the service request
Usman et al., [76] proposed an observability framework management to provide a holistic view of the system’s
namedmicroservices-basedDESKforfine-grainanalysisat overall performance. Tracing or distributed tracing to track
the services level of the microservices-based containerized individual transactions through the various services in the
environment. The proposed framework is designed to effi- system, focusing on performance and cross-service opti-
ciently manage and control Kubernetes-orchestrated edge mizations.Theresearcherdevelopedaninnovativeapproach
clusters. It comprises six stages including Measurement, to evaluate compliance with architectural design decisions
Fusion, Storage, Visualization and Notification, and Pro- (ADDs)inmicroservicessecurityusingspecializedmetrics.
visioning and Orchestration (P&O), as a separate loosely Inthismethod,theyutilizedregressionanalysis,atechnique
coupled component. Granulated metrics, logs, and traces that effectively and accurately correlates the dependent and
are collected from various points using lightweight agents independentvariables.
like Telegraf, Promtail, and Jaeger in the measurement
stage. Prometheus, Loki, and Elasticsearch are utilized for 15) KAIJU
real-time observability, data access, and analysis. Grafana TheKaijuProject[79]introducedanevent-drivenapproach
is employed for data visualization and Prometheus for forenhancingobservabilityincomplexmicroservicesarchi-
open-access anomaly detection and threshold-based alerts tectures,focusingonintegratingmonitoringofmetrics,logs,
management.ProvisioningandOrchestration(P&O)isdone and traces. By treating these data sources as events, the
byHelmandKubectltoolsforedgescalabilityandoperations projectaimstoovercomethelimitationsoftraditionalmon-
management. Based on the results, the DESK utilizes itoring methods in dynamic environments. This integration
VOLUME13,2025 72023

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
allows for near real-time analysis of system behavior, identifying weaknesses in resilience mechanisms related to
| enabling            | faster and | more      | effective   | responses |              | to operational |         | systemcalls. |     |     |     |     |     |     |     |
| ------------------- | ---------- | --------- | ----------- | --------- | ------------ | -------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| issues. Implemented |            |           | and tested  | in        | a real-world |                | setting |              |     |     |     |     |     |     |     |
| with a software     |            | company’s | deployment, |           | the          | Kaiju          | system  | 19) eBPFNM   |     |     |     |     |     |     |     |
Thepaper[83]developedanevent-drivennetworkmonitor-
demonstratesitsabilitytoprovidedetailed,real-timeinsights
into system performance and health efficiently, without ingplatformusinganextendedBerkeleyPacketFilter(eBPF)
demanding excessive resources. The results underline the to improve microservices observability. It addressed key
effectiveness of the Kaiju system as a potent tool for challengessuchasacquiringcustomizedmonitoringmetrics,
observabilityinmoderndistributedsystems. dynamic load balancing, optimizing resource utilization,
|     |     |     |     |     |     |     |     | and implementing |     | rate | limiting | to  | handle | traffic | surges. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- | -------- | --- | ------ | ------- | ------- |
16) STEAM The system leveraged eBPF for real-time, low-overhead
Heetal.,[80]proposedaframeworkSTEAM,approachthat monitoring of network and system performance, providing
focusesonenhancingobservabilityindistributedsystemsby detailed insights into microservices interactions. Addition-
addressing the limitations of traditional uniform sampling ally, it incorporated load-balancing strategies to optimize
|          |           |     |             |     |         |         |       | service | performance | and | resource | management |     | techniques |     |
| -------- | --------- | --- | ----------- | --- | ------- | ------- | ----- | ------- | ----------- | --- | -------- | ---------- | --- | ---------- | --- |
| methods. | The STEAM |     | methodology |     | employs | a novel | trace |         |             |     |          |            |     |            |     |
sampling strategy that preserves a wide range of trace to enhance CPU and memory efficiency. By integrating the
types and maximizes the diversity of the sampled data. platform with Kubernetes, scalability, and reliability were
This is achieved by using a Graph Neural Network (GNN) ensured,makingitwell-suitedforcloud-basedmicroservices
fortracerepresentation,whichincorporatesdomain-specific environments.
| knowledge | to better     | capture |       | the nuances | of  | trace | data, and |             |     |     |     |     |     |     |     |
| --------- | ------------- | ------- | ----- | ----------- | --- | ----- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| employing | Determinantal |         | Point | Processes   |     | (DPP) | to focus  | 20) DyCause |     |     |     |     |     |     |     |
on sampling mutually dissimilar traces. These techniques Pan et al., [84] developed DyCause, a diagnostic tool for
|     |     |     |     |     |     |     |     | microservices | systems |     | that operate | from | user | space | and use |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | ------------ | ---- | ---- | ----- | ------- |
togetherensurethattheobservabilityofthesystemismain-
tained, enabling better system diagnostics and performance crowd crowd-sourcing to collect diagnostic data, avoiding
optimization. the need for kernel-side access. Unlike traditional methods
thatdependonkernelmonitoring,DyCauseuseslightweight
17) AAD API log sharing and a statistical algorithm to uncover
|         |           |         |     |           |               |     |     | time-varying | causal | relationships |     |     | between | services. | This |
| ------- | --------- | ------- | --- | --------- | ------------- | --- | --- | ------------ | ------ | ------------- | --- | --- | ------- | --------- | ---- |
| Mart et | al., [81] | focused | on  | enhancing | observability |     | and |              |        |               |     |     |         |           |      |
anomalydetectionwithinKubernetesclusters.Theproposed approach constructs a dynamic map of service interactions,
methodologyinvolvesusingPrometheusmetricsforcontin- necessaryfortracingfailurepropagation.Testedinsimulated
uousmonitoringandapplyingforecastingtechniquestopre- and real-world cloud environments, DyCause outperformed
dictpotentialanomalies.Byforecastingmetrics,thesystem conventional kernel-based methods in accuracy, efficiency,
|     |     |     |     |     |     |     |     | and data | sensitivity, | proving |     | effective | in  | identifying | root |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ------- | --- | --------- | --- | ----------- | ---- |
canproactivelyalertuserstoanomalies,allowingforquicker
responsetimesandpotentiallyavoidingsystemdefects.The causes of failure with minimal data. This makes DyCause
resultsdemonstratethatthismethodcaneffectivelyenhance aviablesolutionformanagingcomplex,dynamicmicroser-
vicesarchitectures.
theobservabilityoftheKubernetesclusters,providingamore
automatedandpredictivemonitoringsolution.
|     |     |     |     |     |     |     |     | 21) ADMBA |         |                   |     |     |                   |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----------------- | --- | --- | ----------------- | --- | ---- |
|     |     |     |     |     |     |     |     | Vaughan   | et al., | [85] investigated |     | the | high availability |     | (HA) |
18) CHAOSORCA
Simonsson et al., [82] presented CHAOSORCA, a novel ofKubernetesinaprivatecloudsettingbytestingitsdefault
|                 |     |        |          |     |        |     |            | configurations |     | against | various | failure | scenarios. | The | exper- |
| --------------- | --- | ------ | -------- | --- | ------ | --- | ---------- | -------------- | --- | ------- | ------- | ------- | ---------- | --- | ------ |
| fault injection |     | system | designed | to  | assess | the | resilience |                |     |         |         |         |            |     |        |
of containerized applications against system call errors iments, which utilized VLC video streaming microservices,
without requiring modifications to the application within weredesignedtomonitorKubernetes’responsetobothpod
|              |                |     |     |            |     |                |     | and node | failures, | assessing |     | key metrics | such | as  | reaction, |
| ------------ | -------------- | --- | --- | ---------- | --- | -------------- | --- | -------- | --------- | --------- | --- | ----------- | ---- | --- | --------- |
| Docker-based | microservices. |     |     | The system |     | is implemented |     |          |           |           |     |             |      |     |           |
in real conditions without altering the application, using a repair, recovery, and outage times. The results indicated
|             |     |            |     |           |        |         |        | that while | Kubernetes |     | efficiently | handles | internal-triggered |     |     |
| ----------- | --- | ---------- | --- | --------- | ------ | ------- | ------ | ---------- | ---------- | --- | ----------- | ------- | ------------------ | --- | --- |
| combination | of  | monitoring |     | different | levels | of call | to the |            |            |     |             |         |                    |     |     |
systemandimplementingperturbations.Themethodologyof failures through administrative commands, it struggles with
CHAOSORCA includes three main components: a monitor, extended downtime when dealing with external failure
|     |     |     |     |     |     |     |     | triggers, | revealing | a gap | in  | achieving | HA  | under | default |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----- | --- | --------- | --- | ----- | ------- |
aperturbator,andanorchestrator.Themonitortrackssystem
metricsandsystemcalls,theperturbatorintroducesspecific settings.Thestudyunderscoresthenecessityforoptimizing
|             |      |            |        |     |                  |     |      | Kubernetes | configurations |     | to  | enhance | responsiveness |     | and |
| ----------- | ---- | ---------- | ------ | --- | ---------------- | --- | ---- | ---------- | -------------- | --- | --- | ------- | -------------- | --- | --- |
| disruptions | into | the system | calls, | and | the orchestrator |     | man- |            |                |     |     |         |                |     |     |
ages the experiments, recording the impact of perturbations reliabilityinreal-worldoperationalscenarios.
| on system  | behavior.     | CHAOSORCA |        | was      | evaluated |     | on three  |             |     |     |     |     |     |     |     |
| ---------- | ------------- | --------- | ------ | -------- | --------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| real-world | applications: |           | a file | transfer | client,   |     | a reverse | 22) eBPFOaS |     |     |     |     |     |     |     |
proxy server, and a microservice-oriented web application. Liuetal.[86]proposedaprotocol-independentnon-intrusive
The results demonstrate CHAOSORCA’s effectiveness in method to analyze network observability in container
| 72024 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
networksusingeBPFtechnologywithinKubernetesclusters. stringent performance and reliability standards. Utilizing
Themethodologyconsistsofthreemaincomponents:trans- diverse eBPF maps, the agent efficiently collects and
parentdatacollectionwithoutrequiringcodemodifications, processesnetworktrafficdata,showingmarkedperformance
data aggregation into meaningful metrics, and intelligent improvements compared to existing solutions through
analysis using machine learning to detect anomalies and detailed benchmarks. Now available as an open-source,
diagnosenetworkperformanceissues.Theevaluationresults netobserv-ebpf-agenthasbeensuccessfullyincorporatedinto
demonstrate minimal impact on system performance, with the Red Hat OpenShift Container Platform, illustrating its
less than a 1.2% increase in latency and under 1% impact practical benefits and effectiveness in improving network
onthroughput,whileeffectivelydetectingnetworkanomalies observabilityforcloudapplications.
| and finding    | specific | instances | of     | network      | problems, | such   |     |     |     |     |     |     |     |     |
| -------------- | -------- | --------- | ------ | ------------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| as significant | delays   | and       | packet | losses. This | system    | allows |     |     |     |     |     |     |     |     |
26) ADAM
| for real-time | monitoring |     | and problem-solving |     |     | in complex |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Theresearcherintroducedanoveltechnique[90]fordetect-
| containerized | environments, |     | highlighting |     | its efficiency | and |               |     |                 |     |               |     |               |     |
| ------------- | ------------- | --- | ------------ | --- | -------------- | --- | ------------- | --- | --------------- | --- | ------------- | --- | ------------- | --- |
|               |               |     |              |     |                |     | ing anomalies |     | in microservice |     | architectures |     | by monitoring |     |
minimaloperationalintrusion.
|     |     |     |     |     |     |     | distributed   | traces | and        | profiling | metrics.     | The      | authors | devel-  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---------- | --------- | ------------ | -------- | ------- | ------- |
|     |     |     |     |     |     |     | oped a model, |        | structured | as        | an annotated | directed |         | acyclic |
23) ENMA
|               |           |            |                |          |          |          | graph (DAG),  |              | which | utilized | six essential | profiling          |     | metrics |
| ------------- | --------- | ---------- | -------------- | -------- | -------- | -------- | ------------- | ------------ | ----- | -------- | ------------- | ------------------ | --- | ------- |
| This research |           | study [87] | introduces     | an       | advanced | network  |               |              |       |          |               |                    |     |         |
|               |           |            |                |          |          |          | to thoroughly | characterize |       | standard |               | system operations. |     | This    |
| monitoring    | framework |            | that leverages | Extended |          | Berkeley |               |              |       |          |               |                    |     |         |
modeleffectivelycapturedbothlinearandnon-linearmetric
| Packet Filter | (eBPF) | and | Express | Data Path | (XDP) | to opti- |                |     |           |     |         |           |            |     |
| ------------- | ------ | --- | ------- | --------- | ----- | -------- | -------------- | --- | --------- | --- | ------- | --------- | ---------- | --- |
|               |        |     |         |           |       |          | relationships, |     | enhancing | its | ability | to detect | anomalies. |     |
mizenetworkanalyticsefficiency.Thisframeworkutilizesa
|     |     |     |     |     |     |     | The effectiveness |     | of  | the | method | was validated |     | on two |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ------ | ------------- | --- | ------ |
sharedmonitoringprimitive,whichcanbepartiallyoffloaded
|                |     |              |           |     |            |         | open-source        | benchmarks, |      | achieving |           | an F1 | score      | of up to |
| -------------- | --- | ------------ | --------- | --- | ---------- | ------- | ------------------ | ----------- | ---- | --------- | --------- | ----- | ---------- | -------- |
| to a SmartNIC, |     | to calculate | essential |     | high-level | traffic |                    |             |      |           |           |       |            |          |
|                |     |              |           |     |            |         | 86%. Additionally, |             | this | approach  | supported |       | developers | in       |
metrics.Thesemetricsareusedtoselectivelytriggerdetailed
conductingrootcauseanalysisbycomparingtheanomalous
| analyses | when | necessary, | effectively | minimizing |     | redundant |     |     |     |     |     |     |     |     |
| -------- | ---- | ---------- | ----------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
behaviorwiththebaselinebehaviorestablishedbythemodel.
| processing. | Tested  | on a               | Netronome, | NFP,          | SmartNIC, | and     |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------------------ | ---------- | ------------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the Linux   | kernel, | the implementation |            | significantly |           | reduces |     |     |     |     |     |     |     |     |
resource utilization by dynamically managing application 27) OTHERSOBSERVABILITYSOLUTIONS
executions based on the current network conditions, greatly We explore additional observability solutions of a
enhancing the scalability and effectiveness of network microservices-based containerized platform that performed
monitoringoperations. therootcauseanalysisincaseofservicefailureandvarious
|     |     |     |     |     |     |     | performance | parameters. |     | However, |     | they did | not align | with |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | -------- | --- | -------- | --------- | ---- |
24) eBPFTT the holistic approach of our taxonomy. They either propose
The paper [88] explores the application of the extended frameworks or methodologies that are still experimental or
Berkeley Packet Filter (eBPF) for non-intrusive monitoring lackcomprehensivequantitativeevaluations.
of containerized user-space applications in production envi- Shiraishietal.[91]proposedtheextendedBerkeleyPacket
ronments, especially using Linux subsystems. The research Filter(eBPF)technologyforreal-timemonitoring,asasensor
centers on monitoring Interledger connectors through two for capturing container network metrics. The adoption of
comprehensive implementations of the Interledger proto- microservicesarchitecturehasbecomeincreasinglyprevalent
col. Using eBPF, the authors track and analyze critical withinlarge-scalewebservices,drivenbytheneedformore
performance metrics like CPU utilization, memory, and flexibleandscalabledevelopmentanddeploymentsolutions.
network traffic without disrupting the running applications. This shift towards microservices is often accompanied by
The findings highlight eBPF’s utility in providing in-depth the adoption of container technologies such as Docker,
systeminsights,vitalforidentifyingperformancebottlenecks which provides lightweight and portable environments for
and enhancing application efficiency in a non-disruptive runningmicroservices.Whilemicroservicesoffernumerous
manner. This paper emphasizes the value of eBPF in benefits, they also introduce challenges in monitoring and
improving system observability, specifically beneficial in managing the underlying infrastructure to ensure service
scenarios where conventional monitoring tools fall short or qualityandreliability.Effectivemonitoringofmicroservices
areintrusive. requires not only tracking the performance and behavior of
individualservicesbutalsomonitoringtheinfrastructureon
25) NETOBSERV which these services run. This includes containers, virtual
The paper [89] presents the netobserv-ebpf-agent, an opti- machines, and physical machines. Without comprehensive
mizednetworkobservabilityagentformonitoringcloud-based visibility into the infrastructure, it becomes difficult to
microservices using eBPF technology. This tool operates identify and troubleshoot issues that may impact service
smoothly across various hosting environments and is inde- quality. Therefore, there is a growing need for monitoring
pendent of underlying network configurations, significantly solutionsthatprovideinsightsintoboththeservicesandthe
reducing both CPU and memory usage while meeting supportinginfrastructure.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 72025 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
ViperProbe[92]isaneBPF-basedmicroservicescollection for microservices architectures, addressing the challenge of
framework offering two key features: dynamic sampling correlatinglogsacrossdifferentlayers.Byleveragingacom-
andcollectionofdiversesystemmetrics.Dynamicsampling monrequestidentifierandamodularobservabilityplatform,
allows for adaptability in monitoring, while diverse system theproposedsolutionaimstoenableprecisefaultlocalization
metricsensureacomprehensiveviewofmicroservicehealth and detection of issues, ultimately enhancing the reliability
and performance. ViperProbe leverages eBPF (extended andperformanceofmicroservices-basedapplications.Multi-
BerkeleyPacketFilter)technologytocollectmetrics.Ittakes LayerObservabilityforFaultLocalization,theresearch[94]
advantageofcommondesignpatterns,suchasservicemesh, outlines the shift from standalone service-oriented archi-
for offline analysis to optimize the set of collected metrics tecture (SOA) to microservices architecture, driven by the
beforedeploymentinproductionenvironments.Further,itis needforhandlinglargercustomerbasesandmakingsystems
thefirstscalableeBPF-baseddynamicandadaptivemicroser- more responsive to changes. Microservices architecture
vices metrics collection framework. It suggests that Viper- involvesdevelopingandmaintainingeachfunctionalityasa
Probeofferslimitedoverheadwhilesignificantlyenhancing separateservice,offeringbenefitslikescalabilityandeaseof
traditionalmanagementtaskssuchashorizontalauto-scaling. deployment. The researchers aim to address the limitations
Theproposedsystemdemonstrateseffectivenessinaddress- of existing monitoring solutions, which often focus only
ing traditional management tasks, suggesting improved on the application layer. The proposed mechanism offers a
efficiency and effectiveness in monitoring microservices. comprehensiveviewofthemicroservicesarchitecture,facili-
However,specificquantitativeresultsregardingperformance tatingabetterunderstandingandmanagementofthesystem.
overheadorcomparativeanalysiswithexistingtoolsarenot Theresearchersuseddistributedtracingframeworkssuchas
providedinthisexcerpt.Theyaimtoalleviatethechallenges JaegerorZipkintoimplementdistributedtracing.Thesetools
of monitoring microservices by providing a dynamic and enablecapturingandcorrelatingtracesacrossmicroservices.
adaptive approach to metrics collection, leveraging eBPF Process mining techniques involve analyzing event logs to
technologyandofflineanalysisofcommondesignpatterns. discover process models and patterns, which can be visual-
It suggests potential benefits in terms of efficiency and ized for monitoring purposes. The results of this approach
effectivenessinmanagingmicroservicearchitectures. would include improved observability of the microservices
Multi-Layer Observability for Fault Localization, this architecture, better understanding of system behavior, and
research[93]isaproposedsolutiontoenhancemicroservices quicker detection of issues or bottlenecks. However, it’s
observabilitybyaddressingthechallengeofcorrelatinglogs importanttonotethatimplementingsuchamonitoringmech-
across various layers of the application stack. They suggest anism may introduce performance overhead, especially in
thatexistingmonitoringpracticesoftenconcentratesolelyon termsofincreasednetworktrafficfordistributedtracingand
generating logs, metrics, and traces at the application layer. computational resources for process mining. Furthermore,
However, for effective fault localization, it’s crucial to cor- the strategies are discussed in the paper for mitigating this
relate logs across non-application layers like load balancers overhead and optimizing the monitoring mechanism for
and databases. The researchers propose an observability productionenvironmentsinthefuture.AReal-time,Scalable
libraryandplatformaimedataddressingthischallenge.The Monitoring and Analytics, the research [95] highlights the
observabilitylibrarylikelyprovidestoolsandutilitiestotag complexity of monitoring distributed microservices-based
logs with a common request identifier, enabling correlation software applications, particularly in environments where
acrossdifferentlayers.Meanwhile,theobservabilityplatform large amounts of user and transaction data are generated at
serves as the central hub for collecting, analyzing, and a rapid pace. Real-time monitoring is crucial for gaining
visualizing these correlated logs. The proposed solution insightsintouserinteractionsandtransactionsandfacilitating
emphasizes the importance of tagging logs with a common decisions for stakeholders. The focus is on capturing data
request identifier to facilitate correlation across different effectively to learn application usage patterns and predict
layers of the microservices architecture. This allows for events such as error types using machine learning methods.
a holistic view of the entire request life-cycle, from the The researchers utilized various tools and techniques for
front-end load balancer to the back-end database. Further, monitoringmicroservicesandanalyzinguserinteractionand
the observability platform is designed in a modular and transaction data. They captured event data from execution
extensiblemanner,enablingittoaccommodatemultipletypes logsofsoftwareapplicationsrunningondistributedmicroser-
of errors and issues beyond the initial scope. This suggests vices. This could involve using logging frameworks such
that the platform is adaptable to evolving requirements and as Logback, Log4j, or Fluentd to collect logs from each
can scale with the growing complexity of microservices microservice. Machine learning methods were employed to
environments.Theproposedobservabilityplatformhasbeen predictusagepatternsandidentifyerrortypesinreal-timeto
testedonfiveopen-sourcebenchmarks.Theresultsindicate predicterrortypesbasedonhistoricaldata.Thesystemwas
thatthetoolcanreliablyandpreciselydetectelusiveissues, capable of monitoring user actions and transactions in real-
implying its effectiveness in real-world scenarios. Overall, time,enablingimmediateresponsetoeventsandissues.This
this paper proposes a comprehensive observability solution real-time monitoring capability is essential for maintaining
72026 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
system health and ensuring a positive user experience. The and infrastructure. Services level observability focuses on
researchers likely conducted performance tests to evaluate monitoring and analyzing the behavior and performance of
the system’s capacity to handle growing data volumes and individual services within the system. MDF [65], Metro-
maintainresponsiveness. funnel [66], SuanMing [69], ADMBA [85], Kaij [79], and
AdaptiveContainerizationforMicroservices,theresearch MSM [78] focus on observability at the services level.
[96]addresses microservices observability by focusing on These frameworks prioritize monitoring and analyzing the
resource allocation and performance monitoring within behavior and performance of individual services within
containerized microservice deployments. To achieve this, the system. They aim to provide detailed insights into
the researchers likely utilize a combination of tools and serviceinteractions,dependencies,andperformancemetrics
techniques for monitoring the behavior and performance to ensure the reliability and efficiency of service-based
of microservices. Techniques such as logging, tracing, architectures.Network-levelobservabilityinvolvesmonitor-
and monitoring are employed to gather data on resource ing and analyzing network traffic, communication patterns,
utilization,responsetimes,andoverallsystemperformance. and performance metrics to ensure the reliability, security,
Additionally,theframeworkmayincorporatebuilt-inobserv- and efficiency of network infrastructures. Frameworks like
abilityfeaturesprovidedbycontainerorchestrationplatforms CDOF[73],eBPFOAS[86],ENMA[87],andnetobserv[89]
like Kubernetes, enabling real-time monitoring and anal- arecenteredaroundobservabilityatthenetworklevel.These
ysis of microservice performance. Performance evaluation frameworks emphasize monitoring and analyzing network
metrics provide quantifiable evidence of the framework’s traffic, communication patterns, and performance metrics
impact on microservice deployments. Regarding perfor- to ensure the reliability, security, and efficiency of network
mance overhead, the research discusses the computational infrastructures. They aim to provide insights into network
overhead introduced by the resource allocation framework behavior,trafficpatterns,andpotentialbottlenecksorsecurity
and any trade-offs made to achieve cost optimization and threats.
service guarantees. Strategies for mitigating performance In the realm of edge computing, the observability of
overhead,suchasfine-tuningresourceallocationalgorithms systems is paramount for ensuring efficient operations
oroptimizingcontainerconfigurations,alsobediscussed. and troubleshooting potential issues. A comparative anal-
ysis of various proposed methods reveals the types of
data each framework observes for achieving observability.
B. COMPARATIVEANALYSISOFSTATE-OF-THE-ART Frameworks such as MDF [65], MOA [67], BBMA [70],
MICROSERVICESOBSERVABILITYSOLUTIONS Nezha [71], CDOF [73], ADOB [74], DESK, MSM [78],
Thissubsectionconductsacriticalanalysisofmicroservices Kaiju [79], AAD [81], CHAOSORCA [82], DyCause [84],
observability solutions, building on the thematic taxonomy eBPFOAS [86], and ADAM [90] prioritize the observation
outlinedinSectionIV.Table3presentsanoverviewofthis of logs for edge computing observability. Logs provide
comparisonandoffersastructuredviewofthecurrentstate- a detailed record of system events, errors, and activities,
of-the-artmicroservicesobservabilitysolutions. facilitating effective troubleshooting and analysis. Others
Observability is crucial for monitoring and analyzing the such as MDF [65], MOA [67], BBMA [70], Nezha [71],
behavior and performance of complex systems. It enables CDOF[73],ADOB[74],DESK[76],Kaiju[79],AAD[81],
engineers to understand, troubleshoot, and optimize system CHAOSORCA [82], DyCause [84], OAS, and ADAM [90]
operationseffectively.Thissectionincludesthecomparative are among the frameworks that collect metrics data for
analyses of the state-of-the-art microservices observability observability.Metricsofferinsightsintosystemperformance,
frameworks.Incomparingthevariousproposedmethodsfor resource utilization, and other key parameters, aiding in
observability, it’s evident that each framework has its focus performanceanalysisandoptimization.Whileseveralframe-
and priorities regarding different observability levels within works, including Metrofunnel [66], MOA [67], AET [68],
asystem:SystemLevel,ServicesLevel,andNetworkLevel. SuanMing [69], BBMA [70], Nezha [71], CDOF [73],
System-level observability is important because it provides ADOB [74], DESK [76], Kaiju [79], CHAOSORCA [82],
insights into the functioning of the system architecture DyCause[84],eBPFOAS[86],andeBPFTT[88],prioritize
and infrastructure, allowing engineers to identify potential tracing data for observability. Traces provide visibility into
issues, optimize resource allocation, and ensure system the flow of requests and transactions across distributed
reliability and performance. Methods such as MOA [67], systems, enabling the identification of performance bottle-
AET [68], BBMA [70], Nezha [71], KUNERVA [72], necks and latency issues. Some frameworks adopt a mixed
STEAM[80],AAD[81],CHAOSORCA[82],DyCause[84], approach to observability, encompassing a combination of
eBPFTT [88], and ADAM [90] prioritize observability at logs, metrics, and traces. Examples include MDF [65],
the system level. These frameworks emphasize monitoring MOA [67], BBMA [70], Nezha [71], CDOF [73], ADOB
and understanding the overall behavior and performance of [74],DESK[76],Kaiju[79],AAD[81],CHAOSORCA[82],
the system as a whole, including factors such as resource DyCause [84], OAS, and ADAM [90], which leverage
utilization,systemhealth,andstability.Theyaimtoprovide multiple data types to provide comprehensive insights
insights into the functioning of the system architecture into system behavior and performance. Frameworks like
VOLUME13,2025 72027

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
.skrowemarfytilibavresbosecivresorcimtra-eht-fo-etatsfonosirapmoC
.3ELBAT
72028 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
Metrofunnel[66],AET[68],SuanMing[69],STEAM[80], ADOB [74], eBPFM [75], DESK [76], OESS [77], MSM
ADMBA[85],ENMA[87],eBPFTT[88],andnetobserv[89] [78], Kaiju [79], STEAM [80], AAD [81], CHAOSORCA
havemorelimitedobservabilitycapabilities,focusingprimar- [82],eBPFNM[83],DyCause[84],eBPFOAS[86],eBPFTT
ily on tracing or lacking support for certain data types like [88], and netobserv [89], prioritize performance analysis
logsormetrics. as a key objective of monitoring. These frameworks aim
However, the choice of observability framework for edge to assess system performance metrics, identify bottlenecks,
computing depends on the specific data requirements and and optimize resource utilization for enhanced efficiency
objectivesofthesystemorapplicationbeingmonitored.Each and reliability. Several frameworks, including MDF [65],
framework offers distinct capabilities for observing logs, Metrofunnel [66], MOA [67], AET [68], SuanMing [69],
metrics,andtraces,allowingstakeholderstoselectthemost BBMA [70], KUNERVA [72], CDOF [73], ADOB [74],
suitableapproachbasedontheirneeds.Whenanalyzingthe eBPFM [75], DESK [76], OESS [77], MSM [78], Kaiju
implementation paradigms of various proposed frameworks [79],STEAM[80],AAD[81],CHAOSORCA[82],DyCause
foredgecomputing,it’sevidentthateachframeworkhasits [84], and eBPFOAS [86], prioritize RCA as part of their
approachandprioritiesregardingdeploymentacrossdifferent monitoring objectives. These frameworks aim to identify
environments:Cloud,Fog,andEdge.FrameworkslikeMDF the underlying causes of system issues or failures, enabling
[65], Metrofunnel [66], AET [68], SuanMing [69], BBMA timelyresolutionandpreventingrecurrence.Anomalydetec-
[70], Nezha [71], KUNERVA [72], CDOF [73], ADOB tion is emphasized by frameworks like MDF [65], AET
[74],eBPFM[75],MSM[78],STEAM[80],CHAOSORCA [68], BBMA [70], and Kaiju [79]. These frameworks aim
[82], eBPFNM [83], and ADAM [90] support deployment to detect abnormal behavior or deviations from expected
in cloud environments. These frameworks are designed to patternswithinthesystem,facilitatingearlyidentificationof
operate seamlessly within cloud infrastructures, leveraging potential issues or security threats. Monitoring application
the scalability and resources offered by cloud platforms. health is a focus for frameworks such as MDF [65], Metro-
Only a few frameworks, such as DESK [76], OESS [77], funnel[66],ADOB[74],DESK[76],OESS[77],Kaiju[79],
Kaiju[79],AAD[81],DyCause[84],andADMBA[85],are STEAM[80],AAD[81],CHAOSORCA[82],DyCause[84],
tailoredfordeploymentinfogenvironments.Fogcomputing eBPFOAS [86], and netobserv [89]. These frameworks
involvesextendingcloudcomputingcapabilitiestotheedge prioritize monitoring the health and status of applications
of the network, closer to where data is generated and deployedintheedgeenvironment,ensuringtheiravailability,
consumed. These frameworks are optimized for use in reliability, and performance. The choice of monitoring
fogenvironments,offeringefficientprocessingandanalysis frameworkdependsonthespecificmonitoringobjectivesand
of data at the edge. Some frameworks, including DESK requirementsoftheedgecomputingapplication.Whilesome
[76], OESS [77], Kaiju [79], AAD [81], DyCause [84], frameworks prioritize comprehensive performance analysis
ADMBA [85], eBPFOAS [86], ENMA [87], eBPFTT [88], and RCA, others focus on specific aspects such as anomaly
netobserv[89],andADAM[90],arespecificallydesignedfor detectionorapplicationhealthmonitoring.Eachframework
deploymentattheedge.Edgecomputinginvolvesprocessing offersuniquecapabilitiestailoredtoaddressdifferentaspects
data locally at the edge of the network, closer to the ofmonitoringinedgecomputingenvironments.
data source, to reduce latency and bandwidth usage. These When considering the deployment platforms supported
frameworks are tailored to address the unique challenges by various proposed frameworks for edge computing, it’s
and requirements of edge deployments, such as limited evident that each framework has distinct capabilities and
resources and intermittent connectivity. Overall, the choice compatibility with different platforms, primarily Docker
of a specific deployment paradigm depends on factors such Swarm and Kubernetes. Frameworks such as BBMA
as the intended use case, data processing requirements, [70], Nezha [71], DESK [76], Kaiju [79], AAD [81],
and the availability of resources. While cloud deployment CHAOSORCA [82], ADMBA [85], eBPFOAS [86], and
offersscalabilityandcentralizedmanagement,fog,andedge eBPFTT[88]supportdeploymentonDockerSwarm.Docker
deploymentsprovidelow-latencyprocessingandsupportfor Swarm is a container orchestration tool that allows for the
edgecomputingscenarios.Eachframeworkcaterstodifferent managementandscalingofcontainerizedapplicationsacross
deployment environments, allowing organizations to select aclusterofDockerhosts.Manyframeworks,includingMDF
the most suitable option based on their specific needs and [65], Metrofunnel [66], MOA [67], BBMA [70], Nezha
objectivesinedgecomputingapplications. [71],KUNERVA[72],CDOF[73],ADOB[74],DESK[76],
Whenexaminingthepurposeofmonitoringacrossvarious Kaiju [79], AAD [81], CHAOSORCA [82], ADMBA [85],
proposed frameworks for edge computing, it becomes clear eBPFOAS [86], and ADAM [90], support deployment
that each framework has distinct objectives and priorities on Kubernetes. Kubernetes is an open-source container
concerning different aspects of monitoring: performance orchestrationplatform forautomating thedeployment,scal-
analysis,rootcauseanalysis(RCA),anomalydetection,and ing, and management of containerized applications. Some
application health monitoring. Most frameworks, includ- frameworks have mixed or partial support for deployment
ing MDF [65], Metrofunnel [66], MOA [67], AET [68], platforms. For example, MDF [65], Metrofunnel [66], and
SuanMing[69],BBMA[70],KUNERVA[72],CDOF[73], MOA[67]supportKubernetesbutnotDockerSwarm.Onthe
VOLUME13,2025 72029

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
other hand, BBMA [70], Nezha [71], and KUNERVA [72] a high-level tracing language for Linux extended Berkeley
support both Docker Swarm and Kubernetes. Additionally, Packet Filter (eBPF) that allows for dynamic tracing of
some frameworks like OESS [77] support Docker Swarm kernelanduser-spaceapplications.Thechoiceofmonitoring
butnotKubernetes,whileSTEAM[80]supportsKubernetes tools integrated into each framework depends on factors
but not Docker Swarm. Limited or Unspecified Support: suchascompatibility,functionality,andspecificmonitoring
FrameworkssuchasAET[68],SuanMing[69],MSM[78], requirements. These tools collectively contribute to the
ENMA [87], netobserv [89], and eBPFTT [88] do not observabilityandperformancemonitoringcapabilitiesofthe
specify support for either Docker Swarm or Kubernetes, respective frameworks, aiding in troubleshooting, analysis,
indicating limited or unspecified compatibility with these andoptimizationofedgecomputingenvironments.
deploymentplatforms.Ultimately,thechoiceofdeployment
platform for a specific framework depends on factors such VI. EVALUATIONOFMICROSERVICESOBSERVABILITY
as compatibility, scalability requirements, and organiza- SOLUTIONS:TOOLS,FEATURES,ANDPERFORMANCE
tional preferences. While Kubernetes is widely supported METRICS
across many frameworks, Docker Swarm remains a viable Thissectionprovidesacomprehensiveevaluationofobserv-
option for those preferring simpler container orchestration ability frameworks for microservices architecture, based on
solutions.Each framework’scompatibility withdeployment the research and findings reported in the original research
platforms contributes to its versatility and suitability for papers discussed earlier. We analyze various features of
differentedgecomputingenvironmentsandusecases.Inthe these frameworks to gauge their effectiveness and effi-
realm of monitoring tools utilized by various proposed ciency in monitoring microservices within containerized
frameworks for edge computing, each framework exhibits environments, as outlined in table 4. Additionally, a com-
unique preferences and configurations regarding the tools parativeanalysisofstate-of-the-artobservabilityframeworks
integrated into its monitoring infrastructure. Frameworks highlights a diverse array of tools and technologies, each
like MDF [65], MOA [67], BBMA [70], Nezha [71], tailoredtospecificaspectssuchasperformancemonitoring,
KUNERVA [72], Kaiju [79], CHAOSORCA [82], and root cause analysis, anomaly detection, and alerting. The
ADMBA [85] incorporate Prometheus for monitoring. analysis reveals that Root Cause Analysis (34.2%) and
Prometheus is an open-source monitoring and alerting PerformanceAnalysis(30.1%)aretheprimaryfocusareasof
toolkit widely used for collecting and querying time-series observability frameworks, as depicted in the distribution of
data. Only BBMA [70] incorporates Datadog among the observability purposes across frameworks fig 4. Moreover,
listed frameworks. Datadog is a cloud-based monitoring the feature comparison across reviewed frameworks fig 5
and analytics platform that integrates with various cloud demonstrates varying emphases on critical aspects like
providers and technologies. MDF [65], MOA [67], BBMA Metrics,Logs,Tracing,PerformanceImpact,andScalability,
[70], KUNERVA [72], DESK [76], Kaiju [79], AAD [81], providinginsightintothedistinctdesignprioritiesofdifferent
CHAOSORCA [82], and ADMBA [85] utilize Grafana frameworks. Lastly, the frameworks vs resource utilization
for visualization and analytics of monitoring data. Grafana fig6highlightsdisparitiesinCPUusageandlatencyamong
is an open-source platform for creating, exploring, and frameworks,underscoringtheimportanceofefficiencywhen
sharing dashboards and visualizations of time-series data. selectingtoolsformonitoringmicroservices.
Metrofunnel [66], MOA [67], and Kaiju [79] utilize Zipkin The MDF [65] method focused on performance analysis,
fordistributedtracing.Zipkinisadistributedtracingsystem rootcauseanalysis,anomalydetection,andapplicationhealth
usedformonitoringandtroubleshootingmicroservices-based by leveraging Prometheus and Grafana for monitoring and
architectures. BBMA [70] incorporates WeaveScope for visualization. It evaluated a comprehensive set of data,
monitoring. WeaveScope is a visualization and monitoring including logs, metrics, and traces, although it did not
tool for Docker and Kubernetes clusters, providing insights addressresourceutilizationdirectly.ItusedStochasticPetri
intocontainerizedapplicationsandinfrastructure.DESK[76] Net (SPN) models to analyze the data. In contrast, the
utilizes Loki for log aggregation and analysis. Loki is a Metrofunnel[66]methodtargetedperformanceanalysis,root
horizontally scalable, multi-tenant log aggregation system cause analysis, and application health through Zipkin and
inspired by Prometheus. STEAM [80] incorporates Open- Sysdig. It primarily evaluated trace data, without focusing
Telemetryforobservabilityinstrumentation.OpenTelemetry on resource utilization. Metrofunnel [66] employed passive
is a set of APIs, libraries, agents, and instrumentation tracingtounobtrusivelycapturesystemactivityandcontainer
to provide observability data for cloud-native software. monitoring to assess the performance and health of con-
ADAM [90] utilizes Istio for monitoring and managing tainerizedapplications,offeringaviewintotheoperationof
microservices.Istioisanopen-sourceservicemeshplatform containerenvironments.TheMOA[67]methodwasdesigned
that provides traffic management, policy enforcement, and forperformanceanalysis,rootcauseanalysis,andapplication
telemetry collection capabilities. ADAM [90] and netob- health by utilizing OpenTelemetry for collecting metrics,
serv [89] integrate Jaeger for distributed tracing. Jaeger is logs, and tracing data. It specifically included CPU usage
a distributed tracing system used for monitoring and trou- metrics and benefited from the integration of open-source
bleshooting microservices-based architectures. BPFTrace is monitoringframeworks,whichallowedforacomprehensive
72030 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
.scirtemecnamrofrepriehtdnaskrowemarfytilibavresbosecivresorcimfonosirapmocdesab-erutaeF
.4ELBAT
VOLUME13,2025 72031

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
viewofsystemperformance.Ontheotherhand,theAET[68]
methodaddressedperformanceanalysis,rootcauseanalysis,
anomaly detection, and application health through the
analysisoftracedata.Itdidnotfocusonresourceutilization
and relied on a Tree Abstraction approach, which involved
organizingandrepresentingthedatainatree-likestructureto
simplifytheanalysisofcomplexsystembehaviorsandinter-
actions.TheSuanMing[69]methodfocusedonperformance
analysis and root cause analysis using Jaeger and Zipkin
for tracing. It did not address resource utilization directly
and employed a machine-learning approach to analyze the
collected traces. This technique used algorithms to detect
patterns and anomalies in trace data, potentially improving
the accuracy of identifying and resolving issues within
the system. The BBMA [70] method covered performance
FIGURE4. Distributionofmonitoringpurposeoftheframeworks.
analysis, root cause analysis, and application health by
integrating multiple tools: Prometheus and Grafana for
metrics and logs, Datalog for advanced data queries, and allowing programs to be run in the kernel space. This
WeaveScope for visualizing and monitoring containerized approachenableddetailedmonitoringandtracingofsystem
applications. It utilized eBPF (extended Berkeley Packet activities at a granular level, enhancing the ability to detect
Filter)technology,whichprovidedapowerfulmechanismfor and analyze anomalies efficiently. The ADOB [74] method
tracingandmonitoringatalowlevelwithinthekernel.eBPF focused on performance analysis, root cause analysis, and
allowedforhigh-performance,fine-grainedobservabilityby applicationhealth(AH)usingmetrics,logs,andtracingdata.
executing small programs in response to various kernel It was noted for its ability to improve performance insights
events. This technology enhanced the ability to capture andissueresolution.ADOB[74]utilizedgametheory,which
detailed performance data and system behavior, offering involved applying mathematical models of strategic inter-
deep insights into application performance and resource actions to optimize decision-making performances. In the
utilization. The Nezha [71] method was designed for root contextofobservability,gametheorywasusedtomodeland
causeanalysis (RCA)and utilizeda suiteof toolsincluding predict system behavior, allocate resources effectively, and
OpenTelemetry, Prometheus, Grafana, and Loki. It focused make informed decisions based on the strategic interactions
on logs and traces but did not directly address resource betweendifferentsystemcomponents.Thisapproachhelped
utilization. Nezha [71] leveraged the OpenTelemetry SDK in understanding complex system dynamics and improving
and toolkit, which provided a comprehensive framework overall system health and performance. The eBPFM [75]
for collecting and exporting telemetry data. This toolkit method targeted performance analysis (PA), root cause
supported a wide range of observability data, enabling analysis(RCA),andanomalydetection(AD).Itutilizedlogs
detailedanalysisandeffectivetroubleshootingofissuesbased andwasnotedforitsresourceutilizationof1.4%whenper-
on logs and traces. The KUNERVA [72] and CDoF [73] forming 10,000 packets per second. eBPFM [75] employed
methodsaddressedperformanceanalysis,rootcauseanalysis, eBPF (extended Berkeley Packet Filter) technology, which
and anomaly detection. They employed Prometheus and allowed for high-performance, low-overhead monitoring by
Grafanatomonitorandvisualizelogs.KUNERVA[72]was executingsmallprogramsinthekernel.Thisenableddetailed
notable for its focus on resource utilization, with specific andefficientanalysisofnetworktrafficandsystembehavior,
metrics indicating 4.53% CPU usage and a 2.58% baseline enhancingthedetectionandinvestigationofanomalies.
for performance evaluation. The system was built using the The DESK [76] method addressed performance analy-
Go programming language and integrated with Hubble for sis, root cause analysis, and anomaly detection using a
network visibility, MySQL for database management, and suite of tools including Prometheus, Grafana, Loki, and
MongoDB for NoSQL data storage. This combination of OpenTelemetry. It evaluated metrics, logs, and tracing
technologiesallowedKUNERVA[72]toefficientlyperform data, and was capable of monitoring performance with
andanalyzelogs,offeringinsightsintosystemperformance specific timing metrics: 90 milliseconds for 50 pods and
and detecting anomalies based on comprehensive data 130 milliseconds for 110 pods. These timings reflected
collectionandanalysis. the system’s responsiveness and efficiency in performing
The CDoF [73] method is aimed at performance analysis observability data across different scales of deployment.
(PA), root cause analysis (RCA), and anomaly detection The integration of these tools allowed DESK [76] to
(AD). It used metrics, logs, and tracing to gather data, with provide comprehensive observability by aggregating data
a reported resource utilization of 2.69%. CDoF employed from various sources, enabling effective analysis and quick
eBPF (extended Berkeley Packet Filter) technology, which detection of issues in containerized environments. The
provided high-performance, low-overhead observability by OESS [77] method focused on performance analysis (PA),
72032 VOLUME13,2025

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
rootcauseanalysis(RCA),andapplicationhealth(AH)using
metrics. It was designed to maintain stable CPU utilization,
indicating that it effectively managed system resources
while monitoring performance. OESS [77] operated with
SpringBootforapplicationdevelopmentandDockerEngine
for containerization, allowing for effective deployment and
monitoring of applications in a containerized environment.
The MSM [78] method was aimed at performance analysis
(PA), root cause analysis (RCA), and anomaly detection
(AD). It relied on logs and traces for data collection and
did not directly specify resource utilization. MSM [78]
employed statistical methods to analyze the collected data.
These methods involved applying statistical techniques to FIGURE5. Frameworks’featurecomparison.
identify patterns, trends, and anomalies in the logs and
traces.Byusingstatisticalmodelsandalgorithms,MSM[78]
could detect deviations from normal behavior, quantify the
likelihood of certain issues, and provide insights into the
system’sperformanceandpotentialproblems.Thisapproach
enhanced the ability to predict and diagnose issues based
on historical data and statistical analysis. The Kaiju [79]
method targeted performance analysis (PA), root cause
analysis (RCA), anomaly detection (AD), and application
health (AH). It utilized OpenTelemetry, Jaeger, and Zipkin
forcollectingmetrics,logs,andtracingdata.Kaiju[79]was
designed to enhance observability by leveraging these tools
to gather comprehensive performance data. It focused on
increasing visibility into system operations and employed FIGURE6. Resourceutilizationamongtheframeworks.
the EPL (Event Performing Language) for querying and
analyzing the collected data. EPL enabled complex event andscalableacrossdifferentdeployments.Thiscombination
performingbyallowinguserstodefineandexecutequerieson facilitatedeffectivemonitoringandobservability.
eventstreams,providingadvancedcapabilitiesfordetecting The scatter plot fig 7 provides a comparative analysis
andrespondingtoeventsinrealtime. of the observability tools employed in research studies
TheSTEAM[80]methodaddressedperformanceanalysis focused on microservices. The most frequently utilized tool
(PA), root cause analysis (RCA), and application health iseBPF,mentionedinresearchpapersdiscussedinsectionV,
(AH)usingOpenTelemetryfortracingdatacollection.Itdid highlightingitsgrowingpopularityforefficient,kernel-level
not directly focus on resource utilization and relied on monitoring with minimal overhead. This reflects a trend
Graph Neural Networks (GNNs) for analysis. GNNs were towards leveraging low-level system capabilities for deeper
a type of machine learning model designed to work with insightsintoperformanceanddiagnostics.Thesetoolshave
graph-structured data. They were particularly effective in become essential components in monitoring frameworks,
capturing complex relationships and dependencies within offeringcomprehensivevisibilityintospecificallymicroser-
the data. In the context of STEAM [80], GNNs analyzed viceenvironments.
the tracing data to identify patterns and anomalies, model Tracing solutions are also well-represented, with Open-
dependencies between different system components, and Telemetryappearingin5studies,andJaegerandZipkineach
provide insights into the system’s behavior. This approach referenced in 4 papers. This suggests a strong emphasis on
enhanced the ability to detect issues and understand system distributed tracing to capture the flow of requests across
dynamics by leveraging the power of graph-based models microservices, which is critical for identifying performance
to analyze and interpret observability data. The AAD [81] bottlenecks and diagnosing complex issues. The increasing
method focused on performance analysis (PA), root cause useofOpenTelemetryindicatesashifttowardsstandardiza-
analysis (RCA), and anomaly detection (AD). It collected tionandintegrationofmetrics,logs,andtraceswithinasingle
a variety of observability data, including metrics, logs, and observabilityframework.
tracing information, though it did not specify its impact on Specialized tools like BPFTrace, mentioned in 3 papers,
resourceutilization.ThemethodutilizedPythonandDocker showcase the demand for dynamic tracing techniques
foritsoperationswithinKubernetesclusters,leveragingthese that offer detailed system insights. Tools such as Loki,
tools to manage and analyze data efficiently. Python scripts Sysdig, WeaveScope, Apache Kafka, and Istio are less
were often used to perform and interpret the collected data, frequently cited, suggesting their use in specific scenarios
while Docker ensured that the environment was consistent or as supplementary components in broader observability
VOLUME13,2025 72033

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
|     |     |     |     |     |     |     | insights | for optimization, |     | and | integrate | seamlessly |     | with |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | --- | --------- | ---------- | --- | ---- |
variousdistributedsystemarchitectures.
|     |     |     |     |     |     |     | Another         | critical       | challenge     |                 | is real-time | observability |           | at     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ------------- | --------------- | ------------ | ------------- | --------- | ------ |
|     |     |     |     |     |     |     | scale. Although |                | machine       | learning-driven |              | anomaly       | detection |        |
|     |     |     |     |     |     |     | techniques,     | like           | those         | employed        | in           | the SuanMing  |           | frame- |
|     |     |     |     |     |     |     | work, offer     | promising      |               | capabilities    | for          | identifying   | complex   |        |
|     |     |     |     |     |     |     | patterns        | and anomalies, |               | there           | is still     | significant   | room      | for    |
|     |     |     |     |     |     |     | improvement.    |                | These methods |                 | need         | to be         | optimized | to     |
handlethedynamicnatureoflarge-scalesystemseffectively.
|     |     |     |     |     |     |     | As microservices |         | and             | distributed | environments |                  | continue |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | --------------- | ----------- | ------------ | ---------------- | -------- | --- |
|     |     |     |     |     |     |     | to grow          | in size | and complexity, |             | real-time    | monitoring       |          | and |
|     |     |     |     |     |     |     | analysis         | become  | increasingly    |             | challenging. | Future           | research |     |
|     |     |     |     |     |     |     | should focus     |         | on developing   |             | scalable,    | high-performance |          |     |
solutionsthatcanmaintainreal-timeobservabilityandadapt
|     |     |     |     |     |     |     | to the rapidly |     | changing | conditions |     | in modern | distributed |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ---------- | --- | --------- | ----------- | --- |
systems.
FIGURE7. Usagefrequencyoftheobservabilitytools. Additionally, interoperability across diverse platforms
|     |     |     |     |     |     |     | remains | a significant |     | hurdle. | As  | applications | and | ser- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------- | --- | ------------ | --- | ---- |
solutions.Overall,thedatapointstoastrongpreferencefor vices are deployed across various environments—such as
open-source, community-supported tools like Prometheus, cloud infrastructures, edge computing nodes, and IoT
| Grafana, | and OpenTelemetry, |     | which | provide | flexibility | and |                       |     |     |            |     |         |         |     |
| -------- | ------------------ | --- | ----- | ------- | ----------- | --- | --------------------- | --- | --- | ---------- | --- | ------- | ------- | --- |
|          |                    |     |       |         |             |     | devices—observability |     |     | frameworks |     | must be | capable | of  |
integration capabilities vital for complex microservices seamlessly integrating and operating across these hetero-
| architectures. | The | emphasis | on  | kernel-level |     | observability |         |          |         |           |     |       |          |      |
| -------------- | --- | -------- | --- | ------------ | --- | ------------- | ------- | -------- | ------- | --------- | --- | ----- | -------- | ---- |
|                |     |          |     |              |     |               | geneous | systems. | Current | solutions |     | often | struggle | with |
and distributed tracing further underscores the industry’s this interoperability, leading to fragmented visibility and
focusonachievingcomprehensivemonitoringanddiagnostic difficulties in managing observability across different plat-
capabilities.
|     |     |     |     |     |     |     | forms. Enhanced |         | frameworks |             | that | can provide | a       | unified |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | ---------- | ----------- | ---- | ----------- | ------- | ------- |
|     |     |     |     |     |     |     | view and        | support | seamless   | integration |      | across      | diverse | envi-   |
A. ADVANCESANDLIMITATIONSINEXISTING ronments will be crucial for effective monitoring and
MICROSERVICESOBSERVABILITYFRAMEWORKS management of modern distributed systems. Further open
Inthissubsection,weevaluatedandsynthesizedkeyinsights research issues and challenges will be discussed in the
from our comparative analysis of observability frameworks next section, where we will explore these unresolved
| for microservices. |     | Many     | state-of-the-art |       | solutions,    | such | aspects. |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ---------------- | ----- | ------------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
| as Prometheus,     |     | Grafana, | and Zipkin,      | offer | comprehensive |      |          |     |     |     |     |     |     |     |
monitoringcapabilities,integratinglogs,metrics,andtraces VII. OPENRESEARCHISSUESANDFUTUREDIRECTION
for efficient performance analysis and anomaly detection. This section delves into the open research issues and
Advanced frameworks like STEAM [80] and ADOB [74] challengesrelatedtoobservabilityinmicroservices,drawing
employ cutting-edge techniques, such as game theory and on insights from our comparative study. As microservices
architecturesbecomeincreasinglyprevalent,addressingthese
GraphNeuralNetworks(GNNs),toenhancesystembehavior
analysis. Additionally, technologies like eBPF enable low- challengesiscrucialforadvancingthefieldofobservability
overhead, high-performance observability in frameworks andensuringthatsystemsremainefficient,reliable,andscal-
like BBMA [70], making them well-suited for resource- able.Herearesomekeyareasthatrequirefurtherexploration
| constrainedenvironments. |             |                    |        |              |         |                | and          |     |     |     |     |     |     |     |
| ------------------------ | ----------- | ------------------ | ------ | ------------ | ------- | -------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| However,                 | significant | gaps               | remain | in           | several | critical areas | development: |     |     |     |     |     |     |     |
| of observability         |             | for microservices, |        | highlighting |         | the need       |              |     |     |     |     |     |     |     |
for further advancements. One major gap is in resource A. COMPREHENSIVEOBSERVABILITYACROSSLEVELS
utilization monitoring. While some frameworks, such as Achievingthoroughobservabilityacrossalllevels—system,
KUNERVA[72]andnetobserv[89],makestridesinaddress- services, and network—presents a significant challenge.
ingresourcemanagement,thesesolutionsoftenfallshortin Most existing frameworks tend to focus primarily on one
providing a comprehensive view of resource consumption or two of these levels, often overlooking the network
across diverse distributed environments. Effective resource level, which is vital for diagnosing issues in distributed
utilizationmonitoringiscrucialforoptimizingperformance systems. Integrating observability tools that offer insights
and controlling costs, especially in large-scale deployments at all these levels is essential. This integration must be
where efficient use of computational resources directly done in a way that avoids disrupting system performance
impactssystemscalabilityandoperationalefficiency.There and is efficient, especially timely in dynamic microservices
is a pressing need for more robust solutions that can offer environmentswhereconfigurationsandstatescanfrequently
| granular | visibility | into resource |     | usage, | provide | actionable | change[97]. |     |     |     |     |     |               |     |
| -------- | ---------- | ------------- | --- | ------ | ------- | ---------- | ----------- | --- | --- | --- | --- | --- | ------------- | --- |
| 72034    |            |               |     |        |         |            |             |     |     |     |     |     | VOLUME13,2025 |     |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
B. UNIFIEDDATACOLLECTIONANDANALYSIS sensitive system resources. Research is needed to develop
|              |     |           |               |     |     |             |     | robust security |     | mechanisms |     | for kernel-level |     | observability, |     |
| ------------ | --- | --------- | ------------- | --- | --- | ----------- | --- | --------------- | --- | ---------- | --- | ---------------- | --- | -------------- | --- |
| A key aspect | of  | effective | observability |     | is  | the ability | to  |                 |     |            |     |                  |     |                |     |
integrate various types of data—logs, metrics, and traces— including secure instrumentation techniques and access
to create a comprehensive understanding of the system’s controls[101],[102].
condition.Thisholisticviewiscrucialfordiagnosingissues
anddetectinganomaliesinmicroservicesarchitectures[98].
|     |     |     |     |     |     |     |     | 2) USERLEVEL |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Whilesomemethodshavemadeprogressinthisarea,there
|         |            |          |       |     |            |      |     | Personal | Data       | Protection: | Observability |     | at   | the user       | level |
| ------- | ---------- | -------- | ----- | --- | ---------- | ---- | --- | -------- | ---------- | ----------- | ------------- | --- | ---- | -------------- | ----- |
| remains | a need for | improved | tools | and | techniques | that | can |          |            |             |               |     |      |                |       |
|         |            |          |       |     |            |      |     | involves | monitoring | user        | interactions  |     | with | microservices, |       |
seamlesslycorrelatedatafromdifferentsourcesandtypesin
whichmayincludesensitivepersonaldata.Ensuringthepri-
real-time.Thisintegrationisnecessaryforaccuraterootcause
vacyandsecurityofthisdataisparamount,asunauthorized
| analysis | and timely | detection |     | of issues | without | imposing |     |           |          |       |        |     |         |            |     |
| -------- | ---------- | --------- | --- | --------- | ------- | -------- | --- | --------- | -------- | ----- | ------ | --- | ------- | ---------- | --- |
|          |            |           |     |           |         |          |     | access or | exposure | could | result | in  | privacy | violations | and |
significantperformanceoverhead.
legalramifications.Researchisneededtodeveloptechniques
|     |     |     |     |     |     |     |     | for anonymizing |     | or pseudonymizing |     |     | user | data while | still |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | --- | ---- | ---------- | ----- |
C. SCALABILITYANDREAL-TIMEPROCESSING enablingeffectiveobservability[102],[103].
| As microservices |     | architectures |     | become | more | extensive | and |          |     |        |             |     |            |     |         |
| ---------------- | --- | ------------- | --- | ------ | ---- | --------- | --- | -------- | --- | ------ | ----------- | --- | ---------- | --- | ------- |
|                  |     |               |     |        |      |           |     | Identity | and | Access | Management: |     | User-level |     | observ- |
complex,observabilitytoolsmustbeabletohandleincreas- ability requires robust identity and access management
| ing amounts | of data | efficiently |     | [99]. | Scalability | is a | major |                 |     |            |     |        |              |      |       |
| ----------- | ------- | ----------- | --- | ----- | ----------- | ---- | ----- | --------------- | --- | ---------- | --- | ------ | ------------ | ---- | ----- |
|             |         |             |     |       |             |      |       | (IAM) practices |     | to control |     | access | to sensitive | user | data. |
concern,asthesetoolsmustgrowalongsidethesystemsthey
Researchchallengesincludedesigningsecureauthentication
monitorwithoutdegradingperformance.Moreover,real-time mechanisms, enforcing the principle of least privilege, and
| processing | capabilities | are | essential | to  | provide | immediate |     |            |              |     |      |        |              |     |           |
| ---------- | ------------ | --- | --------- | --- | ------- | --------- | --- | ---------- | ------------ | --- | ---- | ------ | ------------ | --- | --------- |
|            |              |     |           |     |         |           |     | preventing | unauthorized |     | data | access | by malicious |     | actors or |
feedback and enable quick responses to detected issues. insiderthreats.[78].
| Ensuring | that observability |     | tools | can scale | effectively |     | while |     |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | ----- | --------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
maintainingtheabilitytoprocessdatainreal-timeiscrucial
|     |     |     |     |     |     |     |     | 3) NETWORKLEVEL |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
formanaginglarge-scaleenvironments.
|     |     |     |     |     |     |     |     | Data in | Transit | Protection: |     | Observability |     | at the | network |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | --- | ------------- | --- | ------ | ------- |
levelinvolvesmonitoringcommunicationbetweenmicroser-
D. ADAPTABILITYTODYNAMICENVIRONMENTS
|               |               |         |             |        |          |                 |      | vices, which         |     | may include |            | the transmission |           | of         | sensitive |
| ------------- | ------------- | ------- | ----------- | ------ | -------- | --------------- | ---- | -------------------- | --- | ----------- | ---------- | ---------------- | --------- | ---------- | --------- |
| Microservices | environments  |         | are         | highly | dynamic, | with            | fre- |                      |     |             |            |                  |           |            |           |
|               |               |         |             |        |          |                 |      | data over            | the | network.    | Research   |                  | is needed | to         | develop   |
| quent updates | in            | service | deployments |        | and      | configurations. |      |                      |     |             |            |                  |           |            |           |
|               |               |         |             |        |          |                 |      | secure communication |     |             | protocols, | such             | as        | encryption | and       |
| Observability | frameworks    |         | need        | to be  | flexible | enough          | to   |                      |     |             |            |                  |           |            |           |
|               |               |         |             |        |          |                 |      | authentication       |     | mechanisms, | to         | protect          | data      | in transit | from      |
| adapt to      | these changes |         | to maintain |        | accurate | monitoring.     |      |                      |     |             |            |                  |           |            |           |
interceptionortampering.Securityhasalwaysbeenanissue
Thismeansdevelopingsystemsthatcanautomaticallydetect
innetworkingsystems,butitgetsmoredifficultwiththeuse
| new services, | adjust | monitoring |     | parameters |     | on the fly, | and |     |     |     |     |     |     |     |     |
| ------------- | ------ | ---------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofmicroservices[104].
continuetoprovidepreciseinsightsdespiteongoingchanges.
|          |               |         |     |          |            |       |     | Network  | Traffic | Analysis: |     | Analyzing     |     | network  | traffic |
| -------- | ------------- | ------- | --- | -------- | ---------- | ----- | --- | -------- | ------- | --------- | --- | ------------- | --- | -------- | ------- |
| Creating | observability | systems |     | that can | seamlessly | adapt | to  |          |         |           |     |               |     |          |         |
|          |               |         |     |          |            |       |     | patterns | and     | anomalies | for | observability |     | purposes | raises  |
theseevolvingconditionsisvitalforeffectivemonitoringin
|     |     |     |     |     |     |     |     | privacy | concerns, | as it | may | inadvertently |     | reveal | sensitive |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----- | --- | ------------- | --- | ------ | --------- |
rapidlychangingenvironments.
|     |     |     |     |     |     |     |     | information | about | system | architecture, |     | data | flows, | or user |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | ------------- | --- | ---- | ------ | ------- |
behavior.Researchchallengesincludedevelopingtechniques
E. PRIVACYANDSECURITY
fornetworktrafficanalysisthatbalancetheneedforobserv-
In this section, we have discussed the research challenges abilitywithpreservinguserprivacy,suchasaggregationand
relatedtoprivacyandsecurityinmicroservicesobservability
anonymizationmethods.
acrossdifferentlevels. To address these challenges, future work should focus
|     |     |     |     |     |     |     |     | on specific | areas | for | further | exploration. |     | Addressing | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | ------- | ------------ | --- | ---------- | --- |
1) KERNELLEVEL comprehensive observability across all system, service, and
Granularity vs. Privacy: At the kernel level, accessing networklevelswillrequiredevelopingunifiedtoolsthatoffer
detailedsysteminformationandresourceusagemetricsmay deeper insights without impacting performance. Refining
provide valuable observability insights. However, this level existing frameworks to incorporate more network-level
of granularity raises concerns about data privacy, as it may observability could help overcome gaps in diagnosing
expose sensitive information about system processes and distributed systems. In terms of unified data collection
interactions. Balancing the need for detailed observability and analysis, there’s a need for tools that can seamlessly
with preserving user privacy poses a significant research correlate logs, metrics, and traces in real time to enable
challenge[100]. accurate root cause analysis without imposing significant
SecureKernelInstrumentation:Implementingobservabil- overhead. Additionally, as microservices architectures grow
ity tools that interact directly with the kernel introduces in complexity, tools must be enhanced to handle increasing
security risks, as any vulnerabilities in these tools could data volumes, improving scalability and real-time pro-
potentially be exploited to gain unauthorized access to cessing capabilities. Observability frameworks should also
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 72035 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
evolvetobecomemoreadaptabletodynamicmicroservices theresilienceandefficiencyofmoderndigitalinfrastructures
environments, incorporating automation and AI to detect that support a wide array of applications and services.
and adjust monitoring parameters in response to frequent Therefore, future research should focus on developing
changes. On the privacy and security front [58], more comprehensive, scalable, and adaptable observability tools
securemethodsforkernel-levelinstrumentationandstronger that can meet the challenges posed by the continuous
identity and real-time management at the user level are evolutionofmicroservicesincomputingenvironments.
| required. | For | network-level | observability, |     |     | future | research |     |     |     |     |     |     |     |
| --------- | --- | ------------- | -------------- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
must focus on developing encryption and traffic analysis ACKNOWLEDGMENT
| techniques | that | prioritize | security | and | privacy. | Addressing |     |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | -------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
TheauthorsextendtheirthankstotheNationalUniversityof
theseareaswillprovidethefoundationformoreeffectiveand ComputerandEmergingSciences(FAST),Karachi,Pakistan,
secureobservabilityinmicroservicesarchitectures. fortheirvaluabletechnicalassistance.Lastly,theyaredeeply
|     |     |     |     |     |     |     |     | appreciative | of  | the anonymous |     | reviewers | for their | detailed |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | --------- | --------- | -------- |
F. POTENTIALOPPORTUNITIESFOREMERGING feedbackandinsightfulsuggestions,whichhavesubstantially
RESEARCHERS
improvedtheoverallqualityandpresentationofthisarticle.
| Future research |               | in microservices |            | observability |      | can         | explore |     |     |     |     |     |     |     |
| --------------- | ------------- | ---------------- | ---------- | ------------- | ---- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| self-adaptive   | observability |                  | frameworks |               | that | dynamically |         |     |     |     |     |     |     |     |
CONFLICTOFINTEREST
| adjust monitoring |            | strategies      | based    |              | on workload |            | patterns, |             |                 |      |         |                  |               |             |
| ----------------- | ---------- | --------------- | -------- | ------------ | ----------- | ---------- | --------- | ----------- | --------------- | ---- | ------- | ---------------- | ------------- | ----------- |
|                   |            |                 |          |              |             |            |           | The authors | declare         | that | there   | are no conflicts |               | of interest |
| system            | anomalies, | and             | resource | constraints. |             | Unlike     | static    |             |                 |      |         |                  |               |             |
|                   |            |                 |          |              |             |            |           | regarding   | the publication |      | of this | article.         | No financial, | per-        |
| observability     |            | configurations, |          | such         | adaptive    | frameworks |           |             |                 |      |         |                  |               |             |
sonal,orotherrelationshipswithorganizationsorindividuals
would leverage reinforcement learning and feedback loops have influenced the content or findings presented in this
| to optimize | metric | collection, |     | trace | sampling, |     | and log |     |     |     |     |     |     |     |
| ----------- | ------ | ----------- | --- | ----- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
manuscript.
aggregationinreal-time,reducingoverheadwhilepreserving
| critical | insights. | Additionally, |     | integrating |     | causal | inference |     |     |     |     |     |     |     |
| -------- | --------- | ------------- | --- | ----------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| techniques | into | observability |     | pipelines | could | enhance | root |     |     |     |     |     |     |     |
| ---------- | ---- | ------------- | --- | --------- | ----- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
[1] S.Luo,C.Lin,K.Ye,G.Xu,L.Zhang,G.Yang,H.Xu,andC.Xu,
causeanalysisbydistinguishingcorrelationfromcausationin
‘‘Optimizingresourcemanagementforsharedmicroservices:Ascalable
| complex | microservices |     | failures. | These | directions | align | with |     |     |     |     |     |     |     |
| ------- | ------------- | --- | --------- | ----- | ---------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
systemdesign,’’ACMTrans.Comput.Syst.,vol.42,nos.1–2,pp.1–28,
| the evolving | need | for intelligent, |     | automated, |     | and | efficient |     |     |     |     |     |     |     |
| ------------ | ---- | ---------------- | --- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
May2024.
observability solutions that can scale with the increasing [2] S.Long,Y.Zhang,Q.Deng,T.Pei,J.Ouyang,andZ.Xia,‘‘Anefficient
taskoffloadingapproachbasedonmulti-objectiveevolutionaryalgorithm
complexityofdistributedcloud-nativearchitectures.
incloud-edgecollaborativeenvironment,’’IEEETrans.Netw.Sci.Eng.,
vol.10,no.2,pp.645–657,Mar.2023.
VIII. CONCLUSION [3] H.J.Syed,A.Gani,R.W.Ahmad,M.K.Khan,andA.I.A.Ahmed,
This paper presents a comprehensive analysis of the tran- ‘‘Cloud monitoring: A review, taxonomy, and open research issues,’’
J.Netw.Comput.Appl.,vol.98,pp.11–26,Nov.2017.
| sition towards |     | microservices |     | architecture |     | in containerized |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[4] I.Shabani,E.Mëziu,B.Berisha,andT.Biba,‘‘Designofmoderndis-
cloud, fog, and edge environments, emphasizing the crit- tributedsystemsbasedonmicroservicesarchitecture,’’Int.J.Adv.Com-
ical need for enhanced observability to sustain system put.Sci.Appl.,vol.12,no.2,pp.1–7,2021.
[5] I.K.Aksakalli,T.Çelik,A.B.Can,andB.Tekinerdoğan,‘‘Deployment
| reliability | and | performance. |     | We have | examined |     | various |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | ------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
andcommunicationpatternsinmicroservicearchitectures:Asystematic
sophisticatedobservabilitymechanismsthatareessentialfor
literaturereview,’’J.Syst.Softw.,vol.180,Oct.2021,Art.no.111014.
the prompt diagnosis and mitigation of potential failures. [6] F. Aydemir and F. Başçiftçi, ‘‘Building a performance efficient core
These mechanisms are indispensable to ensure continuous banking system based on the microservices architecture,’’ J. Grid
serviceavailabilityandmaintainoptimalperformancelevels, Comput.,vol.20,no.4,p.37,Dec.2022.
|     |     |     |     |     |     |     |     | [7] J. | S. Nunes, | S.  | C. Sampaio, | R.  | S. Malaquias, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ----------- | --- | ------------- | --- |
which are crucial for user satisfaction and operational I.DeMoraisBarrocaFilho, ‘‘Deploying the observability of the
continuity. Our analysis reveals a significant gap in current SigSaudesystemusingservicemesh,’’inProc.20thInt.Conf.Comput.
observability frameworks, particularly in their capacity to Sci.ItsAppl.(ICCSA),Jul.2020,pp.9–15.
[8] A.MartínezSaucedo,G.Rodríguez,F.GomesRocha,andR.P.D.Santos,
| manage | the increasing |          | complexity | and       | dynamic |       | nature of |             |     |               |         |                   |     |              |
| ------ | -------------- | -------- | ---------- | --------- | ------- | ----- | --------- | ----------- | --- | ------------- | ------- | ----------------- | --- | ------------ |
|        |                |          |            |           |         |       |           | ‘‘Migration |     | of monolithic | systems | to microservices: |     | A systematic |
| modern | distributed    | systems. | In         | addition, | the     | study | suggests  |             |     |               |         |                   |     |              |
mappingstudy,’’Inf.Softw.Technol.,vol.177,Jan.2025,Art.no.107590.
thatfuturedevelopmentsshouldprioritizethescalabilityand [9] G.Liu,B.Huang,Z.Liang,M.Qin,H.Zhou,andZ.Li,‘‘Microser-
adaptability of observability tools to keep pace with the vices: Architecture, container, and challenges,’’ in Proc. IEEE 20th
Int.Conf.Softw.Quality,Rel.Secur.Companion(QRS-C),Dec.2020,
| rapid evolution |     | of microservices |     | architectures. |     | As  | systems |     |     |     |     |     |     |     |
| --------------- | --- | ---------------- | --- | -------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
pp.629–635.
grow and change, these tools must evolve correspondingly [10] C. Cassé, P. Berthou, P. Owezarski, and S. Josset, ‘‘A tracing based
to provide consistent and reliable insights across various modeltoidentifybottlenecksinphysicallydistributedapplications,’’in
Proc.Int.Conf.Inf.Netw.(ICOIN),Jan.2022,pp.226–231.
deploymentenvironments,fromthecloudtothefogandedge.
[11] T.Zeng,Z.Xu,D.Wu,X.Li,B.Liu,H.Hu,S.Tan,Y.Tan,C.Xu,
| In essence, | advancing |     | observability |     | frameworks | is  | pivotal |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------------- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
C.Stewart,Q.Zhou,andY.Cao,‘‘Exploringnonintrusivemeasurements
not only for maintaining the reliability and performance of ofspatio-temporalportraitofmicroservices,’’Softw.,Pract.Exp.,vol.54,
no.10,pp.2025–2041,Oct.2024.
| microservices   |     | architectures | but      | also | for ensuring |          | that they |                |     |                |               |            |        |                |
| --------------- | --- | ------------- | -------- | ---- | ------------ | -------- | --------- | -------------- | --- | -------------- | ------------- | ---------- | ------ | -------------- |
|                 |     |               |          |      |              |          |           | [12] Y. Wang,  | H.  | Kadiyala,      | and J. Rubin, | ‘‘Promises | and    | challenges of  |
| can effectively |     | meet the      | evolving |      | demands      | of users | and       |                |     |                |               |            |        |                |
|                 |     |               |          |      |              |          |           | microservices: |     | An exploratory | study,’’      | Empirical  | Softw. | Eng., vol. 26, |
technological landscapes. This will ultimately contribute to no.4,p.63,Jul.2021.
| 72036 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
[13] H. Siddiqui, F. Khendek, and M. Toeroe, ‘‘Microservices based [35] X. Liu, Y. Yu, M. Yu, D. Liao, Y. Li, and Z. Ji, ‘‘An edge-
architecturesforIoTsystems—State-of-the-artreview,’’InternetThings, cloudcollaborativecomputingsystemforreal-timeInternet-of-Things
vol.23,Oct.2023,Art.no.100854. applications,’’inProc.Int.Conf.Comput.Sci.Educ.Cham,Switzerland:
[14] A. B. Raharjo, P. K. Andyartha, W. H. Wijaya, Y. Purwananto, Springer,2022,pp.652–663.
D.Purwitasari,andN.Juniarta,‘‘Reliabilityevaluationofmicroservices [36] V. Veeramachaneni, ‘‘Edge computing: Architecture, applications,
andmonolithicarchitectures,’’inProc.Int.Conf.Comput.Eng.,Netw., and future challenges in a decentralized era,’’ Recent Trends Com-
Intell.Multimedia(CENIM),Nov.2022,pp.1–7. put.Graph.MultimediaTechnol.,vol.7,no.1,pp.8–23,2025.
[15] R. Gatev and R. Gatev, ‘‘Observability: Logs, metrics, and traces,’’ [37] G.Carvalho,B.Cabral,V.Pereira,andJ.Bernardino,‘‘Edgecomputing:
in Introducing Distributed Application Runtime (Dapr): Simplifying Currenttrends,researchchallengesandfuturedirections,’’Computing,
MicroservicesApplicationsDevelopmentThroughProvenandReusable vol.103,no.5,pp.993–1023,May2021.
PatternsandPractices.Berkeley,CA,USA:Apress,2021,pp.233–252. [38] A. Dimou, C. Iliopoulos, E. Polytidou, S. K. Dhurandher,
[16] B.Li,X.Peng,Q.Xiang,H.Wang,T.Xie,J.Sun,andX.Liu,‘‘Enjoyyour G.Papadimitriou, and P. Nicopolitidis, ‘‘A comprehensive review on
observability:Anindustrialsurveyofmicroservicetracingandanalysis,’’ edgecomputing:Focusingonmobileusers,’’inAdvancesinComputing,
EmpiricalSoftw.Eng.,vol.27,no.1,pp.1–28,Jan.2022. Informatics,NetworkingandCybersecurity:ABookHonoringProfessor
[17] D. Das, M. Schiewe, E. Brighton, M. Fuller, T. Cerny, M. Bures, Mohammad S. Obaidat’s Significant Scientific Contributions, 2022,
K.Frajtak, D. Shin, and P. Tisnovsky, ‘‘Failure prediction pp.121–152.
by utilizing log analysis: A systematic mapping study,’’ in [39] J. Almutairi and M. Aldossary, ‘‘A novel approach for IoT tasks
Proc.Int.Conf.Res.Adapt.ConvergentSyst.,Oct.2020,pp.188–195. offloadinginedge-cloudenvironments,’’J.CloudComput.,vol.10,no.1,
[18] L.Wang,N.Zhao,J.Chen,P.Li,W.Zhang,andK.Sui,‘‘Root-cause p.28,Apr.2021.
metriclocationformicroservicesystemsvialoganomalydetection,’’in [40] T.Zhang,Y.Li,andC.L.PhilipChen,‘‘Edgecomputinganditsrolein
Proc.IEEEInt.Conf.WebServices(ICWS),Oct.2020,pp.142–150. industrialInternet:Methodologies,applications,andfuturedirections,’’
[19] E. A. Matusse, E. H. M. Huzita, and T. F. C. Tait, ‘‘Metrics and Inf.Sci.,vol.557,pp.34–65,May2021.
indicators to assist in the distribution of process steps for distributed [41] F.Firouzi,B.Farahani,andA.Marinšek,‘‘Theconvergenceandinterplay
software development: A systematic review,’’ in Proc. Conferencia of edge, fog, and cloud in the AI-driven Internet of Things (IoT),’’
LatinoamericanaEnInf.(CLEI),Oct.2012,pp.1–10. Inf.Syst.,vol.107,Jul.2022,Art.no.101840.
[20] M. G. Moreira and B. B. N. De França, ‘‘Analysis of microser- [42] H. G. Abreha, C. J. Bernardos, A. D. L. Oliva, L. Cominardi, and
vice evolution using cohesion metrics,’’ in Proc. 16th Brazilian A.Azcorra,‘‘Monitoringinfogcomputing:State-of-the-artandresearch
Symp.Softw.Compon.,Architectures,Reuse,Oct.2022,pp.40–49. challenges,’’ Int. J. Ad Hoc Ubiquitous Comput., vol. 36, no. 2,
[21] E.Fadda,P.Plebani,andM.Vitali,‘‘Monitoring-awareoptimaldeploy- pp.114–130,2021.
ment for applications based on microservices,’’ IEEE Trans. Services [43] B. Costa, J. Bachiega, L. R. Carvalho, M. Rosa, and A. Araujo,
Comput.,vol.14,no.6,pp.1849–1863,Nov.2021. ‘‘Monitoringfogcomputing:Areview,taxonomyandopenchallenges,’’
[22] M.Söylemez,B.Tekinerdogan,andA.KolukısaTarhan,‘‘Challengesand Comput.Netw.,vol.215,Oct.2022,Art.no.109189.
solutiondirectionsofmicroservicearchitectures:Asystematicliterature [44] D. Soldani, P. Nahi, H. Bour, S. Jafarizadeh, M. F. Soliman,
review,’’Appl.Sci.,vol.12,no.11,p.5507,May2022. L.DiGiovanna, F. Monaco, G. Ognibene, and F. Risso, ‘‘EBPF: A
[23] J. Rios, S. Jha, and L. Shwartz, ‘‘Localizing and explaining faults newapproachtocloud-nativeobservability,networkingandsecurityfor
in microservices using distributed tracing,’’ in Proc. IEEE 15th current(5G)andfuturemobilenetworks(6Gandbeyond),’’IEEEAccess,
Int.Conf.CloudComput.(CLOUD),Jul.2022,pp.489–499. vol.11,pp.57174–57202,2023.
[24] S. Alam, S. Zardari, S. Noor, S. Ahmed, and H. Mouratidis, ‘‘Trust [45] T.Weng,W.Yang,G.Yu,P.Chen,J.Cui,andC.Zhang,‘‘Kmon:An
managementinsocialInternetofThings(SIoT):Asurvey,’’IEEEAccess, in-kerneltransparentmonitoringsystemformicroservicesystemswith
vol.10,pp.108924–108954,2022. eBPF,’’inProc.IEEE/ACMInt.WorkshopCloudIntell.(CloudIntelli-
[25] S.Zhang,M.Zhang,L.Ni,andP.Liu,‘‘Amulti-levelself-adaptation gence),May2021,pp.25–30.
approachformicroservicesystems,’’inProc.IEEE4thInt.Conf.Cloud [46] B.SharmaandD.Nadig,‘‘EBPF-enhancedcompleteobservabilitysolu-
Comput.BigDataAnal.(ICCCBDA),Apr.2019,pp.498–502. tionforcloud-nativemicroservices,’’inProc.IEEEInt.Conf.Commun.
[26] J.Bogner,S.Schlinger,S.Wagner,andA.Zimmermann,‘‘Amodular (ICC),Jun.2024,pp.1980–1985.
approachtocalculateservice-basedmaintainabilitymetricsfromruntime [47] M. R. S. Sedghpour and P. Townend, ‘‘Service mesh and eBPF-
dataofmicroservices,’’inProc.Int.Conf.Product-FocusedSoftw.Pro- poweredmicroservices:Asurveyandfuturedirections,’’inProc.IEEE
cessImprovement.Cham,Switzerland:Springer,Jan.2019,pp.489–496. Int.Conf.Service-OrientedSyst.Eng.(SOSE),Aug.2022,pp.176–184.
[27] J. Kosinska, B. Balis, M. Konieczny, M. Malawski, and S. Zielinski, [48] Y.-T. Wang, S.-P. Ma, Y.-J. Lai, and Y.-C. Liang, ‘‘Analyzing and
‘‘Towardstheobservabilityofcloud-nativeapplications:Theoverview monitoringKubernetesmicroservicesbasedondistributedtracingand
ofthestate-of-the-art,’’IEEEAccess,vol.11,pp.73036–73052,2023. servicemesh,’’inProc.29thAsia–PacificSoftw.Eng.Conf.(APSEC),
[28] M. Stocker, O. Zimmermann, U. Zdun, D. Lübke, and C. Pautasso, Dec.2022,pp.477–481.
‘‘Interfacequalitypatterns:Communicatingandimprovingthequalityof [49] S.Miano,F.Risso,M.V.Bernal,M.Bertrone,andY.Lu,‘‘Aframework
microservicesApis,’’inProc.23rdEur.Conf.PatternLang.Programs, for eBPF-based network functions in an era of microservices,’’ IEEE
Jul.2018,pp.1–16. Trans.Netw.ServiceManage.,vol.18,no.1,pp.133–151,Mar.2021.
[29] D. Berardi, S. Giallorenzo, J. Mauro, A. Melis, F. Montesi, and [50] E.Muškardin,M.Tappler,B.K.Aichernig,andI.Pill,‘‘Reinforcement
M.Prandini, ‘‘Microservice security: A systematic literature review,’’ learning under partial observability guided by learned environment
PeerJComput.Sci.,vol.7,p.e779,Jan.2022. models,’’inProc.Int.Conf.Integr.FormalMethods.Cham,Switzerland:
[30] A. Bhardwaj and T. A. Benson, ‘‘KubeKlone: A digital twin for Springer,Jan.2022,pp.257–276.
simulating edge and cloud microservices,’’ in Proc. 6th Asia–Pacific [51] L.Min,K.A.Alnowibet,A.F.Alrasheedi,F.Moazzen,E.M.Awwad,
WorkshopNetw.,Jul.2022,pp.29–35. andM.A.Mohamed,‘‘Astochasticmachinelearningbasedapproach
[31] J. Soldani and A. Brogi, ‘‘Anomaly detection and failure root cause forobservabilityenhancementofautomatedsmartgrids,’’Sustain.Cities
analysisin(Micro)service-basedcloudapplications:Asurvey,’’ACM Soc.,vol.72,Sep.2021,Art.no.103071.
Comput.Surveys,vol.55,no.3,pp.1–39,Mar.2023. [52] X.Wu,Z.Jing,andX.Wang,‘‘ThesecurityofIoTfromtheperspective
[32] M. Asim, Y. Wang, K. Wang, and P.-Q. Huang, ‘‘A review on of the observability of complex networks,’’ Heliyon, vol. 10, no. 5,
computational intelligence techniques in cloud and edge computing,’’ Mar.2024,Art.no.e27104.
IEEETrans.Emerg.TopicsComput.Intell.,vol.4,no.6,pp.742–763, [53] C. Ding, L. Zhu, L. Shen, Z. Li, Y. Li, and Q. Liang, ‘‘The
Dec.2020. intelligenttrafficflowcontrolsystembasedon6Gandoptimizedgenetic
[33] Y.MansouriandM.A.Babar,‘‘Areviewofedgecomputing:Features algorithm,’’IEEETrans.Intell.Transp.Syst.,earlyaccess,Oct.7,2024,
and resource virtualization,’’ J. Parallel Distrib. Comput., vol. 150, doi:10.1109/TITS.2024.3467269.
pp.155–183,Apr.2021. [54] X.Cong,M.P.Fanti,A.M.Mangini,andZ.Li,‘‘Criticalobservability
[34] C. Mwase, Y. Jin, T. Westerlund, H. Tenhunen, and Z. Zou, verification and enforcement of labeled Petri nets by using basis
‘‘Communication-efficientdistributedAIstrategiesfortheIoTedge,’’ markings,’’IEEETrans.Autom.Control,vol.68,no.12,pp.8158–8164,
FutureGener.Comput.Syst.,vol.131,pp.292–308,Jun.2022. Dec.2023.
VOLUME13,2025 72037

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
[55] M. Akbari, R. Bolla, R. Bruschi, F. Davoli, C. Lombardo, and [75] L.Wüstrich,M.Schacherbauer,M.Budeus,D.FreiherrvonKünßberg,
B. Siccardi, ‘‘A monitoring, observability and analytics framework S. Gallenmüller, M.-O. Pahl, and G. Carle, ‘‘Network profiles for
to improve the sustainability of B5G technologies,’’ in Proc. IEEE detecting application-characteristic behavior using Linux eBPF,’’ in
Int. Conf. Commun. Workshops (ICC Workshops), Jun. 2024, Proc.1stWorkshopeBPFKernelExtensions,Sep.2023,pp.8–14.
pp.969–975. [76] M.Usman,S.Ferlin,A.Brunstrom,andJ.Taheri,‘‘Desk:Distributed
[56] M. Usman, S. Ferlin, A. Brunstrom, and J. Taheri, ‘‘A survey on observabilityframeworkforedge-basedcontainerizedmicroservices,’’in
observabilityofdistributededge&container-basedmicroservices,’’IEEE Proc.JointEur.Conf.Netw.Commun.6GSummit(EuCNC/6GSummit),
| Access,vol.10,pp.86904–86919,2022. |     |     |     |     |     |     |     | Jun.2023,pp.617–622. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
[57] J. Parmar, S. Sanghavi, V. K. Prasad, and P. Shah, ‘‘Microservice [77] K. Alanezi and S. Mishra, ‘‘Utilizing microservices architecture for
architecture observability tool analysis,’’ in Proc. Int. Conf. Soft enhanced service sharing in IoT edge environments,’’ IEEE Access,
Comput. Signal Process. Cham, Switzerland: Springer, Jan. 2023, vol.10,pp.90034–90044,2022.
pp.1–8.
|             |           |         |           |           |     |       |          | [78] U. Zdun, | P.-J. | Queval, G.    | Simhandl,      | R. Scandariato, |          | S. Chakravarty, |     |
| ----------- | --------- | ------- | --------- | --------- | --- | ----- | -------- | ------------- | ----- | ------------- | -------------- | --------------- | -------- | --------------- | --- |
| [58] S. Li, | H. Zhang, | Z. Jia, | C. Zhong, | C. Zhang, | Z.  | Shan, | J. Shen, |               |       |               |                |                 |          |                 |     |
|             |           |         |           |           |     |       |          | M. Jelic,     | and   | A. Jovanovic, | ‘‘Microservice |                 | security | metrics         | for |
and M. A. Babar, ‘‘Understanding and addressing quality attributes securecommunication,identitymanagement,andobservability,’’ACM
of microservices architecture: A systematic literature review,’’ Trans.Softw.Eng.Methodology,vol.32,no.1,pp.1–34,Jan.2023.
Inf.Softw.Technol.,vol.131,Mar.2021,Art.no.106449. [79] M.Scrocca,R.Tommasini,A.Margara,E.D.Valle,andS.Sakr,‘‘The
[59] V. Velepucha and P. Flores, ‘‘A survey on microservices architecture: kaijuproject:Enablingevent-drivenobservability,’’inProc.14thACM
| Principles, | patterns | and migration | challenges,’’ |     | IEEE | Access, | vol. 11, |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------------- | ------------- | --- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Int.Conf.Distrib.Event-basedSyst.,Jul.2020,pp.85–96.
pp.88339–88358,2023.
|     |     |     |     |     |     |     |     | [80] S. He, | B. Feng, | L. Li, X. | Zhang, | Y. Kang, | Q. Lin, | S. Rajmohan, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --------- | ------ | -------- | ------- | ------------ | --- |
[60] S.Zhang,S.Xia,W.Fan,B.Shi,X.Xiong,Z.Zhong,M.Ma,Y.Sun,
andD.Zhang,‘‘STEAM:Observability-preservingtracesampling,’’in
andD.Pei,‘‘Failurediagnosisinmicroservicesystems:Acomprehensive Proc.31stACMJointEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,
surveyandanalysis,’’ACMTrans.Softw.Eng.Methodology,Jan.2025. Nov.2023,pp.1750–1761.
[61] M. Hamza, ‘‘Transforming monolithic systems to a microservices [81] O. Mart, C. Negru, F. Pop, and A. Castiglione, ‘‘Observability in
architecture,’’ACMSIGSOFTSoftw.Eng.Notes,vol.48,no.1,pp.67–69,
Kubernetescluster:Automaticanomaliesdetectionusingprometheus,’’
Jan.2023.
|                |     |          |          |                |     |         |        | in Proc. | IEEE      | 22nd Int.   | Conf. | High Perform. | Comput.    | Commun., |            |
| -------------- | --- | -------- | -------- | -------------- | --- | ------- | ------ | -------- | --------- | ----------- | ----- | ------------- | ---------- | -------- | ---------- |
| [62] A. Razzaq | and | S. A. K. | Ghayyur, | ‘‘A systematic |     | mapping | study: |          |           |             |       |               |            |          |            |
|                |     |          |          |                |     |         |        | IEEE     | 18th Int. | Conf. Smart | City, | IEEE 6th      | Int. Conf. | Data     | Sci. Syst. |
Thenewageofsoftwarearchitecturefrommonolithictomicroservice (HPCC/SmartCity/DSS),Dec.2020,pp.565–570.
architecture—Awareness and challenges,’’ Comput. Appl. Eng. Educ., [82] J. Simonsson, L. Zhang, B. Morin, B. Baudry, and M. Monperrus,
vol.31,no.2,pp.421–451,Mar.2023. ‘‘Observabilityandchaosengineeringonsystemcallsforcontainerized
[63] R.Su,X.Li,andD.Taibi,‘‘Frommicroservicetomonolith:Amultivocal
|     |     |     |     |     |     |     |     | applications | in  | Docker,’’ | Future | Gener. | Comput. | Syst., vol. | 122, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ------ | ------ | ------- | ----------- | ---- |
literaturereview,’’Electronics,vol.13,no.8,p.1452,Apr.2024.
pp.117–129,Sep.2021.
| [64] L. Giamattei, |     | A. Guerriero, | R. Pietrantuono, |     | S. Russo, | I.Malavolta,   |     |            |             |                  |           |       |              |            |         |
| ------------------ | --- | ------------- | ---------------- | --- | --------- | -------------- | --- | ---------- | ----------- | ---------------- | --------- | ----- | ------------ | ---------- | ------- |
|                    |     |               |                  |     |           |                |     | [83] L.-D. | Chou, L.-Y. | Jian,            | and Y.-W. | Chen, | ‘‘EBPF-based |            | network |
| T. Islam,          | M.  | Dînga,        | A. Koziolek,     | S.  | Singh,    | M. Armbruster, |     |            |             |                  |           |       |              |            |         |
|                    |     |               |                  |     |           |                |     | monitoring | platform    | on Kubernetes,’’ |           | in    | Proc. 6th    | Int. Conf. | Com-    |
J. M. Gutierrez-Martinez, S. Caro-Alvaro, D. Rodriguez, S. Weber, put.Commun.Internet(ICCCI),Jun.2024,pp.140–144.
J.Henss,E.F.Vogelin,andF.S.Panojo,‘‘MonitoringtoolsforDevOps
andmicroservices:Asystematicgreyliteraturereview,’’J.Syst.Softw., [84] Y. Pan, M. Ma, X. Jiang, and P. Wang, ‘‘Faster, deeper, easier:
Crowdsourcingdiagnosisofmicroservicekernelfailurefromuserspace,’’
vol.208,Feb.2024,Art.no.111906.
inProc.30thACMSIGSOFTInt.Symp.Softw.Test.Anal.,Jul.2021,
[65] I.Fé,T.A.Nguyen,A.B.Soares,S.Son,E.Choi,D.Min,J.-W.Lee,
pp.646–657.
andF.A.Silva,‘‘Model-drivendependabilityandpowerconsumption
|     |     |     |     |     |     |     |     | [85] L. Abdollahi | Vayghan, | M.  | A. Saied, | M.  | Toeroe, | and F. Khendek, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | --- | --------- | --- | ------- | --------------- | --- |
quantificationofKubernetes-basedcloud-fogcontinuum,’’IEEEAccess,
vol.11,pp.140826–140852,2023. ‘‘Deploying microservice based applications with Kubernetes: Exper-
|     |     |     |     |     |     |     |     |     |     |     |     | Proc. IEEE | 11th | Int. Conf. | Cloud |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | ----- |
[66] M. Cinque, R. D. Corte, and A. Pecchia, ‘‘Microservices monitoring iments and lessons learned,’’ in
Comput.(CLOUD),Jul.2018,pp.970–973.
witheventlogsandblackboxexecutiontracing,’’IEEETrans.Services
|     |     |     |     |     |     |     |     | [86] C.Liu,Z.Cai,B.Wang,Z.Tang,andJ.Liu,‘‘Aprotocol-independent |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Comput.,vol.15,no.1,pp.294–307,Jan.2022.
|                    |       |          |                   |     |     |             |     | container | network | observability | analysis | system | based | on eBPF,’’ | in  |
| ------------------ | ----- | -------- | ----------------- | --- | --- | ----------- | --- | --------- | ------- | ------------- | -------- | ------ | ----- | ---------- | --- |
| [67] I. Tzanettis, | C.-M. | Androna, | A. Zafeiropoulos, |     | E.  | Fotopoulou, | and |           |         |               |          |        |       |            |     |
Proc.IEEE26thInt.Conf.ParallelDistrib.Syst.(ICPADS),Dec.2020,
| S. Papavassiliou,                                                    |     | ‘‘Data | fusion of | observability | signals | for | assisting |             |     |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | ------ | --------- | ------------- | ------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| orchestrationofdistributedapplications,’’Sensors,vol.22,no.5,p.2061, |     |        |           |               |         |     |           | pp.697–702. |     |     |     |     |     |     |     |
Mar.2022. [87] M.Abranches,O.Michel,E.Keller,andS.Schmid,‘‘Efficientnetwork
[68] P.-J. Quéval and U. Zdun, ‘‘Extracting the architecture of monitoringapplicationsinthekernelwitheBPFandXDP,’’inProc.IEEE
Conf.Netw.FunctionVirtualizationSoftw.DefinedNetw.(NFV-SDN),
| microservices: |     | An approach | for explainability |     | and | traceability,’’ | in  |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ------------------ | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nov.2021,pp.28–34.
Proc.Eur.Conf.Softw.Archit.Cham,Switzerland:Springer,Jan.2023,
pp.346–353. [88] C.Cassagnes,L.Trestioreanu,C.Joly,andR.State,‘‘TheriseofeBPF
[69] J.Grohmann,M.Straesser,A.Chalbani,S.Eismann,Y.Arian,N.Herbst, fornon-intrusiveperformancemonitoring,’’inProc.NOMS-IEEE/IFIP
N.Peretz,andS.Kounev,‘‘SuanMing:Explainablepredictionofperfor- Netw.Oper.Manage.Symp.,Apr.2020,pp.1–7.
mancedegradationsinmicroserviceapplications,’’inProc.ACM/SPEC [89] P.G.Kannan,S.M.Gupta,D.Behl,E.Raichstein,andJ.Takvorian,
Int.Conf.Perform.Eng.,Apr.2021,pp.165–176. ‘‘Designingalightweightnetworkobservabilityagentforcloudapplica-
tions,’’inProc.Int.Conf.PassiveAct.Netw.Meas.Cham,Switzerland:
| [70] R. | Brondolin | and M. | D. Santambrogio, |     | ‘‘A black-box |     | monitor- |     |     |     |     |     |     |     |     |
| ------- | --------- | ------ | ---------------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ing approach to measure microservices runtime performance,’’ ACM Springer,Jan.2024,pp.262–276.
Trans.Archit.CodeOptim.,vol.17,no.4,pp.1–26,Dec.2020. [90] M. Panahandeh, A. Hamou-Lhadj, M. Hamdaqa, and J. Miller, ‘‘Ser-
[71] G. Yu, P. Chen, Y. Li, H. Chen, X. Li, and Z. Zheng, ‘‘Nezha: viceAnomaly: An anomaly detection approach in microservices using
Interpretable fine-grained root causes analysis for microservices distributed traces and profiling metrics,’’ J. Syst. Softw., vol. 209,
on multi-modal observability data,’’ in Proc. 31st ACM Joint Mar.2024,Art.no.111917.
Eur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,Nov.2023,pp.553–565. [91] T.Shiraishi,M.Noro,R.Kondo,Y.Takano,andN.Oguchi,‘‘Real-time
monitoringsystemforcontainernetworksintheeraofmicroservices,’’
| [72] S. | Lee and | J. Nam, | ‘‘Kunerva: | Automated |     | network | policy |     |     |     |     |     |     |     |     |
| ------- | ------- | ------- | ---------- | --------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
discovery framework for containers,’’ IEEE Access, vol. 11, in Proc. 21st Asia–Pacific Netw. Oper. Manage. Symp. (APNOMS),
| pp.95616–95631,2023. |     |     |     |     |     |     |     | Sep.2020,pp.161–166. |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
[73] K.Ranjitha,P.Tammana,P.G.Kannan,andP.Naik,‘‘Acaseforcross- [92] J.LevinandT.A.Benson,‘‘ViperProbe:Rethinkingmicroserviceobserv-
domain observability to debug performance issues in microservices,’’ abilitywitheBPF,’’inProc.IEEE9thInt.Conf.CloudNetw.(CloudNet),
in Proc. IEEE 15th Int. Conf. Cloud Comput. (CLOUD), Jul. 2022, Nov.2020,pp.1–8.
pp.244–246.
|     |     |     |     |     |     |     |     | [93] R.Rangaiyengar,R.Komondoor,andR.K.Medicherla,‘‘Multi-layer |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[74] D.Monteiro,Y.Yu,A.Zisman,andB.Nuseibeh,‘‘Adaptiveobservability observability for fault localization in microservices based systems,’’
forforensic-readymicroservicesystems,’’IEEETrans.ServicesComput., in Proc. IEEE Int. Conf. Softw. Anal., Evol. Reengineering (SANER),
| vol.16,no.5,pp.3196–3209,Sep./Oct.2023. |     |     |     |     |     |     |     | Mar.2023,pp.733–737. |     |     |     |     |     |               |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | ------------- | --- |
| 72038                                   |     |     |     |     |     |     |     |                      |     |     |     |     |     | VOLUME13,2025 |     |

U.Faseehaetal.:ObservabilityinMicroservices:AnIn-DepthExplorationofFrameworks
[94] V. Raj and G. P. Chander, ‘‘Monitoring of microservices architecture FAHAD SAMAD received the Ph.D. degree
basedapplicationsusingprocessmining,’’inProc.9thInt.Conf.Com- from RWTH Aachen University (specialization:
put.Sustain.GlobalDevelop.(INDIACom),Mar.2022,pp.486–494. networksecurity).Heiseagerlylookingforward
[95] C.H.ZhangandM.OmairShafiq,‘‘Areal-time,scalablemonitoringand to academic and industrial opportunities and
useranalyticssolutionformicroservices-basedsoftwareapplications,’’in challengesahead.Hisobjectiveisto beactively
Proc.IEEEInt.Conf.BigData(BigData),Dec.2022,pp.6125–6134.
involvedandtoalwaysplayamajorroleinshaping
[96] N.D.KeniandA.Kak,‘‘Adaptivecontainerizationformicroservices
thetechnicallyadvancedsocietyusingtheskillset
indistributedcloudsystems,’’inProc.IEEE17thAnnu.Consum.Com-
thathehasdevelopedoverthepastseveralyears.
mun.Netw.Conf.(CCNC),Jan.2020,pp.1–6.
[97] D.ErnstandS.Tai,‘‘Offlinetracegenerationformicroserviceobservabil-
ity,’’inProc.IEEE25thInt.EnterpriseDistrib.ObjectComput.Workshop
(EDOCW),Oct.2021,pp.308–317.
[98] D.CalaveraandL.Fontana,LinuxObservabilityWithBPF:Advanced
| Programming |     | for Performance |     | Analysis | and Networking. |     | Sebastopol, |     |     |     |     |
| ----------- | --- | --------------- | --- | -------- | --------------- | --- | ----------- | --- | --- | --- | --- |
CA,USA:O’ReillyMedia,2019.
[99] S.Baškarada,V.Nguyen,andA.Koronios,‘‘Architectingmicroservices:
Practicalopportunitiesandchallenges,’’J.Comput.Inf.Syst.,vol.60,
no.5,pp.428–436,Sep.2020.
| [100] D. Gorige, | E.           | Al-Masri,     | S. Kanzhelev, |         | and H.            | Fattah,  | ‘‘Privacy-risk |     |     |     |     |
| ---------------- | ------------ | ------------- | ------------- | ------- | ----------------- | -------- | -------------- | --- | --- | --- | --- |
| detection        | in           | microservices | composition   |         | using distributed |          | tracing,’’ in  |     |     |     |     |
| Proc.            | IEEE Eurasia |               | Conf. IoT,    | Commun. | Eng.              | (ECICE), | Oct. 2020,     |     |     |     |     |
pp.250–253.
| [101] N. Mateus-Coelho, |                  |     | M. Cruz-Cunha,   |     | and L.        | G. Ferreira, | ‘‘Secu-   |     |     |     |     |
| ----------------------- | ---------------- | --- | ---------------- | --- | ------------- | ------------ | --------- | --- | --- | --- | --- |
| rity                    | in microservices |     | architectures,’’ |     | Proc. Comput. | Sci.,        | vol. 181, |     |     |     |     |
pp.1225–1236,Jul.2021.
| [102] Y. He, | R. Guo, | Y. Xing, | X. Che, | K.  | Sun, Z. Liu, | K. Xu, | and Q. Li, |     |     |     |     |
| ------------ | ------- | -------- | ------- | --- | ------------ | ------ | ---------- | --- | --- | --- | --- |
‘‘Crosscontainerattacks:ThebewilderedeBPFonclouds,’’inProc.32nd
USENIXSecur.Symp.(USENIXSecur.),2023,pp.5971–5988.
[103] M.Driss,D.Hasan,W.Boulila,andJ.Ahmad,‘‘MicroservicesinIoT SEHAR ZEHRA receivedtheMasterofScience
security:Currentsolutions,researchchallenges,andfuturedirections,’’ degreeincomputersciencefromtheSirSyedUni-
Proc.Comput.Sci.,vol.192,pp.2385–2395,Jul.2021. versityofEngineeringandTechnology,in2012.
[104] A.HannousseandS.Yahiouche,‘‘Securingmicroservicesandmicroser- She is currently pursuing the Ph.D. degree in
| vice | architectures: | A   | systematic | mapping | study,’’ | Comput. | Sci. Rev., |          |                  |          |            |
| ---- | -------------- | --- | ---------- | ------- | -------- | ------- | ---------- | -------- | ---------------- | -------- | ---------- |
|      |                |     |            |         |          |         |            | computer | science with the | National | University |
vol.41,Aug.2021,Art.no.100415.
|     |     |     |     |     |     |     |     | of Computer | and Emerging      | Sciences       | (FAST),     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | -------------- | ----------- |
|     |     |     |     |     |     |     |     | Karachi,    | Pakistan. She has | amassed        | 20 years of |
|     |     |     |     |     |     |     |     | teaching    | experience and    | is a full-time | Assistant   |
UMMAYFASEEHA(Member,IEEE)iscurrently
|     |     |     |     |     |     |     |     | Professor | with the Khursheed | Government | Girls |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------ | ---------- | ----- |
pursuingthePh.D.degreewiththeDepartmentof
ComputerScience,NationalUniversityofCom- Degree College, Karachi. Over her extensive
puter and Emerging Sciences (FAST), Karachi, teachingcareer,shehascontributedsignificantlytoherstudents’academic
Pakistan. She is an Assistant Professor with and professional growth, supervising numerous projects, and teaching
|              |            | Jinnah | University  |             | for Women,      | Karachi.      | With a variouscoursesacrossthecurriculum. |     |     |     |     |
| ------------ | ---------- | ------ | ----------- | ----------- | --------------- | ------------- | ----------------------------------------- | --- | --- | --- | --- |
|              |            | strong | commitment  |             | to academic     | excellence,   | she                                       |     |     |     |     |
|              |            | has    | been        | involved    | in various      | research      | projects                                  |     |     |     |     |
|              |            | and    | has made    | significant |                 | contributions | to the                                    |     |     |     |     |
|              |            | field  | of computer |             | science through |               | her teaching                              |     |     |     |     |
| and research | endeavors. | Her    | research    | interests   | include         | machine       | learning,                                 |     |     |     |     |
embeddedsystems,SDN,NFV,eBPF,andtheInternetofThings.
|     |     | HASSAN |     | JAMIL | SYED received | the | bachelor’s |     |     |     |     |
| --- | --- | ------ | --- | ----- | ------------- | --- | ---------- | --- | --- | --- | --- |
degreeinelectricalengineeringfromtheQuaid-
e-AwamUniversityofEngineering,Sciences,and
|     |     | Technology, |        | Nawabshah, | Pakistan, |        | in 2003, the  |     |     |     |     |
| --- | --- | ----------- | ------ | ---------- | --------- | ------ | ------------- | --- | --- | --- | --- |
|     |     | master’s    | degree | in         | personal  | mobile | and satellite |     |     |     |     |
communicationfromtheUniversityofBradford,
U.K.,in2008,andthePh.D.degreeincomputer
sciencefromtheUniversityofMalaya,Malaysia,
|     |     | in  | 2019.     | After completing |      | his Ph.D.,     | he was |     |     |     |     |
| --- | --- | --- | --------- | ---------------- | ---- | -------------- | ------ | --- | --- | --- | --- |
|     |     | an  | Assistant | Professor        | with | the Department | of     |     |     |     |     |
Computer Sciences, National University of Computer and Emerging HAMZAAHMEDiscurrentlypursuingthePh.D.
Sciences, Karachi, Pakistan, from August 2019 to June 2022. He was a degree in computer science with the National
SeniorLecturerwiththeFacultyofComputingandInformatics,Universiti University of Computer and Emerging Sciences
MalaysiaSabah(UMS),Sabah,Malaysia,fortwoyears.Healsoworked (FAST), Karachi, Pakistan. He has a rich back-
with WorldCall Telecom Ltd., Karachi, as a Network Engineer for two groundinacademia,havingservedasaLecturer
years,andwiththeFacultyofEngineeringScienceandTechnology,Iqra withFASTUniversityforfouryearsbeforetran-
University, Karachi, for four years. He is currently a Senior Lecturer sitioning to teach A-level students with Karachi
withtheSchoolofTechnology,AsiaPacificUniversityofInnovationand Grammar School for two years. Alongside his
Technology(APU),KualaLumpur,Malaysia.Throughouthiscareer,hehas Ph.D.studies,heisactivelyinvolvedinteachingas
supervisedseveralPh.D./M.S.thesis/finalyearprojectsandtaughtcoursesin aVisitingFacultyMemberatvariousuniversities.
theelectronics,telecommunication,andcomputersciencedepartments.His His extensive experience in education has allowed him to contribute
researchinterestsincludecloudcomputing,cybersecurity,SDN,NFV,eBPF, significantlytotheacademicandprofessionaldevelopmentofhisstudents.
andtheInternetofThings.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     | 72039 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |