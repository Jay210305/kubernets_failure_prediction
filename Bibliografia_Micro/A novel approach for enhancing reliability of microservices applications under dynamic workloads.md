ClusterComputing(2025)28:669
https://doi.org/10.1007/s10586-025-05471-1
(0123456789().,-volV)(0123456789,-().volV)
A novel approach for enhancing reliability of microservices
applications under dynamic workloads
Neha Kaushik1 • Harish Kumar1 • Vinay Raj2
Received:9November2024/Revised:5January2025/Accepted:3May2025/Publishedonline:3September2025
(cid:2)TheAuthor(s),underexclusivelicencetoSpringerScience+BusinessMedia,LLC,partofSpringerNature2025
Abstract
The increasing need for independently developed and deployed web-based applications has made microservices archi-
tecturepopularinthelastdecade.ItsbenefitshaveincentivizedlargeITcompanieslikeNetflix,Uber,andTwittertoadopt
it. However, the distributed and loosely coupled nature of microservices based applications introduces reliability chal-
lengesunderdynamicworkloads.Thefailureofamicroserviceinthepresenceofdynamicworkloadsmakesitsdependent
microservices unresponsive causing cascading failures and communication breakdowns resulting in reduced reliability.
Effective workload handling and robust microservices communication mechanisms are essential to sustaining the relia-
bilityofmicroservicesapplications.Thispaperproposesanovelapproachforthereliabilityimprovementofmicroservice
applications by focusing on these two issues. The proposed approach consists of four phases, the first phase assesses the
reliabilityofmicroservicesapplicationsundervaryingworkloadsintheabsenceoftheproposedapproachandtheseresults
are used later for performing empirical analysis. The second and third phases of the proposed approach have focused on
effectiveworkloadhandlingbypredictingthemicroservicesinstancesbasedontheforecastedworkload.Thefourthphase
reduces the potential points of failure associated with microservices communication by placing interdependent
microservices on the same node. To assess the performance of the proposed approach, an empirical investigation is
performed on a case study application by employing synthetic and realistic workloads. The experimental results have
shown that the proposed framework has significantly improved the reliability of the microservices application.
Keywords Microservices (cid:2) Reliability (cid:2) Machine learning (cid:2) Workloads
1 Introduction
Distributed systems have gained a lot of attention in the
pasttwodecadesasthedemandforindependentdesignand
deployment of the web applications has increased. These
systems play a key role in the timely delivery of diverse
HarishKumarandVinayRajhavecontributedequallytothis
business needs by supporting continuous integration and
work.
continuousdeliveryofservices.Microservicesarchitecture
& NehaKaushik is a distributed system evolved from monolithic and Ser-
20001902008@jcboseust.ac.in vice-Oriented Architectures (SOA) by enhancing their
HarishKumar principles to deliver applications with enhanced modular-
htanwar@jcboseust.ac.in ity, scalability, and maintainability [1, 2]. Microservices
VinayRaj architecture divides an application into small and inde-
vinayraj@nitt.edu pendent services called microservices responsible for per-
forming a single task [3, 30]. Each microservice can be
1 DepartmentofComputerEngineering,J.C.BoseUniversity
ofScienceandTechnology,YMCA,Faridabad, designed using a different programming language or
Haryana121006,India technology stack and can be deployed independently of
2 DepartmentofComputerApplications,NationalInstituteof other microservices residing in the system [4].
TechnologyTiruchirappalli,Tiruchirappalli,
TamilNadu620015,India
123

| 669 Page2of19 |     |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:669 |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
Microservices use HTTP resource API for communication usedforeffectivehandlingofdynamicworkloadsaspartof
with other services present in the application [5]. RQ3.Theproposedapproachconsistsoffourphasesandin
Despite several benefits, performance, reliability, and each phase an algorithm is stated for achieving the goal as
| security | are the | challenges | that | need | to be | addressed | in  | shown | in Fig. | 1.  |     |     |     |     |
| -------- | ------- | ---------- | ---- | ---- | ----- | --------- | --- | ----- | ------- | --- | --- | --- | --- | --- |
ordertoimprovethe qualityofMicroservicesArchitecture In the proposed approach, phase 1 is the reliability
(MSA) [6–8]. Distributed systems like microservices face assessment of the microservices application. In this phase,
silent communication breakdowns which makes the whole an algorithm for assessing the default reliability of the
application unavailable [9]. Most of the existing studies application against the dynamic workload has been devel-
haveimprovedthereliabilityofmicroservicesapplications oped. In phase 2, a machine learning model is trained to
either by focusing on varying workloads [10] or on the predict the number of instances required for handling the
interdependencies between the microservices [11]. In our user requests successfully. Phase 3 of the proposed
work, both varying workloads along with the interdepen- framework focuses on the prediction of the workloads for
dencies between the microservices are considered. the next time interval and also predicts the number of
According to the IEEE standard, Reliability is character- microserviceinstancesrequiredforhandlingthatworkload.
ized as the capacity of an application to execute its des- This way the application becomes reliable by taking
ignated functions within specified conditions throughout a proactiveactionforhandlingthedynamicenvironmentand
defined duration [11]. Dynamic workloads can lead to the user requests are serviced without failure. Proactive
resource exhaustion and make microservices applications action makes the application capable of handling the
unresponsive [12]. The services in an MSA based appli- upcoming workload without any failure. The last phase of
cation are loosely coupled i.e. they rely on other services the proposed approach reduces the potential points of
for some functionalities. So, failure of a microservice can failure associated with microservices communication by
have a cascading effect on its dependent services and can placing the predicted instances on the nodes such that the
lead to a breakdown in communication between services microservices that communicate more frequently are
and affect the overall reliability of the application placed on the same node. This strategic placement of
[9,13,14].Microservicesarchitecturesneedtoberesilient microservices reduces network latency and the risk of
and capable of recovering from such failures because if communication breakdowns, which are essential during
failures occur and the system is unable to recover quickly, dynamic workloads. Relying less on network communica-
it can lead to prolonged periods of reduced reliability. tion makes the system more robust to failures and reduces
Hence, a reliability improvement strategy should be cap- the likelihood that the failure of one service will affect
| able of | handling | dynamic | workload |     | situations | and | also | other | services. |     |     |     |     |     |
| ------- | -------- | ------- | -------- | --- | ---------- | --- | ---- | ----- | --------- | --- | --- | --- | --- | --- |
should be capable of handling the failures that can occur To summarise, this paper makes the following contri-
because of communication breakdown. butions to achieve the proposed objective:
| This        | paper     | addresses      | the challenge |          | of enhancing  |         | relia- |     |                                                  |                 |                  |               |               |             |
| ----------- | --------- | -------------- | ------------- | -------- | ------------- | ------- | ------ | --- | ------------------------------------------------ | --------------- | ---------------- | ------------- | ------------- | ----------- |
|             |           |                |               |          |               |         |        | •   | A literature                                     | survey is       | conducted        | to identify   |               | the factors |
| bility by   | proposing | a              | novel         | approach | for improving |         | the    |     |                                                  |                 |                  |               |               |             |
|             |           |                |               |          |               |         |        |     | affecting                                        | the reliability | of microservices |               | applications. |             |
| reliability | of        | microservices  | applications  |          | under         | dynamic |        |     |                                                  |                 |                  |               |               |             |
|             |           |                |               |          |               |         |        | •   | Proposedanovelapproachforimprovingthereliability |                 |                  |               |               |             |
| workloads.  | If        | an application |               | receives | sudden        | spikes  | in     |     |                                                  |                 |                  |               |               |             |
|             |           |                |               |          |               |         |        |     | of microservices                                 | application     |                  | under dynamic |               | workload.   |
resourcedemandsandthefluctuationsinworkloadpatterns
|     |     |     |     |     |     |     |     | •   | An efficient | machine | learning | model | is used | to predict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | -------- | ----- | ------- | ---------- |
refertodynamicworkload.Theproposedapproachhelpsin
|             |            |             |                  |                  |              |              |     |     | the microservices | instances | for | upcoming | workloads. |     |
| ----------- | ---------- | ----------- | ---------------- | ---------------- | ------------ | ------------ | --- | --- | ----------------- | --------- | --- | -------- | ---------- | --- |
| improving   | the        | reliability | of microservices |                  | applications |              | by  |     |                   |           |     |          |            |     |
| efficiently | handling   | the         | dynamic          | workload         |              | and reducing |     |     |                   |           |     |          |            |     |
| the chances | of         | failures    | caused           | by microservices |              | commu-       |     |     |                   |           |     |          |            |     |
| nication    | breakdown. | The         | following        | research         |              | questions    | are |     |                   |           |     |          |            |     |
framedtoarticulatethemotivationbehindthisstudyandto
| offer insights     |         | into the    | proposed | framework:  |             | RQ 1:         | What |     |     |     |     |     |     |     |
| ------------------ | ------- | ----------- | -------- | ----------- | ----------- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| are the            | factors | that affect | the      | reliability | of          | the microser- |      |     |     |     |     |     |     |     |
| vices application? |         | RQ          | 2: How   | can the     | reliability | of            | MSA  |     |     |     |     |     |     |     |
basedapplicationsbeimproved?RQ3:Whatistheroleof
| machine | learning | in improving |     | the reliability |     | of microser- |     |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
vices applications?
| To address   |               | RQ1, a | detailed | literature | survey   |             | is con- |     |     |     |     |     |     |     |
| ------------ | ------------- | ------ | -------- | ---------- | -------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| ducted to    | identify      | the    | factors  | impacting  | the      | reliability | of      |     |     |     |     |     |     |     |
| microservice | applications. |        | A        | four phase | approach |             | is pro- |     |     |     |     |     |     |     |
posed toaddress the RQ2 and different ML algorithms are Fig.1 Phasesintheproposedapproach
123

ClusterComputing(2025)28:669 Page3of19 669
• Extensivecomparisonofthereliabilityofthecasestudy is difficult because of their distributed architecture. Malki
application under dynamic workloads with and without etal.[16]haveconsideredtheworkloadconfigurationsand
using the proposed approach. predefined rate limits for predicting their effect on the
reliability of the microservices, The author found that
The rest of the paper is structured as follows: Sect. 2 pre-
limiting the API rate significantly improves the reliability
sents notable works on the reliability of service oriented
of microservices applications but also impacts the perfor-
systems and microservices. The proposed approach is dis-
mance and scalability of the application. The insights
cussed in Sect. 3. The machine learning model for
gainedfromthesestudiesunderscorethesignificanceofthe
microservices instance count and workload prediction is
reliabilityqualityattributeinenhancingthe overallquality
discussed in Sect. 4. Empirical Analysis of the proposed
of microservices applications. They reveal that to improve
framework is discussed in detail in Sect. 5. The threats to
reliability, it is essential to efficiently manage workload
validity of the proposed work are presented in Sect. 6 and
and address communication failures among microservices,
Sect. 7 concludes the paper.
which are inherent to the distributed architecture of these
applications. After identifying the factors, the subsequent
2 Literature review study focused on existing research addressing the reliabil-
ity of microservices applications and service oriented
systems.
Microservices, also referred to as services, are the funda-
Pietrantuono et al. [17] have proposed EMART, an
mental architectural elements of Microservices Architec-
operationalreliabilityassessmentmethodformicroservices
ture. In this section, firstly the factors affecting the
applications.Theauthorsuggested using the resulting data
reliability of microservices applications are identified and
for reliability improvement of the applications. Liu et al.
then a detailed study is conducted on the existing work
[18] improved the reliability of microservices applications
related tothe reliability of microservices applications. The
by placing dependent microservices together. In future
detailed study helped to identify the existing gaps for
work, the author suggested including environmental
reliability improvement and then further research was
diversity to predict the reliability of the application. Song
conductedtodeterminestrategiesforaddressingthesegaps
and Tilevich [19] have proposed a data flow based pro-
effectively.
gramming model for better resource utilization and
Wang et al. [6] have found out that performance, reli-
improved reliability. The author has focused on the
ability, and security are the quality attributes that require
development phase reliabilityimprovement while ignoring
more attention in order to improve the overall quality of
the operational reliability of the application. Camilli et al.
microservices applications. Jagadeesan and Mendiratta [9]
[20] have proposed a novel approach, MIPaRT for testing
discussedhowloosecouplingamongmicroservicesaffects
the performance and reliability of microservices applica-
theavailabilityoftheoverallapplication.Theauthorshave
tions under varying workloads. Shafi et al. [10] have pro-
proposedaservice meshandsidecarsbased frameworkto
posed CDAScaler, a novel approach to allocate CPU
analyse the reliability of microservices applications at
resources to each container of microservices applications
scale. Shafi et al. [10] have improved the reliability and
duringthescalingoperations.Theproposedapproachleads
performance of microservices applications by performing
to improved reliability and performance of microservices
dynamic scaling of resources for handling the workload.
applications. Wang et al. [21] have used Convolutional
The author has shown how the improper handling of
Neural Networks (CNN) and Long Short Term Memory
workload can lead to reduced reliability of microservices
(LSTM) for predicting the reliability of service oriented
applications. Li et al. [13] demonstrated how complex
systems. The authosr have used response time and
dependencies among tasks can make an entire microser-
throughput of component services at different time inter-
vices application unavailable, thereby degrading the user
vals for making the predictions. After reviewing the
experience. Consequently, the authors suggest focusing on
existing research on the reliability of microservices appli-
the reliability parameter during the execution of
cations, it is evident that there is a significant gap in work
microservices applications. Ding et al. [15] have empha-
aimed at improving reliability. Most existing studies have
sized considering the runtime environment and software
improved the reliability of microservices applications by
dynamic behaviour for reliability prediction and reliability
either focusing on varying workloads or on the interde-
improvement of Service oriented Systems. The author has
pendencies between microservices necessary for task
proposed a framework that uses run-time data such as
completion. To the best of our knowledge, no current
response time to predict and improve the reliability of
research addresses both efficient workload management
Service Oriented Systems. Francesco et al. [7] have iden-
and communication failures among microservices. This
tified that achieving reliability in MSA based applications
gap has driven us to develop strategies focusing on
123

669 Page4of19 ClusterComputing(2025)28:669
Fig.2 ProposedFramework
effective workload handling and robust microservices cost minimum. The proposed approach used a neural net-
communicationmechanismsforsustainingthereliabilityof work based workload prediction approach and performed
microservices applications. Now,furtherstudieswillfocus thescalingofresources.Inthepaper[25],theauthorsLuo
on the approaches used in existing works for managing et al. discuss that the colocation of dependent microser-
varyingworkloadsandaddressingfailuresarisingfromthe vices reduces the response time and network communica-
communication between microservices required to com- tion overhead of microservices application. Joseph and
plete a task. Chandrasekaran [26] performed the interaction aware
Abdullah et al. [12] have proposed an intelligent auto placement of microservices for reducing communication
scaling method that can predict the burst in workload and breakdowns among microservices and improving the
can make autoscaling decisions by provisioning the response time of the application. It is evident from the
resourcestothemicroservices.Theproblemwiththiswork study that predicting workload and taking appropriate
isthattheauthorusedamicroserviceapplicationconsisting actions based on these predictions are crucial for effective
of a single microservice. Yan et al. [22] have used Bi- workload management. The study also suggests that colo-
LSTM for predicting the workload of a microservices cating dependent microservices can significantly improve
application. The results show the proposed load prediction application response time by reducing potential commu-
method results in the effective utilization of resources nicationbreakdowns.Theproposedapproachimprovesthe
whilemeetingallservicelevelagreements.Fengetal.[23] reliability of microservices application by focusing on
have proposed FAST, a novel prediction model for pre- workload management and colocating dependent
dicting the dynamic workloads of microservices applica- microservices.
tions. The proposed model considers the relationship
between different workload changes and proper window
size, including trend correlation, time correlation, and 3 Proposed approach
randomfluctuations.Inthefuture,thepredictionmodelcan
be used to improve the quality of microservices applica- A machine learning based framework is proposed for
tions. Xu et al. [24] have proposed a CoScal approach to improving the reliability of the microservices architecture
improve the performance of microservices applications based application. The proposed framework mainly con-
while efficiently utilizing the resources and keeping the sists of four phases. Figure 2 shows the steps used by the
123

| ClusterComputing(2025)28:669 |     |     |     |     |     |     |     |     |     |     |     | Page5of19 |     | 669 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
proposed framework for improving the reliability of the Table1 ListofnotationsusedinAlgorithm1
| microservices |             | application. |          |             |            |     |           |     |     |            |     |     |     |     |
| ------------- | ----------- | ------------ | -------- | ----------- | ---------- | --- | --------- | --- | --- | ---------- | --- | --- | --- | --- |
|               |             |              |          |             |            |     | Notations |     |     | Definition |     |     |     |     |
| The           | first phase | deals        | with the | reliability | assessment | of  |           |     |     |            |     |     |     |     |
microservices application. The resource prediction model T Applicationmonitoringintervalduration
m
hasbeentrainedinthesecondphase.Thethirdphaseofthe n NumberofRequestssent
framework performs bursty workload aware horizontal R ApplicationThresholdResponsetime
t
scaling of the resources by using the instance prediction n f Numberoffailedrequests
model trained in phase 2 and also by predicting the res ResponseTimeoftheapplication
workload.Inthefourthphase,theinstancespredictedinthe x Reliability
| third phase | are  | placed | on the        | nodes based | on    | their com- |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------ | ------------- | ----------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| munication  | with | other  | microservices | and         | their | resource   |     |     |     |     |     |     |     |     |
requirement.Allfourphasesalongwiththefouralgorithms
|               |     |              |               |     |              |     | Responsetime(R)aretherequiredvariables. |         |        |            |     |        | Initially, | the   |
| ------------- | --- | ------------ | ------------- | --- | ------------ | --- | --------------------------------------- | ------- | ------ | ---------- | --- | ------ | ---------- | ----- |
| are discussed |     | in detail in | the following |     | subsections. |     |                                         |         | t      |            |     |        |            |       |
|               |     |              |               |     |              |     | algorithm                               | focuses | on the | deployment |     | of the | case       | study |
3.1 Reliability assessment microservicesapplication.Inthebeginning,noworkloadis
|                                                         |     |     |     |     |     |     | applied  | on the     | application, | hence  | the      | number | of      | requests |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------ | ------ | -------- | ------ | ------- | -------- |
|                                                         |     |     |     |     |     |     | sent (n) | and number | of           | failed | requests | (n )   | is 0 in | line 3.  |
| Inthefirststep,thereliabilityofmicroservicesapplication |     |     |     |     |     |     |          |            |              |        |          | f      |         |          |
Subsequently,aworkloadisappliedtotheapplicationfora
isestimated.Theresponsetimeofauserrequestisusedas
|                                                       |        |         |            |          |           |       | durationofT | ,duringwhichthevalueofnisincremented |               |                 |     |     |              |     |
| ----------------------------------------------------- | ------ | ------- | ---------- | -------- | --------- | ----- | ----------- | ------------------------------------ | ------------- | --------------- | --- | --- | ------------ | --- |
| abasicblockfordeterminingthereliability.Iftheresponse |        |         |            |          |           |       |             | m                                    |               |                 |     |     |              |     |
|                                                       |        |         |            |          |           |       | by 1 for    | each                                 | user request. | Simultaneously, |     |     | the response |     |
| time of                                               | a user | request | is greater | than the | threshold | value |             |                                      |               |                 |     |     |              |     |
time(res)ismeasuredandrecordedforeachcorresponding
| then that | request | is considered |     | a failed | request. | The |     |     |     |     |     |     |     |     |
| --------- | ------- | ------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n.Line8toline12focusesoncalculatingthereliabilityof
| Algorithm | 1 focuses | on  | the reliability |     | assessment | of the |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | --------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
microservices application in the presence of dynamic theapplication.Forthispurpose,theresponsetime(res)of
|           |            |     |        |         |        |            | each user | request | is  | compared | with | the | Application |     |
| --------- | ---------- | --- | ------ | ------- | ------ | ---------- | --------- | ------- | --- | -------- | ---- | --- | ----------- | --- |
| workloads | consisting | of  | bursty | and non | bursty | workloads. |           |         |     |          |      |     |             |     |
ThelistofnotationsusedinAlgorithm 1arerepresentedin Threshold Response time (R), if the response time of a
t
|     |     |     |     |     |     |     | user request | (res) | is greater | than | the | Threshold | Response |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ---------- | ---- | --- | --------- | -------- | --- |
Table 1.
|     |     |     |     |     |     |     | time (R) | then | that user | request | is  | considered | as  | failed |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------- | ------- | --- | ---------- | --- | ------ |
t
|           |     |         |           |     |             |        | request | and for | each | failed | request | the value | of  | nf is |
| --------- | --- | ------- | --------- | --- | ----------- | ------ | ------- | ------- | ---- | ------ | ------- | --------- | --- | ----- |
| Algorithm | 1   | aims to | determine | the | reliability | (x) of |         |         |      |        |         |           |     |       |
microservices application, Response Time of the applica- increased by 1. After calculating failed requests, the reli-
|            |     |        |           |          |     |             | ability (x) | of  | the microservices |     | application |     | is calculated |     |
| ---------- | --- | ------ | --------- | -------- | --- | ----------- | ----------- | --- | ----------------- | --- | ----------- | --- | ------------- | --- |
| tion (res) | and | Number | of failed | requests | (n  | ). For this |             |     |                   |     |             |     |               |     |
f
purpose, Application monitoring interval duration (T ), using the formula mentioned in line 13.
m
| Number | of Requests | sent       | (n),                                               | and Application |     | Threshold |     |     |     |     |     |     |     |     |
| ------ | ----------- | ---------- | -------------------------------------------------- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |             | Algorithm1 | ReliabilityassessmentoftheMicroservicesapplication |                 |     |           |     |     |     |     |     |     |     |     |
123

| 669 Page6of19 |     |     |     |     |     | ClusterComputing(2025)28:669 |     |
| ------------- | --- | --- | --- | --- | --- | ---------------------------- | --- |
Table2 Listofnotationsused
|     |     | Notations |     | Definition |     |     |     |
| --- | --- | --------- | --- | ---------- | --- | --- | --- |
inAlgorithm2
|     |     | N   |     | Numberofmicroservicesintheapplication |     |     |     |
| --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
|     |     | T   |     | Applicationmonitoringintervalduration |     |     |     |
m
|     |     | MC  |     | Numberofallocatedcontainerinstancesofeachmicroservice |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
i
|     |     | r   |     | ThresholdResponsetimeofeachmicroservice |     |     |     |
| --- | --- | --- | --- | --------------------------------------- | --- | --- | --- |
threshold
MC0
|     |     | i   |     | Updatedcontainerinstancesforeachmicroservice |     |     |     |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
The value of x will be between 0 and 1 and the higher instances of each microservice needed to handle the user
value of x will represent the higher reliability of the request such that the response time remains less than the
application.Theresultsoftheassessmentwilllaterbeused Threshold Response time of each microservice (rt). A
forcomparingtheperformanceoftheproposedframework reactive approach is used tocollect the performancetraces
of reliability improvement. The Algorithm 1 is applied that will be used later to train the response time model.
only for accessing the reliability of microservices appli- Performance traces are collected using a distributed tool,
cation with and without the proposed approach. Zipkin supporting OpenTracing. The first step for collect-
The output of Phase 1 serves as the foundation for a ingthetracesistoapplyworkloadontheapplicationusing
comparativeanalysisofthemicroservicesapplication with locust.io tool. The workload progressively increases by
andwithouttheproposedapproach.Initially,thecasestudy generatingconcurrentuserrequests,leadingtoasignificant
application was assessed for reliability without the pro- saturation of the microservice’s response time. Now a
posedsolution,followedbyareevaluationafterintegrating reactive autoscaling method is used by Algorithm 2 to
all phases. This approach not only demonstrated how scale in and scale out the container instances of all
reliability was evaluated but also eliminated the need for microservices based on the response time. This algorithm
redeployment to obtain baseline results without the pro- scales out the allocated container instances by adding one
posed method. Although the output of Phase 1 is not container instance whenever the 95th percentile of
directly used insubsequent phases, it remainsintegral as a response time is greater than the user defined Threshold
preparatorystepforestablishingameaningfulcomparison. Response time (rt) and scale-in the allocated resources
|     |     |     |     | whenever | three consecutive | intervals show | the 95th per- |
| --- | --- | --- | --- | -------- | ----------------- | -------------- | ------------- |
3.2 Microservice instance prediction model centile of the response time less than rt/2. Algorithm 2 is
| learning |     |     |     | similarto[27]byextendingitforscale-outandscale-inon |                   |             |                   |
| -------- | --- | --- | --- | --------------------------------------------------- | ----------------- | ----------- | ----------------- |
|          |     |     |     | the basis                                           | of response time. | The list of | notations used in |
This phase is responsible for the designing of a machine Algorithm 2 is represented in Table 2.
| learning model | that can predict                     | the number | of container |     |     |     |     |
| -------------- | ------------------------------------ | ---------- | ------------ | --- | --- | --- | --- |
|                | Algorithm2 ReactiveAutoscalingMethod |            |              |     |     |     |     |
123

| ClusterComputing(2025)28:669 |     |     |     |     |     |     |     |     | Page7of19 | 669 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
Table3 Listofnotationsused
|     |     |     | Notations |     |     | Definition |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | ---------- | --- | --- | --- | --- |
inAlgorithm3
|     |     |     | N   |     |     | Numberofmicroservicesintheapplication |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
|     |     |     | T   |     |     | Applicationmonitoringintervalduration |     |     |     |     |
m
|     |     |     | k           |     |     | Workloadwindowsize                                    |     |     |     |     |
| --- | --- | --- | ----------- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
|     |     |     | I           |     |     | MicroserviceInstancePredictionModel                   |     |     |     |     |
|     |     |     | W           |     |     | WorkloadPredictionModel                               |     |     |     |     |
|     |     |     | B           |     |     | Burstdetectionfunction                                |     |     |     |     |
|     |     |     | r threshold |     |     | ThresholdResponsetimeofeachmicroservice               |     |     |     |     |
|     |     |     | MC          |     |     | Numberofallocatedcontainerinstancesofeachmicroservice |     |     |     |     |
i
|     |     |     | MC0 |     |     | Updatedcontainerinstancesforeachmicroservice |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
i
In Algorithm 2, Line 3 to Line 12 are executed as long The collected data is used to train the microservice
astheworkloadisappliedontheapplication.Afterwaiting instance prediction model. From various supervised
forsomeT timetheperformancemetricssuchasresponse machinelearningalgorithms,theDecisionTreeRegression
m
time, CPU and memory utilization along with microser- model has been used for predicting the number of
vices call graphs are collected in Line 3. Now for each microservices instances needed for handling varying
microservice present in the application extract the 95th workloads. From the total dataset, 80% of the collected
percentile of response time (r) of all user requests that datasethasbeenusedfortrainingthemodeland20%ofthe
t
came in monitoring time. Now compare the r of each dataset has been used for testing the model.
t
| microservicewiththeirthresholdResponsetime(r |                |           |                        | ).           |         |           |       |     |     |     |
| -------------------------------------------- | -------------- | --------- | ---------------------- | ------------ | ------- | --------- | ----- | --- | --- | --- |
|                                              |                |           |                        | threshold    | I :ðw;r |           | Þ)MC‘ |     |     | ð1Þ |
| Nowifr                                       | isgreaterthanr |           | thereisaneedtoscalethe |              |         | threshold | i     |     |     |     |
| t                                            |                | threshold |                        |              |         |           |       |     |     |     |
| microservices                                | instance       | by 1 else | if r of the            | previous two |         |           |       |     |     |     |
t
intervalsandcurrentintervalislessthanthehalfofcurrent 3.3 Autoscaling with workload awareness
| r then | the number | of instances | is decreased | by 1 to |     |     |     |     |     |     |
| ------ | ---------- | ------------ | ------------ | ------- | --- | --- | --- | --- | --- | --- |
threshold
| save resource | wastage. | It can | be said that | Lines 5 to 9 |      |       |                 |           |          |     |
| ------------- | -------- | ------ | ------------ | ------------ | ---- | ----- | --------------- | --------- | -------- | --- |
|               |          |        |              |              | This | phase | of the proposed | framework | concerns | the |
focuses on collecting the number of instances required to autoscaling in the presence of the bursty workload. To
| handle different | workloads | such | that the response | time of |        |           |              |          |                 |     |
| ---------------- | --------- | ---- | ----------------- | ------- | ------ | --------- | ------------ | -------- | --------------- | --- |
|                  |           |      |                   |         | decide | the level | of intensity | of burst | and to allocate | the |
eachmicroserviceremainslessthanthethresholdresponse numberofcontainersforeachmicroservicebasedonit,an
| time value | in a resource | efficient | manner. Line | 11 repre- |                                        |     |     |     |             |     |
| ---------- | ------------- | --------- | ------------ | --------- | -------------------------------------- | --- | --- | --- | ----------- | --- |
|            |               |           |              |           | algorithmispresentedasshowninAlgorithm |     |     |     | 3.Thelistof |     |
sentsthechangeintimeintervali.e.nexttimeintervaland notations used in Algorithm 3 is represented in Table 3.
| then again | Line 3 to Line | 12  | are repeated. |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
123

669 Page8of19 ClusterComputing(2025)28:669
Algorithm3 AutoscalingwithBurstyWorkloadAwareness
Algorithm 3 represents the autoscaling of resources inPhase2oftheproposedapproach.Inline8,theBurstis
based on a bursty workload. Because initially there is no detected using functionB() which uses Sample Entropy as
burstyworkload,thevalueofvariableisBurstisequaltoF discussedin[28].Ifthereisaburstthenthevalueofywill
in line 2. Forecasting the workload and determining the be 1elseit will be0.Thepredictionis madeby observing
optimal number of instances required to handle it effi- the workload of k windows. The condition in line 10 rep-
ciently, from line 3 to line 32, ensures seamless perfor- resents the bursty workload predicted for the next time
mance while the application receives user requests intervalandnoburstatthecurrentmoment.Sointhatcase
continuously.NowforeachmicroserviceM whereivaries the number of instances n will be n i.e. the maximum
i c max
from1toNdenotingthenumberofmicroservices,waitfor instance count predicted in the last k windows and isBurst
T seconds. The T seconds represents the time taken to is set to T from F. The condition in line 13 addresses a
m m
predict the workload and the instances. In Line 6 the scenario where a bursty workload is forecasted for the
workload is predicted using a machine learning algorithm upcoming time interval, and the system is already
as discussed in Sect. 4. The number of microservices managingaburstyworkloadatthecurrentmoment.Inthis
instancesispredictedinline7usingAlgorithm 2discussed case,onlythevalueofn ischangedtomaximuminstance
c
123

| ClusterComputing(2025)28:669 |     |     |     |     |     |     |     |     | Page9of19 |     | 669 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
countn max andthevalueofisBurstremainsthesame.Line 3.4 Communication aware placement
15 represents the case when no burst is predicted for the of microservice instances
| next time interval | and at the current | time there | is no burst. |     |     |     |     |     |     |     |     |
| ------------------ | ------------------ | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
In such a case there is no need to allocate maximum Network latency affects the response time of the applica-
instance count, the instance count n c will be equal to the tion.Ifthenetworklatencycanbereducedthentheoverall
number of instances predicted using machine learning response time of the microservice application can also be
model I i.e. n~ tþ1 and the value of isBurst remains reduced significantly. Algorithm 4 achieves this purpose
unchanged. Line 17 represents the condition where the by using an interaction graph as input. This interaction
burstyworkloadispresentinthecurrentintervalbutinthe graphisagraphwithasingleinstanceofeachmicroservice
future it will not be there. So in that case the value of n deployed on different nodes. Vertex V of the interaction
c
will depend on whetherthe predicted instancesn~ tþ1 is less graphrepresentsthemicroserviceanditsCPUandmemory
than n . The variable n~ shows that in the future there need and edge E represents the communication link
| max | tþ1 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
willbealesserworkloadtohandle,soforefficientresource between the microservices. An edge weight is assigned to
utilization, it is better to use the n~ value and assign F each edge. The edge weight is calculated by observing the
tþ1
valuetoisBurst.Inothercases,thevalueofn c willben max , number of times two microservices communicate in an
and the value of isBurst remains unchanged because we interval of time. The result obtained after observation is
still have a bursty workload. Line 25 checks whether the then divided by 2 because communication was bidirec-
predicted number of instances is greater than the allocated tional and is assigned as edge weight on that particular
| number of instances | of microservices, | if true | then more | edge. |     |     |     |     |     |     |     |
| ------------------- | ----------------- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
instances are allocated accordingly otherwise the allocated Figure 3 depicts the interaction graph of the case study
instances are reduced accordingly. application. The case study application consists of three
microservicesCustomerservice,CatalogserviceandOrder
|     |     |     |     | Service.                               | Each      | node in                        | Fig. 3 represents |             | a microservice |               | of  |
| --- | --- | --- | --- | -------------------------------------- | --------- | ------------------------------ | ----------------- | ----------- | -------------- | ------------- | --- |
|     |     |     |     | thecasestudyapplication.ThenodesinFig. |           |                                |                   |             |                | 3areassigned  |     |
|     |     |     |     | aweight\mem_req,                       |           | cpu_req[wheremem_reqrepresents |                   |             |                |               |     |
|     |     |     |     | the amount                             | of        | memory                         | required          | by that     | microservice   |               | for |
|     |     |     |     | successful                             | execution | of                             | the task          | and cpu_req |                | is represent- |     |
|     |     |     |     | ing the                                | amount    | of CPU                         | required          | by that     | microservice   |               | for |
\mem_req,
|     |     |     |     | successful      | execution         | of              | the task.     | Here        | the   |         |          |
| --- | --- | --- | --- | --------------- | ----------------- | --------------- | ------------- | ----------- | ----- | ------- | -------- |
|     |     |     |     | cpu_req[weights |                   | are             | assigned      | to the      | nodes | using   | Algo-    |
|     |     |     |     | rithm 2         | where             | the application |               | is analysed |       | for a   | specific |
|     |     |     |     | period of       | time              | to collect      | the data.     | The         | arcs  | in Fig. | 3 rep-   |
|     |     |     |     | resents         | the bidirectional |                 | communication |             | link  | and an  | edge     |
|     |     |     |     | weight          | is assigned       | using           | Algorithm     | 2           | based | on the  | com-     |
municationbetweentherespectivenodes.Table4contains
|     |     |     |     | the list | of notations | used | in Algorithm |     | 4.  |     |     |
| --- | --- | --- | --- | -------- | ------------ | ---- | ------------ | --- | --- | --- | --- |
Fig.3 InteractionGraphofCaseStudyApplication
Table4 ListofnotationsusedinAlgorithm4
| Notations Definition |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
G=\V;E[ InteractionGraphwithverticesVandEdgesE.VisthesetcontainingallverticesofgraphGandEisthesetcontainingalledges
ofgraphG
| Vcpu need ItrepresentstheCPUneedofeachvertexV |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Vmem need
ItrepresentsthememoryneedofeachvertexV
| W EdgeWeight                                              |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S Setofnodes/devices                                      |     |     |     |     |     |     |     |     |     |     |     |
| count Arraycontainingpredictedinstancesofallmicroservices |     |     |     |     |     |     |     |     |     |     |     |
123

| 669 Page10of19 |            |                                                     |     |     |     |     |     |     | ClusterComputing(2025)28:669 |     |     |
| -------------- | ---------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
|                | Algorithm4 | Communicationawareplacementofmicroservicesinstances |     |     |     |     |     |     |                              |     |     |
The residual amount of CPU and memory available on yes then they are placed on device D and the array
| the nodes | should be greater | than | 0 and | are presented | by S. |          |           |            |              |     |      |
| --------- | ----------------- | ---- | ----- | ------------- | ----- | -------- | --------- | ---------- | ------------ | --- | ---- |
|           |                   |      |       |               |       | ASSIGNED | and count | is updated | accordingly. | And | also |
The same thing is written in line 2 of Algorithm 4. In line the residual resources on device D are updated. Line 14 is
| 3, an array | named ASSIGNED |     | is created | to keep | track of |             |             |         |               |           |      |
| ----------- | -------------- | --- | ---------- | ------- | -------- | ----------- | ----------- | ------- | ------------- | --------- | ---- |
|             |                |     |            |         |          | responsible | for placing | all the | microservices | instances | that |
whetherthenumberofinstancesofeachmicroservices are failed for communication aware placement by selecting
| adjusted | according to | the prediction | made | by using | Algo- |        |                  |         |              |     |     |
| -------- | ------------ | -------------- | ---- | -------- | ----- | ------ | ---------------- | ------- | ------------ | --- | --- |
|          |              |                |      |          |       | random | devices that can | fulfill | their needs. |     |     |
rithm 3 or not. Initially, no microservice instances are Figure 4representsthecommunicationawareplacement
| adjusted | so it is 0. Now | the | Edge weights | (W) | and set of |                   |         |        |           |           |     |
| -------- | --------------- | --- | ------------ | --- | ---------- | ----------------- | ------- | ------ | --------- | --------- | --- |
|          |                 |     |              |     |            | of microservices. | In this | graph, | the nodes | represent | the |
nodes(S)aresortedindecreasingorderinline4.Nowline serverordeviceonwhichtheservicesaredeployed.Based
5isresponsibleforthecommunicationawareplacementof
|     |     |     |     |     |     | on the residual | CPU and | Memory | space | available | on each |
| --- | --- | --- | --- | --- | --- | --------------- | ------- | ------ | ----- | --------- | ------- |
microservices and hence itcontinuesitsexecutionuntil all nodethemicroserviceinstancesaredeployedonthem.The
| the predicted | instances | of all | microservices | are | not placed |           |                  |     |          |                   |     |
| ------------- | --------- | ------ | ------------- | --- | ---------- | --------- | ---------------- | --- | -------- | ----------------- | --- |
|               |           |        |               |     |            | placement | of microservices |     | based on | their interaction |     |
i.e.untilASSIGNED[]doesnotbecome0.Line6findsthe reducesnetworkdelays.Thesizeofthegraphcanincrease
| microservices | with the | highest | edge | weight | means the |          |                 |        |                 |            |     |
| ------------- | -------- | ------- | ---- | ------ | --------- | -------- | --------------- | ------ | --------------- | ---------- | --- |
|               |          |         |      |        |           | with the | increase in the | number | of microservice | instances. |     |
microservices communicate more often. Line 7 finds the Theorderserviceandcatalogservicehavethehighestedge
device with the highest available CPU and memory weight so they are placed on the same node. The next
resources.Line8focusesonoptimizingresourceallocation largest edge weight links order service and customer ser-
by attempting to colocate the microservices whose CPU vice so they are kept on the same node. Customer service
and memory needs can be fulfilled by the residual resour- and catalog service communicate with each other through
| ces available | on the        | nodes/devices. | Line                   | 9 checks | if the       | API. |     |     |     |     |     |
| ------------- | ------------- | -------------- | ---------------------- | -------- | ------------ | ---- | --- | --- | --- | --- | --- |
| CPU and       | memory needs  | of             | both the microservices |          | can be       |      |     |     |     |     |     |
| fulfilled by  | the node with | the            | highest available      |          | resource, if |      |     |     |     |     |     |
123

ClusterComputing(2025)28:669 Page11of19 669
4 Instance and workload prediction model methods have been evaluated. The results show that deci-
sion tree regression performed better in comparison to the
In this paper, various machine learning techniques like other two methods. Table 5 represents the evaluation
linear regression, support vector regression and decision results.
tree regressionhave beenused forpredictingtheworkload
andmicroservicesinstancecount.Thefinalselectionofthe 4.2 Workload prediction model
machine learning technique has been made based on the
magnitude of relative error (MRE). The machine learning Thetaskoftheworkloadpredictionmodelistopredictthe
techniqueleadingtominimumMREisselectedasthefinal workload for the next time interval t?1 by observing the
technique for workload prediction and microservices workload of the past few k time intervals. For different
instances prediction. MRE is calculated as given below. values of k, different machine learning models like Linear
regression (LR), Support Vector regression (SVR) and
MRE
Decision Tree Regression (DTR) techniques have been
ActualResponseTime(cid:3)EstimatedResponseTime
¼ used for predicting the workload. The window size k and
ActualResponseTime
machine learning model with minimum MRE are selected
ð2Þ for workload prediction. Wikipedia workload has been
used for training and testing of machine learning models.
4.1 Microservice instance prediction model
Theresultsindicatethatlinearregressionoutperformedthe
other two methods. As shown in Table 6, linear regression
Initially, the data set for training the machine learning
has the lowest mean relative error (MRE) for k=12.
model is collected by using the approach discussed in
Phase 2 of Sect. 3. Out of the total data set, 80% of the
collected dataset has been used for training the model and
5 Empirical analysis
20%ofthedatasethasbeenusedfortestingthemodel.For
learning an appropriate instance prediction model, Linear
In this section, the performance of the benchmark appli-
regression (LR), Support Vector regression (SVR) and
cation integrated with the proposed framework is evalu-
Decision Tree Regression (DTR) machine learning
ated. The case study application Microservice Consul is
deployed, managed and scaled using docker, docker com-
pose and docker swarm. Locust.io, an open-source load
testing tool has been used for performance testing of the
application and Zipkin, an open-source distributed tracing
system used to trace calls across microservices. With the
help of Zipkin, response time of each microservice for a
user request can be collected. Prometheus, an open-source
monitoring system is used for collecting the CPU and
memory utilization metrics of each microservice instance.
Grafana, an open source analytics & monitoring solution
was used on top of Prometheus to offer visualization
functionalities for data. For training the workload predic-
tionmodelandforevaluatingtheperformanceofproposed
framework a real time workload [29] is used.
5.1 Case study application
A microservices application named Microservice Consul,
Fig.4 Communicationawareplacementofservices where users can buy books, is used to evaluate and com-
pare the performance of the proposed framework.
Microservice Consul consists of three microservices order
Table5 MREformicroserviceinstancepredictionmodel service, customer service and catalog service. The Cus-
Method LR SVR DTR tomer Service handles customer related data, the Catalog
Service manages the items in the catalog, and the Order
MRE 0.208 (cid:3)0.278 0.154
Service is responsible for orders processing by using Cat-
alog service and Customer service.
123

| 669 Page12of19 |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:669 |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
Table6 MREforworkloadpredictionmodel To assess the proposed approach better, the case study
|                   |     |     |     |     |     | application | is initially |             | deployed | using      | Docker | Swarm | and      |
| ----------------- | --- | --- | --- | --- | --- | ----------- | ------------ | ----------- | -------- | ---------- | ------ | ----- | -------- |
| WindowSize/Method |     | LR  | SVR |     | DTR |             |              |             |          |            |        |       |          |
|                   |     |     |     |     |     | we refer    | to this      | application |          | as Without |        | the   | proposed |
k=4 0.199 0.210 (cid:3)0.215 approach during result analysis. Another version of the
k=8 0.185 0.225 (cid:3)0.237 same case study application is deployed by integrating the
k=12 0.173 0.240 (cid:3)0.250 proposed algorithms with monitoring and logging pro-
cesses.ThisversionoftheapplicationisreferredtoasWith
|     |     |     |     |     |     | the proposed | approach |     | during | result | analysis. |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------ | ------ | --------- | --- | --- |
The Case study application consists of Customer ser- 5.2 Experimental parameters
| vice,Catalogservice,andOrderserviceasshowninFig. |     |     |     |     | 5.  |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The user accesses the application on its computer screen Intheexperimentalevaluation,tofindthemostappropriate
using a web browser. The user sends a request to the valueofmonitoringintervalduration(T m )andwindowsize
application by clicking an option on the website. The (k)theproposedframeworkwasimplementedfordifferent
request is forwarded to the application gateway. The values. The results lead to minimum response time and
applicationgateway routesuser requests totheappropriate minimum MRE for T = 90 s, duration of each interval=
m
service. Each service within the case study application is 8 min and k = 12. The user defined attribute r threshold is
responsible for executing a specific task. The application assigned the value 150 milliseconds during implementa-
gateway selects a microservice for processing the user tion. In the experimentation, several different values were
request based on the kind of request the user has sent and assigned and tested but the values defined in this section
the tasks for which a microservice is responsible. For werefoundtoperformbetterintermsofresponsetimeand
example, if a user wants to make a profile on the appli- resource utilization.
| cation or | wants to update | their | profile then | in that | case |     |     |     |     |     |     |     |     |
| --------- | --------------- | ----- | ------------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
those user requests will be forwarded to customer service, 5.3 Results and discussion
| because customer | service | is responsible | for | handling | user |     |     |     |     |     |     |     |     |
| ---------------- | ------- | -------------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
data.Oncetheuserrequestisroutedtoamicroservice,that This section discusses the evaluation results presented in
tablesforeachmicroserviceandthereliabilityoutcomesof
| microservice | is tasked | with | processing | it. Now | if a |     |     |     |     |     |     |     |     |
| ------------ | --------- | ---- | ---------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
microservice wants to communicate with other microser- the case study application with and without the proposed
framework.Sincethereliabilityoftheapplicationsdepends
vicesoftheapplicationthenitcanbedonewiththehelpof
the application gateway. After processing the user request, on the number of failed requests, during the analysis, we
|     |     |     |     |     |     | presented | the | details | of processed |     | requests | and | failed |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ------------ | --- | -------- | --- | ------ |
anHTTPresponseissenttotheapplicationgateway.After
that, the response is forwarded to the web browser. The requestsalongwiththecostofresourcesforeachserviceof
|                   |                  |     |           |               |     | the case | study application. |     | However, |     | in the | end, | the relia- |
| ----------------- | ---------------- | --- | --------- | ------------- | --- | -------- | ------------------ | --- | -------- | --- | ------ | ---- | ---------- |
| Fig. 6 represents | the interactions |     | and inter | relationships |     |          |                    |     |          |     |        |      |            |
among customer, catalog and order service. bility of the application is compared without and with the
|     |     |     |     |     |     | proposed | approach. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
TheresultsofcustomerservicearepresentedinTable7,
|     |     |     |     |     |     | which consists |           | of four   | columns. | The   | first     | column | lists     |
| --- | --- | --- | --- | --- | --- | -------------- | --------- | --------- | -------- | ----- | --------- | ------ | --------- |
|     |     |     |     |     |     | various        | synthetic | workloads |          | (SWL) | generated |        | using the |
locust.iotoolandareal-timeWikipediaworkloadavailable
|     |     |     |     |     |     | online. | Any number |     | of SWL | can | be generated |     | using |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------ | --- | ------------ | --- | ----- |
locust.iobutinthisexperimentation,onlysixSWLsnamed
|     |     |     |     |     |     | SWL 1,     | SWL 2, | SWL | 3, SWL | 4, SWL   | 5      | and SWL | 6 are |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ------ | -------- | ------ | ------- | ----- |
|     |     |     |     |     |     | generated. | Each   | SWL | varies | from the | others | because | dif-  |
ferentnumbersofrequestscanbesenttotheapplicationfor
|     |     |     |     |     |     | different  | durations | of            | time. | For the | analysis, |      | SWL1 is   |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------- | ----- | ------- | --------- | ---- | --------- |
|     |     |     |     |     |     | considered | with      | 500 requests, |       | SWL2    | with      | 1000 | requests, |
|     |     |     |     |     |     | SWL3 with  | 3000      | requests,     |       | SWL4    | with      | 5000 | requests, |
SWL5for7000andSWL6with10000requestspersecond.
|     |     |     |     |     |     | The second | column |     | of Table | 7 shows |     | the number | of  |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | -------- | ------- | --- | ---------- | --- |
requestsprocessedundertheseworkloads,thethirdcolumn
|     |     |     |     |     |     | indicates | the percentage |     | of  | user requests |     | that     | failed to |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | --- | ------------- | --- | -------- | --------- |
|     |     |     |     |     |     | respond   | on time,       | and | the | final column  |     | provides | a cost    |
Fig.5 MicroserviceArchitectureBasedCaseStudyApplication analysis, evaluating resource usage by the case study
123

| ClusterComputing(2025)28:669 |     |     |     |     |     | Page13of19 | 669 |
| ---------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
Fig.6 Illustrationofthe
interactionsand
interrelatipnshipsamong
microservices
application in presence and absence of the proposed The graphical comparison of the number of failed
framework. The results show that the application success- requestsofcustomerserviceinthepresenceandabsenceof
fully responds to more user requests when using the pro- the proposed framework is represented in Fig. 8 and it is
posed framework. observed that the proposed framework is resulting in a
Graphical comparison between the number of success- reduced number of failed requests.
fully executed user requests of customer service using the The cost comparison of customer service with and
proposed framework and without using the proposed withouttheproposedapproachisrepresentedinFig. 9.The
framework is represented in Fig. 7. It is clear from the graphical depiction of costs indicates that the proposed
graphical representation that the proposed framework is frameworkincreases costsinallscenariosexceptfor SWL
executing more number of user requests successfully. In 4. When SWL 4 is applied to the application then the
thecaseofSWL2,SWL3andSWL5themarginbetween proposed framework leads to reduced cost but in all other
the number of successfully executed user requests for workload cases, the proposed framework results in
| customer | service using both approaches | is the | least. increased | cost. |     |     |     |
| -------- | ----------------------------- | ------ | ---------------- | ----- | --- | --- | --- |
Table7 SimulationResultsofCustomerService
| Workload | ProcessedRequests(%) |     | FailedRequests(%) |     | Cost(%) |     |     |
| -------- | -------------------- | --- | ----------------- | --- | ------- | --- | --- |
WithoutUsingModel WithModel WithoutUsingModel WithModel WithoutUsingModel WithModel
| SWL1      | 97.01 | 98.05 | 2.99 | 1.95 | 1.3   | 1.35  |     |
| --------- | ----- | ----- | ---- | ---- | ----- | ----- | --- |
| SWL2      | 98.8  | 99.01 | 1.2  | 0.99 | 2.56  | 3.5   |     |
| SWL3      | 96.54 | 96.78 | 3.46 | 3.22 | 3.06  | 5.73  |     |
| SWL4      | 91.6  | 94    | 8.4  | 6    | 5.98  | 5.01  |     |
| SWL5      | 92.39 | 92.68 | 7.61 | 7.32 | 8.56  | 9.58  |     |
| SWL6      | 93.91 | 95.57 | 6.09 | 4.43 | 9.05  | 10.11 |     |
| Wikipedia | 90.17 | 93.95 | 9.83 | 6.05 | 10.52 | 13.72 |     |
123

| 669 Page14of19  |            |         |              |             |           |            |          |     |     |     |     | ClusterComputing(2025)28:669 |     |     |
| --------------- | ---------- | ------- | ------------ | ----------- | --------- | ---------- | -------- | --- | --- | --- | --- | ---------------------------- | --- | --- |
| The             | simulation | results | of           | the Catalog | service   |            | are pre- |     |     |     |     |                              |     |     |
| sented in       | Table      | 8. The  | results      | show        | that      | the number | of       |     |     |     |     |                              |     |     |
| failed requests |            | using   | the proposed |             | framework |            | has been |     |     |     |     |                              |     |     |
reduced.Inallscenarios,whetheritisasyntheticworkload
| or real   | time workload |       | situation, | the | proposed      | framework |         |     |     |     |     |     |     |     |
| --------- | ------------- | ----- | ---------- | --- | ------------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| increases | the cost      | while | improving  |     | the processed |           | request |     |     |     |     |     |     |     |
count.
| The           | comparison | of         | a number  | of     | successfully    |          | executed |     |     |     |     |     |     |     |
| ------------- | ---------- | ---------- | --------- | ------ | --------------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| user requests |            | by catalog | service   |        | in the          | presence | and      |     |     |     |     |     |     |     |
| absence       | of the     | proposed   | framework |        | is demonstrated |          | in       |     |     |     |     |     |     |     |
| Fig. 10.      | It is      | clear from | Fig.      | 8 that | the             | absence  | of the   |     |     |     |     |     |     |     |
proposed framework results in a reduced number of suc- Fig.8 GraphicalBasedComparisonofFailedRequestsofCustomer
Service
| cessfully  | executed    | services.   |           |              |            |           |          |     |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | --------- | ------------ | ---------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| The        | graphical   | comparison  |           | of a         | number     | of failed | user     |     |     |     |     |     |     |     |
| requests   | of catalog  | using       | and       | without      | using      | a         | proposed |     |     |     |     |     |     |     |
| framework  | is depicted |             | in Fig.   | 11. It       | is clearly | visible   | from     |     |     |     |     |     |     |     |
| the figure | that        | the absence | of        | the proposed |            | framework | is       |     |     |     |     |     |     |     |
| reducing   | the number  | of          | processed | requests.    |            | In the    | case of  |     |     |     |     |     |     |     |
SWL2andSWL4thenumberoffailedrequestsisalmost
| the same | in both | cases. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Graphicalbasedcomparisonofcostofcatalogservicein
| the presence  | and         | absence   | of        | the proposed |          | framework | of        |                                                       |     |     |     |     |     |     |
| ------------- | ----------- | --------- | --------- | ------------ | -------- | --------- | --------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| reliability   | improvement |           | is shown  | in           | Fig. 12. | In the    | case of   |                                                       |     |     |     |     |     |     |
| SWL1,         | SWL 3,      | SWL       | 4, and    | SWL 6        | the cost | of        | using and |                                                       |     |     |     |     |     |     |
| not using     | proposed    | framework |           | are almost   |          | the same  | but in    |                                                       |     |     |     |     |     |     |
|               |             |           |           |              |          |           |           | Fig.9 GraphicalBasedComparisonofCostofCustomerService |     |     |     |     |     |     |
| the remaining |             | cases of  | workload, | the          | cost     | without   | using     |                                                       |     |     |     |     |     |     |
| proposed      | framework   | is        | less than | the          | cost of  | resulting | from      |                                                       |     |     |     |     |     |     |
successfullywithoutusingtheproposedmodel.Onlyinthe
using the proposed framework. case of SWL 6, the proposed framework is leading to a
| The | number | of processed |     | requests, | failed | requests | and |         |        |                 |     |           |           |     |
| --- | ------ | ------------ | --- | --------- | ------ | -------- | --- | ------- | ------ | --------------- | --- | --------- | --------- | --- |
|     |        |              |     |           |        |          |     | reduced | number | of successfully |     | processed | requests. |     |
cost comparison of Order service are represented in The graphical comparison between the failed user
| Table 9. | The | results | show that | in  | the case | of  | real time |          |          |         |      |             |       |          |
| -------- | --- | ------- | --------- | --- | -------- | --- | --------- | -------- | -------- | ------- | ---- | ----------- | ----- | -------- |
|          |     |         |           |     |          |     |           | requests | of order | service | with | and without | using | the pro- |
workload, the number of processed requests is almost the posed framework is represented in Fig. 14. It is clearly
sameforbothmodelswhilethecostishigherinthecaseof
|     |     |     |     |     |     |     |     | visiblefromFig. |     | 14thatthenumberoffaileduserrequests |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------------------------- | --- | --- | --- | --- |
the proposed framework. fororderserviceisreducedusingtheproposedframework.
| Graphical | based | representation |     | of  | processed | requests | of  |         |          |        |       |          |           |     |
| --------- | ----- | -------------- | --- | --- | --------- | -------- | --- | ------- | -------- | ------ | ----- | -------- | --------- | --- |
|           |       |                |     |     |           |          |     | Only in | the case | of SWL | 6 the | proposed | framework | is  |
orderservicewithandwithoutproposedmodelisshownin resulting in an increased number of failed user requests.
| Fig. 13. | In the | presence | of various | workloads, |     | the | number |               |     |       |            |         |     |              |
| -------- | ------ | -------- | ---------- | ---------- | --- | --- | ------ | ------------- | --- | ----- | ---------- | ------- | --- | ------------ |
|          |        |          |            |            |     |     |        | The graphical |     | based | comparison | between |     | the costs of |
of processed requests using the proposed approach is order service with and without proposed work is shown in
| higher | than | the number |     | of user | requests |     | processed |          |        |         |     |           |     |             |
| ------ | ---- | ---------- | --- | ------- | -------- | --- | --------- | -------- | ------ | ------- | --- | --------- | --- | ----------- |
|        |      |            |     |         |          |     |           | Fig. 15. | In the | case of | SWL | 1 and SWL | 4,  | the cost is |
almostthesameinbothcasesandinthecaseofSWL4,the
costisreducedusingtheproposedframework.Intherestof
|     |     |     |     |     |     |     |     | the cases,      | proposed | framework |              | is increasing | the       | cost.   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | --------- | ------------ | ------------- | --------- | ------- |
|     |     |     |     |     |     |     |     | The performance |          | of        | the proposed |               | framework | is mea- |
suredbasedonthreemetrics,detailedinTable10.Thefirst
|     |     |     |     |     |     |     |     | one is Processed                 |            | requests,    | which          | shows         | the           | number of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | ---------- | ------------ | -------------- | ------------- | ------------- | ---------- |
|     |     |     |     |     |     |     |     | requests                         | served     | successfully |                | within        | the specified | time       |
|     |     |     |     |     |     |     |     | duration.                        | The second | parameter    |                | is the        | number        | of failed  |
|     |     |     |     |     |     |     |     | requests                         | which      | contains     | all the        | user requests | that          | were not   |
|     |     |     |     |     |     |     |     | served successfullywithinthetime |            |              |                | duration,no   |               | matter the |
|     |     |     |     |     |     |     |     | reason for                       | failure.   | The          | last attribute | is            | Reliability,  | repre-     |
sentingthereliabilityofmicroserviceapplicationswithand
Fig. 7 Graphical Based Comparison of Processed Requests of withouttheproposedframework.Thereliabilityofboththe
CustomerService
123

| ClusterComputing(2025)28:669 |     |     |     |     |     | Page15of19 | 669 |
| ---------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
Table8 SimulationResultsofCatalogService
| Workload | ProcessedRequests(%) |     | FailedRequests(%) |     | Cost(%) |     |     |
| -------- | -------------------- | --- | ----------------- | --- | ------- | --- | --- |
WithoutModel WithModel WithoutModel WithModel WithoutModel WithModel
| SWL1      | 97.03 | 98.35 | 2.97 | 1.65 | 1.44  | 1.89  |     |
| --------- | ----- | ----- | ---- | ---- | ----- | ----- | --- |
| SWL2      | 98.76 | 98.99 | 1.24 | 1.01 | 2.6   | 3.73  |     |
| SWL3      | 97.52 | 98.01 | 2.48 | 1.99 | 3     | 3.19  |     |
| SWL4      | 92.59 | 92.59 | 7.41 | 7.41 | 5.96  | 5.74  |     |
| SWL5      | 93.39 | 96.89 | 6.61 | 3.11 | 8.35  | 9.68  |     |
| SWL6      | 91.68 | 93.19 | 8.32 | 6.81 | 9.87  | 10.23 |     |
| Wikipedia | 92.31 | 93.96 | 7.69 | 6.04 | 10.66 | 11.46 |     |
Fig.10 GraphicalBased
ComparisonofProcessed
RequestsofCatalogService
Fig.11 GraphicalBased
ComparisonofFailedRequests
ofCatalogService
cases is calculated using the formula mentioned in Algo- failed requests contributes to determining the reliability of
rithm 1. The results show that the proposed framework is anapplication. That iswhythenextthreefiguresshow the
making the microservice application more reliable in the comparisonbetweentheproposedframeworkapproachand
presence of bursty workloads. the case study application not using the proposed frame-
Now the comparison in the performance of case study work in terms of processed requests, failed requests, and
applications with and without proposed framework is reliability of the complete application.
| made. A number | of successfully | processed requests | and |     |     |     |     |
| -------------- | --------------- | ------------------ | --- | --- | --- | --- | --- |
123

| 669 Page16of19 |     |     |     |     |     |     |     |     |     |     |     | ClusterComputing(2025)28:669 |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- |
AsshowninFig. 16,theproposed framework isalways failed requests in user requests results in improved relia-
leading to an improved number of successfully executed bility of the complete application. So we can say that the
user requests. Only in the case of SWL 5 the number of proposed framework is making the microservice architec-
processedrequestsinboththecasesisalmostthesamebut ture based application more reliable for bursty workloads.
inallotherworkloadcasestheproposedframeworkresults However, the cost of the resources is increasing with the
in better performance. proposed approach as resource utilization is high with the
| The          | graphical | representation |             | of  | failed requests |      | of the  | proposed | approach. |     |     |     |     |
| ------------ | --------- | -------------- | ----------- | --- | --------------- | ---- | ------- | -------- | --------- | --- | --- | --- | --- |
| Microservice |           | Consul         | application | is  | shown in        | Fig. | 17. The |          |           |     |     |     |     |
proposedframeworkresultedinareducednumberoffailed
| requests | in all | workload | cases | except | in the | SWL | 5 case. |     |     |     |     |     |     |
| -------- | ------ | -------- | ----- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- | --- |
WhenasyntheticworkSWL5isappliedtotheapplication
| the number | of          | failed      | requests  | in the        | presence     | and    | absence |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | --------- | ------------- | ------------ | ------ | ------- | --- | --- | --- | --- | --- | --- |
| of the     | proposed    | framework   | is        | almost        | same.        |        |         |     |     |     |     |     |     |
| In Fig.    | 18,         | a graphical | based     | comparison    |              | of the | relia-  |     |     |     |     |     |     |
| bility     | of complete | case        | study     | application   | with         | and    | without |     |     |     |     |     |     |
| proposed   | framework   |             | is done.  | It is clearly | visible      | from   | this    |     |     |     |     |     |     |
| figure     | that the    | proposed    | framework |               | is improving | the    | reli-   |     |     |     |     |     |     |
abilityoftheapplicationfordifferentworkloads.Incaseof
| SWL           | 5, the reliability |              | of case   | study        | application | is            | almost |        |                                                    |     |     |     |     |
| ------------- | ------------------ | ------------ | --------- | ------------ | ----------- | ------------- | ------ | ------ | -------------------------------------------------- | --- | --- | --- | --- |
| same for      | both               | the cases.   |           |              |             |               |        |        |                                                    |     |     |     |     |
| After         | analysing          |              | the       | performance  |             | of individual |        |        |                                                    |     |     |     |     |
| microservices |                    | and complete |           | application, | it          | can be        | con-   |        |                                                    |     |     |     |     |
| cluded        | that               | the proposed |           | framework    | is          | improving     | the    |        |                                                    |     |     |     |     |
|               |                    |              |           |              |             |               |        | Fig.13 | GraphicalBasedComparisonofProcessedRequestsofOrder |     |     |     |     |
| number        | of                 | successfully | processed |              | user        | requests      | and    |        |                                                    |     |     |     |     |
Service
| reducing | the                                            | number | of failed | requests. | This | reduction | of  |         |              |       |            |           |                   |
| -------- | ---------------------------------------------- | ------ | --------- | --------- | ---- | --------- | --- | ------- | ------------ | ----- | ---------- | --------- | ----------------- |
|          |                                                |        |           |           |      |           |     | Fig.    | 14 Graphical | Based | Comparison | of Failed | Requests of Order |
| Fig.12   | GraphicalBasedComparisonofCostofCatalogService |        |           |           |      |           |     | Service |              |       |            |           |                   |
Table9 SimulationResultsofOrderService
| Workload | ProcessedRequests(%) |     |     |     |     | FailedRequests(%) |     |     |     |     | Cost(%) |     |     |
| -------- | -------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | ------- | --- | --- |
WithoutUsing WithProposed WithoutUsing WithProposed WithoutUsing WithProposed
|           | ProposedModel |     |     | Model |     | ProposedModel |     |     | Model |     | ProposedModel |     | Model |
| --------- | ------------- | --- | --- | ----- | --- | ------------- | --- | --- | ----- | --- | ------------- | --- | ----- |
| SWL1      | 96.55         |     |     | 97.48 |     | 3.45          |     |     | 2.52  |     | 1.33          |     | 1.38  |
| SWL2      | 97.81         |     |     | 98.01 |     | 2.19          |     |     | 1.99  |     | 2.59          |     | 3.55  |
| SWL3      | 96.67         |     |     | 96.79 |     | 3.33          |     |     | 3.21  |     | 3.15          |     | 5.77  |
| SWL4      | 93.56         |     |     | 93.79 |     | 6.44          |     |     | 6.21  |     | 5.99          |     | 5.03  |
| SWL5      | 91.73         |     |     | 92.59 |     | 8.27          |     |     | 7.41  |     | 8.59          |     | 9.15  |
| SWL6      | 89.75         |     |     | 89.19 |     | 10.25         |     |     | 10.81 |     | 9.09          |     | 9.27  |
| Wikipedia | 91.27         |     |     | 91.95 |     | 8.73          |     |     | 8.05  |     | 10.59         |     | 11.55 |
123

| ClusterComputing(2025)28:669 |             |     |     |     |     |     |     |            |     | Page17of19 | 669 |
| ---------------------------- | ----------- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- |
| 6 Threats                    | to validity |     |     |     |     |     | 7   | Conclusion |     |            |     |
Several potential threats to validity have been identified in Reliability is a crucial Quality of Service (QoS) parameter
the proposed work. Firstly, the empirical evaluation of the foranysoftwareapplicationasitsignificantlyinfluencesits
proposed framework is carried out on a limited-scale case availability to users in bursty workloads. Conversely,
study application comprising only three microservices. microservices architecture is currently trending and has
Hence,itisessentialtoconductamorethoroughempirical emergedasahighlyfavouredapproachfordesigninglarge-
analysis of applications that feature a greater number of scale enterprise applications. While MSA offers various
microservices to determine the scalability of the proposed advantages over other architectural styles, their
| framework. | As the | number | of microservices |     | grows, | the |     |     |     |     |     |
| ---------- | ------ | ------ | ---------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
placementstrategythatconsiderscommunicationoverhead
maybecomeincreasinglytime-consuming,necessitatingan
| evaluation    | of the            | algorithm’s     | efficacy    | under        | such          | condi-   |     |     |     |     |     |
| ------------- | ----------------- | --------------- | ----------- | ------------ | ------------- | -------- | --- | --- | --- | --- | --- |
| tions.        | Also, reliability | in microservice |             | applications |               | can be   |     |     |     |     |     |
| influenced    | by a myriad       | of              | factors,    | such as      | communication |          |     |     |     |     |     |
| interruptions | due               | to hardware     | issues,     | failure      | of            | external |     |     |     |     |     |
| dependencies, | and               | deployment      | strategies, |              | etc. However, |          |     |     |     |     |     |
thisworkfocusedonlyoneffectiveworkloadhandlingand
| robust    | microservices | communication |             | mechanisms.     |     | Fur-     |     |     |     |     |     |
| --------- | ------------- | ------------- | ----------- | --------------- | --- | -------- | --- | --- | --- | --- | --- |
| thermore, | while the     | results       | demonstrate | that            | the | proposed |     |     |     |     |     |
| approach  | effectively   | enhanced      |             | the reliability |     | of the   |     |     |     |     |     |
microservicesapplicationbyreducingthenumberoffailed Fig. 16 Graphical Based Comparison of Processed Requests of
MicroserviceConsulApplication
| user requests, | it also               | resulted | in increased |     | costs compared |     |        |                                                     |     |     |     |
| -------------- | --------------------- | -------- | ------------ | --- | -------------- | --- | ------ | --------------------------------------------------- | --- | --- | --- |
| to the         | baseline application. |          |              |     |                |     |        |                                                     |     |     |     |
|                |                       |          |              |     |                |     | Fig.17 | GraphicalBasedComparisonofFailedRequestsofMicroser- |     |     |     |
Fig.15 GraphicalBasedComparisonofCostofOrderService viceConsulApplication
Table10 SimulationResultsofMicroserviceConsulApplication
| Workload | ProcessedRequests(%) |     |     |     | FailedRequests(%) |     |     |     | Cost(%) |     |     |
| -------- | -------------------- | --- | --- | --- | ----------------- | --- | --- | --- | ------- | --- | --- |
WithoutUsing WithProposed WithoutUsing WithProposed WithoutUsing WithProposed
|           | ProposedModel |     | Model |     | ProposedModel |     |     | Model | ProposedModel | Model |     |
| --------- | ------------- | --- | ----- | --- | ------------- | --- | --- | ----- | ------------- | ----- | --- |
| SWL1      | 94.06         |     | 96.75 |     | 5.94          |     |     | 3.25  | 0.94          | 0.96  |     |
| SWL2      | 96.23         |     | 98.74 |     | 3.77          |     |     | 1.26  | 0.96          | 0.98  |     |
| SWL3      | 93.45         |     | 96.08 |     | 6.55          |     |     | 3.92  | 0.93          | 0.96  |     |
| SWL4      | 89.52         |     | 93.74 |     | 10.48         |     |     | 6.26  | 0.89          | 0.93  |     |
| SWL5      | 90.39         |     | 90.85 |     | 9.61          |     |     | 9.15  | 0.90          | 0.90  |     |
| SWL6      | 91.91         |     | 94.99 |     | 8.09          |     |     | 5.01  | 0.91          | 0.94  |     |
| Wikipedia | 88.92         |     | 94.33 |     | 11.08         |     |     | 5.67  | 0.88          | 0.94  |     |
123

| 669 Page18of19 |     |     |     |     |     |     |     |               |     |               |          | ClusterComputing(2025)28:669 |            |               |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | -------- | ---------------------------- | ---------- | ------------- |
|                |     |     |     |     |     |     |     | 3. Kaushik,   | N., | Kumar,        | H., Raj, | V.: Empirical                |            | evaluation of |
|                |     |     |     |     |     |     |     | microservices |     | architecture. | In       | International                | Conference | on            |
CommunicationandIntelligentSystems(pp.241-253).Springer,
Singapore(2022)
|     |     |     |     |     |     |     |     | 4. Kaushik, | N., Kumar,  | H., | Raj,       | V.: Micro | frontend      | based perfor- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ---------- | --------- | ------------- | ------------- |
|     |     |     |     |     |     |     |     | mance       | improvement | and | prediction | for       | microservices | using         |
machinelearning.J.GridComput.22(2),1–26(2024)
|     |     |     |     |     |     |     |     | 5. Lercher,A.,Glock,J.,Macho,C.,Pinzger,M.:MicroserviceAPI |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
evolutioninpractice:astudyonstrategiesandchallenges.J.Syst.
Software112110(2024)
|     |     |     |     |     |     |     |     | 6. Wang, | Y., Kadiyala, | H., | Rubin, | J.: Promises | and | challenges of |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------ | ------------ | --- | ------------- |
microservices:anexploratorystudy.Empir.Softw.Eng.26(4),63
(2021)
|                   |     |                  |     |                |     |                 |     | 7. Di Francesco, |     | P., Lago,    | P.,     | Malavolta, | I.: Architecting | with        |
| ----------------- | --- | ---------------- | --- | -------------- | --- | --------------- | --- | ---------------- | --- | ------------ | ------- | ---------- | ---------------- | ----------- |
| Fig. 18 Graphical |     | Based Comparison |     | of Reliability |     | of Microservice |     |                  |     |              |         |            |                  |             |
|                   |     |                  |     |                |     |                 |     | microservices:   |     | a systematic | mapping | study.     | J. Syst.         | Softw. 150, |
ConsulApplication
77–97(2019)
|     |     |     |     |     |     |     |     | 8. Li,S.,Zhang,H.,Jia,Z.,Zhong,C.,Zhang,C.,Shan,Z.,Babar, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
decentralisedanddistributednaturecanimpactapplication M.A.: Understanding and addressing quality attributes of
reliabilityduringburstyworkloads.Thispaperintroducesa microservicesarchitecture:asystematicliteraturereview.Inform.
SoftwareTechnol.131,106449(2021)
| framework           | aimed | at            | enhancing |      | the         | reliability | of      |                |     |                 |     |             |         |             |
| ------------------- | ----- | ------------- | --------- | ---- | ----------- | ----------- | ------- | -------------- | --- | --------------- | --- | ----------- | ------- | ----------- |
|                     |       |               |           |      |             |             |         | 9. Jagadeesan, | L.  | J., Mendiratta, |     | V. B.: When | failure | is (not) an |
| microservices-based |       | applications, |           | with | comparative |             | results |                |     |                 |     |             |         |             |
option:reliabilitymodelsformicroservicesarchitectures.In2020
| demonstrating | satisfactoryoutcomes.Becauseofhardware |     |     |     |     |     |     |      |               |           |     |             |             |       |
| ------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | ------------- | --------- | --- | ----------- | ----------- | ----- |
|               |                                        |     |     |     |     |     |     | IEEE | International | Symposium |     | on Software | Reliability | Engi- |
neeringWorkshops(ISSREW),pp.19–24.IEEE(2020)
| constraints,   | a small | size     | case      | study application |     | is used   | but   |                                                              |                  |     |         |             |     |              |
| -------------- | ------- | -------- | --------- | ----------------- | --- | --------- | ----- | ------------------------------------------------------------ | ---------------- | --- | ------- | ----------- | --- | ------------ |
|                |         |          |           |                   |     |           |       | 10. Shafi,N.,Abdullah,M.,Iqbal,W.,Erradi,A.,Bukhari,F.:2024. |                  |     |         |             |     |              |
| in the future, | the     | proposed | framework |                   | can | be tested | for a |                                                              |                  |     |         |             |     |              |
|                |         |          |           |                   |     |           |       | Cdascaler:                                                   | a cost-effective |     | dynamic | autoscaling |     | approach for |
large real time microservices application. The outcomes containerizedmicroservices.ClusterComput.pp.1–21
demonstratethattheproposedframeworkhasincreasedthe 11. Wang, H., Wang, L., Yu, Q., Zheng, Z., Bouguettaya, A., Lyu,
|              |                   |             |             |             |       |               |     | M.R.:    | Online   | reliability | prediction       | via | motifs-based | dynamic     |
| ------------ | ----------------- | ----------- | ----------- | ----------- | ----- | ------------- | --- | -------- | -------- | ----------- | ---------------- | --- | ------------ | ----------- |
| cost of      | the microservices |             | application |             | while | improving     |     |          |          |             |                  |     |              |             |
|              |                   |             |             |             |       |               |     | Bayesian | networks | for         | service-oriented |     | systems.     | IEEE Trans. |
| reliability. | So in             | the future, |             | an approach | for   | the efficient |     |          |          |             |                  |     |              |             |
SoftwareEng.43(6),556–579(2016)
utilizationofresourcescanbeintegratedwiththeproposed 12. Abdullah,M.,Iqbal,W.,Berral,J.L.,Polo,J.,Carrera,D.:Burst-
framework and other techniques like Normalized Entropy aware predictive autoscaling for containerized microservices.
IEEETrans.Serv.Comput.15(3),1448–1460(2020)
| (NE) and | Fast Fourier |            | Transformation |     | (FFT) | can also | be  |             |            |          |                          |                    |     |                |
| -------- | ------------ | ---------- | -------------- | --- | ----- | -------- | --- | ----------- | ---------- | -------- | ------------------------ | ------------------ | --- | -------------- |
|          |              |            |                |     |       |          |     | 13. Li, Z., | Yu, H.,    | Fan, G., | Zhang,                   | J.: Cost-efficient |     | fault-tolerant |
| explored | for burst    | detection. |                |     |       |          |     |             |            |          |                          |                    |     |                |
|          |              |            |                |     |       |          |     | workflow    | scheduling |          | for deadline-constrained |                    |     | microservice-  |
basedapplicationsinclouds.IEEETransactionsonNetworkand
ServiceManagement(2023)
Author contributions Neha Kaushik has performed the literature 14. Xie,S.,Wang,J.,Li,B.,Zhang,Z.,Li,D.,Hung,P.C.:PBScaler:
reviewandidentifiedtheproblemstatement.Theideawasdiscussed a bottleneck-aware autoscaling framework for microservice-
and validated by Harish Kumar and Vinay Raj. The experimental based applications. IEEE Transactions on Services Computing
| work, analysis | and | writing | the draft | of the | manuscript | was | done by | (2024) |     |     |     |     |     |     |
| -------------- | --- | ------- | --------- | ------ | ---------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
NehaKaushik.TheresultswereverifiedbyHarishKumarandVinay 15. Ding, Z., Xu, T., Ye, T., Zhou, Y.: Online prediction and
Rajhasreviewedthefinaldraftofthepaper. improvement of reliability for service oriented systems. IEEE
Trans.Reliab.65(3),1133–1148(2015)
Funding NotApplicable. 16. ElMalki,A.,Zdun,U.,Pautasso,C.:ImpactofAPIratelimiton
|     |     |     |     |     |     |     |     | reliability | of microservices-based |     |     | architectures. | In  | 2022 IEEE |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------------- | --- | --- | -------------- | --- | --------- |
Data availability No datasets were generated or analysed during the International Conference on Service-Oriented System Engineer-
| currentstudy.      |     |                                        |     |     |     |     |     | ing(SOSE),pp.19–28.IEEE(2022) |         |              |                |                 |             |                |
| ------------------ | --- | -------------------------------------- | --- | --- | --- | --- | --- | ----------------------------- | ------- | ------------ | -------------- | --------------- | ----------- | -------------- |
|                    |     |                                        |     |     |     |     |     | 17. Pietrantuono,             | R.,     | Russo,       | S., Guerriero, | A.:             | Testing     | microservice   |
|                    |     |                                        |     |     |     |     |     | architectures                 | for     | operational  | reliability.   |                 | Software    | Test. Verific. |
| Declarations       |     |                                        |     |     |     |     |     | Reliab.30(2),e1725(2020)      |         |              |                |                 |             |                |
|                    |     |                                        |     |     |     |     |     | 18. Liu, Z.,                  | Yu, H., | Fan,         | G., Chen,      | L.: Reliability | modelling   | and            |
|                    |     |                                        |     |     |     |     |     | optimization                  | for     | microservice |                | based cloud     | application | using          |
| Conflictofinterest |     | Theauthorsdeclarenocompetinginterests. |     |     |     |     |     |                               |         |              |                |                 |             |                |
multiagentsystem.IETCommun.16(10),1182–1199(2022)
|     |     |     |     |     |     |     |     | 19. Song, | Z., Tilevich, |     | E.: Equivalence-enhanced |     |     | microservice |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------------------------ | --- | --- | ------------ |
workfloworchestrationtoefficientlyincreasereliability.In2019
References
|     |     |     |     |     |     |     |     | IEEE | International | Conference |     | on Web | Services | (ICWS), |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | ---------- | --- | ------ | -------- | ------- |
pp.426–433.IEEE(2019)
1. Raj, V., Sadam, R.: Patterns for migration of SOA based appli- 20. Camilli, M., Guerriero, A., Janes, A., Russo, B., Russo, S.:
cations to microservices architecture. J. Web Eng. 20(5), Microservices integrated performance and reliability testing. In
1229–1246(2021) Proceedings of the 3rd ACM/IEEE International Conference on
2. Tapia, F., Mora, M.A., Fuertes, W., Aules, H., Flores, E., AutomationofSoftwareTest,pp.29–39(2022)
Toulkeridis, T.: From monolithic systems to microservices: a 21. Wang,H.,Yang,Z.,Yu,Q.,Hong,T.,Lin,X.:Onlinereliability
comparative study of performance. Appl. Sci. 10(17), 5797 timeseriespredictionviaconvolutionalneuralnetworkandlong
(2020)
123

| ClusterComputing(2025)28:669 |     |     |     |     |     |     |     | Page19of19 | 669 |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
short term memory for service-oriented systems. Knowl.-Based Harish Kumar is currently
| Syst.159,132–147(2018) |     |     |     |     |     |     | working | as Associate | Professor |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --------- |
22. Yan, M., Liang, X., Lu, Z., Wu, J., Zhang, W.: HANSEL: in Department of Computer
adaptive horizontal scaling of microservices using Bi-LSTM. Engineering, J. C. Bose
| Appl.SoftComput.105,107216(2021) |     |     |     |     |     |     | University | of  | Science and |
| -------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- |
23. Feng, B., Ding, Z., Jiang, C.: FAST: a forecasting model with Technology, Faridabad, India.
adaptive sliding window and time locality integration for His research interest includes
dynamic cloud workloads. IEEE Trans. Serv. Comput. 16(2), Microservices,Softwaretesting,
| 1184–1197(2022) |     |     |     |     |     |     | MachineLearning. |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
24. Xu,M.,Song,C.,Ilager,S.,Gill,S.S.,Zhao,J.,Ye,K.,Xu,C.:
CoScal:multifacetedscalingofmicroserviceswithreinforcement
| learning. | IEEE | Trans. | Netw. | Serv. Manage. | 19(4), | 3995–4009 |     |     |     |
| --------- | ---- | ------ | ----- | ------------- | ------ | --------- | --- | --- | --- |
(2022)
25. Luo,S.,Xu,H.,Lu,C.,Ye,K.,Xu,G.,Zhang,L.,He,J.,Xu,C.:
| An in-depth | study | of  | microservice | call graph | and | runtime per- |     |     |     |
| ----------- | ----- | --- | ------------ | ---------- | --- | ------------ | --- | --- | --- |
formance.IEEETrans.ParallelDistrib.Syst.33(12),3901–3914
| (2022) |     |     |     |     |     |     | Vinay | Raj is currently | working |
| ------ | --- | --- | --- | --- | --- | --- | ----- | ---------------- | ------- |
26. Joseph, C.T., Chandrasekaran, K.: IntMA: dynamic interaction- as Assistant Professor in the
aware resource allocation for containerized microservices in Department of Computer
cloudenvironments.J.Syst.Architect.111,101785(2020) Applications, NIT Tiruchirap-
27. Iqbal, W., Dailey, M.N., Carrera, D., Janecek, P.: Adaptive palli.Hecompletedhisfull-time
resourceprovisioningforreadintensivemulti-tierapplicationsin Ph.D. from NIT Warangal and
thecloud.Futur.Gener.Comput.Syst.27(6),871–879(2011)
|     |     |     |     |     |     |     | M.Tech | from BITS | Pilani. His |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ----------- |
28. Tahir,F.,Abdullah,M.,Bukhari,F.,Almustafa,K.M.,Iqbal,W.:
|        |          |       |           |     |           |            | research | interests      | include Soft- |
| ------ | -------- | ----- | --------- | --- | --------- | ---------- | -------- | -------------- | ------------- |
| Online | workload | burst | detection | for | efficient | predictive |          |                |               |
|        |          |       |           |     |           |            | ware     | architectures, | Microser-     |
autoscalingofapplications.IEEEAccess8,73730–73745(2020)
|             |                |     |                           |     |     |               | vices, | Serverless | Computing,  |
| ----------- | -------------- | --- | ------------------------- | --- | --- | ------------- | ------ | ---------- | ----------- |
| 29. Stefan, | S., Niculescu, |     | V.: Microservice-oriented |     |     | workload pre- |        |            |             |
|             |                |     |                           |     |     |               | Cloud  | Computing  | and Machine |
dictionusingdeeplearning.e-InformaticaSoftwareEng.J.16(1)
|     |     |     |     |     |     |     | Learning. | He has | worked as |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --------- |
(2022)
|          |            |                |     |              |     |              | Senior    | software | Engineer in |
| -------- | ---------- | -------------- | --- | ------------ | --- | ------------ | --------- | -------- | ----------- |
| 30. Raj, | V., Sadam, | R.: Evaluation |     | of SOA-based | web | services and |           |          |             |
|          |            |                |     |              |     |              | Capgemini | and      | Software    |
microservicesarchitectureusingcomplexitymetrics.SNComput.
DeveloperinTCS,Hyderabad.
Sci.2,1–10(2021)
| Publisher’s | Note Springer |     | Nature | remains neutral |     | with regard to |     |     |     |
| ----------- | ------------- | --- | ------ | --------------- | --- | -------------- | --- | --- | --- |
jurisdictionalclaimsinpublishedmapsandinstitutionalaffiliations.
SpringerNatureoritslicensor(e.g.asocietyorotherpartner)holds
exclusiverightstothisarticleunderapublishingagreementwiththe
| author(s) | or other | rightsholder(s); |     | author | self-archiving | of the |     |     |     |
| --------- | -------- | ---------------- | --- | ------ | -------------- | ------ | --- | --- | --- |
acceptedmanuscriptversionofthisarticleissolelygovernedbythe
termsofsuchpublishingagreementandapplicablelaw.
NehaKaushikisaPh.D.scholar
|     |     |     |     | in Department  |            | of Computer    |     |     |     |
| --- | --- | --- | --- | -------------- | ---------- | -------------- | --- | --- | --- |
|     |     |     |     | Engineering,   | J.         | C. Bose        |     |     |     |
|     |     |     |     | University     | of         | Science and    |     |     |     |
|     |     |     |     | Technology,    | Faridabad, | India.         |     |     |     |
|     |     |     |     | She has        | completed  | her            |     |     |     |
|     |     |     |     | B.Tech[CSE]    | from       | MDU, Roh-      |     |     |     |
|     |     |     |     | tak, and       | M.Tech     | [CE] from      |     |     |     |
|     |     |     |     | JCBUST,        | Faridabad. | Her            |     |     |     |
|     |     |     |     | research       | interest   | includes Ser-  |     |     |     |
|     |     |     |     | vice Oriented  |            | Architectures, |     |     |     |
|     |     |     |     | Microservices, |            | Machine        |     |     |     |
Learning.
123