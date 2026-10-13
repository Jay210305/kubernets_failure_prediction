2023 IEEE/ACM 18th Symposium on Software Engineering for Adaptive and Self-Managing Systems (SEAMS)
CHESS: A Framework for Evaluation of
Self-adaptive Systems based on Chaos Engineering
Sehrish Malik∗ Moeen Ali Naqvi∗ Leon Moonen∗§
∗Simula Research Laboratory, Oslo, Norway §BI Norwegian Business School, Oslo, Norway
Email: {sehrish, moeen}@simula.no, leon.moonen@computer.org
Abstract—There is an increasing need to assess the correct self-healing systems that build on chaos engineering princi-
behavior of self-adaptive and self-healing systems due to their ples [6]. CHESS systematically perturbates the system-under-
adoption in critical and highly dynamic environments. However,
evaluation and records how the system responds to those
thereisalackofsystematicevaluationmethodsforself-adaptive
perturbations. The artifact1 presented in this paper provides
andself-healingsystems.WeproposedCHESS,anovelapproach
to address this gap by evaluating self-adaptive and self-healing an extensive overview of the use of CHESS through two
systemsthroughfaultinjectionbasedonchaosengineering(CE). microservice-based case studies: a smart office case study
The artifact presented in this paper provides an extensive and an existing demo application called Yelb. Concretely, the
overview of the use of CHESS through two microservice-based
artifactconsistsof(i)predefinedfunctionalandinfrastructural
case studies: a smart office case study and an existing demo
level fault injection scenarios, (ii) a self-monitoring service
applicationcalledYelb.Itcomeswithamanagingsystemservice,
a self-monitoring service, as well as five fault injection scenarios that presents extensive logs for the deployed services’ normal
coveringinfrastructurefaultsandfunctionalfaults.Eachofthese andabnormalbehaviors,(iii)themanagingsystemservicethat
components can be easily extended or replaced to adopt the reacts to the system’s abnormal behavior traces and brings
CHESS approach to a new case study, help explore its promises
the system back to a stable condition, and (iv) a comparison
and limitations, and identify directions for future research.
of the service failure and cascading effects with and without
Index Terms—self-healing, resilience, chaos engineering, eval-
uation, artifact. deployment of the managing system service.
Theremainderofthispaperisorganizedasfollows.InSec-
I. INTRODUCTION tion II, we summarize self-adaptive and self-healing systems
Self-adaptive systems (SAS) and self-healing systems (SHS) for the microservice architecture, evaluation of these systems
arebecomingincreasinglyimportantinfieldssuchastheInter- based on CE, and position CHESS in the landscape of self-
netofThings,Industry4.0,andsmartcities[1].Thesesystems adaptive system artifacts. Section III presents the design and
are designed to operate in highly dynamic environments and architectureofCHESS,alongwiththemicroservice-basedcase
areexpectedtohandleuncertaintyandunanticipatedbehavior, studies and test scenarios considered for the fault injection.
as well as provide fault tolerance and resilience. However, Section IV describes how to use the artifact with both of
due to the complexity and dynamic nature of these systems, the case studies and presents the results of the fault injection
it is challenging to anticipate all possible scenarios that these scenarios.WeconcludeinSectionV,includingdiscussionsof
systems will encounter. This is particularly important for the the artifact’s applicability and directions for future work.
evaluation of these systems, which requires assessing the
correct behavior of these systems.
II. BACKGROUNDANDPOSITIONINGOFTHEARTIFACT
Therehasbeenagrowingconcernamongresearchersabout We briefly introduce the basics of SAS and SHS, and their
the lack of systematic evaluation for SAS and SHS [2–4]. A evaluation in the context of microservices architecture, and
recent systematic mapping study found that only a small per- highlight how CHESS complements the existing artifacts for
centage of studies in this field focus on evaluating previously engineering self-adaptive systems.
developed applications [3]. In addition, there are limited tools
available to support evaluations based on runtime measures, A. Self-Adaptive System for Microservices Architecture
with most studies focusing on evaluating the models used Self-adaptivesoftwaresystemsareaclassofsoftwaresystems
to design the system [4]. These models, however, may not that can adapt to changes in their environment [7]. At a high
take into account all potential scenarios that a system may level, these systems can be seen as comprising a managed
encounter during operation. While runtime models offer a system that is controlled by a managing system, generally
solution to these limitations, they also come with their own realized through a MAPE-K feedback loop [8].
challenges, such as maintenance and the need for model Self-adaptive systems for microservices architecture can
creation[5].Hence,thereisaneedformechanismstoevaluate bring multiple benefits, such as increased scalability, im-
SAS and SHS based on runtime measures that consider proved reliability, and reduced maintenance costs. Studies
potential scenarios a system may encounter during operation. have suggested that there is an overall improvement in
To fill this gap, our earlier work proposed CHESS, an
approach for the systematic evaluation of self-adaptive and 1 CHESSartifactonZenodo:https://doi.org/10.5281/zenodo.6817763
Work licensed under Creative Commons Attribution 4.0 License. https://
creativecommons.org/licenses/by/4.0/ 195
DOI 10.1109/SEAMS59076.2023.00033
33000.3202.67095SMAES/9011.01
:IOD
|
EEEI
3202©
00.13$/32/1-2911-3053-8-979
|
)SMAES(
smetsyS
gniganaM-fleS
dna
evitpadA
rof
gnireenignE
erawtfoS
no
muisopmyS
ht81
MCA/EEEI
3202

the management of microservices-based applications, allo- anoverviewofre-usableartifactsproducedbyresearchersand
cation of microservices among the available servers, qual- engineers in the self-healing and self-adaptive community.
ity attributes such as performance, scalability, and resilience Various existing artifacts focus on web-based systems, mi-
throughtheintroductionofself-healing,self-management,and croservices architecture, or cloud environments that assist in
self-optimization properties [9]. Furthermore, an architecture- the evaluation of the managed systems. Znn.com [18] is a
based self-adaptation framework with a MAPE-K feedback web-basedinformationsystemthatmimicsreal-worldsystems
loopforamicroserviceasamanagedsystemshowsareduced and provides an experimental environment to facilitate the
cost of ownership and faster self-adaptation [10]. On the evaluation. The exemplar applies a self-adaptive framework,
other hand, the introduction of microservices architecture, as Rainbow and presented an evaluation of the self-adaptive
a managing system, can improve the self-adaptation capabil- system based on a benchmark. Hogna [19] is a platform for
ities of systems for various measures such as run-time data deploying self-managing web applications on the cloud. It
analysis [11]. Some challenges in developing a self-adaptive automates operations, monitors the health of the applications,
systembasedonmicroservicesincludedevelopingmonitoring extracts metrics, and analyzes performance data based on a
and adaptation mechanisms for ensuring quality attributes; model to create and execute an action plan. K8-Scalar [20]
determining the level of distribution, observability, and gran- is an exemplar that allows the evaluation of different self-
ularity for deploying control components; and determining adaptive approaches to autoscaling container-orchestrated ser-
mechanismsforevaluationofthegivenqualityattributes[12]. vices. It is based on Docker, and Kubernetes, and extends
a generic testbed for scalability evaluation of large-scale
B. Evaluation of SAS and SHS based on Chaos Engineering
systemscalledScalar.SEAByTE[21]enhancestheautomation
The evaluation of self-adaptive and self-healing systems is
of continuous A/B testing of a microservice-based system.
an important aspect of their design and deployment. In our
Furthermore, exemplars such as SWIM [22], DARTSim [23],
previous work [6], we defined the evaluation of self-adaptive
and RDMSim [24] consist of managed systems which can
and self-healing systems as "an approach to determine if a
assist in the evaluation of external adaptation managers.
system meets objectives under operation, identify areas in
The present artifact represents a departure from existing ar-
whichthesystemperformsaswellasdesiredorpredicted,and
tifacts in the field, as it prioritizes the evaluation of managing
provideevidencetothevalueandapplicabilityofthesystem."
systems by inducing faults within the managed system. Thus,
Several approaches to the evaluation of SAS and SHS
as opposed to primarily focusing on the creation of new self-
include model-based evaluation [13], metric-based evalua-
adaptive approaches, it supports one of the critical tasks of
tion [14], model checking [15], and runtime testing and veri-
software engineering research, i.e., the systematic evaluation
fication [16] each with its benefits and limitations. However,
of novel approaches. This aligns with the growing desire
none of these evaluation approaches are viable for evaluation
to produce artifacts in self-adaptation that support industry-
covering the execution of the system under real-life failure
relevant research [25].
scenarios. Therefore, to address this gap, we introduce a
mechanismthatbuildsonchaosengineeringprinciples.Chaos III. CHESS
engineering (CE) is the practice of intentionally causing and
ThissectionpresentstheCHESSarchitecture,thedemoappli-
studyingcontrolledchaoswithinsoftwaresystemsoperatingin
cations used for testing, and the scenarios for fault injection.
realisticenvironments,withthegoalofincreasingthesystems’
resilienceandabilitytohandleunforeseencircumstances[17]. A. Design and Architecture
ThecoretenetsofCEcanbeoutlinedasfourmainprinciples,
Figure 1 presents a detailed architecture for the CHESS
which include formulating hypotheses based on the steady-
approach. It consists of four main modules: containerized
state behavior of systems, introducing variations to real-world
deployment cluster (CDC), system monitor, system manager,
events, conducting experiments in a production environment,
and fault injection. These modules are presented below.
and automating these experiments for continuous execution.
Containerized Deployment Cluster (CDC): This artifact
Our approach evaluates the systems through a systematic
discusses the process of introducing faults into microservice-
processthatinvolvesexposingthesystemtofaultsandtesting
based applications deployed in a containerized environment
its ability to recover from such perturbations.
using Kubernetes (K8s). The environment details are shown
C. Positioning of the Artifact in Table I. The K8s cluster starts with a total of 20 GB
memory and 4 CPUs to ensure that it has sufficient resources
Artifacts play a vital role in advancing the field of self-
to run the demo applications. To make the demo applications
adaptation. They serve as tangible examples of the algo-
accessible from outside the cluster, we have configured the
rithms and techniques developed by researchers, allowing for
K8s cluster with MetalLB, which is an addon that enables
their evaluation and assessment. In addition, artifacts provide
external IP services in K8s. In addition, the Istio service
problematic scenarios and solutions that can inspire further
mesh is installed in the cluster to monitor the microservices
research,aswellasfacilitatethecomparisonofresultsamong
traffic flow and to provide an easy way to manage the traffic
different studies. The self-adaptive exemplars website2 gives
between microservices. In order to visualize the data traffic
2 http://self-adaptive.org/exemplars/ and services’ status, we have installed Grafana, Kiali, and
196

TABLEII
|     | Microservices  |         | Microservices  |        |     |     | CHAOSEXPERIMENTTEMPLATE |     |     |     |     |     |
| --- | -------------- | ------- | -------------- | ------ | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
|     |                | Scripts |                | Images |     |     |                         |     |     |     |     |     |
steady-state-hypothesis:
|     |     |     |     |     |     | type           |     | probe                               |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | providertype   |     | python                              |     |     |     |     |
|     |     |     |     |     |     | providermodule |     | chaosk8s.probes                     |     |     |     |     |
|     |     |     |     |     |     | func           |     | {deployment_available_and_healthy}, |     |     |     |     |
CDC:
{battery_charged},{timely_response}
|     |     |                      |     |     |            | arguments |     | service_name |     |     |     |     |
| --- | --- | -------------------- | --- | --- | ---------- | --------- | --- | ------------ | --- | --- | --- | --- |
|     |     | Service Deployment N |     |     | Service UI |           |     | namespace    |     |     |     |     |
|     |     |                      |     |     |            | tolerance |     | true         |     |     |     |     |
Service Deployment 2
chaos-method:
Service Deployment 1
|     |     |      |         |         |              | type      |     | action                              |     |     |     |     |
| --- | --- | ---- | ------- | ------- | ------------ | --------- | --- | ----------------------------------- | --- | --- | --- | --- |
|     |     | Pod  | …       | Pod     |              |           |     |                                     |     |     |     |     |
|     |     |      |         |         |              | func      |     | {inject_fault},{deprecate_battery}, |     |     |     |     |
|     |     | 1    |         | N       |              |           |     | {inject_delay},{terminate_pods},    |     |     |     |     |
|     |     |      |         | SSERGNI | Data Storage |           |     |                                     |     |     |     |     |
|     |     |      | Service |         |              |           |     | {load_service}                      |     |     |     |     |
|     |     |      |         |         |              | arguments |     | service_name                        |     |     |     |     |
Fault
| Injection |     |     |     |     |     |     |     | namespace |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
MetalLB load balancer
|     |     |     |     |     |     | pause |     | {before,after}inseconds |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----------------------- | --- | --- | --- | --- |
Istio Injection Enabled
|     |     |     |     |     |     | phase of | the services | that | encounter | faults. | In this | artifact, |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ---- | --------- | ------- | ------- | --------- |
Monitoring UI
Monitoring Tools Deployment
Chaos  the system manager adopts a rule-based approach for fault
logs recovery. The recovery process is automated and follows a
|     |     |     |     |     |     | set of predefined | rules,             | which | have    | been configured |        | for the |
| --- | --- | --- | --- | --- | --- | ----------------- | ------------------ | ----- | ------- | --------------- | ------ | ------- |
|     |     |     |     |     |     | selected          | demo applications. |       | The use | of the          | system | manager |
modulealsoenablesustocomparetheimpactoffaults,known
|     |     | System  |     | System  |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Monitor Manager as the blast radius, for different fault injection scenarios, both
withandwithoutthesystemmanager.Thishelpsustoevaluate
Fig.1. ImplementationArchitecturefortheapplicationsdeployment the effectiveness of the system manager in mitigating the
|     |     |     |     |     |     | effects of | faults in the | running | services. |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------- | ------- | --------- | --- | --- | --- |
Prometheus monitoring tools. Grafana is used to visualize the Fault Injection: The fault injection module follows the
datatraffic,whileKialiisusedtovisualizetheservices’status. principles of Chaos Engineering (CE) to induce faults in the
Prometheus is used to query data metrics from its database deployed application services. A set of chaos experiments
and to store the data for later analysis. The combination is carefully designed and scripted, for each fault injection
| of these | tools | provides | a complete | solution | for monitoring |           |             |        |             |        |          |           |
| -------- | ----- | -------- | ---------- | -------- | -------------- | --------- | ----------- | ------ | ----------- | ------ | -------- | --------- |
|          |       |          |            |          |                | scenario, | in order to | inject | the desired | faults | into the | services. |
microservices-based applications and for evaluating the fault A chaos experiment template is shown in Table II. A chaos
tolerance of these applications. experiment first defines the steady state with a probe function
System Monitor: The system monitor module monitors the and a check against a tolerance. Once the steady state is met,
statusoftherunningservicesandperformsnecessarychecksto thechaosactionmethodiscalledtoinjecttherespectivefault,
ensure their validity. Its purpose is to observe the behavior of using the service_name and namespace arguments to identify
the system under various conditions, distinguish the system’s the service. A pause before or after the fault injection can
normal behavior patterns from abnormal ones, and alert the also be added. A virtual environment in Python is prepared
system manager in case of any abnormal behavior. with "chaostoolkit" and "chaostoolkit-Kubernetes" libraries to
|        |          |     |        |         |              | execute | the chaos injection |     | scripts. Each | chaos | injection | gen- |
| ------ | -------- | --- | ------ | ------- | ------------ | ------- | ------------------- | --- | ------------- | ----- | --------- | ---- |
| System | Manager: | The | system | manager | module plays | a       |                     |     |               |       |           |      |
crucial role in ensuring the continuous operation of services erates chaos logs, which can be used for system observation
| deployedintheCDC.Theprimaryresponsibilityofthesystem |     |     |     |     |     | purposes. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
managermoduleistoreceiveabnormalsystembehavioralerts
|          |        |         |        |            |              | B. Demo      | Applications | for   | Testing     |       |          |         |
| -------- | ------ | ------- | ------ | ---------- | ------------ | ------------ | ------------ | ----- | ----------- | ----- | -------- | ------- |
| from the | system | monitor | module | and handle | the recovery |              |              |       |             |       |          |         |
|          |        |         |        |            |              | The artifact | uses the     | smart | office case | study | from our | earlier |
paper[6]andanopensourceexampleapplicationnamedYelb3
TABLEI
|     |     |     |     |     |     | as the demo | applications | for | chaos injection |     | and testing. |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --------------- | --- | ------------ | --- |
K8SCLUSTERDETAILS
|     |     |     |     |     |     | Smart | Office Case | Study: | The | smart office | case | study |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | ------ | --- | ------------ | ---- | ----- |
K8scluster Minikube consists of nine services, including three input services (tem-
Clustermemory 20GB perature sensor, motion sensor, and external weather), two
|     | Clustercpus  |     | 4       |     |     |          |                    |          |                  |           |      |          |
| --- | ------------ | --- | ------- | --- | --- | -------- | ------------------ | -------- | ---------------- | --------- | ---- | -------- |
|     |              |     |         |     |     | control  | services (heating  | control, | light            | control), | two  | actuator |
|     | Loadbalancer |     | MetalLB |     |     |          |                    |          |                  |           |      |          |
|     |              |     |         |     |     | services | (heating actuator, |          | light actuator), | an        | MQTT | broker,  |
|     | Servicemesh  |     | Istio   |     |     |          |                    |          |                  |           |      |          |
MonitoringDB Prometheus and a user interface. The control services retrieve periodic
|     | Monitoringtools |     | Grafana&Kiali           |     |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Chaostools      |     | chaostoolkit-Kubernetes |     |     |     |     |     |     |     |     |     |
3 TheYelbapplicationwasreusedfromhttps://github.com/mreferre/yelb
197

TABLEIII
Pod  . . . Pod  Side Car Proxy Pod  . . . Pod  Side Car Proxy Pod  . . . Pod  Side Car Proxy TESTSCENARIOSFORFAULTINJECTION
| 1                | N                                                  |                | 1                                                         | N               | 1               | N                  |                |                |          |                           |       |             |                   |         |
| ---------------- | -------------------------------------------------- | -------------- | --------------------------------------------------------- | --------------- | --------------- | ------------------ | -------------- | -------------- | -------- | ------------------------- | ----- | ----------- | ----------------- | ------- |
|                  |                                                    |                |                                                           |                 |                 |                    |                | FaultInjection |          | FaultLevel                |       |             | TargetApplication |         |
| TTT eee mmmSSS   | pppeee ---rrr SSSvvv eeeccc nnneee sss ooo rrr     |                | MMM ooo tttSSS iii oooeee nnnrrr ---vvv SSSiii eeeeee nnn | sss ooo rrr     | E               | x t e r n a l -    |                |                |          |                           |       |             |                   |         |
|                  | iii                                                |                | ccc                                                       |                 |                 |                    |                |                |          |                           |       |             |                   |         |
|                  |                                                    |                |                                                           |                 | Wea t           | h e r   S e r vice |                | SensorDown     |          | Infrastructure&Functional |       |             | Smart-Office      |         |
|                  |                                                    |                |                                                           |                 |                 |                    |                | SensorFaulty   |          | Infrastructure&Functional |       |             | Smart-Office      |         |
|                  |                                                    |                |                                                           |                 |                 |                    |                | ServiceDelayed |          | Infrastructure            |       |             | Smart-Office      |         |
|                  |                                                    |                |                                                           |                 |                 |                    |                | ServiceDown    |          | Infrastructure            |       |             | Smart-Office      |         |
|                  |                                                    |                |                                                           |                 |                 |                    |                | HighSRR        |          | Infrastructure            |       |             | Yelb-App          |         |
|                  | Pod                                                |                | Pod                                                       | Pod             | Pod             | Pod                |                |                |          |                           |       |             |                   |         |
| Pod              | . . .                                              | Side Car Proxy | . . .                                                     | Side Car Proxy  |                 | . . .              | Side Car Proxy |                |          |                           |       |             |                   |         |
| 1                | N                                                  |                | 1                                                         | N               | 1               | N                  |                |                |          |                           |       |             |                   |         |
|                  |                                                    |                |                                                           |                 |                 |                    |                | end logic      | and data | flow.                     | Chaos | Engineering | provides          | support |
| Heating-Control  |                                                    |                | MQTT-Broker                                               |                 | User-Interface  |                    |                |                |          |                           |       |             |                   |         |
Service for functional level faults, which can be injected by writing
|     |     |     | Service |     |     | Service |     |               |          |        |            |           |            |              |
| --- | --- | --- | ------- | --- | --- | ------- | --- | ------------- | -------- | ------ | ---------- | --------- | ---------- | ------------ |
|     |     |     |         |     |     |         |     | custom probes | and      | action | methods    | for       | a specific | scenario and |
|     |     |     |         |     |     |         |     | calling them  | in a     | chaos  | experiment | script.   |            |              |
|     |     |     |         |     |     |         |     | The artifact  | presents |        | 5 fault    | injection | scenarios, | 4 using the  |
Pod  . . . Pod  Side Car Proxy Pod  . . . Pod  Side Car Proxy Pod  . . . Pod  Side Car Proxy smart office case study and 1 using the Yelb app.
| 1   | N   |     | 1                                          | N      | 1   | N   |     |       |            |        |     |                    |     |     |
| --- | --- | --- | ------------------------------------------ | ------ | --- | --- | --- | ----- | ---------- | ------ | --- | ------------------ | --- | --- |
|     |     |     |                                            |        |     |     |     | FS-1: | a deployed | sensor | is  | down unexpectedly. |     |     |
|     |     |     | HHHAAASSS eee aaa tttaaa iii nnn gggoooeee | ---rrr |     |     |     |       |            |        |     |                    |     |     |
ccc ttt uuuvvv ttt     LLL iii ggg hhhSSS ttteee --- AAArrr ccciii ttt uuueee aaa ttt ooo rrr     F S - 2 : a d e p lo ye d se n s o r s e n d s er ro n eo u s readings.
| Lig ht | - C o n trol  |                                        |                 |     |     | vvv ccc |     |           |             |             |             |           |            |              |
| ------ | ------------- | -------------------------------------- | --------------- | --- | --- | ------- | --- | --------- | ----------- | ----------- | ----------- | --------- | ---------- | ------------ |
| S      | e r vi c e    |                                        | eee rrr iii ccc |     |     |         |     |           |             |             |             |           |            |              |
|        |               |                                        |                 |     |     |         |     | F S - 3 : | a ru n n in | g se rv     | i c e i s d | o w n a b | ru p tl y. |              |
|        |               |                                        |                 |     |     |         |     | FS-4:     | a running   | service     | is delayed. |           |            |              |
|        |               |                                        |                 |     |     |         |     | FS-5:     | a running   | service     | is          | loaded    | with a     | high service |
|        | Fig.2.        | ServicegraphfortheSmartOfficecasestudy |                 |     |     |         |     |           |             |             |             |           |            |              |
|        |               |                                        |                 |     |     |         |     |           | request     | rate (SRR). |             |           |            |              |
sensingdataandweatherdata,thenuserulestocontrolheating Table III presents an overview of faults injected with respect
and lighting actuators. The service graph for the smart office to the fault level and the target application. The infrastructure
case study is shown in Figure 2. level fault injection is executed on the system service in a
Yelb Application: The Yelb application consists of four black-box manner. The infrastructure & functional level fault
|           |        |           |          |     |                |     |        | execution | is performed |     | in a | grey-box | manner | where some |
| --------- | ------ | --------- | -------- | --- | -------------- | --- | ------ | --------- | ------------ | --- | ---- | -------- | ------ | ---------- |
| services: | a user | interface | service, |     | an application |     | server |           |              |     |      |          |        |            |
(appserver) service, a redis server service, and a database additional access to the service’s functional status is required.
| service. | It allows | users | to vote | for their | preferred | restaurant |     |     |     |     |     |     |     |     |
| -------- | --------- | ----- | ------- | --------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
among given options, and updates a pie chart based on the IV. EXPERIMENTS
| number | of votes | received | for each | option. | The | Istio | view of |              |              |     |      |                  |     |               |
| ------ | -------- | -------- | -------- | ------- | --- | ----- | ------- | ------------ | ------------ | --- | ---- | ---------------- | --- | ------------- |
|        |          |          |          |         |     |       |         | The artifact | is available |     | in a | virtual machine. |     | The directory |
theservicegraphfortheYelbapplicationisshowninFigure3.
|                   |              |        |                     |     |        |                |        | structure | for artifact | implementation |     | is  | shown in | Figure 4. |
| ----------------- | ------------ | ------ | ------------------- | --- | ------ | -------------- | ------ | --------- | ------------ | -------------- | --- | --- | -------- | --------- |
| C. Test           | Scenarios    | for    | Fault Injection     |     |        |                |        |           |              |                |     |     |          |           |
| Chaos Engineering |              | allows | the injection       |     | of two | types of       | faults |           |              |                |     |     |          |           |
| in a running      | application: |        | infrastructure      |     | level  | and functional |        |           |              |                |     |     |          |           |
| level. In         | the context  | of     | microservices-based |     |        | applications   | de-    |           |              |                |     |     |          |           |
ployedinaCDCcluster,theinfrastructurelevelfaultsinclude
| the faults     | that            | occur due    | to issues  | with   | CDC               | configurations |           |     |     |     |     |     |     |     |
| -------------- | --------------- | ------------ | ---------- | ------ | ----------------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| and resources. |                 | These        | faults can | be     | mostly            | injected       | using     |     |     |     |     |     |     |     |
| predefined     | functions       | available    |            | within | various           | chaos          | toolkits. |     |     |     |     |     |     |     |
| The functional |                 | level faults | are        | unique | to the            | application    | and       |     |     |     |     |     |     |     |
| require        | some additional |              | knowledge  | of     | the application’s |                | back-     |     |     |     |     |     |     |     |
UUsseerr
Fig.3. IstioviewoftheservicegraphfortheYelbcasestudy Fig.4. Artifact’sdirectories’hierarchy
198

|                           |     |                                | TABLEIV             |     |     |     |     |     |                                |                     | TABLEV             |     |     |     |     |
| ------------------------- | --- | ------------------------------ | ------------------- | --- | --- | --- | --- | --- | ------------------------------ | ------------------- | ------------------ | --- | --- | --- | --- |
|                           |     | RUNSMART-OFFICESCENARIOS       |                     |     |     |     |     |     |                                | RUNYELB-APPSCENARIO |                    |     |     |     |     |
| Step1:StartK8sCluster     |     |                                |                     |     |     |     |     |     | Step1:StartK8sCluster          |                     |                    |     |     |     |     |
|                           |     | python3                        | cluster.py          |     |     |     |     |     |                                | python3             | cluster.py         |     |     |     |     |
| Step2:RunDemo-AppScenario |     |                                |                     |     |     |     |     |     | Step2:RunDemo-AppScenario      |                     |                    |     |     |     |     |
|                           |     | python3                        | system_monitor.pyX  |     |     | Y   |     |     |                                | python3             | system_monitor.pyX |     |     |     | 0   |
| Step3:RunChaosVirtualEnv  |     |                                |                     |     |     |     |     |     | Step3:Runpodslogger            |                     |                    |     |     |     |     |
|                           |     | ~/.venvs/chaosEnv/bin/activate |                     |     |     |     |     |     |                                | ./numpods.sh        |                    |     |     |     |     |
| Step4:RunChaosScript      |     |                                |                     |     |     |     |     |     | Step4:Startoverloadingyelb-app |                     |                    |     |     |     |     |
|                           |     | chaos                          | run scenario-X.yaml |     |     |     |     |     |                                | python3             | fastvote.py<url>   |     |     |     |     |
Step5:Kialivisualization[Optional] Step5:Kialivisualization[Optional]
|     |     | istioctl | dashboard |     | kiali |     |     |     |     | istioctl |     | dashboard | kiali |     |     |
| --- | --- | -------- | --------- | --- | ----- | --- | --- | --- | --- | -------- | --- | --------- | ----- | --- | --- |
Step6:Grafanavisualization[Optional] Step6:Grafanavisualization[Optional]
|     |     | istioctl | dashboard |     | grafana |     |     |     |     | istioctl |     | dashboard | grafana |     |     |
| --- | --- | -------- | --------- | --- | ------- | --- | --- | --- | --- | -------- | --- | --------- | ------- | --- | --- |
A. How to use the artifact: Smart-Office Scenarios command:kubectlautoscaledeploymentyelb-appserver–cpu-
|           |      |             |       |      |              |     |           | percent=10 | –min=1 | –max=20.  |     | The       | parameters | cpu-percent, |     |
| --------- | ---- | ----------- | ----- | ---- | ------------ | --- | --------- | ---------- | ------ | --------- | --- | --------- | ---------- | ------------ | --- |
| There are | four | main steps, | along | with | two optional |     | steps for |            |        |           |     |           |            |              |     |
|           |      |             |       |      |              |     |           | min, and   | max    | represent | the | dedicated | CPU        | percentage,  | the |
onlinedatavisualization,toruntheartifactforthesmart-office
minimumnumberofreplicastoberunning,andthemaximum
| scenarios | (refer | to Table | IV). |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
numberofreplicasthatcanrununderheavyload,respectively.
ThefirststepistocreateorstarttheK8sclusterbyrunning
|                                               |             |               |      |                      |         |                |          | These values    | can    | be adjusted  |             | based       | on the    | available   | resources   |
| --------------------------------------------- | ----------- | ------------- | ---- | -------------------- | ------- | -------------- | -------- | --------------- | ------ | ------------ | ----------- | ----------- | --------- | ----------- | ----------- |
| the script                                    | cluster.py. | This          | will | create               | a new   | minikube-based |          |                 |        |              |             |             |           |             |             |
|                                               |             |               |      |                      |         |                |          | in the cluster. |        | In the third | step,       | the         | pods’     | logger      | is executed |
| K8sclusterwith4CPUsand2000MBofmemory.Thenewly |             |               |      |                      |         |                |          |                 |        |              |             | numpods.sh. |           |             |             |
|                                               |             |               |      |                      |         |                |          | by running      | the    | shell        | script      |             |           | This script | records     |
| created cluster                               | will        | be configured |      | with                 | metalLB | load           | balancer |                 |        |              |             |             |           |             |             |
|                                               |             |               |      |                      |         |                |          | changes         | in the | number       | of replicas |             | over time | and         | writes the  |
| and have                                      | istio mesh  | installed,    |      | with istio-injection |         | enabled        | and      |                 |        |              |             |             |           |             |             |
resultstoalogfile,whichcanlaterbeanalyzedtounderstand
| monitoring    | tools    | installed. | Next,       | you | can deploy |            | the demo |                  |     |            |     |        |           |             |         |
| ------------- | -------- | ---------- | ----------- | --- | ---------- | ---------- | -------- | ---------------- | --- | ---------- | --- | ------ | --------- | ----------- | ------- |
|               |          |            |             |     |            |            |          | the relationship |     | between    | the | number | of active | users       | and the |
| application’s | services | for        | a specified |     | scenario   | by running | the      |                  |     |            |     |        |           |             |         |
|               |          |            |             |     |            |            |          | usage of         | CPU | resources, | and | the    | increase  | or decrease | in      |
script system_monitor.py X Y. The value for X represents the replicas. The fourth step is to run the scripted chaos for the
| scenario    | number              | and can      | be 1,   | 2, 3,        | or 4 to | run FS-1,   | FS-2,     |              |      |                     |            |             |                |               |            |
| ----------- | ------------------- | ------------ | ------- | ------------ | ------- | ----------- | --------- | ------------ | ---- | ------------------- | ---------- | ----------- | -------------- | ------------- | ---------- |
|             |                     |              |         |              |         |             |           | fast voting  | onto | the yelb-appserver. |            |             | Finally,       | for real-time | data       |
| FS-3, or    | FS-4, respectively. |              | The     | value        | for Y   | is either   | 0 if you  |              |      |                     |            |             |                |               |            |
|             |                     |              |         |              |         |             |           | observation, | the  | Kiali               | dashboard  | and         | Grafana        | dashboard     | can        |
| want to run | the                 | system       | monitor | alone,       | or 1 if | you want    | to run    |              |      |                     |            |             |                |               |            |
|             |                     |              |         |              |         |             |           | be launched  | in   | separate            | terminals, | as          | an optional    | step.         |            |
| the system  | monitor             | with         | the     | system       | manager | to recover  | the       |              |      |                     |            |             |                |               |            |
| services    | from failures.      |              | To view | the running  |         | deployments | and       | C. Results   |      |                     |            |             |                |               |            |
| services    | in the              | k8s cluster, | run     | the command: |         | kubectl     | get all.  |              |      |                     |            |             |                |               |            |
|             |                     |              |         |              |         |             |           | Smart-Office |      | Scenarios:          | The        | first       | four scenarios |               | (FS1, FS2, |
| Step three  | involves            | activating   |         | the virtual  | chaos   | environment |           |              |      |                     |            |             |                |               |            |
|             |                     |              |         |              |         |             |           | FS3, and     | FS4) | are designed        |            | to evaluate |                | the effect    | of chaos   |
| for chaos   | injection.          | Then,        | run     | the chaos    | command |             | chaos run |              |      |                     |            |             |                |               |            |
|             |                     |              |         |              |         |             |           | injection    | and  | failures            | on a       | running     | system,        | both          | with and   |
scenario-X.ymltoinjectafailurecorrespondingtotherunning
withoutthedeploymentofasystemmanagementservice.They
| scenario. | Where, | scenario-X | represents |     | the chaos | experiment |     |         |              |     |        |          |          |      |          |
| --------- | ------ | ---------- | ---------- | --- | --------- | ---------- | --- | ------- | ------------ | --- | ------ | -------- | -------- | ---- | -------- |
|           |        |            |            |     |           |            |     | provide | a comparison |     | of the | system’s | behavior | when | it fails |
tobeinjected,andXcanbe1,2,3,or4forFS-1,FS-2,FS-3,
|          |               |          |     |         |            |            |     | to recover | from        | an injected |          | fault and | when | it successfully |       |
| -------- | ------------- | -------- | --- | ------- | ---------- | ---------- | --- | ---------- | ----------- | ----------- | -------- | --------- | ---- | --------------- | ----- |
| or FS-4, | respectively. | Finally, |     | you can | use online | monitoring |     |            |             |             |          |           |      |                 |       |
|          |               |          |     |         |            |            |     | recovers   | to evaluate | the         | system’s | behavior  |      | and recovery    | capa- |
toolstoexaminetheonlinemonitoringdataforservicestatuses
|             |       |             |     |       |           |     |         | bilities. | Figure | 5 depicts | the | system | monitor | output | for FS-1 |
| ----------- | ----- | ----------- | --- | ----- | --------- | --- | ------- | --------- | ------ | --------- | --- | ------ | ------- | ------ | -------- |
| and traffic | flow. | If desired, | the | Kiali | dashboard | and | Grafana |           |        |           |     |        |         |        |          |
whenrunwithoutamanagementservice(i.e.,runningpython3
| dashboard   | can    | be launched   | in       | separate | terminals |     | to observe |                |                 |          |          |           |             |         |              |
| ----------- | ------ | ------------- | -------- | -------- | --------- | --- | ---------- | -------------- | --------------- | -------- | -------- | --------- | ----------- | ------- | ------------ |
|             |        |               |          |          |           |     |            | system_monitor |                 | 1 0). In | this     | scenario, | an injected |         | fault in the |
| the service | data   | metrics.      |          |          |           |     |            |                |                 |          |          |           |             |         |              |
|             |        |               |          |          |           |     |            | form of        | data corruption |          | leads    | to a      | cascading   | failure | that the     |
|             |        |               |          |          |           |     |            | system         | is unable       | to       | recover. | On the    | other       | hand,   | Figure 6     |
| B. How      | to use | the artifact: | Yelb-App |          | Scenario  |     |            |                |                 |          |          |           |             |         |              |
|             |        |               |          |          |           |     |            | shows the      | system          | monitor  |          | output    | for FS-1    | when    | run with     |
The execution process for the Yelb application scenario in- a management service (i.e., running python3 system_monitor
volves four main steps, with two additional optional steps for 1 1). In this case, the system manager is able to quickly
online data visualization, as described in Table V. identify and recover from the failed service, resulting in a
|     |     |     |     |     |     |     |     | much smoother |     | and more | efficient | recovery |     | process. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --------- | -------- | --- | -------- | --- |
ThefirststepistocreatetheK8scluster,followedbythede-
ploymentofdemoapplicationservices.Theapp-serverservice Yelb-App Scenario: TheFS5evaluatesthescalabilityofser-
canbeenabledforauto-scalingusingthehorizontalpodauto- vices deployed in a Kubernetes cluster by imposing different
scaling (HPA) functionality of K8s by running the following loads on the service. The resulting log file captures two types
199

| Fig.5. | Runningscenario1withoutsystemmanagerservice |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.9. Dataextractedfromnumpodslogfile
Fig.6. Runningscenario1withsystemmanagerservice servicesindetectingandmitigatingfailuresinthesystem.The
artifactconsistsof(i)predefinedfunctionalandinfrastructural
of data: information about all running pods (obtained through level fault injection scenarios, (ii) a self-monitoring service
kubectl get pods) that presents extensive logs for the deployed services’ normal
|     |     | and | data on | HPA | deployment | (obtained |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
throughkubectlgethpa).Thelogisupdatedevery30seconds andabnormalbehaviors,(iii)themanagingsystemservicethat
and records the name, status, number of restarts, and age of reacts to the system abnormal behavior traces and brings the
each running pod (as shown in Figure 7), and the name, CPU system back to the stable condition, and (iv) a comparison
targets, minimum and maximum number of pods, number of the service failure and cascading effects with and without
of replicas, and age of the HPA deployment (as shown in deployment of the managing system service. The artifact is
|     |     |     |     |     |     |     |     | Zenodo,1 |     |     |     |     | YouTube.4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --------- | --- |
Figure 8). This log can be analyzed to uncover patterns in available on and a demo video is on
the service’s performance and resource utilization over time. Applicability: The artifact provides the SEAMS commu-
For example, Figure 9 presents sample data extracted from nity with support for one of the critical tasks of software
observing generated log files. The extracted data depicts a engineering research, i.e., the systematic evaluation of novel
dramatic increase in CPU usage and the number of replicas approaches. It aligns with the growing desire to produce self-
over a 22-minute period. adaptationartifactsthatsupportindustry-relevantresearch[25]
|     |     |     |     |     |     |     | by using | chaos | engineering |     | to systematically |     | observe | con- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----------- | --- | ----------------- | --- | ------- | ---- |
V. CONCLUDINGREMARKS tainerized applications in Docker [26]. Artifact components
|                |          |            |           |     |          |               | are reusable, | extendable, |           | and | modifiable  | for new | case     | studies. |
| -------------- | -------- | ---------- | --------- | --- | -------- | ------------- | ------------- | ----------- | --------- | --- | ----------- | ------- | -------- | -------- |
| Contributions: |          | This paper | presents  | an  | artifact | that provides |               |             |           |     |             |         |          |          |
|                |          |            |           |     |          |               | Existing      | fault       | scenarios | can | be combined | and     | expanded | to       |
| a detailed     | overview | of how     | the CHESS |     | approach | can be used   |               |             |           |     |             |         |          |          |
to evaluate a system’s resilience and ability to recover from create complex ones. The custom fault injection scripts can
inspireexplorationofgrey-boxlevelfaultinjectionandtesting.
varioustypesoffaults.Theimplementedmoduleshighlightthe
|               |     |            |                       |     |            |          | Futurework:      |                 | Directionsofinterestincludeexploringtheuse |            |               |              |              |         |
| ------------- | --- | ---------- | --------------------- | --- | ---------- | -------- | ---------------- | --------------- | ------------------------------------------ | ---------- | ------------- | ------------ | ------------ | ------- |
| effectiveness | of  | the system | monitoring            |     | and system | managing |                  |                 |                                            |            |               |              |              |         |
|               |     |            |                       |     |            |          | of observability |                 | data and                                   | system     | logs          | for chaos    | engineering- |         |
|               |     |            |                       |     |            |          | controlled       | data            | synthesis.                                 | In         | addition,     | techniques   |              | for the |
|               |     |            |                       |     |            |          | automated        | selection       | of                                         | regions    | for chaos     | experiments  |              | based   |
|               |     |            |                       |     |            |          | on the health    | and             | performance                                |            | status        | of services  | are          | also of |
|               |     |            |                       |     |            |          | interest.        | Finally,        | the inclusion                              |            | of contextual | information, |              | such    |
|               |     |            |                       |     |            |          | as ontologies    | or              | knowledge                                  | graphs,    | can           | also be      | considered   | to      |
|               |     |            |                       |     |            |          | enhance          | fault injection |                                            | targeting. |               |              |              |         |
|               |     |            |                       |     |            |          | Acknowledgments: |                 |                                            | This       | research      | is supported |              | by the  |
|               |     |            |                       |     |            |          | Research         | Council         | of                                         | Norway     | through       | the          | cureIT       | project |
|               |     | Fig.7.     | Podsdataviewinlogfile |     |            |          |                  |                 |                                            |            |               |              |              |         |
|               |     |            |                       |     |            |          | (#300461)        | and             | used resources                             |            | provided      | by the       | Experimental |         |
|               |     |            |                       |     |            |          | Infrastructure   | for             | Exploration                                |            | of Exascale   | Computing    |              | (eX3),  |
|               |     |            |                       |     |            |          | supported        | by the          | Research                                   | Council    | of            | Norway       | (#270053).   |         |
Fig.8. HPAdataviewinlogfile 4 Artifactdemovideo:https://youtu.be/CBcaPJgpi-o
200

REFERENCES [14] J. Porter, D. A. Menascé, H. Gomaa, and E. Albassam.
“TESS: Automated Performance Evaluation of Self-Healing
[1] T.Wong,M.Wagner,andC.Treude.“Self-adaptivesystems:A
and Self-Adaptive Distributed Software Systems.” In: Int’l
systematicliteraturereviewacrosscategoriesanddomains.”In:
Information and Software Technology (IST) 148 (Aug. 2022),
Conf.PerformanceEngineering.ACM,Mar.2018,pp.40–47.
p. 106934. ISSN: 0950-5849. DOI: 10/gp6krm.
ISBN: 978-1-4503-5095-2. DOI: 10/gkgf2n.
[15] J.CámaraandR.deLemos.“Evaluationofresilienceinself-
[2] I. Gerostathopoulos, T. Vogel, D. Weyns, and P. Lago. “How
adaptivesystemsusingprobabilisticmodel-checking.”In:Int’l
doweEvaluateSelf-adaptiveSoftwareSystems?:ATen-Year
Symp. Software Engineering for Adaptive and Self-Managing
PerspectiveofSEAMS.”In:Int’lSymp.SoftwareEngineering
forAdaptiveandSelf-ManagingSystems(SEAMS).IEEE,May Systems (SEAMS). June 2012, pp. 53–62. DOI: 10/gp6kr9.
[16] T. M. King, A. A. Allen, Y. Wu, P. J. Clarke, and A. E.
2021, pp. 59–70. ISBN: 978-1-66540-289-7. DOI: 10/gmvfd2.
Ramirez. “A Comparative Case Study on the Engineering of
[3] W.F.Passini,C.A.Lana,V.Pfeifer,andF.J.Affonso.“Design
Self-Testable Autonomic Software.” In: Int’l Conf. and Ws.
of frameworks for self-adaptive service-oriented applications:
Asystematicanalysis.”In:Software:PracticeandExperience
Engineering of Autonomic and Autonomous Systems (EASE).
(SP&E) 52.1 (2022), pp. 5–38. ISSN: 1097-024X. DOI: 10/ Apr. 2011, pp. 59–68. DOI: 10/c75gr5.
[17] A. Basiri, A. Blohowiak, L. Hochstein, and C. Rosenthal. “A
gpd4x4.
Platform for Automating Chaos Experiments.” In: Int’l Symp.
[4] A. O. de Sousa, C. I. M. Bezerra, R. M. C. Andrade, and
Software Reliability Engineering Workshops (ISSREW). Oct.
J. M. S. M. Filho. “Quality Evaluation of Self-Adaptive
Systems: Challenges and Opportunities.” In: Brazilian Symp. 2016, pp. 5–8. DOI: 10/gkf957.
Software Engineering. ACM, Sept. 2019, pp. 213–218. ISBN: [18] S.-W. Cheng, D. Garlan, and B. Schmerl. “Evaluating the
effectiveness of the Rainbow self-adaptive system.” In: ICSE
978-1-4503-7651-8. DOI: 10/gpd4xj.
Ws. Software Engineering for Adaptive and Self-Managing
[5] S. Ghahremani and H. Giese. “Evaluation of Self-Healing
Systems: An Analysis of the State-of-the-Art and Required
Systems(SEAMS).May2009,pp.132–141. DOI:10/dm9jmh.
Improvements.” In: Computers 9.1 (Mar. 2020), p. 16. DOI: [19] C. Barna, H. Ghanbari, M. Litoiu, and M. Shtern. “Hogna:
A Platform for Self-Adaptive Applications in Cloud Environ-
10/gkgf26.
ments.”In:Int’lSymp.SoftwareEngineeringforAdaptiveand
[6] M.A.Naqvi,S.Malik,M.Astekin,andL.Moonen.“OnEval-
uating Self-Adaptive and Self-Healing Systems using Chaos
Self-ManagingSystems(SEAMS).May2015,pp.83–87. DOI:
Engineering.”In:IEEEInt’lConf.AutonomicComputingand 10/gk5ntg.
Self-OrganizingSystems(ACSOS).Sept.2022,pp.1–10. DOI: [20] W.Delnat,T.Heyman,W.Joosen,D.Preuveneers,A.Rafique,
E. Truyen, and D. V. Landuyt. “K8-Scalar: a workbench to
10/grdjz4.
[7] D.Weyns.Anintroductiontoself-adaptivesystems:acontem- compare autoscalers for container-orchestrated services (Arti-
porary software engineering perspective. Wiley, 2021. ISBN:
fact).”In:DagstuhlArtifactsSeries4.1(2018),2:1–2:6.ISSN:
978-1-119-57494-1.
2509-8195. DOI: 10/gk5ns7.
[21] F. Quin and D. Weyns. SEAByTE: A Self-adaptive Micro-
[8] J. Kephart and D. Chess. “The vision of autonomic comput-
ing.” In: Computer 36.1 (Jan. 2003), pp. 41–50. ISSN: 0018-
serviceSystemArtifactforAutomatingA/BTesting.Apr.2022.
[22] G. A. Moreno, B. Schmerl, and D. Garlan. “SWIM: An
9162. DOI: 10/c3t3bc.
Exemplar for Evaluation and Comparison of Self-Adaptation
[9] M. Filho, E. Pimentel, W. Pereira, P. H. M. Maia, and
Approaches for Web Applications.” In: Int’l Symp. Soft-
M. I. Cortes. “Self-Adaptive Microservice-based Systems -
ware Engineering for Adaptive and Self-Managing Systems
Landscape and Research Opportunities.” In: Int’l Symp. Soft-
ware Engineering for Adaptive and Self-Managing Systems (SEAMS). May 2018, pp. 137–143.
(SEAMS).IEEE,May2021,pp.167–178.ISBN:978-1-66540- [23] G. Moreno, C. Kinneer, A. Pandey, and D. Garlan. “DART-
Sim: An Exemplar for Evaluation and Comparison of Self-
289-7. DOI: 10/gp6kr2.
Adaptation Approaches for Smart Cyber-Physical Systems.”
[10] S.R.BoyapatiandC.Szabo.“Self-adaptationinMicroservice
Architectures: A Case Study.” In: Int’l Conf. Engineering of In: Int’l Symp. Software Engineering for Adaptive and Self-
ComplexComputerSystems(ICECCS).Mar.2022,pp.42–51. Managing Systems (SEAMS). May 2019, pp. 181–187. DOI:
10/gkgfxr.
DOI: 10/gq35n3.
[24] H. Samin, L. H. G. Paucar, N. Bencomo, C. M. C. Hurtado,
[11] A.Banijamali,P.Kuvaja,M.Oivo,andP.Jamshidi.“Kuksa*:
andE.M.Fredericks.“RDMSim:AnExemplarforEvaluation
Self-adaptive Microservices in Automotive Systems.” In:
Product-Focused Software Process Improvement. Ed. by M. and Comparison of Decision-Making Techniques for Self-
Adaptation.”In:Int’lSymp.SoftwareEngineeringforAdaptive
Morisio, M. Torchiano, and A. Jedlitschka. Springer Interna-
and Self-Managing Systems (SEAMS). May 2021, pp. 238–
tionalPublishing,2020,pp.367–384.ISBN:978-3-030-64148-
1. DOI: 10/gjpm6d.
244. DOI: 10/grqbj6.
[25] D.Weynsetal.“GuidelinesforArtifactstoSupportIndustry-
[12] N. C. Mendonca, P. Jamshidi, D. Garlan, and C. Pahl. “De-
Relevant Research on Self-Adaptation.” In: ACM SIGSOFT
velopingSelf-AdaptiveMicroserviceSystems:Challengesand
Directions.” In: IEEE Software 38.2 (Mar. 2021), pp. 70–79. Software Engineering Notes 47.4 (Sept. 2022), pp. 18–24.
ISSN: 0740-7459, 1937-4194. DOI: 10/gp6ksx.
ISSN: 0163-5948. DOI: 10/grnqx9.
[26] J.Simonsson,L.Zhang,B.Morin,B.Baudry,andM.Monper-
[13] D. M. Barbosa, R. G. d. M. Lima, P. H. M. Maia, and E. C.
rus.“Observabilityandchaosengineeringonsystemcallsfor
Junior.“Lotus@Runtime:AToolforRuntimeMonitoringand
VerificationofSelf-adaptiveSystems(Artifact).”In:Dagstuhl containerized applications in Docker.” In: Future Generation
Artifacts Series 3.1 (2017), 7:1–7:5. ISSN: 2509-8195. DOI:
ComputerSystems122(Sept.2021),pp.117–129.ISSN:0167-
10/gk5ns9.
739X. DOI: 10/gjqvps.
201