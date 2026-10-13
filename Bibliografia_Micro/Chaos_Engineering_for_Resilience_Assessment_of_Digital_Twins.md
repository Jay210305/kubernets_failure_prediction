1134 IEEETRANSACTIONSONINDUSTRIALINFORMATICS,VOL.20,NO.2,FEBRUARY2024
Chaos Engineering for Resilience
Assessment of Digital Twins
Mattia Fogli , Graduate Student Member, IEEE, Carlo Giannelli , Senior Member, IEEE,
Filippo Poltronieri , Member, IEEE, Cesare Stefanelli , Member, IEEE,
and Mauro Tortonesi , Member, IEEE
Abstract—Within the Industry 4.0 vision, digital twins in a 2003 presentation and later formalized in a 2014 white
(DTs)havegainedgreatattentionasapromisingapproach paper [1], the DT concept aims at building a high-accuracy
to improve remote monitoring and control by means of
virtual model of a physical system to leverage its capabilities
virtualrepresentationsofphysicalobjects.However,while
torunwhat-ifscenariosforthepurposeofoptimizingphysical
DTs are becoming more and more sophisticated and even
adopted for mission-critical applications, their resilience processes. The appeal of this paradigm is evident in industrial
assessment has not received the required consideration applications, which involve complex processes and expensive
yet. This article originally proposes chaos engineering to machinery.Asaresult,althoughDTsrepresentastillrelatively
assessandimprovetheresilienceofDTsbytestingmulti-
newtechnology,theyhavealreadyattractedalotofattention.
pleaspectsofindustrialenvironmentsinacoordinated,au-
SeveraleffortstoprovideacommonframeworkforDTshave
tomated,andreplicablemanner.First,thearticlediscusses
why and how chaos engineering is promising to improve been made. In a 2019 seminal survey on DT applications in
theresilienceofDTs.Then,itidentifiesandintroducesaset the industry, Tao et al. [2] defined a five-dimensional model
ofchaosengineeringprofilesspecificallydesignedtotake for DTs, including physical system, digital system, updating
intoaccountthemanyaspectsanindustrialenvironmentis
engine, prediction engine, and optimization. In 2020, Minerva
composed of. Finally, it shows the feasibility of assessing
et al. [3] investigated DTs adopting a broader perspective that
the resilience of a proof-of-concept DT through a testbed
basedonwidely-adopted,open-sourcetools. alsoconsideredInternet-of-Thingsapplications,payingspecial
attention to the characterization of qualifying properties for
Index Terms—Chaos engineering, digital twin (DT), en-
DTs. With the term DT, they referred to the ensemble of the
tanglement,industrialInternetofThings,Industry4.0.
physicalobject(PO),thelogicalobject(s),andtherelationship
betweenthem.Thisdoesnotappeartobeauniversallyaccepted
I. INTRODUCTION definition.Forinstance,Kritzingeretal.[4]explicitlyconsidered
THE advent of Industry 4.0 has recently pushed for a per- differentlevelsofvirtualrepresentation,distinguishingbetween
digital models, where no automated data exchange between
vasivespreadofinformationtechnology(IT)technologies
thePOanditslogicalcounterparttakesplace,digitalshadows,
andstandardswithinoperationaltechnology(OT)environments.
whichperformanautomated,unidirectionaldataexchangefrom
The primary outcome is a paradigm shift in the interaction
the PO to its logical counterpart, and DTs, which perform an
withindustrialequipment.Nowadays,thegreatamountoffine-
automated,bidirectionaldataexchangebetweenthePOandits
grainedstatusinformationavailableallowsadeeperobservation
logicalcounterpart.
and understanding of current manufacturing processes, along
Since there appears to be no consensus around a definition
withtheexplorationofnewandsignificantlyimprovedones.
of DT, this work uses the term DT to refer to any software
One of the most compelling pillars of this revolution is the
accuratelycapturingaPOinthevirtualizedworldforactionable
conceptofdigitaltwin(DT).OriginallyintroducedbyGrieves
ordecision-makingpurposes,regardlessofhowitcommunicates
Manuscript received 6 March 2023; accepted 20 March 2023. Date withthePO.Inaddition,weadoptabroaderperspectiveforthe
of publication 3 April 2023; date of current version 19 January 2024. PO term, which may refer to either tangible objects, such as
This work was supported by the Spoke 1 “FutureHPC & BigData” of
a machine or a production line, or intangible ones, such as a
theItalianResearchCenteronHigh-PerformanceComputing,BigData
and Quantum Computing (ICSC) funded by MUR Missione 4 - Next softwarecomponentcontrollingthemanufacturingprocess[3].
GenerationEU(NGEU).Paperno.TII-23-0771.(Correspondingauthor: Finally,relativelycomplexusecasesmayconsiderthepossibil-
MattiaFogli.)
itythatahigh-levelDT,infact,maybebuiltuponacomposition
Mattia Fogli, Filippo Poltronieri, and Cesare Stefanelli are with
the Department of Engineering, University of Ferrara, 44122 Fer- oflower-levelDTs.FromtheperspectiveofthecomposedDT,
rara, Italy (e-mail: mattia.fogli@unife.it; filippo.poltronieri@unife.it; ce- therefore,theunderlyingDTswouldbeconsideredPOs.
sare.stefanelli@unife.it).
DTs have been proposed and investigated in many different
CarloGiannelliandMauroTortonesiarewiththeDepartmentofMath-
ematics and Computer Science, University of Ferrara, 44121 Ferrara, industrialapplicationsandcontexts,suchasjobscheduling[5],
Italy(e-mail:carlo.giannelli@unife.it;mauro.tortonesi@unife.it). resource management [6], network traffic prediction [7],
Color versions of one or more figures in this article are available at
anomaly detection [8], zero-defect manufacturing [9], and
https://doi.org/10.1109/TII.2023.3264101.
DigitalObjectIdentifier10.1109/TII.2023.3264101 structural health monitoring [10]. Since DTs had proved to
1551-3203©2023IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.

FOGLIetal.:CHAOSENGINEERINGFORRESILIENCEASSESSMENTOFDIGITALTWINS 1135
be effective in a wide range of use cases, they became a TABLEI
criticallyimportantelementofthesmartfactoryinfrastructure. LISTOFACRONYMS
| However,        | the deployment |             | of         | DTs    | is everything | but           | trivial. |     |     |     |     |
| --------------- | -------------- | ----------- | ---------- | ------ | ------------- | ------------- | -------- | --- | --- | --- | --- |
| In this regard, |                | it is worth | mentioning |        | the           | heterogeneity | of       |     |     |     |     |
| involved        | devices,       | ranging     | from       | simple | vibration     | sensors       | to       |     |     |     |     |
complexdrilling/assemblytools,andtheadoptionofemerging
| standards | for securing | the | OT  | domain, | such | as IEC 62443 | for |     |     |     |     |
| --------- | ------------ | --- | --- | ------- | ---- | ------------ | --- | --- | --- | --- | --- |
cybersecuritypushingfornetworksegregation[11].
Notethat,inmanyusecases,theDTmustconsistentlymain-
| tain a relatively |            | tight relationship |     | with           | the | PO to capture   | its |     |     |     |     |
| ----------------- | ---------- | ------------------ | --- | -------------- | --- | --------------- | --- | --- | --- | --- | --- |
| behavior          | properly—a | foundational       |     | characteristic |     | that Minerva    |     |     |     |     |     |
| et al. [3]        | explicitly | investigated,      |     | defining       | it  | as entanglement |     |     |     |     |     |
(earlier works, such as [4], have touched upon it implicitly). However, the adoption of chaos engineering in OT environ-
Ensuringthedesiredlevelofentanglement,therefore,represents mentsisnottrivialsinceitrequirestowiselyadaptitbyconsider-
| a key concern | at  | the design |     | level, which, | in  | turn, introduces |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ------------- | --- | ---------------- | --- | --- | --- | --- | --- |
ingtheirspecificcharacteristics,e.g.,intermsofavailabilityand
important constraints on the set of feasible deployment loca- responsiveness. We believe that the definition and application
tions for the DT. For instance, a use case demanding strong of chaos engineering profiles—described as a set of fault in-
entanglement might result in a DT deployed very close to its jectiontests—specificallydesignedforindustrialenvironments
physicalcounterpart,e.g.,onthesameproductionsubnetwithin can bring huge benefits. In particular, when dealing with a
theOTdomain,thusensuringminimumlatencyandmaximum
|     |     |     |     |     |     |     | complex system | composed | of  | several DTs, | the enforcement |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ------------ | --------------- |
reliability.However,deployingaDTascloseaspossibletoits of well-defined and replicable chaos engineering profiles can
physicalcounterpartmightnotalwaysbedesirable,asthismight helpidentifybottlenecksandundisclosedvulnerabilities.Tothis
not satisfy the demanding requirements of the OT domain. In purpose,thisarticlepresentsthefollowing.
fact,whiletraditionalITenvironmentspushforsecurity(based 1) Whyandhowtoproperlyadoptchaosengineeringwithin
onconfidentialityandintegrity),OTonespushforsafety(with
OTenvironmentsbyadaptingittofitOTpeculiarities.
theavailabilityofservicesandreliabilityofcommunicationas 2) Suitablechaosengineeringprofilesandfaultactionsfor
primaryrequirements). a wide range of industrial scenarios. Such profiles are
Ensuring the fulfillment of the desired resilience levels for meant to stress computing and networking resources to
DTs, which build on the dynamic interaction of several soft- identifypossibleissuesofDT-basedOTenvironments.
warecomponentsinverycomplexdistributedscenarios,while
|     |     |     |     |     |     |     | 3) Atestbedbasedonstate-of-the-arttechnologies,suchas |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
satisfyingtheQoSrequirementsofOTenvironments,represents containerization, Kubernetes, and Chaos Mesh, demon-
a very challenging task. On the one hand, the static analysis stratingthefeasibilityandeffectivenessoftestingmulti-
of such solutions can be difficult, since it is not always easy ple aspects of industrial environments in a coordinated,
to clearly identify and test every possible point of failure and automated,andreplicablemanner.
bottleneck. Also, note that DTs are typically made by several Specifically, our approach is capable of assessing if the DT
components, each having its own entanglement requirements respectsthelevelsofentanglementrequiredbythespecificappli-
and that the entanglement a DT should provide is application cation.Theseresultsalsoprovideguidanceonthefundamentally
specificandmayvarydependingontheusecase.Ontheother
importantissueofchoosingwheretodeployaDTwithintheOT
| hand, the | dynamic | analysis | of  | DTs | deployed | in a distributed | environment. |     |     |     |     |
| --------- | ------- | -------- | --- | --- | -------- | ---------------- | ------------ | --- | --- | --- | --- |
mannerhastoconsiderseveralaspectscharacterizingindustrial Therestofthearticleisorganizedasfollows.TableIpresents
environments, ranging from hardware capabilities of nodes to the list of acronyms used in the article. Section II lays out
protocolsadoptedbyapplications. the related work. Section III discusses how chaos engineering
| With the | intent | to verify |     | the fulfillment |     | of resilience | re-               |     |           |                |              |
| -------- | ------ | --------- | --- | --------------- | --- | ------------- | ----------------- | --- | --------- | -------------- | ------------ |
|          |        |           |     |                 |     |               | may be beneficial | for | improving | the resilience | of DTs in an |
quirements in DT-based solutions, the aim of this article is OTenvironment.Then,SectionIVfocusesonthedefinitionof
to originally propose the adoption of chaos engineering [12], chaos engineering profiles, i.e., sets of fault actions that can
which emerged in the last years as a compelling approach to be injected to stress the steady state of DTs at the network
ensurethefulfillmentofQoSincomplexITscenarios.Infact, andatthecomputinglevel.SectionVpresentsarepresentative
chaosengineeringallowsustoestimatetheimpactofunexpected
|     |     |     |     |     |     |     | case study | to demonstrate | the | effectiveness | of the proposed |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------------- | --------------- |
failures, such as server outages or network disruption on the methodologiesforassessingtheresilienceofDTsandimproving
performance of IT applications [13]. In addition, the adoption theirdeployment.Finally,SectionVIconcludesthisarticle.
ofchaosengineeringpushesforacoordinated,automated,and
replicableapproach,allowingustoidentifypossibleshortcom-
II. RELATEDWORK
ingsbasedonasetofpreviouslyidentifiedtestsjointlyconsid-
eringmultipleandheterogeneousaspectsofthetargetenviron- The traditional approach to software testing typically takes
ments.Thiscanbeparticularlyusefultoimprovetheresilience place during the development phase. The rationale is to build
|     |     |     |     |     |     |     | resilient software | before | releasing | it in production. | Therefore, |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ------ | --------- | ----------------- | ---------- |
ofIT-distributedapplicationsbothatthedesignandproduction
levels. theobjectiveistoavoidfailuresinproduction.Yet,adistributed
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore.  Restrictions apply.

1136 IEEETRANSACTIONSONINDUSTRIALINFORMATICS,VOL.20,NO.2,FEBRUARY2024
systemis,infact,acomplexsystemwhosedependenciesmight toimplementresilienceattheperformancelevel,i.e.,tomaintain
notbeevenfullyunderstoodbythosewhohaveengineeredit. highproductivityinspiteofpotentiallydisruptivechangestothe
Asaresult,theproductionenvironmentistheonlyplacewhere productionschedules.Finally,Lietal.[18]analyzedhowDTs
somefailurescanbediscoveredand,aboveall,understood. enhancetheresilienceandimprovetheoverallsecurityposture
Toimprovetheresilienceofdistributedsystems,over20years of manufacturing industry, based on a highly critical scenario
agoAmazonlaunchedGameDay—aprogramwhoseoverarch- unfoldingintheaerospacesector.
ing ambition was to make the company’s systems, software, However, only very few works have specifically addressed
and people more resilient by purposely injecting failures in the problem of realizing resilient DTs. Among those, Vrabicˇ
production on a preplanned day [14]. More recently, Netflix et al. [28] defined resilience as a property of preserving the
hasproposedchaosengineering[12]andreleasedsometoolsto accuracyoftheDTanditsalignmentwiththerealsystemand
implement it [15]. Specifically, Basiri et al.[12] defined chaos focused on the retraining of DT models—a concept somehow
engineeringasthedisciplineof“experimentingonadistributed similar to the management of model drift in machine learning
systemtobuildconfidenceinitscapabilitytowithstandturbulent operations(MLOps).Instead,theworkin[29]and[30]isare-
conditionsinproduction.” cent2-partsurveyonDTliteraturethat,inadditiontoproviding
What makes chaos engineering fundamentally different in acomprehensiveandexcellentpresentationoftheliterature,puts
comparison to the traditional approach to software testing is thefocusonquantifyinguncertaintyasafundamentalelement
how it looks at failures. The rationale is the following. Any ofDTs.Thisrepresentsaconceptsimilar,ifsomewhatbroader,
systemwillbreakregardlessofanypriortestingwhenreleased totheassessmentofthelevelofentanglementbetweentheDT
in production. This happens because many failures, which are anditsphysicalcounterpartexploredinthepresentwork.Tothe
usuallyunpredictablebynature,canonlyhappeninproduction. bestofourknowledge,atthemomentofthiswriting,theonly
Theonlycountermeasure,therefore,istryingtopurposelybreak other work that proposes the adoption of chaos engineering to
thesysteminproductionandlearnhowtomakeitmoreresilient assessandimprovetheresilienceofaDTis[13].However,that
accordingly.Notethatthisisnotmeanttodiminishtheuseful- workconsidersaverydifferentapplication,i.e.,theoptimization
nessofsoftwaretestingindevelopment,whichremainsthebasis oflarge-scaleITservicesinhybridcloudscenariosandcannot
forbuildingresilientsoftwaresystems. beapplied“as-is”toindustrialenvironments.
In the realm of DTs, a trend gaining momentum is to adopt
approaches and technologies typical of Web- and cloud-based
III. ENTANGLEMENTASTHECRITICALCHARACTERISTIC
IT environments, such as virtual machines and containers, to
OFDTS
managetheDTlifecycle.Inparticular,microservice-basedar-
chitectures and containerization development/deployment rep- In the context of DTs, entanglement describes the commu-
resentvaluableapproachestomakethedynamicmanagementof nication relationship between a DT and its PO. The entangle-
DTseasierandtoensuretherequiredQoSwhilealsoimproving ment can be simple, strong, or weak [3]. Simple entanglement
theirreusabilityandcomposability[16],[17].Containerization means that communications between the DT and the PO are
is already a mature technology, widely used in cloud com- unidirectional,intermittent,ornotinrealtime.Aunidirectional
puting, and its adoption is currently gathering speed also in relationshipimpliesone-waycommunications,i.e.,eitherfrom
industrial environments [18], [19], e.g., to develop and deploy thePOtotheDTorvice-versa.Atypicalexampleofaunidirec-
manufacturing execution systems (MESs) and programmable tionalrelationshipconsistsinaPOthatperiodicallysendsstatus
logiccontrollers(PLCs)asmicroservices[20].Notethatwhat updates to its DT. Strong entanglement, instead, occurs when
mentioned above also fits with the vision of a modular design the DT and the PO consistently communicate over time. Such
forDTs,whichmakestheirimplementationmorefeasible,prac- astablelinkisbidirectional,whichmeansthatcommunications
tical,andcost-effective[21].Thereadermayrefertothework flowbothupstreamanddownstream.Thisgivestheabilitytothe
in[16] for athorough analysis of the state-of-the-artliterature DTtonotonlyreceiveupdatesfromthePObutalsotoalterthe
about microservice-based approaches to support the Industry POstate.Finally,weakentanglementmeansthattheDTdoesnot
4.0vision.Itisworthnotingthatamicroservice-basedDTisa receivestatusupdatesdirectlyfromthePObutderivesthePO
distributedsystem.Thisbringstheresilienceissuestraditionally status from secondary sources (e.g., a video stream recording
affectingdistributedsystems(IT)alsointherealmofDTs(OT). thePO).
MostoftheworksinvestigatingresilienceinthecontextofDT In addition, entanglement also refers to the DT responsive-
applicationsusuallyexplorehowtheDTconceptmayimprove ness,i.e.,itscapabilitytocollectdatafromitsphysicalcounter-
the resilience of smart factories [22], [23]. More specifically, part,processthem,andactuponthem.Tothisend,letusnote
one of the most popular applications of DTs in Industry 4.0 thatDTsaretypicallymadebyseveralcomponents,eachhaving
is for maintenance [24]. Other works apply the DT concept to itsownresponsivenessrequirements.Generally,theserequire-
criticalinfrastructure,withthegoalofimprovingtheirresilience ments tend to be application specific but it is conceivable that
capabilities[25],andleveragingtheDTapproachtoincreasethe OT applications would require communication latency within
resilience of industrial 5G systems to avoid production down- 10msandveryhighreliability[31],[32],[33].
time[26].Moreover,Parketal. [27]investigatedtheproblem Morespecifically,theresponsivenesslevelstypicallydepend
of realizing modular manufacturing systems for microsmart on the location of a DT within the OT. In this regard, this
factorieswithahighlyvaryingproductionschedule,usingDTs work refers to the Purdue Model as a general architecture for
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.

FOGLIetal.:CHAOSENGINEERINGFORRESILIENCEASSESSMENTOFDIGITALTWINS 1137
ones.Finally,atthetopLayer4andLayer5resideproduction
planningservices,e.g.,theenterpriseresourceplanning(ERP),
andITservers,e.g.,mailandWebservers,outsideofthescope
ofthisarticle.
Theseenvironmentsclearlyrecallthemaincharacteristicsof
|     |     |     |     | IT distributed | environments |         | composed    |         | of multiple | microser-     |
| --- | --- | --- | --- | -------------- | ------------ | ------- | ----------- | ------- | ----------- | ------------- |
|     |     |     |     | vices deployed |              | on (and | replicated  | across) | several     | platforms     |
|     |     |     |     | along the      | so-called    | compute | continuum   |         | (edge,      | on-premises   |
|     |     |     |     | cloud, public  | cloud,       | etc.).  | The overall |         | outcome     | is a more and |
moreheterogeneousandcomplexscenario,whoserequirements
|     |     |     |     | in terms     | of, e.g., | message        | dispatching |            | latency  | and service    |
| --- | --- | --- | --- | ------------ | --------- | -------------- | ----------- | ---------- | -------- | -------------- |
|     |     |     |     | availability | are       | very difficult | to          | grant.     | In fact, | the industrial |
|     |     |     |     | environment  | can       | be composed    |             | of several | POs,     | delving to the |
|     |     |     |     | development  | and       | deployment     | of          | tens or    | hundreds | of DTs, po-    |
tentiallyduplicatedanddynamicallymigratedonmultiplenodes
toensurefaulttoleranceandtherequiredQoS.
|                    |          |                  |                         | It is,     | therefore, | essential       | to analyze |       | in production | the best  |
| ------------------ | -------- | ---------------- | ----------------------- | ---------- | ---------- | --------------- | ---------- | ----- | ------------- | --------- |
|                    |          |                  |                         | deployment | for        | DTs considering |            | their | requirements, | e.g., the |
| Fig. 1. High-level | overview | of an industrial | networking architecture |            |            |                 |            |       |               |           |
desiredentanglement,andtheheterogeneouscharacteristicsin
basedonthePurduemodel.
|     |     |     |     | terms of | computing | and | network | performance |     | of the different |
| --- | --- | --- | --- | -------- | --------- | --- | ------- | ----------- | --- | ---------------- |
layers.NotethatsoftwaredeploymentatLayer0/1isnotalways
theindustrialenvironment,sinceitsadoptionrepresentsabest aviableoptionsince,asdescribedearlier,Layer0/1istypically
practiceinthefield[34].Itsmainpurposeistosplitanindus- limitedtothesoftwarerequiredforthemanufacturingprocess
trial environment in a hierarchical manner, with bottom layers only. Even if an operator got permission to deploy the DT at
hostingOTproductioncomponentswhiletoplayershostingIT Layer0/1,theDTdeploymentwouldnotbesoclear-cutanyway.
controlservers(seeFig.1). Indeed,Layer0/1isnotprovidedwithasabundantcomputing
At Layer 0 and Layer 1, there are machines and PLCs sup- resources as the upper layers. Therefore, DTs deployed there
portingtheactualproductionofgoods.Usually,theselayersare might take resources at the expense of other processes, po-
basedontime-sensitivenetworks(TSNs)connectingindustrial tentiallyunderminingmission-criticaloperationsandhazarding
machines and related PLCs in a fast and reliable manner. In shop-flooroperatorsafety.
fact, the TSNs are characterized by very low communication As a result, the choice of where to deploy a given DT is a
latency(lessthan10ms)torespectcriticalsafetyrequirements challenging tradeoff among the requirements of the DT itself,
of the industrial environment [35]. Given the peculiarity of the characteristics of the target environment, and the current
the OT environment, the TSN should be limited to industrial circumstances. Therefore, we claim that the assessment and
machinesandcompanionsoftwarecomponentsrequiredbythe optimization of DT resilience could greatly benefit from the
manufacturing process only. By following the best practices applicationofpracticesthathaveprovedeffectiveandvaluable
suggestedinIEC62443[11],weclaimthatsoftwarecomponents inlarge-scaleITenvironments,suchaschaosengineering.
suchasDTsshouldbedeployedatLayer0/1onlyifapprovedby
machinemanufacturersandaftercarefulconsiderationsrelated
IV. ASSESSINGDTRESILIENCEWITHCHAOSENGINEERING
| to the safety | of the whole. | On the contrary, | general-purpose |     |     |     |     |     |     |     |
| ------------- | ------------- | ---------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
DTs supporting nonmission-critical applications developed by Evenifchaosengineeringwasinitiallyproposedforthetest-
third parties should not be deployed at these layers to avoid ingofcomplexanddistributedITservices[12],itsapplication
introducingcriticalfailures.Forinstance,intensivemonitoring (as discussed earlier) may bring huge benefits to other appli-
applications for nonreal-time predictive maintenance, which cationdomainsthatrequirehighreliabilityandfaulttolerance.
coulddraintheavailablebandwidthanddelveintopacketloss In the OT domain, chaos engineering methodologies can help
withpossiblesafetyissues,shouldbehostedinupperlayers. improvetheresilienceoftheOTecosystem,byexecutingwhat-if
TheaboveLayer2andLayer3iswherecontrolcomponents experiments to explore their impact on different configuration
reside.Suchcomponentsallowconfiguringindustrialmachines deployments.Forinstance,suchexperimentscanhelpidentify
and PLCs. These layers present increasing communication the minimum set of resources, i.e., computing and network
latencyvalues,usuallyupto25ms.DifferentlyfromtheTSN, devices, that would guarantee the desired working conditions
these layers support the deployment of software components evenincaseofundesirableandunexpectedfaults.
toon-premiseshardware,e.g.,edgeservers.ThisiswhereDTs Fig.2presentsthetargetscenarioofthiswork,withDTsde-
developedbymachinemanufacturersaswellasbythird-party ployedasmicroservicesinanindustrialenvironmentwhereOT
developers can be deployed. DTs deployed at these layers and IT components coexist. An orchestration system manages
are supposed to interact with both users and the industrial DTs,deployedasmicroservices[16]onsite,offsite(e.g.,cloud),
machinesoperatingintheTSN.Therefore,theselayerstendto orboth.Inthiscontext,DTsrepresentthevirtualizedworldof
experienceahighernetworktrafficwhencomparedtothelower adigitalfactory,whereasPOsrepresentthephysicalworld,i.e.,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore.  Restrictions apply.

1138 IEEETRANSACTIONSONINDUSTRIALINFORMATICS,VOL.20,NO.2,FEBRUARY2024
inthecaseoflatency-sensitiveapplications.Chaosengineering
actionstostressthenetworkresourcescouldincreasenetwork
link latency and/or packet loss, or could terminate a whole
networkappliance,e.g.,anetworkswitch.
The computing performance profile considers issues of
workernodesexecutingtheDT,e.g.,bysimulatingthatrequired
computingresourcesareonlypartiallyavailable.Thiscanbeim-
plemented by saturating the computational resources available
forworkernodes.Forexample,theexecutionoffaultyprocesses
designedtobeCPUandmemoryconsumingwouldreducethe
amountofCPUtimeand/ormemorytheDTcanleverage,thus
likely degrading its performance. Let us note that there are
several other methods to affect the performance of DTs, such
asactingontheniceness(inthecaseofUNIXnodes)toassign
a lower priority to the processes associated to the DT. Finally,
in the case of virtualized worker nodes, e.g., virtual machines
(VMs), another approach is to interact with the virtualization
platformAPItodynamicallydecreasetheamountofcomputing
resourcesreservedforworkernodes.
From a resilience perspective, the computing performance
Fig.2. Targetindustrialscenariowhereacontainer-orchestrationsys- profileandthenetworkprofilearecrucialtoestimatetheperfor-
temmanagesmicroservice-basedDTs,eachentangledwiththePO(s) manceofdifferentdeployments,e.g.,toidentifytheminimum
tobecapturedinthevirtualizedworld.
set of resources capable of providing a target QoS level. Let
us note that this factor is important in OT environments since
thetangiblethingsofadigitalfactory.Notethatcompositions, computingandnetworkresourcesatthedifferentlayersusually
orevenhierarchies,ofDTswouldalsobepossible.Asdiscussed haveveryheterogeneouscharacteristics.Moreover,theintensity
above,acomposedDT—aDTbuiltontopofotherDTs—might oftheseprofilesisanimportantelementtobeconsidered.Chaos
require to be entangled with the intangible things it captures. engineering adopters should, based on their expertise, select a
IntheperspectiveofacomposedDT,therefore,suchintangible reasonableconfigurationandintensitythatwouldreflectreal-life
things—theunderlyingDTsontopofwhichitbuildsupon—are failuresandmalfunctioning.
POs. In some cases, therefore, entanglement goes beyond the Thenode/workeravailabilityprofiledescribesthepossibility
merecyber-physicalrelationship. of having multiple failures caused by, e.g., software and hard-
Notableexamplesofreal-worldfaultsincludehardwarefaults ware issues. Such experiments can be implemented by termi-
(both at the computing and at the network appliance level), natingoneormoreworkernodeshostingtheDT.Specifically,
network issues (such as increased communication latency, or theterminationprocesscanbelimitedtotheworkerexecuting
limitedbandwidthlowerthantheactualtrafficthroughputgener- the DT, to other workers the DT interacts with, or both. This
atedbymachines),andapplication(partial)unavailability(e.g., profile allows us to verify the correctness of the deployment
acrashedmicroservice).Thecombinationofthosefaultsleads configuration,i.e.,ifthecomputingresourceswereopportunely
totheconceptofprofile,i.e.,asetoffaultstoinjectintothetarget replicated to be resilient to such failures. Let us specify that
runningsystemthatwouldmakethetargetsystemrunoutsideits while this profile is easy to implement, its application should
steadystateand,thus,likelycausingundesirableeffectsthatwill be tailored to each given scenario. In fact, this profile is very
expose undiscovered software vulnerabilities and architectural effective for testing the performance of highly distributed and
weaknesses. cloud-based IT applications, which can leverage a plethora of
In industrial scenarios, it is possible to identify three main computing resources at different cloud vendors. However, it
chaosengineeringprofilestargetingeachoneadifferentpossible couldbelesseffectivewhendealingwithOTapplications,usu-
issuecategoryrelatedtonetwork,computingperformance,and allynotcharacterizedbyahugenumberofcomputingdevices
worker/nodeavailability.Moreover,chaosengineeringprofiles ifcomparedwithdatacenters.
mayberegardedasdynamiccomponentsthatstartwithabase- Table II provides a list of possible fault actions that chaos
line“intensity”andincreaseitovertimetoputmorestressover engineeringadopterscanusetoimplementprofiles.Specifically,
theDTsundertesting,e.g.,bygraduallyincreasingthelatency thetabledividessuchactionsintomultiplecategoriestodefine
ofacommunicationlink. theactiontarget,e.g.,theapplicationprotocol,theworkernode,
Bydelvingintofinerdetails,thenetworkprofiletargetspacket orthenetwork.Applicationprotocolfaultactionstargetapplica-
dispatchingissuesoftheindustrialenvironment.Inthisregard, tioncomponentsatmultiplelevels.Forexample,theseactions
itisimportanttoevaluateboththeresilienceoftheDTnetwork canmodifyDNSconfigurationstosimulatenamingandservice
and the network connectivity with the PO. For example, an lookuperrorsorcanintroduceerrorsattheWebserverlevel(in
increasedcommunicationlatencycouldbreaktheentanglement thecaseofWeb-basedapplications),suchasadditionalrandom
between the DT and its PO, or it could cause inconsistencies termination of requests. Differently, software component fault
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.

FOGLIetal.:CHAOSENGINEERINGFORRESILIENCEASSESSMENTOFDIGITALTWINS 1139
TABLEII
LISTOFFAULTACTIONSFORCHAOSENGINEERING
actions can terminate or inject failures into a single software nodes. In fact, by targeting one or more replicas with stress
component, e.g., a microservice running on a worker node, testactions,itispossibletoevaluatehowtheapplicationwould
whilehostcomputingfaultactionsexecuteaprocessonatarget respondinthecaseofanonoptimalnumberofreplicasavailable,
worker node requiring a considerable amount of CPU and/or e.g.,bydetectingadecreasedQoS/accuracyforagivenDT.
memory. Host network fault actions can be injected to create Finally, let us point out that it is possible to identify many
network failures at the host level. Such actions allow chaos additional chaos engineering profiles and fault actions to de-
engineeringadopterstointroducepacketdelayandcorruption, scribeandimplementotherpossiblefaults,e.g.,byconsidering
partitions,andbandwidthshapinginaveryfine-grainedmanner. application-dependentandspecificfeaturesofagivenDT.Such
For example, Linux Netfilter provides a set of components to profiles and actions require low-level access to application in-
changealltheseconfigurationparametersatrun-time.HostI/O terfacesandtothecomputingandnetworkresourcesonwhich
fault actions inject failures such as execution delays or errors DTsareexecuting.ItisthereforeimportanttoanalyzeDT-based
while executing system calls. Such actions could be used to distributed OT applications and identify possible actions that
invalidate the readings coming from external devices, e.g., a could implement the desired faults. However, we believe that
human–machine interface (HMI) or a sensor, and to test how thechaosengineeringprofilesandfaultactionsdescribedabove
thefaultydatawouldaffectthereliabilityofthesystem.Finally, are of general applicability and allow us to test a wide set of
other relevant fault actions are related to host configuration DT-basedenvironments.
errors,e.g.,atimesynchronizationmisalignmentinadistributed
application. These actions can be very helpful for testing the V. CASESTUDY
resilienceofapplicationsthatrelyonaccuratetiming.Addition-
Todemonstratethebenefitsofchaosengineeringinassessing
ally,simulatingstoragefailuresbyunmountingattachednetwork
the resilience of DTs, this section presents the experimental
orphysicaldisksmightrepresentusefulactionsreflectingfaults
validationoftheproposedapproachinthetargetscenariopre-
thatarelikelytohappeninareal-worldscenario.
sented in Section IV (see Fig. 2). Specifically, this section
Withregardtotheimplementationofthechaosengineering
illustrates 1) the technologies used to recreate an instance of
profiles, a network profile may be implemented by applying
the target scenario and the testbed that was built accordingly
some actions of the host network category. To do so, a first
(seeSectionV-A)and2)theexperimentsconductedtovalidate
plausiblestepmightconsistofmodifyingthesteady-statenet-
ourproposal,alongwithadiscussionaboutthecollectedresults
worklatencybyintroducinganadditionalpacketdelay,e.g.,an
(seeSectionV-B).
increaseddelayofabout50mstoall(ortoasubsetof)packets
leaving the host network interface. A computing performance
A. ExperimentSetup
profile,instead,maybeimplementedbyapplyingthestresstest
actionsofthehostcomputingcategorytoconsumememoryand We developed a proof-of-concept DT and tested it against
CPUresources.Thisprofilewouldworkwellinthecaseofappli- differentchaosengineeringprofiles.TheDTcapturesarealistic,
cationswhosecomponentsarereplicatedacrossmultipleworker intelligent manufacturing machine that maintains information
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.

1140 IEEETRANSACTIONSONINDUSTRIALINFORMATICS,VOL.20,NO.2,FEBRUARY2024
onmanufacturedproducts.Inthiscase,themachinerepresents vulnerabilitiesofsoftwaresystemsrunninginaproductionenvi-
thephysicalcounterpartoftheDT,i.e.,thePO.ThePOgenerates ronment.Infact,theapplicationofchaosengineeringwellsuits
dataaboutcraftedproducts inaconfigurable fashionsothatit complexmicroservice-basedapplicationswherethefailureofa
ispossibletotunethenumberofcraftedproductsandtherate singlemicroservicecouldunderminetheexecutionofthewhole
atwhichthemachinecraftssuchproducts.ThePOconsistsof distributed application. Chaos Mesh4 was used to inject faults
aShellscriptthatmimicsamanufacturingprocessbasedonthe into our proof-of-concept DT. Chaos Mesh is a cloud-native
input arguments, i.e., the number of crafted products and the chaosengineeringplatformforKubernetesthatallowsinjecting
rate. In turn, the DT is implemented as a web service that ex- abroadspectrumoffaultsintoatarget.
posesastraightforwardRESTfulAPIforregisteringinformation ThetestbedconsistedofaKubernetesclusteroffournodes,
aboutthemanufacturingprocess.Forthesakeofsimplicity,the eachwithinitsownvirtualmachine.Asinglenodeactedasthe
proof-of-conceptDTcommunicatesthroughHTTP.However,it master(i.e.,thenoderunningthecontrolplane)whiletheothers
isworthmentioningthatsomereal-worldDTimplementations joined as workers (i.e., regular cluster nodes). Each VM was
maysupportmoreefficientprotocolsthanHTTPtocommuni- equippedwith2vCPUand2GBofRAM,eachonerunningthe
catewiththeirphysicalcounterparts,suchasMQTT. Ubuntuoperatingsystem.Thewholesoftwarestackwasauto-
The PO was configured to produce one article per second, maticallyinstalledinaconfigurableandreproduciblefashion.In
whichresultedinanHTTPPOSTrequestpersecondsenttothe thisregard,Ansible5wasused,awell-knownconfigurationman-
DT.EachrequestbodycarriedouttwovaluesencodedinJSON, agementtoolthatallowsacontrolnodetoconfigureasetoftarget
i.e.,productiontimestamp(thetimeatwhichthePOproduced nodesoverSSH.ThroughAnsible,theKubernetesclusterwas
thearticle)andID(thearticleserialnumber).Foreachrequest, built(i.e.,Kubernetesalongwiththeancillarysoftwarerequired
the DT 1) computed the elapsed interval between the current byKubernetestorunsuccessfully,suchascri-o6 andFlannel7)
time and the production time, 2) exposed such information as as well as Istio, Prometheus, and Chaos Mesh deployed. To
a Prometheus histogram metric, and 3) stored in memory the foster the research activity in this field, the developed project
detailsaboutthecurrentarticle.ThreereplicasoftheDTwere to configure the testbed has been made publicly available on
deployed,eachoneperiodicallymonitoredtoscrapemetrics. GitHub.8
The microservice-based DT vision requires an underlying It is worth remarking that the whole technology stack (i.e.,
container-orchestrationsystem.Tothispurpose,Kuberneteswas Kubernetes, Istio, Prometheus, and Chaos Mesh) consists of
used—the de facto industry standard container-orchestration open-source, widely-adopted, state-of-the-art solutions. This
system currently. Specifically, Kubernetes is a platform for makesthedevelopedtestbednotonlyconsistentwiththecurrent
automating the deployment, scaling, and management of con- industry trends but also freely available for anyone interested
tainerizedapplications1. in assessing the resilience of DT-based industrial applications
AsthenumberofDTsgrows,sodoesthesystemcomplexity, byadoptingtheproposedchaosengineeringapproach.Inother
requiring a scalable technology stack that adequately supports words, the proposed technology stack allows us to instantiate
the deployment of DTs as microservices. This calls for the DTswithinanindustrialenvironment,e.g.,theonepresentedin
adoptionofasocalledservicemesh,aninfrastructurelayerthat Fig.2,andinjectfaultstoevaluatetheirresilience.
keepspracticalthemanagement,observability,andsecurityof
thewholeenvironment.Servicemeshestypicallyprovidethose B. ExperimentsandDiscussion
capabilities(almost)transparently,i.e.,withno(orfew)service
The network profiles detailed in Table III come from the
codechanges.Inthisregard,Istiowasadopted,whichisarguably
generically applicable chaos engineering profiles presented in
themostpopularsolution.IstioextendsKubernetestoestablish
Section IV. Specifically, such profiles aim at reproducing the
aprogrammable,application-awarenetwork2.
networkconditionsthatmightoccurinanindustrialenvironment
Inadditiontothetechnologystacklayerprovidingthescal-
basedonthePurduemodel(seeSectionIII).Firstofall,TableIII
able deployment of DTs, there is also the need of supporting
definesabaselineforLayers0/1,2,and3ofthePurduemodel.
the monitoring of the environment, in particular to check that
Forinstance,networkprofile1,i.e.,thebaselineforLayer0/1,
everything works as desired. Let us note that the monitoring
isaffectedbyaone-waylatencytotheDTof2.5ms±2.5ms
phaseisparamountfortheOTdomain,sinceDTshavetofulfill
(with a correlation between consecutive packets of 25%) and
strict requirements, e.g., strong entanglement. In this regard,
no packet loss. Then, the baselines are gradually degraded to
Prometheus3 was chosen to scrape metrics from DTs, store
getmoreinformationabouthowtheentanglementvariesasthe
suchmetricsinareal-timetime-seriesdatabase,andquerythe
network conditions worsen at an increased intensity. Finally,
databasetoextrapolateaggregateinsights.
a computing performance profile was also elaborated, which
SincetheintroductionoftheSymianArmytoolkitbyNetflix
randomlytargetsareplicaoutofthenumberoftheDTdeployed
in 2011 [12], several tools have been released that can help
replicasbystressingitwithaCPUloadof100%.
softwaredevelopersandadministratorstodiscoverunexpected
4[Online].Available:https://chaos-mesh.org/
5[Online].Available:https://www.ansible.com/
1[Online].Available:https://kubernetes.io/ 6[Online].Available:https://cri-o.io/
2[Online].Available:https://istio.io/ 7[Online].Available:https://github.com/flannel-io/flannel/
3[Online].Available:https://prometheus.io/ 8[Online].Available:https://github.com/fglmtt/kubemake/
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.

FOGLIetal.:CHAOSENGINEERINGFORRESILIENCEASSESSMENTOFDIGITALTWINS 1141
TABLEIII
NETWORKPROFILESBASEDONTHEPURDUEMODELLAYERS
Fig.3. Effectofthenetworkprofilesontheentanglement. Fig.4. Effectofnetworkprofilescombinedwiththecomputingperfor-
manceprofileontheentanglement.
As discussed in Section IV, the node/worker availability logarithmic scale (base 10). The top x-axis divides the figures
profile is less important than the others for the OT domain intothreeverticalmacrosections,eachrepresentingalayerofthe
because the computing resources available in the OT domain Purduemodel,i.e.,Layer0/1,Layer2,andLayer3.Thebottom
cannotbecomparedtothoseavailableinadatacenter.Accord- x-axis further divides such macrosections based on the chaos
ingly, the experiments focused on the network and computing engineeringprofilestargetingaspecificPurduemodellayer.
performance profiles. It is worth remarking, however, that the Fig. 3 shows the impact of the different network profiles
developedtestbedisflexibleenoughtocoverallofthem.Finally, illustrated in Table III (x-axis) on the entanglement (y-axis).
note that IT operators should tailor the profiles based on the For example, the yellow triangle in the third column (network
conditionstheyexperienceinthefield.Moreover,thisapproach profile 3) of Fig. 3 means that 95% of the HTTP requests had
is not limited to those contexts that strictly follow the Purdue an entanglement of at most 50 ms over the observed 5-min
model.Infact,thenumberofprofilesandhowtoclusterthose window. The results showed that the entanglement worsened
profiles (e.g., Layer 0/1, 2, and 3 as done here) may vary as as the network profile increased in intensity. Under network
necessary. profiles 1, 4, and 7, the entanglement did not practically vary
Chaos Mesh was used to put the above-mentioned profiles foranypercentile.Theonlyexceptionwasthe99.9thpercentile
intoaction.Thenetworkprofilesresultedinnineexperiments, ofnetworkprofile1,wherethe99.9thpercentilealmostdoubled
one experiment for each network profile. Since the computing (42.9 ms) the others (around 25 ms). As the faults injected
performance profile was combined with the network profiles, by network profiles increased in intensity, so did the variance
the computing performance profile also resulted in nine ex- betweenthepercentiles.Inthisregard,themostrepresentative
periments. The rationale was to show the impact of a single caseswerenetworkprofiles3,6,and9.Forinstance,the90th
overloaded replica out of three (two of them almost idle since and 95th percentiles of network profile 3 were around 50 ms,
theproof-of-conceptDTdidnotperformCPU-intensivetasks) whereasthe98th,99th,and99.9thpercentileswere1.80s,2.15s,
combinedwiththenetworkprofilesontheentanglement. and2.47s,respectively.
Figs.3and4showthecollectedresultsfromtheexperiments. The combined effect of the computing performance profile
The results are expressed in percentiles, i.e., 90th, 95th, with the network profiles can further stress the entanglement
98th, 99th, and 99.9th, and computed based on the metrics of DTs, thus making the deployment even more challenging.
Prometheushadscrapedovera5-minwindow.Notethattheleft In this regard, Fig. 4 shows the impact of a single overloaded
y-axisdepictstheentanglementexpressedinmillisecondsona replica out of three on the entanglement. It is worth pointing
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.

1142 IEEETRANSACTIONSONINDUSTRIALINFORMATICS,VOL.20,NO.2,FEBRUARY2024
outthattheoverloadedreplicamovedtheentanglementupward however, is extensible to any given target environment. This
consistently, making any desired entanglement below 70 ms allowsoperatorstoidentifythevulnerabilitiesandweaknesses
difficult(ifnotimpossible)tobeguaranteed.Notethattherange of a DT deployment based on the on-premises scenario. In
between0and100mscatchesmostoftheentanglementvalues particular, operators can evaluate if and where a given DT
in Fig. 3, whereas the most populated range is between 200 should be deployed, taking into consideration the spectrum of
and300msinFig.4.Thecomputingperformanceprofilealso conditionsunderwhichthedeploymentisexpectedtoworkin
| dramatically | impacted | the | highest | percentiles |     | (i.e., 99.9th) | of  | production. |     |     |     |     |     |     |
| ------------ | -------- | --- | ------- | ----------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
the network profiles 2 (from 49.11 ms to 2.07 s) and 5 (from Future research directions will entail comprehensive testing
99.74msto2.29s). of more sophisticated DT solutions, e.g., DTs composed of
WebelievetheseresultscangiveOT/IToperatorsastraight- other DTs, to encourage the large-scale adoption of our ap-
forwardwaytomakepracticaldecisionsaboutwheretodeploy proach. Since this would likely imply a more complex chain
DTswithinthetargetindustrialenvironment.Forexample,letus of dependencies among the software components under chaos
assumethattoensurethesafetyrequirementsaDTmustachieve engineering,theoverallresultwillbemorechallengingtodigest.
200msofentanglementforatleast95%oftherequests.Inthis Aswesoughttodointhiswork,theambitionwillbetoplotthe
case,theoperatorwoulddrawahorizontallineat200ms(the results to make decision-making easier for operators. Further-
target) and find the vertical sections where the 95th percentile more,weplantoinvestigatetheentanglementpropertymorein
consistentlyfallsbelowthatthreshold.InFig.3,forexample,the detail, with the goal of identifying how it can be expressed in
95th percentile (i.e., 95% of the requests had an entanglement numericaltermsasthebasisfordynamicandautonomousDT
of at most 200 ms) is below the threshold (i.e., 200 ms) up to (re-)deployment.
| network | profile 5. | Note | that the | 95th percentile |     | fell far | above |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | -------- | --------------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
the threshold in network profile 6, defined as the worst case REFERENCES
scenarioforLayer2.Asaresult,theoperatorcanbeconfident
|     |     |     |     |     |     |     |     | [1] M.Grieves,“Digitaltwin:Manufacturingexcellencethroughvirtualfac- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
thattheDTwouldberesilienttoanynetworkprofileifdeployed tory replication,” Florida Inst. Technol., Melbourne, FL, USA, White
| at Layer | 0/1. As | mentioned | above, | software |     | deployment |     | at Paper,2014. |     |     |     |     |     |     |
| -------- | ------- | --------- | ------ | -------- | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
Layer 0/1 is not always a viable option since it is typically [2] F.Tao,H.Zhang,A.Liu,andA.Y.C.Nee,“Digitaltwininindustry:State-
|                                                          |     |     |     |     |     |     |     | of-the-art,” | IEEE | Trans. | Ind. Informat., | vol. | 15, no. 4, | pp.2405–2415, |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------ | --------------- | ---- | ---------- | ------------- |
| delimitedtothesoftwarerequiredforthemanufacturingprocess |     |     |     |     |     |     |     | Apr.2019.    |      |        |                 |      |            |               |
onlyandisnotprovidedwithasabundantcomputingresources [3] R.Minerva,G.M.Lee,andN.Crespi,“DigitaltwinintheIoTcontext:A
surveyontechnicalfeatures,scenarios,andarchitecturalmodels,”Proc.
| as the upper | layers. | Therefore, |     | the operator | might | be  | in the |     |     |     |     |     |     |     |
| ------------ | ------- | ---------- | --- | ------------ | ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
IEEE,vol.108,no.10,pp.1785–1824,Oct.2020.
uncomfortablepositionofselectingbetweenfullorpartialDT
|     |     |     |     |     |     |     |     | [4] W.Kritzinger,M.Karner,G.Traar,J.Henjes,andW.Sihn,“Digitaltwinin |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
resilience.TheformerwouldrequiredeployingtheDTatLayer manufacturing:Acategoricalliteraturereviewandclassification,”IFAC-
PapersOnLine,vol.51,no.11,pp.1016–1022,2018.
0/1,takingchargeoftherelateddrawbacks,e.g.,theDTmight
|     |     |     |     |     |     |     |     | [5] Y.Fang,C.Peng,P.Lou,Z.Zhou,J.Hu,andJ.Yan,“Digital-twin-based |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
takeresourcesattheexpenseofhigherpriorityprocesses.The
jobshopschedulingtowardsmartmanufacturing,”IEEETrans.Ind.In-
format.,vol.15,no.12,pp.6425–6435,Dec.2019.
| latter, instead, | would | require | deploying |     | the DT | at  | Layer | 2,          |         |         |                   |     |              |              |
| ---------------- | ----- | ------- | --------- | --- | ------ | --- | ----- | ----------- | ------- | ------- | ----------------- | --- | ------------ | ------------ |
|                  |       |         |           |     |        |     |       | [6] Z. Zhou | et al., | “Secure | and latency-aware |     | digital twin | assisted re- |
wherecomputingresourcesareabundant,butthenetworkmay
|           |             |              |              |        |         |               |     | source                                                                  | scheduling | for         | 5G edge    | computing-empowered |        | distribution  |
| --------- | ----------- | ------------ | ------------ | ------ | ------- | ------------- | --- | ----------------------------------------------------------------------- | ---------- | ----------- | ---------- | ------------------- | ------ | ------------- |
| undermine | the desired | entanglement |              | (e.g., | network | profile       | 6). |                                                                         |            |             |            |                     |        |               |
|           |             |              |              |        |         |               |     | grids,”                                                                 | IEEE       | Trans. Ind. | Informat., | vol. 18,            | no. 7, | pp.4933–4943, |
| Note that | in the case | of           | the combined | effect | of      | the computing |     | Jul.2022.                                                               |            |             |            |                     |        |               |
|           |             |              |              |        |         |               |     | [7] C.Huetal.,“Digitaltwin-assistedreal-timetrafficdatapredictionmethod |            |             |            |                     |        |               |
performanceprofilewiththenetworkprofiles(seeFig.4),even
for5G-enabledinternetofvehicles,”IEEETrans.Ind.Informat.,vol.18,
networkprofile3(i.e.,theworstcasescenarioofLayer0/1)did
no.4,pp.2811–2819,Apr.2022.
notmatchthedesiredentanglementanymore(the95thpercentile [8] A. Castellani, S. Schmitt, and S. Squartini, “Real-world anomaly de-
fell slightly above 200 ms). The entanglement was still below tection by using digital twin systems and weakly supervised learn-
|                                                       |     |     |     |     |     |     |     | ing,”     | IEEE Trans. | Ind. | Informat., | vol. 17, | no. 7, | pp.4733–4742, |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | ---------- | -------- | ------ | ------------- |
| thethresholdfornetworkprofiles4and5,althoughveryclose |     |     |     |     |     |     |     | Jul.2021. |             |      |            |          |        |               |
toitforthelatter. [9] Z.Lv,J.Guo,andH.Lv,“Safetypokayokeinzero-defectmanufactur-
ingbasedondigitaltwins,”IEEETrans.Ind.Informat.,vol.19,no.2,
pp.1176–1184,Feb.2023.
|     |     |     |            |     |     |     |     | [10] H. V. | Dang, M.       | Tatipamula, | and               | H. X. Nguyen, | “Cloud-based | digital         |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ---------- | -------------- | ----------- | ----------------- | ------------- | ------------ | --------------- |
|     |     | VI. | CONCLUSION |     |     |     |     |            |                |             |                   |               |              |                 |
|     |     |     |            |     |     |     |     | twinning   | for structural |             | health monitoring | using         | deep         | learning,” IEEE |
Trans.Ind.Informat.,vol.18,no.6,pp.3820–3830,Jun.2022.
| DTs have  | emerged     | as  | a compelling | topic | in      | industrial    | sce- |           |                   |     |         |            |            |                   |
| --------- | ----------- | --- | ------------ | ----- | ------- | ------------- | ---- | --------- | ----------------- | --- | ------- | ---------- | ---------- | ----------------- |
|           |             |     |              |       |         |               |      | [11] “IEC | 62443: Industrial |     | network | and system | security,” | Int. Electrotech. |
| narios to | make remote |     | monitoring   | and   | control | of industrial |      |           |                   |     |         |            |            |                   |
Commission,Tech.Rep.,2013.
equipmenteasier.However,safety-relatedindustrialconstraints [12] A.Basirietal.,“Chaosengineering,”IEEESoftw.,vol.33,no.3,pp.35–41,
May/Jun.2016.
requirehighperformanceandreliability.Inthisregard,thiswork
|          |                   |     |     |               |     |                |     | [13] F.Poltronieri,M.Tortonesi,andC.Stefanelli,“ChaosTwin:Achaosengi- |     |     |     |     |     |     |
| -------- | ----------------- | --- | --- | ------------- | --- | -------------- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| proposed | chaos engineering |     | to  | inject faults | in  | a coordinated, |     |                                                                       |     |     |     |     |     |     |
neeringanddigitaltwinapproachforthedesignofresilientITservices,”
automated, and replicable manner, with the primary goal of inProc.17thInt.Conf.Netw.ServiceManage.,2021,pp.234–238.
|             |            |     |            |     |         |     |         | [14] “Resilienceengineering:Learningtoembracefailure,”Commun.ACM, |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------- | --- | ------- | --- | ------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| identifying | if a given | DT  | deployment | can | achieve | the | desired |                                                                   |     |     |     |     |     |     |
vol.55,no.11,pp.40–47,Nov.2012,doi:10.1145/2366316.2366331.
| resilience. | Experimental |     | results | collected | through | our | testbed |                 |               |     |           |                |             |       |
| ----------- | ------------ | --- | ------- | --------- | ------- | --- | ------- | --------------- | ------------- | --- | --------- | -------------- | ----------- | ----- |
|             |              |     |         |           |         |     |         | [15] A. Basiri, | L. Hochstein, |     | N. Jones, | and H. Tucker, | “Automating | chaos |
based on widely-adopted, open-source tools demonstrated the experiments in production,” in Proc. IEEE/ACM 41st Int. Conf. Softw.
Eng.:Softw.Eng.Pract.,2019,pp.31–40.
feasibilityoftheproposedapproach.
|     |     |     |     |     |     |     |     | [16] F.SiqueiraandJ.G.Davis,“Servicecomputingforindustry4.0:State |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
This work also defined chaos engineering profiles tailored oftheart,challenges,andresearchopportunities,”ACMComput.Surv.,
for a Purdue-based industrial environment. The approach, vol.54,no.9,pp.1–38,Oct.2021.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore.  Restrictions apply.

FOGLIetal.:CHAOSENGINEERINGFORRESILIENCEASSESSMENTOFDIGITALTWINS 1143
[17] Z. Wang et al., “Mobility digital twin: Concept, architecture, case Carlo Giannelli (Senior Member, IEEE) re-
study, and future challenges,” IEEE Internet Things J., vol. 9, no. 18, ceivedthePh.D.degreeincomputerengineer-
pp.17452–17467,Sep.2022. ingfromtheUniversityofBologna,Italy,in2008.
[18] L. Li, S. Aslam, A. Wileman, and S. Perinpanayagam, “Digital twin He is currently an Associate Professor in
in aerospace industry: A gentle introduction,” IEEE Access, vol. 10, computersciencewiththeUniversityofFerrara,
pp.9543–9562,2022. Ferrara,Italy.Hisprimaryresearchinterestsin-
[19] V.Damjanovic-BehrendtandW.Behrendt,“Anopensourceapproachto clude Industrial Internet of Things, digital twin
thedesignandimplementationofdigitaltwinsforsmartmanufacturing,” (DT)management,software-definednetworking
Int.J.Comput.Integr.Manuf.,vol.32,pp.366–384,2019. (SDN), Blockchain technologies, and cyberse-
[20] M. Azarmipour, H. Elfaham, C. Gries, T. Kleinert, and U. Epple, “A curityinIndustry4.0.
service-basedarchitecturefortheinteractionofcontrolandMESsystems
inIndustry4.0environment,”inProc.IEEEInt.Conf.Ind.Informat.,2020,
pp.217–222.
[21] F. Arraño-Vargas and G. Konstantinou, “Modular design and real-time
simulators toward power system digital twins implementation,” IEEE
Trans.Ind.Informat.,vol.19,no.1,pp.52–61,Jan.2023.
[22] A.Bécue,E.Maia,L.Feeken,P.Borchers,andI.Praça,“Anewconcept
ofdigitaltwinsupportingoptimizationandresilienceoffactoriesofthe Filippo Poltronieri (Member, IEEE) received
future,”Appl.Sci.,vol.10,no.13,Jun.2020,Art.no.4482. thePh.D.degreeincomputerengineeringfrom
[23] P.Eirinakisetal.,“Cognitivedigitaltwinsforresilienceinproduction:A theUniversityofFerrara,Ferrara,Italy,in2021.
conceptualframework,”Information,vol.13,no.1,Jan.2022,Art.no.33. He is currently an Assistant Professor with
[24] I.Errandonea,S.Beltrán,andS.Arrizabalaga,“Digitaltwinformainte- the Department of Engineering, University of
nance:Aliteraturereview,”Comput.Ind.,vol.123,2020,Art.no.103316. Ferrara. In 2016, 2017, and 2018, he visited
[25] E. Brucherseifer, H. Winter, A. Mentges, M. Mühlhäuser, and M. the Florida Institute for Human and Machine
Hellmann, “Digital twin conceptual framework for improving criti- Cognition(IHMC),Pensacola,FL,USA.Hisre-
cal infrastructure resilience,” Automatisierungstechnik, vol. 69, no. 12, searchinterestsincludedistributedsystems,op-
pp.1062–1080,2021. timization techniques for network and service
[26] G.CainelliandL.Rauchhaupt,“Introducingresilienceinindustrial5G management, edge and cloud computing, and
systems using a digital twin approach,” in Proc. 17th IEEE Int. Conf. tacticalnetworks.
FactoryCommun.Syst.,2021,pp.33–36.
[27] K. T. Park, Y. H. Son, S. W. Ko, and S. D. Noh, “Digital twin and
reinforcementlearning-basedresilientproductioncontrolformicrosmart
factory,”Appl.Sci.(Basel),vol.11,no.7,Mar.2021,Art.no.2977.
[28] R.Vrabicˇ,J.A.Erkoyuncu,M.Farsi,andD.Ariansyah,“Anintelligent
agent-basedarchitectureforresilientdigitaltwinsinmanufacturing,”CIRP
Ann.Manuf.Technol.,vol.70,no.1,pp.349–352,2021.
[29] A.Thelenetal.,“Acomprehensivereviewofdigitaltwin—Part1:Model- CesareStefanelli(Member,IEEE)receivedthe
ingandtwinningenablingtechnologies,”Struct.MultidisciplinaryOptim., Ph.D. degree in computer science engineering
vol.65,no.12,2022. fromtheUniversityofBologna,Bologna,Italy,in
[30] A.Thelenetal.,“Acomprehensivereviewofdigitaltwin—Part2:Roles 1996.
ofuncertaintyquantificationandoptimization,abatterydigitaltwin,and HeiscurrentlyaProfessorofComputerSci-
perspectives,”Struct.MultidisciplinaryOptim.,vol.66,no.1,2023. enceEngineeringwiththeUniversityofFerrara,
[31] “Representative use cases and key network requirements for network Ferrara,Italy.Hisresearchinterestsincludedis-
2030,” Int. Telecommun. Union, Tech. Rep. TR-FG-NET2030 tributed and mobile computing in wireless and
Sub-G1 (2020), 2022. Accessed: Oct. 6, 2022. [Online]. Available: ad hoc networks, network and systems man-
https://www.itu.int/en/ITU-T/focusgroups/net2030/Documents/ agement,andnetworksecurity.
Technical_Report.pdf
[32] H.Yang,A.Alphones,W.-D.Zhong,C.Chen,andX.Xie,“Learning-
basedenergy-efficientresourcemanagementbyheterogeneousRF/VLC
forultra-reliablelow-latencyindustrialIOTnetworks,”IEEETrans.Ind.
Informat.,vol.16,no.8,pp.5565–5576,Aug.2020.
[33] A.E.Kalør,R.Guillaume,J.J.Nielsen,A.Mueller,andP.Popovski,“Net-
workslicinginIndustry4.0applications:Abstractionmethodsandend-to-
endanalysis,”IEEETrans.Ind.Informat.,vol.14,no.12,pp.5419–5427, MauroTortonesi(Member,IEEE)receivedthe
Dec.2018. Ph.D.degreeincomputerengineeringfromthe
[34] P.Koprov,A.Ramachandran,Y.-S.Lee,P.Cohen,andB.Starly,“Stream- UniversityofFerrara,Ferrara,Italy,in2006.
ingmachinegenerateddataviatheMQTTsparkplugBprotocolforsmart HewasaVisitingScientistwiththeFloridaIn-
factoryoperations,”Manuf.Lett.,vol.33,pp.66–73,2022. stituteforHuman&MachineCognition(IHMC),
[35] Y.Luetal.,“Anintelligentdeterministicschedulingmethodforultralow Pensacola, FL, USA, from 2004 to 2005, and
latency communication in edge enabled industrial Internet of Things,” withtheUnitedStatesArmyResearchLabora-
IEEETrans.Ind.Informat.,vol.19,no.2,pp.1756–1767,Feb.2023. tory,Adelphi,MD,USA,in2015.Heiscurrently
anAssociateProfessorwiththeDepartmentof
MattiaFogli(GraduateStudentMember,IEEE) MathematicsandComputerScience,University
received the M.Sc. degree in computer engi- ofFerrara.Hehascoauthoredmorethan90ar-
neeringin2020fromtheUniversityofFerrara, ticlesinthedistributedsystemsresearcharea,withparticularreference
Ferrara,Italy,whereheiscurrentlyworkingto- toIoTsolutionsinindustrialandmilitaryenvironments,CloudandFog
wardthePh.D.degreeincomputerengineering. computing,wirelessmiddleware,andITservicemanagement.
He was a Research Intern with the Florida
InstituteforHumanandMachineCognition,FL,
USA,from2019to2020.Hisresearchinterest
include federated cloud infrastructures for tac-
tical networks, software-defined networking in
wirelessadhocscenarios,anddigitaltwinsfor
Industry4.0.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 18,2026 at 04:18:58 UTC from IEEE Xplore. Restrictions apply.