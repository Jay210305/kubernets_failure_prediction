794 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
XPLOG: A Dynamic Observability Framework for
Distributed Sandboxed Microservices
UtkalikaSatapathy ,Member,IEEE,HarshBorse ,RajatBachhawat ,NehaDalmia ,
SubhrenduChattopadhyay ,andSandipChakraborty ,SeniorMember,IEEE
Abstract—Runtimeapplicationobservabilityiscrucialnotonly theDevOpsphilosophyhassignificantlyimprovedapplication
forsystemprovenancebutalsofortheorchestrationofdeployed development,deployment,andmanagement.Unlikemonolithic
microservices in dynamic sandboxed distributed computing en- applications, microservices divide functionality into indepen-
vironments. Also, log extraction and aggregation in highly dis-
dent, manageable, and easily deployable components, driving
tributedandsandboxedenvironmentsposesignificantchallenges,
a widespread shift from monolithic to microservice-based de-
especiallywhenpreservingthecausalorderoftheeventstriggered
by different asynchronous microservices running over multiple signs. However, this distributed paradigm also introduces new
hosts.However,ensuringcausallyconsistentloggingofapplication operational challenges. As IT infrastructure becomes increas-
events is challenging, although it is vital for continuously trac- ingly heterogeneous, spanning edge computing, cloud-native
ing and profiling the underlying platform. This paper proposes deployments,andIndustrialInternetofThings(IIoT)configura-
XPLOG,ascalable,pluggable,easilydeployable,anddynamicrun-
tions,comprehensivemonitoringandobservabilityareessential.
timeobservabilityframeworkfordistributedsandboxedcomput-
While monitoring tracks predefined metrics, logs, and symp-
ing platforms that leverages the capability of extended Berkeley
toms,observability[1],[2]providesthecontextualunderstand-
Packet Filters (eBPF) to intercept system-level events within the
hostwhilecapturingandamalgamatingrelevantapplicationand ingrequiredtoinvestigateandidentifyrootcausesbyanalyzing
system logs to produce globally causally-consistent log streams. system behavior and interactions. Traditional monitoring and
Through qualitative and quantitative analysis, we observe that observabilitytoolsareofteninadequateforthedynamicnature
XPLOGsignificantlyimproveslogrichnesswithminimumsystem ofmicroservicesandrapiddeploymentcycles,underscoringthe
overhead while preserving the causality of log-generating events
need for advanced observability frameworks in cloud-native
acrossmultiplemicroservices.
distributed environments to improve root cause analysis and
Index Terms—Runtime observability, causally-consistent logs, reduce metrics such as Mean Time To Repair or Mean Time
distributedprovenancetracking. ToRecovery(MTTR).
Building on the challenges of monitoring and observabil-
I. INTRODUCTION ityindistributedcloud-nativesystems,general-purposesyscall
CLOUD-NATIVEtechnologieshavetransformedapplica- telemetry frameworks such as Sysdig [3], SysFlow [4], and
eAudit[5]providevaluablesystem-levelvisibilitybutfallshort
tiondevelopmentbyenablingscalable,dynamic,anddis-
incapturingdistributedcausalityandbridgingapplication-and
tributed IT infrastructure. Built on core components such as
OS-layercontexts.Forinstance,Sysdig[3]enablesrichper-host
containers, microservices, and immutable infrastructure, these
syscalltracingwithcontainerawareness,yetitlacksinter-host
architectures create a robust, maintainable, and loosely cou-
orderingguaranteesandreliesonlyontimestamps.SysFlow[4]
pled ecosystem that, when combined with automation, allows
addresses log volume by summarizing syscall data into flow
frequent and predictable changes with minimal effort. The
Cloud Native Computing Foundation1 (CNCF) aims to make records, but this aggregation discards fine-grained causal re-
lationships, limiting its effectiveness for deep debugging and
cloud-nativecomputingubiquitousandaccessibleacrossindus-
rootcauseanalysisinmulti-hostdeployments.Similarly,eAu-
tries. In particular, integrating microservice architecture with
dit[5]supportscomprehensivesyscallmonitoring,butitsscope
remainsconfinedtosingle-hostOS-levelauditingwithoutcon-
Received20February2025;revised15August2025;accepted11September
2025.Dateofpublication13October2025;dateofcurrentversion5February tainerorcloud-nativeawareness.Theselimitationshighlightthe
2026.ThisworkwassupportedbytheIndiraGandhiCenterforAtomicResearch need for an observability framework that preserves both intra-
(IGCAR).(Correspondingauthor:SandipChakraborty.)
and inter-host causality while enabling end-to-end tracing of
Utkalika Satapathy, Harsh Borse, and Sandip Chakraborty are with the
eventchainsacrossmicroservices.
DepartmentofComputerScienceandEngineering,IndianInstituteofTech-
nology, Kharagpur 721302, India (e-mail: utkalika.satapathy01@gmail.com; One critical requirement for developing an observability
harshzf2@gmail.com;sandipc@cse.iitkgp.ac.in). frameworkistocollatethelogmessagesfromrunningmicroser-
Rajat Bachhawat and Neha Dalmia are with Quadeye, Gurugram
vicesandtheunderlyinghostOSinameaningfulmanner,which
122002, India (e-mail: rbachhawat.96@gmail.com; nehadalmia002@gmail.
com). notonlycapturestheeventsexecutedbyvariousmicroservices
Subhrendu Chattopadhyay is with the Thapar Institute of Engineering butalsoshouldpreservetheircausalorexecutionorder[6],[7].
and Technology (TIET), Patiala 147004, India (e-mail: subhrendu.subho@ Thesecollatedorder-preservinglogs,calledcausally-consistent
gmail.com).
log stream, help better analyze the root cause. For runtime
DigitalObjectIdentifier10.1109/TSC.2025.3612900
1https://www.cncf.io/(Accessed:2025/10/0310:50:39) observability, the platform can apply an event-sequence-based
1939-1374©2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligenceandsimilartechnologies.
Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore. Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 795
filter to the generated log streams, which can extract the nec- is CPU core-specific; therefore, containers pinned in different
essary information more quickly without needing to parse the cores may provide different timestamps [20], [21]. (ii) The
whole log. Also, the causally consistent log messages help to synchronizationprimitivesmayfailtopreservetheorderingof
create the provenance graph [8], [9] dynamically, which can the events when collating logs generated from different user
further be used for system vulnerability detection [10], [11], and kernel threads. For example, the threads that collect logs
root-cause analysis [12], [13], [14], etc. Our paper aims to from individual microservices may need to use a lock while
address this gap by exploring the open research challenges collatingthelogmessagestoavoidwrite-writesynchronization
relatedtoobservabilityindistributedmicroservicearchitecture. conflicts. However, the locking order may not align with the
Research Challenges: Designing an observability frame- log generation order, potentially resulting in out-of-sequence
work over a distributed sandboxing environment (i.e., mostly logs. (iii) Modern systems are capable of ensuring intra-host
lightweightcontainers)hasthefollowingchallenges. logconsistencytosomeextent[22],[23],butdistributedsetups
• Challenge (cid:2)1. Relevant Log Extraction for Multi-Host introduce challenges such as inter-host synchronization and
Sandboxed Applications: Sandboxing platforms (e.g., Docker, eventordering.
Kubernetes) abstract application execution, making it difficult Therefore,thesechallengeshighlighttheneedtodevelopad-
to access fine-grained application behavior. Existing solutions vancedtechniquesthatpreservecausalconsistencyindistributed
(e.g., Dyninst [15], Angr [16], [17]) rely on static or dy- environments,enablingmeaningfulobservabilityandeffective
namic binary analysis to extract relevant logging information. provenanceanalysis.
However,suchmethodsareimpracticalindistributedenviron- OurContributions:ThispaperpresentsXPLOG,aplatform-
ments because (i) application binaries are often proprietary or agnosticdynamicobservabilityframeworkthatdoesnotrequire
inaccessibleinthird-partyormulti-tenantdeployments,and(ii) applicationorplatforminstrumentationandcanbeusedforboth
binaryanalysisisarchitecture-dependent,requiringknowledge runtime analysis of the system behavior as well as periodic or
of instruction sets or program formats. Although intermediate offlinesystemprovenanceanalysis.Ourkeycontributionstothis
representations (e.g., LLVM IR, VEX) can aid cross-platform paperareasfollows.
analysis, deploying and maintaining these at scale across het- • Contribution (cid:2)1. Development of a grey-box observabil-
erogeneous hosts is infeasible. Thus, rather than inspecting ity framework for multi-host sandboxed applications: We de-
application internals, we need a grey-box approach that ex- velop the first-of-its-kind observability framework for sand-
tracts meaningful logs directly from running microservices, boxeddistributedplatforms.Itmonitorscontainerizedmicroser-
relying solely on application-generated logs without visibility vices running across multiple physical or virtual hosts, gener-
intosourcecode. atingcausally-consistent,context-awarelogswithoutrequiring
• Challenge (cid:2)2. Partial Visibility of Application and System applicationorplatforminstrumentation.Atitscore,XPLOGuses
Logs: The sandboxing environment uses separate namespaces eBPF [24], [25], [26], [27] to inject customized byte-codes to
fromthebasekernel;Theuseofseparatenamespacesinsand- specifickernelhookpointsformonitoringOS-leveleventswith
boxingenvironmentsisolatesprocesshierarchiesfromthebase zeromodificationintheOSkernel.
kernel,leadingtofragmentedlogvisibility.Existingtoolssuch •Contribution(cid:2)2.Causality-AwareCollationofSystemand
asOmegaLog,Logstash,andFluentd[1],[18],[19]can Application Logs: We develop novel methods for preserving
eitheraccessbasekernelsystemlogs(whenexecutedonthehost) causality during the log collection from multiple sandboxed
orcontainer-specificapplicationlogs(whenexecutedwithinthe microservices running over multiple hosts while handling the
container), but not both. Consequently, system logs often lack abovementioned challenges. The core of our approach utilizes
application-specificcontext,suchasuserinteractionsorthread eBPFring buffers to develop a method for making the syscalls
behaviors,andapplicationlogsfailtoreflectunderlyingresource atomic. It thus ensures that all the log messages relevant to a
usage or kernel-level interactions. This separation necessitates syscall are observed together at the generated log streams. At
independentconfigurationofloggingtoolsonboththehostand runtime,itdynamicallymapsapplicationlogstosyscalllogsin
containers,resultinginlimitedvisibility.Thisseparationcreates an application-agnostic manner, ensuring consistent causally-
apartialviewofthesystem,makingitchallengingtocorrelate orderedloggeneration.
logsacrossnamespaces. •Contribution(cid:2)3.Implementationandthoroughevaluation:
•Challenge(cid:2)3.PreservingCausalConsistencyAcrossEvent Weopen-sourcetheimplementationofXPLOG,evaluateitwith
Logs:Onecrucialaspectofsystemobservabilityistomeaning- a benchmark DeathStarBench [32] social media applica-
fully combine the application logs with the system-generated tion with 30 microservices, each with 3–5 replicas, spawning
logstopreserveeachapplicationthread’scontextandresource over 10-30 different hosts, and compare its performance with
access patterns over the host OS kernel. However, combin- Tracee [33], an eBPF-based widely-used enterprise applica-
ing application and system logs in a distributed microservice tion for platform log management. We observe that XPLOG-
environment requires maintaining causal consistency, which generated log reduces the disorders among the log entries and
is challenging due to parallel execution and heterogeneity generatesacausally-orderedlogforparallellyrunningmicroser-
across hosts. Therefore, we must combine the logs generated vices with varying numbers (10,000 to 30,000) of concurrent
from the running microservices with the logs from the host requests from different service endpoints the benchmark pro-
OS kernel. Traditional ways of aggregating logs based on vides. The logs (ordered logs) generated are comparable to
timestampsdonotworkforthefollowingreasons.(i)Thesystem thoseobtainedfromrunningthemicroservicessequentiallyona
timestamp is typically taken from CLOCK_MONOTONIC (the singlehost.Further,weobservethatXPLOGconsumesminimal
absoluteelapsedwall-clocktimesincethesystemboot),which resourceswhenrunningasabackgroundloggingservicewhile
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore. Restrictions apply.

796 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
providingsignificantlymorecontextualinformation,whichcan collectthelogsatahighlevelandlackthegranularityneeded
helpinefficientsystemprovenance. to capture the lower-level system events within the distributed
|     |     |                 |     |     |     |     |     | environment.     | Moreover, | these tools     | are   | licensed | and are nei- |
| --- | --- | --------------- | --- | --- | --- | --- | --- | ---------------- | --------- | --------------- | ----- | -------- | ------------ |
|     |     |                 |     |     |     |     |     | ther open-source | nor       | cost-effective. | Also, | research | work like    |
|     |     | II. RELATEDWORK |     |     |     |     |     |                  |           |                 |       |          |              |
lprof[60]andStitch[61]usesruntimeapplicationlogstorecon-
Several research efforts have explored various aspects of structtheexecutionflowofrequestsindistributedapplications.
provenancedataextraction,provenancetracking,auditlogging,
However,lprofperformsstaticbinaryanalysis,andStitchrelies
loganalysis,andcausalityanalysis. onstructuredapplicationlogswithinstrumentationinthecode
foranalysis.Theyaremoresuitablechoiceforlogmanagement
A. LogginginDistributedCloudInfrastructure ratherthanloganalysisbecausethecollectedlogslackcontext
andcausality.
| Existingsystemloggingapproaches |                |      |           | primarilyfocusoncol- |                |       |       |                       |     |     |     |     |     |
| ------------------------------- | -------------- | ---- | --------- | -------------------- | -------------- | ----- | ----- | --------------------- | --- | --- | --- | --- | --- |
| lecting                         | effective logs | for  | system    | provenance           | [34],          | [35], | [36], |                       |     |     |     |     |     |
|                                 |                |      |           |                      |                |       |       | C. UseofeBPFinLogging |     |     |     |     |     |
| [37]. Many                      | of these       | rely | on custom | kernel               | modules—either |       |       |                       |     |     |     |     |     |
static[1],[38],[39],proxy-based[2],[40],orLoadableKernel
|     |     |     |     |     |     |     |     | On the | other hand, | eBPFhas been | widely | studied | to extend |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ------------ | ------ | ------- | --------- |
Module (LKM)-based [41]—to merge application and kernel thekernel functionalityfromseveral perspectives, likeforfast
logsintoprovenancegraphs.Statichookingrequiresrecompil- packetprocessing[62],networkfunctionmanagement[63],ac-
ingtheentirekernel,makingitfragileandhardtomaintain,while
celeratingdistributedprotocols[64],in-kernelstoragemanage-
| proxy and | LKM-based | methods |     | attach | only at | specific | hook |     |     |     |     |     |     |
| --------- | --------- | ------- | --- | ------ | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
ment[65],path-awareTCP[66],containernetworkobservabil-
points, limiting their scalability in large microservice deploy- ity[29],[67],etc.Givenitswide-scaleadaptabilityforvarious
ments.LKM-basedsolutionsarealsobrittleagainstkernelup- applicationsonsystemobservability,eBPFcanmeettherequire-
grades[42].Beyondkernelhooks,severalworksattempttoen-
|     |     |     |     |     |     |     |     | ments for | the development | of a | fast logging | mechanism | for |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | ---- | ------------ | --------- | --- |
hancesystemobservabilitythroughlogprocessingandanomaly systemprovenancebydynamicallydeployinganobservability
detection. For example, SLEUTH [43] reconstructs attack sce- moduletocombinetheapplicationlogsfromthemicroservices
nariosinrealtimeusingmemory-baseddependencygraphsof
andthekernelsystemlogstogeneratetheprovenancegraphon
auditlogs,[44]combineslogparsingandmachinelearningto
thefly.Asdiscussedearlier,widelyadoptedstate-of-the-artlog-
detectruntimeproblemsinconsolelogs,andELT[45]leverages gingmechanismslikefluentd[19],Logstash[18],Tracee[33],
fine-andcoarse-grainedlogfeaturesforanomalydetection. Tetragon [68] etc., are not suitable for multi-layer logging.
| Provenance | tracking | has | also been | widely | studied |     | for both |     |     |     |     |     |     |
| ---------- | -------- | --- | --------- | ------ | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
Whereasseveralworksintheliteraturehavefocusedonefficient
monolithic[1],[38],[40],[46]andmicroservice-basedapplica- systemauditing[5],[40],[69],theyhaveprimarilyfocusedon
tions[2],[39],[41].ApproachessuchasPROV2R[47]capture developing a logging mechanism for a single-host monolithic
| provenance | from unstructured |     | processes |     | via record/replay |     | and |     |     |     |     |     |     |
| ---------- | ----------------- | --- | --------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
application.Therehavebeenseveralworksintheliterature[70],
tainttracking,thoughtheyrequireinstrumentation;Scippa[48]
[71],[72],whichhavefocusedondistributedloggingofevents;
extendsAndroidIPCtodetectattacks;Hi-Fi[49]leveragesthe however, they use specific techniques and resources like in-
Linux Security Modules (LSM) framework for whole-system memory databases, far memory and remote memory archi-
provenance;[50]introducesdocumentprovenanceinclouden-
|     |     |     |     |     |     |     |     | tecture, etc., | and are | not suitable | for sandboxed |     | applications. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ------------ | ------------- | --- | ------------- |
vironments;andSmartProvenance[51]employsblockchainand Further,thesetoolsfailtogeneratecausally-consistentlogsfrom
smartcontractsforprivacy-preserving,access-controlledprove- multiplemicroservices.Notably,thisisoneofthevitalrequire-
| nance with | trust enforcement. |     | Despite |     | these advances, |     | chal- |     |     |     |     |     |     |
| ---------- | ------------------ | --- | ------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
mentsforruntimeprovenanceoverahighlydistributedmicroser-
lengesremain,includingdependencyexplosion—whereexces- vicearchitecture,whichourproposedobservabilityframework
| sivedependenciescomplicateanalysisandincreaseoverhead— |     |     |     |     |     |     |     | handles. |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
andinstrumentationrequirements,whichareresource-intensive
| and impractical | for | enterprise | deployment. |     | Recent | works | on  |      |                                   |     |     |     |     |
| --------------- | --- | ---------- | ----------- | --- | ------ | ----- | --- | ---- | --------------------------------- | --- | --- | --- | --- |
|                 |     |            |             |     |        |       |     | III. | PROBLEMSTATEMENTANDSYSTEMOVERVIEW |     |     |     |     |
causality[28],[31],[52],[53],[54]attempttogobeyondprove-
nancebylinkingevents,butmostrelyonlyontemporalrelation- Our proposed observability framework XPLOG uses a
shipsratherthantruecausalinference.Forinstance,Falcon[31] distributed log collection architecture to generate causally-
analyzesthecontextofnetworkrequestsbutlackscontent-aware consistent log message streams from running microservices
analysis of storage I/O, while CauseInfer [55] focuses mainly over sandboxed distributed platforms. In this section, we first
onnumericaldataandcannothandlenon-numericalinformation formallydefinetheconceptofCausally-consistentlogmessage
suchaslogeventsorconfigurationdata. streamandthendiscussthebroadoverviewofXPLOG.
| B. ObservabilityinDistributedSystems |     |     |     |     |     |     |     | A. ProblemStatement |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
The lack of visibility into microservice applications run- Leteiandejbetwolog-generatingapplicationevents(events
ningascontainersindistributedcloudplatformsisapersistent thatgeneratelogmessages,likeafunction/procedurecall,com-
challenge. This has led to the development of various tools, puting loops, branching, etc.). We say ei happens-before ej,
fromobservabilityframeworktologmanagementandanalysis denotedasei ≺ej,ifoneofthefollowingconditionsholds.
solutionsforcloudinfrastructureandcontainersDatadog[56], 1) ei and ej execute on the same microservice and
|     |     |     |     |     |     |     |     | T(ei | )<T(ej ), | T(e) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---- | --- | --- | --- |
Dynatrace [57], New Relics [58], Aqua [59] to enhance ob- where indicates the local clock
servability and debugging. However, these solutions majorly (i.e.,CLOCK_MONOTONIC)readingforanevente.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 797
TABLEI
RECENTRESEARCHWORKFORLOGGINGFRAMEWORKSCOMPAREDTOXPLOG
TABLEII providetheexecutablefilelocationandthefilesaccessedbythe
LOGINFOCATEGORIESANDFIELDS
callerprogram.
|     |     |     |     |     |     |     | XPLOG | utilizes | eBPFto | deploy | the | logging | module | within |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------ | ------ | --- | ------- | ------ | ------ |
thehostOSkernelinanapplication-agnosticmannerandgen-
L.
|     |     |     |     |     |     |     | erates the  | causally-consistent |           |               | log message | stream |        | Notably,  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | --------- | ------------- | ----------- | ------ | ------ | --------- |
|     |     |     |     |     |     |     | eBPFenables |                     | injection | of customized |             | codes  | called | probes to |
specifickernelhookpoints,calledthetracepoints,andthuscan
|     |     |     |     |     |     |     | extend | the capabilities |     | of the | kernel | safely and | efficiently | at  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------------- | --- | ------ | ------ | ---------- | ----------- | --- |
runtimewithoutrequiringanychangestothekernelsourcecode
orloadingthekernelmodules.Togeneratecausally-consistent
logsacrossmicroservicesrunningovermultiplehostmachines,
2) eiandejexecuteondifferentmicroservicesandeitriggers
XPLOGemploysatwo-stepapproach:(1)first,itensurescausal
| (causes)ej   | (forexample,ei |                                    | isasendcallonanetwork |     |     |     |               |        |               |              |           |     |              |           |
| ------------ | -------------- | ---------------------------------- | --------------------- | --- | --- | --- | ------------- | ------ | ------------- | ------------ | --------- | --- | ------------ | --------- |
|              |                |                                    |                       |     |     |     | consistency   | across | the           | log messages | generated |     | from         | microser- |
| socket,andej |                | isthecorrespondingreceivecallatthe |                       |     |     |     |               |        |               |              |           |     |              |           |
|              |                |                                    |                       |     |     |     | vices running |        | over a single | host,        | and then, | (2) | it preserves | the       |
otherendofthesocket).
≺ej ≺ek,thenei ≺ek. causal-consistency during log collation from multiple hosts.
| 3) ifei | andej |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LetL(e)bethelogmessagescorrespondingtotheapplication Notably, while we can use the concept of logical clocks from
thestandarddistributedsystemsliterature(likeaper-hostvector
| event e. | Let E be the | set of | events generated |     | over all | the mi- |     |     |     |     |     |     |     |     |
| -------- | ------------ | ------ | ---------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
clock[75])tosolve(2),thefirstoneismuchmorechallengingas
croservicesforanapplication,andLbethecollatedlogmessage
streamfromalltherunningmicroservices.WecallLcausally- thecontainersuseadifferentnamespacethanthehostOSkernel.
|                                                      |     |     |     |     |     |     | Further, | the application |     | logs generated |     | from the | containerized |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | -------------- | --- | -------- | ------------- | --- |
| consistentifandonlyifforanytwoapplicationeventsei,ej |     |     |     |     |     | ∈E  |          |                 |     |                |     |          |               |     |
microservicesuseseparatethreadexecutioncontextsatvarious
| andthecorrespondinglogmessagesL(ei |     |     |     | ),L(ej | )∈L, |     |             |               |     |     |       |              |          |     |
| ---------------------------------- | --- | --- | --- | ------ | ---- | --- | ----------- | ------------- | --- | --- | ----- | ------------ | -------- | --- |
|                                    |     |     |     |        |      |     | namespaces. | Consequently, |     | we  | use a | novel design | approach |     |
ei ≺ej ⇐⇒L(ei )(cid:7)→L(ej ) (1) following the idea that containerized applications use syscalls
toaccessresourcesoverthehostOS,andsyscallexecutionsare
Notably, an application event ei can generate multiple log atomicoperationsinsideathreadexecutioncontext.Therefore,
| messages | (e.g., for | the same | event, | both application |     | logs and |     |     |     |     |     |     |     |     |
| -------- | ---------- | -------- | ------ | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
XPLOGmonitorssyscallexecutionsacrosstherunningthreads
| systemlogs).Inthiscontext,L(ek |     |     | )(cid:7)→L(el |     | )indicatesthatthe |     |          |      |           |     |          |               |     |          |
| ------------------------------ | --- | --- | ------------- | --- | ----------------- | --- | -------- | ---- | --------- | --- | -------- | ------------- | --- | -------- |
|                                |     |     |               |     |                   |     | over the | host | OS kernel | and | collates | the generated |     | log mes- |
L(ek )
entries of come together and sequentially precede the sages based on the syscall execution order. However, as the
| entries of | L(el ) in | the generated | log | message | stream | L. The |     |     |     |     |     |     |     |     |
| ---------- | --------- | ------------- | --- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
containerizedapplicationsuseadifferentPIDnamespacethan
causal-consistencyalsoensuresthatthelogmessagesgenerated
|     |     |     |     |     |     |     | the host | OS, there | is a | need to | map the | application |     | processes |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ------- | ------- | ----------- | --- | --------- |
frommultipleeventsdonotgetmixedupwitheachother.We withthecorrespondinghostOSprocesses.XPLOGusesvarious
| next discuss | the broad | overview | of our | proposed | observability |     |     |     |     |     |     |     |     |     |
| ------------ | --------- | -------- | ------ | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eBPFdatastructurestoaddressthis.
frameworkXPLOGtoextractthecausally-consistentlogsfrom
AsshowninFig.1,XPLOGcomprises(1)theXPLOGAgent,
therunningmicroservices.
residingwithineachhost,responsibleforensuringcausalconsis-
tencyofthelogmessagesgeneratedfrommicroservicesrunning
B. BasicWorkingPrincipleandSystemOverview
|           |             |           |     |                 |     |           | over a single |          | host, and | (2) the | XPLOG       | Collector   | that | collates |
| --------- | ----------- | --------- | --- | --------------- | --- | --------- | ------------- | -------- | --------- | ------- | ----------- | ----------- | ---- | -------- |
|           |             |           |     |                 |     |           | the log       | messages | across    | the     | hosts while | maintaining |      | causal   |
| Following | the general | principle |     | of microservice |     | architec- |               |          |           |         |             |             |      |          |
consistencyandstreamsthelogmessagestothedownstreamser-
| ture [73], | [74], we | assume | the application |     | microservices | de- |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------ | --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ployed on each host run inside individual containers. XPLOG vicesdependingontheirneeds.Consequently,variousplatforms
|          |            |           |            |     |               |      | and application |     | components | can | be attached |     | with the | XPLOG |
| -------- | ---------- | --------- | ---------- | --- | ------------- | ---- | --------------- | --- | ---------- | --- | ----------- | --- | -------- | ----- |
| captures | the system | logs from | individual |     | hosts, orders | them |                 |     |            |     |             |     |          |       |
collectorforextractingtherelevantlogmessagesandusingthem
| based on | the causal | order of | application | events | executed | over |     |     |     |     |     |     |     |     |
| -------- | ---------- | -------- | ----------- | ------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
forruntimeanalysis.Next,wediscussthefunctionalitiesofthese
| different | microservices, | and | streams | them | to the downstream |     |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
servicesinthecausally-consistentorder.Toenrichtheindividual twocomponentsindetail.
| logentries,XPLOGaddsfourcategories(see |          |               |     |       | TableII)ofinfor-  |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | -------- | ------------- | --- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mation along                           | with the | log messages. |     | Among | these categories, |     |     |     |     |     |     |     |     |     |
IV. COMPONENTSOFXPLOG
| Event | contextandTask |     | contextarehelpfultodisam- |     |     |     |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
biguatelogentriesfrommultiplePIDnamespaces.Arguments The XPLOG Agents are deployed as privileged contain-
preciselycapturethesyscallparametersrelevantfordebugging ers over the host machines, which allows them to moni-
syscalls,forensics,etc.Ontheotherhand,Artifactsfields tor the microservice logs (application-level logs) from other
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

798 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
|     |     |     |     |     | 1) Tracepoints  |         | & eBPFProbes: |       | We       | configure   | Kernel-space |         |
| --- | --- | --- | --- | --- | --------------- | ------- | ------------- | ----- | -------- | ----------- | ------------ | ------- |
|     |     |     |     |     | tracepoints     | to hook | syscall       | entry | and      | exit events | by           | execut- |
|     |     |     |     |     | ing eBPFprobes. |         | The entry     | probe | extracts | syscall     | arguments,   |         |
whiletheexitprobemonitorscontextualinformation(e.g.,task,
container,eventcontext)andartifactslikeexecutablepathand
|     |     |     |     |     | syscall return     | value. | Separate |     | probe programs |     | are developed |           |
| --- | --- | --- | --- | --- | ------------------ | ------ | -------- | --- | -------------- | --- | ------------- | --------- |
|     |     |     |     |     | for each monitored |        | syscall  | due | to variations  |     | in the        | extracted |
information.
|     |     |     |     |     | 2) eBPFMaps: |     | Themapsareusedtosharedatabetweenthe |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- |
userandthekernel-space.WeusefollowingeBPFmaps:
|     |     |     |     |     | i) pid_args_map:      |     | An      | eBPFmap    |           | data      | structure   | named     |
| --- | --- | --- | --- | --- | --------------------- | --- | ------- | ---------- | --------- | --------- | ----------- | --------- |
|     |     |     |     |     | pid_args_map          |     | is used | to collate | the       | extracted | information |           |
|     |     |     |     |     | from the tracepoints. |     | Without |            | this map, | logging   | of          | entry and |
exittracepointsseparatelyincreasestheoutputlogsizeandmay
|     |     |     |     |     | impact the  | performance. |           | The pid_args_map |       |              | is indexed | by       |
| --- | --- | --- | --- | --- | ----------- | ------------ | --------- | ---------------- | ----- | ------------ | ---------- | -------- |
|     |     |     |     |     | thread IDs, | as it        | is unique | in the           | host. | We designate |            | the com- |
binationofthreadIDandhostPIDastheXPLOGIDaidingin
Fig.1. XPLOG:UserandKernel-spaceComponents.
distinguishinghost-levelloggingwithintheXPLOGlogmessage
stream.DespitethecausalorderingoftheXPLOGgeneratedlog,
logswithinthecollatedlogmessagestreambecomeinterleaved
containers. In addition, they require capabilities such as across different hosts. Therefore, the absence of the XPLOG
CAP_BPF,CAP_SYS_ADMIN,andCAP_PERFMONtoattach ID makes it challenging to discern logs from various hosts or
|     |     |     |     |     | containers | associated | with | a request. | Each | syscall | entry | probe |
| --- | --- | --- | --- | --- | ---------- | ---------- | ---- | ---------- | ---- | ------- | ----- | ----- |
eBPFprobes.However,themonitoredmicroservicecontainers
donotneedanyadditionalprivilege.Theobservabilitylayeris placestheextractedsyscallargumentsasthevalueinthemap.
decoupledfromapplicationlogic,anditsupportsbetteropera- The syscall exit probe pops the argument from the map and
tionalsimplicityandbroadercompatibility.Theuser-spaceand generatesthehost-levelcollatedsyscalllog.Oncethehost-level
thekernel-spacecomponentsofXPLOGAgentsworkasfollows. collatedsyscalllogisgenerated,itisputintotheeBPFBufferto
|     |     |     |     |     | be polled | from the | user-space |     | component. | Consequently, |     | only |
| --- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | ---------- | ------------- | --- | ---- |
onelogwillbepushedtotheeBPFbufferatatime,ensuringse-
A. XPLOGAgent:User-SpaceComponent quentialprocessing.Thisensuresthecausalorderingassyscall
Theuser-spacecomponentofXPLOGAgentisresponsiblefor executionsareatomicoperationsinsideathreadexecutioncon-
interfacing between the Log collector and the host OS kernel. text.Moreover,theprocessensuresreutilizationofmapentries
fordifferentsyscallscalledfromasinglethread,whichreduces
Administratorscanconfigurethesystemthroughtheuser-space
component to monitor specific syscalls based on their prefer- thememoryfootprintofXPLOG.
ences.ThepackageutilizeskerneltracepointswitheBPFprobes (ii) pid_exec_map: Notably, extracting the absolute path of
to monitor the host kernel-level events. To enrich individual theprogramexecutablethattriggeredtheapplicationorsystem
log entries, XPLOG adds four categories of log information, calllogisnecessarytoensurethecausalordering.Inacomplex
as shown in Table II. Although the probe creation and other distributedapplication,havingtheabsolutepathoftheprogram
auxiliaryactivitiesareexplainedinSectionIV-Binmoredetail, executableinlogshelpsinpreciseidentificationoftheexecuted
|     |     |     |     |     | program, | which | helps in | tracing | to pinpoint |     | the location | of  |
| --- | --- | --- | --- | --- | -------- | ----- | -------- | ------- | ----------- | --- | ------------ | --- |
theuser-spacecomponentisresponsiblefortheinvocationand
management of these tracepoints. The generated event logs the executable. Although the absolute paths of the program
fromthetracepointsarestoredinaneBPFringbuffer,whichis executablesareavailableintheprocesscontrolblock(PCB),ex-
tractionrequiresdereferencingmultiplelayersofpointersinthe
| shared with | the user-space | and minimizes | the synchronization |     |     |     |     |     |     |     |     |     |
| ----------- | -------------- | ------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
overhead.Periodically,theuser-spacecomponentpolls,parses, kernelspace,whichdegradesperformance.Therefore,weusea
interprets,andsendstheeventlogstotheXPLOGCollectoras separateeBPFmapdatastructurenamedpid_exec_map.The
aggregatedhost-levellogoverTCP.Utilizingkerneltracepoints HostPIDindexesthismapandstorestheexecutablefilepathasa
value.Theentriesareaddedonlywhenanewprocessisspawned
withthehelpofthekernel-spacecomponentasdiscussednext,
especiallysyscallentryandexitevents,aneBPFprobeensures (i.e.,afork()/clone()syscallinvoked)andremovedatthe
the causal order of host-level logs within the host’s scope, timeofprocesstermination(e.g.,exit()syscall).
|              |           |                      |                 |     | 3) Host-Specific |     | eBPFRing |     | Buffer: | For multiple |     | microser- |
| ------------ | --------- | -------------------- | --------------- | --- | ---------------- | --- | -------- | --- | ------- | ------------ | --- | --------- |
| consequently | extending | this causality order | to the collated | log |                  |     |          |     |         |              |     |           |
messagestream. vices running on a host, each microservice produces its own
setofapplicationandsystemlogs.Now,thelogsgeneratedby
differentmicroservicesmaybecausallyrelated,whichXPLOG
B. XPLOGAgent:Kernel-SpaceComponent should capture. To ensure causal ordering among the inter-
Once the user-space component is configured correctly, it microservicelogs,wemaintainahost-specificeBPFringbuffer
invokesthekernel-spacecomponent.Thekernel-spacecompo- toaddressthefollowingtwochallenges.
|     |     |     |     |     | 1) Writinglogstoacommonbufferfrommultiplecontainers |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
nenthasseveralmodulesthatworktogethertoextractandorder
thelogmessagesfrombothapplicationsandthehostOSwhile executingindifferentprocessorcoresdoesnotguarantee
preservingtheeventexecutionorder. causal ordering, as the synchronization primitives may
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 799
particularlog.Furthermore,XPLOGusesanidentifier,“tagID”
frommicroserviceendpointstofilterapplicationlogsresulting
fromconcurrentrequestsandcorrespondingsystemlogsinthe
collatedlogmessagestream.
AtomicSystemEventLogging:XPLOGusesanovelapproach
foratomicsystemeventloggingtogeneratecausally-consistent
logs for the microservices running over a single host. A mi-
croservice,duringitsexecution,typicallytriggerssomesystem
Fig.2. UsingeBPFringbuffertoensurecausalorderingwhilegeneratinga
events in the kernel and generates log/debugging statements.
commonlogfile.
These log/debugging statements are written to the log file by
invokingthewrite()(orequivalent)syscall(Fig.1 (cid:2) 1 ),which
(cid:2)
triggers a syscall entry tracepoint program (Fig. 1 2 ) in the
enforce different ordering than the application event ex-
XPLOG Agent. This program populates the pid_args_map
ecution order, as discussed earlier. Therefore, the log
with the host PID & Thread ID and the syscall arguments
messagesneedtobeorderedatthetimeofexecutionofthe
(cid:2) (cid:2)
(Fig.1 3 ).Thenthesystemcallexecutes(Fig.1 4 ),andonce
underlyingwritesyscallitself,astheseareguaranteed
theexecutioniscomplete,ittriggersthesyscallexittracepoint
tobesuccessiveforagivenrequestpathway.
(cid:2)
(Fig. 1 5 ) to populate the executable file path of the event to
2) The significance of timestamps at the container level
thepid_exec_map(Fig.1 (cid:2) 6 ).Consequently,theeBPFring
diminishes when comparing the log timestamps across
bufferispopulatedwiththelogdatabyextractingthecontents
containers due to the core-specific nature of timestamps
of the pid_args_map and pid_exec_map (Fig. 1 (cid:2) 7 ).
obtained using CLOCK_MONOTONIC, lacking a global
Thus, for each pair of consecutive application events that are
clock. Consequently, achieving total ordering through
sequentially executed, alltheassociated logentries atthe host
timestampsbecomesunattainable.
OS kernel are registered together on the eBPFmaps, making
Toaddress theseproblems, acommon logspaceisrequired
thematomicrecords.TheUser-spacecomponentpollsthering
whichisaccessibletoasinglesource.Ahost-specificeBPFring
(cid:2)
buffer (Fig. 1 8 ) and writes these atomic log entries to the
bufferissuitableforthistask.Itservesasaneventqueueforboth
XPLOGCollectorSectionIV-C(Fig.1 (cid:2) 9 ).Thestepsbetween
system and application logs, which are polled and consumed
(cid:2) (cid:2)
(Fig. 1 2 - 5 ) help in writing the logs sequentially in the
(Fig. 2). Consequently, the kernel-space component plays a
orderofthecorrespondingeventexecutionwithinthehostOS
crucial role in generating both system and application logs by
kerneltocreateaunifiedcausally-consistentlogmessagestream
collating them while preserving the causal order. To monitor
fromeachindividualhosts.Also,topreserveper-threadcausal
applicationlogswithinthekernelspace,specializedeBPFprobes
orderingonmulti-coresystems,XPLOGmaintainsamonotonic
areemployedforthewrite()syscall.Wheneveranapplica-
locallogicalcounter[76]attheentryprobeofeachsyscall.This
tion generates a log intended for storing in a specific log file,
counterisattachedtothelogentryandincrementedperthread
write()syscallsaretriggeredaccordingly.Byleveragingthe
context.Inpractice,suchacountercanbeimplementedinthe
filecontextinformationsuchasFileDescriptors(FD),FilePath,
hostkernelusingper-taskdatastructures(e.g.,task_struct
etc.,obtainedatthesyscallentryprobe,thesystemcandetermine
in Linux) where a thread-local counter is updated atomically
thedestinationofthemessagestringandascertainwhetheritis
at each probe entry, thereby avoiding contention across cores.
alog-relatedoperation,suchaswritingtoSTDOUT/STDERR
Thiscounteristhenusedtosortlogsbeforeingestion,ensuring
or a log repository (typically /var/log/*). If the write
intra-threadconsistencydespitepotentialout-of-orderexitsdue
operation pertains to logging, the probe captures the message
tocontextswitching.However,westillneedtoensurecausally-
string and categorizes it as an application log. Consequently,
orderedloggingacrossmultiplehosts,ashandledbytheXPLOG
XPLOG ensures the coherent aggregation of causally-ordered
Collectordiscussednext.
system and application logs. The generated log messages are
periodicallytransmittedtotheXPLOGCollectormicroservice.
Handling PID namespaces: A process operating within a
C. XPLOGCollector
containermighthavethesamePIDasanotherprocessrunning
in a separate container. To distinguish logs originating from TheXPLOGCollectorgathersthelogentriestransmittedby
differentcontainers,XPLOGincorporatesa“TaskContext”into various XPLOG agents. To ensure causally-consistent logging
the application logs (refer to Table II). This inclusion proves across hosts with varying clocks, XPLOG employs “Vector
invaluable in segregating log contexts for processes across di- Clock” [75] implemented in the kernel space triggered with
verse containers. Consider a scenario where a microservice eachcross-hostcommunicationevent.Fig.3demonstrateshow
in Container 1 executes a request, followed by invoking an- XPLOG maintains causal consistency across a three-host mi-
other microservice in Container 2 (both residing on the same croservice deployment. Each host has an initial vector clock:
host). Both microservices generate application logs, and dis- H1 [1,0,0],H2 [0,1,0], and H3 [0,0,1]. When a user writes a
ambiguating these logs in a global file becomes challenging logmessageonHost1(ComposePostservice),thelocalvector
in the absence of a clear distinction. This difficulty arises due clockisincrementedtoH1 [2,0,0],andXPLOGlogsthisevent
to the shared process namespace between containers and the using the write() syscall. Later, when H1 connects to H2
host,withnamespacesnotvisiblepercontainer.Toaddressthis (Textservice)usingconnect(),XPLOGinjectsthecurrentvector
issue,addinga“TaskContext”(HostPIDandHostTID)tothe clock H1 [2,0,0] into the syscall metadata. When this con-
application logs clearly indicates which container generated a nection is accepted by H2 using accept(), XPLOG updates
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore. Restrictions apply.

800 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
TABLEIII
LISTOFMONITOREDSYSCALLS
A. ImplementationDetails
Thesourcecode,documentation,andtheexperimentalcon-
|     |     |     | H   | H   |     | H   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 3. Three hosts 1(ComposePost), 2(Text), 3(Storage) processing figuration scripts of XPLOG implementation have been open-
| a user  | request. | Initial | State: H1[1,0,0],  | H2[0,1,0], |            | H3[0,0,1]. An example |     |           |                    |     |          |     |                |     |
| ------- | -------- | ------- | ------------------ | ---------- | ---------- | --------------------- | --- | --------- | ------------------ | --- | -------- | --- | -------------- | --- |
|         |          |         |                    |            |            |                       |     | sourced2. | The implementation |     | of XPLOG |     | Agent consists | of  |
| showing | how      | vector  | clocks are updated | during     | inter-host | communication         | in  |           |                    |     |          |     |                |     |
3,232linesofcode(LoC),whiletheXPLOGCollectorisimple-
athree-microservicedeployment.
|     |     |     |     |     |     |     |     | mented | with 176 LoC.  | During     | implementation, |     | we have   | used |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | ---------- | --------------- | --- | --------- | ---- |
|     |     |     |     |     |     |     |     | C with | libbpf library | to realize | eBPFprobe       |     | programs. | We   |
the vector clock of H2 according to the merge rule: VC[i]= monitor 19 syscalls across file I/O, process, and socket types
max(VC [i],VC [i])∀i,resultinginH2 [2,1,0]andthen (Table III),which are configurable at runtime. We have devel-
|     | local |     | received |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[2,2,0].
incrementing the local component to H2 This process oped corresponding eBPFprobes for each of them separately.
recurswhenH2 connectstoH3 (Storageservice),whereH3’s Each syscall-generated log contains the fields listed in Ta-
vector clock is updated from [0,0,1] to [2,2,1] and then to ble II. These fields are obtained using eBPFhelper functions,
[2,2,2] after incrementing the local component. Each syscall task struct, etc. As and when they are obtained, the fields are
eventcreatesalogentrywiththecurrentvectorclocktimestamp, populatedinthekernel-reservedspace.Sincethespacereserved
whichXPLOGagentssendperiodicallytothecollector.Thecol- is a stream of bytes, it needs to be dereferenced appropriately
dependingonthesyscall.Notably,eachlogentryspansbetween
lectorappliesthehappens-beforerelation((2))tocausallyorder
|     |     | [2,0,0]→H2 | [2,2,0]→H3 |     | [2,2,2]andmakesthe |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thelogs:H1 500 to 600 bytes, encompassing comprehensive contextual in-
finallogstreammaintaintheactualcausalorderofeventsonall formationaboutasyscall,asgeneratedbytheeBPFinstrumenta-
hostsdespitenetworklatencyorclockskew. tionframework.Toidentifythesyscall,wehaveusedthefirst32
bitsinthereservedspace,whichcontainthesyscallID.Syscall
|     | VC1 | <VC2 | ⇐⇒  | (∀i.VC1 | [i]≤VC2 | [i]) |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
logsandapplicationlogsaredistinguishedwiththehelpoflms
∧(∃j.VC1 [j]<VC2 [j]) fieldsetupinthelogstructure.ToimplementtheKernel-space
(2)
|     |     |     |     |     |     |     |     | Component, | we have used | the | eBPFring | buffer | (described | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | -------- | ------ | ---------- | --- |
Inthevectorclockimplementation,weuseavectorofinteger Section IV-B3) size as 1 MB with a polling interval of 50 ms,
valuestorepresentthelogicaltimestampcorrespondingtoeach whichsignifiesthataftereach50ms,thelogsstoredinthering
host. Application processes update the host OS’s vector clock bufferwillbeforwardedtotheXPLOGcollector.Additionally,
when an event occurs on the host (from any of the running we have reserved 2 MB for pid_exec_map and 64 KB for
microservices).Duringinter-hostcommunication,suchaswhen pid_args_map. The XPLOG Collector is implemented as
two microservices over two different hosts communicate, a a lightweight TCP server that receives serialized logs from
| network-related |     | syscall | is invoked. |     | This | syscall includes | the |             |            |         |                 |     |          |      |
| --------------- | --- | ------- | ----------- | --- | ---- | ---------------- | --- | ----------- | ---------- | ------- | --------------- | --- | -------- | ---- |
|                 |     |         |             |     |      |                  |     | agents over | persistent | sockets | and immediately |     | persists | them |
vector clock of the host, which is stored in the eBPFmap. A instructuredJSONLformatwithtimestamps,hostIDs,service
host’s local vector clock is updated based on the local events names,andvectorclockmetadata.
| and | the received | timestamps |     | over the | network | calls, following |     |     |     |     |     |     |     |     |
| --- | ------------ | ---------- | --- | -------- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
the standard vector clock update procedure [75]. Notably, we B. ExperimentalSetup
| do  | not modify | syscall | payloads | or  | application | data, we | only |             |              |     |           |     |                |     |
| --- | ---------- | ------- | -------- | --- | ----------- | -------- | ---- | ----------- | ------------ | --- | --------- | --- | -------------- | --- |
|     |            |         |          |     |             |          |      | To evaluate | the efficacy |     | of XPLOG, | we  | use DeathStar- |     |
piggybackthevectorclockintoXPLOG’sownlogs.Thecollector
Bench[32],anopen-sourcebenchmarksuiteforcloudmicroser-
utilizesthislogicalclocktoconsolidatelogsfromvarioushosts,
vices.WehaveusedtheSocialNetworkmicroserviceofDeath-
ensuringcausalorderingofeventsacrossthehosts.
StarBenchforitshighservicecomposition(+30microservices)
andrichinteractionpatternsforlarge-scaletestingofmicroser-
|     |     | V.  | PERFORMANCEEVALUATION |     |     |     |     |                    |      |            |             |     |             |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | ------------------ | ---- | ---------- | ----------- | --- | ----------- | --- |
|     |     |     |                       |     |     |     |     | vice applications. | This | particular | application |     | is composed | of  |
We evaluate XPLOG with the following objectives: (1) how 30differentmicroserviceswith3differentactiveendpointsfor
wellXPLOGcanreducedisordersinthegeneratedlogcompared user interaction, such as Compose-Post-service (CP),
User-Timeline-service(UT)andHome-Timeline-
toTracee[33],awidelyusedsystemauditingframeworkthat
useseBPFtocaptureruntimesyscallexecutionlogs,(2)runtime service (HT) where each client request directly impacts
resourceconsumptionoverheadofXPLOG,(3)scalability,and
(4)completenessandrichnessofthegeneratedloginformation, 2https://github.com/usatpath01/Pluggable_Logging (Accessed: 2025/10/03
| comparedtoTracee. |     |     |     |     |     |     |     | 10:50:39) |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 801
| different | microservices; |     | primarily | (a) | “Load balancer”, | (b) |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
“ComposePost”,(c)“Text”,and(d)“UserMention”.However,
thesemicroservicesmakeuseofseveralothermicroservicesand
| triggerthemasandwhenrequired3 |     |     |     | (like,“poststorage”,“user |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
timeline”,“RabbitMQ”,etc.)duringtheprocessingofindividual
requests.WehaveusedanHTTPbenchmarkingtoolforwork-
| load generation, |     | called | wrk 4, | which sends | a variable | number |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | ------ | ----------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ofmultithreadedasynchronousrequestsrangingfrom10,000to
30,000parallelrequeststargetedtowardstheservicesandlook
| into the | consolidated | log | generated | by  | the application. | To test |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --------- | --- | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
themulti-hostlogcollectioncapabilityofXPLOG,wehavede-
ployedthemicroservicesin10-30VMs,eachconfiguredasedge
|     |     |     |     |     |     |     | Fig. 4. | Log disorder |     | between | Tracee | and XPLOG | (Service | endpoint: |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------- | ------ | --------- | -------- | --------- |
computinghostsrunningmultiplecontainerizedmicroservices
CP+UT+HT)
| using Docker | Swarm | as  | container | orchestration. |     | Each VM | is  |     |     |     |     |     |     |     |
| ------------ | ----- | --- | --------- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
configuredwithUbuntu22.04SMPwithLinuxkernelversion
| 6.5.0−41−generic,eachwith16vCPUcoresand64GBof |     |     |     |     |     |     |     |     |     |     | TABLEIV |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
IRRELEVANTLOGSRECEIVEDVSRELEVANTLOGSLOST
RAM.Amongthesehosts,oneisassignedasaDockerSwarm
| manager | and the | rest as | workers. | The | Docker | manager host |     |     |     |     |     |     |     |     |
| ------- | ------- | ------- | -------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
schedulesthemicroservicesacrosstheworkerhosts.Toprevent
underutilizationoftheVMs,wehavereplicatedtheserviceswith
| a replication | factor | ranging | from | 3 to 5; | consequently, | a mini- |     |     |     |     |     |     |     |     |
| ------------- | ------ | ------- | ---- | ------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
mumof4to5microservicesarescheduledperhostmachine.We
| have used | Docker | Swarm | as an | orchestrator | due | to its simpler |     |     |     |     |     |     |     |     |
| --------- | ------ | ----- | ----- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
multi-hostorchestrationandlightweightconfiguration.Notably,
|       |          |             |     |                |     |             | endpoints | randomly |     | during | execution. | We  | have | also collected |
| ----- | -------- | ----------- | --- | -------------- | --- | ----------- | --------- | -------- | --- | ------ | ---------- | --- | ---- | -------------- |
| XPLOG | can also | be deployed |     | as a DaemonSet | in  | Kubernetes, |           |          |     |        |            |     |      |                |
thelogsbyrandomlyvaryingtherequestsandserviceendpoints
enablingper-nodeXPLOGAgentstomonitorallpodsscheduled
toreplicateareal-worlduserinteraction.
onthatnode.
|     |     |     |     |     |     |     | To measure |     | the | causal | distance | between |     | the baseline |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ------ | -------- | ------- | --- | ------------ |
Forcomparison,wecollectlogsusing(a)Tracee[33]and
|                  |             |        |          |        |          |              | (sequentially-ordered)                    |     |     | log | and the   | log generated |             | by the two |
| ---------------- | ----------- | ------ | -------- | ------ | -------- | ------------ | ----------------------------------------- | --- | --- | --- | --------- | ------------- | ----------- | ---------- |
| (b) the proposed |             | XPLOG. | Notably, | Tracee | also     | uses eBPFto  |                                           |     |     |     |           |               |             |            |
|                  |             |        |          |        |          |              | frameworks,                               | we  | use | two | different | disorder      | metrics     | adopted    |
| capture          | the runtime | system | events   | and    | log them | based on the |                                           |     |     |     |           |               |             |            |
|                  |             |        |          |        |          |              | fromtheexistingliterature[77]:(a)exchange |     |     |     |           |               | (Ex)%:which |            |
timestampedorder.TheXPLOGAgentsaredeployedasseparate
measurestheminimumnumberofentriesthatrequireswapping
| containers  | in each   | worker, | and  | the XPLOG | Collector          | in the      |          |                |     |            |     |               |       |              |
| ----------- | --------- | ------- | ---- | --------- | ------------------ | ----------- | -------- | -------------- | --- | ---------- | --- | ------------- | ----- | ------------ |
|             |           |         |      |           |                    |             | to order | a sub-sequence |     | concerning |     | the baseline, |       | with respect |
| manager     | host. As  | Tracee  | does | not       | support multi-host | log         |          |                |     |            |     |               |       |              |
|             |           |         |      |           |                    |             | to total | number         | of  | log lines  | and | (b) rem%:     | which | measures     |
| collection, | we deploy | Tracee  |      | in each   | host, and          | log message |          |                |     |            |     |               |       |              |
theminimumnumberofentriesthatmustberemovedtoorder
streamsarecollectedusingSFTP,merged,andsortedbasedon
|     |     |     |     |     |     |     | a sub-sequence |     | concerning |     | the baseline |     | with respect | to total |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ------------ | --- | ------------ | -------- |
thetimestampavailableforeachlogentry.
numberofloglines.
Ex
|     |     |     |     |     |     |     | Fig. 4(a) | shows | the | percentage |     | of disorder | in  | terms of |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | ---------- | --- | ----------- | --- | -------- |
C. AnalysisofCausalOrderingLevel
|     |     |     |     |     |     |     | and rem | with | respect | to  | the number | of  | concurrent | requests |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------- | --- | ---------- | --- | ---------- | -------- |
Ground truth: To show the level of causally ordered logs from the clients. We observe that the measure of disorder
|              |          |                |     |     |           |           | is significantly |     | lower | in  | XPLOG | compared | with | Tracee, |
| ------------ | -------- | -------------- | --- | --- | --------- | --------- | ---------------- | --- | ----- | --- | ----- | -------- | ---- | ------- |
| for multiple | parallel | microservices, |     | we  | have used | real-time |                  |     |       |     |       |          |      |         |
sequential logs as the ground-truth baseline by sending se- proving that XPLOG-generated logs are closer to the baseline
quential requests to the application endpoints (CP, UT, and (sequentially-orderedlog)andthusclosertotruecausalorder-
ing.AsshowninFig.4(a),foraserviceendpoint:CP+UT+HT,
| HT) on | a single | host | machine | while | ensuring | synchronized |     |     |     |     |     |     |     |     |
| ------ | -------- | ---- | ------- | ----- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
XPLOG
CLOCK_MONOTONIC across all the processor cores for that generates only 83 log lines, among which 2 to 3 log
host.Notably,theloggeneratedthroughsequentialrequestson linesrequireswapping(EX)and2to3loglinesrequireremoval
such a single host machine will always maintain a true causal (REM) to match the baseline ordering. In contrast, Tracee
|     |     |     |     |     |     |     | records | 2,586 | log lines, | of  | which | 1,034 require |     | swapping and |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------- | --- | ----- | ------------- | --- | ------------ |
orderwithoutanyinterferencefromparallelrequests.Forcom-
parison,wecollectedXPLOG-generatedandTracee-generated 1,552 need removal to match the same baseline. This signifi-
logs while sending 10,000–30,000 parallel and asynchronous cantreductionindisorderisduetoXPLOG’sselectivefiltering
|          |        |                    |     |               |        |         | of irrelevant | system |     | calls | and its | causality-preserving |     | design. |
| -------- | ------ | ------------------ | --- | ------------- | ------ | ------- | ------------- | ------ | --- | ----- | ------- | -------------------- | --- | ------- |
| requests | to the | target application |     | over multiple | hosts, | without |               |        |     |       |         |                      |     |         |
anyexplicitclocksynchronization.Theserequestswereissued Notably, for 30,000 parallel requests for the same set of mi-
overa120-secondinterval,correspondingtoanaverageloadof croservices, Tracee generated almost 3.5GB and compara-
∼80 to ∼250 requests per second. To emulate real-world user tivelyXPLOGgenerates5.7GBoflogmessagesintotal(more
|     |     |     |     |     |     |     | details in | Section | V-E, | Table | V). | Similarly, | Fig. | 4(b) shows |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | ----- | --- | ---------- | ---- | ---------- |
interactionpatterns,wealsovariedtherequestratesandservice
|     |     |     |     |     |     |     | the disorder | percentage |     | with    | respect | to the | increasing | number      |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------- | ------- | ------ | ---------- | ----------- |
|     |     |     |     |     |     |     | of host      | machines.  | We  | observe | that    | Ex and | rem        | percentages |
3https://github.com/delimitrou/DeathStarBench/raw/master/socialNetwork/
are6x-8xlessinXPLOGcomparedtoTracee,evenwhenthe
| figures/socialNet_arch.png |     | (All | URLs | in this paper | have | accessed last | on  |     |     |     |     |     |     |     |
| -------------------------- | --- | ---- | ---- | ------------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2025/10/0310:50:39) number of hosts increases. The negligible disorder shown by
4https://github.com/wg/wrk(Accessed:2025/10/0310:50:39) XPLOGisduetothebufferbloatatthecommunicationchannel
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

802 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
TABLEV
LOGSIZESVS#REQUESTS(SERVICEENDPOINT:CP)
|     |     |     |     |     |     |     | Fig. 5. Average | CPU (both kernel-space |     | overhead | from eBPF | probes and |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------------------- | --- | -------- | --------- | ---------- |
user-spaceoverheadfromXPLOGagentlogprocessingandtransmission)and
networkutilizationof19XPLOGagents.
| between | the agents | and the | collectors | when there | is a | spike | in  |     |     |     |     |     |
| ------- | ---------- | ------- | ---------- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
thenumberofgeneratedlogmessages;however,weobservethat
thehost-generatedlogsaretrulycausalfor>99%oftheexper-
| iment scenarios. | While       | XPLOG        | significantly |          | improves    | causal |     |     |     |     |     |     |
| ---------------- | ----------- | ------------ | ------------- | -------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
| consistency      | in logging, | it currently | only          | supports | Linux-based |        |     |     |     |     |     |     |
environments.
D. AnalysisofRuntimeObservability
| To test      | the capability | of XPLOG   | in    | producing | relevant | logs   |     |     |     |     |     |     |
| ------------ | -------------- | ---------- | ----- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
| with minimal | query          | processing | time, | we        | apply an | event- |     |     |     |     |     |     |
sequence-based filter on the generated log streams to extract Fig.6. CPUutilizationperrequest(Serviceendpoint:CP).
| the necessary | information. |       | The results | are          | summarized |       | in  |     |     |     |     |     |
| ------------- | ------------ | ----- | ----------- | ------------ | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| Table IV.     | The table    | shows | the number  | of “relevant | logs       | lost” |     |     |     |     |     |     |
and“irrelevantlogsreceived”,asextractedfromthelogstreams E. ResourceOverheadAnalysis
foraneventwhenapplyingthefilter.Wedefineirrelevantlogsas
TomeasuretheoverheadofXPLOG,wehaveusedcAdvi-
thosecapturedbytheloggingframeworkthatdonotpertainto sor 5, an open-source tool developed by Google to monitor
thespecificeventorcontextbeinginvestigated,astheyinclude
|     |     |     |     |     |     |     | containers. | Also, to measure | the resource |     | consumption | by the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | ------------ | --- | ----------- | ------ |
datafromunrelatedprocessesoractivities,makingitharderto
|     |     |     |     |     |     |     | hosts, we | have used NodeExporter |     | 6 to | measure | the CPU, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------- | --- | ---- | ------- | -------- |
focusontherequiredinformation.Incontrast,relevantlogsare Memory,andNetworkutilizationofeachhost.
pertinenttothespecificeventorcontextbutwerenotcaptured 1) CPUandNetworkUtilizationforXPLOGAgents: Fig.5
bytheloggingtool.Missingtheselogscanleadtoincomplete
showsthetotalCPU(kernel-spaceanduser-space)andnetwork
information,potentiallyhinderingeffectivemonitoring,debug- utilization of 19 XPLOG agents running in the workers. We
ging,andinvestigation. observe that the average CPU usage (see Fig. 5(a)) of XPLOG
| In Table | IV, we | present | the results | for relevant |     | logs lost, |            |              |           |      |       |            |
| -------- | ------ | ------- | ----------- | ------------ | --- | ---------- | ---------- | ------------ | --------- | ---- | ----- | ---------- |
|          |        |         |             |              |     |            | Agents are | 2.9%, 3.10%, | and 3.15% | with | error | bars show- |
irrelevant logs received, and the time taken to extract query ±0.5−0.8%.
|     |     |     |     |     |     |     | ing a variance | of about |     | when | 10K, | 20K, and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ---- | ---- | -------- |
resultsforthreedifferenttypesofeventsobservedbythesystem 30K requests are sent concurrently. This indicates that even
administrator.Theeventsaree1:triggeredbytheCPendpoint, underburstyrequestpatterns,CPUoverheadremainsstableand
| e2:triggeredbytheUTendpoint, |     |     | ande3:triggeredbytheHT |     |     |     |              |                       |     |        |           |          |
| ---------------------------- | --- | --- | ---------------------- | --- | --- | --- | ------------ | --------------------- | --- | ------ | --------- | -------- |
|                              |     |     |                        |     |     |     | low, without | significant deviation |     | across | runs. The | overhead |
endpoint. The timestamp of the event serves as the input. We measurements show the total CPU utilization observed in the
ran both Tracee and XPLOG alongside the microservices to container,includingsystemcalllatencyfromkernelprobesand
demonstrateourfindings.XPLOGisspecificallydesignedtouse XPLOG’s
|         |           |        |              |              |     |        | the resource | usage of              | user-space |       | agent.    | In Fig. 6, |
| ------- | --------- | ------ | ------------ | ------------ | --- | ------ | ------------ | --------------------- | ---------- | ----- | --------- | ---------- |
| tag IDs | and XPLOG | IDs to | filter logs. | To establish | the | ground |              |                       |            |       |           |            |
|         |           |        |              |              |     |        | we show      | the % CPU utilization | in         | terms | of kernel | space and  |
truth, we repeatedly sent the requests to the 3 endpoints to user-space of XPLOG Agent and application service. For the
determinethenumberoflogsgeneratedforthatspecificevent. XPLOG Agents, the majority of CPU utilization is due to the
Thisapproachhelpsunderstandthetypicalvolumeoflogsand
underlyingeBPFprograms;thus,utilizationbykernel-spacepro-
theirvariability,whichrangesbetween80to100logmessages cessesiscomparativelyhigherthanuser-spaceprocesses(shown
pereventduetocontextswitchesinthesystemduringtheevent astheredshadedarea)attheapplicationservices.Theseresults
processing.Thetableshowsthatthequeryprocessingtimefor
|     |     |     |     |     |     |     | show that | the proposed XPLOG | framework |     | is a low-overhead |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------ | --------- | --- | ----------------- | --- |
Traceeisalmost3xthatofXPLOGtofigureouttherelevant
|     |     |     |     |     |     |     | solution | with minimal processing | requirements. |     | We  | also show |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------------- | ------------- | --- | --- | --------- |
logsfromthecollatedlogmessagestream.However,itreturns the network utilization (see Fig. 5(b)) of the XPLOG agents,
manyirrelevantlogs(asthelogmessagesaredisordered)while
missingseveraloftherelevantlogmessages.Incontrast,XPLOG
canfilterouttheexactlogmessagescorrespondingtoanevent
5https://github.com/google/cadvisor(Accessed:2025/10/0310:50:39)
followingitscapabilityofpreservingthecausalorderofthelog 6https://github.com/prometheus/node_exporter
|     |     |     |     |     |     |     |     |     |     |     | (Accessed: | 2025/10/03 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- |
messages.
10:50:39)
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 803
Fig.7. AveragenetworkutilizationanddiskwritespeedofXPLOGcollector.
Fig.9. HostResourceutilization(Serviceendpoint:CP+UT+HT).
than disposing of these logs, XPLOG uses a different mecha-
nism to separate them (XPLOG -relevant logs, as indicated in
SectionV-D),resultinginmeaningfullogentriesinthecollated
logmessagestream.
ThepercentageutilizationoftheeBPFringbufferwhilevary-
ing the number of requests from 10K to 30K is presented
in Fig. 8(b). We have declared the eBPF ring buffer with
Fig. 8. Average memory consumption and eBPF ring buffer utilization of
__uint(max_entries, 256 * 1024), which sets its
19XPLOGAgentsforworkloadsof10K,20K,and30Krequestswithina
120-secondinterval.
totalcapacityto262,144bytes(≈256KB).Giventhateachlog
entryinourimplementation(ReferListing1)isapproximately
500to600bytes,thebuffercanstoreuptoaround437entries
whichis∼1.7Mbps,becauseoftheconstantstreamingofthe beforereachingfullcapacity.Sincethebufferispolledevery50
generatedlogmessagestothecollector. ms,thistranslatestoasustainedhandlingcapabilityofroughly
2) Resource Usage by XPLOG Collector: Fig. 7(a) shows 8,740logentriespersecondwithoutoverflow.Weobservethat
thetheXPLOGcollector’snetworkthroughput,whichsustained thepeakutilizationofeBPFringbufferis5.2%forCP,UT,and
progressivelyhigheringestionratesastheworkloadincreased, HTendpoints.
starting from 10.3 Mbps at a load of 10K requests, rising to Notably,theboundedin-kernelringbuffermaylimitperfor-
13.2 Mbps at 20K requests, and reaching 14.3 Mbps at 30K mance,asoncefullitoverwritesolderentries,causingpotential
requests. On the other hand, Fig. 7(b) shows the disk write loglossduringshorthigh-throughputbursts.Hence,buffersize
performanceofXPLOGcollector.At10Krequests,theCollector mustbechosencarefullybyadministratorsbasedonapplication
achievedasustainedwritespeedof5.2MB/s,whichincreased log rates. Nevertheless, XPLOG’s vector clock–based times-
to9.0MB/sat20Krequestsandfurtherto12.8MB/sat30K tampingpreservescausalrelationshipsamongremainingevents,
requests. ensuring logs across threads and hostscan be reconstructed in
3) Memory Overhead: We observe that the memory over- correct partial order. Thus, while minor detail loss may occur,
head (see Fig. 8(a)) of XPLOG Agents remains constant with thesystemavoidsanalysisblindspotsfromeventreorderingor
10K,20K,and30Krequestsbeingsent,whereasthememory omission.
usagebytheXPLOGCollectorvariesfrom2.21MBto2.7MB. 4) Host-LevelResourceUtilization: Wehavealsomeasured
To measure the size of the total log messages generated by the resource utilization of hosts to determine how the overall
XPLOG, we observed that the logging framework generates systemhandlesincreasingloads(showninFig.9).Forthisload
5.7GBwhenthenumberofparallelrequestsis10,000whereas testing,wefollowconstantdurationwithavariablerequestrate
Traceegenerates2.1GBoflogmessages.Notably,thistotal strategy where we vary the number of requests, keeping the
size of the log messages increased to 5.2GB and 13GB for duration of the test constant at 120 seconds, i.e., for 10,000
30,000 concurrent requests for Tracee and XPLOG, respec- requests, the rate of request is 83; for 20,000, it is 166, and
tively (see Table V). Notably, XPLOG also incorporates the for 30,000, it is 250 requests per second. We observe that the
application logs generated from the microservices within the CPU Utilization of the manager is around 7% when only the
global log, whereas Tracee only captures the syscall logs; microservices are running, whereas, with Tracee, it is 12%
therefore, the number of log entries in the XPLOG-generated (showninthehashedlineofFig.9(a)).However,withXPLOG,
log is comparatively higher than Tracee-generated logs, as it goes up to 21% (shown in dotted of Fig. 9) as the collector
indicatedinTableV. continuously consumes the log messages sent by the agents.
XPLOGcanhandlethishighamountoflogsreasonablywell, However,weobservethatthememoryusage(showninFig.9(b))
whichcanbejustifiedbyFig.8(a)wherethememoryrequire- bythehostswhenonlythemicroservicesarerunningis1.6%;
mentoftheagentsdoesnotincreasesignificantlyevenincase withXPLOG,itis1.7%,andwithTracee,itis2.3%.Thisis
of a high request load. We also observe that (see Table IV), a becausetheXPLOGagentsendsthelogstothecollectorservice
significantamount(i.e.,≈2/3rdofalllogs)ofthegeneratedlogs where Tracee stores them in the host itself. These results
are due to the sandboxing environment and platform. Rather indicatethatwhileXPLOGintroducesamarginallyhigherCPU
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore. Restrictions apply.

804 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
TABLEVI
LOGWRITINGLATENCY(#CONCURRENTREQUESTS:10,000)
overheadduetothecontinuouslogtransmissiontothecollector
service,itachievesbettermemoryefficiencybyoffloadinglog
| storage.                      | This | trade-off   | can | be advantageous |           | in scenarios | for         |     |     |     |     |     |
| ----------------------------- | ---- | ----------- | --- | --------------- | --------- | ------------ | ----------- | --- | --- | --- | --- | --- |
| memory-intensive              |      | application |     | workloads,      | which     | is           | typical for |     |     |     |     |     |
| edge Computing-on-Demand(CoD) |      |             |     |                 | scenarios | [78],        | [79]. The   |     |     |     |     |     |
overalllowermemoryfootprintofXPLOGmakesitamoreviable
| option for   | environments |             | with | high         | memory | usage     | demands, |     |     |     |     |     |
| ------------ | ------------ | ----------- | ---- | ------------ | ------ | --------- | -------- | --- | --- | --- | --- | --- |
| highlighting | its          | suitability |      | for scalable | and    | efficient | logging  |     |     |     |     |     |
indistributedsystems.Notably,reducedresourceconsumption
alsolowersoperationalcosts,particularlyincloudenvironments
whereresourcesarebilledbasedonusage.
| To demonstrate |            | the        | real-time  | collection |          | of logs, | which de-    |     |     |     |     |     |
| -------------- | ---------- | ---------- | ---------- | ---------- | -------- | -------- | ------------ | --- | --- | --- | --- | --- |
| pends on       | the        | underlying | network    | latency,   |          | we have  | used the     |     |     |     |     |     |
| Linux tc       | utility    | to         | configure  | latency    | between  | each     | host and     |     |     |     |     |     |
| collector      | as 0.5     | ms.        | For 10,000 | parallel   | requests |          | on different |     |     |     |     |     |
| application    | endpoints, |            | we have    | calculated | the      | latency  | between      |     |     |     |     |     |
thegenerationofalogmessageandtheappearanceofthesame
| message   | at the | XPLOG   | collector. | The      | results | (see          | Table VI) |     |     |     |     |     |
| --------- | ------ | ------- | ---------- | -------- | ------- | ------------- | --------- | --- | --- | --- | --- | --- |
| show that | the    | average | latency    | is close | to 1    | s, indicating | that      |     |     |     |     |     |
theproposedobservabilityframeworkmakesthelogmessages
availabletothedownstreamapplicationsreasonablyfast.
F. QualitativeEvaluation
|     |     |     |     |     |     |     |     | Listing1: | ExampleofXPLOG-generatedlogentries |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------------------- | --- | --- | --- |
Aspartofourqualitativeanalysis,wefocusontwoprimary
| factors: | (a) ease | of log | consultation |             | and (b) | richness | level of   |     |     |     |     |     |
| -------- | -------- | ------ | ------------ | ----------- | ------- | -------- | ---------- | --- | --- | --- | --- | --- |
| logs. We | have     | used   | a sample     | application | log     | and      | system log |     |     |     |     |     |
entry format in Listing 1 with relevant fields highlighted for can be used to realize the same. From the real example logs
easeofunderstanding7.
|                           |     |     |     |                       |     |     |     | (shown | partially for brevity), | it is visible | that both | application |
| ------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | ------ | ----------------------- | ------------- | --------- | ----------- |
| 1) EaseofLogConsultation: |     |     |     | AsshowninTableV,XPLOG |     |     |     |        |                         |               |           |             |
andsystemlogsfrommultiplesystemscanbeaccessedasper
generatesmuchmorelogsthantheexistingsystemslikeTracee, theircausalorderingfromtheoutput(seeListing1).
whilecombiningtheapplicationlogswiththesystemlogs.One 2) Log-Richness Level: As both Tracee and XPLOG are
| pertinent | question | is  | how difficult | it  | is to | identify | contextual |     |     |     |     |     |
| --------- | -------- | --- | ------------- | --- | ----- | -------- | ---------- | --- | --- | --- | --- | --- |
eBPF-basedapproaches,theycanmonitorselectedsystemcalls,
informationfromthegeneratedlogs.Todeterminethecontex- but in terms of expressibility, both frameworks differ signif-
tualinformation,asystemadministratortriestoisolatethelogs icantly. To compare this feature, we have customized both
relevanttoaparticularrequestduringloganalysisandthenlooks
frameworkstomonitoralistofsystemcallsaslistedinTableIII
intothesequenceofeventsthathappenedwhileprocessingthat
|     |     |     |     |     |     |     |     | and collected | the logs | while executing | the application | above |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------------- | --------------- | ----- |
request.Toextracttheapplicationlogsfromtheentirelogfile, usingboththeframeworks.
shecanfilterthelogfilewiththerequestIdentifier(“tagID”), We observe that XPLOG-generated application and system
| which is | available | inside | the | lms field | (see | Line | 1 of Listing |     |     |     |     |     |
| -------- | --------- | ------ | --- | --------- | ---- | ---- | ------------ | --- | --- | --- | --- | --- |
logs(Listing1)providemoreinformationincomparisontothe
1).Thisprocesswillprovidealltheapplicationlogsgenerated Tracee-generatedlogs(Listing2).Asummaryofthecompar-
by all the microservices across all the hosts. The host_pid ison(TableVII)showsthatTraceecannotprovideapplication
| and host_tid |     | fields | together | can | be used | to identify | all the |     |     |     |     |     |
| ------------ | --- | ------ | -------- | --- | ------- | ----------- | ------- | --- | --- | --- | --- | --- |
logs.Further,understandingthecontextiscomplicatedasthere
logsgeneratedbyallthemicroservicesineachhostduringthe areoverlappinglogs(i.e.,withoutcausalorder,seeTIMEfieldof
processingoftherequestasshowninListing1(seeLines13,21, Line4inListing2).Moreover,Traceeprovidesonlythefile
22,23).Althoughitmaylookabitcomplicated,asimplescript8 descriptors value, where XPLOG provides more readable path
|     |     |     |     |     |     |     |     | information | (see Line | 21 of Listing | 1). Additionally, | XPLOG |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------------- | ----------------- | ----- |
7EachlogentrycontainsfieldsasdescribedinTableII.SamplelogsforXPLOG capturesthesyscallarguments,whichprovideseveraladditional
andTraceeareavailableathttps://github.com/usatpath01/Pluggable_Logging/ information, like the network addresses from socket calls (see
tree/main/Logs(Accessed:2025/10/0310:50:39)
8https://github.com/usatpath01/Pluggable_Logging/tree/main/scripts Line 22 of Listing 1), contents read/written to a file from the
(Accessed:2025/10/0310:50:39) syscallargumentsfields,etc.Therefore,comparedtoTracee,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 805
TABLEVII framework effectively captures both application and system
COMPARISONOFCAPABILITIESBETWEENTraceeANDXPLOG logs,maintainingcausalconsistencytoprovideaholisticview
ofevents.Deployedasalightweightmemory-efficientmodule,
|     |     |     |     |     |     |     | XPLOG | reduces | the disorder | among | the | generated |     | log entries |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------------ | ----- | --- | --------- | --- | ----------- |
whilepreservingthecausalorderingoflogswithrespecttothe
|     |     |     |     |     |     |     | sequential | execution | of corresponding |     |     | microservices. |     | Notably, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ---------------- | --- | --- | -------------- | --- | -------- |
XPLOGenablesdetailedextractionofdatapathexecutionsfrom
|     |     |     |     |     |     |     | parallel        | microservices, | including  |              | valuable | information |          | like bi- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ---------- | ------------ | -------- | ----------- | -------- | -------- |
|     |     |     |     |     |     |     | nary executable |                | file paths | and accessed |          | files,      | a unique | feature  |
absentintheexistingloggingframeworks.Theresultinglogsare
significantlyhelpfulfordownstreamservicesthatneedruntime
systemobservability.
XPLOGcanbefurtherenhancedthroughefficiency-oriented
optimizationssuchascoalescing.Atpresent,itdoesnotsupport
hostswithmultipleoperatingsystems,makingitunsuitablefor
|     |     |     |     |     |     |     | heterogeneous |            | platforms.      | A promising |           | extension     | is        | to export |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --------------- | ----------- | --------- | ------------- | --------- | --------- |
|     |     |     |     |     |     |     | tagged        | logs into  | OpenTelemetry   |             | pipelines | and           | integrate | with      |
|     |     |     |     |     |     |     | frameworks    | like       | Pixie, enabling |             | broader   | observability |           | and im-   |
|     |     |     |     |     |     |     | proved        | end-to-end | visibility.     | Overall,    |           | XPLOG         | offers    | a strong  |
foundationforcausality-preservingobservabilityindistributed
|     |     |     |     |     |     |     | microservices |     | and opens | directions | for | research | in  | hybrid log |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ---------- | --- | -------- | --- | ---------- |
integration,cross-platformsupport,andautomatedprovenance-
basedanalyticsincloud-edgedeployments.
ACKNOWLEDGMENT
NehaDalmiaandRajatBachhawatwereassociatedwiththe
| Listing2: | Tracee-generatedsyscalllogsnippet |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IndianInstituteofTechnologyKharagpurduringthiswork.
XPLOGiseasytounderstandandlearnforsysadminsduetoits
REFERENCES
expressiveness.
However, there are several avenues to further enhance the [1] W.U.Hassan,M.A.Noureddine,P.Datta,andA.Bates,“OmegaLog:
robustness and efficacy of XPLOG. Although XPLOG supports High-fidelityattackinvestigationviatransparentmulti-layerloganalysis,”
inProc.27thNetw.Distrib.Syst.Secur.,2020.
bothsystem-andapplication-levellogging,itscurrentevaluation
[2] P.Datta,I.Polinsky,M.A.Inam,A.Bates,andW.Enck,“ALASTOR:
primarily focuses on low-level audit tools such as Tracee. It Reconstructing the provenance of serverless intrusions,” in Proc. 31st
does not yet integrate with full-stack observability platforms USENIXSecur.,2022,pp.2443–2460.
[3] “Sysdig-thecloudmovesfast.yoursecurityshouldtoo,”2013.Accessed:
| like Pixie9, | which | operate | at the | RPC tracing | and | telemetry |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------- | ------ | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Jul.24,2025.[Online].Available:https://sysdig.com/
| layers. | As a promising |     | future direction, |     | we plan | to extend |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ----------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[4] T.Taylor,F.Araujo,andX.Shu,“Towardsanopenformatforscalable
XPLOG to export causally tagged system and application logs systemtelemetry,”inProc.IEEEInt.Conf.BigData,2020,pp.1031–1040.
toOpenTelemetry-compatiblepipelinesandintegratewithtools [5] R.Sekar,H.Kimm,andR.Aich,“eAudit:Afast,scalableanddeployable
auditdatacollectionsystem,”inProc.45thIEEESymp.Secur.Privacy,
| like Pixie. | This | would | broaden XPLOG’s |     | applicability | within |     |     |     |     |     |     |     |     |
| ----------- | ---- | ----- | --------------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
2024,pp.3571–3589.
modernobservabilityecosystemsandenablemorecomprehen- [6] W.Kellerer,P.Kalmbach,A.Blenk,A.Basta,M.Reisslein,andS.Schmid,
siveend-to-endvisibility. “Adaptableanddata-drivensoftwarizednetworks:Review,opportunities,
andchallenges,”Proc.IEEE,vol.107,no.4,pp.711–731,Apr.2019.
[7] M.Scrocca,R.Tommasini,A.Margara,E.D.Valle,andS.Sakr,“The
VI. CONCLUSION Kaijuproject:Enablingevent-drivenobservability,”inProc.14thACM
Int.Conf.Distrib.Event-BasedSyst.,2020,pp.85–96.
| This | paper introduced |     | an innovative | and | non-invasive | plat- |     |     |     |     |     |     |     |     |
| ---- | ---------------- | --- | ------------- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
[8] S.Zawoad,R.Hasan,andK.Islam,“SECProv:Trustworthyandefficient
| form observability |     | framework | called | XPLOG | that | leverages |            |            |     |                |     |          |            |         |
| ------------------ | --- | --------- | ------ | ----- | ---- | --------- | ---------- | ---------- | --- | -------------- | --- | -------- | ---------- | ------- |
|                    |     |           |        |       |      |           | provenance | management |     | in the cloud,” |     | in Proc. | IEEE Conf. | Comput. |
Commun.,2018,pp.1241–1249.
| eBPFto | generate | comprehensive |     | logs for distributed |     | edge ap- |     |     |     |     |     |     |     |     |
| ------ | -------- | ------------- | --- | -------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[9] T.Blount,A.Chapman,M.Johnson,andB.Ludascher,“Observedvs.
| plications.UnlikepriorframeworkssuchasKubeArmor10 |     |     |     |     |     | that |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
possibleprovenance(researchtrack),”inProc.13thInt.WorkshopTheory
primarilyfocusonsecuritypolicyenforcementandauditlogging
Pract.Provenance,2021.
atthecontainerboundarywithoutintegratingapplication-level [10] M. Zipperle, F. Gottwalt, E. Chang, and T. Dillon, “Provenance-based
intrusiondetectionsystems:Asurvey,”ACMComput.Surv.,vol.55,no.7,
| events or | supporting | unified | provenance | reconstruction |     | across |     |     |     |     |     |     |     |     |
| --------- | ---------- | ------- | ---------- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
pp.1–36,2022.
| distributed | execution | paths, | XPLOG | is specifically |     | designed |     |     |     |     |     |     |     |     |
| ----------- | --------- | ------ | ----- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[11] M.M.Anjum,S.Iqbal,andB.Hamelin,“ANUBIS:Aprovenancegraph-
toenablecomprehensive,provenance-awareobservability.The
basedframeworkforadvancedpersistentthreatdetection,”inProc.37th
ACM/SIGAPPSymp.Appl.Comput.,2022,pp.1684–1693.
|     |     |     |     |     |     |     | [12] A.Chen,Y.Wu,A.Haeberlen,W.Zhou,andB.T. |     |     |     |     |     | Loo,“Differential |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- |
9https://px.dev/,Accessed:2025/10/0310:50:39 provenance:Betternetworkdiagnosticswithreferenceevents,”inProc.
10https://kubearmor.io/,Accessed:2025/10/0310:50:39 ACMWorkshopHotTopicsNetw.,2015,pp.1–7.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore.  Restrictions apply.

806 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.1,JANUARY/FEBRUARY2026
[13] A.Tabiban,H.Zhao,Y.Jarraya,M.Pourzandi,M.Zhang,andL.Wang, [37] K.Suo,Y.Zhao,W.Chen,andJ.Rao,“vNetTracer:Efficientandpro-
“ProvTalk:Towardsinterpretablemulti-levelprovenanceanalysisinnet- grammablepackettracinginvirtualizednetworks,”inProc.38thIEEE
workingfunctionsvirtualization(NFV),”inProc.29thNetw.Distrib.Syst. Int.Conf.Distrib.Comput.Syst.,2018,pp.165–175.
Secur.,2022. [38] X.Ge,B.Niu,andW.Cui,“Reversedebuggingofkernelfailuresinde-
[14] Y.Gan,G.Liu,X.Zhang,Q.Zhou,J.Wu,andJ.Jiang,“Sleuth:Atrace- ployedsystems,”inProc.USENIXAnnu.Tech.Conf.,2020,pp.281–292.
basedrootcauseanalysissystemforlarge-scalemicroserviceswithgraph [39] S.Y.Lim,B.Stelea,X.Han,andT.Pasquier,“Securenamespacedkernel
neural networks,” in Proc. 28th ACM Int. Conf. Architectural Support auditforcontainers,”inProc.12thACMSymp.CloudComput.,2021,
Program.LanguagesOperatingSyst.,2023,pp.324–337. pp.518–532.
[15] A.R.BernatandB.P.Miller,“Anywhere,any-timebinaryinstrumen- [40] J.Zeng,Z.L.Chua,Y.Chen,K.Ji,Z.Liang,andJ.Mao,“WATSON:
tation,”inProc.10thACMSIGPLAN-SIGSOFTWorkshopProg.Anal. Abstractingbehaviorsfromauditlogsviaaggregationofcontextualse-
Softw.Tools,2011,pp.9–16. mantics,”inProc.Netw.Distrib.Syst.Secur.,2021.
[16] F. Wang and Y. Shoshitaishvili, “Angr-the next generation of binary [41] U.Satpathy,R.Thakur,S.Chattopadhyay,andS.Chakraborty,“DisPro-
analysis,”inProc.IEEECybersecur.Develop.,2017,pp.8–9. Track:Distributedprovenancetrackingoverserverlessapplications,”in
[17] Y.Shoshitaishvilietal.,“Sok:(stateof)theartofwar:Offensivetech- Proc.IEEEConf.Comput.Commun.,2023,pp.1–10.
niques in binary analysis,” in Proc. IEEE Symp. Secur. Privacy, 2016, [42] L.Zhouetal.,“Hardware-assistedlivekernelfunctionupdatingonintel
pp.138–157. platforms,” IEEE Trans. Dependable Secure Comput., vol. 21, no. 4,
[18] Elastic, “Logstash: Collect, parse, transform logs| Elastic,” 2010. Ac- pp.2085–2098,Jul./Aug.2024.
cessed:Feb.4,2025.[Online].Available:https://www.elastic.co/logstash/ [43] M. N. Hossain et al., “Sleuth: Real-time attack scenario reconstruc-
[19] Fluent, “Fluentd | open source data collector | unified logging layer,” tion from cots audit data,” in Proc. 26th USENIX Secur. Symp., 2017,
Jun. 2024, Accessed: Feb. 4, 2025. [Online]. Available: https://www. pp.487–504.
fluentd.org/ [44] W. Xu, L. Huang, A. Fox, D. Patterson, and M. I. Jordan, “Detecting
[20] X. Merino and C. E. Otero, “The cost of virtualizing time in linux large-scalesystemproblemsbyminingconsolelogs,”inProc.22ndACM
containers,”inProc.8thIEEECloudSummit,2022,pp.63–68. Symp.OperatingSyst.Princ.,2009,pp.117–132.
[21] M.Cinque,R.D.Corte,andA.Pecchia,“Microservicesmonitoringwith [45] K.KcandX.Gu,“ELT:Efficientlog-basedtroubleshootingsystemfor
eventlogsandblackboxexecutiontracing,”IEEETrans.Serv.Comput., cloudcomputinginfrastructures,”inProc.30thIEEEInt.Symp.Reliable
vol.15,no.1,pp.294–307,Jan./Feb.2022. Distrib.Syst.,2011,pp.11–20.
[22] X. Han, T. Pasquier, A. Bates, J. Mickens, and M. Seltzer, “Unicorn: [46] F. Yang, J. Xu, C. Xiong, Z. Li, and K. Zhang, “PROGRAPHER: An
Runtimeprovenance-baseddetectorforadvancedpersistentthreats,”in anomaly detection system based on provenance graph embedding,” in
Proc.27thAnnu.Netw.Distrib.Syst.Secur.Symp.,SanDiego,CA,USA, Proc.32ndUSENIXSecur.Symp.,2023,pp.4355–4372.
2020. [47] M.Stamatogiannakis,E.Athanasopoulos,H.Bos,andP.Groth,“Prov
[23] A.Goyal,X.Han,G.Wang,andA.Bates,“Sometimes,youaren’twhat 2r:Practicalprovenanceanalysisofunstructuredprocesses,”ACMTrans.
youdo:Mimicryattacksagainstprovenancegraphhostintrusiondetection InternetTechnol.,vol.17,no.4,pp.1–24,2017.
systems,”inProc.30thAnnu.Netw.Distrib.Syst.Secur.Symp.,SanDiego, [48] M.Backes,S.Bugiel,andS.Gerling,“Scippa:System-centricIPCprove-
CA,USA,2023. nanceonandroid,”inProc.30thACMAnnu.Comput.Secur.Appl.Conf.,
[24] M.A.Vieira,M.S.Castanho,R.D.Pacıf´ico,E.R.Santos,E.P.C.Júnior, 2014,pp.36–45.
andL.F.Vieira,“FastpacketprocessingwitheBPFandXDP:Concepts, [49] D.J.Pohly,S.McLaughlin,P.McDaniel,andK.Butler,“Hi-Fi:Collect-
code,challenges,andapplications,”ACMComput.Surv.,vol.53,no.1, ing high-fidelity whole-system provenance,” in Proc. 28th ACM Annu.
pp.1–36,2020. Comput.Secur.Appl.Conf.,2012,pp.259–268.
[25] L.Security,“UseofeBPFasamoresecurealternativetokernellevel [50] C. Collberg, A. Gibson, S. Martin, N. Shinde, A. Herzberg, and
observability,” Jan. 2022, Accessed: Feb. 4, 2025. [Online]. Available: H. Shulman, “Provenance of exposure: Identifying sources of leaked
https://redcanary.com/blog/ebpf-for-security/ documents,” in Proc. IEEE Conf. Commun. Netw. Secur., 2013,
[26] B. Gregg, “Learning eBPF and BCC,” Jan. 2019, Accessed: Feb. pp.367–368.
4,2025.[Online].Available:https://www.brendangregg.com/blog/2019- [51] A.RamachandranandM.Kantarcioglu,“Smartprovenance:Adistributed,
01-01/learn-ebpf-tracing.html blockchainbaseddataprovenancesystem,”inProc.8thACMConf.Data
[27] T.L.Foundation,“ThestateofeBPF,”Jan.2024,Accessed:Feb.4,2025. Appl.Secur.Privacy,2018,pp.35–42.
[Online]. Available: https://www.linuxfoundation.org/hubfs/eBPF/The_ [52] M. Markakis et al., “Sawmill: From logs to causal diagnosis of large
State_of_eBPF.pdf systems,”inProc.Int.Conf.Manage.Data,2024,pp.444–447.
[28] F.Neves,N.Machado,R.Vilaça,andJ.Pereira,“Horus:Non-intrusive [53] T.Esteves,F.Neves,R.Oliveira,andJ.Paulo,“Cat:Content-awaretracing
causalanalysisofdistributedsystemslogs,”inProc.51stAnnu.IEEE/IFIP andanalysisfordistributedsystems,”inProc.22ndACMInt.Middleware
Int.Conf.DependableSyst.Netw.,2021,pp.212–223. Conf.,2021,pp.223–235.
[29] C. Liu, Z. Cai, B. Wang, Z. Tang, and J. Liu, “A protocol- [54] Y. Han et al., “Holistic root cause analysis for failures in cloud-native
independent container network observability analysis system based on systemsthroughobservabilitydata,”IEEETrans.Serv.Comput.,vol.17,
eBPF,” in Proc. IEEE 26th Int. Conf. Parallel Distrib. Syst., 2020, no.6,pp.3789–3802,Nov./Dec.2024.
pp.697–702. [55] P.Chen,Y.Qi,andD.Hou,“Causeinfer:Automatedend-to-endperfor-
[30] J. Levin and T. A. Benson, “ViperProbe: Rethinking microservice ob- mancediagnosiswithhierarchicalcausalitygraphincloudenvironment,”
servabilitywitheBPF,”inProc.IEEE9thInt.Conf.CloudNetw.,2020, IEEETrans.Serv.Comput.,vol.12,no.2,pp.214–230,Mar./Apr.2019.
pp.1–8. [56] “Datadog-logcollectionandintegrations,”Accessed:Feb.4,2025.[On-
[31] F.Nevesetal.,“Falcon:Apracticallog-basedanalysistoolfordistributed line]. Available: https://docs.datadoghq.com/logs/log_collection/?tab=
systems,” in Proc. 48th Annu. IEEE/IFIP Int. Conf. Dependable Syst. host
Netw.,2018,pp.534–541. [57] “Dynatrace-loganalytics,”2023.Accessed:Feb.4,2025.[Online].Avail-
[32] Y.Ganetal.,“Anopen-sourcebenchmarksuiteformicroservicesandtheir able:https://docs.dynatrace.com/docs/analyze-explore-automate/logs
hardware-softwareimplicationsforcloud&edgesystems,”inProc.24th [58] “New relic - get started with log management,” 2019. Accessed: Feb.
Int.Conf.ArchitecturalSupportProgram.Lang.OperatingSyst.,2019, 4, 2025. [Online]. Available: https://docs.newrelic.com/docs/logs/get-
pp.3–18. started/get-started-log-management/
[33] A.Security,“Tracee|Github,”Jun.2024,Accessed:Feb.4,2025.[Online]. [59] “Understanding container monitoring: Best practices and tools,” 2021.
Available:https://github.com/aquasecurity/tracee Accessed:Feb.4,2025.[Online].Available:https://www.aquasec.com/
[34] M.A.Inametal.,“SoK:Historyisavastearlywarningsystem:Auditing cloud-native-academy/docker-container/container-monitoring/#section-
theprovenanceofsystemintrusions,”inProc.IEEESymp.Secur.Privacy, 2
2023,pp.2620–2638. [60] X.Zhaoetal.,“lprof:Anon-intrusiverequestflowprofilerfordistributed
[35] D.Huye,Y.Shkuro,andR.R.Sambasivan,“LiftingtheveilonMeta’s systems,”inProc.11thUSENIXSymp.OperatingSyst.Des.Implementa-
microservicearchitecture:Analysesoftopologyandrequestworkflows,” tion,2014,pp.629–644.
inProc.USENIXAnnu.Tech.Conf.,2023,pp.419–432. [61] X.Zhao,K.Rodrigues,Y.Luo,D.Yuan,andM.Stumm,“Non-intrusive
[36] B. Debnath et al., “LogLens: A real-time log analysis system,” performanceprofilingforentiresoftwarestacksbasedontheflowrecon-
in Proc. IEEE 38th Int. Conf. Distrib. Comput. Syst., 2018, structionprinciple,”inProc.12thUSENIXSymp.OperatingSyst.Des.
pp.1052–1062. Implementation,2016,pp.603–618.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore. Restrictions apply.

SATAPATHYetal.:XPLOG:ADYNAMICOBSERVABILITYFRAMEWORKFORDISTRIBUTEDSANDBOXEDMICROSERVICES 807
[62] M. Bonola et al., “Faster software packet processing on FPGA NICs HarshBorsereceivedtheBTechdegreeincomputer
witheBPFprogramwarping,”inProc.USENIXAnnu.Tech.Conf.,2022, scienceandengineeringfromtheAcropolisInstitute
pp.987–1004. of Technology, India. He is currently working to-
[63] S. Miano, F. Risso, M. V. Bernal, M. Bertrone, and Y. Lu, “A frame- wardthemaster’sdegreewiththeIndianInstituteof
work for eBPF-based network functions in an era of microservices,” Technology,Kharagpur,India.Hisresearchinterests
IEEE Trans. Netw. Service Manag., vol. 18, no. 1, pp. 133–151, includeanomalydetection,distributedsystems,and
Mar.2021. machinelearning.HarshisamemberofIEEEand
[64] Y.Zhou,Z.Wang,S.Dharanipragada,andM.Yu,“Electrode:Accelerating IEEECommunicationsSociety.
distributedprotocolswitheBPF,”inProc.20thUSENIXSymp.Networked
Syst.Des.Implementation,2023,pp.1391–1407.
[65] Y. Zhong et al., “XRP: In-kernel storage functions with eBPF,” in
Proc.16thUSENIXSymp.OperatingSyst.Des.Implementation,2022,
pp.375–393.
[66] M.Jadin,Q.D.Coninck,L.Navarre,M.Schapira,andO.Bonaventure,
“LeveragingeBPFtomakeTCPpath-aware,”IEEETrans.Netw.Service Rajat Bachhawat received the BTech degree in
Manage.,vol.19,no.3,pp.2827–2838,Sep.2022. computer science and engineering from the Indian
[67] C.Cassagnes,L.Trestioreanu,C.Joly,andR.State,“TheriseofeBPF Institute of Technology Kharagpur, India, in 2023.
for non-intrusive performance monitoring,” in Proc. IEEE/IFIP Netw. He is currently a systems engineer with Quadeye.
OperationsManage.Symp.,2020,pp.1–7. His research interests include computer networks,
[68] Tetragon,“Tetragon|github,”Apr.2023,Accessed:Feb.5,2025.[Online]. operating systems, distributed systems, and tracing
Available:https://github.com/cilium/tetragon technologies.
[69] A.Ahmad,S.Lee,andM.Peinado,“HARDLOG:Practicaltamper-proof
systemauditingusinganovelauditdevice,”inProc.43thIEEESymp.
Secur.Privacy,2022,pp.1791–1807.
[70] C.Yao,D.Agrawal,G.Chen,B.C.Ooi,andS.Wu,“Adaptivelogging:Op-
timizingloggingandrecoverycostsindistributedin-memorydatabases,”
inProc.17thInt.Conf.Manage.Data,2016,pp.1119–1134.
[71] S.Maetal.,“Kernel-supportedcost-effectiveauditloggingforcausality NehaDalmiareceivedthebachelor’sandmaster’s
tracking,”inProc.USENIXAnnu.Tech.Conf.,2018,pp.241–254.
degreesincomputerscienceandengineeringfromthe
[72] J.Lockermanetal.,“TheFuzzyLog:Apartiallyorderedsharedlog,”in IndianInstituteofTechnologyKharagpur,India.She
Proc.13thUSENIXSymp.OperatingSyst.Des.Implementation,2018,
iscurrentlyasystemsengineerwithQuadeye.Her
pp.357–372. research interests include distributed systems, low-
[73] S.Boucher,A.Kalia,D.G.Andersen,andM.Kaminsky,“Puttingthe latencyC++dev,andtraveling.
‘micro’backinmicroservice,”inProc.Conf.UsenixAnnu.Tech.Conf.,
2018,pp.645–650.
[74] S. Wang, Z. Ding, and C. Jiang, “Elastic scheduling for microservice
applicationsinclouds,”IEEETrans.ParallelDistrib.Syst.,vol.32,no.1,
pp.98–115,Jan.2021.
[75] A.Arora,S.Kulkarni,andM.Demirbas,“Resettablevectorclocks,”in
Proc.19thAnnu.ACMSymp.Princ.Distrib.Comput.,2000,pp.269–278. SubhrenduChattopadhyayreceivedtheMTechand
[76] M.Raynal,“Aboutlogicalclocksfordistributedsystems,”ACMSIGOPS PhDdegreesfromtheIndianInstituteofTechnology
OperatingSyst.Rev.,vol.26,no.1,pp.41–48,1992. Guwahati.Heiscurrentlyanassistantprofessorwith
[77] V.Estivill-CastroandD.Wood,“Asurveyofadaptivesortingalgorithms,” theThaparInstituteofEngineeringandTechnology,
ACMComput.Surv.,vol.24,no.4,pp.441–476,1992. India. His research interests include computer net-
[78] Y.Tokusashi,H.T.Dang,F.Pedone,R.Soulé,andN.Zilberman,“The works,operatingsystems,anddistributedcomputing.
caseforin-networkcomputingondemand,”inProc.14thACMEuroSys Dr.SubhrenduisaMemberIEEECommunications
Conf.,2019,pp.1–16. SocietyandAssociationforComputingMachinery
[79] N.Hu,Z.Tian,X.Du,andM.Guizani,“Anenergy-efficientin-network
computingparadigmfor6G,”IEEETrans.GreenCommun.Netw.,vol.5,
no.4,pp.1722–1733,Dec.2021.
Sandip Chakraborty (Senior Member, IEEE) re-
ceivedthebachelor’sdegreefromJadavpurUniver-
sity,Kolkata,in2009,andtheMTechandPhDde-
greesfromIITGuwahati,in2011and2014,respec-
tively.Heiscurrentlyanassociateprofessorwiththe
Utkalika Satapathy (Member, IEEE) received the DepartmentofComputerScienceandEngineering,
master’s degree from the International Institute of IndianInstituteofTechnologyKharagpurandleading
InformationTechnology,Bhubaneswar,India.Sheis theUbiquitousNetworkedSystemsLab(UbiNet–
currently working toward the PhD degree with the https://ubinet-iitkgp.github.io/ubinet/).Hisresearch
IndianInstituteofTechnology,Kharagpur,India.Her interestsincludedistributedsystems,pervasive,ubiq-
researchinterestsincludedistributedsystems,operat- uitous,edgecomputing,andhuman-computerinter-
ingsystems,andobservability.Utkalikaisamember actions.HeistheAreaEditorofIEEETransactionsonServicesComputing,
oftheIEEEandIEEECommunicationsSociety. Elsevier Ad Hoc Networks, and Elsevier Pervasive and Mobile Computing
journals.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:40:10 UTC from IEEE Xplore. Restrictions apply.