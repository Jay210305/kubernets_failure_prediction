IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021 3595
Multi-Agent Based Autonomic Network
Management Architecture
Sisay Tadesse Arzo , Member, IEEE, Riccardo Bassoli , Member, IEEE,
Fabrizio Granelli , Senior Member, IEEE, and Frank H. P. Fitzek , Senior Member, IEEE
Abstract—The advent of network softwarization is enabling I. INTRODUCTION
multiple innovative solutions through software-defined
AUTONOMIC networking is the ability of a communica-
networking (SDN) and network function virtualization (NFV).
tion network to self-manage without (or with minimal)
Specifically,networksoftwarizationpavesthewayforautonomic
and intelligent networking, which has gained popularity in human intervention. In other words, it is the process of
the research community. Along with the arrival of 5G and enabling the network system to have a self-X property; X can
beyond,whichinterconnectsbillionsofdevices,thecomplexityof
representmanaging,configuring,healing,andprotectingcapa-
networkmanagementissignificantlyincreasingbothinvestments
bility of the network. An autonomic management system has
and operational costs. Autonomic networking is the creation of
self-organizing, self-managing, and self-protecting networks, to to be able to capture, respond and adapt to the dynamic and
afford the network management complexes and heterogeneous evolving behavior of the network, according to the users’ and
networks. To achieve full network automation, various aspects services’ demands. In general, the primary aim of autonomic
of networking need to be addressed. So, this article proposes a
network management systems is not to completely exclude
novel architecture for the multi-agent-based network automa-
humans from the process. Rather it is aimed at shifting the
tion of the network management system (MANA-NMS). The
architecture rely on network function atomization, which defines burden of routine works, such as maintenance, configuration,
atomic decision-making units. Such units could represent virtual and management, from network administrator to technology,
network functions. These atomic units are autonomous and
alleviating tedious and repetitive tasks.
adaptive.First,thearticlepresentsatheoreticaldiscussionofthe
Traditionally, in the networking community, network man-
challenges arisen by automating the decision-making process.
Next, the proposed multi-agent system is presented along with agement was typically performed either manually or by using
its mathematical modeling. Finally, MANA-NMS architecture is pre-defined scripts to monitor and control software and hard-
mathematically evaluated from functionality, reliability, latency, ware. Those solutions implement pre-defined strategies that
and resource consumption performance perspectives.
are triggered by scenarios defined by the network managers.
Index Terms—Autonomic networking, multi-agent system, Recently, with the introduction of the concept of network
network management, network function virtualization, software softwarization, the capabilities of network management are
defined networking, C-RAN, 5G, future networks.
enhanced by the programmability and adaptability of the
networking infrastructure. However, while modern networks
provide a high level of programmability, still automation in
Manuscript received November 19, 2020; revised January 21, 2021 network management is supported by limited intelligence in
and February 1, 2021; accepted February 13, 2021. Date of publica-
the network.
tion February 16, 2021; date of current version September 9, 2021. This
work has been partially funded by NATO Science for Peace and Security Therefore, in the next generation networks, autonomic
(SPS) Programme in the framework of the project SPS G5428 “Dynamic networking is required to scale up the network management
Architecture based on UAVs Monitoring for Border Security and Safety.”
capability to meet the expected big growth in the network
ThisworkhasalsobeenpartiallyfundedbytheGermanResearchFoundation
(DFG, Deutsche Forschungsgemeinschaft) as part of Germany’s Excellence introducing intelligence in the systems. This is because bil-
Strategy U˝ EXC 2050/1 U˝ Project ID 390696704 U˝ Cluster of Excellence lions of devices will access and use the network. Thus, it
“Centre for Tactile Internet with Human-in-the-Loop” (CeTI) of Technische
will be extremely complex and cumbersome to continue man-
UniversitätDresden.Theassociateeditorcoordinatingthereviewofthisarti-
cleandapprovingitforpublicationwasJ.-M.Kang.(Correspondingauthor: aging future networks with the current practice. Moreover,
SisayTadesseArzo.) fromabusinessperspective,networkoperatorsaimatreducing
Sisay Tadesse Arzo and Fabrizio Granelli are with the Department
capital expenditure (CapEx) and operating expense (OpEx),
of Information Engineering and Computer Science, University of Trento,
38122Trento,Italy(e-mail:sisay.arzo@unitn.it;fabrizio.granelli@unitn.it). while increasing their revenues. Managing next-generation
Riccardo Bassoli is with the Deutsche Telekom Chair of Communication networks would require numerous highly-skilled manpower.
Networks, Institute of Communication Technology, Faculty of Electrical
Especially, with the arrival of the Internet of Things (IoT),
andComputerEngineering,TechnischeUniversitätDresden,01069Dresden,
Germany(e-mail:riccardo.bassoli@tu-dresden.de). andultra-reliablemachine-typecommunication(uMTC),there
FrankH.P.FitzekiswiththeDeutscheTelekomChairofCommunication
is a dramatic increase in the amount of network information
Networks, Institute of Communication Technology, Faculty of Electrical
andComputerEngineering,TechnischeUniversitätDresden,01069Dresden, to actively and proactively process. This requires a com-
Germany, and also with the Centre for Tactile Internet with Human- pletely novel approach to network management. Therefore,
in-the-Loop, Cluster of Excellence, 01067 Dresden, Germany (e-mail:
5G, and beyond networks [1] are trying to address this
frank.fitzek@tu-dresden.de).
DigitalObjectIdentifier10.1109/TNSM.2021.3059752 issuethroughsomeformofnetworkmanagementautomation,
1932-4537(cid:2)c 2021IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

3596 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
alleviating the need for a huge number of skilled human
network administrators.
Current networking researches mostly focus on network
softwarization relying on SDN and NFV. These two emerg-
ing technologies enable the traditional static network to be
flexible paving the way for network innovation. This opens
the door for rapid network evolution and transition to intel-
ligent networking, network automation, and smart networks.
Network softwarization consists of mapping hardware-based
network functions into software.
Moreover, SDN implies the physical separation of the
network control plane from the forwarding data plane [2]. In
the SDN architecture, the controller and the forwarding ele-
ments in the network are decoupled. This allows for a range
of considerably more flexible and effective network manage-
ment solutions using network programming. SDN enables the
network to be programmed and dynamically re-configured,
Fig.1. UnifiedSDN-NFVarchitecturalframework[4].
using software to outsource computing to external servers.
NFV is a software implementation of network function,
which can run on general-purpose hardware [3]. The archi-
tecture of NFV contains three main components, such as ‘monolithic process’ in their implementations. However, in
• Network functions virtualization infrastructure (NFVI) themonolithicprocess,therearestrongdependenciesbetween
consistsofthehardwareandsoftwarethathostsdifferent sub-functions. If one of the function fails, it affects or hinders
virtual network functions (VNFs). the operation of other sub-functions [6], [7]. In addition, a
• VNFs are the implementation of network functions monolithicSDNcontrollerandanNFVNetworkManagement
such as firewall, network address translation (NAT), and Orchestration Architecture (MANO) [3] result to be
and packet/serving-gateway(P/S-G), and baseband unit complex and difficult to scale. This is because a given
(BBU) in software that could be deployed in an NFVI sub-function can not be modified or scaled independently.
environment. Moreover,monolithicimplementationofnetworkmanagement
• NFVmanagementandnetworkorchestration(MANO)is is not flexible, reusable, and scalable for complex systems.
the place where management and orchestration of VNF This makes it unsuitable for network management automa-
are implemented. tion [6], [7]. Sub-system based approach has previously been
SDN and NFV are complementary technologies. Adopting introduced [6], [7]. However, their discussion is limited to
themtogetherprovidedmyriadofinnovativepossibilities,such the sub-system creation and distributed deployment. They are
as dynamic network configurations, network states estimation limited in the introduction of intelligence in the sub-systems.
andmeasurementanddynamicnetworkmanagementandcon- Given the above open challenges, this article proposes
trol. They are enablers of network automation through the a MANA-NMS architecture. The core principle behind this
softwarization and orchestration of network functions. A uni- architecture is network function division based on autonomic
fied architecture for SDN-NFV, which is presented in [4] is agents. The idea is to subdivide the monolithic network man-
depicted in Figure 1. agement and control function into sub-functions. It employs
Another enabling technology for network automation is agents to be implemented in a virtualized or containerized
machine learning (ML)/artificial intelligence (AI), which has environments [8], [9]. A given sub-function is deployed as
recentlyseengreateradvancements.Thisisexpectedtoplaya an independent autonomous unit, called agent. Each agent is
significant roleintheautomation ofnetworks [5].Infact,ML autonomous and specialized in performing specific network
hasbeenappliedinvariousareasofnetworkingsuchastraffic sub-functions, such as network slicing, path computation,
prediction, resource management, Quality-of-Service (QoS), and QoS monitoring. Agents are organized to perform the
and network security. ML provides cognition and reasoning overall network management functionalities. Next, agents
capability in automated decision making. The goal of ML is could be orchestrated with standard orchestration such as
toextractthehiddenknowledgefromthenetwork,service,and Kubernetes. However, orchestration could also be consid-
users’behaviorusinghistoricdataforitstrainingandlearning. ered as a sub-function to be implemented as an atomic
SDN and NFV enable the possibility of network pro- agent.
gramming, virtualization, and orchestration; however, they Specifically, the overall system behavior and functions
do not actually automate network management. Therefore, should be represented, using multiple interacting autonomous
a new framework should be developed to incorporate SDN agents. This requires a new architecture that defines the
(fornetworkcontrolandprogrammability),NFV(fornetwork interaction, functionality, communication, and coordination
functionvirtualizationandorchestration),andML(forknowl- betweentheagentsindeliveringtheoverallsystemfunctional-
edge management and cognitive ability) in a single archi- ity.Ingeneral,theoverallsystembehaviorneedstoencompass
tecture. Moreover, the current architectures typically use a differentattributessuchasagentcommunication,coordination
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3597
strategies, decision making, learning, and cognition, in stan- 1) Autonomic Networking Before the Introduction of SDN
dard architecture. and NFV: Autonomic computing and networking were first
In this article, we follow European Telecommunication envisioned by IBM in 2001 [14]. Inspired by autonomic com-
Standards Institution (ETSI) standard’s called Generic puting, numerous research works had been done in autonomic
Autonomic Network Architecture (GANA) reference networking since 2004 [15]–[19]. Some works also specif-
model [10]. The main goal of the GANA reference model is ically focused on network management [18], [20]. In [18],
toprescribethedesignandoperationalprinciplesforDecision the author proposed a system for autonomic network control
Elements (DEs) as the drivers for cognitive, self-managing, and management. In [20], the authors presented an interesting
and self-adaptive network behaviors. ETSI is performing approach to enable the self-X capability for network man-
several GANA instantiations onto various targeted standard- agement. An early study of autonomic network architecture
ized reference network architectures, to enable autonomic is discussed in [21]–[23]. In particular, Bouabene et al. [22]
algorithm implementation and to design and implement DEs aimed at designing a generic architecture by introducing the
in such architectures, in a standardized way. Our proposed concept of abstraction. The main idea behind abstraction is
autonomic architecture is presented in comparison with the to provide a platform for the coexistence of heterogeneous
ETSI’s GANA reference model. The authors had already networking styles and protocols. In [23], the authors intro-
proposed a general architecture for autonomic network man- duced an architecture called AutoXL. It adopts a knowledge
agement (in terms of the autonomic operator) in [11], [12]. plane (responsible for the management of knowledge) and a
Moreover, they also described and extensively evaluated the Policy plane, (responsible for managing policies). The study
self-management of a virtual network based on SDN, via in [21] focuses on developing autonomic network monitor-
the exploitation of adapted fuzzy cognitive maps at the SDN ing for decision-making through information gathering, using
controller [13]. a random number of monitoring devices. The work in [24]
The main contributions of this article can be summarized developed a specific network architecture for cognitive radio
| as follows: |     |     |     |     |     |     | nodes. |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
• Discussingthechallengesofautonomicdecision,consid- There are also other specific network-based autonomic
ering decision generation, organization, planning, valida- architectures and conceptual models. The works in [25], [26]
tion,andexecutioninthecontextofnetworkmanagement mainly targeted transport networks. The authors in [25]
automation. presentedadiscussiononanattempttoenableself-optimizing
• Defining and proposing multi-agent-based autonomic and self-protecting optical burst-switched networks. Similarly,
network architecture. in [26] a model was developed using self-configuration, self-
• Mathematical modeling of the autonomic network man- optimization, self-healing, and self-protection for service pro-
agement system behavior. visioning in automatically switched transport networks. The
• Performance evaluation in terms of functionality and developedarchitectureaimedatenablingautonomiccapability
| system | behavior | analysis. |     |     |     |     | through | self-governing |     | systems. |     |     |     |
| ------ | -------- | --------- | --- | --- | --- | --- | ------- | -------------- | --- | -------- | --- | --- | --- |
The rest of the paper is organized as follows. Section II Autonomic networking models for wireless networks are
reviews existing works. Section III discusses the auto- also a relatively well-studied subject [27]–[32]. A specific
nomic network management challenges. The proposed multi- work that focuses on wireless access networks, is presented
agent-based autonomic management system is presented in in [33]. Specifically, it developed a distributed generic and
Section IV. Next, the mathematical formulation of this multi- autonomic management paradigm for decentralized manage-
agent system is discussed in Section V. Section VI presents mentofwirelessaccessnetworks.Consideringthepeculiarand
a performance evaluation as a proof of concept. Finally, con- inherentchallengesofwirelessnetworking,theauthorsin[27]
cludingremarksandfutureresearchdirectionsareprovidedin provided an analysis of autonomic networking. In particular,
Section VII. they aimed at providing autonomic support in the wireless
|     |     |     |     |     |     |     | network  | design process. |     |          |             |     |                |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | -------- | ----------- | --- | -------------- |
|     |     |     |     |     |     |     | In [29], | the idea        | of  | function | atomization |     | was presented. |
II. LITERATUREREVIEW
|            |             |               |         |             |                |      | Moreover, | a consideration |       | of   | composing   | autonomic | elements         |
| ---------- | ----------- | ------------- | ------- | ----------- | -------------- | ---- | --------- | --------------- | ----- | ---- | ----------- | --------- | ---------------- |
| Automation | is          | not a new     | subject | since       | it was applied | in   |           |                 |       |      |             |           |                  |
|            |             |               |         |             |                |      | was the   | scope in        | [30]. | This | composition |           | aimed at provid- |
| several    | fields such | as industrial |         | automation, | business       | pro- |           |                 |       |      |             |           |                  |
ingaself-governingmanagementsystemforoverlaynetworks
cessautomation,andvehicular-drivingautomation.Forclarity,
|           |        |                |     |          |                  |     | and a self-organizing |     | composition |     | towards | autonomic | overlay |
| --------- | ------ | -------------- | --- | -------- | ---------------- | --- | --------------------- | --- | ----------- | --- | ------- | --------- | ------- |
| we mainly | divide | the literature |     | into two | main categories: |     |                       |     |             |     |         |           |         |
networks.
| network      | automation     | and | architecture, | and | the application | of  |             |                    |        |            |         |                 |                |
| ------------ | -------------- | --- | ------------- | --- | --------------- | --- | ----------- | ------------------ | ------ | ---------- | ------- | --------------- | -------------- |
|              |                |     |               |     |                 |     | As per      | the authors’       |        | knowledge, | the     | work            | in [31] showed |
| multi-agents | in networking. |     |               |     |                 |     |             |                    |        |            |         |                 |                |
|              |                |     |               |     |                 |     | the first   | use of agent-based |        | modeling   |         | for automated   | elements.      |
|              |                |     |               |     |                 |     | The authors | argued             | the    | use of     | network | management      | automa-        |
| A. Autonomic | Networking     |     |               |     |                 |     |             |                    |        |            |         |                 |                |
|              |                |     |               |     |                 |     | tion for    | wireless           | sensor | networks   | as      | a self-recovery | model.         |
Autonomics in communication networks can be reviewed An interesting conceptual contribution could be extracted
considering state-of-the-art before and after softwarization. In from the above works, which is network element atomiza-
fact, SDN and NVF along with cloud computing created a tion. This provides the possibility of sub-dividing monolithic
seismic change in the way we design, implement, operate and network management systems into sub-units. The mono-
manage networks. lithic network management design has drawbacks such as
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3598 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
reusability, scalability, tight coupling between components. the introduction of self-aware adaptive techniques combined
Similarly,withafocusonaparticularnetworktype,fewworks with reasoning and learning mechanisms. The goal of these
attempted to incorporate autonomic in the network operation techniques is to tackle inefficiency and guarantee satisfac-
and management [32], [34]–[36]. tory performance in complex and dynamic scenarios. In [13],
Apart from an application on particular network scenarios, the author proposes a cognitive SDN architecture based on
there are also works focusing on automating specific func- fuzzycognitivemaps.Aspecificdesignmodificationsoffuzzy
tionalities such as QoS monitoring, fault-management, traffic cognitive maps are proposed to overcome some well-known
management, and security [37]–[43]. For instance, in [37], issues of this learning paradigm. The authors also discussed
a discussion on a model-based approach is presented. The the efficient integration with an SDN architecture.
model-based method is to equip the fault-management system Significant standardization efforts are also taking place
withautonomiccapabilities.Article[38]studiedautomationof by prominent standardization organizations such as ETSI
networkoperationsforfault-managementandresilience,while and Internet Research Task Force (IRTF). The first project
the article in [41] analyzed a memory-enabled autonomic launched to develop a network automation model is
resilient networking. Autonomic Network Architecture (ANA) [22]. The project
2) AutonomicNetworkingAftertheWidespreadAdoptionof aimed at designing an autonomic architecture to mitigate
SDN and NFV: SDN and NFV introduced a dramatic change network complexity enabling protocols and algorithms to
in the legacy static network, paving the way for network operate in an autonomic manner. Recently, ETSI has taken
software-basedevaluation.Fromanarchitecturepointofview, a prominent role in autonomic architecture standardization
SDN provides centralized network provisioning and manage- and adaptation. An Industry Specification Group (ISG) on
ment capability, considering a global view of the network. Autonomic network engineering for the self-managing Future
Now, we focus on the most recent literature on autonomic Internet (AFI) has been established under ETSI [56]. Various
networksthathavebeendonesincethewidespreadacceptance versions of this model were presented since its incep-
of SDN and NFV. tion [10], [57], [58]. More recently, ETSI developed an auto-
Ironically, after the introduction of SDN and NFV, there nomic network standard reference architecture [10], which is
arerelativelyfeworganizedeffortsintheresearchcommunity called GANA. In [59], SDN enablers in the ETSI AFI GANA
for network automation [10], [44]–[47]. In [48], an experi- Reference Model for Autonomic Management & Control
mental study on dynamic network reconfiguration in a virtu- (emerging standard), and Virtualization impact.
alized network environment, using autonomic management, is In [60], an implementation guide for the ETSI AFI GANA
discussed. An autonomic management system for a software- modelispresentedconsideringastandardizedreferencemodel
enabled network is also presented in [45]. The article in [49] for autonomic networking, cognitive networking, and self-
presented a novel management architecture and elaborated management. The document in [61] provides standardization
the ongoing standardization efforts. Most of the concepts in ofresilience&survivabilityandautonomicfault-management,
the reference model, autonomic networking integrated model in future networks: this is an ongoing initiative recently
and approach (ANIMA) are heavily inspired by GANA archi- launched in ETSI. As per the authors’ knowledge, despite the
tecture [10]. This architecture for IPv6 based radio access tremendous effort to introduce an autonomic architecture and
network (RAN) management. More recently, in [50], the softwaremodel,noneoftheworkshavegivenenoughempha-
authors presented a demonstration of an open-source MANO sis on the concept of function atomization. Network function
framework, an extension within the scope of the 5GTANGO atomization and multi-agent-based representation of atomized
H2020project.Theydiscussedautomatedservicedeployment, functionsarethecorecontributionofourwork.Networkfunc-
considering policy-based service level agreement (SLA) pro- tion atomization is the sub-division of the monolithic process
visioning and monitoring. Richard et al. [51] discussed a data into smaller functions with cognitive and adaptive capability.
and knowledge-driven intelligent network for future network Withthisaddedautonomiccapability,sub-functionsarerepre-
transformation. In [52], a first attempt to integrate SDN and sentedasautonomicagents.Autonomicagentsareatomicunits
autonomic network management was presented. This white that will be used as building blocks for autonomous network
paper shows the challenges and opportunities along with the management systems.
autonomous network framework. An SDN-based autonomic Finally,thedawnofIoTandmachine-typecommunications
architecture was envisioned in [53]. This architecture aims at has dramatically increased the network size and complex-
enabling the coexistence of heterogeneous virtual networks, ity [62]. 5G and Beyond networks are evolving towards
supporting hierarchical autonomic management. In [54], the autonomic.
authors introduced an architectural framework to be inte-
grated with the network device operating system. It can work
B. Multi-Agent Systems for Autonomic Networking
eitherindependentlyonthedeviceorcanbeaggregatedacross
multiple devices in a network deployment. Now, we present a brief overview of the part of the litera-
Inspired by the cognition process of human beings, a cog- tureemphasizingtheapplicationofmulti-agent-basedsystems
nitivenetworkimplementsintelligentandadoptiveprocedures in networking. Multi-agent systems have been used in many
in responding to network dynamic behavior. The authors areas [63]–[65]. A multi-agent-based configuration in a ubiq-
in [55] presented an evolutionary road-map of communica- uitouswirelessnetworkispresentedin[66].Whereagentsare
tion protocols towards the cognitive internet. They discussed used in the Radio Access Network (RAN). The information
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3599
| is loaded      | and fed  | back | through | agent           | communication. |           | The       |     |     |     |     |
| -------------- | -------- | ---- | ------- | --------------- | -------------- | --------- | --------- | --- | --- | --- | --- |
| Q-learning     | paradigm | is   | used    | for the agent’s |                | cognitive | ability   |     |     |     |     |
| to identifying | whenever |      | to make | load            | balancing.     | In        | [65], the |     |     |     |     |
authorsproposedtheuseofmulti-agentsystemswithinAuRA-
| NMS. They       | presented   |             | the use      | of multi-agent |      | system          | (MAS)   |     |     |     |     |
| --------------- | ----------- | ----------- | ------------ | -------------- | ---- | --------------- | ------- | --- | --- | --- | --- |
| technology      | for         | distributed | system       | automation     |      | and             | network |     |     |     |     |
| control,        | considering | the         | issues       | associated     | with | robustness      | of      |     |     |     |     |
| distributed     | MAS         | platforms,  | the          | arbitration    | of   | different       | con-    |     |     |     |     |
| trol functions, | and         | the         | relationship | between        |      | the ontological |         |     |     |     |     |
requirements.
| Other                   | works focused |             | on more        | specific        | applications |            | such as  |                                  |     |     |     |
| ----------------------- | ------------- | ----------- | -------------- | --------------- | ------------ | ---------- | -------- | -------------------------------- | --- | --- | --- |
| security,               | service       | discovery,  | and            | service         | migration.   | The        | article  |                                  |     |     |     |
| in [67]                 | proposed      | an approach |                | for dynamic     |              | service    | discov-  |                                  |     |     |     |
|                         |               |             |                |                 |              |            |          | Fig.2. Networkmanagementcycle.   |     |     |     |
| ery in service-oriented |               |             | architectures. |                 | The approach |            | is based |                                  |     |     |     |
| on a multi-agent        |               | system      | using          | the matchmaking |              | technique. |          |                                  |     |     |     |
| Patri et                | al. [68]      | developed   |                | a generic       | migration    | algorithm. |          |                                  |     |     |     |
| This algorithm          | is            | derived     | from           | a search-based  |              | rational   | agent    |                                  |     |     |     |
|                         |               |             |                |                 |              |            |          | III. NETWORKMANAGEMENTAUTOMATION |     |     |     |
| decision                | process.      | Such        | an algorithm   |                 | can deal     | with       | uncer-   |                                  |     |     |     |
CHALLENGES
| tainties | to provide | the | migration | path. | This | migration |     | is  |     |     |     |
| -------- | ---------- | --- | --------- | ----- | ---- | --------- | --- | --- | --- | --- | --- |
computed by using a maximized utility function. For mili- Future generation networks are very complex systems with
tary networks of computing and communication, the author numerous heterogeneous devices, users and services involved.
in [69] presented an initial reference architecture. The ref- However, they will be very dynamic and consistently advanc-
erence architecture is a cyber defense application of intel- ing. Thus, managing such a dynamic environment involves
ligent software agents. Several works also exist showing handling heterogeneous real-time events in a sophisticated
the use of intelligent autonomic agents for security appli- manner. This also means dealing with complex events, which
cation such as risk assessment [70], and network intrusion require complex event processing. The problem is mainly
detection [71]. The authors in [72] presented mobility man- complicated because of the huge amount of data generated
agement over the satellite networks based on virtual agent by users, services, and network devices. Managing such an
clustering. amount of data in such a complex environment, within a
None of the previews works considered an organized short period of time, requires a very tedious, enormous, and
management architecture, like in [73]–[75], for the overall sophisticatedprocessing.However,dataalsocontainsvaluable
network system management. These works are closer to our information about users/services and network states even if it
approach towards utilizing agents, hierarchically organized is cumbersome to manage them. Data could systematically be
them into specialized autonomous-atomic units. The work managed and analyzed to extract and use the information for
in [73] presented an attempt to organize a multi-agent hier- self-management of the network. Extracted information could
archical system for a self-adaptive network service. They be used to facilitate services provisioning.
discussed a hierarchical division of agents, effectively pro- To automate a network management system, a comprehen-
viding an abstract model, in which multi-agents are divided sive understanding of the complete cycle of the automation
and organized into principal agents and sub-agents, accord- process is required. This includes measuring and under-
ing to different layers. Each principal agent is responsible for standing the environment, decision-making process, planning
the management and coordination of sub-agents. Similarly, strategy, verification of the action plan, execution of actions,
Taoqing and Xiaoying [73] presented a multi-agent-based and/orfinallymonitoringthesystembehavior[11],asdepicted
| management | system | designed |     | for distributed |     | network. | They | in Figure 2. |     |     |     |
| ---------- | ------ | -------- | --- | --------------- | --- | -------- | ---- | ------------ | --- | --- | --- |
developedanintelligentmanagementarchitecturalframework. • Measuring and understanding the environment deter-
This architecture organizes agents into three types: center mines a network behavior in a reactive or proactive
layer-agent, region-layer agent, and access-layer agent. An manner, based on continuous observation of the con-
interesting work about control systems is presented in [76] stituentnetworkelements.Thisenablestheaccumulation
from the control research community. Several existing works of network knowledge in the knowledge domain. For
related to steady-states of the closed-loop systems studied example, self-monitoring means having the ability to
state analysis of multi-agent-based system [77], [78]. Finally, observe own internal state. Observation of this internal
an article developed a mathematical graph representation of state can be a continuous measurement of QoS metrics
agents’ coordination [79]. such as latency, reliability, congestion, and throughput.
Despite all the effort to develop a specific or general • A decision-making process is used to learn, understand
architecture and several applications of multi-agents, there and decide what action to take to respond to network
is no work considering multi-agents for network manage- events. For example, in a decision-making process, a
ment system automation, combining the concept of SDN, machine learning model could be used to predict the
NFV, and ML in the context of the ETSI GANA reference incomingtraffic,whichistrainedbasedonthepreviously
| model. |     |     |     |     |     |     |     | accumulated | data. Based | on the prediction, | a decision |
| ------ | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------------ | ---------- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3600 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
could be made on the type and quantity of resources to the metaspace, or manipulating and modifying the exist-
required to satisfy the service’s demand. ing instances or models of the metapace. This goes with the
• Planning action strategy means executing the decision, assumptionthattheexistinginstancesarealreadyknown.They
such as what kind of actions or configurations should be couldalreadybeintheknowledgebaseortheycouldbeadded
performed on an element to have the required network via new instances or models. The metaspace and instances
behavior.Forexample,oncethedecisionismadetoallo- constitute a knowledge base of the cognitive process.
cate resources, a configuration file needs to be prepared A domain expert could be considered to provide knowl-
tobeexecutedinnetworkelementsordevices.Thisallo- edge to the knowledge acquisition module. That knowledge is
cates the required network resources, which are decided encoded in the knowledge base, usually as part of the devel-
in the decision-making process. opmentprocess.Theuserordecisionmakerentersthesystem
• Verification of action plan is the validation of the plan through an interface. Next, the user may directly access the
before executing it on the target network elements or knowledge such as a reference for past cases, or the inference
devices. This could be a configuration file, which has engine to infer from past cases to a new case. The user may
to be verified and checked for accuracy and consistency. drill down for an explanation of the inference from the expla-
• Executing action and/or output is implementing the veri- nationmodule.Theintelligentsystemcouldhaveamechanism
fiedorvalidatedactionplan.Itcouldbeapathconfigura- to capture, collect and infer knowledge from a domain expert,
tionfortherequestedserviceorreservationofend-to-end and pass that expertise to a decision-maker.
network resources for service isolation, as part of QoS Generally, decision making is limited by available
provisioning and guaranteeing. informationandtimetomakethedecision,togetherwithcog-
• Monitoring the system’s behavior completes the cycle. It nitiveabilityandresources.Inputtoadecision-makerincludes
continues to analyze the effect of the executed action on a knowledge database and model base. The database contains
theoverallsystembehaviorwhilemonitoringtheenviron- data relevant to the decision problem, while the knowledge
ment for new events and changes. This could be through base may include, for example, guidance in selecting alterna-
a loop-back control. tives. The model base holds formal models, algorithms, and
methodologies for developing outcomes. Processing involves
using decision models to simulate or examine different states
A. Decision Theory From Network Automation Perspectives
and find the best solution under the constraints. Feedback
Decision-making means selecting one or more courses of from processing can provide additional inputs that may be
action among the available alternatives. Humans make deci- updated in real-time to improve problem-solving. The output
sions every day. Humans have characteristics of weighing may generate forecasts and explanations to justify recom-
alternativesanddecidingbasedoncriteriasuchasgoodorbad mendations and offer advice. Results are provided to the
(i.e., quality). Decisions are generally characterized by gath- decision-maker, who may interact with the system to provide
ering knowledge, learning, reasoning, and deciding distinctly. additional information or query the results.
Gathering knowledge is the first step in the decision process. Decisions could be categorized as structured, semi-
Based on the collected knowledge and experience, humans structured or unstructured. An example of a structured deci-
learn and reason. Humans also learn how to respond with- sion is the shortest path between two nodes that could be
out an identifiable reasoning basis, just following instinct. For computed as a closed-form solution. However, if we are to
instance, a child may touch fire just to fulfill his/her curiosity. provide a routing path for a packet or flow, then the short-
However, a reasonable decision is based on previous experi- est path may not be the best decision. It may not consider
ence through pattern-matching. The human decision-making the current state of the network that could affect the routing
process is a long-studied subject in research and it is out of such as congestion and available resources. The current state
the scope of this article. Here, the aim is to get inspired by of the network could be so dynamic that we may not have the
the human decision process to delegate intelligent decisions complete and exact network state information. This leads to a
in network automation. In general, a decision is the key part sub-optimal decision, which is considered semi-structured. In
of network management in the automation of processes. We the unstructured decision, the problems have no agreed-upon
aimtoemulateandreplacehumaninvolvementinthenetwork criteria or solution and rely on the preferences of the decision
management process [80]. making elements.
In a similar analogy with the human decision process, Depending on the time it takes to reach the final deci-
intelligent-decision systems could have a knowledge accumu- sion, decisions can also be categorized as instant decisions
lation step to observe and experience the network environ- and long-term decisions. Examples of instant decisions are
ment through parametric measurements. Besides, intelligent- routing packets or flows from source to destination. Whereas,
decision systems could overcome human cognitive limitations an example of long-term decision is the scheduling of system
and biases by providing a rational basis for comparison of or re-configuring decisions for periodic updates.
alternatives [80]. The observation and experience are accu- In general, taking care of the network without administra-
mulated in a knowledge domain or metaspace. A cognitive tors’consciousknowledgerequiresmakinganintelligentdeci-
process may modify the metaspace and the elements of its sion through decision generation, organization, verification,
instances or models [80]. This could be through a learn- applying, and cheeking system behavior through loop-back
ing process, by adding new rules, principles, and concepts control.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3601
1) DataAnalyticsandCognition: Managingthenetworkis of autonomous decision-making is intelligent reasoning and
the ability of the network administrator or autonomic system cognition that as discussed previously above. That could be
to maintain the network within the desirable behavior. This is supported by AI/ML techniques.
a very complex problem. It requires handling multiple and 3) Decision Organization: Networks systems consist of
complex real-time events such as monitoring the network heterogeneous devices, which involve cross-layer complex-
and computing resources which could be a physical channel events such as signaltransmission,processing, coding, decod-
(wired and wireless channels), encoding techniques, comput- ing,routing,loadbalancing,slicing,QoSmonitoring,resource
ing resources, stored network, and user data, users, service, management. Decisions at various layers have to be made
and network devices (ports, links, configuration files) so on. and each decision has its peculiarities but also dependencies
Reasoning and cognition are the key pillars in a decision- on one another. For example, the decision made to provide
making process. Cognition is learning, analyzing, and rea- end-to-end QoS for a certain type of traffic involves deci-
soning to generate decisions. Useful information could be sions on protocols, the physical layer, the data-link layer, and
generatedaboutusers,services,andnetworksbyanalyzingthe the network layer. Moreover, a decision made at the phys-
data. And then, this information could be used for reasoning ical layer could impact the once’s at the data-link layer or
out and generating management decisions, such as allocating network layer. Hence, abstraction is necessary to isolate and
resources, monitoring and guaranteeing QoS, authenticating focus on particular aspects. Various approaches could be fol-
users, and protecting the network from intruders. lowed. One approach could be using a standard seven-layer
There are various methods to extract information for given OSI or four-layer TCP/IP model. Another one could be using
data.AItoolsprovidepowerfulaidsinsolvingdifficultapplied a new customized version of these layers as followed in
problems that are often real-time, involving large amounts the ETSI GANA model. In our proposed architecture, we
of distributed data, and benefiting from complex reasoning. followed ETSI’s GANA model for decision abstraction and
AI tools could be fuzzy logic, case-based reasoning, evolu- organization [10], [74].
tionary computing, artificial neural networks, and intelligent 4) Overall Autonomic Decision Assessment and
agents [74], [80]. Verification: The outcome of an autonomic decision
Currently, machine learning is the most adopted means should be assessed according to both the process to and
of extracting valuable information about users, services, and outcomeof,decisionmaking.Theprocessofdecisionmaking
networks. With the interconnection of machine type devices, is very critical. And it should be assessed since it has a big
there is a colossal amount of data to learn from. The goal of implication on the time it takes to decide and the additional
machinelearningistoextractthehiddenknowledgeaboutthe computation and communication overhead. The quality of a
network and users through training, using a network data set. final decision is also very important that should be assessed
2) Generating Cumulative Decision: Communication based on a defined criterion, which could be specific for a
networks will be very dynamic and complex. Handling events given management demand. Assessing a decision requires
appropriately to maintain the desired behavior of the network defining measurement matrices.
requires making various intelligent and adaptive decisions. Inthenetworkmanagementautomationprocess,weneedto
Autonomic generation of various decisions through data haveamechanismtovalidatethefinaldecisionforconsistency,
gathering, analysis, and intelligent reasoning are critical accuracy,andoptimality.Thefinaldecision’smeasurementand
steps. These decisions are dependent on various internal verificationmechanismsshouldconsiderconsistencyincollec-
and/or external factors. Events could be triggered by external tivesystembehavior.Thatisbecause,inacumulativedecision,
factorssuchasservicerequests,devicediscovery,newservice individual decisions may not be the best or optimal one,
discovery, topology change discovery, traffic classification, sincemultiplefactorsshouldbetakenintoconsiderations.Itis
traffic prediction (amount of traffic on each link may be importanttomodeldesirednetworkbehaviorpatternforproper
for congestion control), traffic scheduling, fault or anomaly evaluation of the performance of the automation techniques.
behavior detection, and security breach. Internal decisions Typically, healthy network behavior initially is decided by a
could be the network update, scheduled re-configuration for network service provider or network administrator, through a
networkoptimization,availableresourcemonitoring,handling set of behavior constraints.
network device failure or misbehavior. All types involve Verification mechanisms could be a mathematical proce-
complex correlations. For instance, network re-configuration dure to verify and validate intelligent decisions for autonomic
for optimization of decisions may affect the QoS as it may networking. It could be choosing the best solution from a set
involve a configuration that may limit the availability of of, sometimes infinite, possible solutions. This may involve
allocated resources at a given time. The QoS for one service making sense out of ambiguity or contradiction in selecting
may affect the decision for another service, in case of limited thealternatives.Apossiblesimpleexampleofcontradictingor
network resources. conflictingdecisionsinautonomicnetworkmanagementcould
Therefore, in the network automation process, decisions beasecurityalertwithcrediblethreats,suchasaDDoSattack
have to be made considering other interrelated decisions on the network that may require network reconfiguration for
to see the cumulative effect on the overall network behav- self-protection and attack mitigation. However, at the same
ior. Autonomous decision-making requires the generation of time, the network may be serving critical users or verticals
various decisions such as automatic event handling through such as remote surgery or an automated car. An early act on
scheduling of events and tasks. Moreover, the crucial part the intruder could prevent or reduce the damage. However,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

3602 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
the response may require some possible configuration sce- as with other agents. Modularity also helps in reducing
narios, which could impact the critical services. Therefore, network management complexity through the independent
how to solve such conflicting situations has to be defined implementation of sub-units and components. These units are
| or acquired | and | developed | through |     | training, | to be embed- | reusable. |     |     |     |     |     |     |
| ----------- | --- | --------- | ------- | --- | --------- | ------------ | --------- | --- | --- | --- | --- | --- | --- |
ded in the network automation process. Finally, the generated As previously mentioned, we focus mostly on proposing
re-configuration files have to be verified for the impact that general principles and directions to follow for automated
it would have on the network (the accuracy of the intended network management. Moreover, the proposed MANA-NMS
outcome of the actions to be taken). In general, we need to architecture requires to deal with a vast area and numer-
verify and validate the final solution before applying it. And ous challenging topics. Therefore, studying all potential areas
it is beyond the scope of this article to exhaustively discuss and topics including implementation technologies are beyond
the validation and verification mechanisms to each type of the scope of this article. Nevertheless, our article attempts
decision. to investigate the feasibility of the proposed architecture
5) Decision Execution: In network management automa- through mathematical analysis of a preliminary representative
| tion; action | or        | decision | execution     | is needed | to                   | fulfill network | system.        |         |     |     |     |     |     |
| ------------ | --------- | -------- | ------------- | --------- | -------------------- | --------------- | -------------- | ------- | --- | --- | --- | --- | --- |
| management   | demands.  |          | An action     | could     | be re-configuration, |                 |                |         |     |     |     |     |     |
| database     | updating, | path     | re-computing, |           | authentication,      | autho-          |                |         |     |     |     |     |     |
|              |           |          |               |           |                      |                 | A. Multi-Agent | Systems |     |     |     |     |     |
rization,andmonitoring[11].Theoutcomeofdecisiongener-
ation needs to be applied to the system to change the part of Anetworkmanagementsystemisacomplexsystemhaving
the (overall) network system to fulfill service or management multiple events such as multiple-input, multiple-processing,
demands. The network’s behavior change comes by applying and multiple-output or action. We identify that multi-agent
the final verified decision to change the network environment systems are the best candidate in developing such complex,
so that it behaves as per the network management demands. distributed, large-scale heterogeneous systems [64]. In addi-
The response to the change has to be done appropriately and tion to automation, the proposed MANA-NMS architecture
|              |            |                |       |        |          |               | provides modularity, |     | re-usability, | scalability, |     | robustness, | and |
| ------------ | ---------- | -------------- | ----- | ------ | -------- | ------------- | -------------------- | --- | ------------- | ------------ | --- | ----------- | --- |
| timely. This | is         | very critical. | A     | simple | example  | could be when |                      |     |               |              |     |             |     |
| we make      | a decision | to             | route | a flow | based on | the currently | re-configurable.     |     |               |              |     |             |     |
available path. The path status or available resource changes As a set of autonomous entities, agents are capable of per-
very quickly, which may invalidate or outdated the decision. formingagiventaskautonomously.Agentshavethecapability
This is mostly because, in network automation, the aim is to toreplicateasingleormultiplecollaborativedecision-makers.
|         |                 |     |          |     |              |          | In a multi-agent | system, | agents |     | are the | smallest | building |
| ------- | --------------- | --- | -------- | --- | ------------ | -------- | ---------------- | ------- | ------ | --- | ------- | -------- | -------- |
| develop | a context-aware |     | response | to  | the demands. | Decision |                  |         |        |     |         |          |          |
execution as apart of the automated process is also a vast and blocks. The blocks are specialized in performing specific
challenging area that needs to be explored. functions. Using the appropriate set of autonomic agents,
6) Monitoring System Behavior: After implementing the it is possible to build a complete multi-agent system to
final decisions, the network behavior has to be monitored to replace the complex and distributed monolithic systems like
|         |         |        |         |            |          |            | network management |     | systems. | The | constituting |     | autonomic |
| ------- | ------- | ------ | ------- | ---------- | -------- | ---------- | ------------------ | --- | -------- | --- | ------------ | --- | --------- |
| observe | how the | action | affects | the system | behavior | [11]. This |                    |     |          |     |              |     |           |
is to evaluate the applied solution, which could be for consis- agents can communicate, collaborate, cooperate, and coordi-
tency, correctness, and appropriateness. A typical mechanism nate to accomplish complex tasks. In building a multi-agent
that is applied in most automation comes from control the- system, several challenging aspects, such as autonomy, col-
ory, such as loop-back or feedback control. This also requires laboration, activity, reactivity, communicativeness, and goal
|     |     |     |     |     |     |     | setting, have to | be addressed. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------- | --- | --- | --- | --- | --- |
datagatheringanddataprocessingdiscipline,whichcorrelates
data from multiple sources to identify patterns of events that Agents could be distributed to perform distributed tasks
the network is expected to behave. Exploring this from an or assigned to handle different functions in a localized and
autonomic network management perspective is also a critical specialized rule. Or they could be centrally located to per-
research area that needs to be investigated. form the tasks arriving into the central computing or task
|     |     |     |     |     |     |     | performing multi-agents. |             | Agents | could  | also | be homogeneous |            |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ----------- | ------ | ------ | ---- | -------------- | ---------- |
|     |     |     |     |     |     |     | or heterogeneous.        | Homogeneous |        | agents | are  | agents         | with iden- |
IV. MULTI-AGENTBASEDAUTONOMICNETWORK
|     |     |     |     |     |     |     | tical characteristics. |     | They could | be  | designed | or  | instantiated |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ---------- | --- | -------- | --- | ------------ |
MANAGEMENTSYSTEM to perform workload sharing. They could collaboratively per-
MANA-NMS architecture divides the monolithic manage- formlargetasksthatcouldbesub-dividedintosub-taskstobe
mentsystemintosub-functionstobeperformedbyautonomic assigned to different agents. Moreover, agents could also be
multi-agents. It can be considered as a way to organize paral- organized hierarchically [73], [74]. They could be organized
lel computing or task execution, as it includes the division to handle different functionalities.
of a complicated task into several more simple ones. The An example of a multi-agent based system for network
tasks are performed by the group of agents autonomously. automation could be to perform network management func-
In other words, we aim to provide a systems architecture tions.Forexample,someagentscouldbedesignedtomonitor
calledMANA-NMSwhichpartitionsacomplexnetworkman- and analyze the network parameters that are required to pro-
agement system into autonomic units or modules. These vide given services or tasks. Other types of agents could be
autonomic units are atomic units capable of performing tasks designed and dedicated for QoS monitoring for a given type
autonomously while interacting with the environment as well of service. Some other types of agents could be decision aid
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3603
TABLEI
C. Proposed Architecture
MICROSERVICEANDMULTI-AGENTCOMPARISON
Currently, there is no universally accepted definition for
what is an agent. We define every component in the network
management system as agents, in our context. We propose
agents to be implemented with full autonomic capability,
which is derived from agent-design principles. The overall
network management becomes a multi-agent system. In prin-
ciple, agents are assumed to have multiple algorithms such as
cognitive and intelligent algorithms, which could be based on
ML or Deep Learning (DL), computational intelligence, and
other intelligent algorithms. This provides a cognitive abil-
ity for agents in their autonomic operations. In general, the
internal components and specification of agents vary depend-
ing on the functionality and type of tasks or services they are
designed to perform. A specification of a standard agent is
discussed later in Section V.
1) NetworkFunctionsAtomization: Tosubdivideandorga-
nize functions into agents, let us first elaborate the concept
of network function atomization. Network function atomiza-
or classifier or RAN slicer. Each of them is specialized in
tion (atomic agent in our context) is the idea of organizing
performingaspecifictaskasperthedemand.Finally,theover-
autonomic functions at different abstraction level. This with
allsystemcouldrepresentanautomatednetworkmanagement
the obvious reason of separately dealing with each layer.
system.
Functional unit representation is based on autonomic agents.
A multi-agent system has been applied in implement-
The abstraction is based on the GANA model. Network
ing complex software systems [64]. They are capable of
management functions could be physical-layer, device-level,
automating heterogeneous and complex real-time systems.
and network layer functionality. Physical-layer functionality
A network management system is a heterogeneous complex
(low-level atomic actions) could be network resource block
system with real-time and complex environments. Therefore,
(channel) allocation or physical transmission and reception of
we propose that a multi agent system is an effective
frames, error correction, data framing, etc. Device-level func-
approach for the network automation process. However,
tionality could be packet/flow forwarding etc. Network-level
several challenges need to be addressed to exploit the
functionality (high-level atomic actions) could be end-to-end
solutions offered by this approach. This includes deci-
QoS provisioning and monitoring etc. All those functions
sion generation which involves environment monitoring, data
could be provided by autonomic agents with suitable internal
analytic, cognition, complex event processing (CEP), and
components. Since agents represent various functionalities,
context-awareness.
they need to be modeled and categorized accordingly.
In a general category, the types of agents could be service-
type or device-type agents. Alternatively, to align with ETSI
B. Multi-Agents and Microservices GANA model definition of decision units [10], agents could
The industry is heading in the direction of highly decen- be categorized into four types: protocol-level agents, repre-
tralized and loosely-coupled softwarized systems such as dis- senting protocol-level DE, function-level agents representing,
tributed NFV and mobile edge computing (MEC). Currently, function-level DE, device-level agents, representing device-
large-scale software development is based on microservices. levelDE,andnetwork-levelagents,representingnetwork-level
A microservice is a model, in which systems are built from DE.Eachfunctionineachlayercouldberepresentedasagents
small and loosely-coupled services. They have the potential in the proposed architecture. All agents are specialized and
to be a tool for building systems such as network manage- dedicated to performing tasks autonomously while coordinat-
ment systems. They adhere to the Isolated state, Distribution, ing and communicating with other agents. However, we will
Elasticity, Automated management, and Loose (IDEAL) cou- limit the description to only network-level functions. The fol-
pling design principles. Multi-agent systems have many sim- lowingarethemosttypicalnetwork-layerfunctions,thatcould
ilarities with microservices [8], [9]. Their core similarity is be defined as agents:
related to independence and loose-coupling. • Topology Management Agents (TM-AG)
Despite their similarity, agents have an advantage over • Routing Management Agents (RM- AG)
microservices for dynamic network management system’s • Network Slicing Agents (NS-AG)
design.Agentshavetheautonomiccapabilitytoprovidemulti- • Service Function Chaining Agents(SFC-AG)
agents the advantage in building automated systems. Recent • Forwarding Management Agents (FM-AG)
work presented in Collier et al. showed the possibility of • QoS Management Agents (QoS-AG)
combining microservices and multi-agent systems [9]. Table I • Mobility Management Agents (MM-AG)
presents a comparison between microservices and multi-agent • Security Management Agents (SM-AG)
systems. • Fault Management Agents (FM-AG)
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

3604 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
Fig.3. Multi-agentbasedrepresentationofMANA-NMSforcloudRAN.
Fig.4. Simpleexamplefornetworklevelagentrelationship.
| • Resilience |     | and Survivability |     | Agents | (RS-AG) |     |     |     |     |     |     |
| ------------ | --- | ----------------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
• ServiceandApplicationManagementAgents(SAM-AG)
| • Monitoring  |     | Management |     | Agents | (MM-AG)    |     |        |     |     |     |     |
| ------------- | --- | ---------- | --- | ------ | ---------- | --- | ------ | --- | --- | --- | --- |
| • Generalized |     | Control    |     | Plane  | Management |     | Agents |     |     |     |     |
(GCPM-AG)
| Now we              | focus      | on building    | the           | multi-agent-based |                |             | autonomic     |     |     |     |     |
| ------------------- | ---------- | -------------- | ------------- | ----------------- | -------------- | ----------- | ------------- | --- | --- | --- | --- |
| network             | management |                | system.       | Therefore,        |                | by using    | the above     |     |     |     |     |
| atomic units        | as         | a building     | block,        | we                | should         | be          | able to real- |     |     |     |     |
| ize an autonomic    |            | network        | management    |                   | system,        |             | replacing the |     |     |     |     |
| existing            | monolithic | management     |               | system.           |                | Figure      | 3 shows an    |     |     |     |     |
| example             | of a       | multi-agent    | autonomic     |                   | network        |             | management    |     |     |     |     |
| system.             | The figure | also           | shows         | functions’        |                | abstraction | into          |     |     |     |     |
| four layers/levels/ |            | protocol-level |               | agents,           | function-level |             | agents,       |     |     |     |     |
| node-level          | agents,    | and            | network-level |                   | agent.         |             |               |     |     |     |     |
| In the              | process    | of             | building      | the               | autonomic      |             | management    |     |     |     |     |
| system,             | there      | could          | be a          | complex           | relationship   |             | between       |     |     |     |     |
| functions/sub-units |            | that           | should        | clearly           | be             | defined.    | Each func-    |     |     |     |     |
tion performs specific service processing. In doing so, there Fig.5. Multi-agentbasedrepresentationofGANAarchitecture.
| could be    | an interaction |            | of functions |     | or units | to          | accomplish |     |     |     |     |
| ----------- | -------------- | ---------- | ------------ | --- | -------- | ----------- | ---------- | --- | --- | --- | --- |
| the overall | goal           | of service | processing   |     | in       | the network | man-       |     |     |     |     |
agement system. For example, when a given service arrives and they could share information with each other. Moreover,
at the input of the system, it has a set of service constraints therearealsodifferenttypesofagentsthatshouldbeorganized
that have to be satisfied by the system for successful pro- in layers/levels. Figure 5 shows agents’ layers organization
cessing of the service. To perform that the functions or units in the proposed multi-agent-based architecture. The picture
collaborateorcooperateorcompetetosatisfyandperformthe alsodepictsacomparisonbetweentheproposedMANA-NMS
| required | service | processing. |     | This relationship |     | could | be com- |              |               |               |                   |
| -------- | ------- | ----------- | --- | ----------------- | --- | ----- | ------- | ------------ | ------------- | ------------- | ----------------- |
|          |         |             |     |                   |     |       |         | architecture | and ETSI GANA | architecture. | Each agent repre- |
plex in that in satisfying the service constraints, there could sents an atomized network function such as QoS management
be contradictory requirements. This means that for instance function.Agentsareexpectedtoperformtheintendedoriginal
to satisfy the reliability constraints of a given service while functionality of the network components or functional units.
maintaining latency and resource constraints could be a com- Multi-agents should represent all softwarized network com-
plex optimization if we consider the overall system state. An ponents and functions as a system. Using the MANA-NMS
example of the units composition relationship is presented in architecture, agents are categorized as protocol level, function
Figure 4. The overlapping of agents shows the close physical level, node/device level, and network-level agents as depicted
| and/or logical |     | proximity. |     |     |     |     |     | in Figure | 5.  |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
2) Proposed MANA-NMS Architecture in Comparison 3) Proposed MANA-NMS Architecture in Comparison With
With GANA Architecture: As indicated above, agents are SDN-NFV Architecture: As discussed previously, SDN and
used as building blocks, replacing the network function NFV are the enabling technologies for network automa-
to autonomously perform network management functions. tion. The joint architecture is presented in Figure 1. Here,
Agents communicate by passing ACL messages to coordinate we present our proposed architecture in comparison with
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3605
Fig.6. Multi-agent-basednetworkmanagementautomationonunifiedSDN-
NFVarchitecturalframework.
| SDN-NFV          | architecture. |            | Figure       | 6 shows        | a mapping     |            | of the  |     |     |     |     |     |     |
| ---------------- | ------------- | ---------- | ------------ | -------------- | ------------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
| proposed         | architecture  | in         | an SDN-NFV   | based          | architecture. |            | As      |     |     |     |     |     |     |
| it can be        | seen from     | Figure     | 6,           | the management |               | units      | are     |     |     |     |     |     |     |
| built using      | autonomic     | units.     | These        | autonomic      |               | atomic     | units   |     |     |     |     |     |     |
| are organized    | to            | cooperate  | and          | collaborate,   | and           | perform    | the     |     |     |     |     |     |     |
| overall          | network       | management | functions.   |                | Moreover,     | as         | indi-   |     |     |     |     |     |     |
| cated in         | the above     | sections,  | the          | function       | of SDN        | and        | NFV     |     |     |     |     |     |     |
| could themselves |               | be built   | using agents | as             | the building  |            | blocks. |     |     |     |     |     |     |
| Each component   |               | or modules | of           | the SDN        | controller    | could      | be      |     |     |     |     |     |     |
| designed         | as autonomic  | agents.    | And          | the            | overall       | controller | as      |     |     |     |     |     |     |
a multi-agent system. However, a detailed discussion of this Fig.7. Fundamentalcomponentsofautonomicagent.
topicisbeyondthescopeofthisarticleandleftasfuturework.
|     |     |     |     |     |     |     | is a service-request |     | accepting | and/or | environment |     | measur- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --------- | ------ | ----------- | --- | ------- |
V. MATHEMATICALREPRESENTATIONOFMULTI-AGENT
|     |     |     |     |     |     |     | ing points; | FACTS, | are | knowledge | database | of  | the agent; |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --------- | -------- | --- | ---------- |
AUTONOMICNETWORKMANAGEMENTSYSTEM
|     |     |     |     |     |     |     | COGNITION | (REASONING) |     | UNIT | gives | agents | the reason- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ---- | ----- | ------ | ----------- |
We proposed a multi-agent system for network automation. ing capability; PLANNING STRATEGY organizes the steps or
In the system, several agents are organized and coordinated procedures for the action to be taken to satisfy the requested
to perform the network management autonomously, based service; VALIDATION is the unit that verifies the action plan
on underlying control rules, laws, or policies. Developing forconsistency;andanOUTPUT/ACTION isthefinaldecision
multi-agent systems with a certain desired behavior requires (result or action) to be taken by the agent. An agent also has
analyzing the effect of each constituent agents to understand amechanismtocommunicatewithotheragentsthroughagent
thecollectivesystemdynamics.Therearefewsimulationtools communication units. Following the definition of Genesereth,
available in the research, which could be used to analyze in [81], an agent is defined as a software component that is
our MANA-NMS architecture. This is due to the complexity capable of exchanging knowledge and information. We con-
and dynamic nature of the network management environment. sider the standard agent communication language called ACL
Therefore,weusemathematicalmodelingandanalysisforthe messaging[82].ACLprovidesacomplexknowledgeexchange
proposed multi-agent-based automated network management mechanism such as facts, agent’s goal, strategy, and plans.
system to understand the collective multi-agent-based system First, we denote an agent Ag with a characteristic speci-
| behavior. |     |     |     |     |     |     | fication: | Ag = (A | ,A  | ,F,R,PS,V), |     | where | ID is the |
| --------- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- | ----------- | --- | ----- | --------- |
|           |     |     |     |     |     |     |           |         | ID  | type        |     |       |           |
Let us start with characteristic description and specifica- agent’s identification number, A type is its type which could
tion of agents, which are considered as the atomic units be one of the following A |A |A |A |A . A
|     |     |     |     |     |     |     |     |     |     | vh prtcl | fun | nod | ntk vh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------ |
of MANA-NMS. For the sake of simplicity and readability, stands for virtualized or containerized agent type, which rep-
here we characterize an agent with a very general specifica- resents a hardware device such as switches or routers. A
prtcl
tion. As depicted in Figure 7: an agent has an ID, for its standsforprotocol-levelagents.A standsforfunction-level
fun
identification; a TYPE describes agent category; an INPUT, agents. A nod stands for node-level agents. A ntk stands for
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3606 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
The configuration of the system, which is defined by the
occupation vector is given by
(cid:2)M
N = n ×u˜ (2)
k k
j=1
where k is a discrete state with value k = 1, 2, 3 ..., M.
N is the number of agents in state k. The probability distri-
k
bution P(N ,t) is the probability of the system being in the
k
configuration N at time t. u˜ is the associated unit vector to
k
each state. The transition rates for a Markov process, which
is defined by the conditional probabilities, is given by [83]:
P(N ,t +Δt|n˜,t)
W(N |n˜,t)= lim k (3)
k Δt→0 Δt
Fig.8. Agentstates. Theaboveequationdescribesthetransitionstoandfromstates
in the configuration of the system, and it is known as the
Master Equation.
Let w j be the transition rate from state j to state i then the
i
network-level agents. F stands for facts or lists of character-
Rate Equation is given by:
istics parameters that describe agents’ knowledge base, which
∂n (cid:2) (cid:2)
isextendable.TheF listincludesinformationsuchasthetype k = w ((cid:2)N (cid:3))n −(cid:2)n (cid:3)× w ×((cid:2)N (cid:3)) (4)
of provided services and the desired delivery time. R is a
∂t jk k j k kj k
j=1 j=1
reasoning mechanism such as machine learning techniques to
The first term describes an increase in the occupation num-
generate decisions. PS is the action planning strategy such as
bern duetoatransitiontostatekfromotherstates,whilethe
configuration values and procedures to be performed. Finally, k
second term describes the loss due to the transitions from the
V is the validation technique along with the evaluation crite-
statek tootherstates.Thisequationcouldbeusedasatoolto
ria to be used to verify the action plan for consistency and
analyze the collective dynamics of an agent-based system. In
correctness.
simple terms, the rate equation is useful to study the system
Weemployastochasticapproachfortheanalysisandmath-
configuration and evolution in time.
ematical formulation of the multi-agent system behavior [83].
A more useful system equation could be found if we con-
First, let us define a simplified agent states assuming agents
sider agents as queue to model the overall system as M/M/1.
withzeroprobabilityoffailure.Leusassumeanagenthaving
Let us assume the service arriving at the system has a service
four states: start/input, internal execution, action and waiting
as depicted in Figure 8. This is a very general agent’s state
arrival rate (λ tot) and a mean serving rate (μ tot). Therefore,
in formulating the overall system dynamics, we use the over-
definition.Inactualscenarios,eachofthesestatesmayconsist
all system as an input-output system to analyze the resource
ofasinglestate(actionorbehavior),orasetofstates(behav-
and reliability constraint, serving capability, and processing
iors). For instance, when an agent is in the internal execution
latency.
state, it could be performing reasoning, strategy planning,
validation or even communicating with other agent and wait-
A. Service Arrival, Scheduling, and Admission
ing for responses. To find the collective system behavior of
a multi-agent system such as system stability, steady-state, Before presenting the formulation, let us define the incom-
and network equilibrium, we assume the system as Markov ing services to be scheduled for processing in the system. For
process. Agents cannot meet Markov’s property directly since the purpose of prioritizing service scheduling, we character-
they could use the memory of previous actions in decision istically define services. Each characteristic and preference
making. It is commonly right to assume to include the con- is represented D to be the demand set, which defines
i
tents of an agent’s memory as part of its state to maintain the requirements in terms of latency, reliability, processing
the Markov property. Even if this may increase the number of demand (workload), and service class (priority indicator)
states, many types of software agents and sensors do satisfy for that specific application. If the commodity is elastic
the Markov property with a reasonable number of states. D i ={[T ˜ h max ],[τ˜ min ,τ˜ max ],[ρ˜ min ,ρ˜ max ],L ij ,β}. The first
Beforedelvingintothedescription,letusrestatetheMarkov two requirements (latency and reliability) are ranges that
property; the configuration of a given system at time (t+Δt) representservices’Type2andserviceType3,otherwiseinelas-
depends only on the configuration of the system at time t. tic cases which represents service Type 1. The set becomes
Let p(n, t) be the probability of an agent be in state n at D = {c˜,τ˜,ρ˜,β}, with constant first three members. The
i
timet.Withthisassumption,thechangeinprobabilitydensity priority β is a value in the range [0,1], which is used to clas-
is written as [83]: sify the serving priority of the commodity; the sum of all the
priorities is 1.
Based on the priority, services are categorized into three
Δp(n,t)=p(n,t +Δt)−p(n,t) (1) type of services: service Type 1 (inelastic), service Type 2
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3607
(elastic), and service Type 3 (with relaxed latency demand). B. Service Latency in Edge Data Center
In general, service traffic consists of all the three types of
Theoveralldelayinthesystemisthesumofmeandelayin
services. The total service workload composition and propor-
theservingagentsandmeandelayinthequeues.Inthemodel,
tionality equation at a given time is given by
the dependence of service processing and service transmis-
(cid:2)Nt1 (cid:2)Nt2 (cid:2)Nt3 sion between cascaded agents is eliminated by approximating
Srv tot = Srv t1 + Srv t2 + Srv t3 the arrival process of each ïnˇC´ow at the subsequent agents
i=1 i=1 i=1 as a Poisson process. This enables us to employ an M/M/1
=α 1 ×Srv tot +α 2 ×Srv tot +α 3 ×Srv tot (5) queueing model to calculate the average processing latency.
Therefore, the total delay is given by
whereα 1 ×Srv tot,α 2 ×Srv tot andα 3 ×Srv tot referstoType1,
Type 2 and Type 3 services’ workload in GOPS, respectively, (cid:2)K (cid:2)K
N t1, N t2 and N t3 refer to the number services of each type. D tot = Qu D + Ag D (11)
TheoverallserviceadmissionprobabilityofC-RANsystem i=1 i=1
isdefinedastheratiobetweentotaladmittedservicesandtotal
where Qu and Ag are mean delay in the agent and
D D
requested services
mean delay in the service scheduling queue, respectively. The
(cid:3)
Nsrv−Adm ×Srv above equation assumes all the required ordering sequences
Ap = (cid:3) i=1 (cid:3) i (6) ofagents.However,therealapplicationvariesfromserviceto
EDC N i= sr 1 v−adm Sr i + N j= sr 1 v−rej Srv j service,becauseofthepossibilityofsplittingservicesbetween
multiple agents for a faster process of a long single process.
where Ap is the total service admission probability of a
EDC Moreover, to calculate the total delay in passing through
givensystem(EdgeDataCenterinourcase),N srv−Adm isthe
therequiredsequenceofserviceagents,wesumallthedelays
total admitted service workload, N srv−rej is the total rejected
incurred by the given service in the service function chain
service workload.
(SFC),assumingaqueueateachstageoftheAgentsequence.
Let us assume service arrival rate to be Poisson distribute.
This is given by
Using Poisson addition property, the total service arrival rate
(λ tot) at a given time is given by: (cid:2)N 1
N(cid:2)t1 N(cid:2)t2 N(cid:2)t3 τ˜ queue = M ×U −λ (12)
λ tot = λ i + λ j + λ k (7) i=1 sfc Ag
i=1 j=1 k=1 where M
sfc
is the processing capacity of an agent sequence
(thenumberofagenttypesthataservicerequire(N)multiplied
whereN t(1−3)servicegeneratingsources.Weassumethecrit-
by each Agents’ capacity U ), ignoring agents’ CPU (over-
ical determining factor for the system processing capacity is Ag
head) requirements. That means all the allocated capacity of
only dependent on the service processing agents, which are
serviceprocessingagents inthedatacenter wouldbeusedfor
directly involved in service processing. The total serving rate
service processing (without any other processing overhead),
of the system is given by
given by
(cid:2)N (cid:2)M
μ tot = μ ij =N Ag ×U srv (8) M = CPU tot−srv =U ×N (13)
sfc Ag Ag
i=1j=1 N Ag
where N is the types of agents, M is the number of instanti- Therefore, to meet the end-to-end delay for a service that is
ated agents of a given type, N Ag represents the total number constrained to pass through a given sequence of agents, the
of service processing agents that are required for a given ser- data center delay is the sum of SFC decision delay (over-
vice to complete its service cycle. We can calculate the mean head), queuing delay, processing delay at each agent, and
number of services in the system using interconnecting links delay (virtual links) between hosts, so
λ that
ρ tot = μ t t o o t t (9) K(cid:2) link N(cid:2)Ag L N(cid:2)Ag 1
τ˜ = δ + ij + (14)
The agents have finite resources to perform the required Edc i U M ×U −λ
service processing. Hence, we need to consider this in the
i=1 i=1 Ag i=1 sfc Ag
constraint equations. A constraint equation is developed con- where K is the number of links interconnecting different
link
sidering the overall system to have multiple agents, working sequence of agents in the SFC. The above equation shows the
together performing the tasks. Following the M/M/1 queueing total delay at edge data center.
modeling, we can apply Little’s Law, which states that the
incoming rate of services has to be equal to the service rate
C. Data Center Based Multi-Agent System Reliability
to have a stable system with no rejected services. The overall
loadofthesystemmustbeequaltoorlessthantheprocessing Finally, we provide reliability formulation for server and
speed of the overall system. That is given by agents. The overall reliability is calculated by considering
the reliability of server and agents to be mutually indepen-
μ tot ≥λ tot . (10) dent events [84]. A given physical server’s reliability is given
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

3608 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
by [85], [86]
MTBF
ρ˜ = phs (15)
phs MTBF +MTTR
phs phs
where MTBF is mean time between failure, and
phy
MTTRphy is mean time to repair. Similarly, a given Agent’s
reliability is given by [85], [86]
MTBF
ρ˜ = Ag (16)
Ag MTBF +MTTR
Ag Ag
where MTBF is mean time between failure and MTTR
Ag Ag
ismeantimetorepair.Therefore,theoverallreliabilityofedge
data center (EDC) is given by
ρ˜ Edc =[(ΠN i=1 ρ˜ vlink )×(ΠK i=1 ρ˜ phs )×(ΠN i=1 ρ˜ Ag )] (17) Fig.9. Cyclicstepofservicescheduling,processingandmonitoring.
To improve agents reliability, we may need to apply backup
andoverprovisioningofagents.Ifweapplybackupforagents,
data center network that interconnects servers, which contain
the reliability increases. Therefore, the reliability of SFC
memory, CPU, and storage. In the edge data center, multiple
incorporating backup Agents is defined as [87], which is
types of agents could be instantiated to provide different
given by
functions. These functions could be service-traffic workload
ρ˜ Ag−with−backup =ΠN i=1 (1−ΠN i=1 [1−ρ˜ Ag )] (18) prediction, network-state database management, and synchro-
nization,serviceauthenticationandadmission,resourceslicing
The reliability of edge data center considering the data center
and service scheduling, path computation and routing, service
links becomes
QoS monitoring, and security/firewall.
ρ˜
Edc
=[(ΠN i=1Pr
link
)×(ΠK i=1Pr
phs
) The evaluation is performed for a simple case of multiple
types of agents, performing service processing and network
×(ΠN i=1 ρ˜ Ag−with−backup ] (19)
management.Fortheevaluationpurpose,welimitourconsid-
Using these techniques, maximizing reliability increases the eration to only the following type of agents. All of them are
total number of idle agents. Idle agents could be backup network-level agents A ntk .
agents, which are waiting to replace working agents in case • Service workload arrival prediction agents
of failure or waiting to be scheduled in case of sudden and • Event handler and service scheduling agents
unexpectedworkloadspikes.However,thisrequiresadditional • Service-processingagents,performingserviceprocessing
physical servers to be activated. This increases the total cost suchasauthenticationandadmission,routing,QoSmon-
duetopowerconsumptionandcomputingresourceutilization. itoring, and path computation for the arriving services
Therefore,weproposetousebackupagentsforthoseservices • Network state database updates, synchronization and
that requires ultra reliability. In other words, we only use this management agents
technique for Type 1 services. We reserve some number of • Service function chaining and orchestration agents
agents considering the required SFC for Type 1 services. We categorized agents into two main types with the spec-
ification shown in Table II. These two types of agents are
system background service agents and user-traffic processing
VI. PERFORMANCEEVALUATION
agents. Background service agents provide necessary prelim-
This section provides a proof-of-concept for the
inary functions such as service traffic workload prediction,
performanceevaluationoftheproposedmulti-agentautonomic
agents instantiation, and resource allocation, network moni-
networkmanagementsystem,usingMATLABsimulation.We
toring, and service-agents orchestration. Such types of agents
rely on the mathematical formulation presented in Section V.
are assumed to have no direct impact on the service pro-
cessing (e.g., delay). User/traffic/service workload processing
A. System Description and Simulation Environment
agents perform functions that are directly related to handling
Specification
theincomingservices.Thesecouldbepathcomputing,authen-
The simulation environment is aimed at emulating a ticating,admitting,andschedulewhilemonitoringagivenser-
MANA-NMS hosted in a cloud-based edge data center that vice’sQoSrequirementsforprocessingintheedgedatacenter.
autonomically manages a backhaul network and 5G service Figure 9 shows a complete cyclic step of the overall multi-
processing. A depiction of the simulation environment is agent-based autonomic service management and processing
presented in Figure 3. As it can be seen from the figure, there system. The figure shows the steps needed to accomplish the
are three types of 5G services arriving at the edge data center. scheduling, processing, and monitoring tasks for a given ser-
Theseservicesareultra-reliablelow-latencyservices(uMTC), vice. Note that the simulation system is built based on the
machine-type communication (mMTC), and enhanced mobile proposedprinciplesthattheatomicagentsareusedasbuilding
broadband service (xMBB). The figure also shows an edge blocks for the automated network management system.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3609
TABLEII
INTERNAL-FUNCTIONALSPECIFICATIONOFAGENTS
TABLEIII
DETAILEDAGENTSPARAMETRIC-SPECIFICATIONSUSEDINDEVELOPINGTHEOVERALLSIMULATIONSYSTEM
| As discussed |     | above, | one | of the agents |     | is an | event han- |     |     |     |     |     |     |
| ------------ | --- | ------ | --- | ------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
dlerthatrespondstoincomingservicesoranynetwork-related
events.Basedontheevents,itreactsanddispatchestheevents
| (i.e., arrival | of  | tasks, | services, | packets, | network | changes, | etc) |     |     |     |     |     |     |
| -------------- | --- | ------ | --------- | -------- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
toappropriateagentsforeventhandlingandprocessing.There
| are also        | traffic      | prediction | agents,    | which         | predict    | the         | incoming   |     |     |     |     |     |     |
| --------------- | ------------ | ---------- | ---------- | ------------- | ---------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
| service         | workload.    | Based      | on         | the predicted |            | amount      | of work-   |     |     |     |     |     |     |
| load, the       | required     | number     | of         | service       | processing |             | agents are |     |     |     |     |     |     |
| instantiated,   | and          | service    | function   | chains        | (a         | sequence    | of ser-    |     |     |     |     |     |     |
| vice processing |              | agents)    | are        | created.      | In the     | simulation, | this       |     |     |     |     |     |     |
| is performed    | proactively, |            | every      | hour.         | Based      | on the      | predicted  |     |     |     |     |     |     |
| workload,       | additional   |            | agents are | instantiated  |            | if an       | increase   | in  |     |     |     |     |     |
workload is predicted in the next hour compared to the cur- Fig.10. Agentsequencingandschedulingforarrivalserviceprocessing.
| rent period. | Or     | some      | agents | are destroyed | to  | reduce   | and free |     |     |     |     |     |     |
| ------------ | ------ | --------- | ------ | ------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
| edge data    | center | resources | if     | a decrease    | in  | incoming | service  |     |     |     |     |     |     |
workload is predicted. techniques(optional),execution(output),whichareprovidedat
| Depending | on  | the | service | requirements, | the | service | agents |                         |     |        |                |      |            |
| --------- | --- | --- | ------- | ------------- | --- | ------- | ------ | ----------------------- | --- | ------ | -------------- | ---- | ---------- |
|           |     |     |         |               |     |         |        | the agent instantiation |     | stage. | The simulation | only | considered |
are sequenced as a service function chain for a given service ID, capacity, type, and status (busy, idle, or fail). In the agent
topassthroughasapartofserviceprocessing.Weconsidered specification Table II, the agent IDs are given as Ag rvm
|     |     |     |     |     |     |     |     |     |     |     |     |     | s x |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
four service agents as a control plane and data plane func- and Ag b p x. Where srvm indicates service processing type of
tions[88].Sincethedataplaneservicefunctionchainnormally agents,bpindicatesbackgroundprocessingtypeofagentsand
would not span more than a few service agents, the evalua- X, which could take 1, 2, 3, ... N, indicates number used
tion considers chains that are limited in size (four agents). An to identify a specific agent instance from a given category.
exampleofagentsequencingisdepictedinFigure10.Theser- Table III presents all type of agents used in developing the
| vice function | chain | that | we assumed | is  | two | serially | connected |                    |     |              |                      |     |           |
| ------------- | ----- | ---- | ---------- | --- | --- | -------- | --------- | ------------------ | --- | ------------ | -------------------- | --- | --------- |
|               |       |      |            |     |     |          |           | overall simulation |     | system, with | detailed parameters. |     | The table |
agentsworkinginparallelwithanothertwoseriallyconnected also shows different type of agents are instantiated for each
agents, see Figure 10 for agents sequencing (SFC). type of services. These agents are use in creating SFC. Using
Based on agents’ general specification guidelines presented the type of agents indicated in Table III, a simulation of an
in Section V, let us provide the specification of agents to be autonomic network management system is developed.
usedintheevaluation.Agentshaveauniqueidentifiernumber,
|     |     |     |     |     |     |     |     | The network | topology | considered | in the | simulation | is rep- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---------- | ------ | ---------- | ------- |
service capacity, service state (information or facts), adaptive resentedinFigure 11.Thefigure shows aCaliforniaResearch
serving methods (mostly a machine learning model), strategy and Education Network (CalREN), to be used as a backhaul
(how to perform service processing), validation/verification or metro network in the evaluation which aggregate traffics to
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3610 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
TABLEIV
SERVICESPECIFICATION
|     |     |     |     |     | computing     | overhead    |              | is assumed | to          | be added    | as          | a compu- |
| --- | --- | --- | --- | --- | ------------- | ----------- | ------------ | ---------- | ----------- | ----------- | ----------- | -------- |
|     |     |     |     |     | tational      | processing  | workload.    |            | The         | detailed    | study       | of agent |
|     |     |     |     |     | computational | overhead    |              | is left    | as future   | work.       |             |          |
|     |     |     |     |     | In general,   | the         | evaluation   |            | is based    | on          | service     | workload |
|     |     |     |     |     | prediction,   | path        | computation, |            | resource    | allocation, |             | service  |
|     |     |     |     |     | workload      | scheduling, |              | service    | processing, |             | and network | and      |
resourcestateupdates.Servicearrivalsareconsideredasinput
|     |     |     |     |     | to the system | and    | handling      | agents.      |       | The even       | handling | agents     |
| --- | --- | --- | --- | --- | ------------- | ------ | ------------- | ------------ | ----- | -------------- | -------- | ---------- |
|     |     |     |     |     | may request   | the    | orchestration |              | agent | to instantiate |          | and create |
|     |     |     |     |     | a chain of    | agents | for           | the services | to    | be processed.  |          | The chain  |
Fig.11. Considerednetworktopologyforpathcomputation.
|     |     |     |     |     | of agents | represents | a   | service | function | chain | required | by the |
| --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | -------- | ----- | -------- | ------ |
TABLEV services.Thisinfactissetproactivelyeveryhourbypredicting
SIMULATIONPARAMETERS
|     |     |     |     |     | the incoming | service | type     | and     | amount    | of service   |             | workload.  |
| --- | --- | --- | --- | --- | ------------ | ------- | -------- | ------- | --------- | ------------ | ----------- | ---------- |
|     |     |     |     |     | Given        | service | progress | through |           | the sequence |             | of service |
|     |     |     |     |     | processing   | agents  | getting  | the     | necessary | service      | treatments; | it         |
couldbeserviceauthenticationandauthorizationtouseagiven
|     |     |     |     |     | set of resources, |          | SFC           | path, and | service          | management. |          | A snap-    |
| --- | --- | --- | --- | --- | ----------------- | -------- | ------------- | --------- | ---------------- | ----------- | -------- | ---------- |
|     |     |     |     |     | shot of           | agents   | sequencing    | from      | a                | different   | type     | of service |
|     |     |     |     |     | agents is         | provided | in            | Figure    | 10. In           | a given     | type     | of agents, |
|     |     |     |     |     | service agents    |          | are scheduled |           | in a round-robin |             | fashion. | That       |
meansthefirstarrivedserviceisscheduledtobeservedbythe
anedgedatacenter.Thenodesinthetopologyareforwarding first agent from a given set of agents of that type, the second
SDN switches. Aggregate traffic containing multiple types of arriving services by the second agent if the first agent is still
services such as uMTC, mMTC, and xMBB. The weights on busy, and so on. The evaluation is considered to show agents’
the links and nodes are snapshot values indicating the cost of interaction to perform a given service, service schedule, and
| each element. |     |     |     |     | processing. |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
In the evaluation, the fraction of service composition is Arriving services are classified into three categories. And
assumedtobe10:20:70foruMTC,mMTC,andxMBBrespec- each service is scheduled and stored into three separate
tively. This is because there is no representative data to infer queues depending on its service categories. These are uMTC,
the 5G traffic composition. Table IV shows the service ratio mMTC, and xMBB queues. The scheduler allocates separate
and measurement values used in the evaluation. The overall resources and SFCs depending on each queue state. This way
simulation parametric values are presented in Table V. services are scheduled maintaining service separation, prior-
It should be noted that there are important assumptions ity, and service differentiation. The evaluation is considered
madeintheevaluation.Weassumedequalcomputationalover- toshowagents’interactiontoperformagivenservice,service
heads for all service processing types of agents, which may schedule, and processing.
notalwaysbetrue.Itisbecauseagentscouldperformdifferent Generally, based on the above evaluation specifications
computations for each service type. The internal components and developed simulation environment (emulation of MANA-
are designed for the intended function specialization of that NMS), the simulation evaluation is performed for: service
agents. Agents could have event monitoring, cognition, plan- admission and processing, agent utilization and service pro-
ning, verification, and action performing components to make cessing, resource consumption, processing and queuing delay,
autonomic decisions and dynamic responses. These compo- agent and server (agent host) failure analysis, and building a
nents require CPU processing and processing delay, which resilience system and its impact on resource consumption and
can be added to the virtualization overheads (assuming agents processingdelay.Weperformedthesimulationfor120hrs,rep-
are normally instantiated in a given container or virtualized resenting a five days traffic pattern. The results are discussed
| environment).   |                     |            |               |          | in the following |         | subsections. |            |            |     |     |     |
| --------------- | ------------------- | ---------- | ------------- | -------- | ---------------- | ------- | ------------ | ---------- | ---------- | --- | --- | --- |
| Other agents’   | computational       | overhead   | is considered | vari-    |                  |         |              |            |            |     |     |     |
| able, depending | on the type         | of agents. | For instance, | traf-    |                  |         |              |            |            |     |     |     |
|                 |                     |            |               |          | B. Service       | Arrival | and          | Processing | Evaluation |     |     |     |
| fic prediction  | agents are expected | to have    | different     | internal |                  |         |              |            |            |     |     |     |
componentsthandatabasemanagementagentsserviceorches- Arriving services are allocated a network resource after the
tration agents. Therefore, in the evaluation, a given CPU bestavailablepathiscomputed.Theservicescheduleisbased
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3611
Fig.12. Workloaddistribution.
Fig.14. Servicerejection.
Fig.13. Averagearrivingserviceworkload.
Fig.15. Serviceadmissionprobability.
| on service   | priority. It is in | the order of URLLC  | (high prior-     |            |              |          |            |                 |
| ------------ | ------------------ | ------------------- | ---------------- | ---------- | ------------ | -------- | ---------- | --------------- |
| ity) –> mMTC | –> xMBB            | (least priority) in | a given service  |            |              |          |            |                 |
|              |                    |                     |                  | bandwidth. | As indicated | in Table | III, there | is a fixed num- |
| scheduling   | period. Based on   | the amount of       | arriving service |            |              |          |            |                 |
workload, resources are allocated to agents before they are ber of background processing agents. They are instantiated at
instantiated. Based on the total serving capability of agents, the beginning of the simulation. These agents are even han-
a service is injected using the workload percentage shown in dlingagents,serviceworkloadpredictionagents,orchestration
Figure12.Theevaluationalsoconsidersthreetypesofservices agents, and network and resource state database management
agents.Therearealsoserviceagentsthatarescaledaccording
| with a different | workload demand | to the autonomic | network |     |     |     |     |     |
| ---------------- | --------------- | ---------------- | ------- | --- | --- | --- | --- | --- |
management functions. The arrival is assumed to be Poisson totheincomingserviceworkloaddemands.Inoursimulation,
distributed with a workload distribution, shown in Figure 12. weconsideredonlythenumberofagentsthatarescalingwith
The arriving service patter is plotted in Figure showing the the workload. However, it is also possible that a given agent
total average service workload for each type of service and could scale its processing capability according to the service
|             |                   |                 |                   | demands. This | could be | possible | by dynamically | adding the |
| ----------- | ----------------- | --------------- | ----------------- | ------------- | -------- | -------- | -------------- | ---------- |
| the overall | services workload | arriving to the | edge data center. |               |          |          |                |            |
Basedontheavailabilityofserviceagents,servicesaresched- necessary resource to the agent. Such kind of agent’s capacity
uled until all active agents are fully loaded. Figure 13 shows scaling is called “horizontal scaling.” However, the discussion
average arriving service workload over a 120hrs evaluation of such a scenario is out of the scope of this work.
period. Figure 14 shows rejection of services due to agents The number of active agents instantiated at a given time
|               |                 |                       |        | is directly | related to the | service prediction. | Service | workload |
| ------------- | --------------- | --------------------- | ------ | ----------- | -------------- | ------------------- | ------- | -------- |
| overload. The | overall service | admission probability | of the |             |                |                     |         |          |
multi-agent system is calculated as the ratio of service admit- is predicted by the service workload predicting agents. On
ted to service requested. The result is presented in Figure 15. the other hand, the CPU consumption in the edge data center
|     |     |     |     | is directly | related to the | number of | active agents | instantiated |
| --- | --- | --- | --- | ----------- | -------------- | --------- | ------------- | ------------ |
AsitcanbeseenfromtheFigure,serviceadmissionisapprox-
imatelyone during non-peak hours and whereas there issome at a given time. Since active agents consume resources, it is
probability of services rejected at peak hours. necessary to reduce the number of active (but idle) agents
|     |     |     |     | to have efficient | resource    | utilization. | Figure     | 16 depicts the |
| --- | --- | --- | --- | ----------------- | ----------- | ------------ | ---------- | -------------- |
|     |     |     |     | average number    | of required | agents       | in a given | hour. This is  |
C. Agent Utilization and Edge Data Center Resource calculated based on the predicted arriving service workload.
Consumption
Agentsareassignedtoprovideserviceschedulingandmon-
Agents require CPU resources to process services. The itoring functions. Once agents are assigned to accomplish the
instantiatingofmultipleagentsconsumesdatacenterresources given task, they will be locked into a busy (internal execu-
such as memory, storage, CPU, and network bandwidth. In tion)statebeforebecomingtheidlestate.Theaveragenumber
our simulation, we considered only CPU, assuming equiva- of busy agents and idle agent during the 120hrs simulation
lent requirements would be scaled for memory, storage, and period are depicted in Figure 18 and Figure 17. The Figures
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3612 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
Fig.16. Averagenumberofrequiredserviceagents. Fig.19. Agentsutilization.
Fig.17. Averagenumberofidleagents. Fig.20. Edgedatacenterresourceutilization.
|     |     |     |     |     |     | Figure      | 20 shows | the       | average amount  | of      | resource     | consump-    |
| --- | --- | --- | --- | --- | --- | ----------- | -------- | --------- | --------------- | ------- | ------------ | ----------- |
|     |     |     |     |     |     | tion in     | the edge | data      | center in terms | of      | the consumed | CPU.        |
|     |     |     |     |     |     | The maximum |          | available | CPU resource    | in      | GOPS         | is given in |
|     |     |     |     |     |     | Table V.    | As can   | be seen   | from the        | Figure, | the resource | con-        |
sumptionisdirectlyrelatedtothenumberoftotalactiveagents
|     |     |     |     |     |     | which is | also         | directly   | related to the      | service | workload     | arrival |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ---------- | ------------------- | ------- | ------------ | ------- |
|     |     |     |     |     |     | pattern. | As indicated |            | the arrival pattern |         | is predicted | by the  |
|     |     |     |     |     |     | service  | workload     | prediction | agents.             |         |              |         |
Moreover,wehaveevaluatedagents’loadratioover120hrs
|     |     |     |     |     |     | period for | each    | service | type agent. | This           | is an average | busy       |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ----------- | -------------- | ------------- | ---------- |
|     |     |     |     |     |     | period for | a given | type    | of agent.   | The evaluation |               | shows, on  |
|     |     |     |     |     |     | average,   | how     | much a  | given agent | is utilized    | over          | the 120hrs |
Fig.18. Averagenumberofbusyagents. period. This parameter indicates the efficiency of agents in
|     |     |     |     |     |     | processing | and | delivering | the given | service | while | the agents |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --------- | ------- | ----- | ---------- |
indicate the average number of agents that are actively per- are in an active state.
formingserviceprocessingandwaitingforservicescheduling,
|               |          |           |        |            |         | One        | capability | of     | an autonomic   | multi-agents   |     | network |
| ------------- | -------- | --------- | ------ | ---------- | ------- | ---------- | ---------- | ------ | -------------- | -------------- | --- | ------- |
| respectively. | The idle | number of | agents | is a total | average |            |            |        |                |                |     |         |
|               |          |           |        |            |         | management |            | system | is the ability | to communicate |     | between |
over the whole period which is approximately 4000 agents. agents to accomplish a given task. In our evaluation sce-
| This number | indicates         | idle agents | that are | actively consuming |         |                                           |            |     |                     |     |         |            |
| ----------- | ----------------- | ----------- | -------- | ------------------ | ------- | ----------------------------------------- | ---------- | --- | ------------------- | --- | ------- | ---------- |
|             |                   |             |          |                    |         | nario, we                                 | considered |     | agent communication |     | between | schedul-   |
| resources   | without providing | services.   | This     | shows the          | ineffi- |                                           |            |     |                     |     |         |            |
|             |                   |             |          |                    |         | ingandmonitoringagentsandresourcedatabase |            |     |                     |     |         | management |
ciency of resource consumption which is the consequence of agents. Accordingly, the evaluation indicated the communi-
| the prediction | model accuracy. | However, |     | if we reduce | these |                  |     |        |               |     |           |          |
| -------------- | --------------- | -------- | --- | ------------ | ----- | ---------------- | --- | ------ | ------------- | --- | --------- | -------- |
|                |                 |          |     |              |       | cation frequency |     | needed | to accomplish |     | the given | arriving |
idle agents, we may increase the service rejection and ser- serviceworkload.Figure22showstheaveragecommunication
| vice latency    | in the edge       | data center. | This | is because          | the |           |      |         |         |     |     |     |
| --------------- | ----------------- | ------------ | ---- | ------------------- | --- | --------- | ---- | ------- | ------- | --- | --- | --- |
|                 |                   |              |      |                     |     | frequency | over | a 120hr | period. |     |     |     |
| service arrival | is a random       | process      | and  | an exact prediction |     |           |      |         |         |     |     |     |
| is dependent    | on the prediction | model        | used | in the prediction   |     |           |      |         |         |     |     |     |
agents. Moreover, given the model used in the prediction D. Service Queuing and Processing Latency Evaluation
agent, the prediction is the optimal value to avoid further ser- The simulation has two main stages of queuing for each
vicerejectionandservicedelayinthedatacenter.Theoverall typeofservice.Theseareserviceaarrivalqueueandaservice
service-processing-agents utilization by each type of services processing queue. As the services arrive at the edge data cen-
is depicted in Figure 19. ter, they are first stored in the service arrival queue of the
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3613
Fig.21. Agentbusyperiod. Fig.24. Serviceprocessingdelayintheserviceprocessingagents.
Fig.22. Agentsaveragecommunicationfrequencyfordatabaseupdatedue Fig.25. End-to-endservicelatencyinedgedatacenter.
toservicearrival.
E. System Evaluation for Fail-Over Scenarios
In the above evaluation scenarios, agents are assumed to be
100% reliable and available. However, this may not be true
as agents are software components with a non-zero probabil-
ity of failure. The agents are an event handler, orchestration,
prediction agent, and database management. These agents are
very critical for system resilience. Therefore, such agents
are redundant with a well-synchronized backup system. Such
types of agents are fixed in our simulation, and a few are
compared to service processing types of agents. And assumed
to be 100% reliable. However, service processing agents are
Fig.23. Arrivalservicequeuingdelay. assumed to be less reliable and their number is scaled accord-
ing to the arrival service workload. In the simulated system,
corresponding service queue before they are scheduled for such types of agents are not protected by a backup system.
processing in the service agents. Service is processed sequen- However, overpraising of 1% is considered to accommodate
tially through the service function chain. Since we considered the imperfection of the service workload prediction, which is
amaximumoftwoagentsconnectedserially,thereisaservice dependent on the machine learning model incorporated in the
processing queue between the two serial connected service service workload prediction agents.
agents.Inthisscenario,theserviceisscheduledandprocessed Different failure scenarios could be analyzed using the
in the service function chain which is connecting service developed simulation environment. It could be a backhaul
agents.ThesimulationresultdepictedinFigure23presentsthe networknodefailurethataffectsthelinkutilizationandservice
averagedelayinthequeuesforeachtypeofservice.Figure24 admission or server/agent failure which affects the edge data
depicts the average processing delay in service agents passing center service admission probability and service latency. A
throughtheservicefunctionchain.Thetotaldelayintheedge networknodefailureishandledbyrecomputingnewavailable
data center is assumed to be the sum of the two delays as paths until the node is back into operation. This is a classical
formulated in the above section. Figure 25 shows the total scenario thoroughly considered in the literature. We consider
end-to-end latency in the edge data center which ignores the limitedscenariosforthemulti-agent-basedautonomicnetwork
communication link delay between subsequent service agent management system failure. In simulation two fail-over sce-
delay in the SFC. nariosareconsidered;asingleoraveryfewnumbersofagents
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

3614 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
Fig. 26. Impact of server (hosting service processing agents) failure on Fig. 27. Impact of server failure on end-to-end latency in the edge data
| servicerejection. |        |        |              |          |       |           |            | center. |     |     |     |
| ----------------- | ------ | ------ | ------------ | -------- | ----- | --------- | ---------- | ------- | --- | --- | --- |
| failure and       | single | server | failure.     | A single | agent | failure   | has an     |         |     |     |     |
| insignificant     | impact | on     | the overall  | service  |       | admission | and ser-   |         |     |     |     |
| vice delay        | in the | edge   | data center. | This     | is    | because   | agents are |         |     |     |     |
lightweightserviceunitsthatcanbeinstantiatedeasilyandina
| few more            | for overprovisioning, |         |               | with      | littleincrease |          | in resource |         |                                                     |     |     |
| ------------------- | --------------------- | ------- | ------------- | --------- | -------------- | -------- | ----------- | ------- | --------------------------------------------------- | --- | --- |
| consumption.        | They                  | can     | also          | be easily | and            | quickly  | instanti-   |         |                                                     |     |     |
| ated to compensate  |                       | for     | the reduction |           | in the         | number   | of service  |         |                                                     |     |     |
| agents due          | to service            | agent   | failure.      |           |                |          |             |         |                                                     |     |     |
| However,            | the                   | failure | of a          | server,   | hosting        | several  | agents,     |         |                                                     |     |     |
| could significantly |                       | affect  | the           | edge      | data           | center   | processing  |         |                                                     |     |     |
|                     |                       |         |               |           |                |          |             | Fig.28. | Impactofserverfailureonserviceadmissionprobability. |     |     |
| capacity.           | The extent            | of      | the impacts   |           | depends        | on how   | the SFC     |         |                                                     |     |     |
| is created.         | That                  | means   | if a single   | type      | of             | agent is | hosted      | in      |                                                     |     |     |
| a single            | server,               | and if  | that server   | fails,    | the            | impact   | will be the |         |                                                     |     |     |
theadmissionprobabilityforalltypeofservices,dependingon
| highest.   | It is because | a         | given      | service | may            | need to | get service |            |                      |                 |                 |
| ---------- | ------------- | --------- | ---------- | ------- | -------------- | ------- | ----------- | ---------- | -------------------- | --------------- | --------------- |
|            |               |           |            |         |                |         |             | the time   | of failure of server | hosting a given | type of service |
| treatment  | from          | all types | of service |         | processing     | agents  | in the      |            |                      |                 |                 |
|            |               |           |            |         |                |         |             | processing | agents.              |                 |                 |
| SFC. The   | failure       | of such   | server     | would   | significantly  |         | reduce      |            |                      |                 |                 |
| the number | of            | agents    | of a       | given   | type, creating |         | a shortage  |            |                      |                 |                 |
of such agents for SFC creation. The least impact could be F. System Reliability Evaluation and Service Differentiation
|          |            |           |     |                  |     |     |            | for Resource | Efficiency |     |     |
| -------- | ---------- | --------- | --- | ---------------- | --- | --- | ---------- | ------------ | ---------- | --- | --- |
| achieved | by rightly | balancing |     | and distributing |     | the | agent type |              |            |     |     |
to different servers. With such considerations, the simulation Reliability of network management system is very impor-
is performed for maximum impact of hosting a single type of tant. In Section V, we discussed and presented a reliability
agent in a single server. Moreover, a single server failure at improvement technique based on a backup system. We eval-
a random time within the 120hrs simulation period is intro- uate the system performance by introducing backup service
duced. And the impact on service admission probability and processing agents. Figure 30 shows the admission probabil-
service processing latency is evaluated. ity using backup system. Compared to the result obtained
As it can be seen from Figure 26, the impact of a server without backup, which is depicted in Figure 15, the admis-
failure is significant in that it increased the service rejection. sionprobabilityhasincreased.Moreover,Figure29showsthe
However, the impact does not last long because the agent reduction of service rejection compared to the system without
monitoringandorchestratingotheragentsimmediatelydetects back service processing agents, see Figure 29 and Figure 14.
the reduction in the number of service processing, agents and The spike (seen in the figure) in-service rejection is due to
next instantiate additional agents of such type. The instanti- the introduced server failure impacting the available service
ated agents are updated with the service state and information processing agents. This shows that even if we have a backup
to take over the service processing. After instantiating the system, the impact is significant for a small duration. This is
required service processing agents, as a replacement to the because, after the active serving agents’ unexpected sudden
failed agents, the orchestrating agents also create the neces- failure, it needs time until new service agents are instanti-
sary SFC. Figure 27 depicts the overall service latency in the ated and taking over the service processing abandoned by
edge data center. As can be seen from the Figure, there is a the failed agents. Figure 30 shows the admission probability
significantlatencyoneachtypeofserviceprocessing,depend- improvement by using backup system.
ing on the time of failure of the server hosting a given type Figure31showstheincreaseinresourceconsumptioncom-
of service processing agents. Figure 28 shows the impact of pared to Figure 20, which is plotted for the system without
server failure on the service admission probability. As it can backup service processing agents. Since there is a large num-
be observer from the Figure, there are significant reduction in ber of service processing agents, having a backup for all of
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3615
Fig.29. Servicerejectionwithbackupserviceprocessingagents. Fig.32. CPUconsumptionwithbackupsystemforuMTCserviceprocessing
agents.
|     |     |     |     |     |     |     |     |     | VII. CONCLUSIONANDFUTUREWORKS |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
Networksoftwarizationenablesmyriadinnovativepossibili-
ties.Themostimportantinnovationsofnetworksoftwarization
|     |     |     |     |     |     |     |     | are design   | flexibility  |         | and programmability. |           |         | SDN         | and NFV   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ------- | -------------------- | --------- | ------- | ----------- | --------- |
|     |     |     |     |     |     |     |     | architecture | miss         | network | automation.          |           | The     | advancement | and       |
|     |     |     |     |     |     |     |     | explosion    | of machine   |         | learning             | would     | further | enable      | the real- |
|     |     |     |     |     |     |     |     | ization of   | full network |         | automation.          | Autonomic |         | networking  | is        |
becomingthenecessityforfuturenetworks,thatareaimingat
|     |     |     |     |     |     |     |     | interconnecting |               | billions   | of heterogeneous |                  | device,  |              | with strin- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ---------- | ---------------- | ---------------- | -------- | ------------ | ----------- |
|     |     |     |     |     |     |     |     | gent services’  | requirements. |            |                  | In this          | article, | we presented | a           |
|     |     |     |     |     |     |     |     | review of       | autonomic     | networking |                  | since            | 2004,    | categorizing | lit-        |
|     |     |     |     |     |     |     |     | erature         | into before   | and        | after            | the introduction |          | of           | SDN and     |
Fig.30. Serviceadmissionprobability.
|     |     |     |     |     |     |     |     | NFV. We           | then discussed |       | the           | challenges | of              | network      | automa-  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------------- | ----- | ------------- | ---------- | --------------- | ------------ | -------- |
|     |     |     |     |     |     |     |     | tion. Multi-agent |                | based | network       | automation |                 | architecture | is       |
|     |     |     |     |     |     |     |     | presented         | along          | with  | the Markovian |            | mathematical    |              | model of |
|     |     |     |     |     |     |     |     | the system.       | Finally,       | we    | presented     |            | the performance |              | of the   |
systemforasimplifiedcase.Theperformanceanalysisshowed
|     |     |     |     |     |     |     |     | the possibility | of      | utilizing          | a multi-agent  |          | system     | for            | network     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | ------------------ | -------------- | -------- | ---------- | -------------- | ----------- |
|     |     |     |     |     |     |     |     | management      | system  | automation.        |                | What     | we         | can guess      | from        |
|     |     |     |     |     |     |     |     | the preliminary |         | analysis           | is that        | the      | use        | of multi-agent | in          |
|     |     |     |     |     |     |     |     | automating      | network | management         |                | provides |            | a scalable,    | flexi-      |
|     |     |     |     |     |     |     |     | ble, dynamic,   | and     | resource-efficient |                |          | system.    | However,       | due to      |
|     |     |     |     |     |     |     |     | the distributed | nature  |                    | of the system, |          | the effect | of             | virtualiza- |
tionandcommunicationoverheadhastobeevaluatedasfuture
|     |     |     |     |     |     |     |     | work. Testbed  | implementation |           |     | of MANA-NMS |         | and       | the exact |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --------- | --- | ----------- | ------- | --------- | --------- |
|     |     |     |     |     |     |     |     | implementation |                | of agents | for | specific    | network | functions | are       |
Fig.31. CPUresourceconsumptionwithbackupsystem. also left as future works.
|     |     |     |     |     |     |     |     | Moreover,   | we       | also | aimed at     | performing |        | a detailed | multi-   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---- | ------------ | ---------- | ------ | ---------- | -------- |
|     |     |     |     |     |     |     |     | agent study | focusing |      | on designing |            | agents | and their  | internal |
components.
| them approximately |        | doubles | the resource |        | consumption. |              | This |     |     |     |     |     |     |     |     |
| ------------------ | ------ | ------- | ------------ | ------ | ------------ | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicated          | that a | backup  | system has   | a huge | cost         | of resources |      |     |     |     |     |     |     |     |     |
and energy consumption. To reduce such consumption, we REFERENCES
| propose | service | differentiation | in  | providing | a backup |     | system |               |     |       |           |          |           |      |           |
| ------- | ------- | --------------- | --- | --------- | -------- | --- | ------ | ------------- | --- | ----- | --------- | -------- | --------- | ---- | --------- |
|         |         |                 |     |           |          |     |        | [1] Consensus | on  | 6G Is | Gradually | Forming. | Accessed: | Mar. | 24, 2020. |
by providing backup agents for only critical services or by [Online]. Available: https://telecoms.com/503142/consensus-on-6g-is-
gradually-forming/
| providing | flexibility | to         | provide such | options |        | to use | by the |                                                                |     |     |     |     |     |     |     |
| --------- | ----------- | ---------- | ------------ | ------- | ------ | ------ | ------ | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |             |            |              |         |        |        |        | [2] Software-DefinedNetworking:TheNewNormforNetworks,OpenNetw. |     |     |     |     |     |     |     |
| network   | operator    | to decide. | This makes   | the     | system | more   | effi-  |                                                                |     |     |     |     |     |     |     |
Found.,MenloPark,CA,USA,2012.
cientinresourceutilizationandresilientcomparedtoasystem
|     |     |     |     |     |     |     |     | [3] NFV | Technology. | Accessed: |     | Oct. 30, | 2019. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --------- | --- | -------- | ----- | --------- | ---------- |
https://www.etsi.org/technologies/nfv
| without  | any backup   | mechanism. | A        | more | detailed  | analysis | is     |           |              |     |                     |     |     |       |              |
| -------- | ------------ | ---------- | -------- | ---- | --------- | -------- | ------ | --------- | ------------ | --- | ------------------- | --- | --- | ----- | ------------ |
|          |              |            |          |      |           |          |        | [4] Á. L. | V. Caraguay, | P.  | J. Ludeña-González, |     | R.  | V. T. | Tandazo, and |
| left for | future work. | Figure     | 32 shows | the  | reduction |          | in CPU |           |              |     |                     |     |     |       |              |
L.I.B.López,“SDN/NFVarchitectureforIoTnetworks,”inProc.14th
consumption compared to a backup system without service Int.Conf.WebInf.Syst.Technol.Vol.1(ITSCO),2018,pp.425–429.
differentiation. However, more critical services are admitted [5] R. Boutaba et al., “A comprehensive survey on machine learning
|            |          |             |             |     |          |     |        | for networking: |     | Evolution, | applications |     | and research | opportunities,” | J.  |
| ---------- | -------- | ----------- | ----------- | --- | -------- | --- | ------ | --------------- | --- | ---------- | ------------ | --- | ------------ | --------------- | --- |
| with a few | increase | in resource | consumption |     | compared |     | to the |                 |     |            |              |     |              |                 |     |
InternetServ.Appl.,vol.9,no.1,p.16,Jun.2018.[Online].Available:
system without service backup. https://doi.org/10.1186/s13174-018-0087-2
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3616 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
[6] D.Gavalas,D.Greenwood,M.Ghanbari,andM.O’Mahony,“Ahybrid [29] T. Braga, F. Silva, J. M. Nogueira, A. Loureiro, and L. B. Ruiz, “A
centralised-distributednetworkmanagementarchitecture,”inProc.IEEE tinyandlight-weightautonomicelementforwirelesssensornetworks,”
Int.Symp.Comput.Commun.,RedSea,Egypt,1999,pp.434–441. inProc.4thInt.Conf.Auton.Comput.(ICAC),Jacksonville,FL,USA,
[7] W.W.Tseng,P.K.Muller,K.M.Chow,M.W.Meyer,andG.D.Bruno, 2007,p.17.
“Distributed service subsystem architecture for distributed network [30] I.Al-OqilyandA.Karmouch,“Aself-organizingcompositiontowards
management,”U.S.Patent6308207,2001. autonomicoverlaynetworks,”inProc.IEEENetw.Oper.Manag.Symp.
[8] G. A. Oparin, V. G. Bogdanova, A. A. Pashinin, and S. A. Gorsky, (NOMS),2008,pp.287–294.
“Distributed solvers of applied problems based on microservices and [31] C. Ma, X. Lin, H. Lv, and H. Wang, “ABSR: An agent based
agentnetworks,”inProc.41stInt.Conv.Inf.Commun.Technol.Electron. self-recovery model for wireless sensor network,” in Proc. 8th IEEE
Microelectron.(MIPRO),May2018,pp.1415–1420. Int. Conf. Depend. Auton. Secure Comput., Chengdu, China, 2009,
[9] R. W. Collier, E. O’Neill, D. Lillis, and G. O’Hare, “MAMS: pp.400–404.
Multi-agent microservices*,” in Proc. Companion World [32] M. ElGammal and M. Eltoweissy, “Towards aware, adaptive and
Wide Web Conf., 2019, pp.655–662. [Online]. Available: autonomic sensor-actuator networks,” in Proc. IEEE 5th Int. Conf.
https://doi.org/10.1145/3308560.3316509 Self-Adapt.Self-Org.Syst.,AnnArbor,MI,USA,2011,pp.210–211.
[10] T.B.Meriem,R.Chaparadza,B.Radier,S.Soulhi,J.-A.Lozano-López, [33] S. Schuetz, K. Zimmermann, G. Nunzi, S. Schmid, and M. Brunner,
andA.Prakash,“GANA—Genericautonomicnetworkingarchitecture,” “Autonomic and decentralized management of wireless access
ETSI,SophiaAntipolis,France,WhitePaper,2016. networks,”IEEETrans.Netw.ServiceManag.,vol.4,no.2,pp.96–106,
[11] F.GranelliandR.Bassoli,“Autonomicmobilevirtualnetworkoperators Sep.2007.
forfuturegenerationnetworks,”IEEENetw.,vol.32,no.5,pp.76–84, [34] J.A.McCannandR.Sterritt,“Autonomicpervasivenetworks(APNs)—
Sep./Oct.2018. Extendedabstract,”inProc.7thIEEEInt.Conf.WorkshopsEng.Auton.
[12] F. Granelli and R. Bassoli, “Towards autonomic mobile network oper- Auton.Syst.,2010,pp.145–148.
ators,” in Proc. IEEE 7th Int. Conf. Cloud Netw. (CloudNet), Tokyo, [35] B. Mathieu et al., “Autonomic management of context-aware ambi-
Japan,2018,pp.1–4. ent overlay networks,” in Proc. 2nd Int. Conf. Commun. Netw. China,
[13] G. Baggio, R. Bassoli, and F. Granelli, “Cognitive software-defined Shanghai,China,2007,pp.727–733.
networkingusingfuzzycognitivemaps,”IEEETrans.Cogn.Commun. [36] Y. Qiang, Y. Li, and J. Chen, “The workload adaptation in auto-
Netw.,vol.5,no.3,pp.517–539,Sep.2019. nomicDBMSsbasedonlayeredqueuingnetworkmodel,”inProc.2nd
[14] J.O.KephartandD.M.Chess,“Thevisionofautonomiccomputing,” Int. Workshop Knowl. Discov. Data Min., Moscow, Russia, 2009,
Computer,vol.36,no.1,pp.41–50,Jan.2003. pp.781–785.
[15] J. Strassner, “Autonomic networking—Theory and practice,” in Proc. [37] Y.Liu,J.Zhang,M.Jiang,D.Raymer,andJ.Strassner,“Amodel-based
IEEE/IFIPNetw.Oper.Manag.Symp.,vol.1.Seoul,SouthKorea,2004, approachtoaddingautonomiccapabilitiestonetworkfaultmanagement
p.927. system,” in Proc. IEEE Netw. Oper. Manag. Symp., Salvador, Brazil,
[16] J. Strassner and J. O. Kephart, “Autonomic systems and networks: 2008,pp.859–862.
Theory and practice,” in Proc. IEEE/IFIP Netw. Oper. Manag. Symp. [38] N. Tcholtchev and R. Chaparadza, “Autonomic fault-management and
(NOMS),Vancouver,BC,Canada,2006,p.588. resiliencefromtheperspectiveofthenetworkoperationpersonnel,”in
[17] J.Strassner,“Autonomicnetworking,”inProc.5thIEEEWorkshopEng. Proc.IEEEGlobecomWorkshops,Miami,FL,USA,2010,pp.469–474.
Autonom.Auton.Syst.(EASE),2008,p.3. [39] J.C.NobreandL.Z.Granville,“Towardsconsistencyofpolicystates
[18] A.TizghadamandA.Leon-Garcia,“AORTA:Autonomicnetworkcon- in decentralized autonomic network management,” in Proc. IEEE Int.
trol and management system,” in Proc. IEEE INFOCOM Workshops, Symp.Pol.Distrib.Syst.Netw.,London,U.K.,2009,pp.170–173.
Phoenix,AZ,USA,2008,pp.1–4. [40] H.Zhang,M.Zhao,W.Wang,X.Gong,andX.Que,“Anovelautonomic
[19] M. Behringer, A. Dutta, Y. Hertoghs, and S. Bjarnason, “Autonomic architecture for QoS management in wired network,” in Proc. IEEE
networking—From theory to practice,” in Proc. IEEE Netw. Oper. GlobecomWorkshops,2010,pp.529–533.
Manag.Symp.(NOMS),2014,pp.1–17. [41] B. Mokhtar and M. Eltoweissy, “Memory-enabled autonomic resilient
[20] H. Gogineni, A. Greenberg, D. A. Maltz, T. S. E. Ng, H. Yan, and networking,” in Proc. 7th Int. Conf. Collab. Comput. Netw. Appl.
H.Zhang,“MMS:Anautonomicnetwork-layerfoundationfornetwork Worksharing(CollaborateCom),Orlando,FL,USA,2011,pp.132–141.
management,”IEEEJ.Sel.AreasCommun.,vol.28,no.1,pp.15–27, [42] L. Noirie et al., “Semantic networking: Flow-based, traffic-aware, and
Jan.2010. self-managednetworking,”BellLabsTechn.J.,vol.14,no.2,pp.23–38,
[21] M. May, M. Siekkinen, V. Goebel, T. Plagemann, R. Chaparadza, and 2009.
L. Peluso, “Monitoring as first class citizen in an autonomic network [43] M. B. Lehocine and M. Batouche, “Self-management in IP networks
universe,” in Proc. 2nd Bio-Inspired Models Netw. Inf. Comput. Syst., usingautonomiccomputing,”inProc.Int.Conf.WorkshopNetw.Future
Budapest,Hungary,Dec.2007,pp.247–254. (NOF),Paris,France,2014,pp.1–3.
[22] G.Bouabene,C.Jelger,C.Tschudin,S.Schmid,A.Keller,andM.May, [44] R. Sterritt, “Autonomous and autonomic systems: Paradigm for engi-
“The autonomic network architecture (ANA),” IEEE J. Sel. Areas neering effective software-based systems?” in Proc. 33rd Annu. IEEE
Commun.,vol.28,no.1,pp.4–14,Jan.2010. Softw.Eng.Workshop,Skovde,Sweden,2009,p.57.
[23] W. Berrayana, H. Youssef, and G. Pujolle, “A generic cross-layer [45] A. Galis, S. Clayman, and L. Mamatas, “Towards autonomic manage-
architecture for autonomic network management with network wide mentofsoftwareenablednetworks,”inProc.8thInt.Symp.Adv.Topics
knowledge,”inProc.8thInt.WirelessCommun.MobileComput.Conf. Elect.Eng.(ATEE),Bucharest,Romania,2013,pp.1–3.
(IWCMC),Limassol,Cyprus,2012,pp.82–87. [46] P.ZhangandJ.Wang,“SIPbasedschemeforcollaborativeautonomic
[24] S.Wang,H.Zhao,B.Zhang,H.Liu,andL.Xie,“Anautonomiccom- network management,” in Proc. 5th IEEE Int. Conf. Broadband Netw.
municationbasedconceptualandarchitecturemodelforcognitiveradio MultimediaTechnol.,Guilin,China,2013,pp.323–326.
nodes,” in Proc. IET 3rd Int. Conf. Wireless Mobile Multimedia Netw. [47] L. Wang and E. Gelenbe, “Demonstrating voice over an autonomic
(ICWMNN),Beijing,China,2010,pp.200–204. network,” in Proc. IEEE Int. Conf. Auton. Comput., Grenoble, France,
[25] J.Praveen,B.Praveen,andC.S.R.Murthy,“Afirststeptowardsauto- 2015,pp.139–140.
nomicopticalburstswitchednetworks,”inProc.2ndInt.Conf.Auton. [48] X. Liu, P. Juluri, and D. Medhi, “An experimental study on dynamic
Comput.(ICAC),Seattle,WA,USA,2005,pp.306–307. network reconfiguration in a virtualized network environment using
[26] F. Baroncelli, B. Martini, and P. Castoldi, “Autonomic service provi- autonomic management,” in Proc. IFIP/IEEE Int. Symp. Integr. Netw.
sioningforautomaticallyswitchedtransportnetwork,”inProc.JointInt. Manag.(IM),Ghent,Belgium,2013,pp.616–622.
Conf. Opti. Internet Next Gener. Netw. (COIN-NGNCON), Jeju, South [49] X. Long et al., “Autonomic networking: Architecture design and stan-
Korea,2006,pp.15–17. dardization,”IEEEInternetComput.,vol.21,no.5,pp.48–53,2017.
[27] A. A. F. Loureiro and L. B. Ruiz, “Autonomic wireless networks in [50] G. Xilouris et al., “Towards autonomic policy-based network service
smart environments,” in Proc. 5th Annu. Conf. Commun. Netw. Serv. deploymentwithSLAandmonitoring,”inProc.IEEEConf.Netw.Func.
Res.(CNSR),Fredericton,NB,Canada,2007,pp.5–7. Virtualization Softw. Defined Netw. (NFV-SDN), Verona, Italy, 2018,
[28] A.Moursy,A.Aly,B.Xu,D.Perkins,andM.Bayoumi,“Testbedimple- pp.1–2.
mentationforautonomicnetworkperformancemanagementofwireless [51] A.Richardetal.,“Autonomousnetworks:Empoweringdigitaltransfor-
mesh networks,” in Proc. IEEE Globecom Workshops, Anaheim, CA, mation for the telecoms industry,” TM Forum, Parsippany, NJ, USA,
USA,2012,pp.903–907. WhitePaper,2019.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore. Restrictions apply.

ARZOetal.:MULTI-AGENTBASEDAUTONOMICNETWORKMANAGEMENTARCHITECTURE 3617
[52] K.Tsagkaris,M.Logothetis,V.Foteinos,G.Poulios,M.Michaloliakos, [72] X.Zhang,K.Shi,S.Zhang,D.Li,andR.Xia,“Virtualagentclustering
and P. Demestichas, “Customizable autonomic network manage- basedmobilitymanagementoverthesatellitenetworks,”IEEEAccess,
ment:Integratingautonomicnetworkmanagementandsoftware-defined vol.7,pp.89544–89555,2019.
networking,” IEEE Veh. Technol. Mag., vol. 10, no. 1, pp.61–68, [73] Z. Taoqing and H. Xiaoying, “Self-adaptive network service research
Mar.2015. basedonmulti-agentsinhierarchy,”inProc.1stInt.Conf.Netw.Distrib.
[53] Q. Qi, W. Wang, X. Gong, and X. Que, “A SDN-based network Comput.,Hangzhou,China,2010,pp.314–316.
virtualization architecture with autonomie management,” in Proc. [74] G.-Z. Liu and D. Juan, “Design of distributed network management
|             |          |           |     |          |         |                | system                         | based | on multi-agent,” |     | in Proc. | 3rd | Int. Symp. | Inf. Process., |
| ----------- | -------- | --------- | --- | -------- | ------- | -------------- | ------------------------------ | ----- | ---------------- | --- | -------- | --- | ---------- | -------------- |
| IEEE        | Globecom | Workshops | (GC | Wkshps), | Austin, | TX, USA, 2014, |                                |       |                  |     |          |     |            |                |
| pp.178–182. |          |           |     |          |         |                | Qingdao,China,2010,pp.433–436. |       |                  |     |          |     |            |                |
[54] A.Mercian,P.Sharma,R.Aguiar,C.Chen,andD.Pinheiro,“UDAAN: [75] H. Tianfield, “Multi-agent based autonomic architecture for network
Embedding user-defined analytics applications in network devices,” management,”inProc.IEEEInt.Conf.Ind.Informat.(INDIN),Banff,
in Proc. Workshop Netw. Meets AI ML, 2019, pp.70–75. [Online]. AB,Canada,2003,pp.462–469.
|     |     |     |     |     |     |     | [76] N. A. | M. Subha, | G.-P. | Liu, | and N. | H. M. Yusof, | “External | consen- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----- | ---- | ------ | ------------ | --------- | ------- |
Available:https://doi.org/10.1145/3341216.3342216
|                   |     |                |     |               |     |                    | sus | in networked | multi-agent |     | systems | with random | network | delay,” in |
| ----------------- | --- | -------------- | --- | ------------- | --- | ------------------ | --- | ------------ | ----------- | --- | ------- | ----------- | ------- | ---------- |
| [55] F. Granelli, |     | D. Kliazovich, | and | N. Malheiros, |     | “Towards cognitive |     |              |             |     |         |             |         |            |
Internet: An evolutionary vision,” in Cognitive Radio and Networking Proc.57thAnnu.Conf.Soc.Instrum.ControlEng.Japan(SICE),2018,
| forHeterogeneousWirelessNetworks:RecentAdvancesandVisionsfor |     |     |     |     |     |     | pp.427–432. |           |            |           |     |               |     |             |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | --------- | --- | ------------- | --- | ----------- |
|                                                              |     |     |     |     |     |     | [77] M.     | Sharf and | D. Zelazo, | “Analysis |     | and synthesis | of  | MIMO multi- |
theFuture.Cham,Switzerland:Springer,2015,pp.181–200.
agentsystemsusingnetworkoptimization,”IEEETrans.Autom.Control,
| [56] M. Wódczak |     | et al., “Standardizing |     | a reference |     | model and autonomic |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------------------- | --- | ----------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.64,no.11,pp.4512–4524,Nov.2019.
networkarchitecturesfortheself-managingfutureInternet,”IEEENetw.,
|     |     |     |     |     |     |     | [78] M. Sharf | and | D. Zelazo, | “Network | feedback |     | passivation | of passivity- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | -------- | -------- | --- | ----------- | ------------- |
vol.25,no.6,pp.50–56,Nov.2011.
|     |     |     |     |     |     |     | short | multi-agent | systems,” |     | IEEE Control | Syst. | Lett., | vol. 3, no. 3, |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --------- | --- | ------------ | ----- | ------ | -------------- |
[57] AutonomicNetworkEngineeringfortheSelf-ManagingFutureInternet pp.607–612,Jul.2019.
| (AFI): | Scenarios, | Use | Cases | and Requirements |     | for Autonomic/Self- |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ----- | ---------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[79] A.Y.Yazıcıogˇlu,M.Egerstedt,andJ.S.Shamma,“Formationofrobust
ManagingFutureInternet,documentETSIGSAFI001,ETSI,Sophia
|     |     |     |     |     |     |     | multi-agent |     | networks | through | self-organizing |     | random | regular graphs,” |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------- | --------------- | --- | ------ | ---------------- |
Antipolis,France,2011.
IEEETrans.Netw.Sci.Eng.,vol.2,no.4,pp.139–151,Oct./Dec.2015.
| [58] “Network | technologies |     | (NTECH): | Autonomic |     | network engineering |         |         |            |     |     |            |              |        |
| ------------- | ------------ | --- | -------- | --------- | --- | ------------------- | ------- | ------- | ---------- | --- | --- | ---------- | ------------ | ------ |
|               |              |     |          |           |     |                     | [80] G. | Uma, B. | E. Prasad, | and | O.  | N. Kumari, | “Distributed | intel- |
for the self-managing future Internet (AFI): autonomicity and self- ligent systems: Issues, perspectives and approaches,” Knowl.
managementinthebroadbandforum(BBF)architectures,”ETSI,Sophia Based Syst., vol. 6, no. 2, pp.77–86, 1993. [Online]. Available:
Antipolis,France,ETSIRep.TR103473,2018.
http://www.sciencedirect.com/science/article/pii/095070519390022L
| [59] R. Chaparadza |     | et al., | “SDN enablers | in  | the ETSI | AFI GANA refer- |         |               |     |       |           |           |          |         |
| ------------------ | --- | ------- | ------------- | --- | -------- | --------------- | ------- | ------------- | --- | ----- | --------- | --------- | -------- | ------- |
|                    |     |         |               |     |          |                 | [81] M. | R. Genesereth | and | S. P. | Ketchpel, | “Software | agents,” | Commun. |
encemodelforautonomicmanagement&control(emergingstandard),
|     |     |     |     |     |     |     | ACM, | vol. | 37, no. | 7, p.48, | Jul. | 1994. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ------- | -------- | ---- | ----- | --------- | ---------- |
and virtualization impact,” in Proc. IEEE Globecom Workshops (GC https://doi.org/10.1145/176789.176794
Wkshps),Atlanta,GA,USA,2013,pp.818–823. [82] G. K. Soon, C. K. On, P. Anthony, and A. R. Hamdan, “A review
[60] R.Chaparadzaetal.,“ImplementationguidefortheETSIAFIGANA on agent communication language,” in Computational Science and
| model: | A standardized |     | reference | model | for | autonomic networking, |     |     |     |     |     |     |     |     |
| ------ | -------------- | --- | --------- | ----- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Technology,R.Alfred,Y.Lim,A.A.A.Ibrahim,andP.Anthony,Eds.
| cognitive | networking | and | self-management,” |     | in  | Proc. IEEE Globecom |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ----------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Singapore:Springer,2019,pp.481–491.
Workshops(GCWkshps),Atlanta,GA,USA,2013,pp.935–940. [83] K. Lerman, A. Galstyan, and T. Hogg, “Mathematical analysis of
[61] R.Chaparadza,M.Wodczak,T.B.Meriem,P.DeLutiis,N.Tcholtchev, multi-agentsystems,”2004.[Online].Available:https://arxiv.org/abs/cs/
| and L. | Ciavaglia, | “Standardization |     | of  | resilience | & survivability, and | 0404002. |     |     |     |     |     |     |     |
| ------ | ---------- | ---------------- | --- | --- | ---------- | -------------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
autonomicfault-management,inevolvingandfuturenetworks:Anongo- [84] R.Guerzoni,Z.Despotovic,R.Trivisonno,andI.Vaishnavi,“Modeling
inginitiativerecentlylaunchedinETSI,”inProc.9thInt.Conf.Design
|     |     |     |     |     |     |     | reliability | requirements |     | in coordinated |     | node | and link | mapping,” in |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | -------------- | --- | ---- | -------- | ------------ |
Rel.Commun.Netw.(DRCN),Budapest,Hungary,2013,pp.331–341. Proc.IEEE33rdInt.Symp.Rel.Distrib.Syst.,Nara,Japan,Oct.2014,
| [62] S.vanderMeer,J.Keeney,andL.Fallon,“5Gnetworksmustbeauto- |     |     |     |     |     |     | pp.321–330. |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
nomic!”inProc.IEEE/IFIPNetw.Oper.Manag.Symp.(NOMS),Taipei, [85] S.Ayoubi,Y.Zhang,andC.Assi,“RAS:Reliableauto-scalingofvirtual
Taiwan,2018,pp.1–5. machinesinmulti-tenantcloudnetworks,”inProc.IEEE4thInt.Conf.
CloudNetw.(CloudNet),NiagaraFalls,ON,Canada,Oct.2015,pp.1–6.
[63] G.SakarkarandV.M.Thakar,“Autonomoussoftwareagentforlocal-
|           |          |      |               |       |             |                 | [86] R. Birke, | I.  | Giurgiu, | L. Y. | Chen, D. | Wiesmann, | and | T. Engbersen, |
| --------- | -------- | ---- | ------------- | ----- | ----------- | --------------- | -------------- | --- | -------- | ----- | -------- | --------- | --- | ------------- |
| ization,” | in Proc. | Int. | Conf. Intell. | Agent | Multi-Agent | Syst., Chennai, |                |     |          |       |          |           |     |               |
India,2009,pp.1–4. “Failureanalysisofvirtualandphysicalmachines:Patterns,causesand
[64] N. R. Jennings, K. Sycara, and M. Wooldridge, “A roadmap characteristics,”inProc.44thAnnu.IEEE/IFIPInt.Conf.Depend.Syst.
of agent research and development,” Auton. Agents Multi-Agent Netw.,Atlanta,GA,USA,Jun.2014,pp.1–12.
|        |         |        |          |      |       |                      | [87] L. Qu,      | M. Khabbaz, |             | and C.     | Assi, “Reliability-aware |      | service       | chaining |
| ------ | ------- | ------ | -------- | ---- | ----- | -------------------- | ---------------- | ----------- | ----------- | ---------- | ------------------------ | ---- | ------------- | -------- |
| Syst., | vol. 1, | no. 1, | pp.7–38, | Jan. | 1998. | [Online]. Available: |                  |             |             |            |                          |      |               |          |
|        |         |        |          |      |       |                      | in carrier-grade |             | softwarized | networks,” |                          | IEEE | J. Sel. Areas | Commun., |
https://doi.org/10.1023/A:1010090405266
vol.36,no.3,pp.558–573,Mar.2018.
[65] E.M.DavidsonandS.D.J.McArthur,“Exploitingmulti-agentsystem
technologywithinanautonomousregionalactivenetworkmanagement [88] S.T.Arzo,R.Bassoli,F.Granelli,andF.H.P.Fitzek,“Studyofvirtual
system,” inProc. Int.Conf.Intell.Syst. Appl.PowerSyst., Kaohsiung, network function placement in 5G cloud radio access network,” IEEE
Trans.Netw.ServiceManag.,vol.17,no.4,pp.2242–2259,Dec.2020.
Taiwan,Nov.2007,pp.1–6.
[66] Q.Jiang,M.Xu,L.Tang,andQ.-B.Chen,“Researchonloadbalancing
basedonmulti-agentinubiquitousnetworks,”inProc.Int.Conf.Intell.
Comput.Technol.Autom.,vol.3.Changsha,China,2010,pp.10–13.
| [67] T. Amudha, | N.  | Saritha, | and P. | Usha, “A | multi-agent | based framework |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------ | -------- | ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
fordynamicservicediscoveryandaccessusingmatchmakingapproach,”
inProc.Int.Conf.Intell.AgentMulti-AgentSyst.,Chennai,India,2009,
pp.1–4.
| [68] S. K. | Patri, E. | Grigoreva, | W. Kellerer, |     | and C. M. | Machuca, “Rational |     |     |     |     |     |     |     |     |
| ---------- | --------- | ---------- | ------------ | --- | --------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
agent-based decision algorithm for strategic convergednetwork migra- Sisay Tadesse Arzo (Member, IEEE) received the
tion planning,” IEEE/OSA J. Opt. Commun. Netw., vol. 11, no. 7, B.Sc.degreefromHawassaUniversity,Ethiopia,and
pp.371–382,Jul.2019.
theM.Sc.degreeintelecommunicationengineering
| [69] A. Kott | et al.,       | “Autonomous |         | intelligent | cyber-defense | agent (AICA)         |     |     |           |     |            |            |         |              |
| ------------ | ------------- | ----------- | ------- | ----------- | ------------- | -------------------- | --- | --- | --------- | --- | ---------- | ---------- | ------- | ------------ |
|              |               |             |         |             |               |                      |     |     | from      | the | University | of Trento, | Italy,  | where he is  |
| reference    | architecture. |             | release | 2.0,”       | 2018.         | [Online]. Available: |     |     |           |     |            |            |         |              |
|              |               |             |         |             |               |                      |     |     | currently |     | pursuing   | the Ph.D.  | degree. | He is a for- |
arXiv:1803.10664. merVisitingResearchFellowwiththeUniversityof
[70] M.Mohammadian,“Networksecurityriskassessmentusingintelligent Luxembourg.Hehasmorethanfiveyearsofindus-
agents,”inProc. Int.Symp.AgentMulti-AgentSyst. Robot.(ISAMSR), trial experience with Telecom, Huawei Technology
| 2018,pp.1–6. |     |     |     |     |     |     |     |     | andEthio-Telecom,andfiveyearsofacademicexpe- |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
[71] S. Ouiazzane, M. Addou, and F. Barramou, “A multi-agent model for rience as a Lecturer with Addis Ababa University.
network intrusion detection,” in Proc. 1st Int. Conf. Smart Syst. Data His research interest included network softwariza-
Sci.(ICSSD),Rabat,Morocco,2019,pp.1–5. tion,SDN,NFV,IoT,andnetworkautomation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.

3618 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.3,SEPTEMBER2021
Riccardo Bassoli (Member, IEEE) received the Frank H. P. Fitzek (Senior Member, IEEE)
B.Sc. and M.Sc. degrees in telecommunications received the Diploma (Dipl.-Ing.) degree in
engineering from the University of Modena and electrical engineering from the University of
ReggioEmilia,Italy,in2008and2010,respectively, Technology—Rheinisch-Westfälische Technische
and the Ph.D. degree from 5G Innovation Centre, Hochschule, Aachen, Germany, in 1997, and the
UniversityofSurrey,U.K.,in2016.Heiscurrentlya Ph.D. (Dr.-Ing.) degree in electrical engineering
SeniorResearcherwiththeDeutscheTelekomChair from the Technical University Berlin, Germany, in
of Communication Networks, Faculty of Electrical 2002. He became an Adjunct Professor with the
and Computer Engineering, Technische Universität UniversityofFerrara,Italy,in2002.Heiscurrently
Dresden, Germany. From 2011 to 2015, he was aProfessorandtheHeadoftheDeutscheTelekom
also a Marie Curie Early Stage Researcher with Chair of Communication Networks, Technische
the Instituto de Telecomunicações, Portugal, and a Visiting Researcher with UniversitätDresden,Germany,andalsocoordinatingthe5GLab,Germany.
AirbusDefenceandSpace,France. He is the spokesman of the DFG Cluster of Excellence, CeTI. In 2003,
|     |     |     |     | he joined Aalborg | University as | an Associate Professor | and later became |
| --- | --- | --- | --- | ----------------- | ------------- | ---------------------- | ---------------- |
Professor.
|     | Fabrizio       | Granelli (Senior  | Member,             | IEEE) is |     |     |     |
| --- | -------------- | ----------------- | ------------------- | -------- | --- | --- | --- |
|     | an Associate   | Professor         | with the Department | of       |     |     |     |
|     | Information    | Engineering       | and Computer        | Science, |     |     |     |
|     | University     | of Trento, Italy. | From 2012           | to 2014, |     |     |     |
|     | he was Italian | Master School     | Coordinator         | in the   |     |     |     |
frameworkwiththeEuropeanInstituteofInnovation
|     | and Technology, | ICT Labs | Consortium. | He is the |     |     |     |
| --- | --------------- | -------- | ----------- | --------- | --- | --- | --- |
Coordinatoroftheresearchanddidacticalactivities
oncomputernetworks.Hehasauthored/coauthored
morethan250paperspublishedininternationaljour-
|                 | nals, books,         | and conferences | on networking. | He      |     |     |     |
| --------------- | -------------------- | --------------- | -------------- | ------- | --- | --- | --- |
| was an IEEE     | ComSoc Distinguished | Lecturer from   | 2012 to 2015,  | an IEEE |     |     |     |
| ComSoc Director | for Online Content   | from 2016       | to 2017, and   | an IEEE |     |     |     |
ComSocDirectorforEducationalServicesfrom2018to2019.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:15:21 UTC from IEEE Xplore.  Restrictions apply.