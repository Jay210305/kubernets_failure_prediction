IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026 767
MADGuard: A High-Performance Microservice
Anomaly Detection System With Multidimensional
Data Fusion and Temporal Causal Analysis
Yanshang Yin , Tiantian Zhu , Member, IEEE, Tieming Chen , and Mingqi Lv
Abstract—With the widespread adoption of microservice Scaling: The dynamic scaling mechanism causes continuous
architectures, the security threats they face have become changesinserviceinstancetopology,leadingtoanexponential
increasingly sophisticated. Existing anomaly detection methods
increase in the attack surface [6]. (2) Cross-Network
based on system calls exhibit significant limitations in three
Communication: Frequent communication between services
key aspects: multidimensional data fusion, temporal causal-
ity modeling, and forensic analysis of anomalies. This paper renders traditional perimeter defense models ineffective.
proposesMADGuard,aprovenancegraph-basedanomalydetec- Middleware components, such as API gateways and
tion system for microservices. MADGuard addresses these service meshes, become new targets for attacks [6]. (3)
challenges through three key innovations: (1) It constructs a
Containerized Deployment: The use of containerization
nativeprovenancegraphbyintegratingmultisourceservicesand
introduces cloud-native security risks, including image
multidimensionaldata,employingfeaturehashingandpositional
encoding for efficient graph representation; (2) The system vulnerabilities and container escape [7], [8], [9]. Once a
introduces a Temporal Graph Network (TGN) model combined single microservice is compromised, attackers can quickly
withedgereconstructionerrorandInverseDocumentFrequency move laterally to penetrate the entire system, potentially
(IDF) weighting, achieving a 15. 07% improvement in the
causing catastrophic consequences such as data breaches and
F1 score compared to existing methods; (3) For the first time
service interruptions [10]. These security challenges mean
in microservice security, an integrated forensic analysis module
is implemented, allowing rapid anomaly path reconstruction thatanomalydetectionsystemsinmicroservicesenvironments
through aggregated anomaly subgraphs. Comprehensive evalua- must not only address traditional network attacks but also
tionsontypicalmicroservicebenchmarks(TeaStore,RobotShop, meet new defense needs, such as distributed tracing and zero-
SockShop) demonstrate MADGuard’s superior performance:
trust verification [11], [12]. As a result, anomaly detection
94.08% detection accuracy, significantly outperforming state-
has become a cornerstone for ensuring the stable operation of
of-the-art approaches while maintaining practical operational
efficiency. cloud-native systems [13].
Currentresearchinmicroserviceanomalydetectionfocuses
Index Terms—Microservices security, provenance graph, tem-
primarily on analysis of system calls using machine learn-
poral graph network, anomaly forensics, anomaly detection.
ing or signature-based methods [14], [15], [16], [17], [18],
I. INTRODUCTION [19]. However, three critical limitations persist in enterprise
THE MICROSERVICE architecture improves the environments:
(1) Multi-dimensional data fusion: Existing approaches
scalability and agility of the system by decoupling
such as CDL [20] oversimplify detection by relying solely on
monolithic applications into lightweight, loosely coupled
system call frequencies, neglecting crucial contextual features
services [1], [2], [3]. This architecture is characterized
(process hierarchies, file process patterns, network flows).
by service modularization, independent deployment,
decentralized governance, and API-based communication Thisfeaturesparsityseverelylimitsthedetectionaccuracyfor
mechanisms [4], [5]. These characteristics enable each sophisticated attacks.
microservice to be independently scalable and updatable, (2) Shallow temporal causality: Methods such as STIDE-
but also introduce unique security challenges: (1) Dynamic BoSC [21], CHIDS [22], and ReplicaWatcher [23] analyze
shortsystemcallsequenceswithoutmodelingtemporaldepen-
Received19March2025;revised6September2025;accepted15November dencies, leading to high false negatives for multistage attacks.
2025. Date of publication 24 November 2025; date of current version
For example, our TeaStore case study (Section II) reveals
29December2025.ThisworkwassupportedinpartbytheNationalNatural
Science Foundation of China under Grant U22B2028, Grant 62002324, and howthesemethodsfailtodetectlow-frequencyattackpatterns
Grant62372410;inpartbytheFundamentalResearchFundsfortheProvincial masked within normal operational sequences.
UniversitiesofZhejiangunderGrantRF-A2023009;inpartbytheZhejiang
(3) Lack of anomaly forensic analysis: Current
ProvincialNaturalScienceFoundationofChinaunderGrantLQ21F020016,
GrantLD22F020002,andGrantLZ23F020011;andinpartby“Pioneer”and systems [20], [21], [22], [23] lack causal analysis capabilities,
“Leading Goose” R&D Program of Zhejiang under Grant 2025C01082 and providing isolated alerts without reconstruction of the attack
Grant2025C01013.Theassociateeditorcoordinatingthereviewofthisarticle
path. This gap significantly impedes incident response, partic-
and approving it for publication was R. Riggio. (Corresponding authors:
TiantianZhu;TiemingChen.) ularly for cross-service attacks requiring end-to-end visibility.
The authors are with the School of Computer Science and Technology, Table I presents the detection capabilities of existing
Zhejiang University of Technology, Hangzhou 310023, China (e-mail:
microserviceanomalydetectionsystemsacrossvariousdimen-
ttzhu@zjut.edu.cn;tmchen@zjut.edu.cn).
DigitalObjectIdentifier10.1109/TNSM.2025.3634590 sions. However, no existing method can simultaneously
1932-4537(cid:2)c 2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligence
andsimilartechnologies. Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

768 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
TABLEI
THEEXISTINGANOMALYDETECTIONMETHODSARECOMPAREDINTHREEDIMENSIONS:DATAFEATUREMULTI-DIMENSIONALFUSION,TIME
SERIESCAUSALCORRELATION,ANDANOMALYFORENSICSANALYSIS
address the three main challenges. The provenance graph the accuracy and efficiency of anomaly detection. Moreover,
representsthecontrolflowanddataflowrelationshipsbetween by adopting provenance graphs, the original data’s tem-
system subjects (such as processes, threads, etc.) and objects poral information is retained, and the causal relationships
(such as files, network sockets, etc.) through a directed between data are more intuitively represented, providing
graph, thereby reflecting the causal relationship between stronger explanatory and predictive power in complex data
system events. Due to their rich semantics and robustness, environments.
provenancegraphsarewidelyusedinnetworkintrusiondetec- Abnormal forensic analysis can infer the chain of abnormal
tion [24], [25], [26]. To address these challenges and improve events and restore the abnormal path based on the prove-
theperformanceofanomalydetectionsystemsinmicroservice nance graph. However, as time passes and the volume of
environments, this paper designs a microservice anomaly data increases, the size of the provenance graphs increases
detection system based on provenance graphs. The system exponentially [29], making manual construction impractical.
integratesmultidimensionalinformationfromthemicroservice Existing forensic methods in other fields construct concise
environment and combines graph learning to construct an summary graphs to restore abnormal event paths, reducing
effective anomaly detection model. the need for human intervention [30]. However, in microser-
Consideringthedistributednatureofthemicroservicearchi- vice environments, virtualization characteristics can confuse
tecture, this paper collects key information events covering identical data information across different services, leading
multipledimensions(e.g.,processes,files,networks)inamul- to inaccurate exception source localization. To address this,
tisource service environment. To integrate these multi-source this paper introduces unique identifiers to distinguish services
and multi-dimensional data information without causing con- and designs an anomaly forensic analysis algorithm. The
fusion, this paper employs service identification (mid) and experimental results show that the proposed algorithm sig-
Hasche algorithm to uniquely identify system objects across nificantly reduces the workload of security staff, clarifies
different services. Based on these objects, related events are abnormal data in different microservice environments, and
merged. After data fusion, these complex data are uniformly shortens the forensic analysis time. Furthermore, this paper is
characterized to facilitate subsequent model learning. Inspired the first to integrate an anomaly forensic analysis module into
by previous work [27], this paper adopts feature hashing the microservice anomaly detection system, enhancing overall
and location encoding techniques to efficiently encode multi- system efficiency and accuracy.
source information in the microservice environment into To verify the effectiveness of the proposed method, exper-
compact and semantic-rich feature vectors. Furthermore, a iments were conducted in three representative microservice
time-sliding window mechanism with a time interval T is environments, simulating three typical attack scenarios. The
designed to accumulate feature vectors in real-time. This results indicate that the proposed anomaly detection system
mechanism not only maintains data timeliness but also outperforms existing methods, with a 15.07% improvement
addresses the issue of insufficient multi-dimensional fusion in in detection accuracy. The main contributions of this paper
existing data features. Experimental results in the deployed are:
microserviceenvironmentdemonstratethatembeddingfeature (1) Innovative System Design: A novel microservice
vectors through the time-sliding window mechanism effec- anomaly detection system based on provenance graphs is
tively improves anomaly detection accuracy and reduces the proposed. By integrating multi-source services and multi-
false alarm rate. dimensional data, the system constructs a provenance graph
To address the issue that existing anomaly detection meth- in the microservice environment and leverages graph learning
ods do not fully consider temporal causal relationships in to significantly enhance anomaly detection accuracy.
data sequences, this paper uses the structural characteris- (2) Enhanced Data Features: Advanced feature hashing
tics of provenance graphs to construct data information. By techniques are employed to efficiently fuse multi-source,
structuring data into provenance graphs, temporal continuity multi-dimensional data, optimizing data samples. The time-
and causality are strengthened. The Temporal Graph Network sliding window mechanism enriches data diversity and
(TGN) model is also introduced to dynamically capture com- timeliness, providing more comprehensive and accurate data
plex temporal causal relationships between data [28]. The for anomaly detection.
unique advantage of the TGN model is its ability to analyze (3) Integrated Forensic Analysis: The system introduces an
both temporal and spatial characteristics of graph sequences, anomaly forensic analysis module for the first time, enabling
enablingtheidentificationoflocalandglobalabnormalevents accurate restoration of abnormal events and saving consider-
with high accuracy. This capability significantly enhances able time in security forensic analysis.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 769
Fig.1. Teastore-webshellattack.Initially,theattackerleveragedtheWebUI
| service to   | upload a | WebShell | file named    | shell.jsp, | thereby | gaining | unautho-      |     |     |     |     |     |     |     |     |
| ------------ | -------- | -------- | ------------- | ---------- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| rized access | to the   | server.  | Subsequently, | through    | local   | port    | scanning, the |     |     |     |     |     |     |     |     |
attackerobtainedthedatabaseconnectiondetails.Usingthisinformation,they
createdaShellscriptnamedsql.shtoaccesstheremoteuserdatabase.Finally,
| the attacker | employed | the | mysqldump | tool to | export | sensitive | information, |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --------- | ------- | ------ | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
includinguserlogincredentialsandcreditcarddetails.
| (4) Comprehensive  |     |                 | System         | Evaluation:          |               | The       | system’s    |          |                |     |       |         |           |         |          |
| ------------------ | --- | --------------- | -------------- | -------------------- | ------------- | --------- | ----------- | -------- | -------------- | --- | ----- | ------- | --------- | ------- | -------- |
| performance        | is  | comprehensively |                | evaluated            |               | in        | three real- |          |                |     |       |         |           |         |          |
| world microservice |     |                 | environments,  |                      | demonstrating |           | excellent   |          |                |     |       |         |           |         |          |
| performance        | in  | key metrics     |                | such as detection    |               | accuracy, | detec-      |          |                |     |       |         |           |         |          |
| tion time,         | and | overhead.       |                |                      |               |           |             |          |                |     |       |         |           |         |          |
|                    |     |                 |                |                      |               |           |             | Fig. 2.  | ReplicaWatcher | and | CHIDS | anomaly | detection | methods | identify |
|                    |     |                 | II. MOTIVATION |                      |               |           |             | feature. |                |     |       |         |           |         |          |
| This chapter       |     | presents        | a              | critical examination |               | of        | webshell    |          |                |     |       |         |           |         |          |
CDLanomalydetectionmethoddetectsabnormaleventsby
| attack detection |              | in microservice |           | environments |            | through | a case   |            |               |     |           |      |        |               |            |
| ---------------- | ------------ | --------------- | --------- | ------------ | ---------- | ------- | -------- | ---------- | ------------- | --- | --------- | ---- | ------ | ------------- | ---------- |
|                  |              |                 |           |              |            |         |          | analyzing  | the frequency |     | of system |      | calls. | Specifically, | CDL        |
| study on         | the TeaStore |                 | platform, | highlighting |            | both    | the con- |            |               |     |           |      |        |               |            |
|                  |              |                 |           |              |            |         |          | counts the | frequency     | of  | system    | call | events | every         | second and |
| straints of      | conventional |                 | anomaly   | detection    | techniques |         | and the  |            |               |     |           |      |        |               |            |
identifiesdeviationsfromthebaselinebasedonthisfrequency
| advantages | of our | proposed |     | methodology. |     |     |     |             |          |      |        |     |                |     |           |
| ---------- | ------ | -------- | --- | ------------ | --- | --- | --- | ----------- | -------- | ---- | ------ | --- | -------------- | --- | --------- |
|            |        |          |     |              |     |     |     | (Table II). | However, | this | method | is  | only effective |     | for high- |
TheTeaStorebenchmark—adistributedsystemencompass-
|     |     |     |     |     |     |     |     | frequency | attacks | and is | limited | in  | detecting | low-frequency |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | ------- | --- | --------- | ------------- | --- |
ingauthentication,procurement,andthreeotherindependently
|                     |                 |                |                 |                  |            |              |           | attacks.        | For instance, | in     | the                | case of  | the    | CVE-2017-12615 |              |
| ------------------- | --------------- | -------------- | --------------- | ---------------- | ---------- | ------------ | --------- | --------------- | ------------- | ------ | ------------------ | -------- | ------ | -------------- | ------------ |
| scalable            | services—serves |                | as              | the experimental |            | foundation.  | As        |                 |               |        |                    |          |        |                |              |
|                     |                 |                |                 |                  |            |              |           | vulnerability   | attack,       | the    | attacker’s         | impact   |        | on system      | calls is     |
| depicted            | in Figure       | 1,             | we simulate     | a sophisticated  |            | attack       | chain     |                 |               |        |                    |          |        |                |              |
|                     |                 |                |                 |                  |            |              |           | minimal,        | and the       | normal | and                | abnormal | system | call           | frequency    |
| initiated           | by exploiting   |                | CVE-2017-12625, |                  |            | an arbitrary | file      |                 |               |        |                    |          |        |                |              |
|                     |                 |                |                 |                  |            |              |           | characteristics | are           | nearly | indistinguishable, |          |        | making         | it difficult |
| write vulnerability |                 | in             | the WebUI       | component.       |            | Attackers    | first     |                 |               |        |                    |          |        |                |              |
|                     |                 |                |                 |                  |            |              |           | to detect       | the attack.   |        |                    |          |        |                |              |
| intercept           | service         | communications |                 | via              | Burpsuite, |              | injecting | a               |               |        |                    |          |        |                |              |
|                     |                 |                |                 |                  |            |              |           | STIDE-BoSC      |               | method | combines           |          | the    | STIDE          | [32] and     |
maliciousJSPfileintotheTomcatdirectorytoestablishremote
|                                |                |            |              |                |           |               |             | Bosc [33]           | techniques    | to        | detect      | abnormal   | events.   | It          | counts the  |
| ------------------------------ | -------------- | ---------- | ------------ | -------------- | --------- | ------------- | ----------- | ------------------- | ------------- | --------- | ----------- | ---------- | --------- | ----------- | ----------- |
| code execution.                |                | Subsequent |              | abuse of       | database  | misconfigura- |             |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | frequency           | of different  |           | system      | calls      | within    | the current | time        |
| tions [31]                     | enables        | credential |              | harvesting     | and       | deployment    | of          |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | window              | based on      | their     | temporal    | sequence   |           | and         | maintains a |
| SQL.sh                         | scripts,       | ultimately | compromising |                | sensitive |               | customer    |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | system call         | vector        | database  | with        | a window   |           | size of     | 10. During  |
| financial                      | data through   |            | orchestrated | database       |           | queries.      |             |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | detection,          | the system    | call      | vector      | of         | an epoch  |             | is matched  |
| For the                        | aforementioned |            | attack       | scenario,      |           | existing      | anomaly     |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | against             | the database. | If        | the         | mismatched |           | vector      | exceeds a   |
| detection                      | methods        | such       | as           | ReplicaWatcher |           | and           | CHIDS       |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | certain threshold,  |               | the epoch | is          | deemed     | abnormal. |             | Although    |
| detect                         | window-based   |            | anomaly      |                | events    | by            | identifying |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | this method         | considers     | the       | order       | of system  |           | calls,      | even minor  |
| isolated                       | features.      | For        | example,     |                | they      | may           | detect the  |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | changes             | in the system | can       | trigger     | false      | alarms,   | resulting   | in a        |
| /usr/local/Tomcat/webapps/ROOT |                |            |              | folder         |           | path in       | the file    |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             | high false-positive |               | rate.     |             |            |           |             |             |
| direction                      | feature        | or the     | shell.jsp    | file           | and Java  | process       | in the      |                     |               |           |             |            |           |             |             |
| process                        | feature        | (Figure    | 2).          | However,       | these     | methods       | analyze     |                     |               |           |             |            |           |             |             |
|                                |                |            |              |                |           |               |             |                     |               | III.      | THREATMODEL |            |           |             |             |
featuresinisolation,leadingtoahighfalse-negativerate.Even
if malicious processes or files are identified, it is challenging Toconstructaclassicalthreatmodel,wefocusonmicroser-
to trace the source of the anomaly. vices deployed in Kubernetes environments [34], as most
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

770 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
Fig.3. MADGuardsystemarchitecture.
TABLEII
THENORMALANDABNORMALSYSTEMCALLFREQUENCY temporal sequencing, causality, and forensic analysis. As
CHARACTERISTICSOFCDLSTATISTICS illustrated in Figure 3, the architecture comprises five core
components:provenancegraphconstruction,graphpreprocess-
|     |     |     |     |     |     |     | ing, graph | learning, |     | anomaly | detection, | and | forensic | analysis. |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------- | ---------- | --- | -------- | --------- | --- |
Theoperationalworkflowproceedsasfollows:(1)Thesystem
|     |     |     |     |     |     |     | collects                                   | process,      | file,         | network    | log           | data       | from        | multi-source |       |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | ------------- | ------------- | ---------- | ------------- | ---------- | ----------- | ------------ | ----- |
|     |     |     |     |     |     |     | services.                                  | Temporal      | and           | causal     | relationships |            | are         | analyzed     | to    |
|     |     |     |     |     |     |     | construct                                  | comprehensive |               | provenance |               | graphs     | across      | distributed  |       |
|     |     |     |     |     |     |     | services.                                  | (2)           | Hash          | encoding   | and           | positional | encoding    |              | tech- |
|     |     |     |     |     |     |     | niques are                                 | used          | to preprocess |            | the node      | and        | edge        | information  |       |
|     |     |     |     |     |     |     | in the provenance                          |               | graph         | into       | feature       | vectors.   | For         | each         | 1-hop |
|     |     |     |     |     |     |     | event, composite                           |               | feature       | vectors    | are           | generated  | by          | concatenat-  |       |
|     |     |     |     |     |     |     | ingnode-edgeattributes.Dynamictimewindowsτ |               |               |            |               |            |             | togenerate   |       |
|     |     |     |     |     |     |     | real-time                                  | embedding     |               | feature    | vectors.      | (3)        | Considering |              | the   |
temporaldynamiccharacteristicsofdata,thesystemconstructs
|     |     |     |     |     |     |     | a TGN       | dynamic         | time | series         | network | to        | learn  | the temporal |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ---- | -------------- | ------- | --------- | ------ | ------------ | --- |
|     |     |     |     |     |     |     | and spatial | characteristics |      | of             | benign  | log data. | (4)    | An anomaly   |     |
|     |     |     |     |     |     |     | detector    | computes        | edge | reconstruction |         |           | errors | per window.  |     |
Threshold-exceedingerrorstriggeralertsandforensicpipeline
|          |               |     |        |                  |     |             | activation. | (5) | The | forensic | module | reconstructs |     | anomaly |     |
| -------- | ------------- | --- | ------ | ---------------- | --- | ----------- | ----------- | --- | --- | -------- | ------ | ------------ | --- | ------- | --- |
| existing | microservices | are | hosted | there. Similarly |     | to previous |             |     |     |          |        |              |     |         |     |
propagationpathsthroughsubgraphanalysisandvisualization.
| studies [20], | [21],       | [22],       | [23], | this article | examines | attacks  |     |     |     |     |     |     |     |     |     |
| ------------- | ----------- | ----------- | ----- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| initiated     | by external | adversaries |       | that exploit | open     | vulnera- |     |     |     |     |     |     |     |     |     |
bilities. Specifically, attackers target microservices through A. Provenance Graph Construction
software-level vulnerabilities, including remote code exe- The construction of traditional provenance graph is mainly
| cution, directory  |                | traversal,      | and          | code injection | attacks.  | We        |                |               |          |                   |                   |            |               |              |        |
| ------------------ | -------------- | --------------- | ------------ | -------------- | --------- | --------- | -------------- | ------------- | -------- | ----------------- | ----------------- | ---------- | ------------- | ------------ | ------ |
|                    |                |                 |              |                |           |           | aimed          | at a single   |          | host environment, |                   | while      | microservices |              |        |
| assume             | that attackers | leave           | identifiable | traces         | after     | success-  |                |               |          |                   |                   |            |               |              |        |
|                    |                |                 |              |                |           |           | run in         | a distributed |          | manner.           | Therefore,        |            | information   |              | from   |
| fully compromising |                | a microservice. |              | Additionally,  |           | we assume |                |               |          |                   |                   |            |               |              |        |
|                    |                |                 |              |                |           |           | multiple       | service       | sources  |                   | must be           | integrated |               | when         | build- |
| that the           | collected      | system          | log data     | is complete,   | accurate, | and       |                |               |          |                   |                   |            |               |              |        |
|                    |                |                 |              |                |           |           | ing provenance |               | diagrams |                   | in a microservice |            |               | environment. |        |
untampered. This paper does not address internal attacks, (1) Multi-source Data Integration: Leveraging Kubernetes
system-levelattacks,side-channelattacks,orhardware-related
|     |     |     |     |     |     |     | deployment | characteristics, |     |     | we collect | pod-specific |     | logs | from |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | --- | --- | ---------- | ------------ | --- | ---- | ---- |
attack scenarios.
|     |                                |     |     |     |     |     | cluster    | nodes,      | including | process     | execution  |          | traces, | file       | oper- |
| --- | ------------------------------ | --- | --- | --- | --- | --- | ---------- | ----------- | --------- | ----------- | ---------- | -------- | ------- | ---------- | ----- |
|     |                                |     |     |     |     |     | ations,    | and network |           | activities. | Hash-based |          | entity  | resolution |       |
| IV. | DESIGNOFANOMALYDETECTIONSYSTEM |     |     |     |     |     |            |             |           |             |            |          |         |            |       |
|     |                                |     |     |     |     |     | reconciles | system      | objects   |             | across     | services | while   | maintain-  |       |
This paper proposes a microservice anomaly detection ing pod isolation through unique service identifiers (mid).
system addressing four critical dimensions: data diversity, (2) Definition and Representation of Provenance Graph:
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 771
TABLEIII
nodes, it does not accurately represent the positional relation-
ATTRIBUTESANDFEATURES
ships of nodes within the graph. To address this, we employ
position encoding to restore the positional relationships.
n =Φ(n)+position(n) (2)
(3) Encoding Events in 1-Hop Subgraphs. To effectively
applytheencodedfeaturestographlearning,weencodeevents
represented by each 1-hop subgraph. This coding process
strictly follows chronological order to ensure the temporality
According to the definition of the system-level provenance ofevents,whichisessentialtorevealthedynamicchangesand
graph [24], the system call event E can be represented by a < causality of events. Specifically, we generate a comprehensive
subject,object,time,operation>quadruple.Subjectandobject event feature vector by stacking the feature vectors of times-
represent application process, file and network information, tamps, source context, edge types, and destination context.
andoperationrepresentssystemcalltypes,suchasread,write,
t (cid:2)
timeend
etc. The entire provenance graph G is represented by (S, Gm = [srct ,dstt ,t,msgt ] (3)
O, E) and includes all subjects S, objects O, and events E. t
t
timestart
Given the distributed nature of microservices, podname is
where
introduced when building provenance graphs to distinguish
between different pod events. Microservice system call event msgt =[midt ,edget ,srcmsgt ,dstmsgt ] (4)
Em by<mid,subject,object,time,operation>.Torepresent
the provenance diagram Gm by (ID,S,O,E) to show that. (4)DynamicWindowEmbedding.Slidingwindowsτ create
(3) Data Storage Optimization: Database schemas orga- temporal embeddings balancing real-time responsiveness and
nize subject/object nodes and operational edges for efficient anomaly progression capture.
retrieval, reducing preprocessing latency. (cid:2)T
Zτ = Gτ (5)
B. Graph Preprocessing
Graph Learning Given the temporal dynamics of log
Before graph learning, it is necessary to preprocess the
data and their corresponding provenance graphs, conventional
provenance graph so that the model can learn the information
Graph Neural Networks (GNNs) prove inadequate as they
in the system log.
primarily handle static graph structures. To address this lim-
(1) Encoding Node, Edge, and Position Information. To
itation, we employ a TGN with memory-enhanced update
efficiently encode edge, node, and node position information
mechanisms to capture spatio-temporal patterns in evolving
within the graph, this section integrates Hash encoding
graphs.
and node position encoding techniques. These techniques
MADGuard selects TGN (Temporal Graph Network) as the
transform the nodes, edges, context information, and node
coretemporalmodelingarchitectureduetoitsdeepadaptation
positionsintheprovenancegraphintocompactfeaturevectors.
to the inherent dynamism, distribution, and causal complexity
Traditional encoding methods, such as one-hot and BoSC,
of microservice environments. Compared to general temporal
can convert features into sparse vectors, but fail to capture
graph models (such as TGAT or EvolveGCN), TGN demon-
rich contextual semantics. In contrast, Hash encoding maps
strates significant advantages in the following three aspects:
high-dimensional feature information to low-dimensional vec-
First,TGNintroducesuniquemicroserviceidentifiers(mid)
tors through feature hashing, albeit without capturing node
and Pod names (podname) to represent cross-service events
position information. To address this limitation, we combine
as <mid, subject, object, time, operation> quintuples. This
position encoding technology to extract node features from
mechanism enables the spatiotemporal correlation modeling
the provenance graph. Additionally, to capture the complexity
ofdistributedmulti-sourceheterogeneousevents,ensuringthat
of system behavior, we select nine features closely related to
interactions between different service nodes can be accu-
system behavior, including process name, file path, network
rately captured and associated. It overcomes the topological
source-destination IP and port, and system call type. These
complexity brought by dynamic scaling and cross-node com-
features can effectively describe system behavior, as detailed
munication in microservice environments.
in Table III.
Second,TGNcombinesadynamictimewindowmechanism
Using Hash encoding, we convert node, edge, and node
(such as a 1-minute sliding window) to maintain the temporal
context information strings into fixed-length feature vectors.
continuity of events while effectively covering the complete
This is achieved through two Hash functions: one maps
anomaly propagation chain (such as file upload, database
element nj to the i-th dimension of the feature vector, while
access, and data export in a WebShell attack). This design
the other maps nj to ±1. The formula is defined as follows:
balancesreal-timeresponsivenessandtheintegrityofanomaly
(cid:2) (cid:3) (cid:4)
Φ(n)= ξ nj (1) progression, avoiding feature fragmentation caused by overly
short windows (e.g., a significant drop in Recall with a
j:h(s )=i
j 30-secondwindow)ornoiseinterferenceintroducedbyoverly
(2) Restoring Node Position Relationships. Although the long windows (e.g., a decrease in Precision with a 90-second
above feature encoding restores the relationships between window).
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

772 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
Third, TGN’s memory-enhanced mechanism dynamically isnotablyhigh,itsignalsthatthecurrentsubgraphstraysfrom
aggregates historical node states, edge attributes, and current the expected pattern, hinting at potential suspicious activities.
features through an encoder, enabling the maintenance of (2) Suspicious node identification: Suspicious edges often
long-term cross-service causal dependencies. This is particu- linktosuspiciousnodes.Afteridentifyingansuspiciousedge,
larly suitable for detecting multi-stage low-frequency attacks we check connected nodes for unusual behavior. Furthermore,
in microservices. The mechanism performs outstandingly in in real-world environments, attackers might use common
attack scenarios that require long-term context awareness, processesforsensitiveoperations,likeaccessingsensitivefiles
such as code injection and information leakage. For related /etc/passwd. In such cases, uncommon nodes may emerge,
experimental evidence, see Section V-E. exhibiting suspicious behaviors. We use Inverse Document
TheTGNframeworkoperatesthroughcoordinatedencoder- Frequency (IDF) [35] to spot these sensitive files. The math-
decoder components. The encoder is used for feature ematical formula is as follows:
(cid:5) (cid:6)
embedding from the provenance graph, and the decoder N
predicts the edge type according to the embedded feature IDFυ =log dfυ +1 (8)
vector. Specifically:
where N is the number of nodes in the current time window,
Encoder: Dynamically embeds edge features through tem-
poralaggregation.Foranedgeet attimestampt,itsembedding
dfυ is node υ’s occurrence frequency in the current time
z(t) synthesizes three information streams: Historical node window. If IDFυ exceeds the threshold, the node is flagged.
states s(t −) preceding t; Edge attributes e(t); Current node (3)Anomaly propagation chain construction:Onceiden-
features v(t) via graph neural network propagation: tifying suspicious edges and nodes within each time window,
wetracerelatedeventstoformaone-hopeventqueue.Wethen
z(t)=GNN(s(t),e(t),v(t)) (6) calculatetheanomalyscoreforthecorrespondingqueue.Ifall
queue scores in the window exceed θ (benign data threshold),
Decoder: Predicts edge types through sequential modeling.
we confirm an anomaly. Following this, we construct the
A Long Short-Term Memory (LSTM) network decodes the
anomaly propagation link within the window based on these
temporaldependenciesbetweennodesstates,generatingprob-
queues.
abilistic edge type predictions:
pred(e(t))=LSTM(z(t)) (7) D. Anomaly Forensic Analysis
The output pred(e(t)) ∈ R1×5 represents a probabil- The primary objective of the attack forensics component is
to provide security analysts with a streamlined global attack
ity distribution over five predefined edge types, allowing
graph, which includes two key tasks: 1) reconstructing the
reconstruction-based anomaly detection through prediction
global attack chain; 2) filtering out false positives to refine
errors.
the attack graph. During the anomaly detection phase, it is
commontoidentifyisolatedanomalouseventswithoutgaining
C. Anomaly Detection
a comprehensive view of the anomalies, which forces security
To efficiently identify anomalous events, we segment the analyststosiftthroughnumerousisolatedanomalousnodesto
entire provenance graph into consecutive, fixed-length time find the source of the attack, a process that is extremely time-
window sequences. Within each time window, we detect consumingandlabor-intensive[36].Toaddressthisissue,this
suspicious edges and nodes. Based on these suspicious edges paper compresses benign redundant nodes and edges within
and nodes, we construct a suspicious propagation chain. We services based on the one-hop events constructed during the
thencalculatetheanomalyscoreofthesuspiciouspropagation anomaly detection phase, reducing the overhead of graph
chain. If the anomaly score exceeds the benign data threshold construction. We have observed that the anomaly scores of
θ, we conclude that an anomaly exists within the current anomalouseventsaresignificantlyhigherthanthoseofbenign
window. events. Therefore, by ranking the anomaly scores of events
Our system is tailored for multi-container microservices, and selecting the top-k anomalous events, we can essentially
using 1-minute detection interval. This avoids the resource reconstruct the attack path while refining the attack graph.
contention of high-frequency detection seen in complex Furthermore, since existing cross-service trace tracking can
architectures. The 1-minute window also allows for detailed only reconstruct the application-level call chains between
data analysis with Tetragon, covering process behaviors and servicesandcannotachievecross-servicecallchainsbasedon
network traffic. Unlike methods like ReplicaWatcher with a kernel-levellogs,externalattackersofteninfiltratetheinternal
30-second interval,ourapproach captures thefullpropagation service systems to gain maximum privilege information.
chain of progressive anomalies like resource leaks. Combined Hence, we have designed a global microservices attack graph
with a four-day pre-trained model, it balances real-time reconstruction method to track both single-service and cross-
response with long-term pattern generalization, optimizing serviceglobalattackchains.Forcybersecurityteams,anomaly
resource use, analysis depth, and detection accuracy. forensic analysis is crucial for quickly pinpointing the source
(1)Suspiciousedgeidentification:Weutilizeawell-trained ofeventsandrestoringaffectedpaths.Toexpeditethisprocess,
andhigh-performanceanomalydetectionmodeltoreconstruct we simplify complex anomaly data, including consolidating
edges within each time window. Meanwhile, we calculate the edgesforidenticalnodesacrossvarioustimesandversions.To
reconstruction error of these edges. If the reconstruction error accurately trace the source of anomalous events, our module
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 773
Algorithm 1 Anomaly Graph Construction kernel-levelmonitoringtoolTetragontocollectlogsandattach
θ;
Input: List of anomaly events Q; Anomaly threshold Number of repre- Pod-level metadata (such as pod_id, container paths, and
sentativeeventsk source/destination Pod information for network connections)
| Output: | Service-Specific | anomaly graphs | G |p∈pods; | Global | anomaly |     |     |     |     |     |     |     |
| ------- | ---------------- | -------------- | ---------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
p
graphG to each node, rather than relying solely on node names for
global
1: //Step1:Filtertop-krepresentativeanomalyevents identification. For example:
| InitializeG | ←{}//mapspodnamestolistsofevents |     |     |     |     |         |       |     |          |            |      |             |
| ----------- | -------------------------------- | --- | --- | --- | --- | ------- | ----- | --- | -------- | ---------- | ---- | ----------- |
| 2:          |                                  |     |     |     |     | Process | nodes | are | uniquely | identified | by a | combination |
3: count←0
4: foreacheventeinQdo of “process name-Pod name” (e.g., java-teastore-webui,
5: computeloss←crossEntropy(e) java-teastore-db). Even if the process names are the
6: p←podname(e)
ifloss>θ same, instances in different Pods are treated as sep-
| 7:  | then |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8: ifp(cid:4)∈Gthen arate nodes. File nodes are associated with Pods
9: G[p]←emptylist through their absolute paths within the container (e.g.,
10: endif
|     |     |     |     |     |     | /usr/local/tomcat/webapps/ROOT/shell.jsp |     |     |     |     | belongs | to the |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ------- | ------ |
11: appendetoG[p]
count←count+1 teastore-webui Pod, while /var/lib/mysql/teadb.sql belongs to
12:
13: ifcount≥kthen
|     |       |     |     |     |     | the teastore-db |     | Pod). Network |     | nodes are    | bound to | Pods based  |
| --- | ----- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | ------------ | -------- | ----------- |
| 14: | break |     |     |     |     |                 |     |               |     |              |          |             |
|     |       |     |     |     |     | on the source   | and | destination   |     | IP addresses | of the   | connections |
15: endif
(e.g.,thedestinationIP10.0.0.10:3306belongstotheteastore-
16: endif
17: endfor db Pod, while the source IP 10.0.0.5 corresponds to the
18: //Step2:Constructanomalygraphforeachservice
|                   |     |                                       |     |     |     | teastore-webui |     | Pod). |     |     |     |     |
| ----------------- | --- | ------------------------------------- | --- | --- | --- | -------------- | --- | ----- | --- | --- | --- | --- |
| 19: initializepod |     | ←emptydictionary//mapsnodestopodnames |     |     |     |                |     |       |     |     |     |     |
node
20: initializesrc ←emptydictionary//mapspodnamestosourcenodes During the anomaly graph construction process,
| foreachpodnamep∈Gdo | node |     |     |     |     |           |             |     |           |            |        |        |
| ------------------- | ---- | --- | --- | --- | --- | --------- | ----------- | --- | --------- | ---------- | ------ | ------ |
| 21:                 |      |     |     |     |     | Algorithm | 1 maintains |     | a podnode | dictionary | (steps | 19–27) |
G ←createnewdirectedgraph
| 22: | p   |     |     |     |     | to record | the | Pod IP | information | of  | each network | node. |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------ | ----------- | --- | ------------ | ----- |
23: foreachevente∈G[p]do
24: foreachnodeninnodes(e)do When processing an anomaly event for a particular Pod,
25: ifn(cid:4)∈pod then the algorithm checks the network nodes. If it finds that the
pod node [n]←p
26: node destination IP of a network node exists in podnode and the
| 27: | endif |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
28: addntoG correspondingPodofthisdestinationIPisnotthecurrentPod
p
29: endfor being processed, then this node is identified as a cross-Pod
30: foreachedge(u,v)inedges(e)do
add(u,v)toG node (step 43). Subsequently, the algorithm locates the initial
| 31: |     | p   |     |     |     |               |      |            |     |                |     |              |
| --- | --- | --- | --- | --- | --- | ------------- | ---- | ---------- | --- | -------------- | --- | ------------ |
|     |     |     |     |     |     | attack source | node | srcnode[p] |     | of the current | Pod | (obtained by |
32: endfor
33: src←identifySourceNode(e) sorting and filtering based on anomaly scores, steps 33–36)
| 34: | ifsrc(cid:4)∈src | [p]then |     |     |     |                                                      |       |            |         |       |          |            |
| --- | ---------------- | ------- | --- | --- | --- | ---------------------------------------------------- | ----- | ---------- | ------- | ----- | -------- | ---------- |
|     |                  | node    |     |     |     | andconstructsanedgefromsrcnode[p]tothiscross-Podnode |       |            |         |       |          |            |
| 35: | src node         | [p]←src |     |     |     |                                                      |       |            |         |       |          |            |
|     |                  |         |     |     |     | n, adding                                            | it to | the global | anomaly | graph | G_global | (step 46). |
36: endif
37: endfor
|     |     |     |     |     |     | Taking | the | TeaStore | WebShell | attack | as  | an example |
| --- | --- | --- | --- | --- | --- | ------ | --- | -------- | -------- | ------ | --- | ---------- |
38: endfor
|     |     |     |     |     |     | (Section | V-D, Figure | 1,  | Figure | 6), when | the database | process |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------ | -------- | ------------ | ------- |
39: //Step3:Constructglobalanomalygraph
|              |                         |     |     |     |     | mysqld-teastore-db |     | is  | accessed | by the | abnormal | process java- |
| ------------ | ----------------------- | --- | --- | --- | --- | ------------------ | --- | --- | -------- | ------ | -------- | ------------- |
| 40: G global | ←createnewdirectedgraph |     |     |     |     |                    |     |     |          |        |          |               |
foreachpodnamep∈Gdo
| 41: |     |     |     |     |     | teastore-webui |     | (marked | as abnormal |     | due to the | execution |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ----------- | --- | ---------- | --------- |
42: //addcross-podedges
|     |                 |           |     |     |     | of the | malicious | file | shell.jsp) | in the | teastore-webui | Pod, |
| --- | --------------- | --------- | --- | --- | --- | ------ | --------- | ---- | ---------- | ------ | -------------- | ---- |
| 43: | foreachnodeninG | .nodes do |     |     |     |        |           |      |            |        |                |      |
p
44: ifpod [n](cid:4)=p then specific sockets are generated. In the teastore-webui Pod,
|     | addedge(src node | [p],n)toG | //assumingsrc |     | [p]is |     |     |     |     |     |     |     |
| --- | ---------------- | --------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
45: node global node the socket 10.244.2.168:55602→10.102.87.233:3306 is cre-
sourcenodeofpodp ated, where the destination IP 10.102.87.233:3306 points
46: endif
47: endfor to the database service. In the teastore-db Pod, the socket
48: endfor 10.244.2.167:3306→10.244.2.168:55602iscreated.Whenthe
G p,G
| 49: return | global |     |     |     |     |           |           |          |             |       |                        |     |
| ---------- | ------ | --- | --- | --- | --- | --------- | --------- | -------- | ----------- | ----- | ---------------------- | --- |
|            |        |     |     |     |     | algorithm | processes | the      | anomaly     | event | for the teastore-webui |     |
|            |        |     |     |     |     | Pod, it   | detects   | that the | destination | IP    | 10.102.87.233:3306     |     |
correspondstotheteastore-dbPod,nottheteastore-webuiPod,
compiles anomaly subgraphs from each microservice into a and thus identifies this network node as a cross-Pod node.
unified global graph. Using this approach, we have developed Meanwhile,thealgorithmlocatestheinitialattacksourcenode
an algorithm (Algorithm 1) that identifies the top K most srcnode[teastore-webui] as java-teastore-webui and constructs
significant anomalies by evaluating anomaly values across a cross-service edge from java-teastore-webui to mysqld-
different service subgraphs. Finally, we employ Graphviz to teastore-db. This cross-service edge, together with subsequent
visualizethecompleteanomalypath.Thistooloffersadetailed database operation nodes (such as the node executing mysql-
and interactive representation, aiding in efficient root cause dump to export sensitive data), forms a complete attack
| analysis. |     |     |     |     |     | chain. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
In Algorithm 1, the detection of cross-service edges Itisworthnotingthatinmicroserviceenvironments,evenif
relies on the Pod identification native binding mecha- thesamenode(suchas/etc/hostsoradatabaseIP)isaccessed
nism introduced during the provenance graph construction bymultiplePods,Tetragongeneratesuniquesocketidentifiers
phase (Section IV-A). This ensures that each system entity for each interaction (e.g., 10.0.0.5:55602→10.0.0.10:3306 vs.
(processes, files, network connections) is explicitly associated 127.0.0.1:3306→127.0.0.1:48921), and these socket details
with its respective Pod. Specifically, we use the eBPF-driven are preserved through edge attributes (Section IV-B). This
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

774 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
|     |     |     |     |                    |           | V.        | EVALUATION |                   |             |          |
| --- | --- | --- | --- | ------------------ | --------- | --------- | ---------- | ----------------- | ----------- | -------- |
|     |     |     |     | To comprehensively |           |           | evaluate   | the effectiveness |             | of our   |
|     |     |     |     | proposed           | anomaly   | detection | system,    | we                | investigate | four key |
|     |     |     |     | research           | questions | through   | rigorous   | experimentation:  |             |          |
|     |     |     |     | RQ1.               | Detection | Accuracy: | How        | does              | our system  | compare  |
withexistingmicroserviceanomalydetectionsystemsinterms
|     |     |     |     | of detection     | performance? |             |      |                 |             |          |
| --- | --- | --- | --- | ---------------- | ------------ | ----------- | ---- | --------------- | ----------- | -------- |
|     |     |     |     | RQ2.             | Runtime      | Overhead:   | What | is the          | operational | cost of  |
|     |     |     |     | our anomaly      | detection    | system,     | and  | how does        | it compare  | with     |
|     |     |     |     | state-of-the-art | solutions?   |             |      |                 |             |          |
|     |     |     |     | RQ3.             | Forensic     | Capability: |      | How effectively |             | does the |
Fig.4. Lossvaluescomparison. forensic analysis module trace anomaly sources, and what
|                  |                    |                |                     | performance  | impact    | does      | it introduce? |          |                |              |
| ---------------- | ------------------ | -------------- | ------------------- | ------------ | --------- | --------- | ------------- | -------- | -------------- | ------------ |
|                  |                    |                |                     | RQ4.         | Component | Ablation: |               | What is  | the individual | con-         |
| ensures          | that the algorithm | can accurately | distinguish between |              |           |           |               |          |                |              |
|                  |                    |                |                     | tribution    | of each   | component | in            | MADGuard | to             | the system’s |
| Pod interactions | and                | avoid missing  | real cross-service  | performance? |           |           |               |          |                |              |
dependencies.
|           |        |     |     | A. Experimental |              | Setup |             |     |              |         |
| --------- | ------ | --- | --- | --------------- | ------------ | ----- | ----------- | --- | ------------ | ------- |
| E. Online | Update |     |     |                 |              |       |             |     |              |         |
|           |        |     |     | (1) Test        | Environment: |       | We deployed |     | a Kubernetes | cluster |
To address the issue of performance degradation of with one master node and two worker nodes running Ubuntu
MADGuard over time, we propose an online update mecha- 22.04 and Containerd v1.6.33.
nism(OnlineUpdate,OU).ThecoreofOUliesintheconcept Teastore[37], SockShop [38], and RobotShop[38] cover the
of real-time drift detection and targeted incremental model common multi-technology stacks found in enterprise-level
updates. To automatically identify when model performance microservices, as shown in Table IV below. These scenarios
degrades due to changes in data distribution (concept drift), encompass mainstream languages such as Java, PHP, Node.js,
OU utilizes the standard deviation of anomaly scores output and Go, and their attack surfaces (such as Tomcat remote
by the model as a key metric. This approach relies on the code execution, PHP code injection, and Node.js path traver-
analysis of three types of typical data (pure benign daily data, sal) are consistent with real-world enterprise environments.
new daily data generated by the evolution of benign behavior, We have selected Teastore, SockShop, and Teastore as test
andanomalousdailydata).Thestandarddeviationofanomaly environments.Regardinglogcollectiontools,sinceKubernetes
scores s for pure benign data is relatively stable; the standard native observability tools (such as service mesh, Istio) focus
deviation snew produced by the evolution of benign behavior on application-level call chain monitoring, they are unable to
typically falls within 3 times the historical standard deviation capture kernel-level attack traces (such as access to sensitive
∈(s,3s));
s (i.e., snew whereas the standard deviation sanom fileslike/etc/passwd,creationofmaliciousfileslikeshell.jsp).
generated by anomalous data significantly exceeds this range, Therefore, MADGuard employs a kernel-level observation
as shown in Figure 4. Based on this finding, the system tool, Tertagon, which uses eBPF technology to collect pro-
maintains a sliding window to record the current baseline of cess, file, network, and other low-level events, ensuring the
benign behavior and calculates the standard deviation snew of completecaptureofattackbehaviors.TheTetragonmonitoring
newly incoming data in real-time. When snew falls within the component [39] was deployed as a DaemonSet to ensure non-
(s,3s) range, a concept drift alarm is triggered. intrusive data collection across all nodes.
Once drift is detected, the system initiates an incremental (2) DataSet: We injected representative vulnerabilities into
model update process. To prevent the model from updating threemicroservicebenchmarks(Teastore[37],Sockshop[38],
solely on new data, which could lead to a “catastrophic Robotshop [38]) to simulate critical attack scenarios:
forgetting” of old knowledge, the update does not only use WebShellattack(CVE-2017-12615): Theattackerfirstcon-
the new window data that triggered the drift. The system structs a WebShell file named shell.jsp within the webui
looks back at an equally sized historical old window of data servicetogainunauthorizedaccesstotheserver.Subsequently,
(representingpreviouslystablenormaldata).Subsequently,the by scanning local ports, the attacker acquires connection
newwindowdatacausingthedriftismergedwiththeretrieved details for the teadb database. Using this information, the
old window data to form a small-scale incremental training attacker creates a shell script named sql.sh to remotely access
dataset. The existing model is then incrementally trained the user database. Finally, leveraging the mysqldump utility,
with the merged dataset, allowing the model to learn new theattackerextractssensitiveinformation,includinguserlogin
patternswhileconsolidatingoldknowledge.Aftersuccessfully credentials and credit card details.
updatingthemodel,thereferenceslidingwindowdatausedfor Code injection (CVE-2024-2961): The attacker creates a
detecting drift also needs to be updated, typically refreshing malicious shell.php file, leverages a remote code execution
thereferencebaselinewiththenewwindowdatathattriggered flaw in the ratings service to run it, and exfiltrates server
this update, providing the most current standard deviation s details (RobotShopRatingsKernelDevbugContainer.php.meta)
baseline for subsequent drift detection. and sensitive file data (/etc/group).
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 775
TABLEIV
| vectors, | if the | reconstruction |     | error exceeds | a   | predetermined |     |
| -------- | ------ | -------------- | --- | ------------- | --- | ------------- | --- |
MICROSERVICESPLATFORMSANDTHEIRTECHNOLOGIES
| threshold, | the | system | call sequence | is  | determined | to  | be an |
| ---------- | --- | ------ | ------------- | --- | ---------- | --- | ----- |
anomaly.
ReplicaWatcher[23]:Thismethodfirstprocessesacontin-
| uous stream                          | of             | events        | into a short | monitoring     |                    | interval (called |        |
| ------------------------------------ | -------------- | ------------- | ------------ | -------------- | ------------------ | ---------------- | ------ |
| a“Snapshot”).                        |                | Next, feature | vectors      | are            | generated          | from             | each   |
| snapshot                             | to capture     | the           | differences  | between        | that               | snapshot         | and    |
| othersnapshots.Intheanomalydetection |                |               |              |                | phase,thedeviation |                  |        |
| of each                              | snapshot       | from          | the ideal    | state          | (where             | all snapshots    |        |
| are identical)                       | is             | evaluated.    | If any       | snapshot       | is                 | found to have    | a      |
| significant                          | deviation,     | it            | is judged    | to be          | abnormal.          |                  |        |
| Table                                | VII summarizes |               | key          | implementation |                    | differences.     |        |
| Our system                           |                | (MADGuard)    |              | uniquely       | incorporates       |                  | multi- |
| service                              | monitoring     | with          | Tetragon     | while          | requiring          | extended         |        |
pre-training.
| B. Detection | Performance   |           | (RQ1)         |                  |          |                |     |
| ------------ | ------------- | --------- | ------------- | ---------------- | -------- | -------------- | --- |
| Table        | VIII presents |           | comprehensive | detection        |          | metrics across |     |
| three attack | scenarios.    |           | Our analysis  | reveals          | three    | key patterns:  |     |
| WebShell     | Attack        | Analysis: |               | MADGuard         | achieves | superior       |     |
| F1-score     | (0.8666)      | through   | optimal       | precision-recall |          | balance,       |     |
Information leakage (CVE-2017-14849): The attacker while CDL’s exceptional accuracy (99.92%) stems from its
exploits a vulnerability in the front-end service to construct frequency-based reconstruction mechanism that effectively
maliciousfilepaths(e.g.,/../../../../etc/XX)andaccesssensitive filters common system call patterns. However, CDL’s 41.26%
server files such as passwd, shells, group, fstab, profile, and missed detection rate (1 - 0.5874 Recall) exposes limitations
protocols. in recognizing novel attack signatures. STIDE-BoSC’s poor
For each scenario, we collected 4 days of operational data performance (F1=0.044) confirms the inadequacy of slid-
containing more than 30 million normal events and 900,000 ing window approaches for stealthy WebShell activities that
anomalous events, as detailed in Tables V and VI. exhibit temporal dispersion.
(3) Baseline Systems: We compare against four state-of- Code Injection Dynamics: While CHIDS demonstrates
the-art approaches: competitive F1-score (0.8881), its 19.64% false positive rate
STIDE-BOSC [21]: It combines STIDE and BOSC tech- (1 - 0.8036 Precision) suggests over-sensitivity to parameter
niques to model a sequence of system calls. Specifically, the variations in PHP execution contexts. MADGuard’s per-
method uses a time window with a size of 10 to record the fect precision demonstrates exceptional discriminative power
frequency of each system call and constructs a system call in containerized PHP environments, accurately distinguish-
bag-of-wordsvectordatabase.Intheanomalydetectionphase, ing legitimate Composer operations from malicious payload
thenewsystemcallbag-of-wordsvectoriscomparedwiththe injections.
vector in the database. Once the number of mismatched bag- Information Leakage Characteristics: The proposed
of-words vectors exceeds the set threshold, the current time system’s complete recall (1.0000) in Node.js environments
period is judged to be an anomaly. validates our graph neural network’s capability to detect low-
CHIDS [22]: This method focuses on identifying unusual and-slow data exfiltration patterns. CHIDS’ precision-recall
sequences of system calls while integrating the sequence’s imbalance (1.0000 vs 0.4428) reveals inherent challenges
parametersandcontextinformation.Itdividesalongsequence in modeling asynchronous I/O operations characteristic of
into small segments of fixed length and represents these seg- Node.js microservices.
mentsasgraphs.Byanalyzingthedegreecentralityandweight Overall,theproposedmethodinthispaperperformswellin
of the graph, feature vectors such as sequence frequency all scenarios, especially on F1-score and Accuracy, showing
and parameters are extracted, and these feature vectors are itshighefficiencyandreliabilityinanomalydetection,andthe
trained by autoencoder. In the anomaly detection stage, by effectiveness of the proposed method in anomaly detection,
reconstructingthesefeaturevectors,ifthereconstructionerror compared with the existing anomaly detection system, the
exceeds the preset threshold, the sequence is considered to be accuracy is improved by 15.07%. CDL does very well on
abnormal. Accuracy, but lacks Recall, which can lead to some under-
CDL[20]:Thisapproachfocusesoncountingthefrequency reporting. CHIDS perform well in code injection scenarios,
of various types of system calls and constructing frequency but Recall is low in information leak scenarios, affecting
vectorsbasedonthesestatistics.Subsequently,anautoencoder overall performance. ReplicaWatcher has high Precision in
is used to train and learn these frequency patterns. In the some scenarios but low Recall, which means it can generate
anomaly detection phase, by reconstructing these frequency false positives in different scenarios.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

776 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
TABLEV
MICROSERVICEATTACKENVIRONMENT
TABLEVI
|     |     |     |     |     |     |     |     | The experimental |     | results | (Figure |     | 5) show | that | the trace |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------- | --- | ------- | ---- | --------- |
DISTRIBUTIONOFEXPERIMENTALDATA
|     |     |     |     |     |     |     |     | storage          | increment   | of           | the trace       | graph        | grows      | linearly         | with       |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | ------------ | --------------- | ------------ | ---------- | ---------------- | ---------- |
|     |     |     |     |     |     |     |     | increasing       | load:       | although     | the             | storage      | increment  | per              | hour in    |
|     |     |     |     |     |     |     |     | the high         | load        | scenario     | is slightly     | higher       |            | than in          | the light  |
|     |     |     |     |     |     |     |     | load scenario,   |             | the overall  | growth          | is           | stable,    | with             | no non-    |
|     |     |     |     |     |     |     |     | linear expansion |             | observed.    | This            | performance  |            | is attributed    | to         |
|     |     |     |     |     |     |     |     | the optimized    |             | storage      | strategy        | of the       | trace      | graph,           | including  |
|     |     |     |     |     |     |     |     | hash coding      | techniques  |              | for             | compressing  |            | high-dimensional |            |
|     |     |     |     |     |     |     |     | features         | and pod     | isolation    | mechanisms      |              | to         | avoid            | redundant  |
|     |     |     |     |     |     |     |     | cross-service    | data,       | proving      | its             | controllable |            | storage          | overhead   |
|     |     |     |     |     |     |     |     | during long-term |             | high         | load operation. |              | At the     | same             | time, the  |
|     |     |     |     |     |     |     |     | peak memory      | of          | TGN          | remains         | stable       | across     | all load         | levels,    |
|     |     |     |     |     |     |     |     | without          | significant | fluctuations |                 | with         | increasing | load,            | due to     |
|     |     |     |     |     |     |     |     | the dynamic      | memory      | management   |                 | strategy     |            | adopted          | by TGN,    |
|     |     |     |     |     |     |     |     | which focuses    |             | on recent    | key data        | and          | reduces    | the              | storage of |
|     |     |     |     |     |     |     |     | the full         | historical  | log          | to efficiently  |              | control    | memory           | usage.     |
|     |     |     |     |     |     |     |     | Additionally,    | with        | increasing   |                 | load, the    | graph      | reconstruction   |            |
timeper60kdatashowsaslowgrowthtrend:thelowestinthe
|     |     |     |     |     |     |     |     | light load  | scenario,  | slightly | higher   | in    | the high | load        | scenario, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | -------- | ----- | -------- | ----------- | --------- |
|     |     |     |     |     |     |     |     | but overall | maintained |          | at a low | level | within   | 14 seconds. | This      |
indicatesthateveninhighloadscenarios,theanomalyforensic
| Fig. 5. | MADGuard | core | component | runtime | overheads | at different | load |            |          |     |         |            |         |     |             |
| ------- | -------- | ---- | --------- | ------- | --------- | ------------ | ---- | ---------- | -------- | --- | ------- | ---------- | ------- | --- | ----------- |
|         |          |      |           |         |           |              |      | process of | MADGuard |     | remains | efficient, | without | a   | significant |
levels.
|            |          |     |               |     |          |       |     | increase         | in time | due to | the increase | in     | data  | volume, | verifying |
| ---------- | -------- | --- | ------------- | --- | -------- | ----- | --- | ---------------- | ------- | ------ | ------------ | ------ | ----- | ------- | --------- |
|            |          |     |               |     |          |       |     | the practicality |         | of the | forensic     | module | under | complex | load      |
| C. Runtime | Overhead |     | & Scalability |     | Analysis | (RQ2) |     |                  |         |        |              |        |       |         |           |
conditions.
| The runtime |             | comparison   |     | in Table | IX reveals | critical | engi- |     |     |     |     |     |     |     |     |
| ----------- | ----------- | ------------ | --- | -------- | ---------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| neering     | trade-offs: | STIDE-BoSC’s |     |          | efficiency | (9s)     | comes | at  |     |     |     |     |     |     |     |
the cost of limited detection scope - its single-container D. Forensic Analysis (RQ3)
focus ignores 30% of cross-service anomalies in our testbed; To validate the effectiveness of the forensic module,
CHIDS’ prolonged runtime (960s) stems from expensive performance analysis was conducted in three typical attack
graph isomorphism checks, increasing exponentially with scenarios:CodeInjection,InformationLeakage,andWebShell
sequencecomplexity;MADGuard’smoderateoverhead(240s) Attack, with comparisons made to the Kairos [27] anomaly
reflects the computational intensity of our hybrid architecture, reconstruction method.
but remains practical given its 1-minute detection interval. In the Code Injection attack scenario, MADGuard demon-
Combing Table VII, MADGuard’s achieves 56% better F1- strated high precision: apart from benign events frequently
score than ReplicaWatcher with only 2.4× time increase. accessed within the service (such as ‘/etc/hosts’) being mis-
To analyze the runtime overhead of MADGuard in the judged as anomalies and occasional omissions of ‘/proc’ file
trace storage, TGN memory update, and forensic graph eventsassociatedwithanomalies,coreanomalousevents(such
reconstruction phases, performance analysis was conducted as the creation of the malicious file ‘/shell.jsp’) were all
under different load conditions. The experiment was based accurately identified. With the help of unique event identi-
on a Kubernetes cluster environment verified in the paper, fication and cross-service event reconstruction methods, the
simulating varying degrees of load intensity by injecting real entire attack chain could be clearly and completely traced.
businesstraffic:CPUloadsof20%(lightload),40%(medium In contrast, although Kairos’ anomaly reconstruction method
load), 60% (medium-high load), and 80% (high load), corre- could detect some anomalies, it missed key events such as
sponding to peak business scenarios of Sockshop, Robotshop, ‘shell.jsp’,anditscommunitypartitioningstrategyfragmented
and Teastore benchmark microservices. The collected log the attack graph into multiple subgraphs, obscuring the rela-
volume increased with the load and covered a mixed load tionships between anomalous events.
pattern of complex attacks such as Web shell attacks and In the Information Leakage attack scenario, MADGuard
code injection, to meet the stress testing needs of real-world effectively filtered out most false-positive events, with only a
business scenarios. few‘/proc’filesbeingmisjudged;similartotheCodeInjection
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 777
TABLEVII
COMPARISONOFEXPERIMENTALDETAILSOFANOMALYDETECTION
TABLEVIII
PERFORMANCECOMPARISONOFANOMALYDETECTIONSYSTEM
TABLEIX
scenario, the frequent access to ‘/etc/hosts’ within the service
RUNTIMEOVERHEADCOMPARISON
wasmisjudgedasananomaly,butcoreanomalousevents(such
assensitiveaccessesto‘/etc/passwd’and‘/etc/fstab’)wereall
successfullydetected,andtheattackpathcouldbecompletely
reconstructed. Kairos performed poorly in this scenario, not
onlymisjudgingalargenumberofnormaleventsasanomalies
but also disrupting the coherence of the attack chain due to and “MADGuard with a forensic module” (the relevant
its graph partitioning strategy. results are shown in Figure 6), with a detailed analysis as
In the WebShell Attack scenario, MADGuard significantly follows:
filtered out false-positive events through top-k event filtering, WhenMADGuardisnotintegratedwithaforensicanalysis
achieving a 33% increase in precision compared to Kairos, module (Figure 6a)), the system can only present the detected
with only a 3% decrease in recall, thus balancing precision anomalous nodes in isolation, without the ability to correlate
and completeness. the attack propagation paths between nodes, nor to label
In terms of throughput performance, MADGuard demon- the microservices to which the anomalous nodes belong (for
strated efficient processing capabilities: it processed 26,672 example, it cannot distinguish whether the anomalous nodes
events in the Code Injection scenario in just 4 seconds, arefromthe“OrderService”orthe“PaymentService”),caus-
handled 118,784 events in the Information Leakage scenario ing security analysts to manually investigate the relationships
in 7 seconds, and processed 452,608 events in the WebShell andaffiliationsofnodes,greatlyincreasingthecomplexityand
Attack scenario in 10 seconds. On average, it could handle time consumption of attack tracing.
over 60,000 events every 7 seconds. Compared to Kairos’ RegardingtheexistingKairosforensicmethod(Figure 6b)),
real-time attack reconstruction capability, MADGuard’s event although it can connect some anomalous nodes to form
processing rate per second increased by more than 7,000. The paths, there are two key shortcomings: First, Kairos uses a
specific performance metrics are shown in Table X. community division algorithm for path aggregation, which is
To further illustrate the core value of the security forensics prone to splitting cross-service attack propagation chains into
module, this section starts from the actual operational needs severalisolatedsubgraphs(forexample,thecompletepathofa
of security analysts, taking the WebShell attack scenario WebShellattackfromthe“FrontendService”tothe“Database
in the TeaStore environment as an example, and compares Service” is split), failing to reconstruct the global propagation
the differences in the forensic results of “MADGuard with- process of the attack; Second, due to the possibility of
out a forensic module,” “existing Kairos forensic method,” similar names or paths of nodes across different services
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

778 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
TABLEX
PERFORMANCECOMPARISONOFMADGUARDANDKAIROSINDIFFERENTATTACKSCENARIOS
Fig.6. ComparisonofforensicanalysismethodsinWebShellattack:impactonattackpathreconstructionandnodeaffiliationclarity.
in a microservices environment (for example, each service (mid), it labels each node with explicit service affiliation
contains a “log.txt” file node), Kairos lacks a mechanism information (for example, “order-service:node-123”), helping
for clearly identifying node affiliations, which can lead to analysts quickly locate the service to which the anomalous
analysts mistakenly identifying nodes under different services node belongs; On the other hand, relying on a cross-service
as belonging to the same service, resulting in misjudging the attack chain identification mechanism, it can associate iso-
scope of the attack. latedanomalousnodesbeyondserviceboundaries,completely
In contrast, MADGuard’s forensic analysis module reconstructing the global propagation path from the attack
addressestheaforementionedissuesthroughtwocoredesigns: entry point (such as the WebShell implantation point) to
On one hand, by introducing a unique service identifier the target service (such as the database data theft point)
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 779
Fig.9. ForensicanalysisofInformationLeakageinSockShop.
|     |     |     |     | E. Comparison |     | of MADGuard-TGN |     | With | Existing | Temporal |     |
| --- | --- | --- | --- | ------------- | --- | --------------- | --- | ---- | -------- | -------- | --- |
Models
|     |     |     |     | To verify | the     | superiority | of  | the TGN          | (Temporal |     | Graph   |
| --- | --- | --- | --- | --------- | ------- | ----------- | --- | ---------------- | --------- | --- | ------- |
|     |     |     |     | Network)  | adopted | by MADGuard |     | in microservices |           |     | anomaly |
Fig.7. ForensicanalysisofWebshellattackinTeaStore.
|     |     |     |     | detection | scenarios, | this | paper | designs | comparative |     | experi- |
| --- | --- | --- | --- | --------- | ---------- | ---- | ----- | ------- | ----------- | --- | ------- |
mentsinthreetypicalmicroservicesbenchmarkenvironments:
|     |     |     |     | TeaStore,        | SockShop, | and              | RobotShop.   |            | The data    | preprocess-   |         |
| --- | --- | --- | --- | ---------------- | --------- | ---------------- | ------------ | ---------- | ----------- | ------------- | ------- |
|     |     |     |     | ing procedures   |           | (hash encoding,  |              | positional | encoding),  |               | feature |
|     |     |     |     | dimensions       | (each     | 16-dimensional), |              | and        | evaluation  | protocols     |         |
|     |     |     |     | (with Precision, |           | Recall,          | and F1-score |            | as core     | metrics)      | are     |
|     |     |     |     | kept completely  |           | consistent,      | with         | only       | the         | core temporal |         |
|     |     |     |     | modeling         | module    | TGN being        | replaced     |            | by existing | temporal      |         |
graphmodelsTGAT(TemporalGraphAttentionNetwork)and
|     |     |     |     | EvolveGCN       | (Evolving    | Graph          | Convolutional |     | Networks) |             | for a |
| --- | --- | --- | --- | --------------- | ------------ | -------------- | ------------- | --- | --------- | ----------- | ----- |
|     |     |     |     | fair comparison |              | of the models’ | adaptability. |     |           |             |       |
|     |     |     |     | The             | experimental | results        | (Figure       |     | 10) show  | that        | TGN   |
|     |     |     |     | exhibits        | better       | detection      | performance   |     | in all    | three types | of    |
Fig.8. ForensicanalysisofcodeinjectioninRobotShop.
|     |     |     |     | microservices  |         | attack scenarios, | especially |               | in cross-service |               | and    |
| --- | --- | --- | --- | -------------- | ------- | ----------------- | ---------- | ------------- | ---------------- | ------------- | ------ |
|     |     |     |     | highly         | dynamic | scenarios:        | in         | the RobotShop |                  | code          | injec- |
|     |     |     |     | tion scenario, |         | TGN’s F1-score    | reaches    |               | 0.8888           | and Precision |        |
(Figure 6c)). Ultimately, it provides security analysts with maintains 1.0, accurately distinguishing normal dependency
forensicresultsthatare“clearinnodeaffiliationandcomplete calls in the PHP environment from malicious code injection,
in path continuity,” significantly reducing the difficulty and whileTGATandEvolveGCN’sF1-scoresareonly0.8177and
time cost of attack tracing. 0.7615,respectively;intheTeaStoreWebShellattackscenario,
MADGuard Forensic Analysis Results: TGN’sF1-scoreis0.8666,althoughTGAT’sF1-score(0.8809)
WebShell Attack (TeaStore): MADGuard detected edges is slightly higher, TGAT’s Precision (0.8916) is significantly
relatedtotheshell.jsp,sql.sh,andmysqldump attacknodes in lower than TGN’s (1.0), with more normal events being mis-
theteastore-webuiserviceenvironment.Theseedgesexhibited judged;intheSockShopinformationleakagescenario,TGN’s
significant reconstruction errors compared to benign edges. Recall reaches 1.0000, fully capturing the low-frequency
Similarly, in the teastore-db service environment, MADGuard sensitive file access behavior in Node.js asynchronous I/O,
identified unusual teadb files and IP information communicat- while TGAT and EvolveGCN’s Recall are 0.8881 and 0.7926,
ing with the webui service. respectively,easilyomittinglocaltemporalanomalies.Overall,
Code Injection (RobotShop): During the attack, the TGN’saverageF1-scoreinthethreescenariosreaches0.9130,
attackergeneratedaccesstoservicemetadataintheRobotShop improving by 3.87% over TGAT (0.8743) and 13.51% over
ratings service, including KernelDevbugContainer.php.meta, EvolveGCN (0.7779), with better balance between Precision
urlmatchingroutes.php.meta, and .htaccess. By identifying and Recall, better meeting the actual needs of microservices
malicious edges associated with these nodes, MADGuard anomaly detection for “low false positives, low false nega-
| traced the malicious | nodes and their | related chain | information | tives.” |     |     |     |     |     |     |     |
| -------------------- | --------------- | ------------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
to reconstruct the entire attack path. Further analysis of the core reasons for the performance
Information Leakage (SockShop): The attacker left differences between models: Although TGAT strengthens the
traces of accessing sensitive files in the front-end service. temporal correlation weights between nodes through temporal
MADGuardidentifiedabnormaledgesrelatedtosensitivefiles attention mechanisms, in microservices scenarios, its atten-
through a reconstruction error and used IDF to assist in iden- tion allocation is easily disturbed by high-frequency normal
tifying abnormal nodes. By tracing the one-hop events related events (such as inter-service heartbeat calls, routine business
totheseabnormaledgesandnodes,MADGuardreconstructed requests)—for example, in the TeaStore WebShell attack, the
the attack path. normal communication frequency between the webui service
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

780 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
|     |     |     |     |     |     |     | F. Ablation | Study    | (RQ4)        |      |             |         |           |          |      |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------------ | ---- | ----------- | ------- | --------- | -------- | ---- |
|     |     |     |     |     |     |     | To verify   |          | the specific |      | roles       | of each | component |          | in   |
|     |     |     |     |     |     |     | MADGuard,   |          | we designed  | an   | ablation    | study   | using     | the      | con- |
|     |     |     |     |     |     |     | trolled     | variable | method,      | with | the results |         | shown     | in Table | XI.  |
Bysystematicallyremovingmodelcomponentsandobserving
changesinperformance,thecorefunctionsofeachcomponent
|     |     |     |     |     |     |     | and their     | impact       | on the         | model’s | effectiveness |     | can     | be     | clearly |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | -------------- | ------- | ------------- | --- | ------- | ------ | ------- |
|     |     |     |     |     |     |     | demonstrated: |              | after removing |         | the Memory    |     | module, | the    | model   |
|     |     |     |     |     |     |     | loses its     | ability      | to dynamically |         | capture       |     | and     | update | node    |
|     |     |     |     |     |     |     | and edge      | information, |                | leading | to confusion  |     | between |        | benign  |
Fig.10. Comparisonofmodelperformanceacrossscenarios. and anomalous event features, and a significant increase
|     |     |     |     |     |     |     | in the          | false positive |         | rate; without |            | the Embedding |        | module,     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ------- | ------------- | ---------- | ------------- | ------ | ----------- | --- |
|     |     |     |     |     |     |     | edge embeddings |                | rely    | on static     | historical |               | node   | information |     |
|     |     |     |     |     |     |     | and fail        | to capture     | dynamic |               | changes    | in            | nodes, | making      | it  |
TABLEXI
COMPARISONOFABLATIONCOMPONENTSPERFORMANCE difficult to distinguish subtle differences in events, leading to
|     |     |     |     |     |     |     | a large         | number    | of false       | positives;      | the         | Encoder        | module,   |               | as the |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | -------------- | --------------- | ----------- | -------------- | --------- | ------------- | ------ |
|     |     |     |     |     |     |     | core integrator |           | of memory      | and             | embeddings, |                | when      | removed,      |        |
|     |     |     |     |     |     |     | causes the      | model     | to lose        | its             | ability     | to dynamically |           | learn         | the    |
|     |     |     |     |     |     |     | evolution       | of graph  | structures,    |                 | resulting   | in             | decreased | precision     |        |
|     |     |     |     |     |     |     | in anomaly      | detection |                | and an          | increased   |                | false     | positive      | rate;  |
|     |     |     |     |     |     |     | and after       | removing  | the            | Decoder         | module,     | the            | model     | is            | unable |
|     |     |     |     |     |     |     | to explore      | long-term | dependencies   |                 |             | between        | nodes,    | and           | since  |
|     |     |     |     |     |     |     | anomalous       | events    | often          | manifest        |             | through        | the       | accumulation  |        |
|     |     |     |     |     |     |     | of long-term    |           | features,      | this ultimately |             | leads          | to        | a significant |        |
|     |     |     |     |     |     |     | increase        | in the    | false negative |                 | rate.       |                |           |               |        |
Inadditiontothesynergisticeffectofthecorecomponents,
|     |     |     |     |     |     |     | the model’s | anomaly |                  | detection        | capability  |         | also      | relies  | on the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------------- | ---------------- | ----------- | ------- | --------- | ------- | ------ |
|     |     |     |     |     |     |     | support     | of a    | multidimensional |                  | information |         | fusion    | mecha-  |        |
|     |     |     |     |     |     |     | nism. Among |         | them,            | Multidimensional |             | message |           | fusion  | has    |
|     |     |     |     |     |     |     | been proven |         | to be a          | core mechanism   |             | for     | effective | anomaly |        |
detection—byintegratingmulti-dimensionalmessagefeatures,
|         |            |           |     |         |                |      | the model’s |         | AUC value         | is  | significantly |               | improved | from        | a       |
| ------- | ---------- | --------- | --- | ------- | -------------- | ---- | ----------- | ------- | ----------------- | --- | ------------- | ------------- | -------- | ----------- | ------- |
|         |            |           |     |         |                |      | baseline    | level   | of 0.5, providing |     | a more        | comprehensive |          |             | feature |
| and the | db service | (50 times | per | second) | is much higher | than |             |         |                   |     |               |               |          |             |         |
|         |            |           |     |         |                |      | basis for   | anomaly | identification.   |     | The           | importance    |          | of Temporal |         |
the malicious data theft frequency (once per second), caus- fusion,however,isscenario-dependent:inWebshelldetection,
| ing TGAT’s | attention | weights | to  | tilt towards | normal | events, |          |        |             |            |     |     |       |            |     |
| ---------- | --------- | ------- | --- | ------------ | ------ | ------- | -------- | ------ | ----------- | ---------- | --- | --- | ----- | ---------- | --- |
|            |           |         |     |              |        |         | temporal | fusion | is crucial, | supporting |     | the | model | to achieve |     |
resulting in decreased sensitivity to low-frequency anoma- a 100% recall rate (although the precision is 29.8%); it also
lies; EvolveGCN relies on fixed-frequency updates (default plays a key role in code injection identification; while the
| every 30 | seconds) | of graph | convolutional |     | kernels | to adapt |             |         |           |     |          |              |     |     |       |
| -------- | -------- | -------- | ------------- | --- | ------- | -------- | ----------- | ------- | --------- | --- | -------- | ------------ | --- | --- | ----- |
|          |          |          |               |     |         |          | information | leakage | detection |     | scenario | demonstrates |     | the | inde- |
to temporal changes, unable to cope with the rapid topology pendence oftemporalpatterns,indicating thatthenecessityof
| adjustments | caused | by microservices |     | dynamic | scaling—when |     |          |        |               |     |       |         |            |     |     |
| ----------- | ------ | ---------------- | --- | ------- | ------------ | --- | -------- | ------ | ------------- | --- | ----- | ------- | ---------- | --- | --- |
|             |        |                  |     |         |              |     | temporal | fusion | is relatively |     | lower | in such | scenarios. |     |     |
SockShop’s frontend service scales from 2 to 5 Pods due to Insummary,MADGuardensuresthecaptureandintegration
traffic fluctuations, EvolveGCN’s kernel updates lag behind of dynamic graph features through its core compo-
| the topology | changes, | leading | to  | broken | cross-service | event |                 |     |      |                    |     |     |         |     |        |
| ------------ | -------- | ------- | --- | ------ | ------------- | ----- | --------------- | --- | ---- | ------------------ | --- | --- | ------- | --- | ------ |
|              |          |         |     |        |               |       | nents, combined |     | with | a multidimensional |     |     | message |     | fusion |
associationsandsignificantperformancedegradation(F1-score and scenario-adaptive temporal fusion mechanism, together
drops by 8.2%). achievingacomprehensiveimprovementinanomalydetection
Incontrast,TGN’sadapteddesignformicroservicescharac-
|     |     |     |     |     |     |     | performance: |     | the core | components |     | address | the | issues | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ---------- | --- | ------- | --- | ------ | --- |
teristics (distributed tracing graph’s mid/podname identifiers, dynamic feature learning and long-term dependency capture,
memory-enhanced node state updates, dynamic time window while the fusion mechanism enhances feature discrimi-
temporal aggregation) effectively avoids the above issues: its nation capability through multi-dimensional and temporal
memory-enhancedmechanismmaintainsthecausaldependen- information, both synergistically supporting the model’s
| cies of long-term |     | cross-service | attacks | (such | as the | 10-minute | effectiveness. |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | ------- | ----- | ------ | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
attack chain temporal modeling in WebShell attacks), and To further verify the model’s long-term adaptability in
the dynamic time window (60 seconds) balances real-time dynamic scenarios, we designed comparative experiments for
performance with event completeness, both working together theOnlineUpdatemechanism.OnegroupwastheMADGuard
tokeepTGN’sstabledetectionperformanceinhighlydynamic without OU, which did not incorporate the OU mechanism,
and cross-service scenarios of microservices, verifying the and we observed the evolution of its performance over
rationality of TGN as the core temporal modeling module. time steps; the other group was the MADGuard with OU,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 781
|     |     |     |     | Fig.12. | TPR,TNR,andFPRfordifferentscenariosandCPUloads. |     |     |
| --- | --- | --- | --- | ------- | ----------------------------------------------- | --- | --- |
Fig.11. F1-ScoreComparisonwithandwithoutOU.
which integrated the OU mechanism, and we analyzed the thelibthriftlibrarydependencyoftherecommenderserviceof
trend of its performance over time. The experimental results the teastore application from version 0.16.0 to 0.20.0, simu-
|         |                 |         |                   | lating business | component | dependency upgrades. | Both types |
| ------- | --------------- | ------- | ----------------- | --------------- | --------- | -------------------- | ---------- |
| (Figure | 11) showed that | without | the OU mechanism, | the             |           |                      |            |
model’s performance degraded significantly over time, with of operations are benign changes without malicious intent but
the F1-score dropping sharply from 96% to 80% within just may cause short-term fluctuations in service communication
|     |     |     |     | patterns | and resource consumption | characteristics, | potentially |
| --- | --- | --- | --- | -------- | ------------------------ | ---------------- | ----------- |
sixtimesteps;afterintroducingtheOUmechanism,themodel
could continuously learn new event patterns, and the F1- interfering with the detection system.
score was essentially stable, maintaining around 96%. This To further simulate the combined effects of load and
indicates that the OU mechanism can effectively overcome configuration changes in a real environment, the experiment
the performance degradation caused by temporal evolution, repeatedtheabovepodupdateoperationsunderdifferentCPU
|     |     |     |     | load pressures: | controlling | the system CPU | load occupancy |
| --- | --- | --- | --- | --------------- | ----------- | -------------- | -------------- |
allowingthemodeltomaintainstableanomalydetectioncapa-
bilities over the long term, and working in conjunction with rate to 40% (light load), 60% (medium load), and 80% (high
core components and fusion mechanisms to jointly enhance load), covering typical load ranges in daily microservices
the lifecycle performance of MADGuard. operations. Through this design, a comprehensive evaluation
|               |             |     |     | of MADGuard’s | stability under    | “configuration | change + load     |
| ------------- | ----------- | --- | --- | ------------- | ------------------ | -------------- | ----------------- |
|               |             |     |     | fluctuation”  | compound scenarios | is possible.   |                   |
| G. Robustness | Experiments |     |     |               |                    |                |                   |
|               |             |     |     | Experiment    | Results (as shown  | in Figure      | 12) indicate that |
In a microservices environment, the dynamic evolution of MADGuard maintained excellent robustness in various syn-
business loads (such as resource consumption changes) and thetic stress environments: for benign behavior changes (such
updates to benign behavior (such as component upgrades) as OS image upgrades, dependency package updates), its true
are common occurrences. These changes can easily be mis- positiverate(TPR)remainedconsistentlyabove90%,ensuring
judged as anomalies by anomaly detection systems, leading effectivedetectionofgenuineanomalies;atthesametime,the
to increased false positive rates or decreased detection accu- false positive rate (FPR) was controlled below 8%, without
racy. To verify the robustness of MADGuard under such generatingalargenumberoffalsealarmsduetoconfiguration
scenarios—namely, its “resistance to interference” against updates or load fluctuations. This performance is attributed to
benignbehaviorchangesanditsstabledetectioncapabilityfor MADGuard’s core technical mechanisms: a sliding window
genuineanomalies—wedesignedsyntheticstressenvironment dynamically capturing the latest baseline of benign behavior,
experiments that closely mimic real-world operational scenar- combined with an online update mechanism to adjust the
ios and evaluated its performance using key metrics such as featuredistributioninreal-time,enablingthemodeltoquickly
TPR(TruePositiveRate),TNR(TrueNegativeRate),andFPR adapt to normal evolution of business, rather than misjudging
| (False Positive | Rate). |     |     | benign | changes as anomalies. |     |     |
| --------------- | ------ | --- | --- | ------ | --------------------- | --- | --- |
Experiment Design focuses on two typical benign dynamic To verify the robustness of MADGuard in cross-
changes in a microservices environment: pod configuration microservices scenarios, we designed a cross-environment
updates and load fluctuations. Regarding pod configuration training-testing experiment: we selected different microser-
updates, we selected common base component upgrade sce- vicesenvironmentsandtrainedthemodelinoneenvironment,
nariosencounteredinmicroservicesoperations:oneisthebase then migrated it to another for testing. Specifically, we set
OSimageupdate,upgradingtheshippingserviceoftherobot- up two groups of experiments: one trained in the robot-
shopapplicationfromDebian10-bustertoDebian11-bullseye, shop environment and tested in the teastore environment; the
simulating version iteration of the underlying operating envi- other trained in the sockshop environment and tested in the
ronment; the other is dependency package updates, upgrading robotshop environment. The experimental results (as shown
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

782 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
|θ|.
Fig.13.
TABLEXII
|     |     |     |     |     |     |     | benign | data (≤3), | which | led | to a | large | number | of benign |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ----- | --- | ---- | ----- | ------ | --------- |
CROSS-ENVIRONMENTTRAININGANDTESTINGRESULTS
|     |     |     |     |     |     |     | data being | misclassified |     | as anomalies. |     | Although | the | AUC was |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ------------- | --- | -------- | --- | ------- |
θ
|     |     |     |     |     |     |     | 0.929, the | false | alarm | rate was | excessively |     | high. When | was |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----- | -------- | ----------- | --- | ---------- | --- |
setto4,thethresholdexceededtheupperlimitofbenigndata,
|          |               |      |          |       |                   |     | causing | some      | abnormal         | data      | to be missed |      | due to   | insufficient |
| -------- | ------------- | ---- | -------- | ----- | ----------------- | --- | ------- | --------- | ---------------- | --------- | ------------ | ---- | -------- | ------------ |
|          |               |      |          |       |                   |     | scores, | resulting | in a significant |           | increase     | in   | the miss | rate and     |
|          |               |      |          |       |                   |     | a sharp | drop in   | AUC              | to 0.700. | However,     | when | θ        | was set to   |
| in Table | XII) indicate | that | although | there | was a performance |     |         |           |                  |           |              |      |          |              |
3,theAUCreachedthehighestvalueof0.996,indicatingthat
| fluctuation | of about        | 1% during    | cross-environment |            |                 | testing, the |                                       |         |           |             |                   |                 |             |        |
| ----------- | --------------- | ------------ | ----------------- | ---------- | --------------- | ------------ | ------------------------------------- | ------- | --------- | ----------- | ----------------- | --------------- | ----------- | ------ |
|             |                 |              |                   |            |                 |              | the model                             | could   | most      | accurately  | distinguish       |                 | between     | benign |
| F1-score    | metric remained |              | consistent        | with       | the performance |              |                                       |         |           |             |                   |                 |             |        |
|             |                 |              |                   |            |                 |              | and abnormal                          |         | events at | this point, | effectively       |                 | controlling | false  |
| of training | and testing     | within       | the               | same       | environment.    | For          |                                       |         |           |             |                   |                 |             |        |
|             |                 |              |                   |            |                 |              | alarmswhileavoidingmisses.Therefore,θ |         |           |             |                   | =3wasdetermined |             |        |
| instance,   | when trained    | in robotshop |                   | and tested | in teastore,    | the          |                                       |         |           |             |                   |                 |             |        |
|             |                 |              |                   |            |                 |              | to be the                             | optimal | threshold | for         | this environment. |                 |             |        |
precisionreached1.0,recallwas0.7923,andtheF1-scorewas
|               |              |             |        |          |           |            | In the    | SockShop | microservice |                   | environment, |        | the | anomaly  |
| ------------- | ------------ | ----------- | ------ | -------- | --------- | ---------- | --------- | -------- | ------------ | ----------------- | ------------ | ------ | --- | -------- |
| 0.8841;       | when trained | in sockshop |        | and      | tested in | robotshop, |           |          |              |                   |              |        |     |          |
|               |              |             |        |          |           |            | scores of | benign   | data         | were concentrated |              | around | 2.  | When the |
| the precision | was 0.8333,  |             | recall | was 1.0, | and the   | F1-score   |           |          |              |                   |              |        |     |          |
θ
|             |                   |     |      |          |     |            | threshold | was | set to | 1 (below | 2), a | large | number | of benign |
| ----------- | ----------------- | --- | ---- | -------- | --- | ---------- | --------- | --- | ------ | -------- | ----- | ----- | ------ | --------- |
| was 0.9090. | This demonstrates |     | that | MADGuard |     | can stably |           |     |        |          |       |       |        |           |
datawasmisclassifiedasanomalies,leadingtoasurgeinfalse
maintaindetectionperformanceincross-microservicessystem
alarmsandanAUCofonly0.729.Whenθwassetto3(above
| scenarios, | fully verifying | its | cross-system |     | robustness | and its |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | ------------ | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
2),someabnormaldataweremissedduetoinsufficientscores,
abilitytoeffectivelyadapttomicroservicesenvironmentswith
|           |                           |     |     |     |     |     | resulting | in a significant |     | increase | in misses |     | and an | AUC drop |
| --------- | ------------------------- | --- | --- | --- | --- | --- | --------- | ---------------- | --- | -------- | --------- | --- | ------ | -------- |
| different | loads and configurations. |     |     |     |     |     |           |                  |     |          |           |     |        |          |
θ
|     |     |     |     |     |     |     | to 0.808. | However, | when      | was        | set to | 2, the  | AUC            | reached the |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ---------- | ------ | ------- | -------------- | ----------- |
|     |     |     |     |     |     |     | highest   | value    | of 0.997, | indicating | the    | optimal | distinguishing |             |
H. Alert Threshold and Sliding Window Optimization ability of the model. Thus, θ = 2 was established as the
In this section, we provide a detailed description of the optimal threshold for this environment.
|              |         |         |     |            |              |     | For the | TeaStore | microservice |     | environment, |     | the | anomaly |
| ------------ | ------- | ------- | --- | ---------- | ------------ | --- | ------- | -------- | ------------ | --- | ------------ | --- | --- | ------- |
| optimization | process | for two | key | parameters | in MADGuard: |     |         |          |              |     |              |     |     |         |
the alert threshold and the sliding window. scores of benign data were also concentrated around 2. When
AlertThreshold Optimization.Duringtheoptimizationof θ was set to 1, the model’s distinguishing ability was close
|     |     |     |     |     |     |     | to random | (AUC | =   | 0.501), | resulting | in  | a large | number |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --- | ------- | --------- | --- | ------- | ------ |
thealertthreshold,wefirstperformedapreliminaryevaluation
θ
usingbenigndatathathadnotbeentrainedon.Thedistribution of misses. When the threshold was set too high (e.g.,
of anomaly scores of benign data was observed to have = 5), the AUC dropped to 0.793, with an increased risk
θ
scenario-specific characteristics across the three microservice of false alarms. However, when was set to 2, the AUC
scenarios. In the RobotShop environment, the anomaly scores reached the highest value of 0.909, indicating that the model
|           |           |              |     |        |          |        | could effectively |     | balance | false | alarms | and | misses. | Therefore, |
| --------- | --------- | ------------ | --- | ------ | -------- | ------ | ----------------- | --- | ------- | ----- | ------ | --- | ------- | ---------- |
| of benign | data were | concentrated |     | within | 3, while | in the |                   |     |         |       |        |     |         |            |
|           |           |              |     |        |          |        | θ =               |     |         |       |        |     |         |            |
SockShopandTeaStoreenvironments,thesescoreswerestable 2 was determined to be the optimal threshold for this
| around | 2. Based on | these observations, |     | we  | set different | alert | environment. |     |     |     |     |     |     |     |
| ------ | ----------- | ------------------- | --- | --- | ------------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(θ)
thresholds within the range of 1 to 5 and evaluated their Sliding Window Optimization. To verify the effectiveness
rationality using the ROC curve and AUC value (a core of the model’s default τ = 1-minute (60s) time window set-
|           |                |         |     |             |         |        | ting,we | compared | theperformance |     | of  | 30s (ashorter |     | window) |
| --------- | -------------- | ------- | --- | ----------- | ------- | ------ | ------- | -------- | -------------- | --- | --- | ------------- | --- | ------- |
| indicator | of the model’s | ability | to  | distinguish | between | benign |         |          |                |     |     |               |     |         |
and abnormal events). The results are shown in Figure 13. and 90s (a longer window) in the RobotShop, SockShop,
In the RobotShop environment, when the threshold θ was and TeaStore microservice environments. We evaluated the
set to 1, it was below the general anomaly score range of impactofwindow lengthondetection performance usingfour
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 783
TABLEXIII
EXPERIMENTALRESULTSOFHASHCODINGDIMENSIONS
Fig.14. |τ|.
core metrics: precision, recall, f1-score, and accuracy. The
TABLEXIV
experimental results are shown in Figure 14.
EXPERIMENTALRESULTSOFPOSITIONCODINGDIMENSIONS
From the trends of the metrics, it was evident that the
shorter30swindowexhibitedsignificantdrawbacksinallthree
environments. Since attackers often exhibit latent behavior
in microservice environments, the features of attack events
are dispersed across multiple short windows, resulting in a
lowerproportionofabnormalfeatureswithinasinglewindow.
The data showed that in the RobotShop environment, the
recall dropped to around 0.6 with the 30s window, while in
the SockShop environment, the recall was less than 0.7. The
composite f1-score was approximately 0.65 in the RobotShop
environment and around 0.7 in the SockShop environment,
both significantly lower than the 60s window level. This microservice benchmarks, while the core model parameters—
indicatesthatthe30swindowispronetomissingkeyabnormal TGN structure, sliding-window τ, and anomaly threshold θ
events due to feature fragmentation. remainunchanged;onlyencoding-relatedvariablesaremanip-
However, the longer 90s window, although capable of ulated.
covering more potential attack event sequences, also included
1) Encoding-Dimension Hyper-Parameter Study: We
too many normal events, resulting in a lower feature purity
determine the optimal dimensions for hash encoding (H) and
within the window. The experimental data showed that in the
positional encoding (P) through two independent-variable
90s window, the precision in all three environments declined.
experiments.Hash-dimension experiment: Fix positional
In the RobotShop environment, the precision dropped to
encoding at 16-D, vary hash dimensions in {8, 16, 32},
around0.8,andintheTeaStoreenvironment,itfellbelow0.75.
and evaluate detection metrics (Precision, Recall, F1-score)
The increased misclassification of normal events as anomalies
together with the hash-collision rate.Positional-dimension
directly led to a lower f1-score in the 90s window compared
experiment: Fix hash encoding at 16-D, vary positional
to the 60s window in all three environments.
dimensionsin{8,16,32},andevaluatedetectionperformance
In contrast, the 60s window demonstrated optimal
plus the completeness of positional information (measured by
performanceacrossallmetrics.IntheRobotShopenvironment,
anomaly-path reconstruction clarity on a 1–5 scale, 5 being
the f1-score reached 0.95, with precision and recall both
best).Tables XIIIandXIVsummarizetheresults.Theoptimal
stable above 0.9. In the SockShop environment, the f1-score
configuration is 16-D for both hash and positional encodings.
was approximately 0.9, with precision and recall maintained
Hash-dimension results: 8-D hash encoding yields a col-
above 0.85. In the TeaStore environment, the f1-score was
lision rate above 20% due to the compact space, confusing
the highest, reaching 0.92. This indicates that a 1-minute
normal and abnormal node features. 32-D hash encoding
window can effectively aggregate the continuous features of
reduces collisions below 9%, but F1-score improves by only
attackeventswhilecontrollingtheexcessivemixingofnormal
0.5%–2%whiledoublingstorageandcomputationcost,offer-
events,fullyadaptingtothelatentnatureandfeaturecontinuity
ing poor cost-effectiveness.Positional-information results:
requirementsofattackbehaviorinmicroserviceenvironments.
16-D positional encoding fully captures node spatial rela-
tionships, achieving the maximum clarity score (5). 8-D
I. Impact of Hash Encoding and Positional Encoding on encoding suffers from insufficient capacity, causing cross-
Model Performance service path discontinuities; 32-D yields no additional gain
To clarify the dimensions of hash and positional encodings, and only increases computational complexity.
the risk of hash collisions, and the stability of the encod- 2) Hash-Collision Risk Analysis: We localize collision
ing scheme when new data types appear, we conduct three sources and quantify their impact in two steps. (1) Collision
targeted experiments to systematically validate the rationality sourcelocalization:Afterdeduplicationoflogsfromthethree
and robustness of our encoding mechanism. All experiments scenarios, we hash all nodes (process paths, file directories,
are carried out on the TeaStore, SockShop, and RobotShop network IPs, etc.) and identify colliding original log entries.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

784 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
|     |     |     | TABLEXV |     |     |     |     |     |     |     | TABLEXVII |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
STATISTICSOFHASHCOLLISIONSOURCES CODINGSTABILITYCOMPARISONUNDERNEWDATATYPES
TABLEXVI
IMPACTOFHASHCOLLISIONSONMODELRECOGNITIONABILITY
|            |           |         |             |       |                |        |             | Section           | IV-D)      | mechanism. | To              | avoid               | affecting      | other      | services, |
| ---------- | --------- | ------- | ----------- | ----- | -------------- | ------ | ----------- | ----------------- | ---------- | ---------- | --------------- | ------------------- | -------------- | ---------- | --------- |
|            |           |         |             |       |                |        |             | the OU            | training   | process    | is encapsulated |                     | and            | executed   | within    |
|            |           |         |             |       |                |        |             | a dedicated       | Docker     | container  |                 | (MADGuard-retrain). |                |            | Inside    |
|            |           |         |             |       |                |        |             | MADGuard-retrain, |            | modules    |                 | for data            | preprocessing, |            | model     |
| Common     | patterns  | are     | analyzed.   |       | (2) Collision  | impact | ver-        |                   |            |            |                 |                     |                |            |           |
|            |           |         |             |       |                |        |             | training,         | and weight | updates    |                 | are pre-installed,  |                | completing | the       |
| ification: | Log       | entries | responsible |       | for collisions |        | are labeled |                   |            |            |                 |                     |                |            |           |
|            |           |         |             |       |                |        |             | model weight      |            | update     | by inputting    |                     | historical     | window     | data      |
| ‘collision | samples.’ | We      | compute     | their | proportion     |        | among nor-  |                   |            |            |                 |                     |                |            |           |
mal and abnormal events, and compare the anomaly-detection and new window data. Once the new model is generated, it
|          |              |         |                   |     |          |         |        | immediately | triggers | a             | containerized |           | deployment         |     | at the ser- |
| -------- | ------------ | ------- | ----------------- | --- | -------- | ------- | ------ | ----------- | -------- | ------------- | ------------- | --------- | ------------------ | --- | ----------- |
| accuracy | of collision |         | vs. non-collision |     | samples. |         |        |             |          |               |               |           |                    |     |             |
|          |              |         |                   |     |          |         |        | vice layer. | The      | model service |               | container | (MADGuard-service) |     |             |
| Tables   | XV           | and XVI | present           | the | results. | Roughly | 80% of |             |          |               |               |           |                    |     |             |
collisions stem from Linux /proc/pid directory accesses: dynamicallyloadsthemodelthroughasharedstoragevolume
|            |         |     |        |           |     |           |          | and initiates | an  | automated |     | verification | process. |     | First, A/B |
| ---------- | ------- | --- | ------ | --------- | --- | --------- | -------- | ------------- | --- | --------- | --- | ------------ | -------- | --- | ---------- |
| the kernel | creates | a   | unique | /proc/pid |     | for every | process; |               |     |           |     |              |          |     |            |
logs differ only in PID, causing high structural similarity and testing is conducted in a shadow environment, comparing the
|          |      |             |           |     |         |         |          | new model’s | anomaly |     | detection | accuracy |     | and false | positive |
| -------- | ---- | ----------- | --------- | --- | ------- | ------- | -------- | ----------- | ------- | --- | --------- | -------- | --- | --------- | -------- |
| frequent | hash | collisions. | Collision |     | samples | account | for less |             |         |     |           |          |     |           |          |
ratewiththeoldmodelunderreal-timelogs.Afterverification,
| than 0.5% | of  | abnormal | events, | and | the | anomaly-detection |     |     |     |     |     |     |     |     |     |
| --------- | --- | -------- | ------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accuracy difference between collision and non-collision sam- a canary deployment is performed, using Tertagon to route
|     |     |     |     |     |     |     |     | 5% of production |     | logs | to the | new version | container, |     | while the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- | ------ | ----------- | ---------- | --- | --------- |
plesisbelow0.3%.Thus,/proc/pidlogsareredundantfor
|             |                  |           |      |      |            |        |             | Prometheus    | monitoring |             | module     | collects | performance    |          | metrics |
| ----------- | ---------------- | --------- | ---- | ---- | ---------- | ------ | ----------- | ------------- | ---------- | ----------- | ---------- | -------- | -------------- | -------- | ------- |
| anomaly     | discrimination,  |           | and  | hash | collisions | do not | impair the  |               |            |             |            |          |                |          |         |
|             |                  |           |      |      |            |        |             | in real-time. |            | If key      | business   | metrics  | (false         | positive | rate    |
| model’s     | core capability. |           |      |      |            |        |             |               |            |             |            |          |                |          |         |
|             |                  |           |      |      |            |        |             | threshold)    | do         | not exhibit | anomalies, |          | the Kubernetes |          | rolling |
| 3) Encoding |                  | Stability | With | New  | Data       | Types: | To simulate |               |            |             |            |          |                |          |         |
production scenarios in which new data types emerge, we update strategy is initiated, gradually replacing old version
|            |               |          |           |      |     |        |             | containers | until | full coverage |     | is achieved. |     |     |     |
| ---------- | ------------- | -------- | --------- | ---- | --- | ------ | ----------- | ---------- | ----- | ------------- | --- | ------------ | --- | --- | --- |
| design     | the following |          | protocol: | (1)  | Add | new    | data types: |            |       |               |     |              |     |     |     |
| We augment | the           | original | logs      | with | two | common | production  |            |       |               |     |              |     |     |     |
sources—container-resource monitoring logs (memory usage, VI. DISCUSSION
| container | start/stop |         | events) | and microservice |           | API-call | logs  |            |          |            |     |                 |     |         |           |
| --------- | ---------- | ------- | ------- | ---------------- | --------- | -------- | ----- | ---------- | -------- | ---------- | --- | --------------- | --- | ------- | --------- |
|           |            |         |         |                  |           |          |       | Generality |          | Challenges |     | of Microservice |     |         | Anomaly   |
| (response | time,      | success | rate).  | (2)              | Stability | metrics: | Using |            |          |            |     |                 |     |         |           |
|           |            |         |         |                  |           |          |       | Detection  | Systems. | Existing   |     | microservice    |     | anomaly | detection |
+
| the existing | 16-D    | hash |         | positional | encodings   |     | without any |              |              |         |     |        |            |                |           |
| ------------ | ------- | ---- | ------- | ---------- | ----------- | --- | ----------- | ------------ | ------------ | ------- | --- | ------ | ---------- | -------------- | --------- |
|              |         |      |         |            |             |     |             | methods      | typically    | require |     | model  | retraining | for            | different |
| parameter    | tuning, | we   | compare | model      | performance |     | (Precision, |              |              |         |     |        |            |                |           |
|              |         |      |         |            |             |     |             | microservice | environments |         | to  | ensure | accurate   | identification |           |
Recall,F1-score)between‘originalonly’and‘original+new
|               |             |     |     |             |        |     |           | of abnormal    |     | events. | With      | the widespread |     | adoption | of     |
| ------------- | ----------- | --- | --- | ----------- | ------ | --- | --------- | -------------- | --- | ------- | --------- | -------------- | --- | -------- | ------ |
| data’ inputs. | Performance |     |     | fluctuation | within | 2%  | is deemed |                |     |         |           |                |     |          |        |
|               |             |     |     |             |        |     |           | microservices, |     | diverse | operation | modes          | are | employed | across |
stable.
|     |     |     |     |     |     |     |     | various | microservice | systems, |     | and | system | log | information |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | -------- | --- | --- | ------ | --- | ----------- |
Table XVIIshowsresults.Afteraddingbothnewdatatypes,
|              |        |         |      |           |      |                |          | also varies. | This         | necessitates |     | training | models       | from | scratch for  |
| ------------ | ------ | ------- | ---- | --------- | ---- | -------------- | -------- | ------------ | ------------ | ------------ | --- | -------- | ------------ | ---- | ------------ |
| F1-score     | varies | by less | than | 0.7%,     | with | no significant | drop     |              |              |              |     |          |              |      |              |
|              |        |         |      |           |      |                |          | different    | microservice | systems,     |     | making   | it difficult |      | for existing |
| in Precision | or     | Recall. | This | indicates | that | the 16-D       | encoding |              |              |              |     |          |              |      |              |
|              |        |         |      |           |      |                |          | anomaly      | detection    | models       | to  | achieve  | the “compile |      | once, run    |
schemedoesnotrelyonpriorknowledgeofspecificdatatypes.
|          |          |            |     |                  |     |     |             | everywhere” | goal.   |               |     |            |     |        |          |
| -------- | -------- | ---------- | --- | ---------------- | --- | --- | ----------- | ----------- | ------- | ------------- | --- | ---------- | --- | ------ | -------- |
| The hash | function | compresses |     | high-dimensional |     |     | features of |             |         |               |     |            |     |        |          |
|          |          |            |     |                  |     |     |             | Public      | Dataset | Availability. |     | Currently, |     | in the | field of |
newdataintoa16-Dvectorviauniformmapping,whileposi- microservice anomaly detection, public datasets either do not
| tional encoding        |     | supplements |           | structural |           | information    | through |           |         |             |      |            |        |         |           |
| ---------------------- | --- | ----------- | --------- | ---------- | --------- | -------------- | ------- | --------- | ------- | ----------- | ---- | ---------- | ------ | ------- | --------- |
|                        |     |             |           |            |           |                |         | exist or  | contain | only benign |      | data [40], | which  | lack    | practical |
| spatial relationships, |     |             | requiring | no         | re-tuning | to accommodate |         |           |         |             |      |            |        |         |           |
|                        |     |             |           |            |           |                |         | reference | value.  | The lack    | of a | unified    | public | dataset | makes it  |
new data types.
|     |     |     |     |     |     |     |     | difficult | to evaluate | and      | compare | the | performance |     | of different |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | -------- | ------- | --- | ----------- | --- | ------------ |
|     |     |     |     |     |     |     |     | anomaly   | detection   | methods. |         |     |             |     |              |
J. Deployment Concept Drift. Concept drift is a common problem in
MADGuard is deployed in a continuous delivery environ- machine learning models [41], [42]. With the evolution of
ment using containerization, with Tertagon collecting event microservice systems, new components or services continue
stream information in real-time. When the real-time event to appear, and anomaly detection models may misidentify
stream detection results deviate from the historical base- new normal patterns as anomalies, resulting in false positives.
line, the system automatically triggers continuous integration Usually,thewaytosolvethisproblemistoupdatethetraining
tools (such as CircleCI) to initiate the Online Update (OU data set and retrain the anomaly detection model. Although
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 785
the anomaly detection system proposed in this paper can external attacks and struggle to effectively identify and trace
update the detection model efficiently, it becomes impractical attack paths.
to update the model manually over time. Therefore, how to
realizetheautomaticupdateofanomalydetectionmodelisan
important challenge.
VII. RELATEDWORK
Ensuring the Integrity of Logs. The log sources of our Contemporary microservice anomaly detection strategies
system are based on Tetragon, a Kubernetes observation tool fall into three primary categories.
builtoneBPFtechnology.ThecoreadvantageofTetragonlies Unsupervised approaches [20], [21], [22], [52] analyze
in its ability to dynamically insert and remove probes directly systemcallpatternsthroughfrequencythresholdsandsequen-
inthekernelspace,whichgreatlyreducesthelatencyandrisk tial context modeling. Early implementations focused on call
ofloglossthatmaybeintroducedbytraditionallogcollection frequency metrics but evolved to incorporate graphical repre-
methods.However,wefullyunderstandthechallengesthatlog sentations of call sequences and deep learning architectures,
integrity may face in real-world environments. In response to enhancing contextual awareness. However, these methods
theissueoflogloss,existingresearchprimarilyfocusesonlog remain vulnerable to “normal drift” as system behaviors
compressiontechniques,includinglosslessandlossycompres- gradually diverge from initial training baselines. Existing
sion [36], [43], [44], [45]. Lossless compression technology Federated Learning-based Anomaly Detection methods
reduces the size of log data by identifying and eliminating (e.g.,MT-FL[13],FL-IDS[53])focusondetectinganomalies
redundant information within it, having minimal impact on withinmicroservices.Theyemploytechniqueslikedistributed
the performance of subsequent anomaly detection models training combined with multi-task learning and feature fusion
based on log sequences. Lossy compression techniques, in to identify internal anomalies such as network latency and
pursuit of higher compression ratios or processing efficiency, packet loss. While they excel in privacy preservation and
actively discard some log data that is considered to have distributed collaboration, they struggle to characterize cross-
lowervalueorhigherredundancy.Thismethodofcompression servicecausaldependencies.Consequently,theyareineffective
can affect the performance of anomaly detection models to against external attackers exploiting internal vulnerabilities to
varying degrees, depending on the amount and strategy of launch cross-service attacks and information leakage attacks.
the discarded log data. We plan to focus on and test the Untrained detection methods circumvent model training
robustness of our anomaly detection model under different through comparative analysis of service replica behav-
types and degrees of log loss in future research, and explore iors [23], [54], [55]. By tracking ten operational features
the integration of lossless compression technology to enhance related to system calls, files, and processes, these techniques
detection efficiency. calculate Jaccard similarity metrics across time intervals to
Zero-day/Unknown Anomaly Detection. Zero-day and identify deviations. While eliminating training overhead, they
unknown anomalies represent emerging patterns of mali- sufferfromlimitedfeaturecorrelationanalysisanddependence
cious behavior that do not yet have established signatures on manual feature engineering.
or labeled datasets. Traditional security systems, which rely Rule-basedsystemsemploypredefinedsecuritypatternsfor
on predefined rules and signature databases, are inherently network activity, file access, and system calls [56], [57], [58].
limited in their ability to detect such novel threats [46], Though initially effective, their static nature conflicts with
[47]. MADGuard, however, is designed to operate without microservices’ dynamic architecture, requiring labor-intensive
the need for prior knowledge of attack patterns. It is trained rule updates and generating excessive false positives that
on benign data and employs edge reconstruction errors to overwhelm security teams. Each paradigm presents distinct
identify behaviors that deviate from the norm. This approach trade-offs between detection granularity, adaptability, and
is particularly well-suited for the detection of unknown or operational sustainability. Tracee [59] leans towards low-
zero-day anomalies, as it does not rely on pre-existing attack overheadcollectionofsystemcallsandeventdata.Whileitcan
signatures. beintegratedwithanomalydetectionsystems,itlacksintrinsic
Limitations of Existing Distributed Tracing causal analysis capabilities and cannot directly support attack
Technologies. In response to the challenges of large-scale path tracing.Deep Learning Tools for Kubernetes (e.g.,
distributed systems, Google has developed large-scale tracing KubAnom, DevGraph [60]) leverage the integration of Large
tools such as Dapper [48]. Widely adopted, Dapper has Language Models (LLMs) to achieve automated anomaly
given rise to a range of derivative tools, including Zipkin, detection, enhancing capability by incorporating microservice
Jaeger, osprofiler, and opentracing. Building on these tracing topology graphs. However, these methods depend on mas-
tools, researchers have designed intelligent anomaly detection sive natural language corpora and significant computational
solutions for microservices in spatiotemporal and edge resources, creating technical barriers for small and medium-
computing environments [49], [50], [51]. However, existing sized enterprises (SMEs). Furthermore, these deep learning
tracing tools (such as Dapper) primarily focus on data tools do not integrate system-level data such as kernel logs,
at the application layer of microservices (e.g., API call limitingtheirscopeandmakingitdifficulttocoverunderlying
chains, latency information) and are unable to capture the resourceanomalies.Theexistingmicroservicesanomalydetec-
characteristics of external attackers targeting microservices tionsystems have been summarized fromthree major aspects:
(for instance, the malicious file sql.sh in a WebShell attack). detectiontechnology,deploymentoverhead,andforensiccapa-
As a result, these tools are limited in their ability to detect bility (Table XVIII).
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

786 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
TABLEXVIII
COMPARISONOFDETECTIONMETHODS
VIII. CONCLUSION [7] M. S. Haq, T. D. Nguyen, A. S. Tosun, F. Vollmer, T. Korkmaz,
andA.-R.Sadeghi,‘‘SoK:Acomprehensiveanalysisandevaluationof
| This | study | presents | a   | provenance |     | graph-based | detec- |     |     |     |     |     |     |     |     |
| ---- | ----- | -------- | --- | ---------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
dockercontainerattackanddefensemechanisms,”inProc.IEEESymp.
| tion system | addressing |     | microservice |     | anomaly |     | identification |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------------ | --- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
SecurityPrivacy(SP),2024,pp.4573–4590.
[8] Y.Heetal,“Crosscontainerattacks:ThebewilderedeBPFonclouds,”
| through  | three key | innovations: |       | multi-dimensional |     |           | data fusion, |          |      |        |          |       |         |            |       |
| -------- | --------- | ------------ | ----- | ----------------- | --- | --------- | ------------ | -------- | ---- | ------ | -------- | ----- | ------- | ---------- | ----- |
|          |           |              |       |                   |     |           |              | in Proc. | 32nd | USENIX | Security | Symp. | (USENIX | Security), | 2023, |
| temporal | graph     | networks     | (TGN) |                   | for | causality | modeling,    |          |      |        |          |       |         |            |       |
pp.5971–5988.
| and an | automated | forensic |     | analysis | module. |     | Experimental |     |     |     |     |     |     |     |     |
| ------ | --------- | -------- | --- | -------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[9] V.S.DeviPriya,S.C.Sethuraman,andM.K.Khan,“Containersecu-
evaluations demonstrate superior detection accuracy (15.07% rity:Precautionlevels,mitigationstrategies,andresearchperspectives,”
improvement over baselines) across diverse microservice con- Comput.Security,vol.135,Dec.2023,Art.no.103490.
|     |     |     |     |     |     |     |     | [10] R. Feng, | Z.  | Yan, S. Peng, | and | Y. Zhang, | “Automated |     | detection of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | --------- | ---------- | --- | ------------ |
figurations. The integrated forensic component enables full password leakage from public Github repositories,” in Proc. 44th Int.
attack chain reconstruction, significantly advancing incident Conf.Softw.Eng.,2022,pp.175–186.
investigation capabilities. [11] Q. Y. Zeng, M. Kavousi, Y. H. Luo, L. Jin, and Y. Chen, “Full-stack
|          |            |     |       |             |     |         |         | vulnerability |     | analysis of | the cloud-native |     | platform,” | Comput. | Security, |
| -------- | ---------- | --- | ----- | ----------- | --- | ------- | ------- | ------------- | --- | ----------- | ---------------- | --- | ---------- | ------- | --------- |
| Although | effective, |     | three | limitations |     | warrant | further |               |     |             |                  |     |            |         |           |
vol.129,Jun.2023,Art.no.103173.
| research: | (1) System |     | generalizability |     | across | heterogeneous |     |         |               |      |            |     |        |               |     |
| --------- | ---------- | --- | ---------------- | --- | ------ | ------------- | --- | ------- | ------------- | ---- | ---------- | --- | ------ | ------------- | --- |
|           |            |     |                  |     |        |               |     | [12] A. | Pereira-Vale, | E. B | Fernandez, | R.  | Monge, | H. Astudillo, | and |
cloud platforms requires enhanced architecture-agnostic G.Márquez, “Security in microservice-based systems: A multivocal
|           |         |       |          |       |              |     |         | literature | review,” | Comput. | Security, | vol. | 103, | Apr. 2021, | Art. no. |
| --------- | ------- | ----- | -------- | ----- | ------------ | --- | ------- | ---------- | -------- | ------- | --------- | ---- | ---- | ---------- | -------- |
| modeling; | (2) The | field | urgently | needs | standardized |     | anomaly |            |          |         |           |      |      |            |          |
102200.
| datasets | with labeled | attack | patterns; |     | (3) Concept |     | drift mitiga- |            |      |          |          |     |        |             |        |
| -------- | ------------ | ------ | --------- | --- | ----------- | --- | ------------- | ---------- | ---- | -------- | -------- | --- | ------ | ----------- | ------ |
|          |              |        |           |     |             |     |               | [13] J. F. | Hao, | P. Chen, | J. Chen, | and | X. Li, | “Multi-task | feder- |
tion demands self-adaptive models with automated retraining ated learning-based system anomaly detection and multi-classification
triggers. Future directions should explore federated learning for microservices architecture,” Future Gener. Comput. Syst., 159,
forcross-environmentadaptationandblockchain-baseddataset pp.77–90,Oct.2024.
[14] “Aquasec.”Reverseshell.Accessed:Jul.19,2023.[Online].Available:
sharing frameworks to collectively address these challenges. https://kubernetes.io/
|     |     |     |     |     |     |     |     | [15] O. I. | Alqaisi, | M. S. Haq,     | and | A. S. Tosun, | “Security | of    | containerized |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------------- | --- | ------------ | --------- | ----- | ------------- |
|     |     |     |     |     |     |     |     | computer   | vision   | applications,” |     | in Proc.     | 2nd Int.  | Conf. | Comput. Inf.  |
REFERENCES
Technol.(ICCIT),2022,pp.115–120.
|     |     |     |     |     |     |     |     | [16] Z. | Q. Jian | and L. | Chen, | “A defense | method | against | docker |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ----- | ---------- | ------ | ------- | ------ |
[1] P.DiFrancesc,P.Lago,andI.Malavolta,“Architectingwithmicroser-
vices:Asystematicmappingstudy,”J.Syst.Softw.,vol.150,pp.77–97, escape attack,” in Proc. Int. Conf. Cryptogr. Security Privacy, 2017,
pp.142–146.
Apr.2019.
|     |     |     |     |     |     |     |     | [17] “Secure | Flag.” | Privilege | escalation. |     | Accessed: | Jul. | 19, 2023. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | ----------- | --- | --------- | ---- | --------- |
[2] A.HannousseandS.Yahiouche,“Securingmicroservicesandmicroser-
|      |                |     |            |         |         |         |            | [Online]. | Available: | https://www.aquasec.com/cloud-native-academy/ |     |     |     |     |     |
| ---- | -------------- | --- | ---------- | ------- | ------- | ------- | ---------- | --------- | ---------- | --------------------------------------------- | --- | --- | --- | --- | --- |
| vice | architectures: | A   | systematic | mapping | study,” | Comput. | Sci. Rev., |           |            |                                               |     |     |     |     |     |
cloud-attacks/reverse-shell-attack/
vol.41,Aug.2021,Art.no.100415.
[3] X.Li,Y.Chen,Z.Q.Lin,X.Wang,andJ.H.Chen,“Automaticpolicy [18] X. Gao, Z. Gu, Z. Li, H. Jamjoom, and C. Wang, “Houdini’s escape:
generation for inter-service access control of microservices,” in Proc. Breaking the resource rein of Linux control groups,” in Proc. ACM
USENIXSecuritySymp.USENIXSecuritySymp.,Jan.2021. SIGSACConf.Comput.Commun.Security,2019,pp.1073–1086.
[4] S. S. Li et al., “Understanding and addressing quality attributes of [19] Y.Q.Sun,D.Safford,M.Zohar,D.Pendarakis,Z.Gu,andT.Jaeger,
|               |     |               |     |            |            |          |             | “Security | namespace: | Making |     | Linux security | frameworks |     | available to |
| ------------- | --- | ------------- | --- | ---------- | ---------- | -------- | ----------- | --------- | ---------- | ------ | --- | -------------- | ---------- | --- | ------------ |
| microservices |     | architecture: | A   | systematic | literature | review,” | Inf. Softw. |           |            |        |     |                |            |     |              |
Technol.,vol.131,Mar.2021,Art.no.106449. containers,”inProc.27thUSENIXSecuritySymp.(USENIXSecurity),
[5] Z.Z.Zhang,M.K.Ramanathan,P.Raj,A.Parwal,T.Sherwood,and 2018,pp.1423–1439.
M. Chabbi, “CRISP: Critical path analysis of large-scale microservice [20] Y.H.Lin,O.Tunde-Onadele,andX.H.Gu,“CDL:Classifieddistributed
architectures,”inProc.USENIXAnnu.Tech.Conf.(USENIXATC),2022, learningfordetectingsecurityattacksincontainerizedapplications,”in
pp.655–672. Proc.36thAnnu.Comput.SecurityAppl.Conf.,2020,pp.179–188.
[6] H. Ahmad, C. Treude, M. Wagner, and C. Szabo, “Towards [21] A. S. Abed, C. Clancy, and D. S. Levy, “Intrusion detection system
resource-efficient reactive and proactive auto-scaling for microservice for applications using Linux containers,” in Proc. 11th Int. Workshop
architectures,”J.Syst.Softw.,vol.225,Jul.2025,Art.no.112390. SecurityTrustManag.,2015,pp.123–135.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:MADGuard:AHIGH-PERFORMANCEMICROSERVICEANOMALYDETECTIONSYSTEM 787
[22] A. El Khairi, M. Caselli, C. Knierim, A. Peter, and A. Continella, [47] Y. Guo, “A review of machine learning-based zero-day attack detec-
“Contextualizingsystemcallsincontainersforanomaly-basedintrusion tion: Challenges and future directions,” Comput. Commun., vol. 198,
detection,”inProc.CloudComput.SecurityWorkshop,2022,pp.9–21. pp.175–185,Jan.2023.
[23] A.ElKhairi,M.Caselli,A.Peter,andA.Continella,“Replicawatcher: [48] B. H. Sigelman et al., “Dapper, a large-scale distributed systems
Training-less anomaly detection in containerized microservices,” in tracinginfrastructure,”Google,Inc.,MountainView,CA,USA,Google
Proc.Netw.Distrib.Syst.SecuritySymp.,2024,pp.1–17. Technical Report dapper-2010-1, 2010. [Online]. Available: https://
[24] Z. Y. Li, Q. A. Chen, R. Q. Yang, Y. Chen, and W. Ruan, “Threat static.googleusercontent.com/media/research.google.com/en//archive/
detection and investigation with system-level provenance graphs: A papers/dapper-2010-1.pdf
survey,”Comput.Security,vol.106,Jul.2021,Art.no.102282. [49] Y.Zuo,Y.Wu,G.Min,C.Huang,andK.Pei,“Anintelligentanomaly
[25] M.U.Rehman,H.Ahmadi,andW.U.Hassan,“Flash:Acomprehensive detection scheme for micro-services architectures with temporal and
approach to intrusion detection via provenance graph representa- spatialdataanalysis,”IEEETrans.Cogn.Commun.Netw.,vol.6,no.2,
tion learning,” in Proc. IEEE Symp. Security Privacy (SP), 2024, pp.548–561,Jun.2020.
pp.3552–3570. [50] F. Al-Doghman, N. Moustafa, I. Khalil, N. Sohrabi, Z. Tari, and
[26] W.U.Hassan,A.Bates,andD.Marino,“Tacticalprovenanceanalysis A. Y. Zomaya, “AI-enabled secure microservices in edge computing:
for endpoint detection and response systems,” in Proc. IEEE Symp. Opportunitiesandchallenges,”IEEETrans.ServicesComput.,vol.16,
SecurityPrivacy(SP),2020,pp.1172–1189. no.2,pp.1485–1504,Mar./Apr.2023.
[27] Z.J.Chengetal.,“Kairos:Practicalintrusiondetectionandinvestigation [51] J. Chen et al., “TraceGra: A trace-based anomaly detection for
usingwhole-systemprovenance,”inProc.IEEESymp.SecurityPrivacy microservice using graph deep learning,” Comput. Commun., vol. 204,
(SP),2024,pp.3533–3551. pp.109–117,Apr.2023.
[28] X. T. Chen, H. Irshad, Y. Chen, and V. Yegneswaran, “{CLARION}: [52] S. Jacob, Y. S. Qiao, Y. H. Ye, and B. Lee, “Anomalous distributed
Sound and clear provenance tracking for microservice deployments,” traffic: Detecting cyber security attacks amongst microservices using
in Proc. 30th USENIX Security Symp. (USENIX Security), 2021, graph convolutional networks,” Comput. Security, vol. 118, Jul. 2022,
pp.3989–4006. Art.no.102728.
[29] J. Zengy et al., “ShadeWatcher: Recommendation-guided cyber threat [53] M.Chen,Z.Dai,Y.Li,andZ.Lu,“FedTag:Towardsautomatedattack
analysis using system audit records,” in Proc. IEEE Symp. Security investigationusingfederatedlearning,”inInt.Artif.Intell.Conf.,2023,
Privacy(SP),2022,pp.489–506. pp.112–126.
[30] S. Wang et al., “ThreatRace: Detecting and tracing host-based threats [54] J. Castro, N. Laranjeiro, and M. Vieira, “Exploring logic scoring of
in node level through provenance graph learning,” IEEE Trans. Inf. preference for DoS attack detection in microservice applications,” in
ForensicsSecurity,vol.17,pp.3972–3987,2022. Proc.IEEEInt.Conf.WebServices(ICWS),2023,pp.573–584.
[31] S. Kasinathan, “You’re one misconfiguration away from [55] U. Zdun et al., “Detection strategies for microservice security tactics,”
a cloud-based data breach,” 2020. [Online]. Available: IEEETrans.DependableSecureComput.,vol.21,no.3,pp.1257–1273,
https://community.spiceworks.com/t/youre-one-misconfiguration-away- May/Jun.2024.
from-a-cloud-based-data-breach/760522/2 [56] “Falco: Container native runtime security.” Accessed: 2022. [Online].
[32] C.Warrender,S.Forrest,andB.Pearlmutter,“Detectingintrusionsusing Available:https://falco.org/
system calls: Alternative data models,” in Proc. IEEE Symp. Security [57] X.Gu,Q.Wang,J.Liu,andJ.Wei,“Gruntattack:Exploitingexecution
Privacy,1999,pp.133–145. dependencies in microservices,” in Proc. 54th Annual IEEE/IFIP Int.
[33] Y.Zhang,R.Jin,andZ.-H.Zhou,“Understandingbag-of-wordsmodel: Conf.DependableSyst.Netw.(DSN),2024,pp.115–128.
Astatisticalframework,”Int.J.Mach.Learn.Cybern.,vol.1,pp.43–52, [58] “Twisklock: The most complete container cybersecurity platform,”
Aug.2010. Accessed:2018.[Online].Available:https://www.twistlock.com/
[34] “Kubernetes.”May24,2019.[Online].Available:https://kubernetes.io/ [59] “Tracee:LinuxruntimesecurityandforensicsusingEBPF,”Accessed:
[35] A.K.Jainetal.,“AcontentandURLanalysis-basedefficientapproach 2023.[Online].Available:https://aquasecurity.github.io/tracee/latest/
to detect smishing SMS in intelligent systems,” Int. J. Intell. Syst., [60] “DevGraph,” Accessed: 2022. [Online]. Available: https://www.
vol.37,no.12,pp.11117–11141,2022. devgraph.com/
[36] A.Ibrahim,A.Bozhinoski,andS.Pretschner,“Attackgraphgeneration
formicroservicearchitecture,”inProc.34thACM/SIGAPPSymp.Appl.
Comput.,2019,pp.1235–1242.
[37] J.vonKistowski,S.Eismann,N.Schmitt,A.Bauer,J.Grohmann,and
S.Kounev,“TeaStore:Amicro-servicereferenceapplication,”inProc.
IEEE 4th Int. Workshops Found. Appl. Self* Syst. (FAS* W), 2019,
pp.263–264.
[38] “Sockshop:Amicroservicedemoapplication.”Weaveworks.Accessed: Yanshang Yin received the M.S. degree from
2017. [Online]. Available: https://github.com/microservices-demo/ Zhejiang Gongshang University, Hangzhou, China,
microservices-demo in 2023. She is currently pursuing the Ph.D.
[39] “Tetragon—eBPF-based security observability and runtime enforce- degreeincomputersciencewithZhejiangUniversity
ment,” Cilium, Accessed: Jul. 34, 2023. [Online]. Available: https:// of Technology, Hangzhou. Her research interests
github.com/cilium/tetragon includesystemsecurityandmicroservicesecurity.
[40] J.FloraandN.Antunes,“Evaluatingintrusiondetectionformicroservice
applications: Benchmark, dataset, and case studies,” J. Syst. Softw.,
vol.216,Oct.2024,Art.no.112142.
[41] L. Yang et al., “{CADE}: Detecting and explaining concept drift
samplesforsecurityapplications,”inProc.30thUSENIXSecuritySymp.
(USENIXSecurity),2021,pp.2327–2344.
[42] J.Lu,A.Liu,F.Dong,F.Gu,J.Gama,andG.Zhang,“Learningunder
conceptdrift:Areview,”IEEETrans.Knowl.DataEng.,vol.31,no.12,
pp.2346–2363,Dec.2019.
[43] S. S. Bokade and P. Kulkarni, “A tool for analyzing and detecting
anomalies in unstructured log data,” in Proc. 8th Int. Conf. Comput.
Tiantian Zhu (Member, IEEE) received the
Syst.Inf.Technol.Sustain.Solut.(CSITSS),2024,pp.1–6.
Ph.D. degree in computer science from Zhejiang
[44] X.Y.Li,H.Y.Zhang,V.H.Le,andP.F.Chen,“LogShrink:Effective
University, Hangzhou, China, in 2019. He is cur-
logcompressionbyleveragingcommonalityandvariabilityoflogdata,”
rently an Associate Professor with the College
inProc.46thIEEE/ACMInt.Conf.Softw.Eng.,2024,pp.1–12.
of Computer Science and Technology, Zhejiang
[45] T.Zhuetal.,“General,efficient,andreal-timedatacompactionstrategy
University of Technology, Hangzhou. His research
foraptforensicanalysis,”IEEETrans.Inf.ForensicsSecurity,vol.16,
interests include mobile security, system security,
pp.3312–3325,2021.
andartificialintelligence.
[46] R. Ahmad, I. Alsmadi, W. Alhamdani, and L. Tawalbeh, “Zero-day
attack detection: A systematic literature review,” Artif. Intell. Rev.,
vol.56,no.10,pp.10733–10811,2023.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.

788 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOLUME23,2026
Tieming Chen received the Ph.D. degree in com- Mingqi Lv received the Ph.D. degree in computer
putersoftwareandtheoryfromBeihangUniversity, sciencefromZhejiangUniversity,Hangzhou,China,
Beijing, China, in 2011. He is currently a in2019.HeiscurrentlyanAssociateProfessorwith
Professor with the College of Computer Science the College of Computer Science and Technology,
andTechnology,ZhejiangUniversityofTechnology, Zhejiang University of Technology, Hangzhou. His
Hangzhou, China. His research interests include researchinterestsincludesystemsecurityandartifi-
cyberspacesecurityandintelligencesecurity. cialintelligence.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 23,2026 at 21:14:22 UTC from IEEE Xplore. Restrictions apply.