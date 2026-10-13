ReceivedFebruary20,2020,acceptedFebruary26,2020,dateofpublicationMarch2,2020,dateofcurrentversionMarch12,2020.
DigitalObjectIdentifier10.1109/ACCESS.2020.2977464
A Framework of Virtual War Room and Matrix
Sketch-Based Streaming Anomaly Detection
for Microservice Systems
HONGYANGCHEN ,PENGFEICHEN,ANDGUANGBAYU
SchoolofDataandComputerScience,SunYat-senUniversity,Guangzhou510006,China
Correspondingauthor:PengfeiChen(chenpf7@mail.sysu.edu.cn)
TheworkwassupportedinpartbytheNationalKeyResearchandDevelopmentPlanunderGrant2019YFB1804002,inpartbythe
NationalNaturalScienceFoundationofChinaunderGrant61802448,Grant6190244,andGrantU1811462,andinpartbythe
ProgramforNaturalScienceFoundationofGuangdongunderGrant2019A1515012229.
ABSTRACT Recently,microservicehasbeenapopulararchitecturetoconstructcloud-nativesystems.This
novelarchitecturebringsagilityandacceleratesthesoftwaredevelopmentprocesssignificantly.However,
itisnoteasytomanageandoperatemicroservicesystemsduetotheirscaleandcomplexity.Manyapproaches
areproposedtoautomaticallyoperatemicroservicesystemssuchasanomalydetection.Nevertheless,those
methods cannot be sufficiently validated and compared due to a lack of real microservice systems, which
leads to the slow process of intelligent operation. These challenges inspire us to build a system named
‘‘VWR’’, a framework of Virtual War Room for operating microservice applications which allows users
to simulate their microservice architectures with low overhead and inject multiple types of faults into the
microservice system with chaos engineering. VWR can mimic user requests and record the end-to-end
tracing data (i.e., service call chains) for each request in a way consistent with OpenTracing. With easily
designed tests and the produced streaming tracing data, the users can validate the performance of their
intelligent operation algorithms and improve the algorithms as needed. Besides, based on the streaming
tracingdatageneratedbyVWR,weintroduceanovelunsupervisedanomalydetectionalgorithmbasedon
Matrix Sketch and set it as a default intelligent operation algorithm in VWR. This algorithm can detect
anomalies by analyzing high-dimensional performance data collected from a microservice system in a
streamingmanner.TheexperimentalresultinVWRshowsthatthematrixsketchbasedmethodcanprecisely
detectanomaliesinmicroservicesystemsandoutperformsomewidelyusedanomalydetectionmethodssuch
asisolationforestinsomescenario.Webelievemoreapproachesontheintelligentoperationofmicroservice
systemscanbeconstructedbasedonVWR.
INDEXTERMS Microservice,virtualwarroom,matrixsketch,anomalydetection,chaosengineering.
I. INTRODUCTION softwarebugsorruntimeenvironmentchanges[2],[3].What
Nowadays, the microservice has become a widely adopted isworse,ifafaulthappensinamicroservicearchitecture,itis
architectureforenterprisestodeploytheirlargecloud-native more difficult for operators to locate root causes due to the
applications.Withthemicroservicearchitecture,alargesoft- increasing complexity of service dependencies. Any single
ware application is decoupled into a suite of independent, problem in a service such as a hard disk fault or a network
distributed,andlooselycoupledservicesthatcanbeallowed disconnection may cause the microservice system to break-
to implement in different programming languages and can down.Inordertodetectanomalies,infertherootcauseand
also be managed by different teams [1]. However, we have restorethefailedserviceassoonaspossible,operatorsrelyon
tonoticethatnomatterwhicharchitectureweusetodeploy tracingsystemssuchasX-trace[4],Zipkin[5]toprofileand
our application, faults and problems are inevitable due to monitorthemicroservicearchitecture.Thesetracingsystems
can record the execution path of each request. With these
The associate editor coordinating the review of this manuscript and information,thecomplexityofamicroservicesystemcanbe
approvingitforpublicationwasDongWang . managed.
VOLUME8,2020 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttp://creativecommons.org/licenses/by/4.0/ 43413

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
Extensive studies have been done to resolve performance (i.e.,normalandabnormal)tousersandprovideaplatform3
problems in distributed systems such as anomaly detection for users to test their intelligent operation algorithms with
[6]–[8], root cause analysis [2], [9]–[11]. In these studies, theproduceddata.VWRisinspiredbytheconceptof‘‘war
theresearchersneedtodeploytheirownmicroservicebench- room’’ which is a battlefield where the army leaders can
marks and inject some faults into these systems in order get together to simulate any possible problems and propose
to get abnormal cases. Otherwise, they need some existing the corresponding methods. In IT and Internet companies,
performance data provided by commercial enterprises or there are also war rooms to resolve problems coming from
communities.However,thisapproachposessomechallenges online systems. Similarly, we construct a virtual war room
forresearchers: without real systems to test the efficiency and effectiveness
• Veryfewmicroservicebenchmarks.Itisalwaysnec- ofsomeintelligentoperationalgorithms.However,combing
essarytohavemicroservicebenchmarkstovalidatethe theconceptofwarroomandthemicroservice,wefindithard
efficiency of intelligent operation methods. However, forustosimulatefaultsinmicroservicesystemsduetolackof
thereareveryfewopensourcemicroservicebenchmark- microservicebenchmarksandfaultinjectiontools.Therefore,
ingsystemsexceptsomesimplearchitectures,likeSock- we build a digital version of microservice systems in VWR
shop[12].Itistime-consumingandevenunfeasiblefor bysimulatingthebehaviorofeveryserviceinamicroservice
researcherstodesignanddeploytheirownmicroservice system and defining the communication protocol between
systemsatscale. each service. By moving microservice from reality to the
• A high cost in distributed tracing. A large scale digital world, the researchers can be allowed to run any
microservicesystemalwayscomprisesnumerousinter- microservicesystemsassoonaspossibleandinjectanyfaults
connected services. To operate and understand their toanyserviceofthesystemswhichcanhelpthemobservethe
behavior,adistributedtracingwhichrecordstheexecu- actionofthemicroserviceandfindawaytodetectandlocate
tion paths of each request has been a default module. faults.Afterthesimulation,byuploadingtheiralgorithmsto
However,thetracingsystemetherrequirescodeinstru- theplatform,theresearcherscantesttheperformanceoftheir
mentation into the application and modifications of algorithms with the produced tracing data on VWR before
therun-timeenvironmentwhichmeansthatresearchers applyingthemtoarealsystem.
needtobefamiliarwiththebenchmarkandinstrument Anomaly detection is a typical kind of intelligent opera-
codesontheirown. tion.However,existingapproacheshaveshortcomingstoana-
• Difficulty in fault injection. In reality, the cases of lyzethehigh-dimensionalstreamingtracingdata.Inaddition
faultsandanomaliesarefewerthannormalcases.Tocol- to building VWR, we leverage VWR to analyze the tracing
lectmoreabnormalcases,wealwaysrelyonfaultinjec- data and study the performance of some anomaly detection
tion to mimic faults. Therefore, some fault injection algorithms. Moreover, we introduce an anomaly detection
tools are needed. There are some methods and existed algorithm based on randomized Matrix Sketch to resolve
toolsfortheresearcherstoconductachaosengineerlike the challenge brought by high-dimensional streaming trace
NetflixChaosMonky[13],[14],andIstio[15].However, data.Aftervalidatingitseffectiveness,wesetitasadefault
itisstillanannoyingtaskinmicroservicesystemsdue anomaly detection strategy in VWR. The effectiveness of
totheirscaleandcomplexity. thisanomalydetectionalgorithmisvalidatedandcompared
• Alargevolumeofchaostracingdata.Althoughmany againstIsolationForestandSupportVectorMachine(SVM)
existingreal-worldmicroservicesystemshavecollected basedmethods.TheexperimentresultsshowthatVWRcan
a large volume of tracing data, these tracing data are be a good simulation benchmark for microservice systems
always chaos with a lot of noises and errors such as and Matrix Sketch outperforms other anomaly detection
missingdata,disorderedeventsequences,andincorrect methodsinastreamingdetectionmode.
measurement values. Due to these chaos, it is nontriv- Beyondanomalydetection,VWRcanalsobeleveragedto
ial to find efficient algorithms to operate microservice validateotherintelligentoperationalgorithmssuchasperfor-
systems. Moreover, most of collected tracing data are mance prediction, root cause analysis, and so on. However,
not labeled with ‘‘normal’’ or ‘‘abnormal’’. These data thesealgorithmsareoutofscopeofthispaper.Wewillextend
are collected in a streaming manner which should be ourresearchbyconsideringrootcauseanalysisinthefuture
processedintime. work.
To address the aforementioned challenges and shortages Generally speaking, the contributions of this paper are
of previous work, we propose Virtual War Room(VWR)
three-fold:
based on Spigo,1 a framework to mimic the behavior of • We firstly propose the concept ‘‘Virtual War Room’’
the microservice architecture and to inject faults readily which helps researchers to observe the behavior of the
with chaos engineering [13], which has been open sourced microservice system and to validate the effectiveness
in the Github. VWR2 can deliver tracing data with labels and performance of their intelligent operation algo-
rithms.
1Spigo:https://github.com/adrianco/spigo
2VWRbackend:https://github.com/chenhy97/sysu_VWR 3VWRfrontend:https://github.com/chenhy97/VWR_front
43414 VOLUME8,2020

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
• Wedesignanddevelop‘‘VWR’’tomimicrealmicroser- on the dependency graph which does not need the tracing
vice systems digitally for simulation, tracing, chaos data. Microscope [10] depends on the system calls it inter-
engineering and fault analysis. Moreover, the labeled cepts on Network to build dependency graphs and use SLO
tracingdataproducedbytheplatformcanhelptheevo- metricstofindtherootcause.NetMedic[23]inferstheroot
lutionofresearchonanomalydetectionalgorithms. cause by constructing component dependencies with preset
• Weintroduceanunsupervisedanomalydetectionalgo- templates.Although,wedonotintroducerootcauseanalysis
rithm based on Matrix Sketch to detect anomalies in inthispaper,VWRcanprovidealargevolumeoftracingdata
microservice systems. This algorithm works in a real- tovalidatetheeffectivenessandefficiencyofthoserootcause
time mode and analyzes the high-dimension run-time analysisapproaches.
data.Itcanachieveacomparativeresult.
|     |     |     |     |     |     |     |     | B. ANOMALYDETECTION |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Thispaperisorganizedasfollows.InSection2,wepresent
therelatedwork.InSection3,weintroducethesystemdesign Anomaly detection is a well-studied topic and there are
|             |         |                  |           |             |         |            |         | many approaches |              | such           | as the          | method  | we introduce |                 | from    |
| ----------- | ------- | ---------------- | --------- | ----------- | ------- | ---------- | ------- | --------------- | ------------ | -------------- | --------------- | ------- | ------------ | --------------- | ------- |
| of VWR.     | Section | 4 introduces     |           | the details | of      | the        | anomaly |                 |              |                |                 |         |              |                 |         |
|             |         |                  |           |             |         |            |         | [24]. Reference |              | [24] is        | an unsupervised |         | technique    |                 | that is |
| detection   | method  | based            | on Matrix | Sketch.     | Section |            | 5 shows |                 |              |                |                 |         |              |                 |         |
|             |         |                  |           |             |         |            |         | suitable        | for the      | high-dimension |                 | data    | in real-time | applica-        |         |
| the results | of      | the experimental |           | evaluation. |         | In Section | 6,      |                 |              |                |                 |         |              |                 |         |
|             |         |                  |           |             |         |            |         | tions. The      | state-of-art |                | approach        | IForest | [25]         | is an efficient |         |
weconcludethispaper.
|     |     |     |     |     |     |     |     | method | that is | not suitable | for | real-time | scenarios. | What | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------------ | --- | --------- | ---------- | ---- | --- |
more,someothersupervisedapproacheshavebeenproposed
II. RELATEDWORK for anomaly detection such as [26] and [27] which needs
| Previous | studies | have attempted |     | to use | system | simulator | to  |     |     |     |     |     |     |     |     |
| -------- | ------- | -------------- | --- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
labeleddata.
| gain knowledge |     | on performance/resource |     |     | trade-offs |     | in sys- |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------------------- | --- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
temsthatcareaboutrequestlatency.Therearetwoclassical
|     |     |     |     |     |     |     |     | C. MICROSERVICEBENCHMARKSFORTRACE-BASED |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
simulationsystemsthatareclosetoVWR,namely,BigHouse
APPROACH
[16]andµqSim[17].BigHouseisanevent-drivenqueueing
Forthoseapproachesofrootcauseanalysisoranomalydetec-
| simulator  | targeting | datacenter |     | service | simulation | using    | pre- |         |              |          |     |      |         |         |      |
| ---------- | --------- | ---------- | --- | ------- | ---------- | -------- | ---- | ------- | ------------ | -------- | --- | ---- | ------- | ------- | ---- |
|            |           |            |     |         |            |          |      | tion on | microservice | systems, |     | most | of them | have to | rely |
| calculated | workload  | models     | and | system  | models.    | However, |      |         |              |          |     |      |         |         |      |
onmicroservicebenchmarks.Thereareseveralbenchmarks
| BigHouse | only | models | each application |     | as  | a single | queue |     |     |     |     |     |     |     |     |
| -------- | ---- | ------ | ---------------- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
beingreleasedfromacademiaorindustry,suchasCloudsuite
andsomeintra-microservicestagescannotbecapturedbya
|               |     |              |            |     |                 |     |      | [28], Tailbench  |     | [29], Sirius | [30]. | However, | the       | limitation | of  |
| ------------- | --- | ------------ | ---------- | --- | --------------- | --- | ---- | ---------------- | --- | ------------ | ----- | -------- | --------- | ---------- | --- |
| single queue, |     | causing poor | simulation |     | of microservice |     | sys- |                  |     |              |       |          |           |            |     |
|               |     |              |            |     |                 |     |      | these benchmarks |     | is that      | they  | only pay | attention | on single- |     |
tems.Toaddresstheproblem,µqSimtakesadifferentmethod
|                |          |             |                    |     |            |            |         | tier applications, |      | or at   | most         | three-tiers | services, | which         | is  |
| -------------- | -------- | ----------- | ------------------ | --- | ---------- | ---------- | ------- | ------------------ | ---- | ------- | ------------ | ----------- | --------- | ------------- | --- |
| by explicitly  | modeling |             | each application’s |     | execution  |            | phases, |                    |      |         |              |             |           |               |     |
|                |          |             |                    |     |            |            |         | different          | from | the way | microservice |             | systems   | are deployed. |     |
| and accounting |          | for queuing | effects            |     | throughout | execution. |         |                    |      |         |              |             |           |               |     |
DeathstarBench[31]focusesondeployinglarge-scaleappli-
µqSim
| What is       | more,    |     | supports   | user-defined |       | microservice |     |           |              |           |        |           |        |                |       |
| ------------- | -------- | --- | ---------- | ------------ | ----- | ------------ | --- | --------- | ------------ | --------- | ------ | --------- | ------ | -------------- | ----- |
|               |          |     |            |              |       |              |     | cations   | with several | different |        | services, | which  | allows         | us to |
| architecture. | However, |     | the target | of           | µqSim | and BigHouse |     |           |              |           |        |           |        |                |       |
|               |          |     |            |              |       |              |     | study the | performance  |           | effect | that only | exists | in large-scale |       |
is to get insight on performance of distributed systems and systems. What is more, DeathstarBench is designed with
| they are    | not able      | to produce  | large | volume     | of        | labeled      | trac- |                   |           |         |             |          |         |                |        |
| ----------- | ------------- | ----------- | ----- | ---------- | --------- | ------------ | ----- | ----------------- | --------- | ------- | ----------- | -------- | ------- | -------------- | ------ |
|             |               |             |       |            |           |              |       | five microservice |           | systems | integrated  |          | with    | tracing system |        |
| ing data    | immediately.  | What        | is    | more,      | VWR       | provides     | chaos |                   |           |         |             |          |         |                |        |
|             |               |             |       |            |           |              |       | which is          | helpful   | for the | researches  |          | [32] on | artificial     | oper-  |
| engineering | for           | users which | is    | another    | important | aspect       | for   |                   |           |         |             |          |         |                |        |
|             |               |             |       |            |           |              |       | ation algorithm   |           | based   | on tracing. | However, |         | because        | of the |
| research    | on artificial | operation   |       | algorithms | on        | microservice |       |                   |           |         |             |          |         |                |        |
|             |               |             |       |            |           |              |       | challenges        | mentioned | in      | Section     | I, VWR   | is      | another impor- |        |
systems.
|     |     |     |     |     |     |     |     | tant tool. | Compared | to  | them, | VWR | does not | need | to be |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ----- | --- | -------- | ---- | ----- |
Furthermore,artificialoperationsonmicroservicesystems
|     |     |     |     |     |     |     |     | deployed | in a | real distributed |     | environment. |     | With its | help, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------------- | --- | ------------ | --- | -------- | ----- |
suchasanomalydetectionandRootcauseanalysisarechal-
|     |     |     |     |     |     |     |     | you can | run any | microservice |     | systems | on one | machine | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | ------- | ------ | ------- | --- |
lengingtopics.Extensiveapproacheshavebeenproposedto
conductanyexperimentswithchaosengineeringwithavery
| detect anomalies |     | or to | pinpoint | root causes. |     | However, | there |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | -------- | ------------ | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
limitedcost.
| are still | some | challenges, | such | as the | lack | of benchmarks |     |     |     |     |     |     |     |     |     |
| --------- | ---- | ----------- | ---- | ------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forevaluationexperiments.Inthefollowing,wepresentthe
|     |     |     |     |     |     |     |     | III. SYSTEMDESIGN |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
relatedworkbriefly.
|     |     |     |     |     |     |     |     | A. SYSTEMOVERVIEW |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
TheoverallsystemdesignofVWRisshowedinFig.1.Once
A. ROOTCAUSEANALYSIS the architecture definition file of a microservice system is
Themainmethodofthisareaarebasedonend-to-endrequest uploadedbytheuserandrunningparametersincludingsim-
tracing. There are lots of work and systems designing to ulation time are configured, then VWR can be launched.
instrument source code, collect tracing data, and find out Thesimulationstartswhilethetracingdataareproducedand
requestswithlongresponselatencysuchasMagpie[18],X- stored in a local file. When the simulation starts, VWR can
trace[4],Pinpoint[19],TheMysteryMachine[20].Basedon visualize the microservice architecture and help users run
thesufficienttracingdata,[21],[22]pinpointssystemprob- some algorithms to detect anomalies. The core functions of
lems by comparing traces. Another main approach depends VWRarelistedasfollowed.
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 43415 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
|     |     |     |     |     |     |     | components                    | of        | the continuously                      |          | generated             | streaming |            | data.  |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --------- | ------------------------------------- | -------- | --------------------- | --------- | ---------- | ------ |
|     |     |     |     |     |     |     | The core                      | of Matrix | Sketch                                |          | is PCA (Primary       |           | Components |        |
|     |     |     |     |     |     |     | Analysis)                     | [33]      | which                                 | consists | of three              | parts.    | The first  | one    |
|     |     |     |     |     |     |     | is encoding                   | the       | original                              | data     | ( i.e., a large       | matrix    | M)         | into a |
|     |     |     |     |     |     |     | smallermatrixN                |           | whichhasthefeaturesoftheoriginaldata. |          |                       |           |            |        |
|     |     |     |     |     |     |     | ThesecondoneisusingthematrixN |           |                                       |          | tocalculatetheanomaly |           |            |        |
scoreforeverydatapointofthecomingdata.Thethirdone
|     |     |     |     |     |     |     | is labeling | the | data point | with | a high | score as | an anomaly |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---- | ------ | -------- | ---------- | --- |
andusethemtoupdatethematrixN.MatrixSketchwillbe
FIGURE1. Frameworkofvirtualwarroom.
introducedindetailinSectionIV.
1) ARCHFILE
B. SYSTEMDETAILS
Fig.2isthreearchfilesforAWS,NetflixandLAMPwhich
1) SIMULATOR
canhelpuserstoseehowtodefineanarchitecturethatcanbe
a: KEYCOMPONENTS
| simulated | on VWR. | In the | arch file, | users | set the | simulated |     |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ---------- | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Tosupportthesimulation,thesimulatorhassomekeycompo-
| architecture’s | name | by the | ‘‘arch’’ | parameter. | Services | of  |     |     |     |     |     |     |     |     |
| -------------- | ---- | ------ | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nents,andthedesignofthesimulatorisshowninFig.3.Four
| the simulated | architecture |     | are recorded | by  | the | ‘‘services’’ |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
keycomponentswillbeintroducedindetailinthefollowing.
| parameter. | The ‘‘name’’ |     | parameter | records | each | service’s |               |     |      |          |         |                  |     |      |
| ---------- | ------------ | --- | --------- | ------- | ---- | --------- | ------------- | --- | ---- | -------- | ------- | ---------------- | --- | ---- |
|            |              |     |           |         |      |           | • ‘‘parser’’: |     | Once | the user | uploads | the architecture |     | def- |
name,the‘‘package’’parameterstipulatesthebehavioreach
|         |              |            |     |               |     |           | inition | file | to the | simulator, | ‘‘parser’’ | will | parse | the |
| ------- | ------------ | ---------- | --- | ------------- | --- | --------- | ------- | ---- | ------ | ---------- | ---------- | ---- | ----- | --- |
| service | takes during | simulation | and | the ‘‘count’’ |     | parameter |         |      |        |            |            |      |       |     |
recordsthenumberofeachservice.Theconnectionbetween architecture and send the architecture configuration to
‘‘asgard’’.Inthedefinitionfile,theuserneedstoillus-
servicesisconfiguredbythe‘‘dependencies’’parameter.
|     |     |     |     |     |     |     | trate | the name | of  | the service, | the     | number  | of instances |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ------------ | ------- | ------- | ------------ | --- |
|     |     |     |     |     |     |     | per   | service, | the | type of      | service | and the | architecture |     |
2) SIMULATION
topology.
| In the simulation | stage, | VWR | needs | to parse | the | uploaded |     |     |     |     |     |     |     |     |
| ----------------- | ------ | --- | ----- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
microservicearchitecturedefinitionfilesandsettherunning • ‘‘asgard’’:Accordingtothereceivedarchitecturecon-
|            |                     |     |       |       |               |      | figuration, |     | ‘‘asgard’’ | will | spawn | every needed |     | service |
| ---------- | ------------------- | --- | ----- | ----- | ------------- | ---- | ----------- | --- | ---------- | ---- | ----- | ------------ | --- | ------- |
| parameters | for the simulation. |     | After | that, | the simulator | will |             |     |            |      |       |              |     |         |
simulatethebehaviorofimportantservicesinthemicroser- instanceandhelpalltheinstancestobuildtheirdepen-
dencylists.ThesimulatorofVWRsupportswellupto
| vice system | such as | a database, | a   | load balancer |     | and so on. |         |             |     |         |           |     |       |       |
| ----------- | ------- | ----------- | --- | ------------- | --- | ---------- | ------- | ----------- | --- | ------- | --------- | --- | ----- | ----- |
|             |         |             |     |               |     |            | 100,000 | independent |     | service | instances | in  | a few | GB of |
Thetracingdatawillbeproducedandstoredtomakefurther
| analysis. |     |     |     |     |     |     | RAM.Afterspawningalltheneededserviceinstances, |           |      |       |             |      |      |        |
| --------- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --------- | ---- | ----- | ----------- | ---- | ---- | ------ |
|           |     |     |     |     |     |     | these                                          | instances | will | begin | to interact | with | each | others |
3) FAULTINJECTION usingthecommunicationprotocolandproducethecom-
|        |                 |     |                 |     |           |      | munication |     | data. | The communication |     | protocol |     | will be |
| ------ | --------------- | --- | --------------- | --- | --------- | ---- | ---------- | --- | ----- | ----------------- | --- | -------- | --- | ------- |
| During | the simulation, | the | fault injection |     | component | will |            |     |       |                   |     |          |     |         |
introducedindetailinSectionIII-B.1.c.
| receiveinjectionrequestsfrom |     |     | usersandinjectfaultstothe |     |     |     |                  |     |        |     |             |     |              |     |
| ---------------------------- | --- | --- | ------------------------- | --- | --- | --- | ---------------- | --- | ------ | --- | ----------- | --- | ------------ | --- |
|                              |     |     |                           |     |     |     | • ‘‘collector’’: |     | During | the | simulation, | all | the produced |     |
simulationsystem.
communicationdataarecollectedandconvertedintothe
4) VISUALIZATION form of tracing data by ‘‘collector’’. After that, ‘‘col-
|     |     |     |     |     |     |     | lector’’ | will | writes | these | data to | a write-only | log | file. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | ----- | ------- | ------------ | --- | ----- |
Inthevisualizationstage,therearetwoprimarytasksneeded
‘‘collector’’alsoleveragesadataforwardertoolnamed
tobehandled.Firstofall,whenthemicroservicearchitecture
|     |     |     |     |     |     |     | filebeat | [34] | to  | fetch the | change | of this | log file | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | --------- | ------ | ------- | -------- | --- |
fileisparsed,thevisualizationcomponentwillvisualizethe
feedthenewaddeddataintoElasticSearchwhichallows
| topology | of the architecture, |     | which | facilitates | users | if they |     |     |     |     |     |     |     |     |
| -------- | -------------------- | --- | ----- | ----------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
userstogetthelatesttracingdatawhenevertheywant.
| need to | inject faults. | Moreover, | when | the | tracing | data is |     |     |     |     |     |     |     |     |
| ------- | -------------- | --------- | ---- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
• ‘‘chaosmonkey’’:VWR’sabilitytoinjectfaultisakey
generated,thevisualizationcomponentwillconvertittotime
feature.Thefaultinjectioncomponentofthesimulator
| series that | can help | users | understand | the | behavior | of the |     |     |     |     |     |     |     |     |
| ----------- | -------- | ----- | ---------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ischaosmonkeywhichwaitsforthefaultrequestsfrom
simulatedmicroserviceandtheeffectofinjectedfaults.
theuser,extractsthefaultinformationfromrequestsand
sendsthefaultmessagetothetargetserviceaccordingto
5) EVALUATION
theparametersinthefaultrequest.Therearethreetypes
| In the evaluation | stage,       | VWR   | will         | detect | anomalies  | in the |           |     |             |     |       |         |            |     |
| ----------------- | ------------ | ----- | ------------ | ------ | ---------- | ------ | --------- | --- | ----------- | --- | ----- | ------- | ---------- | --- |
|                   |              |       |              |        |            |        | of faults | in  | chaosmonkey |     | which | will be | introduced | in  |
| generated         | tracing data | using | the uploaded |        | algorithms | from   |           |     |             |     |       |         |            |     |
detailinSectionIII-B.2.
| the users.   | By default, | VWR     | employs | Matrix | Sketch    | (MS)  |     |     |     |     |     |     |     |     |
| ------------ | ----------- | ------- | ------- | ------ | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| based method | to detect   | anomaly | due     | to the | collected | high- |     |     |     |     |     |     |     |     |
dimensional performance data. When the evaluator receives b: DIFFERENTSIMULATEDSERVICES
thetracingdata,theevaluatorwillpre-processthetracingdata Asweallknow,realmicroservicearchitecturesaremadeup
and convert it to the format that MS needs.Matrix Sketch is of different small services that are responsible for different
an effective and online algorithm that can extract primary singleandsimplefunctions.Tosimulatethebehaviorofthe
| 43416 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME8,2020 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
|     | FIGURE2. | ExamplesofarchfiletosimulateinVWR. |     |     |     |     |                 |                 |        |                |               |
| --- | -------- | ---------------------------------- | --- | --- | --- | --- | --------------- | --------------- | ------ | -------------- | ------------- |
|     |          |                                    |     |     |     |     | • Load Balance: | In microservice |        | systems,       | the load bal- |
|     |          |                                    |     |     |     |     | ancer allows    | designers       | to add | more instances | of their      |
microserviceinawaythatistransparenttoanyservice
consumer,whichgivesdesignersanincreasedcapacity
tohandletheworkload,andalsoreducestheprobability
|     |     |     |     |     |     |     | of a single | host failing.   | Therefore, | we also         | simulated |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ---------- | --------------- | --------- |
|     |     |     |     |     |     |     | it as an    | ‘‘elb’’ service | in our     | simulator which | spreads   |
messagesovermicroservicesinthoseavailablezones.
|     |     |     |     |     |     |     | • Service | registry: In | microservice | systems, | we need |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------------ | -------- | ------- |
FIGURE3. Frameworkofsimulator.
|     |     |     |     |     |     |     | one mechanism | for a | service | instance to | register itself. |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | ----------- | ---------------- |
Weshouldalsohaveawaytodiscovertheserviceonce
| microservice   | systems, | we           | need to build | the | key          | services in |                    |           |           |              |            |
| -------------- | -------- | ------------ | ------------- | --- | ------------ | ----------- | ------------------ | --------- | --------- | ------------ | ---------- |
|                |          |              |               |     |              |             | it is registered.  | There     | are three | main-stream  | dynamic    |
| our simulator. | The      | introduction | about         | the | key services | in a        |                    |           |           |              |            |
|                |          |              |               |     |              |             | service registers: | Zookeeper |           | [35], Consul | and Eureka |
realmicroservicesystemandhowwesimulatetheminVWR
[36].Inoursimulator,wesimulatethebasicfunctionof
areillustratedasbelow.
Eurekawhichrecordsexistingservicesandalsousesa
| • Database: |     | To store | the data and | provide | easy | access |     |     |     |     |     |
| ----------- | --- | -------- | ------------ | ------- | ---- | ------ | --- | --- | --- | --- | --- |
round-robinlookupapproachtodiscovernewservices.
todata,microservicesystemsusethedatabasetoman-
• APIgateway:AnAPIgatewayencapsulatestheinternal
| age | their | data. Furthermore, |     | the key | feature | of the |     |     |     |     |     |
| --- | ----- | ------------------ | --- | ------- | ------- | ------ | --- | --- | --- | --- | --- |
architectureandprovidesanAPIthatistailoredtoeach
microservicesystemislooselycoupled.Therefore,dif-
client.Moreover,itisalsoresponsibleforrequestrout-
| ferent | service | components | may | use different |     | databases |     |     |     |     |     |
| ------ | ------- | ---------- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- |
ingandsoon.Inoursimulator,wesimulateitwiththe
tomanagetheirdata.Therearetwotypesofmain-stream
|            |     |         |              |            |     |        | Zuul [37] | service. Zuul     | is an | open source         | API gateway |
| ---------- | --- | ------- | ------------ | ---------- | --- | ------ | --------- | ----------------- | ----- | ------------------- | ----------- |
| databases, |     | SQL and | NoSQL (e.g., | Cassandra, |     | Redis, |           |                   |       |                     |             |
|            |     |         |              |            |     |        | provided  | by Netflix. which |       | routes the requests | to one      |
etc).AsthoseSQLdatabasesarecentralized.Therefore,
specificservice.
| we  | implement | them | as an individual |     | service | ‘‘store’’ |     |     |     |     |     |
| --- | --------- | ---- | ---------------- | --- | ------- | --------- | --- | --- | --- | --- | --- |
inoursimulatorwhichsupports‘‘Put’’,‘‘GetRequest’’,
andotherdatabaseoperationsinsidethesimulation.For c: THECOMMUNICATIONPROTOCOL
those NoSQL databases, many of them are distributed In practice, the microservice system is always deployed in
andshouldbebuiltasaclustertomanagedata.There- a distributed way. Services usually communicate with each
fore,weimplementedCassandraNoSQLasoneservice otherusingsimpleprotocolssuchasRPCorHTTP.Tosim-
‘‘priamCassandra’’inoursimulatorwhichsupportsdis- ulate these interactions, we construct a simple communica-
tributeddatamanagement. tion protocol by Golang’s channel mechanism. There are
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     | 43417 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
FIGURE4. Differentmicroservicearchitectures.
somedifferenttypesofmessageswhichneedtobeintroduced ‘‘PriamCassandra’’serviceinstance,the‘‘GetRequest’’
indetail. messagewillbeforwardedtootherinstancesofthesame
• Hello: At the beginning, ‘‘Hello’’ messages are sent to servicetosearchforthatvalue.
all service instances to help initialize the configuration • GetResponse: ‘‘GetResponse’’ message simulates the
of these instances. Using Hello message, the service response to the ‘‘GetRequest’’ message. The response
instancecanconfirmitsnameanditsaddressofchannel. containsamessagegeneratedrandomly.
• Namedrop: When all instances are created, ‘‘asgard’’
will send ‘‘Namedrop’’ messages to all service
instances.Asshownbefore,everyserviceinstanceman- 2) CHAOSENGINEERING
ages a dependency service list which records succes- Beyond the simulator of the microservice architecture,
sor service instances’ names and channels. Therefore, we also integrate the fault injector in VWR. Similar to
‘‘Namedrop’’messagessenttoaninstanceshouldcon- the ‘‘ChaosMonkey’’ provided by Netflix, the name of our
taininformationabouttheirsuccessorserviceinstances’ fault injector in the simulator is also called chaosmonkey.
namesandchannels.Bythisway,allinstancescanbuild Weimplementitasacomponentofthesimulator.Duringthe
theirdependencylists. simulation,thefaultinjectorshowninFig.1willreceivefault
• Put: ‘‘Put’’ message simulates the process of inserting injectionrequestsfromusersandextractthefaultinformation
data into the data table of the database. When ‘‘Put’’ from requests including the type of fault, the target service
messages arrive at a ‘‘store’’ service instance, it will and so on. After parsing, the injector will use the ‘‘chaos-
record the key and the value into the map it manages. monkey’’toinjectfaults.
If messages arrive at one ‘‘PriamCassandra’’ service In previous work [38] and [39], researchers collected
instance, the ‘‘Put’’ message will be sent repeatedly to 22 representative microservice faults and listed the detail
otherinstances. description of these faults. For those faults that result in
• GetRequest:‘‘GetRequest’’messagesimulatesasearch the malfunctioning of system services by raising errors or
request to the database in practice. ‘‘GetRequest’’ producingincorrectresults,researchersregardthemasfunc-
from ‘‘denominator’’ service will be forwarded to tionalfaults.Thosefaultsthatinfluencethequalityofservice
the database service. When ‘‘GetRequest’’ message componentssuchasperformanceandreliabilityareregarded
arrives at any instance of ‘‘store’’ service, the instance as non-functional faults. In fact, our simulator only sim-
will search for requested values in its map. If the ulates the communication between service components in
requested value exists, the instance will respond with the simulated architecture without any fine-grain function
a ‘‘GetResponse’’ message. Otherwise, that instance of service components, any detailed malfunctioning of sys-
will have no response. If the message arrives at one temservicescannotbereflectedinoursimulator.Therefore,
43418 VOLUME8,2020

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
TABLE1. Threetypesoffaultsthatcanbeinjected. 4) VISUALIZATION
|     |     |     |     |     |     |     |     | We integrate | Netflix’s     |      | Vizceral | [41]         | into VWR | to       | visualize |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ---- | -------- | ------------ | -------- | -------- | --------- |
|     |     |     |     |     |     |     |     | the defined  | architecture. |      | The      | architecture | files    | uploaded | by        |
|     |     |     |     |     |     |     |     | users will   | be converted  |      | to       | the format   | that     | Vizceral | needs     |
|     |     |     |     |     |     |     |     | and then     | Vizceral      | will | help     | to show      | the      | topology | in the    |
dashboard.Whatismore,VWRusesGrafana[42]toprovide
differentwidgets,e.g.,timeseries,tables,textfieldsforsingle
metrics.
|            |       |                |     |        |        |     |       | IV. MATRIXSKETCHBASEDANOMALYDETECTION |                  |         |           |            |             |     |         |
| ---------- | ----- | -------------- | --- | ------ | ------ | --- | ----- | ------------------------------------- | ---------------- | ------- | --------- | ---------- | ----------- | --- | ------- |
|            |       |                |     |        |        |     |       | Due to                                | the continuously |         | generated | data,      | traditional |     | offline |
| we provide | three | non-functional |     | faults | in VWR | as  | shown |                                       |                  |         |           |            |             |     |         |
|            |       |                |     |        |        |     |       | algorithms                            | that             | attempt | to store  | the entire | stream      | for | analy-  |
inTable1.
|     |     |     |     |     |     |     |     | sis is not | able | to handle | a   | large volume | of  | streaming | data. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --------- | --- | ------------ | --- | --------- | ----- |
Inreality,duetotheoverloadofservers,allrequestssent
|     |     |     |     |     |     |     |     | What is | more, | an important |     | requirement | of  | anomaly | detec- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------------ | --- | ----------- | --- | ------- | ------ |
toaspecificservicemaynotbeansweredintime.Therefore,
|           |                 |     |         |           |      |           |     | tion is to | detect | anomalies |     | in real-time | before | the | system |
| --------- | --------------- | --- | ------- | --------- | ---- | --------- | --- | ---------- | ------ | --------- | --- | ------------ | ------ | --- | ------ |
| our first | fault ‘‘Delay’’ |     | behaves | like long | time | responses | to  |            |        |           |     |              |        |     |        |
isseriouslyimpactedbyanomalies.Therefore,weconstruct
| requests | of one specific |     | service. | Secondly, | due | to improper |     |                 |     |         |           |           |     |       |        |
| -------- | --------------- | --- | -------- | --------- | --- | ----------- | --- | --------------- | --- | ------- | --------- | --------- | --- | ----- | ------ |
|          |                 |     |          |           |     |             |     | an unsupervised |     | anomaly | detection | algorithm |     | based | on the |
orinconsistentconfigurationsofmicroservicesortheirenvi-
methodproposedin[24]andintegrateitinVWRtoprovide
ronments,aserviceinstancewouldcrash.Therefore,another
abaselineforusers.ThealgorithmisbasedonMatrixSketch
| fault ‘‘Delete’’ |     | behaves | as one | specific | service | instance |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------ | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anditcanefficientlyandeffectivelydetectanomaliesinlarge
| fails. Thirdly, | caused |     | by the | low network |     | performance, |     |     |     |     |     |     |     |     |     |
| --------------- | ------ | --- | ------ | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
onlinedatastreams.Whatismore,thisalgorithmconsumes
theconnectionbetween2serviceswouldbelost.Therefore,
|              |     |                |     |       |       |          |     | limited | memory | and | requires | just one | pass | over | the data |
| ------------ | --- | -------------- | --- | ----- | ----- | -------- | --- | ------- | ------ | --- | -------- | -------- | ---- | ---- | -------- |
| we simulated | the | ‘‘Disconnect’’ |     | fault | which | disables | the |         |        |     |          |          |      |      |          |
whichsupportsuserstodetectanomaliesassoonaspossible.
connectionbetween2specificservices.Moreover,sincethere
Inthissection,wewillshowthedetailofthisalgorithmand
| is a large | volume | of service | instances |     | in microservice |     | sys- |     |     |     |     |     |     |     |     |
| ---------- | ------ | ---------- | --------- | --- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
illustratehowtousethisalgorithmtodetectanomaliesonthe
tems,thefaultinjectionswillbeconductedrandomlytoone
tracingdata.
instance.
Firstly,therearetwowaystogetthedurationofarequest.
| Next, | the process | of  | how | these faults | are | injected | into |     |     |     |     |     |     |     |     |
| ----- | ----------- | --- | --- | ------------ | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.5showsthetracingprocessofarequestfromaclientto
| the simulated | architecture |     | will       | be described |          | in detail. | For    |           |         |         |      |          |         |          |       |
| ------------- | ------------ | --- | ---------- | ------------ | -------- | ---------- | ------ | --------- | ------- | ------- | ---- | -------- | ------- | -------- | ----- |
|               |              |     |            |              |          |            |        | a server. | In this | figure, | when | a client | service | instance | sends |
| the ‘‘Delay’’ | fault,       | the | user needs | to           | give the | name       | of the |           |         |         |      |          |         |          |       |
arequesttotheserverserviceinstance(i.e.,cs),wewillget
| target service | A   | and the | delay | time σ | in the | request | which |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ----- | ------ | ------ | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
anewrecordwhichiscalled‘‘span’’[43]inthetracingdata
| will be | sent to VWR. | After | that, | ‘‘chaosmonkey’’ |     | will | send |     |     |     |     |     |     |     |     |
| ------- | ------------ | ----- | ----- | --------------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
withanewendpointwhosevalueis‘‘cs’’andthetimestamp
| the ‘‘Delay’’ | message       | to       | one instance | of      | service    | A. When | it     |                                                      |     |     |     |     |     |     |     |
| ------------- | ------------- | -------- | ------------ | ------- | ---------- | ------- | ------ | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |               |          |              |         |            |         |        | isT .Whentheserverserviceinstancereceivesthisrequest |     |     |     |     |     |     |     |
| receives      | the ‘‘Delay’’ | message, |              | it will | halt until | the     | end of | cs                                                   |     |     |     |     |     |     |     |
(i.e.,sr),therequestisprocessedattheserverend.Afterthat,
theinjectionduration.Forthe‘‘Delete’’fault,theuserneeds
theserverserviceinstancewillsendtheresponsebacktothe
togivethetargetserviceAintherequest.Afterthat,‘‘chaos-
|     |     |     |     |     |     |     |     | client service | instance |     | (i.e., | ss), then | the span | will | get two |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ------ | --------- | -------- | ---- | ------- |
monkey’’willsendthe‘‘Delete’’messagetooneinstanceofA
|                                                     |     |          |     |            |      |        |      | new endpoints |                                                 | whose | value | is ‘‘sr’’  | and ‘‘ss’’ | with     | times- |
| --------------------------------------------------- | --- | -------- | --- | ---------- | ---- | ------ | ---- | ------------- | ----------------------------------------------- | ----- | ----- | ---------- | ---------- | -------- | ------ |
| whichwillsoonstopforwardingotherreceivedmessagesand |     |          |     |            |      |        |      |               | ,T                                              |       |       |            |            |          |        |
|                                                     |     |          |     |            |      |        |      | tampsT        | sr ss respectively.Whentheclientserviceinstance |       |       |            |            |          |        |
| send ‘‘GetResponse’’                                |     | messages |     | with Error | code | (e.g., | 404) |               |                                                 |       |       |            |            |          |        |
|                                                     |     |          |     |            |      |        |      | receives      | the response                                    |       | from  | the server | service    | instance | (i.e., |
backtothoseserviceinstancesthatdependonitwhichwill
|     |     |     |     |     |     |     |     | cr), the | span will | get | another | endpoint | whose | value | is ‘‘cr’’ |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------- | -------- | ----- | ----- | --------- |
removethedeletedinstancefromthedependencylist.Forthe
|                                                        |     |     |     |     |     |     |     | withtimestampT |     | .   |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| ‘‘Disconnect’’fault,usersneedtogivetwotargetservicesA, |     |     |     |     |     |     |     |                |     | cr  |     |     |     |     |     |
B,andaprobabilityλ.Then,‘‘chaosmonkey’’willsendthe
‘‘Delete’’messagetoλinstancesofAandremoveBfromA’s
dependencylist.
|     |     |     |     |     |     |     |     | FIGURE5. | Thetracingprocessbetweenaclientandaserver. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
3) EVALUATOR
Therearetwotaskstheevaluatorneedstofinish.Firstofall, Duration2intheequation2meanstheprocessingtimeof
whenuserssendrequeststoactivatetheevaluator,theevalu- thereceivedrequest.Duration1intheequation1meansthe
atorwillaccesstoElasticSearch[40],andfetchtheproduced duration of the whole request including Duration2 and the
tracingdata.Afterthat,theevaluatorwillconvertthetracing propagation time of the request and the response between
data into the format that the anomaly detection algorithm the client and the server. Therefore, we can use Duration1
needs and then detect anomalies. Besides, users can upload orDuration2ofeveryrequestbetweentwoserviceinstances
the anomaly detection or root cause analysis algorithms asaperformanceindicator.Ifoneofthesetwoindicatorsofa
before evaluation. After the evaluation, users can download requestismuchlargerthanotherrequests,wecanregardthis
theresultsofthesealgorithmsfromVWR. requestasanabnormalrequest.Inourexperiment,wechoose
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 43419 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
Duration1asourevaluationindicatorbecauseitcoversdiffer- Algorithm1AnomalyDetectionAlgorithm
enttransmissionphaseswhichshowstheperformancestatus Input:
ofarequestmoreholistic. newdatapointsY ∈Rm×n;
t
Duration1 = T cr −T cs (1) p
r-
r
r
i
a
o
n
r
k
fa
m
u
a
lt
tr
p
i
r
x
o
w
ba
it
b
h
il
o
it
r
y
th
(cid:15)
o
;
gonalcolumnsU (t−1)r ;
Duration2 = T −T (2) Output:
ss sr
updatedsetofnon-anomalousdatapointsN ;
[t]n
Secondly,whenwegetthetracingdatafromVWR,thedata updatedr-rankorthogonalmatrixU tr ;
will be converted into a matrix in the following manner. 1 N ta ,N tn ←[],[];
Regard every service instance as a bucket and the sent 2 //N ta ,N tn denoteabnormalandnormaldatapoints
requestsasobjectsinthebucket.Then,wecountthenumber respectively
N of arriving requests at time t in every bucket and get the 3 foreachcolumny i ∈Y t do
duration of every request by subtracting the timestamp in 4 Calculateanomalyscore:
(cid:13) (cid:13)
t
e
h
n
e
dp
e
o
n
i
d
n
p
t
o
w
in
h
t
o
w
se
ho
v
s
a
e
lu
v
e
al
i
u
s
e
‘
i
‘
s
cr
‘
’
‘
’
c
.
s
F
’’
o
a
r
n
e
d
ve
th
ry
e t
s
i
e
m
rv
e
i
s
c
ta
e
m
in
p
st
i
a
n
n
t
c
h
e
e
,
5 score=(cid:13) (cid:13) (I m −U (t−1)r U ( T t−1)r )y i (cid:13) (cid:13)
2
6 ifscore≤(cid:15) then
it will sum up the duration of all requests at time t and
dividethedurationsumbyN.Thus,wecangettheaverage 7 N tn ←[N tn ,y i ]
8 else
requestcompletiontimeattimet foreveryserviceinstance.
The produced tracing data arrives in streaming and every 9 N ta ←[N ta ,y i ]
10 end
serviceinstancewillsendrequestsatanytime.Bydoingthis,
11 end
we can form a high-dimension matrix as an input data for
theMatrixSketchalgorithm,thenumberofrowsrepresents 12 N [t]n ←[N [t−1]n ,N tn ]
13 Updatesingularvectors:
the number of service instances, the number of columns
represents the number of all coming datapoints at time t 14 U tr ←Update(U (t−1)r )
andtheelementofthematrixdenotestheinstance’saverage 15 returnN [t]n ,U tr
request completion time at time t. Let {Y ∈ Rm×n,t =
t
1,2,3,...} denote a sequence of streaming tracing data,
Aftergettingtheanomalousscoreforeverycomingpoint
and Y means all datapoints arrive at time t. The goal of
t
in Y , we use the threshold (cid:15) to decide which points are
the Matrix Sketch algorithm is to detect ‘‘anomalous data- t
p [N oi 1 n n t , s N ’’ 2n i , n N Y 3 t n , a . t .. e , v N er t y −1 t n im ]r e ep t r . es W en e ts a t s h s e um se e to th f a a t ll N da [t t − a 1 p ] o n in = ts s e a p x n o t o r n m a d c a i t l n o a g u s s d e . a t I t f a o t f p h o n e i o n s n c t - o a i r s n e o a i m b s n a g o l r o r e m u a s t a e l p r . o I t i h n n a t t n s hi N (cid:15) s , s w t i e e n p s , Y a w y . e t W h c e i a t n h co a N r l r s e o - ,
that had been identified as non-anomalous by the algorithm tn t tn
inY [t−1] = [Y 1 ,Y 2 ,Y 3 ,...,Y t−1 ].Attimet,N tn denotesall w
m
e
at
s
r
t
i
a
x
r
U
tto
.
updatethematrixU (t−1)r andgetthenextsketch
l n o o w n e -a r n r o a m nk al m ou a s tri d x at w ap it o h in o t r s th i o n g Y o t n a a n l d co U lu (t m − n 1) s r t i h s a a t s c s a u n m l e in d e a a s rly a There t a r rethreewaystoupdatethematrixU (t−1)r in[24].
reconstruct N in Y . At time t = 1, we can firstly gather a The first algorithm is based on global algorithm, which
tn t
generates the matrix from the globally collected sample set
small set of non-anomalous data and initialize N from it,
because it is easier for us to collect a set of non-a 1 n n omalous N [t]n = [N [t−1]n ,N tn ]. As we can see, both the compu-
tational and memory requirement of this global algorithm
data. Or we can also collect a small set of data and use any
will increase with time. According to [24], the random
unsupervised anomaly detection algorithm to label the data
sketch update algorithm almost gets the same result as the
whichwecanusetoconstructN .
1n
global algorithm more efficiently. Therefore, we use the
Afterillustratingthedetailofhowtogettheinputmatrix
random sketch update algorithm to update the matrix U .
and the goal of our algorithm, we will talk about the t
The procedure of the random sketch update is listed as
framework of the algorithm. The framework of the stream-
algorithm2.
ing anomaly detection using Matrix Sketch is listed in
Ineachiteration,matrixM willbecomputedbycombin-
Algorithm1. This algorithm alternates between an anomaly t
detectionandasingularvectorupdatingstep. ing current sketch matrix E t−1 with N tn . E 0 will be initial-
ized as an empty matrix. Then, Y will be generated using
The rank r matrix which can represent all datapoints in
M and a random Gaussian distributed matrix, and then Y
N [t−1]n isU (t−1)r ,andwecanusethismatrixtodetectanoma-
wi
t
ll be conducted a QR factorization [44] to get matrix Q
lousdatapointsinY bycalculatingthescoreforeverypoint
y i ∈Y t throughthec
t
alculation3.Notethatinthiscalculation, and R. Next, we get the eigen value
(cid:80)2
t and eigen vec-
tor A by conducting the eigen function with Q and M .
I isIdentitymatrixwhichsizeismandafterthesubtraction, t t
m
After that, we multiply Q by A to get U , from which we
wegettheL -normoftheresult. t t
2
choose top-r vectors to form matrix U and choose top-
tr
score= (cid:13) (cid:13) (cid:13) (I m −U (t−1)r U ( T t−1)r )y i (cid:13) (cid:13) (cid:13) 2 (3) o (cid:96) f t v o e u ct p o d r a s t . e matrix E t where r and (cid:96) represent the number
43420 VOLUME8,2020

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
FIGURE6. Fig.(a)-Fig.(c)istheexampleviewofserviceslatencyandFig.(d)showsthetimeweinjectedDelayfaults.TogetFig.(a)-Fig.(c),inevery
200ms,wecollectalltraces,sumuptherequestcompletiontimeofalltracesanddivideitbythecountoftraces.
Algorithm2RandomUpdateAlgorithm architectures to VWR, we make some simplification and
Input: describe the architectures in arch files using the format
|     | ∈Rm×n; |     |     |     |     |     |     | VWRrequires.ForAWS,‘‘rdsMysql’’serviceand‘‘content- |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
N t
|     |                                  |     |     |     |     |     |     | S3’’ service | are Database |     | services | which are configured |     | as  |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | -------- | -------------------- | --- | --- |
|     | randomizedmatrixsketchupdatedatt |     |     |     |     | −1, |     |              |              |     |          |                      |     |     |
E ∈Rm×l; ‘‘store’’ package in the arch file, ‘‘app server-elb’’ service
t−1
≤(cid:96); and ‘‘web server-elb’’ service are Load Balance services
r
Output: which are configured as ‘‘elb’’ package in the arch file,
|     |                                   |     |     |     |     | ∈Rm×l; |     | ‘‘cloudfront’’service,‘‘webserver’’serviceand‘‘appserver’’ |              |     |               |              |          |     |
| --- | --------------------------------- | --- | --- | --- | --- | ------ | --- | ---------------------------------------------------------- | ------------ | --- | ------------- | ------------ | -------- | --- |
|     | randomizedmatrixsketchupdateatt,E |     |     |     |     | t      |     |                                                            |              |     |               |              |          |     |
|     |                                   |     |     |     |     |        |     | service are                                                | the services |     | that simulate | a monolithic | business |     |
U ;
tr
M ←[E ,N ] logic. They are all configured as ‘‘monolithic’’ package.
| 1   | t   | t−1 | t   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
←100(cid:96) Another architecture Netflix is applied to provide stream-
2 k
Generateanm×krandomGaussianmatrix(cid:127) ing media service. Therefore, ‘‘cassSubscriber’’ service and
3
←M T(cid:127) ‘‘evcacheSubscriber’’ service are Database services which
| 4 Y | t   | M t |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
areconfiguredasstorepackage,‘‘subscriber’’servicewhich
| 5 QR←Q |     | (Y)(QRfactorizationforY) |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R
(cid:80)2 AT ←E (QTM TQ)(where is configured as ‘‘staash’’ package mainly accesses the data
| 6 A | t   |     | IG  | t M |     |     |     |                                                    |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | t t |     |     | t   |     |     |     | fromalldownstreamDatabaseservicesandforwardsdatato |     |     |     |     |     |     |
(cid:80)2 =diag(σ2,...,σ2))
|     | t   | t1  |     | tk  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
←QA (QQTM TQQt T) theupstreamservice,‘‘login’’serviceand‘‘homepage’’ser-
| 7 U | t   | t                      | t M | approximatesM |            | t M  |     |                                                       |     |     |     |     |     |     |
| --- | --- | ---------------------- | --- | ------------- | ---------- | ---- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |                        |     | t             |            |      | t   | viceareconfiguredas‘‘monolithic’’package,‘‘wwwproxy’’ |     |     |     |     |     |     |
| U   | ←[u | ,...,u(cid:96)](whereU |     |               | =[u ,...,u | ]and |     |                                                       |     |     |     |     |     |     |
8 t(cid:96) 1 tk 1 k service simulates an API proxy service which is configured
(cid:96)≤k)
(cid:80)( trunc) (cid:113) σ −σ ,...,(cid:113)σ −σ ,0) a s ‘‘ z u u l’ ’ p ac k a g e , ‘ ‘ w w w - el b ’ ’ se rv ic e i s c o n fi g u r e d a s
| 9   |     | ←diag( |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t(cid:96) t 2 t(cid:96) 2 t(cid:96) 2 −1 t(cid:96) 2 ‘‘ elb ’ ’ p a c k ag e . T h e l a st a rc h i te c tu re s im u l at e s t h e s i m p le
1
| E   | ←U  | (cid:80)( trunc) |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10 t t(cid:96) t(cid:96) LAMP stack. Therefore, ‘‘rdsMysql’’ service and ‘‘mem-
11 U ←[u ,...u ](whereU =[u ,...u(cid:96)]) cache’’serviceareDatabaseserviceswhichareconfiguredas
|     | tr  | 1   | r   | tl  | 1   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
returnE andU ‘‘store’’package,‘‘webserver’’servicesimulatestheApache
| 12  | t   |     | tr  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
serverwhichisconfiguredas‘‘monolithic’’packageandthe
|     |     |     |     |     |     |     |     | ‘‘webserver-elb’’ |     | service | is configured | as ‘‘elb’’ | package. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ------------- | ---------- | -------- | --- |
V. EXPERIMENTEVALUATION
|           |                 |     |       |          |                   |               |        | LAMP                | stack’s Linux | component |            | and PHP component    |           | can   |
| --------- | --------------- | --- | ----- | -------- | ----------------- | ------------- | ------ | ------------------- | ------------- | --------- | ---------- | -------------------- | --------- | ----- |
| In        | this section,   | we  | now   | validate | the effectiveness |               | of VWR |                     |               |           |            |                      |           |       |
|           |                 |     |       |          |                   |               |        | not be demonstrated |               | on        | VWR, since | VWR only             | simulates |       |
| and       | the performance |     | of    | Matrix   | Sketch by         | simulating    | three  |                     |               |           |            |                      |           |       |
|           |                 |     |       |          |                   |               |        | the behavior        | of each       | service   | and        | ignores the detailed |           | logic |
| classical | architectures   |     | shown | in       | Fig.4. The        | configuration | of     |                     |               |           |            |                      |           |       |
each corresponding architecture is shown in Fig.2. We vali- ofservices.Forthreearchitectures,the‘‘www’’servicecon-
figuredasa‘‘denominator’’packagedrivesthearchitectures
dateVWRwithrespecttotwoaspects.
viacontinuoussimulatedrequests.
|     | We validate | that | against | the | actual microservice |     | struc- |     |     |     |     |     |     |     |
| --- | ----------- | ---- | ------- | --- | ------------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
•
|     | tures, | VWR | is able | to gain | great improvement. |     | Firstly, |     |     |     |     |     |     |     |
| --- | ------ | --- | ------- | ------- | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
VWRcanrapidlygeneratelargevolumeoftracingdata. A. VALIDATINGTHEIMPROVEMENTOFVWR
Secondly,VWRhastheabilitytosimulatemultipleself- TodemonstratetheimprovementofVWR,weconductexper-
definedarchitectures.Finally,thecostandtheoverhead imentsusingAWSarchitectureonourserver.Table2shows
ofVWRislowerthanrealsystems. the specs of our experimental platform. There are three
• We validate VWR can simulate the latency curves of aspectsshownasfollowed.
realapplications.EnsuringthatVWRcanreproducethe
• SimulationDiversity.Aswehaveshownbefore,VWR
latencyincreasingpatternisessentialinitseffectiveness. achievesmostofkeyservices’actionwhichensuresthat
Before our experiment, we obtain three architectures AWS, users can convert many real microservice systems into
Netflix and LAMP from [45]–[47]. In order to apply these theirdigitalversionsthatcanrunonVWR.
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     |     |     |     | 43421 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
TABLE2. Platformspecification. injected anomalies. Table 3 records one request’s response
time of denominator service, cloudfront service and web-
server elb service in normal condition or in fault condition
whenonewebserverserviceisdelayed.Fromthetrendthat
reflectsonTable3,wefindthatthedelayofup-streamingser-
vice(i,e,webserver)willaffectthelatencyofdown-streaming
services(i,e, denominator, cloudfront and webserver elb).
Furthermore, from the following aspects, we find that the
TABLE3. Therequestcompletiontimeofthreeservicesindifferent
condition. faultdatacreatedfromthesimulationareconsistentwiththe
datafromrealmicroservicesystems.
• Firstofall,wenoticethat,inthemicroservicearchitec-
ture,theeffectofdelayfaultwillbeaccumulatedalong
theservicecallchain.Forexample,ifoneinstanceofthe
app-server elb is injected with a delay fault, the effect
will be propagated to the instance of the denominator
TABLE4. Thedelayfaultinjectionrule.
service.IntheAWSarchitecture,thesethreeserviceslie
in the same service call chain, so we can find that the
curvesofthesethreeservicesarequitesimilar.
• Secondly,ifoneup-streamingservicedependsononly
one down-streaming service which failed, the fault
effectofthefaileddown-streamingservicewillbefully
reflected on the up-streaming service. In our simu-
lated AWS architecture, the denominator service only
depends on the cloudfront service. Therefore, we can
findthattheirperformancecurvesarethesame.
• Fast Traces Generation. In order to obtain enough
• Thirdly, in real microservice systems, if one service
data to conduct intelligent analysis, the speed of trace
instance is delayed because of its low performance,
datagenerationisanotherkeyaspectthatrequiresusto
therequestissuedtothisinstancewillnotbeprocessed
notice.RunningAWSinVWRgenerates124961traces
intime.Therefore,iftheup-streamingservicedepends
in a 300s simulation and generates 251289 traces in a
on a down-streaming delayed service, the delay effect
600ssimulation.Moreover,thegenerationspeedcanbe
willbereflectedintheup-streamingservice.Forexam-
tunedaccordingtousers’requirement.
ple,atPoint1showninFig.6,thedelayfaultisinjected
• Low Simulation Overhead. Due to the architec-
intowebserverelbservicewhilethedelayfaulteffectis
ture simulation, traces generation, and the amount of
reflectedinthecloudfrontservice.Moreover,
resources needed to store trace data, VWR also brings
• Fourthly, in the real microservice system, if the
additional overhead. After testing the performance of
up-streaming service depends on two down-streaming
VWR during simulation, we find the overhead is low.
services, the delay fault effect reflected on the
During a 100s simulation, VWR costs only 3% CPU
up-streamingservicemaycomefromoneofthedown-
utilization. What is more, the memory usage of VWR
streaming services. For example, cloudfront service
increases as the simulation goes and after 100s, VWR
depends on webserver elb service and content-S3 ser-
uses about 20MB. As VWR is simulating, traces are
vice.Therefore,atPoint2showninFig.6,thefaulteffect
cachedinmemorythatwillbepreservedinthediskonce
reflectedoncloudfrontservicecomesfromthecontent-
thesimulationisdone.
S3service.
Because of these observations, the produced tracing data
B. SIMULATEDFAULTSVALIDATION can be used in the Matrix Sketch algorithm and we will
We conducted experiments to evaluate the effectiveness of introduce the result of the algorithm in detail in the next
faultinjection,byinjectingfaultsintoamicroservicesystem section.
spawnedbytheAWSarchitectureshowninFig.4a.
2) DELETEFAULT
1) DELAYFAULT Moreover,weinjectedaDeletefaulttodeletetheappserver
According to injection rules listed in Table 4, we injected servicewhichhasonlyoneinstanceandaggregatedalltraces
7 delay faults into different services shown in Fig.4a, then in the simulation. Because there is only one instance of
usedcollectedtracestocreatedatagraphsinFig.6andcreate the deleted service along the service call chain, incomplete
Table3.Fig.6a-Fig.6crepresentaveragerequestscompletion tracesandabnormaltraceswitherrorcodemaybeproduced.
time of denominator service, cloudfront service, and web- However,whenthedeletedappserverservicehasmorethan
server elb service respectively. Fig.6d shows timestamps of oneinstance,wecanonlygetincompletetracesbecausethe
43422 VOLUME8,2020

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
FIGURE7. ROCcurvesformatrixsketch,iForest,SVM-RBFondatasetsthathavedifferentanomalyrates.
FIGURE8. ROCcurvesforMatrixSketch,iForest,SVM-RBFondatasetsthatareproducedbysimulatingthreedifferentarchitectureswithuniform
anomalyrate.
subsequent requests from the predecessor instances can be TABLE5. Descriptionofthedatasets.
senttootherinstancesofthedeletedservice.
C. MATRIXSKETCHPERFORMANCEEXPERIMENTS
Intheprevioussection,weillustratedtheeffectivenessofthe
simulated faults. In this section, we will use the produced
tracingdatatoevaluatetheperformanceofMatrixSketch.
1) EXPERIMENTPREPARATION
a: DATASETS and the anomaly rate is 3.94%. The AWS-900-10 dataset is
WesimulatedthreeclassicalarchitecturesshowninFig.4and obtainedfroma900secondssimulationontheAWSarchitec-
periodicallyinjecteddelayfaultstodifferentservices.From ture.Weinjecteddelayfaultsper10secondsapproximately
Fig.4 and Table 5, the AWS architecture has 8 services and the anomaly rate is 1.97%. The AWS-600-0.5 dataset
and 26 instances; the Netflix architecture has 8 services comes from a 600 seconds simulation on the AWS archi-
and 65 instances; the Lamp architecture has 5 services and tecture and was injected delay faults per 0.5 seconds. The
23 instances. The feature in Table 5 means the number anomalyrateis9.14%.TheNETFLIX-1800-10datasetand
of instances of each architecture. After simulation, we get the LAMP-1800-10 dataset are produced by 1800 seconds
the tracing data and convert them into different datasets simulation on Netflix architecture(Fig.4b), Lamp architec-
showninTable5.Weconductedexperimentsondatasetsto ture(Fig.4c).Theywereinjecteddelayfaultsper10seconds
detect the performance of Matrix Sketch. The AWS-1800- andtheiranomalyratesare2%,1.52%.
30 dataset is produced in 1800 seconds simulation on the
AWSarchitectureshowninFig.4a.Weinjecteddelayfaults b: BASELINES
per 30 seconds approximately and the anomaly rate of this Therearenumberofapproachesforanomalydetectionwhich
datasetis0.56%.TheAWS-1800-10datasetisalsoproduced isdiscussedinSectionII.Wecomparedagainsttwopopular
in 1800 seconds simulation on the AWS architecture. How- and easily implemented algorithms for anomaly detection.
ever,weinjecteddelayfaultsper10secondsapproximately These algorithms were chosen considering their scalability
and the anomaly rate is 2.48%. The AWS-1800-5 dataset is on large datasets. SVM-RBF is a one-class support vector
obtained in 1800 seconds simulation on the AWS architec- machineclassifierusingaradialbasisasthekernel.Isolation
ture. We injected delay faults per 5 seconds approximately Forestisusedasanotherbaselinebecauseofitscapabilityin
VOLUME8,2020 43423

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
|     |     |     |     | result. The      | training       | set                                    | was          | randomly   | selected          |               | from non-  |
| --- | --- | --- | --- | ---------------- | -------------- | -------------------------------------- | ------------ | ---------- | ----------------- | ------------- | ---------- |
|     |     |     |     | anomalous        | samples        | and                                    | the          | order of   | samples           | was           | also ran-  |
|     |     |     |     | domly shuffled   |                | each                                   | time.        | In our     | experiments,      |               | we regard  |
|     |     |     |     | the anomaly      | as             | the positives                          |              | while      | the non-anomalous |               | data       |
|     |     |     |     | as the negatives |                | because                                | the          | main       | goal              | of our        | task is to |
|     |     |     |     | detect anomalies |                | that                                   | have         | lower      | probabilities.    |               | Therefore, |
|     |     |     |     | TPofourROC       |                | curverepresentsthoseanomalydatathatare |              |            |                   |               |            |
|     |     |     |     | classified       | correctly,     | while                                  | FP           | represents | the               | non-anomalous |            |
|     |     |     |     | data that        | are classified |                                        | incorrectly. |            | We make           | the           | following  |
observations:
|     |     |     |     | • From | Figures | 7a, | 7b, and | 8a, | it is evident |     | that Matrix |
| --- | --- | --- | --- | ------ | ------- | --- | ------- | --- | ------------- | --- | ----------- |
Sketchgetsabetterperformancethanotheralgorithms.
|     |     |     |     | However, |     | as shown | in Figure | 7a  | and | 7d, the | other two |
| --- | --- | --- | --- | -------- | --- | -------- | --------- | --- | --- | ------- | --------- |
comparedalgorithmsperformslightlybetterthanMatrix
|     |     |     |     | Sketch. | Note | that | the performance |              | of  | Matrix       | Sketch is |
| --- | --- | --- | --- | ------- | ---- | ---- | --------------- | ------------ | --- | ------------ | --------- |
|     |     |     |     | better  | when | the  | fraction        | of anomalies |     | approximates | to        |
therealanomalyrateinreal-worldsystems.
FromFig.8b,wecanfindthatMatrixSketchusingfewer
•
featuresoutperformsMatrixSketchusingmorefeatures
(i.e.,serviceinstances).Whenfewerinstancesareused,
|     |     |     |     | the           | impact        | that some | inconspicuous |               | services |               | do on the |
| --- | --- | --- | --- | ------------- | ------------- | --------- | ------------- | ------------- | -------- | ------------- | --------- |
|     |     |     |     | algorithm     |               | will be   | reduced       | and           | the      | algorithm     | can be    |
|     |     |     |     | easier        | to understand |           | the           | impact        | that     | the anomalies | do        |
|     |     |     |     | to bottleneck |               | services. |               | Due to        | the same | reason,       | from      |
|     |     |     |     | Figures       | 8a,           | 8b, and   | 8c,           | it is evident |          | that our      | approach  |
outperformsotheralgorithmsonAWSandLamparchi-
|     |     |     |     | tecture    | which | has    | relative | small   | number       |     | of service |
| --- | --- | --- | --- | ---------- | ----- | ------ | -------- | ------- | ------------ | --- | ---------- |
|     |     |     |     | instances, |       | except | on the   | Netflix | architecture |     | which has  |
FIGURE9. Theeffectofparametersonmatrixsketch. moreinstances.Therefore,ouralgorithmissensitiveto
thearchitecture.Ittendstoworkwellwhenthenumber
thehigh-dimensionalanalysis.Forthesealgorithms,wetuned ofserviceinstancesissmaller.However,ifuserswantto
improvetheperformanceofthealgorithm,usingfewer
| their parameters | to get the highest | Recall without | loosing a |     |     |     |     |     |     |     |     |
| ---------------- | ------------------ | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
featureswillhelpitworkbetter.
highF1score.
| c: PARAMETERSETTINGS |     |     |     | 3) PARAMETERIMPACTANALYSIS |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thereareprimarilytwoparametersthatwecantunetofinda
AsillustratedinSectionIV,MatrixSketchalgorithmrequires
an initial training set to construct N . In our experiment, better performance of Matrix Sketch based anomaly detec-
1
weassumethatthereisasmalltrainingsetofnon-anomalous tion. We will discuss the impact of these two parameters,
((cid:15))
tracingdatasamplesatthebeginning.Therefore,wesetthe namely the value of the prior fault probability and the
size of the initial training set as 3000. Moreover, we select batch size n of every step. (cid:15) ranges from 0.01 to 0.04 with
t
|                  |               |                          |     | increments          | of 0.002 | while | n                                | ranges | from | 500 to | 3000 with |
| ---------------- | ------------- | ------------------------ | --- | ------------------- | -------- | ----- | -------------------------------- | ------ | ---- | ------ | --------- |
| training samples | randomly from | the set of non-anomalous |     |                     |          |       |                                  | t      |      |        |           |
| traces.          |               |                          |     | incrementsof100.ROC |          |       | curvesaresimilarbetweendifferent |        |      |        |           |
We tuned other necessary parameters to achieve bet- values of parameters. Therefore, we calculate the precision,
ter performance of our Matrix Sketch when we compared recall and F1 scores at different settings and draw Fig.9a,
the performance between algorithms. Besides, we also dis- Fig.9b.Then,wegetthefollowingobservations:
cuss the effect of these parameters using AWS-1800-10 at • FromFig.9a,wecanfindthatifweincreasethevalueof
SectionV-C.3,including the batchsize and the prior fault thepriorfaultprobability(cid:15),therecallofitwillincrease
probabilitygivenforthedetection.
|     |     |     |     | whichiseasiertounderstand:whenn |      |      |         |            | t   | datapointscome, |                |
| --- | --- | --- | --- | ------------------------------- | ---- | ---- | ------- | ---------- | --- | --------------- | -------------- |
|     |     |     |     | (cid:15) ×                      | n of | them | will be | identified | as  | anomaly,        | so if (cid:15) |
t
2) COMPARISONSBETWEENDIFFERENTALGORITHMS is higher, Matrix Sketch will identify more data points
Fig.7andFig.8showtheROC curvesofselectedalgorithms. asanomalies.TheprecisionandF1-scorewillincrease
To increase the effectiveness of the comparison between along with the increment of (cid:15) until (cid:15) is slightly larger
thesethreealgorithms,weconductedexperimentswithcross- thantherealfaultprobabilitywhichdemonstratesthatif
validation. Each point represents the average True Posi- weuseMatrixSketchtodetectanomalies,weshouldset
(cid:15)
tive(TP)andFaultpositive(FP)ofa20-foldcross-validation slightlylargerthantherealvalue.
| 43424 |     |     |     |     |     |     |     |     |     |     | VOLUME8,2020 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
• From Fig.9b, it is evident that the trends of precision, [8] C.Sauvanaud,M.Kaaniche,K.Kanoun,K.Lazri,andG.DaS.Silvestre,
recall,andF1scorearesimilarwhichdemonstratesthat ‘‘Anomaly detection and diagnosis for cloud services: Practical exper-
|            |     |       |      |             |             |     |         | iments | and lessons | learned,’’ |     | J. Syst. | Softw., vol. | 139, | pp.84–106, |
| ---------- | --- | ----- | ---- | ----------- | ----------- | --- | ------- | ------ | ----------- | ---------- | --- | -------- | ------------ | ---- | ---------- |
| the effect | of  | batch | size | n t on them | is similar. |     | What is |        |             |            |     |          |              |      |            |
May2018.
| more, | we can | find | that the | value | of precision | increases |     |                                                                |     |     |     |     |     |     |     |
| ----- | ------ | ---- | -------- | ----- | ------------ | --------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|       |        |      |          |       |              |           |     | [9] M.Y.Chen,A.Accardi,E.Kiciman,J.Lloyd,D.Patterson,A.Fox,and |     |     |     |     |     |     |     |
E.Brewer,‘‘Path-basedfaliureandevolutionmanagement,’’inProc.1st
slightlyalongwiththebatchsizeuntilthebatchsizeis
Conf.Symp.Netw.Syst.DesignImplement.(NSDI),vol.1.SanFrancisco,
2500.Whenthebatchsizeislargerthan2500,thevalue
CA,USA:USENIXAssociation,2004,pp.1–23.
| of precision |     | stops | increasing. | These | results | indicate | a   |                                                                     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ----------- | ----- | ------- | -------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|              |     |       |             |       |         |          |     | [10] J.Lin,P.Chen,andZ.Zheng,‘‘Microscope:Pinpointperformanceissues |     |     |     |     |     |     |     |
very stable behavior of Matrix Sketch across different withcausalgraphsinmicro-serviceenvironments,’’inProc.16thInt.Conf.
batchsizes. (ICSOC),Hangzhou,China.Berlin,Germany:Springer,2018,pp.3–20.
|     |     |     |     |     |     |     |     | [11] P. Wang,  | J.Xu, | M.Ma, | W.Lin,               | D.Pan, | Y.Wang,   | and    | P.Chen,    |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ----- | -------------------- | ------ | --------- | ------ | ---------- |
|     |     |     |     |     |     |     |     | ‘‘CloudRanger: |       | Root  | cause identification |        | for cloud | native | systems,’’ |
VI. CONCLUSIONANDFUTUREWORK in Proc. 18th IEEE/ACM Int. Symp. Cluster, Cloud Grid Comput.
This paper designs and implements VWR, a framework (CCGRID),May2018,pp.492–502.
|     |     |     |     |     |     |     |     | [12] WeaveworksContainerSolutions.(2018).SocksShop—AMicroservices |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
withmicroservicearchitecturesimulation,faultinjection,and
|     |     |     |     |     |     |     |     | Demo | Application. | Accessed: |     | Dec. 3, | 2019. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --------- | --- | ------- | ----- | --------- | ---------- |
visualization, which aims to help researchers to test and https://www.weave.works/blog/sock-shop-microservices-demo-
application
| compare  | their intelligent |              | operation | algorithms |      | in   | multiple |                 |               |              |         |           |        |          |           |
| -------- | ----------------- | ------------ | --------- | ---------- | ---- | ---- | -------- | --------------- | ------------- | ------------ | ------- | --------- | ------ | -------- | --------- |
|          |                   |              |           |            |      |      |          | [13] C. Bennett | and           | A. Tseitlin. | (2012). | Chaos     | Monkey | Released | Into      |
| kinds of | large-scale       | microservice |           | systems.   | With | VWR, | it is    |                 |               |              |         |           |        |          |           |
|          |                   |              |           |            |      |      |          | the             | Wild. Netflix | Tech         | Blog.   | Accessed: | Dec.   | 3, 2019. | [Online]. |
convenienttovalidatetheiralgorithmsforanomalydetection
|     |     |     |     |     |     |     |     | Available: | https://netflixtechblog.com/netflix-chaos-monkey-upgraded- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
1d679429be5d
androotcauseanalysis.Wesimulatethreeclassicalarchitec-
|           |         |          |         |      |            |     |           | [14] M.A.Chang,B.Tschaen,T.Benson,andL.Vanbever,‘‘Chaosmonkey: |     |             |         |            |         |                |     |
| --------- | ------- | -------- | ------- | ---- | ---------- | --- | --------- | -------------------------------------------------------------- | --- | ----------- | ------- | ---------- | ------- | -------------- | --- |
| tures and | use the | produced | tracing | data | to conduct |     | different |                                                                |     |             |         |            |         |                |     |
|           |         |          |         |      |            |     |           | Increasing                                                     | SDN | reliability | through | systematic | network | destruction,’’ | in  |
experimentsinordertovalidatetheeffectivenessofproduced Proc. ACM Conf. SpecialInterest Group Data Commun. (SIGCOMM),
tracing data. We introduce an anomaly detection algorithm 2015,pp.371–372.
basedonMatrixSketchwhichisanunsupervisedalgorithm [15] Istio.Accessed:Oct.21,2019.[Online].Available:https://istio.io/
|     |     |     |     |     |     |     |     | [16] D.Meisner,J.Wu,andT.F.Wenisch,‘‘BigHouse:Asimulationinfrastruc- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
and performs well on the high-dimension streaming data. turefordatacentersystems,’’inProc.IEEEInt.Symp.Perform.Anal.Syst.
Wecomparethisalgorithmwithtwopopularanomalydetec- Softw.,Apr.2012,pp.35–45.
|                 |     |        |         |     |           |     |         | [17] Y. Zhang, | Y.Gan, | and | C.Delimitrou, | ‘‘µqSim: | Enabling | accurate | and |
| --------------- | --- | ------ | ------- | --- | --------- | --- | ------- | -------------- | ------ | --- | ------------- | -------- | -------- | -------- | --- |
| tion algorithms |     | namely | IForest | and | 1SVM-RBF. |     | We find |                |        |     |               |          |          |          |     |
scalablesimulationforinteractivemicroservices,’’inProc.IEEEInt.Symp.
| that Matrix | Sketch | based | anomaly | detection |     | algorithm | per- |     |     |     |     |     |     |     |     |
| ----------- | ------ | ----- | ------- | --------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Perform.Anal.Syst.Softw.(ISPASS),Mar.2019,pp.212–222.
formswellwhentheanomalyrateisapproximatetothereal
|                |         |            |          |                  |     |     |           | [18] P. Barham, | A.Donnelly, |                 | R.Isaacs, | and R.Mortier, |          | ‘‘Using   | magpie for  |
| -------------- | ------- | ---------- | -------- | ---------------- | --- | --- | --------- | --------------- | ----------- | --------------- | --------- | -------------- | -------- | --------- | ----------- |
|                |         |            |          |                  |     |     |           | request         | extraction  | and             | workload  | modelling,’’   | in Proc. | 6th       | Conf. Symp. |
| anomaly        | rate in | real-world | systems. | Moreover,        |     | we  | find that |                 |             |                 |           |                |          |           |             |
|                |         |            |          |                  |     |     |           | Operating       | Syst.       | Des. Implement. |           | (OSDI),        | vol. 6.  | Berkeley, | CA, USA:    |
| this algorithm | is      | sensitive  | to       | the architecture |     | and | we can    |                 |             |                 |           |                |          |           |             |
USENIXAssociation,2004,p.18.
improveitsperformancebyusingfewerfeatures.Inthefuture
|     |     |     |     |     |     |     |     | [19] M.Y.Chen,E.Kiciman,E.Fratkin,A.Fox,andE.Brewer,‘‘Pinpoint: |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
work,wewillcontinuetouseVWRtoconductexperiments Problemdeterminationinlarge,dynamicInternetservices,’’inProc.Int.
Conf.Depend.Syst.Netw.(DSN),Jun.2002,pp.595–604.
forotheranomalydetectionalgorithmsandrootcauseanaly-
|     |     |     |     |     |     |     |     | [20] M.Chow,D.Meisner,J.Flinn,D.Peek,andT.F.Wenisch,‘‘Themys- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
sisalgorithms. tery machine: End-to-end performance analysis of large-scale Internet
services,’’inProc.11thUSENIXConf.OperatingSyst.Des.Implement.
(OSDI).Berkeley,CA,USA:USENIXAssociation,2014,pp.217–231.
ACKNOWLEDGMENT
|     |     |     |     |     |     |     |     | [21] F.DorayandM.Dagenais,‘‘Diagnosingperformancevariationsbycom- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
The authors would like to thank anonymous reviewers and paringmulti-levelexecutiontraces,’’IEEETrans.ParallelDistrib.Syst.,
whohelpedtoimprovethispaper. vol.28,no.2,pp.462–474,Feb.2017.
|     |     |     |     |     |     |     |     | [22] R. R. | Sambasivan, | A.X.Zheng, |     | M.DeRosa, | E.Krevat, |     | S.Whitman, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---------- | --- | --------- | --------- | --- | ---------- |
M.Stroucken,W.Wang,L.Xu,andG.R.Ganger,‘‘Diagnosingperfor-
REFERENCES
mancechangesbycomparingrequestflows,’’inProc.8thUSENIXConf.
NetworkedSyst.Des.Implement.(NSDI).Berkeley,CA,USA:USENIX
| [1] G. Yu, | P.Chen, | and Z.Zheng, |     | ‘‘Microscaler: | Automatic |     | scaling for |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------------ | --- | -------------- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Association,2011,pp.43–56.
microserviceswithanonlinelearningapproach,’’inProc.IEEEInt.Conf.
|     |     |     |     |     |     |     |     | [23] S.Kandula,R.Mahajan,P.Verkaik,S.Agarwal,J.Padhye,andP.Bahl, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
WebServices(ICWS),Jul.2019,pp.68–75.
[2] P.Chen,Y.Qi,P.Zheng,andD.Hou,‘‘CauseInfer:Automaticanddis- ‘‘Detaileddiagnosisinenterprisenetworks,’’ACMSIGCOMMComput.
tributedperformancediagnosiswithhierarchicalcausalitygraphinlarge Commun.Rev.,vol.39,no.4,pp.243–254,Aug.2009.
distributed systems,’’ in Proc. IEEE Conf. Comput. Commun. (INFO- [24] H.HuangandS.P.Kasiviswanathan,‘‘Streaminganomalydetectionusing
|     |     |     |     |     |     |     |     | randomized | matrix | sketching,’’ |     | Proc. VLDB | Endowment, | vol. | 9, no. 3, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | ---------- | ---------- | ---- | --------- |
COM),Apr.2014,pp.1887–1895.
pp.192–203,Nov.2015.
[3] P.Chen,Y.Qi,X.Li,D.Hou,andM.Lyu,‘‘Arf-predictor:Effectivepre-
dictionofaging-relatedfailureusingentropy,’’IEEETrans.Dependable [25] F.T.Liu,K.M.Ting,andZ.-H.Zhou,‘‘Isolationforest,’’inProc.8thIEEE
SecureComput.,vol.15,no.4,pp.675–693,Jul./Aug.2018. Int.Conf.DataMining,Pisa,Italy,Dec.2008,pp.413–422.
[4] R.Fonseca,G.Porter,R.H.Katz,S.Shenker,andI.Stoica,‘‘X-trace:A [26] C.C.Aggarwal,OutlierAnalysis,2nded.NewYork,NY,USA:Springer,
| pervasivenetworktracingframework,’’inProc.4thUSENIXConf.Netw. |     |     |     |     |     |     |     | 2016. |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Syst.Des.Implement.(NSDI),Berkeley,CA,USA:USENIXAssociation, [27] V.Chandola,A.Banerjee,andV.Kumar,‘‘Anomalydetection:Asurvey,’’
| 2007,p.20. |     |     |     |     |     |     |     | ACMComput.Surv.,vol.41,no.3,p.15,2009. |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[5] Zipkin Homepage. Accessed: Oct. 21, 2019. [Online]. Available: [28] M.Ferdman,B.Falsafi,A.Adileh,O.Kocberber,S.Volos,M.Alisafaee,
https://zipkin.io/ D.Jevdjic, C.Kaynak, A.D.Popescu, and A.Ailamaki, ‘‘Clearing the
[6] S.Roy,A.C.Konig,I.Dvorkin,andM.Kumar,‘‘PerfAugur:Robustdiag- clouds: A study of emerging scale-out workloads on modern hard-
nosticsforperformanceanomaliesincloudservices,’’inProc.IEEE31st ware,’’ACMSIGARCHComput.Archit.News,vol.40,no.1,pp.37–48,
| Int.Conf.DataEng.,Apr.2015,pp.1167–1178. |     |     |     |     |     |     |     | Apr.2012. |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[7] C. Zhou and R.C.Paffenroth, ‘‘Anomaly detection with robust deep [29] H.KastureandD.Sanchez,‘‘Tailbench:Abenchmarksuiteandevaluation
autoencoders,’’inProc.23rdACMSIGKDDInt.Conf.Knowl.Discovery methodologyforlatency-criticalapplications,’’inProc.IEEEInt.Symp.
DataMining(KDD),2017,pp.665–674. WorkloadCharacterization(IISWC),Sep.2016,pp.1–10.
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 43425 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.Chenetal.:FrameworkofVWRandMS-BasedStreamingAnomalyDetectionforMicroserviceSystems
[30] J. Hauswald, M.A.Laurenzano, Y.Zhang, C.Li, A.Rovinski, [46] A. Cockcroft, ‘‘The evolution of microservices,’’ in Proc. ACM Learn.
A.Khurana, R.G.Dreslinski, T.Mudge, V.Petrucci, and L.Tang, Webinar,2016,pp.1–61.
‘‘Sirius: An open end-to-end voice and vision personal assistant and [47] G. Lawton, ‘‘LAMP lights enterprise development efforts,’’ Computer,
its implications for future warehouse scale computers,’’ in Proc. 20th vol.38,no.9,pp.18–20,2005.
Int.Conf.ArchitecturalSupportProgram.Lang.OperatingSyst.,2015,
pp.223–238.
[31] Y. Gan, Y.Zhang, D.Cheng, A.Shetty, P.Rathi, N.Katarki, A.Bruno,
J.Hu,B.Ritchken,andB.Jackson,‘‘Anopen-sourcebenchmarksuitefor HONGYANG CHEN is currently pursuing the
microservicesandtheirhardware-softwareimplicationsforcloud&edge bachelor’s degree with the School of Data and
systems,’’inProc.24thInt.Conf.ArchitecturalSupportProgram.Lang. ComputerScience,SunYat-senUniversity,where
OperatingSyst.,2019,pp.3–18. he also prepares to pursue the master’s degree
[32] Y.Gan,M.Pancholi,S.Hu,D.Cheng,Y.He,andC.Delimitrou,‘‘Seer: with the School of Data and Computer Science.
Leveragingbigdatatonavigatetheincreasingcomplexityofclouddebug-
Hiscurrentresearchinterestsincludedistributed
ging,’’inProc.ACMInt.Conf.ArchitecturalSupportforProgram.Lang.
systems,microservices,andcloudcomputing.
OperatingSyst.(ASPLOS),2019,pp.1–15.
[33] Elasticsearch.(2018).Filebeat.Accessed:Dec.3,2019.[Online].Avail-
able:https://www.elastic.co/beats/filebeat
[34] B.Elasticsearch,‘‘Filebeat,’’Software,Version6,Tech.Rep.,2018,no.1.
[35] P.Hunt,M.Konar,F.P.Junqueira,andB.Reed,‘‘Zookeeper:Wait-free
coordinationforInternet-scalesystems,’’inProc.USENIXAnnu.Tech. PENGFEI CHEN received the degree from the
Conf.,vol.8,no.9,2010,pp.1–14. DepartmentofComputerScience,Xi’anJiaotong
[36] K. Ranganathan. (2012). Netflix Shares Cloud Load Balancing and University,in2016.HeiscurrentlyaPh.D.advi-
Fail Over Tool: Eureka! Netflix Tech Blog. Accessed: Nov. 10, 2019. sorinSunYet-senUniversity.Hewasselectedas
[Online]. Available: https://netflixtechblog.com/netflix-shares-cloud-
a member of Rising Star Program of Microsoft
load-balancing-and-failover-tool-eureka-c10647ef95e5
ResearchAsia,fromJuly2012toNovember2012.
[37] M. Cohen and M. Hawthorne. (2013). Announcing Zuul: Edge Ser-
Aftergraduation,heworkedasaResearchScien-
vice in the Cloud. Netflix Tech Blog. Accessed: Nov. 10, 2019.
tistwithIBMResearch,China,fromJune2016to
[Online]. Available: https://netflixtechblog.com/announcing-zuul-edge-
January2018.HewaswiththeIBMT.J.Watson,
service-in-the-cloud-ab3af5be08ee
[38] X.Zhou,X.Peng,T.Xie,J.Sun,C.Ji,W.Li,andD.Ding,‘‘Faultanalysis fromFebruary2017toApril2017.Heiscurrently
and debugging of microservice systems: Industrial survey, benchmark an Associate Professor with the School of Data and Computer Science,
system,andempiricalstudy,’’IEEETrans.Softw.Eng.,tobepublished. Sun Yat-sen University. He is currently interested in distributed systems,
[39] X. Zhou, X.Peng, T.Xie, J.Sun, C.Ji, D.Liu, Q.Xiang, and C.He, AIOps,cloudcomputing,microservices,andblockchain.Especially,hehas
‘‘Latent error prediction and fault localization for microservice appli- strong skills in cloud computing. Until now, he has published more than
cations by learning from system trace logs,’’ in Proc. 27th ACM Joint 30articlesinsomeinternationalconferencesincludingtheIEEEINFOCOM,
MeetingEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.(ESEC/FSE), WWW,theIEEEICWS,theIEEEICSOC,theIEEEBigData,andjournals,
2019,pp.683–694. includingtheIEEETDSC,theIEEETR,theIEEETSC,theIEEETETC,
[40] C. Gormley and Z. Tong, Elasticsearch: The Definitive Guide: A Dis- andtheIEEETCC.HeservesasaProgramCommitteeMemberofmultiple
tributed Real-Time Search and Analytics Engine. Newton, MA, USA: conferences and a Reviewer of some internal journals such as the IEEE
O’Reilly,2015.
TRANSACTIONSONCYBERNETICS,InformationSciences,andNeurocomputing.
[41] J. Reynolds and C. Rosenthal. (2016). Vizceral Open Source.
Netflix Tech Blog. Accessed: Nov. 10, 2019. [Online]. Available:
https://netflixtechblog.com/vizceral-open-source-acc0c32113fe
GUANGBA YU received the B.E. degree from
[42] E.BetkeandJ.Kunkel,‘‘Real-timeI/O-monitoringofHPCapplications
theGuangzhouUniversityofChineseMedicine,
withSIOX,elasticsearch,GrafanaandFUSE,’’inProc.Int.Conf.High
Perform.Comput.Jaipur,India:Springer,2017,pp.174–186. China,in2018.Heiscurrentlypursuingthemas-
[43] Zipkin Span. Accessed: Nov. 10, 2019. [Online]. Available: ter’s degree with the School of Data and Com-
https://zipkin.io/zipkin/2.11.3/zipkin/zipkin2/Span.html puterScience,SunYat-senUniversity,China.His
[44] W.Gander,‘‘AlgorithmsfortheQRdecomposition,’’Res.Rep,vol.80, currentresearchareasincludedistributedsystems,
no.2,pp.1251–1268,1980. cloudcomputing,andAIdrivenoperations.
[45] A. Cockroft, ‘‘Microservices: Why, what, and how to get there,’’ in
MicroservicesWorkshopAllTopicsDeck.NewYork,NY,USA:ACM,
2016.
43426 VOLUME8,2020