PDF Download
3772052.3772244.pdf
23 March 2026
Total Citations: 0
. Total Downloads: 118
.
Latest updates: hps://dl.acm.org/doi/10.1145/3772052.3772244 .
.
Published: 13 January 2026
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
PerfMon: Performance Monitoring of Host Network Stack
.
.
SoCC '25: ACM Symposium on Cloud
Computing
RANJITHA K., Indian Institute of Technology Hyderabad, Sangareddy, TG, India
November 19 - 21, 2025
. Online, USA
ANKIT SHARMA, Indian Institute of Technology Hyderabad, Sangareddy, TG, India
.
. . Conference Sponsors:
MALSAWMSANGA SAILO, Indian Institute of Technology Hyderabad, Sangareddy, TG, India
SIGOPS
. SIGMOD
ARUN SIDDARDHA, Indian Institute of Technology Hyderabad, Sangareddy, TG, India
.
AMRIT KUMAR, Indian Institute of Technology Hyderabad, Sangareddy, TG, India
.
PRAVEEN TAMMANA, Indian Institute of Technology Hyderabad, Sangareddy, TG, India
.
View all
.
.
Open Access Support provided by:
.
Indian Institute of Technology Hyderabad
.
IBM Research
.
SoCC '25: Proceedings of the 2025 ACM Symposium on Cloud Computing (November 2025)
hps://doi.org/10.1145/3772052.3772244
ISBN: 9798400722769
.

PerfMon: Performance Monitoring of Host Network Stack
RanjithaK AnkitSharma MalsawmsangaSailo ArunSiddardha∗
IITHyderabad IITHyderabad IITHyderabad IITHyderabad
India India India India
AmritKumar∗ PraveenTammana PraveinGovindan PriyankaNaik
IITHyderabad IITHyderabad Kannan IBMResearch
India India IBMResearch India
India
Abstract 1 Introduction
Moderncloudapplicationsarerefactoredintomicroservices,which Cloudapplicationsarerefactoredintomultiplemicroservicesdis-
aredeployedascontainersacrossmultipleservers.Anend-user tributedacrossphysicalorvirtualnodes.Theseapplicationsgener-
requestoftentriggersseveralremoteprocedurecalls(RPCs)be- allyhaveonepublic-facingorfront-endservicethathandlesuser
tweenthesemicroservices.RPClatencyanomaliescausedbypacket- requestsbycommunicatingwithseveralothermicroservicesusing
processingdelays(bottlenecks)inthehostnetworkstackarecom- remoteprocedurecalls(RPC).Typically,auserrequestcomprises
mon.Bottlenecksatafewnetworkcomponentscancompound multipleRPCs,witheachRPCtraversingacomplexpaththatin-
acrossservices,causingSLAviolationsformanyrequests. cludesmultipleentities-thesourceanddestinationend-hostnodes,
DiagnosingRPClatencyanomaliesischallengingbecausemany and the underlying network. Within an end-host node, the RPC
host-levelcomponentscancontributetothedelay.Identifyingthe traversesmultiplecomponentsinthehostnetworkingstack-the
bottleneckcomponentisacrucialfirststep.However,itoftentakes containernetworkstack,thehostnetworkstackintherootnamespace,
significantmanualeffortandexpertisetofindthebottleneckcompo- andthenetworkinterfacestack(Fig.1).
nentduetothelackofvisibilityonper-componentprocessingtime. Requestlatencyanomalies(userrequeststakinglongertofinish)
Inthispaper,wepresentPerfMon,alightweightsystemdesignedto arecommonincloudapplications[9,15]duetotheirdistributedna-
monitortheperformanceofcomponentsinthehoststackthatauto- ture.Manyrecentworks[9,15,21,34,37,39]haveshownthatspo-
maticallyidentifiesthebottleneckcomponent.WedevelopPerfMon radictransientpacket-processingdelayswithinthehostnetwork
usingeBPFtechnologyandevaluateitonaKubernetes-managed stackcanincreaserequestcompletiontimebytensofmilliseconds.
clusterofbaremetalservers.OurevaluationdemonstratesthatPerf- Moreover,delaysatafewcomponentscancompound,eventually
Monintroducesminimalmonitoringoverheadswhileaccurately leadingtoSLAviolationsonthecompletiontimeofmanyuser
identifyingthebottleneckcomponents. requests.DebuggingsuchSLAviolationsisbothchallengingand
time-consuming,astherearemultiplecomponentsalongthere-
CCSConcepts questpathtosuspect.Thechallengeisfurthercompoundedbythe
transientandsporadicnatureofthesedelays.Therefore,accurately
•Networks→Cloudcomputing;Networkmonitoring.
identifyingthebottleneckcomponent,especiallywithinthehost
stack,isacrucialfirststeptowarddiagnosingtheissue.Inpractice,
Keywords
duetoalackoffine-grainedandend-to-endvisibility,theblame
networkstackmonitoring,RPCperformancemonitoring gameacrosstheteams(application,server,network)continuesun-
tiltherespectiveteamisproveninnocent[37],whichtakesalot
ACMReferenceFormat: oftimebeforetheissueisassignedtotheappropriateteam.Itis
RanjithaK,AnkitSharma,MalsawmsangaSailo,ArunSiddardha,Amrit crucialtohaveaperformancemonitoringsystemthatprovides
Kumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik. end-to-endvisibilityandautomaticallyidentifiesthebottleneck
2025.PerfMon:PerformanceMonitoringofHostNetworkStack.InACM
componentcausingRPClatencyanomalies.
SymposiumonCloudComputing(SoCC’25),November19–21,2025,Online,
Theexistingperformancemonitoringsystemsoperateeitherat
USA.ACM,NewYork,NY,USA,13pages.https://doi.org/10.1145/3772052.
theapplicationleveloratthehostlevel.Application-levelmoni-
3772244
toringsystems[5,13,19,35,43,45,50]performdistributedtracing
andprovidethetimespentateachmicroservice.Whilethishelps
identifywhichRPCsexperienceddelays,itlacksthegranularity
∗WorkdonewhileatIITHyderabad
neededtopinpointthespecificcomponentwithinthehoststack
responsibleforthosedelays.Ontheotherhand,end-hosttracing
approaches[11,12,16,22,33,39]providedeepvisibilityintothe
hostnetworkstack.However,theyareprimarilydesignedforafter-
the-factanalysisratherthanthecontinuousmonitoringneededto
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense.
SoCC’25,Online,USA detecttransientandsporadicdelays.Always-ontracecollection
©2025Copyrightheldbytheowner/author(s). imposessignificantprocessingandstorageoverhead,makingit
ACMISBN979-8-4007-2276-9/2025/11
https://doi.org/10.1145/3772052.3772244
430

SoCC’25,November19–21,20R2a5n,jOithnalinKe,,AUnSkAitSharma,MalsawmsangaSailo,ArunSiddardha,AmritKumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik
vethpair
virtual switch
(bridge)
RNS TCP/IP
netdev subsystem
(driver, IRQ, NAPI polling,
qdisc, GSO, GRO)
hardware NIC
NIS
1dop
ppA
TCP/IP
vethpair
virtual switch
(bridge)
netdev subsystem
(driver, IRQ, NAPI polling,
qdisc, GSO, GRO)
hardware NIC
2dop
ppA
3dop
ppA
ndop
ppA
CNS
RNS TCP/IP
NIS
network
1dop
ppA
TCP/IP
2dop
ppA
3dop
ppA
ndop
ppA
Node N1 Node N2 anomaly when the observed processing time deviates from the
expectedtimeusingapredefinedthreshold.Arrivingattheright
thresholdischallengingduetotheheterogeneityindeployments
(multipleinstancesofeachservicearedeployedacrossnodesina
clusterwithmultipleRPCtypesanddifferentcomponent-specific
processingtimes).Athresholdvaluethatistoolowcanincrease
CNS thedatacollectionoverheadandfalsepositives,whereasahigh
thresholdcanmisslatencyanomalies,increasingfalsenegatives.We
addressthisbycarefullyprofilingapplicationRPCsundervarious
workloadsandderivingthresholdsthatstrikeabalancebetween
overheadandaccuracy(detailsin§4.2)
C3.Distinguishinganomalyfromnoise. Thethirdchallenge
isdistinguishingtransientandsporadiclatencyanomaliesfrom
noise(e.g.,jitter).Otherwise,PerfMoncouldraisefalsepositives,
producingalertsthatarenotrelevant.Weaddressthisproblem
usingasmoothingfactorthatabsorbsthenoisewhiledetectingab-
normaldelaysandreportsonlyrelevantalertsrepresentinglatency
anomalyevents(detailsin§5).
Thekeycontributionsofthispaperare:
• WedesignPerfMon,aperformancemonitoringsystemthat
enablesautomaticidentificationofbottleneckcomponents
withinthehostnetworkstackresponsibleforRPClatency
Figure1:AnRPCrequestandresponsetraversemultiple
anomalies.
entities-N1,N2,andnetwork.Withineachnode,ittraverses
• WeprototypePerfMonanddeployitonaKubernetes-managed
host-levelcomponents-CNS(containernamespace),RNS
serverclusterrunningamicroservice-basedapplicationfrom
(Rootnamespace),andNIS(networkinterfacespace).
DeathStarBench[14],anopensourcebenchmarksuite.Perf-
impracticalforreal-timeuseinproductionenvironments.Oneal-
Monprototypeisavailableat1.
ternativeistosampleormonitorperiodically,butitishardtoknow • WeevaluatePerfMonrunningontheKubernetesclusterand
whentocollecttracesandhowlong,sotheyoftenfailtodetect observethatitintroducesminimalmonitoringoverheads
sporadicandtransienteventscausingbottlenecks(morein§2). whileaccuratelydetectingabnormaldelayeventswithalow
We propose PerfMon, a system that complements the exist- falsepositiverate.At40%applicationload(representingthe
ingapplication-levelmonitoringsystemswithfine-grainedper- baselineaverageload),theP999requestcompletiontime
formancemonitoringofthecomponentswithinthehostnetwork.
increasesbyonly0.9%.Additionally,whilescalingwitha
PerfMonenablestheidentificationofthebottleneckcomponent largenumberofconcurrentflows(onemillionconcurrent
causingRPClatencyanomalies,significantlyacceleratingthedebug- flows),PerfMonincursonly3%dropinthroughput.
gingprocess.Thekeyideaistocontinuouslymonitortheprocessing
2 BackgroundandMotivation
timeofeachcomponentinthehoststackandreportbottleneck
component details when the processing time takes longer than 2.1 SLAviolationduetoslowRPCs
expected.Thisapproachkeepstheresourceoverheadslowwhile
Userrequeststomicroservice-baseddistributedapplicationsgen-
accuratelydetectingabnormalevents.Werealizethisideausing
erallygotoafront-endmicroservice,whichtheninvokesmulti-
lightweighteBPFprogramsdeployedatvarioushookpointsinthe
plebackendmicroservicesrecursivelyviaremoteprocedurecalls
Linuxkernel.
(RPCs).EachRPCrequestandresponsetraversesmultipleend-host
WhiledevelopingPerfMon,weaddressthreemainresearchchal-
nodesandnetworkdevicesalongitspath.
lenges.
Host-levelcomponents.Withineachend-hostnode,anRPCre-
C1.Identifyingandinstrumentingtherelevantcomponents.
quest traverses multiple components in the host network stack
Thefirstchallengeisdeterminingwhichcomponenttimestamps
atboththesenderandthereceiver,asshowninFig.1.Thecom-
tocollectwithinthehoststackandhowtomaintainthemtoac-
ponents include: (1) the root network stack (RNS) in the host’s
curatelyidentifythebottleneckcomponent.Weaddressthisby
rootnamespace;(2)thecontainernetworkstack(CNS)withinthe
understandingthecomponentsapackettraversesinthehostnet-
container namespace; and (3) the network interface stack (NIS)
workstackandinstrumentingthesecomponentstocomputetheir
associatedwiththephysical/virtualNIC.
processingtime.PerfMoncontinuouslymonitorstheprocessing
Userrequeststakinglongertofinish,leadingtoanSLAviolation,
timeofpacketsinbothdirections(dataandacks)andraisesalerts
oftenresultfromoneormoreoftheunderlyingRPCsexperiencing
wheneverabnormaldelaysaredetected(detailsin§4.1).
unexpecteddelays.OperatorsoftenstruggletodebugsuchSLA
C2.Balancingdetectionaccuracyandoverhead. Thesecond violationsbecauseabottleneckatanyofthehost-levelcomponents
challenge is ensuring that PerfMon’s abnormal delay detection
approachisbothaccurateandefficient.PerfMondetectsalatency 1https://github.com/networked-systems-iith/PerfMon-SoCC
431

PerfMon:PerformanceMonitoringofHostNetworkStack SoCC’25,November19–21,2025,Online,USA
|                |     |          |           |          |                 | RPC request |           | increased span due to issue at ??? |                 |     | RPC response |
| -------------- | --- | -------- | --------- | -------- | --------------- | ----------- | --------- | ---------------------------------- | --------------- | --- | ------------ |
| client request |     |          |           |          | client response |             |           |                                    |                 |     |              |
| 1              |     |          |           |          |                 | 12          |           |                                    |                 |     |              |
|                |     |          | front-end |          |                 | r s v       | e         |                                    | serviceA        |     | e v r s      |
|                |     |          |           | r        | r s             | r           |           |                                    |                 |     |              |
| r ss           |     |          |           | s        |                 | s N1        |           |                                    |                 |     |              |
|                | 2   |          |           |          |                 |             |           |                                    | serviceB        |     |              |
|                |     | serviceA |           | 7 8 9    | 10              | 11          |           |                                    |                 |     |              |
| trace          | r s |          | r s       | r s r s  | r               | s           | N2 e      | v                                  | r s             | v e |              |
|                | 3   |          | 5         | serviceD | serviceE        |             |           |                                    |                 |     |              |
|                |     |          | 4         | 6        |                 |             |           | CNS issue                          | span unaffected |     |              |
|                |     | r s      | r s       |          |                 |             |           |                                    |                 |     |              |
| span           |     | serviceB | serviceC  |          | r receive       | e ext       | r receive | CNS time                           |                 |     |              |
|                |     |          |           |          | s send          | v veth      | s send    | RNS time                           |                 |     |              |
anomaly
(a)ApplicationtracewithspansofassociatedRPCs (b)Tracewithspansofhost-levelcomponents
Figure2:Applicationtrace(left)lacksvisibilityintothehoststack.Tracewithcomponent-levelspan(right)isdesired.
Span -time taken by a single microservice
Trace -end-to-end request comprising of single/multiple spans
(eitheratthesenderorthereceiver),orabottleneckintheunderly- Table1:Issuesathost-levelcomponents
ingnetworkorintheapplication,couldleadtohighRPCdelays.
ApplicationtracingtoolslikeJaeger[13]providethespanandtrace Bottleneck Reasonfor Details
ofuserrequests(Fig.2a),wherethespanisthetimeasinglemi- compo- request
croservicetakestoexecuteanRPC,andthetracecontainsspansof nent latency
allRPCsinvokedonbehalfoftheuserrequest.Thishelpsidentify anomaly
issuesattheapplicationlevelandRPCsthattooklongertofinish.
|                                                              |     |     |     |     |     |     |     | Incast  | When multiple                   | senders | send traf- |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------- | ------- | ---------- |
| However,applicationtracingtools[5,13,19,35,43,45,50]lackvis- |     |     |     |     |     | NIS |     |         |                                 |         |            |
|                                                              |     |     |     |     |     |     |     | [31,37] | fictothesamereceiver,packetsget |         |            |
ibilityintodelaysoriginatingfromthehoststackandthenetwork.
queuedattheNICRxbufferasthe
Conversely,bottlenecksatthenetworklevelarediagnosedusing
end-hostnetworkstackstrugglesto
networktelemetrytools[38,40,42,44,48,51].Inthispaper,we
processthepackets.
focusonlocalizingbottlenecksintheend-hoststack,whichhappen
easilybutaredifficulttomitigateandtroubleshoot. Unexpected UnexpectedCPUinterferencefrom
RNS
|     |     |     |     |     |     |     |     | interfer- | system calls | delays | scheduling |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------ | ---------- |
2.2 Host-levelbottlenecksinflateRPClatency ence at netdev_subsystem processes (e.g.
|     |     |     |     |     |     |     |     | CPU core | ksoftirqthread)slowingreadsfrom |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------------------- | --- | --- |
Table1listtheeventsathost-levelcomponentsleadingtoRPCla-
|     |     |     |     |     |     |     |     | [9,15] | NICRxbuffers,causingdelaysup |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------------- | --- | --- |
tencyanomalies.Thetwoleadingcausesforbottlenecksare(1)un-
to100sofmilliseconds.
expectedCPUschedulingduetointerferenceand(2)trafficbursts.
Unexpected CPU scheduling. CPU interference causes unex- CNS CPU Due to CPU starvation, the appli-
|     |     |     |     |     |     |     |     | polling | cationcorereadsthedatafromthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------------------- | --- | --- |
pectedCPUscheduling,leadingtoCPUstarvation(duetoHOL
|     |     |     |     |     |     |     |     | hang[37] | TCPreceivebufferslowly. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------------- | --- | --- |
blockingatthescheduler’sreadyqueue),furthercausingbuffer
build-upatdifferentbuffers(suchasNIXRxbuffer,CNSsocket Burst[53] Amicroburstofrequeststoanap-
buffer).Arecentwork,nSight[39],observedthatunexpectedCPU plicationpodfillstheTCPreceive
schedulingandHOLblockingcanintroduceupto5msdelay.Simi-
buffer.
larly,unexpectedCPUinterferencefromsystemcallsdelayedthe
ksoftirqthread,slowingreadsfromtheNICRxbufferanddelaying
RPCpacketsuptotensofmilliseconds[9,15].
|     |     |     |     |     |     | identifyslowRPCs(Fig.2a)among |     |     | allRPCs | invoked.However, |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | ------- | ---------------- | --- |
Incastandmicroburst.Asuddenburstofincomingoroutgoing theydonotprovidethefine-grainedvisibilitynecessarytoiden-
requestscancausebufferbuildupattheNIC,RNS,andCNS.An
tifythebottlenecknetworkstackcomponentinflatingRPCs.More
| incast of many | requests | to  | an application | pod from | other | pods |     |     |     |     |     |
| -------------- | -------- | --- | -------------- | -------- | ----- | ---- | --- | --- | --- | --- | --- |
specifically,serviceB’sspancapturestherequestprocessingtime
causesbufferbuildupattheNICRx[31]andCNSsocketbuffer
attheapplicationlevelbutdoesnotincludethetimespentinN2’s
[53],eventuallyinflatingRPClatency.AtRNS,ahightrafficrate
CNS,RNS,andNIS.Ontheotherhand,serviceA’sspanincludes
orburstfromoneormoreoutgoingflowscausesbufferbuildup (1)thetimespentinCNS,RNS,andNISatbothN1andN2;(2)
(formingastandingqueueatQDisc)[2,53].
thetimespentintheunderlyingnetwork;and(3)serviceB’sspan.
However,itlacksthefine-grainedvisibilitynecessarytoidentify
2.3 Identifyingbottleneckcomponent
thebottleneckcomponentatN2(e.g.,CNSissueinFig.2b).
Needforfine-grainedhost-stackvisibility.Assumethatser- GivenanRPClatencyanomalyasdiscussedabove(e.g.,serviceA
viceAandserviceBfromFig.2aaredeployedonnodeN1andN2, toBinFig.2a),identifyingtheentity(sender,receiver,ornetwork)
respectively,asshowninFig.1.ConsiderthattheRPCfromser- andassociatedbottleneckcomponent(CNS,RNS,orNIS)isthefirst
viceAtoserviceB(3-4)isdelayedduetoahost-levelbottleneck andmostcrucialsteptowardfixingtherootcause.Inpractice,this
atN2.Consequently,theassociateduserrequestobservedanSLA isoftenatediousandcontentiousprocess.Mostoften,application
violation.Withtheexistingapplicationtracingapproaches,wecan teamsblametheserverornetworkteamsfordelays[37],andthe
432

SoCC’25,November19–21,20R2a5n,jOithnalinKe,,AUnSkAitSharma,MalsawmsangaSailo,ArunSiddardha,AmritKumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik
blamegamepersistsuntileachteamprovesitisnotatfault.A Solutions based on continuous trace collection have high
significantamountoftimeiswastedjustassigningresponsibility overheadsorrequirespecifichardware.Onecommonapproach
tothecorrectteambeforedebuggingcanevenbegin.Streamlining istomanuallycollectandanalyzepcap-liketracesateachcompo-
this process requires having a tool that can automatically iden- nent’singressoregressatboththesenderhostandthereceiver
tifytheentityandthecomponentresponsiblefortheissue.With host[9,15,21,34].Thisisfollowedbycollectingandanalyzinghost-
suchatool,engineerscanimmediatelybeginfocuseddebugging leveltraces[11,12,16,22,25,33,39](e.g.,perf,kprobes,intel-pt)to
bycollectingandanalyzingcomponent-specifictraces(e.g.,perf findtherootcause.Thisapproachprovidesdeepvisibilityintohost-
record[8])insteadofspendingmanyman-hoursoncollectingand levelevents,andsuchtoolsarewellsuitedforafter-the-factroot
analyzingtracesfromallcomponentsacrossentities,asdiscussed causeanalysis,butnotforalways-onmonitoringbecauseoftheir
inblogs[9,15]andpriorresearchwork[37,39]. highprocessingandstorageoverheads.Forinstance,NSight[39]
collectstracesusinghardwareprofilingtoolcalledintel_pt[25],
whichrequires1GBofstoragespacefor1minute.Onealternative
2.4 Challengesinidentifyingbottleneck
istooffloadmonitoringcomputation[37]tospecializedhardware
component such as smartNICs, but this hinders the deployment because it
Twofeaturesmakebottleneckcomponentidentificationchallenging requiresupgradationtospecifichardware.
F1:Bottleneckshappenatanyhost-levelcomponent.The
3 Design
bottleneckcomponentcouldbeintheRPC’ssenderhostnetwork
stack,thereceiverhostnetworkstack,orboth.Findingwhichcom- WedesignPerfMontoidentifythebottleneckcomponentaccurately
ponentinthehostnetworkstackiscausingSLAviolationisnon- whilekeepingthecomputeandstorageoverheadslow.Thispaper
trivial[9,15,21,34]becauseitrequiresfine-grainedinstrumen- focusesonRPCsusingTCPastheunderlyingtransportprotocol,
tationcapableofmonitoringprocessingtimeateachcomponent whichisthemajoritycaseinpractice.Oneapproachistocapture
acrossmultiplehosts. fine-grainedper-packetlogsofTCPconnectionsateveryhost,such
F2:Bottleneckeventsaresporadicandtransient.Eventsthat asRTTandper-componenttimestampsinbothdirectionsandana-
causebottlenecksareusuallysporadicandtransient.(i)Sporadic lyzethetimespentateachcomponent.Moreover,continuousRTT
because they occur randomly at unpredictable times [15]. Any monitoringofeveryRPC’sTCPpacketgivesagoodestimateof
RPCandassociatedpacketsprocessedduringthebottleneckevent
end-to-enddelay[32]asitcoversthetimespentintheentities(i.e.,
observeperformancedegradation.Thus,themonitoringsystem hostnetworkstack,andtheunderlyingnetwork).Thisapproach
mustcaptureperformancedataofeveryRPCatallcomponents. canaccuratelyrecordtransientandsporadicbottleneckevents,but
(ii)Transientbecausetheydisappearquickly[9].Therefore,the collecting,maintaining,andanalyzingper-packetlogshashigh
monitoringsystemshouldmaintainfine-grainedinformation(e.g., computeandstorageoverheads.Also,onlyafewpacketlogsare
component,timestamp)ofabnormaldelayssothatthebottleneck relevanttothebottleneckevent,whereastherestaddsignificant
componentcausinganSLAviolationcanbeidentifiedaccurately. overheadwithoutcontributingusefuldiagnosticinformation.An
alternativeistocollectonlyrelevantlogs.Butitisextremelychal-
lengingtoknowwhentostartcollectinglogsandhowlongbecause
2.5 Existingsolutionsfallshort ofthesporadicandtransientnatureoftheevents.
PerfMonaddressesthisproblembasedonthedesignprinciple
Solutionsbasedonend-to-endlatencymonitoringareinsuffi-
thatcapturerelevantlogsattherighttime followingdistributed
cient.Distributedapplication-leveltracingtoolssuchasJaeger[13],
monitoring.Thekeyideaistocontinuouslymonitorper-packet
jcallgraph[45],andxtrace[35],measurethetimeauserrequest
spendsateachmicroservice(i.e.,span),providingvisibilityatthe RTTandcomponent-levelprocessingtimeandcapturerelevant
logsonlywhentheydeviatefromnormalbehavior;thatis,theyare
applicationlevel,butlackcomponent-levelprocessingtimevisi-
foundtobeabnormal.Thisapproachkeepstheresourceoverheads
bility.AnalternativeapproachistomonitorTCPstatistics[27,28,
lowwhileaccuratelydetectingtransientandsporadicdelayevents.
46,50,53]ofapplicationtrafficorprobetrafficandidentifythe
WerealizethisideausinglightweighteBPFprogramsdeployedat
problematicentity,suchastheapplication,thehoststack,andthe
varioushookpointsintheLinuxkernel.eBPFallowssafeandsecure
network.However,thisapproachwouldnotprovidethenecessary
extensionswithoutchangingthekernelsourcecodeorloading
visibilitytoidentifythebottleneckcomponentinsidethehoststack
kernelmodules.Theabilitytorunprogramsinkernelspaceenables
(F1).
massiveefficiencygainsofupto10x[26]fasterexecutionwhen
Solutionsbasedonstatisticscollectedatcoarsetimescalesare
comparedtorunningtheminuserspace,makingitanidealchoice
inaccurate.Asmentionedearlier,eventsthatcausebottlenecksare
formonitoringandobservability.
sporadicandtransient.Therefore,identifyingabottleneckcompo-
nentrequiresmonitoringtheperformanceofeveryRPCatalltimes
3.1 PerfMon
forallcomponentsandcapturinglogsrelevanttolatencyanom-
alyateachcomponent.Existingfaultlocalizationworks[28,53] PerfMon system overview. PerfMon comprises three compo-
monitorTCPconnectionperformanceandcollectTCPstatistics nents:(1)aDataPlaneAgent(DPA);(2)aControlPlaneAgent
periodicallyatcoarsetimescalestokeepthemonitoringoverhead (CPA);and(3)aCentralController(CC),asshowninFig.3.The
low.Thesestatisticsareinsufficientastheyoftenfailtocapture DPAisdeployedacrosseBPFhookpoints,whichmonitorper-packet
sporadicandtransientanomalyevents(F2). RTT and component-level timestamps and raise alerts for CPA
433

PerfMon:PerformanceMonitoringofHostNetworkStack SoCC’25,November19–21,2025,Online,USA
Data Center  Application  andidentifyfivetypesofper-componenttimestampssufficientto
|     |     | Network | dashboard |          |     |     |     |     |
| --- | --- | ------- | --------- | -------- | --- | --- | --- | --- |
|     |     |         | S1        | monitor. |     |     |     |     |
Cluster node with  SLA  Tounderstandthisbetter,webreakdownthehostcomponents
violation
PerfMon SS12 betweenthetwonodes,N1andN2.Fig.4ashowsthedataexchange
a p p
11 cluster t ra c e betweenN1andN2inaTCP-basedRPC.Thedata(D)packetfrom
|     | Data Plane Agent     |     | SS13 sSS114 |     |     |     |     |     |
| --- | -------------------- | --- | ----------- | --- | --- | --- | --- | --- |
(monitor, detect) theapplicationmicroserviceAtraversestheN1’sCNSandenters
| abnormal  | alert | Application |     |     |     |     |     |     |
| --------- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
delay tracing
Control Plane Agent RNSviathevethinterfaceassociatedwithA’spod.FromtheRNS,
|     | 2   |     | 3   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
alert N1isleftviatheextinterface(thenetworkinterfacethatconnects
alertDB
• S1: SLA violation N1tootherclusternodes).Ittraversestheunderlyingnetwork,
| • S2: Get slow RPC details  |     |     | Central    |                                                      |     |     |     |     |
| --------------------------- | --- | --- | ---------- | ---------------------------------------------------- | --- | --- | --- | --- |
|                             |     |     | Controller | followedbyRNS,CNS,andapplicationmicroserviceBatN2.It |     |     |     |     |
comprises(i)data(D)fromN1toN2;(ii)data+ack(DA)fromN2to
Figure3:PerfMonsystemoverview
N1and;(iii)ack(A)fromN1toN2.Thedata+ack(DA)packetfrom
N2’sCNSfollowsthereversepathwhereasack(A)packettraverses
wheneverlatencyanomaliesaredetected.WhiledesigningDPA,
thepathsameasdata(D).
weaddressthechallengesC1,C2,andC3,asmentionedin§1,and
incorporatetheproposedsolutions.TheCPAsharesthetimeand Weinstrumentthehostnetworkstacktocapturefivetypesof
locationofeachlatencyanomalywiththecentralcontroller.Finally, timestampsthataresufficienttoidentifythebottleneckcomponent:
| thecentralcontrollerrunsqueriesonthedatabaseandpinpoints |     |     |     | •   |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
thebottleneckcomponent(i.e.,CNS,RNS,NIS). RTT:Thetimebetweentheoutgoingdatapacketandcorre-
spondingincomingacknowledgmentobservedatthepod’s
Exampleworkflow.S1:Fromthedashboard,assumethatanoper-
vethinterface.(e.g.,N1-RTTandN2-RTTinFig.4a).
atorobservesauserrequesttakeslongertofinish(SLAviolation).
|     |     |     |     | • RNST | : The time | spent | in RNS by | data packet (e.g., N1- |
| --- | --- | --- | --- | ------ | ---------- | ----- | --------- | ---------------------- |
D
S2:Theoperatorretrievestheapplication-leveltraceforthisuserre- RNST inFig.4a).
D
quest,whichcontainsdetailsofallRPCsinvokedandthetimeeach • :ThetimespentinRNSbydata+ackpackets(e.g.,
|     |     |     |     | RNST | DA  |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
RPCtakes.S3:Next,theoperatoridentifiestheslowRPCs(those
|     |     |     |     | N1-RNST | DA inFig.4a). |     |     |     |
| --- | --- | --- | --- | ------- | ------------- | --- | --- | --- |
tooklongerthanexpected)andrequeststhecentralcontrollerto
|                                                          |     |     |     | • RNST | :ThetimespentbytheackpacketinRNS(e.g.,N1- |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | ------ | ----------------------------------------- | --- | --- | --- |
| findifthereisanyproblematicnetworkstack-levelcomponentin |     |     |     |        | A                                         |     |     |     |
|                                                          |     |     |     | RNST   | inFig.4a).                                |     |     |     |
A
theslowRPCpath.S4:Thecentralcontrollerqueriesthedatabase, • CNST:Thetimeelapsedbetweenanincomingdatapacket
analyzesalertsfromthecomponentsintheRPCpath,andidentifies
andcorrespondingoutgoingacknowledgementobservedat
theentityandassociatedcomponentspotentiallyaffectingtheRPC thevethinterface(e.g.,N1-CNSTandN2-CNSTinFig.4a).
completiontime.
Causeaffectanalysis.AsshowninFig.4b,anabnormaldelayat
Rootcausediagnosis.Findingthebottleneck’scauseisnotinthe
scopeofthispaper.However,wehighlighthowidentifyingthebot- anyoftheabovemonitoredtimesaffectstheRTTobservedatN1
tleneckcomponent(theoutcomeofthispaper)helpstoautomate andN2.Forexample,highN1-RTTcouldbeduetoanincreasein
andfindtherootcause.Oncethebottleneckcomponentisidentified, oneormoreN1-RNST ,N2-RNST ,N2-CNST,N2-RNST ,N1-
|     |     |     |     |     |     | D   | D   | DA  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
wecaninstructthehost(i.e.,entity)toenabletracecollectiononly RNST .Thecausalitygraphdepictingthecause-and-effectrela-
DA
tionshipbetweentheabove-mentionedmonitoredtimesandthe
attheproblematiccomponent(insteadofallcomponentsatthe
senderandreceiver)usingeithereBPFkprobes[17]orCPUhard- RTTobservedatN1andN2isalsoshowninFig.4b.Sincetheper-
wareprofilerslikeintel_pt[25]orothertracingtools[12,22].The componentdelayinformationcollectedatonenodeisnotlocally
collectedtraceshaveprocessIDs,calltraces,andper-calllatency visibletotheothernode,theinformationmustbeeithershared
distributions,whichcanbecorrelatedtofindthecause[9,15]. betweenthenodesorreportedtoacentralentity.Weadoptthe
latterapproach,usingacentralcontroller(CC)becauseofitsease
4 DataPlaneAgent(DPA) ofmanagingandabstractingtheunderlyingprimitives.TheCC
takescareofidentifyingthebottleneckentityandthecomponent
| PerfMon’s DPA | is designed | to perform the following | tasks: (1) |     |     |     |     |     |
| ------------- | ----------- | ------------------------ | ---------- | --- | --- | --- | --- | --- |
(detailsin§6)
monitorstheperformanceofTCPconnections(associatedwith
TodifferentiatebetweenthetimespentinRNSbyanoutgoing
eachRPC)acrosshost-levelnetworkcomponents(§4.1),(2)detects
datapacket(D)andanincomingdatapacket(DA),weseparate
abnormaldelaysandreportstheoccurrenceofabnormaldelaysto
|     |     |     |     | theRNSTintoRNST1(sumofRNST |     |     | D andRNST | DA )andRNST2 |
| --- | --- | --- | --- | -------------------------- | --- | --- | --------- | ------------ |
acontrolplaneagent(§4.2).
|     |     |     |     | (sumofRNST | DA andRNST | A ).Tosummarise,PerfMoncollectsand |     |     |
| --- | --- | --- | --- | ---------- | ---------- | ---------------------------------- | --- | --- |
monitorsRTT,RNST1,RNST2,andCNSToneachend-hostnode.
4.1 Performancemonitoring
Inthiswork,wedonotmonitorthetimespentinNISexplicitly;
RTTmonitoringgivesagoodestimateofend-to-enddelay[32]. instead, we treat NIS as part of the underlying network. Using
However,thisisinsufficienttofindthebottleneckcomponentin
|     |     |     |     | smartNICs | for capturing | NIC timestamps | is  | a promising future |
| --- | --- | --- | --- | --------- | ------------- | -------------- | --- | ------------------ |
thehoststack,causinghighRTTdelays.Thebottleneckcomponent
researchdirection.
couldbeoneormorehost-levelcomponentssuchasCNS,RNS,and
NIS.Therefore,per-componentmonitoringandnecessaryinstru-
4.2 Capturinglatencyanomalies
mentationareessentialforaccuratelyidentifyingthebottleneck
component(C1in§1).Todoso,wetrackthesetofcomponents Latencyanomalydetection.Continuouslycollectingandmain-
thatapackettraversesinatypicalLinux-basedhostnetworkstack taining all per-packet timestamps at each component helps to
434

SoCC’25,November19–21,20R2a5n,jOithnalinKe,,AUnSkAitSharma,MalsawmsangaSailo,ArunSiddardha,AmritKumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik
| N1 CNS     |     |     |     | N2 CNS          |     |     |     |
| ---------- | --- | --- | --- | --------------- | --- | --- | --- |
| transport  |     |     |     | transport  App  |     |     |     |
App
| layer | N1 veth | N1 ext | N2 ext N2 veth | layer serviceB |     |     |     |
| ----- | ------- | ------ | -------------- | -------------- | --- | --- | --- |
serviceA
|     | t1  |     | data |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
t2
|     |     |     | t3 t4 |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- |
N1-RNST
|     |     | D   | N2-RNST |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
D N2-CNST data
N1-RTT
data+ack
|     | N1-RNST | DA data+ack | t5  |     |     |     |     |
| --- | ------- | ----------- | --- | --- | --- | --- | --- |
t6
|          |     | t7  | N2-RNST |     |     |     |     |
| -------- | --- | --- | ------- | --- | --- | --- | --- |
| data+ack |     |     | DA      |     |     |     |     |
| data     | t8  |     |         |     |     |     |     |
ack N1-CNST
N2-RTT
t9
|     |     |     | N2-RNST A |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- |
t10 ack
t11
N1-RNST
|     |     | A   | t12 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
nw_latency
| N1-RNST  = t2 - t1; N2-RNST |     |  = t4 - t3; N2-RNST |  = t6 - t5; N1-RNST |  = t8 - t7; |     |     |     |
| --------------------------- | --- | ------------------- | ------------------- | ----------- | --- | --- | --- |
| D                           |     | D                   | DA                  | DA          |     |     |     |
 N1-RNST = t10 - t9; N2-RNST = t12 - t11; N1-CNST = t9 - t8; N2-CNST = t5 – t4
| A                |                         | A   |                                             |                         |       |     |     |
| ---------------- | ----------------------- | --- | ------------------------------------------- | ----------------------- | ----- | --- | --- |
| N1-RTT = N1-RNST |  + nw_latency + N2-RNST |     |  + N2-CNST + N2-RNST                        |  + nw_latency + N1-RNST |       |     |     |
|                  | D                       |     | D                                           | DA                      | DA    |     |     |
| N2-RTT = N2-RNST |  + nw_latency + N1-RNST |     |  + N1-CNST + N1-RNST + nw_latency + N2-RNST |                         |       |     |     |
|                  | DA                      |     | DA                                          | A                       | A     |     |     |
(a)RPCperformancemonitoring
(b)Causeandaffect
Figure4:AbnormaldelaysatdifferentcomponentsinflateRTTobservedatdifferententities
intwosteps.First,wederiveabaselineprocessingtime(𝐵)foreach
achievegoodaccuracybuthashugecomputationandstorageover-
heads(C2in§1).Tokeeptheoverheadslow,wedesignPerfMon’s componentbyprofilingtheapplicationundervariousworkloads.
DPAtomonitorper-componentpacketprocessingtimeandde- Next,wederivethethreshold(T)higherthanthebaselinebyΔ.
tectlatencyanomalies.Thiswillsignificantlyreducethecollection Thedesignchoicesandtheirimportanceareasfollows.
andstorageoverheadswithoutcompromisingdetectionaccuracy.
(1)Derivingbaseline.Foracloud-nativeapplicationmanagedby
Specifically,wedesigntheDPAtomonitoranddetectdeviationsin aKubernetes-likecluster,derivingabaselinefortheexpectedpro-
per-componentprocessingtimes.Upondetectingananomaly,the cessingtimeofeachhostnetworkstackcomponentischallenging.
DPAcapturesthecomponentdetailsandthetimeofoccurrenceof Thisisbecausetheapplicationcomprisesmultipleservices,where
thebottleneckeventsothattheSLAviolationsobservedattheRPC eachservicehasmultipleinstancesdeployedacrossnodesinthe
levelcanbereasonedbycorrelatingwiththeproblematichost-level
cluster.SomeRPCsaremadeacrossnodes(inter-node),andsome
component.
withinthesamenode(intra-node).Toaddressthis,weproposea
Torealizeourlight-weightapproach,wedesignourdetection topology-basedcategorizationapproach.WeclassifytheRPCsinto
algorithmwiththefollowingtwokeyfeatures.First,wemaintain twocategories:inter-nodeandintra-node,andderiveseparatebase-
thetimespentvaluesattheconnectionlevel(i.e.,flowlevel)instead lines(andcorrespondingthresholds)foreachcomponentwithin
ofatthepacketlevelsothatallpacketsofaconnectionsharethe
thesecategories.Thisapproachisbasedontheobservationthat
state.Also,weobservedthatmultipleRPCsfromoneserviceto
thelayer-4RTTisprimarilyinfluencedbydelaysinthenetwork
anothersharethesameconnectionthatstaysforlongerdurations. pathcomprisingboththehostnetworkstackandtheunderlying
Thismeansthestateperserviceinstance(sayA)isproportional network,andisrelativelyunaffectedbyapplication-layerprocess-
tothenumberofinstancesoftheotherservice(sayB)itistalking ingtime.Tobeconcrete,inspiredbyarecentwork[47],weprofile
to.Foreachconnection,wemaintainf-RTT,f-RNST1,f-CNST,and
theapplicationat40%workload(representingtypicalworkload
f-RNST2asamovingaverageoftimespentbyindividualpackets,
|     |     |     |     | condition) | and find the P99 values | for RTT, RNST1, | CNST, and |
| --- | --- | --- | --- | ---------- | ----------------------- | --------------- | --------- |
i.e.,RTT,RNST1,CNST,andRNST2,respectively.
RNST2forallRPCs.Then,wecategorizetheRPCsintotwobuck-
Second,tokeepthedetectionalgorithm’scomputationlight- ets(inter-nodeandintra-node),andtheaverageofeachbucketis
weightandamenabletoimplementationataneBPFhookpoint,we consideredthebaselinevalue.
doathreshold-basedcheckonper-componentprocessingtimes. (2)Derivingthreshold(T).Ingeneral,athresholdT
isderived
Themainchallengeisconcernedwithderivingtherightthreshold;
|     |     |     |     | fromthebaselineB[29]followingtheequation,𝑇 |     | =𝐵+Δ,whereΔ |     |
| --- | --- | --- | --- | ------------------------------------------ | --- | ----------- | --- |
athresholdvaluethatistoolowcanleadtotoomanyfalsealerts ischosenbasedontherequirementsspecifictoanomalydetection.
andassociatedoverheads,whereasathresholdvaluethatistoohigh SinceourgoalistodetectRPClatencyanomaliesintheorderoftens
mayfailtocapturelatencyanomalies(falsenegatives).Anideal
ofmilliseconds(50ms-100ms)thatpotentiallycauseSLAviolations,
thresholdshouldstrikeabalance.Wecarefullyderivethethreshold
weadoptapercentile-basedthresholdingapproach[47].Specifically,
435

PerfMon:PerformanceMonitoringofHostNetworkStack SoCC’25,November19–21,2025,Online,USA
Algorithm1DPApseudocodeformonitoringanddetectingab-
normalpacket-processingdelayevents
1: Input:
2: f,RTT,RNST1,CNST,RNST2
3: f=(srcIP,srcPort,dstIP,dstPort)
4: 𝛼 -smootheningfactor,variesfrom(0,1)
5: Output:
6: alertforthemonitoreddata
7: alert RTT =(f,1,RTT,seqNo,ackNo)
8: alert RNST1 =(f,2,RNST1,seqNo,ackNo)
Figure5:f-RTT,f-RNST1,f-CNSTandf-RNST2aremonitored
9: alert CNST =(f,3,CNST,seqNo,ackNo)
atthreedifferenthookpoints
10: alert RNST2 =(f,4,RNST2,seqNo,ackNo)
wedefineΔasamultipleofthebaselinevaluecalculatedasthe
averageofP99valuesinthepreviousstep.Webelievethatthis 11: begin:
strategyiswell-suitedforidentifyingtheclassoflatencyanomalies 12: (1)Atvethegress:
wetarget(intheorderof50-100ms).Toderivethethresholdforeach 13: foreachdata+ackpacketforflowf do
componenttimestamp(RTT,RNST1,CNST,andRNST2),onenaive 14: f-RTT=𝛼 ∗f-RTT+(1−𝛼)∗RTT
approachistoscaleallthebaselinevaluesbyaconstantfactorX.
15:
f-RNST1=𝛼 ∗f-RNST1+(1−𝛼)∗RNST1
However,sinceCNSTandRNSTvaluesarerelativelymuchsmaller 16: iff-RTT>T RTT then
thantheRTT,thisapproachcanleadtogeneratingmanyfalsealerts 17: send_event(alert RTT )
forCNSTandRNSTwithoutanyRTTalerts,leadingtotoomany 18: endif
false positives. As an alternative, we adopt to scale component 19: iff-RNST1>T RNST then
thresholdsproportionallybasedontheircontributiontoRTT(Eq. 20: send_event(alert RNST1 )
(1)).ThisensuresCNSTandRNSTanomaliesareflaggedonlywhen 21: endif
theircontributiontotheoverallRTTissignificant,thatis,when 22: endfor
theyarelikelytoaffecttheRPClatency,thuskeepingthefalse
positiveratelow.Inourprototype,weempiricallyselectthescaling 23: (2)Atvethingress:
factorX thatminimizesthenumberofalerts(seeFig.12b)at40% 24: foreachackpacketforflowf do
applicationload[30].However,operatorscanalsotuneX based 25: f-CNST=𝛼 ∗f-CNST+(1−𝛼)∗CNST
ontheapplication’slatencytolerance,suchasacceptabledelay 26: iff-CNST>T CNST then
magnitudeandduration. 27: send_event(alert CNST )
𝑇 RTT =𝑋 ∗𝑅𝑇𝑇 28: endif
𝑘 =⌊𝑅𝑇𝑇/𝑅𝑁𝑆𝑇1⌋ 𝑎𝑛𝑑 𝑇 =𝑋 ∗𝑘∗𝑅𝑁𝑆𝑇1 29: endfor
RNST1
(1)
𝑙 =⌊𝑅𝑇𝑇/𝐶𝑁𝑆𝑇⌋ 𝑎𝑛𝑑 𝑇 =𝑋 ∗𝑙∗𝐶𝑁𝑆𝑇
CNST 30: (3)Atextegress:
𝑚=⌊𝑅𝑇𝑇/𝑅𝑁𝑆𝑇2⌋ 𝑎𝑛𝑑 𝑇
RNST2
=𝑋 ∗𝑚∗𝑅𝑁𝑆𝑇2
31: foreachackpacketforflowf do
32:
f-RNST2=𝛼 ∗f-RNST2+(1−𝛼)∗RNST2
Handlingchangeinthreshold.ThepresetthresholdusedinPerf-
Mondependsontheunderlyinghardware,operatingsystem,and 33: iff-RNST2>T RNST then
theaverageworkload;thus,itcanchangeifanyofthesefactorsvary. 34: send_event(alert RNST2 )
35: endif
Forinstance,ifthebaselineaverageapplicationworkloadchanges
36: endfor
oriftheoperatorupgradestheunderlyinghardware/OS/software,
37: end
leadingtoachangeinearlieragreedSLAonrequestlatency,then
PerfMonrequiresreprofilingandupdatingthethreshold.Theoper-
atorcanplantoreprofileeitherduringtheplannedmaintenance
windoworduringnon-peakhours,minimisingtheimpactonap- Detectionalgorithm.Algorithm1showsthepseudo-codeofPerf-
plicationperformance.Further,DPAcanbeconfiguredtousethe Mon’sdetectionoflatencyanomaliesatnodeN1.Uponexceeding
newlyupdatedthreshold. thepre-definedthreshold(asdiscussedin§4.2),analertcomprising
fivefields:4-tupleflow-id(f),alertType(1to4),abnormalpacket
4.3 DetectionalgorithmandImplementation processing time (one of RTT, RNST1, RNST2, CNST), sequence
number(seqNo),andacknowledgmentnumber(ackNo),issentto
eBPFhookpoints.PerfMonattacheseBPFprogramsformoni-
theCPA.
toringandanomalydetectionattwohookpointsinthehost:1)
microservice’svirtualethernet(veth)interfaceingressandegress,
5 Controlplaneagent(CPA)
and2)ext’singressandegress,whereextistheinterfacethatcon-
nectsthehosttootherclusternodes.AsshowninFig.5,f-RTTand Aburstofpacketscanarriveatacomponentduringthebottleneck
f-RNST1aremonitoredatvethegress,f-CNSTatvethingress,and period,whereper-componentprocessingtimeforthesepackets
f-RNST2atextegress. exceedstherespectivethreshold.Itiscrucialtonottooverwhelm
436

SoCC’25,November19–21,20R2a5n,jOithnalinKe,,AUnSkAitSharma,MalsawmsangaSailo,ArunSiddardha,AmritKumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik
client request client response identifiedasthecandidatebottleneckcomponent.Morespecifically,
|       |     |     | s p a n       |     |         | considerC   | ,C ,...,C                                    |                                        |     |     |     |
| ----- | --- | --- | ------------- | --- | ------- | ----------- | -------------------------------------------- | -------------------------------------- | --- | --- | --- |
|       |     |     | RT T   sp ike |     |         |             | 1 2                                          | nasthecandidatebottleneckcomponentsand |     |     |     |
| t1    |     |     |               |     | t2      | t ,t ,...,t |                                              |                                        |     |     |     |
|       |     |     |               |     |         | 1 2         | n asthetimespentattherespectivecomponents.We |                                        |     |     |     |
| r s v | e   |     | front-end     |     | e v r s |             |                                              |                                        |     |     |     |
representRTTasthesumoftimespentateachcomponent(Eq.2).
N1
|     |     |            | recommend |       |       |                                  |     |     | ∑︁  |                       |     |
| --- | --- | ---------- | --------- | ----- | ----- | -------------------------------- | --- | --- | --- | --------------------- | --- |
|     |     |            |           |       |       |                                  |     | 𝑅𝑇𝑇 | =   | 𝑡                     | (2) |
|     | N2e | v          | r         | s v e |       |                                  |     |     |     | i                     |     |
|     |     | CNST spike | span      |       | 1S S2 | WethendeterminetheRTTdeviation(𝐷 |     |     |     |                       |     |
|     |     |            |           | S3    |       |                                  |     |     |     | RTT )andper-component |     |
f entity RTT seqNo ackNo tstamp S4 deviation(𝐷)asthedeviationoftheobservedvaluefromthethresh-
|       |      |       |       | S1: User request with SLA violations |     |                    | i   |     |     |     |     |
| ----- | ---- | ----- | ----- | ------------------------------------ | --- | ------------------ | --- | --- | --- | --- | --- |
| f1 N1 | 20ms | S1 S2 | t1+δ1 |                                      |     | oldvalue(T)(Eq.3). |     |     |     |     |     |
|       |      |       |       | S2: List of request’s slow RPCs      |     |                    | i   |     |     |     |     |
S3: Get problematic component in slow
|          |      |             |        | RPC’s path (f, startTime t1, endTime t2) |     |     |     | 𝐷   | =𝑅𝑇𝑇 −𝑇 |     |     |
| -------- | ---- | ----------- | ------ | ---------------------------------------- | --- | --- | --- | --- | ------- | --- | --- |
| f entity | CNST | seqNo ackNo | tstamp |                                          |     |     |     | RTT |         | RTT |     |
|          |      |             |        | S4: Result(entity:N2, component: CNS)    |     |     |     |     |         |     | (3) |
f1’ N2 18ms S1 S2 t1+δ f = (srcIP, srcPort, dstIP, dstPort) 𝐷 =𝑡 −𝑇
|     |     |     |     |         |                  |     |     | i   | i i |     |     |
| --- | --- | --- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | e ext r | receive CNS time |     |     |     |     |     |     |
Per-componentrelativeimportance,𝑋
|     |     | alertDB |     | v veth s | send RNS time |                         |     |     |         | i iscomputedbasedon |     |
| --- | --- | ------- | --- | -------- | ------------- | ----------------------- | --- | --- | ------- | ------------------- | --- |
|     |     |         |     |          |               | thecontributiontowardsD |     | RTT | (Eq.4). |                     |     |
Figure6:Identifyingproblematiccomponent
|     |     |     |     |     |     |     |     | 𝑋   | =𝐷 /𝐷 |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
theCPAwithtoomanyalerts.Atthesametime,thealertsduetoa i i RTT
bottleneckeventshouldbedifferentiatedfromrandomalertsdue
ThecomponentthatcontributesthemaximumtowardsRTTde-
tonoise(C3mentionedin§1).Weaddressthisbyintroducinga
viationisidentifiedasthecandidatebottleneckcomponent(Eq.5).
temporarybufferattheCPA,whichbuffersalertsfromtheDPAfor
ashorttime.Morespecifically,theCPAstartsatimeronreceiving if𝑋 =max(𝑋 ,𝑋 ,...,𝑋 )then,
|     |     |     |     |     |     |     |     | i   | 1 2 | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
an alert, if the timer is not running. If the number of alerts in (5)
|                                                       |     |     |     |     |             |     | 𝑏𝑜𝑡𝑡𝑙𝑒𝑛𝑒𝑐𝑘_𝑐𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡 |     |     | =𝐶  |     |
| ----------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | -------------------- | --- | --- | --- | --- |
| awindowexceedsapre-definedthreshold,sayT,thealertsare |     |     |     |     |             |     |                      |     |     | i   |     |
| senttothecontroller;otherwise,theyareignored.T        |     |     |     |     | isinversely |     |                      |     |     |     |     |
Example.ConsiderN1-RTTviolationcausedbyabottleneckin
| proportional | to  | the smoothing | factor𝛼 | used in | per-connection |     |     |     |     |     |     |
| ------------ | --- | ------------- | ------- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
N2-CNSTandN1-RNST1,resultinginanincreaseinend-userre-
processingtime(i.e.,RTT,RNST1,CNSTandRNST2)computation
questdelay.CCidentifiesN2-CNSTandN1-RNST1asthecandidate
intheDPA(seeAlgorithm1).Thatis,forhigher𝛼values(e.g.,0.6≤
bottleneckcomponents.
𝛼
≤1),astheaveragesmoothsoutwithoutimmediatelyreflecting
onRTT/RNST1/CNST/RNST2violations,therearefewerrandom
𝐶 ={𝑁2-𝐶𝑁𝑆𝑇,𝑁1-𝑅𝑁𝑆𝑇1}
alerts.Ontheotherhand,forlower𝛼values(e.g.,0≤𝛼≤0.4),more
|     |     |     |     |     |     |     | 𝑅𝑇𝑇 | =𝑡  | +𝑡  |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
randomalertsaresenttotheCPA.Fig.7depictsthisrelationship N2-CNST N1-RNST1
| between𝛼,T,andthealertsgenerated.Basedonthe𝛼 |     |     |     |     | value,T |                      |     |     |                              |     |     |
| -------------------------------------------- | --- | --- | --- | --- | ------- | -------------------- | --- | --- | ---------------------------- | --- | --- |
|                                              |     |     |     |     |         | WithanRTTdeviation(D |     |     | )of50msandper-componentdevi- |     |     |
RTT
isconfiguredsuchthattheclassificationofrandomandrelevant ationof35ms(D )and15ms(D ),CCcomputesthe
|     |     |     |     |     |     |     | N2-CNST |     |     | N1-RNST1 |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | -------- | --- |
alertsisaccurate.WesetT to10assuggestedin[27]. relativeimportanceandcandidateselectionasbelow.
6 Centralcontroller(CC)
𝑋 =35/50=0.7
N2-CNST
ThissectionexplainshowtheCCidentifiesthebottleneckcompo- 𝑋 =15/50=0.3
N1-RNST1
| nentcausingincreasedRPCcompletiontime(i.e.,slowRPC). |     |     |     |     |     |     |     |     |     |     | (7) |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑋 =𝑚𝑎𝑥(0.7,0.3)=0.7
TheCCreceivesalertsfromCPAagentsrunningoneachcluster
|     |     |     |     |     |     |     | 𝑏𝑜𝑡𝑡𝑙𝑒𝑛𝑒𝑐𝑘_𝑐𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡 |     |     | =𝑁2−𝐶𝑁𝑆𝑇 |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------- | --- |
nodeandaddsthealertstothealertDBthatarelaterqueriedfor
bottleneckidentification.AsshowninFig.6,onobservinghighde-
7 Identifyingbottleneckcomponentusing
laysforend-userrequests(S1),theoperatorretrievestheassociated
| applicationtrace(likeJaeger)andthedetailsofslowRPC(S2).The |     |     |     |     |     | PerfMon |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
operatorthenqueriesthealertDBandretrievesalertsoverlapping
ThissectionexplainshowPerfMon’sbottleneckcomponentidenti-
withtheslowRPCperiod(S3).CCthenexecutesitsbottleneck ficationhelpstodiagnosetherootcauseofRPClatencyanomalies
identificationalgorithm(discussedbelow)ontheretrievedalertsto observedforanapplicationdeployedinaKubernetescluster.We
identifythebottleneckcomponentresponsibleforslowRPC(S4). deployhotelReservationapplicationfromDeathStarBench,anopen
Bottleneckidentification.TolocalizethesourceofanRPCla- sourcebenchmarksuite[14,36],onaKubernetesclusterwiththree
tency,CCretrievesthepotentialbottleneckcomponents(bottle- bare-metalservers(master,worker1,andworker2).Wesenduserre-
neckcandidates)andtimestampsfromthealertDB.CCidentifies queststohotelrecommendationsusingaworkloadgeneratorfrom
thebottleneckcomponentfromthebottleneckcandidatesusinga thebenchmarksuite[14].Eachuserrequestpassesthroughthree
candidateselectionalgorithmbasedontherelativeimportanceof services:frontend,recommendation,andprofile.Usingstress-ng[23]
tool,weinjectafaultthatthrottlesCPUforrecommendationcon-
eachcomponent[41]inaffectingtheRTT.Per-componentrelative
importanceiscomputedbasedoneachcomponent’scontribution tainerforevery30seconds.Whenauserrequestoverlapswiththe
CPUthrottlingperiod,thecompletiontimeofGetRecommendation
towardsRTTdeviation(fromthethreshold).Thecomponentwith
themaximumcontributionisgiventhehighestimportanceand RPCfromthefrontendshootsupto≈100ms,asshowninFig.8.
437

PerfMon:PerformanceMonitoringofHostNetworkStack SoCC’25,November19–21,2025,Online,USA
80
60
40
20
0
0 20 40 60 80 100 120
Figure7:Alertsratefordifferent𝛼and Time
T values
)sm(noitaruD
napS
GetRecommendation
With Issue 0.40
Without Issue
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0 20 40 60 80 100 120
Time
Figure 8: GetRecommendation span
showslatencyanomalies
)sm(noitaruD
napS
recommend
With Issue
Without Issue
Figure9:Recommendspandoesnotcap-
tureabnormaldelaysbyCNScomponent
Thespanofrecommendmicroservice,asshowninFig.9,doesnot
detectanydeviation,whichindicatesthedelaysarenotfromthe
applicationlevel.Next,wequeryPerfMon’scentralcontroller(§6)
tofindpossiblebottlenecksinthehoststackduringtheslowRPC
period.ItrespondswithCNSasthebottleneckcomponentand
workernode2astheentity.ThiswayPerfMonhelpstoquicklynar-
rowdownandlookatthepotentialissuesataspecificcomponent
whichsavesalotoftime.Tofindthecauseforthebottleneck,the
operatorcancheckforthepossibilityofsocketbufferbuild-upby (a)Alertsgenerated (b)Averagealertrate
monitoringthesocket’ssendandreceivequeueusinglsof-Tq[6]) Figure10:ThresholdscalingfactorX=3hastheleastalert
commandfromthepod’snamespace.Themostpopularrootcauses rate.
forsocketbufferbuild-upareasuddenincreaseinrequests(incast)
centraldatabaseisMongoDB(version7.0.2),containingfourtables.
orCPUcontentioninthepod(Table1).Finally,thecausecanbe
Each table stores the RTT, RNST1, CNST, and RNST2 violation
determinedbycollectingandanalyzinglow-levellogs,suchasthe
reportsreceivedfromthecontrolplaneagent.TocomparePerf-
pod’sinterfacestatisticsfortheincastcaseandperfrecord[8]for
MonwithTCP-stats-basedperiodicmonitoring,wealsoimplement
theCPUcontentioncase.
TCP-stats-basedperiodicmonitoringinpython3.7comprising150
LOC.Theprogramperiodicallymonitorstheper-flowRTTfrom
8 Evaluation
eachservicepodusingLinuxss[3]command.
WeevaluatePerfMonagainstthefollowingquestions:
• Performanceoverhead:WhatistheimpactofPerfMonon 8.1 Impactonapplicationperformance
application’srequestcompletiontime(RCT)andrequests Objective. TounderstandthePerfMon’simpactonapplication
completedpersecond(RCS)? performanceanditscomputeandmemoryoverheads.
• Scalability:WhatistheimpactofPerfMonalways-onmoni-
Experimentsetup.WeevaluatePerfMoninaKubernetescluster
toringonthroughputathighpacketrate?
withthreebaremetalservers,oneasamasterandtheothertwoas
• Effectiveness:DoesPerfMondetectabnormaltransientspo-
workers.Theserversareconnectedtoatop-of-rackswitchviaa
radicdelayeventsandcapturealertsrelevantforidentifying 1Gbpslink.EachserverhasAMDEPYC72628-core3.20GHzCPU
theproblematiccomponent? and64GBRAM.WedeployedthehotelReservationapplicationfrom
Implementation. PerfMon comprises three modules: (1) Data DeathStarBenchopensourcebenchmarksuite[14,36].Flannel[4]
planemodule,(2)Controlplanemodule,and(3)Controllermodule. isusedastheCNI.PerfMon’sDPAandCPAaredeployedonthe
ThedataplanemodulecomprisesfoureBPFprogramsattachedto workernodes,andPerfMon’scontrolleranddatabasearedeployed
oneoftheTChookpoints(showninFig.5)thattrackthetimes- onthemasternode.Workloadsaregeneratedusingwrk2[24],an
tamps as discussed in Fig.4a. We enable receive flow steering HTTPbenchmarkingtool.
(RFS)[20]tosteerpacketstotheCPUonwhichthereceivingap-
plicationisrunninganduseper-CPULRU(leastrecentlyused) Derivingthreshold.Tofindthethresholdvalueforoursetup,
hashmapstostorethemonitoredtimestamps.Weimplementthe weprofilethehotelReservationapplication.Wecollectper-packet
eBPF program on Linux kernel version 5.15.0-86-generic using RTTforeachRPCflowandderivetheinter-nodeandintra-node
≈1200LOC.ThecontrolplanemoduleisimplementedintheC baselineastheaverageP99valuesofalltheinter-nodeandintra-
language(GLIBC2.35)using≈850LOC.Thecentralcontrolleris nodeRPCflows.Asdiscussedin§4.2,weusethecontribution-based
implementedinPython3.10.WeimplementaUDPserveratthe scalingapproachat40%applicationload(assuggestedin[30])and
controllertoreceiveflowreportsfromthecontrolplaneagent.The findthescalingfactorX thathasalertrate≤1.Fig.10showsthe
438

SoCC’25,November19–21,20R2a5n,jOithnalinKe,,AUnSkAitSharma,MalsawmsangaSailo,ArunSiddardha,AmritKumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik
(a)RCTandRCSat40%load (b)RCTandRCSat60%load (c)RCTandRCSat70%load
Figure11:Average,P99,andP999applicationRCTandaverageRCSfordifferentloads.
(a)CPUandmemoryutilization (b)AlertratefromDPA
Figure13:ImpactofPerfMonalways-onmonitoringonappli-
Figure12:Forvaryingapplicationload,(a)utilizationand(b) cationthroughputwithincreasingconcurrentconnections
alertrate
FromFig.12a,weobservethataverageCPUutilizationincreases
astheloadincreasesforallthesystems.Itisworthnotingthat
alertsgeneratedbyDPAandthealertratefordifferentX values.
theCPUutilizationremainsalmostthesameforBandPacross
Basedontheresults,wesetX to3asithasthelowestalertrate
differentloads.However,TCP-stats-basedmonitoringincreases
andderivethethresholdasdescribedin§4.2.
theCPUutilizationby32%for40%load.Ontheotherhand,Band
P have similar average memory utilization across workloads; P
Performancemetricsandexperiment.Westudytheimpact
increasethememoryutilizationbyameagre1%accountingtothe
ofPerfMononapplicationperformanceintermsof:(1)thenumber
eBPFmapsforstoringmonitoredcomponenttimestamps.Whereas
ofapplicationrequestscompletedpersecond(RCS),(2)request
J,P+J,andTrequiresmorememory.JandP+Jincreasesmemory
completiontime(RCT),(3)memoryutilization,and(4)CPUutiliza-
utilizationby≈4%duetoJaeger’smemoryoverheadsfortrace
tion.Wevaryapplicationworkload(40%,60%,and70%)andconduct
collectionandTincreasesthememoryutilizationby26%.
experimentsforfivedifferentsystems:(1)Benchmarkapplication
withoutanymonitoring(B);(2)BenchmarkwithPerfMon(P);(3)
8.2 Scalability
Benchmarkwithonlyapplication-leveltracingusingJaeger(J);(4)
BenchmarkwithPerfMonandJaeger(P+J).and(5)Benchmarkwith Objective.TostudytheimpactofPerfMonDPA(always-onper-
TCP-stats-basedmonitoring(T). packetmonitoring)athighpacketrates(40Gbps)andwithmany
concurrentflows.
Results.Fig.11showstheRCTandRCSofallfivesystemsatdif-
ferentworkloads.Comparedtothebenchmark(B),weobservethat Experimental setup. The experimental setup comprises a Ku-
PerfMon(P)overheadisminimalasitslightlyincreasestheP999 bernetesclusterwithtwonodes.Eachnodeisabaremetalserver
latencyby0.9%for40%load.Thisincreaseinlatencyisattributed equippedwithtwoIntel(R)Xeon(R)Silver431620-core2.30GHz
toPerfMon’smonitoringandprocessingoverheads.However,as CPUwith256GBRAManda40GbpsNetronomeAgiloSmart-
weincreasetheworkload,P999latencyincreasesby15%,and25% NIC [10]. These nodes are directly connected using QSFP40Gb
for60%,and70%workloads,respectively.Theincreaseishigher
Ethernetcoppercable.Weusentttcp[7]togeneratemanyconcur-
at60%and70%loadbecauseastheloadincreases,morealertsare
rentflows(1millionconcurrentflows).Wedeployedntttcpclient
generatedbyPerfMon’sDPA,whichisevidentfromFig.12b.At
onthemasternodetogenerateflows.ntttcpserverwithPerfMon
highload,packetsarequeuedattheapplicationsocketbuffers,ex- monitoringdeployedontheworkernodeactsastheDUT(device
ceedingCNSTandRTTthresholds,followedbyalerts.Ontheother undertest).
hand,TincreasesbothP99andP999latencywhichisreflectedalso Performancemetricsandexperiment. Westudytheimpact
asadropinRCS.WhencomparedwithB,TincreasesP999latency ofPerfMon’salways-onper-packetmonitoringusingapplication
46%,400%,and440%respectively,for40,60,and70%workload. throughputastheperformancemetric.Weperformtheexperiment
439

PerfMon:PerformanceMonitoringofHostNetworkStack SoCC’25,November19–21,2025,Online,USA
byvaryingthenumberofconcurrentconnectionsusingntttcp.Our Fault DPA CPA Avg.alertrate
experimentcomprises5iterations.Eachiterationconsistsof5runs,
FPR FNR FPR FNR
eachlasting120seconds.
CNS 0.071 0 0.014 0 1.36
Results.Fig.13showstheapplicationthroughputachievedwith-
outanymonitoring(benchmarkB),withPerfMonmonitoring(P), RNS 0.056 0 0.015 0 6.87
andwithalways-onTCP-statsmonitoring(T).ThesecondaryY- Table2:CPAreducesFPRby80%forCNSfaultsandby73%
axisshowsthedropinthroughputcomparedwiththebaseline forRNSfaults.
case.WecanobservethatPerfMoncausesminimalimpactonappli-
cationthroughputwithincreasingconcurrentconnections.With
onemillionconcurrentconnections,PerfMonmonitoringreduces
theapplicationthroughputby≈3%.Thisdropisnegligibleforan
always-onper-packetmonitoring.Ontheotherhand,Treducesthe
throughputby≈13%adverslyaffectingapplicationperformance.
8.3 Effectiveness
Objective.TostudyPerfMon’seffectivenessindetectingtransient (a)CNSfault (b)RNSfault
andsporadiceventscausingbottlenecksinthehost. Figure14:PerfMon’sDPAdetectsbottleneckcomponentand
Setupandmetrics.Theexperimentsetupisthesameastheone generatesalerts
describedpreviouslyin8.1.WeevaluatePerfMon’seffectivenessin
termsofitsabilityto(1)detectbottleneckcomponents,(2)minimize
random alerts, and (3) detect transient and sporadic bottleneck
events. We use tc-netem [1] to inject processing delays in CNS
(podinterfaceeth0)andRNS(Linuxbridgecni0).WeconsiderFPR
(falsepositiverate),FNR(falsenegativerate),andaccuracyasthe
metrics.Fromtheliteratureandblogs[9,15,39],weunderstand
thattransientandsporadicbottleneckeventscancauseprocessing
delaysvaryingfrom10msto100msandcanlastfor30msto50ms. (a)Accuracy (b)FPRandFNR
Hence,weinject10msprocessingdelays(fault)randomlyatCNS Figure15:PerfMon’sdetectionaccuracyishighforbottle-
and RNS, each lasting for 40 ms in our experiment run for 120 neckeventslasting8msormore.
seconds.
affectedbythefault;itishigherforRNSfaultbecauseRNSfault
8.3.1 Detectingbottleneckcomponent. Fig.14showstheDPAand affectsmultipleRPCs.
CPAalertsgeneratedbyPerfMonwithsyntheticfaultinjection
8.3.3 Detecttransientandsporadicbottleneckevents. Tounder-
atCNSandRNS.AsshowninFig.14,weinjectprocessingdelays
standPerfMon’sabilitytodetecttransientandsporadicbottleneck
(fault)twiceduringthe120-secondrun,andPerfMondetectsand
events,weinjectprocessingdelays(faults)atCNSrandomly,caus-
capturesboththedelayevents.CNSfaultinthepodinflatesthe
inga10msdelaywhilevaryingthedurationofthefaultfrom1msto
RTTandCNSTofingressRPCrequestpacketsdestinedforthe
32ms.Fig.15showsthedetectionaccuracy,FPR,andFNRobserved
pod.HencethenumberofCNSTandRTTalertsarealmostequal
atCPAandDPA.WeobservethatPerfMon’sdetectionaccuracy
(Fig.14a).However,withtheRNSfaultinthenode,thenumber
increaseswithfaultduration(Fig.15a).Withfaultslasting8msor
ofalertsishigher(Fig.14b)astheRNSfaultaffectsmultipleRPCs.
more,PerfMonhashighaccuracywithFNRclosetozero(Fig.15b).
Also, the number of RTT alerts is almost double that of RNST
Butforshorterfaultdurations(1msand2ms),PerfMon’saccuracy
alertsbecauseRNSfaultinflatestheRTTofbothRPCrequestsand
is low because the fault affects only a few packets, which gets
responses(packetsexchangedinbothdirections).Thatis,theRNS smoothenedwithoutinflatingtheEWMAforlarger𝛼 values(as
faultinflatesRNST1ofRPCresponsepackets(egresspacketsfrom
discussedin§5).Consequently,theDPAeitherfailstogenerateor
thenode)andRNST2ofRPCrequestpackets(ingresspacketsto
generatesfeweralerts,leadingtohigherDPA-FNR.Further,CPA’s
thenode),thusinflatingRTTofbothrequestandresponse.
noisereductionidentifiesthesealertsasnoise,leavingCPA-FNRat
1.Asthefaultdurationincreases,PerfMon’sFNRdecreases.Specif-
8.3.2 Minimizerandomalerts. Table2showstheFPRandFNRof
ically,PerfMonFNRfallstozerofortransientfaultslastingaslow
DPAalerts(alertswithnoise)andCPAalerts(alertsafternoise
as8ms.
reduction). CPA reduces the FPR by 80% and 73% for CNS and
RNSfaults,respectively.ThisshowsthatCPAsuccessfullyignores 8.3.4 ComparisonwithTCP-stats-basedmonitoring. Wecompare
randomalerts(noise)fromrelevantalerts,whichminimizesfalse PerfMon’seffectivenessindetectingtransientandsporadicfaults
positivesandreducesPerfMon’scomputeandstorageoverhead withthatofTCP-stats-basedalways-onmonitoring.Weinjecta
(which will otherwise be spent on false positives). As PerfMon CNSTdelayof10msandsetthefaultdurationto8and16mil-
detectsboththeinjectedfaults,FNRbecomeszeroforCNSand lisecondsandcomparetheeffectivenessusingFNRasthemetric.
RNS. Also, the average alert rate shows the number of packets In the previous experiment, we already observed that PerfMon
440

SoCC’25,November19–21,20R2a5n,jOithnalinKe,,AUnSkAitSharma,MalsawmsangaSailo,ArunSiddardha,AmritKumar,PraveenTammana,PraveinGovindanKannan,andPriyankaNaik
switches,endhosts,andapplicationcontainers.Host-INTcollects
recordsforeverypacketateveryhostandexportsrecordstoacen-
traldatabase.Continuousper-packetrecordcollection,processing,
andstoragehavehugeperformanceandstorageoverheads.
10 Discussions
Impactofworkloadvariationonpresetthresholdandalerts.
(a)FNR (b)CPUandmemoryutilization
IndeploymentsusingorchestratorslikeKubernetes,podautoscal-
Figure16:ComparisonbetweenPerfMon(P)andTCP-stats ingensuresapredictablemaximumworkloadateachpodasthe
basedmonitoring(T) workloadvaries.Basedonthepredictions,itisfeasibletoderivea
presetthresholdtodetectanomalies.Insuchcases,higherappli-
successfullycapturesallthefaultswhenthefaultlastsfor8msor
cationloaddoesnotleadtolatencyanomalies;therefore,donot
more(Fig.16a).However,onthecontrary,withTCP-stats-based
generatealerts.Hence,variationinworkloaddoesnotrequireany
monitoring,weobservethatwhenthedelaylasts8msand16ms,
changeinthepresetthreshold.However,ifanincreasedworkload
theFNRisashighas81%and79%.ThisisbecauseTCP-stats-based
stillresultsinlatencyanomalies,itindicatesanunderlyingissue.
monitoringdoesnotmonitorper-packetlatenciesandhenceisnot
Insuchscenarios,PerfMoncorrectlydetectstheanomalyandgen-
fine-grainedenoughtocapturetransientsporadicfaults.Addition-
eratesalerts,whichistheintendedbehavior.PerfMonuse40%load
ally,whencomparedwithPerfMon,always-onTCP-stats-based
asthebaselineworkloadforderivingthethreshold.However,ifthe
monitoringrequires6xand24xmoreCPUandmemory(Fig.16b).
operatorwishestochangethebaselineworkload(duetoapplica-
tionfeaturechange/optimization/configurationandinfrastructure
9 RelatedWork
changeetc.),thenPerfMonrequiresreprofilingtheapplicationat
Application-leveltracing.Application-leveltracingtools[5,13, thenewbaselineloadandupdatingthethresholdvalues.
19,35,43,45,50,52]providethedatapath(microservices)thata ImpactofsoftwareandhardwareupgradesonPerfMonthresh-
requesthastraversedandtheamountoftimespentateachmicroser- old.Inthecloud,operatorsoftenperformperiodicupdatesand
vice.However,theydonotprovidevisibilitybelowtheapplication maintenanceoftheoperatingsystem,middleware,andtheunder-
layer.Thatis,theycantellwhichRPCinagivenuserrequestis lyinghardwareinfrastructure.Thesetasksareoftentransparent
experiencingdelaysbutcannottellwhichunderlyingentityand tothetenantsandperformedwithoutimpactingtheapplication
associatedcomponentiscausingthosedelays. SLA.ThoughanOSupgradeorahardwareupgradecanimprove
Host-leveltracing.End-hosttracingtools[11,12,16,22,33,39] thebaselineRNST,CNST,andRTTvalues,PerfMonneednotre-
providedeepvisibilityintohost-levelevents.Forinstance,NSight[39] computethethresholdbecauseanyanomalyattheRPClevelthat
capturestheendhostsystemstateusingahardwareprofilingtool potentiallycausesanSLAviolationisstilldetectedbythepreset
calledintel_pt[25]andidentifiestherootcauseofdelays.Though threshold.However,iftheproviderandthetenantdecidetoupdate
suchtoolscanidentifytheproblematiccomponent,theysuitwell theSLAfollowingtheupgrade,thenPerfMonrequiresreprofiling
forafter-the-factrootcauseanalysisbecauseoftheirhighstorage andupdatingthethreshold.Theprovidercanplantoreprofileei-
overheads.Weobservethatrunningintel_ptfor30secondsand60 therduringtheplannedmaintenancewindoworduringnon-peak
secondsrequiresaround440MBand1GBofstoragespace,respec- hourstominimizetheimpactontheapplicationperformance.
tively.Weenvisionsuchtoolscomplementourapproach–after
identifyingtheproblematiccomponent,component-leveltraces
providedbythesetoolhelpstofindtherootcause. 11 Conclusion
NIC-levelmonitoring.BuffScope[37]isabuffer-basedrequest WepresentPerfMon,alightweightperformancemonitoringsys-
eventmonitoringsystemthatprovidesend-to-endvisibilityacross temthatenablestheautomaticidentificationofbottleneckcompo-
differententitiesandalsoattheend-hoststacklevel.Visibilityatthe nentsinthehostnetworkstack.PerfMoncomplementstheexisting
end-hoststackisachievedbymonitoringvariousbufferevents,and application-levelmonitoringsystemandhelpstoquicklyassignthe
end-to-endvisibilityisachievedbyRPCpacketinstrumentation, issuetotherightteaminoperations.WedevelopedPerfMonusing
leveragingthecapabilitiesofSmartNICs.Buffscopeassumesthat eBPFtechnologyandtesteditbydeployingitonaKubernetes-
thedatacentre’seast-westtraffic isunencrypted, whichmakes managedclusterofservers.PerfMon’smonitoringoverheadsare
packet-levelinstrumentationlesspracticaltodeploy. lowanddetectthebottleneckcomponentwithhighaccuracy.
Networkmonitoring.Networkmonitoringtools[38,40,42,44,
48,51]providedetailsofflowssubjecttocongestionataswitchin 12 Acknowledgements
adatacenternetworkspace.SincetheRPCinformationfroman Wethanktheanonymousreviewersfortheirthoughtfulfeedback.
applicationtracecontainsflowinformationintheclusteraddress WethankAnirudhSivaramanforhisvaluableinputontheearlier
space,thisinformationisinsufficientforcorrelatingflowinforma- draftthathelpedimprovethepapersubstantially.Wealsothank
tionfromdifferentlocations,hinderingend-to-endvisibility. PrashanthPS,KShivKumar,andHarishSAfortheirparticipation
Hostnetworkstack-levelmonitoring.Host-INT[49],aneBPF- inthediscussionsandfeedback.ThisworkissupportedbyNM-
basedsystem,extendsINT[18]supporttotheend-hostnetwork- ICPSTiHAN,PMRF,NationalSecurityCouncilSecretariat(NSCS),
ingstack.Thisprovidesend-to-endvisibilityaspacketstraverse ZFTechnologies,andMarvellTechnologies.
441

PerfMon:PerformanceMonitoringofHostNetworkStack SoCC’25,November19–21,2025,Online,USA
| References |     |     |     | implicationsforcloud&edgesystems.InASPLOS. |
| ---------- | --- | --- | --- | ------------------------------------------ |
tc-netem(8)—Linuxmanualpage. [37] KaihuiGao,ChenSun,ShuaiWang,DanLi,YuZhou,HongqiangHarryLiu,
| [1] 2011. |     | Retrieved"December2023"from |     |     |
| --------- | --- | --------------------------- | --- | --- |
https://man7.org/linux/man-pages/man8/tc-netem.8.html LingjunZhu,andMingZhang.2022. Buffer-basedend-to-endrequestevent
monitoringinthecloud.InUSENIXNSDI).
| [2] 2013. QueueingintheLinuxNetworkStack. |     | Retrieved"October2024"from |     |     |
| ----------------------------------------- | --- | -------------------------- | --- | --- |
[38] ArpitGupta,RobHarrison,MarcoCanini,NickFeamster,JenniferRexford,and
https://www.coverfire.com/articles/queueing-in-the-linux-network-stack/
[3] 2013.ss(8)—Linuxmanualpage. Retrieved"October2024"fromhttps://man7. WalterWillinger.2018.Sonata:Query-drivenstreamingnetworktelemetry.In
ACMSIGCOMM.
org/linux/man-pages/man8/ss.8.html
[4] 2014.flannel. https://github.com/flannel-io/flannel [39] RoniHaecki,RadhikaNiranjanMysore,LalithSuresh,GerdZellweger,BoGan,
TimothyMerrifield,SujataBanerjee,andTimothyRoscoe.2022.Howtodiagnose
| [5] 2014.Zipkin. | Retrieved"December2023"fromhttps://zipkin.io/ |     |     |     |
| ---------------- | --------------------------------------------- | --- | --- | --- |
2015.lsof(8)—Linuxmanualpage. nanosecondnetworklatenciesinrichend-hoststacks.InUSENIXNSDI.
| [6] |     | Retrieved"October2024"fromhttps://man7. |     |     |
| --- | --- | --------------------------------------- | --- | --- |
org/linux/man-pages/man8/lsof.8.html [40] NikhilHandigol,BrandonHeller,VimalkumarJeyakumar,DavidMazières,and
2015.ntttcp-for-linux. NickMcKeown.2014. Iknowwhatyourpacketdidlasthop:Usingpacket
[7] Retrieved"July2025"fromhttps://github.com/microsoft/ historiestotroubleshootnetworks.InUSENIXNSDI.
ntttcp-for-linux
[41] HiranyaJayathilaka,ChandraKrintz,andRichWolski.2017.Performancemoni-
| [8] 2015. perf-record(1)—Linuxmanualpage. |     | Retrieved"October2024"from |     |     |
| ----------------------------------------- | --- | -------------------------- | --- | --- |
toringandrootcauseanalysisforcloud-hostedwebapplications.InProceedings
https://man7.org/linux/man-pages/man1/perf-record.1.html ofthe26thInternationalConferenceonWorldWideWeb.
| [9] 2015. Thestoryofonelatencyspike. |     | Retrieved"December2023"fromhttps: |     |     |
| ------------------------------------ | --- | --------------------------------- | --- | --- |
[42] RajJoshi,TingQu,MunChoonChan,BenLeong,andBoonThauLoo.2018.
//blog.cloudflare.com/the-story-of-one-latency-spike/
[10] 2016.NETRONOME. Retrieved"December2023"fromhttps://www.netronome. BurstRadar:Practicalreal-timemicroburstmonitoringfordatacenternetworks.
InProceedingsofthe9thAsia-PacificWorkshoponSystems.
com/products/agilio-cx/
[11] 2017. Uprobe-tracer:Uprobe-basedEventTracing. https://www.kernel.org/doc/ [43] JonathanKaldor,JonathanMace,MichałBejda,EdisonGao,WiktorKuropatwa,
Documentation/trace/uprobetracer.txt JoeO’Neill,KianWinOng,BillSchaller,PingjiaShan,BrendanViscomi,etal.
2017.ftrace-FunctionTracer. 2017.Canopy:Anend-to-endperformancetracingandanalysissystem.InACM
| [12] | https://www.kernel.org/doc/Documentation/trace/ |     |     | SOSP. |
| ---- | ----------------------------------------------- | --- | --- | ----- |
ftrace.txt
[44] PraveinGovindanKannan,NishantBudhdev,RajJoshi,andMunChoonChan.
| [13] 2017. Jaeger: | open source, end-to-end | distributed tracing. | https://www. |     |
| ------------------ | ----------------------- | -------------------- | ------------ | --- |
jaegertracing.io/ 2021.DebuggingTransientFaultsinDataCentersusingSynchronizedNetwork-
widePacketHistories..InUSENIXNSDI.253–268.
| [14] 2019. DeathStartBench. | Retrieved"December2023"fromhttps://github.com/ |     |     |     |
| --------------------------- | ---------------------------------------------- | --- | --- | --- |
[45] HaifengLiu,JinjunZhang,HuasongShan,MinLi,YuanChen,XiaofengHe,and
delimitrou/DeathStarBench
[15] 2019.DebuggingnetworkstallsonKubernetes. https://github.blog/2019-11-21- XiaoweiLi.2019.Jcallgraph:tracingmicroservicesinverylargescalecontainer
cloudplatforms.InCloudComputing–CLOUD2019:12thInternationalConference,
debugging-network-stalls-on-kubernetes/
[16] 2019.KernelProbes(Kprobes). Retrieved"December2023"fromhttps://www. HeldasPartoftheServicesConferenceFederation,SCF2019,SanDiego,CA,USA,
June25–30,2019,Proceedings12.
kernel.org/doc/Documentation/kprobes.txt
Dynamicallyprogramthekernelforefficientnetworking,observability, [46] MattMathis,JohnHeffner,PeterO’neil,andPeteSiemsen.2008. Pathdiag:
| [17] 2020.           |                                            |     |     | automatedTCPdiagnosis.InPAM. |
| -------------------- | ------------------------------------------ | --- | --- | ---------------------------- |
| tracing,andsecurity. | Retrieved"October2025"fromhttps://ebpf.io/ |     |     |                              |
In-bandNetworkTelemetry(INT)DataplaneSpecificationl. [47] ShicongMeng,ArunKIyengar,IsabelleMRouvellou,andLingLiu.2013.Volley:
| [18] 2020. |     |     | Retrieved |     |
| ---------- | --- | --- | --------- | --- |
"December2023"fromhttps://p4.org/p4-spec/docs/INT_v2_1.pdf Violationlikelihoodbasedstatemonitoringfordatacenters.InIEEEICDCS.
[48] SrinivasNarayana,AnirudhSivaraman,VikramNathan,PrateeshGoyal,Venkat
| [19] 2020.OpenTelemetry. | https://opentelemetry.io/ |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- |
2020.ScalingintheLinuxNetworkingStack¶. Arun,MohammadAlizadeh,VimalkumarJeyakumar,andChanghoonKim.2017.
| [20] |     | Retrieved"February2025"from |     |     |
| ---- | --- | --------------------------- | --- | --- |
https://docs.kernel.org/networking/scaling.html Language-directedhardwaredesignfornetworkperformancemonitoring.In
| WanttoDebugLatency? |                                           |     |     | ACMSIGCOMM. |
| ------------------- | ----------------------------------------- | --- | --- | ----------- |
| [21] 2020.          | Retrieved"October2024"fromhttps://rakyll. |     |     |             |
medium.com/want-to-debug-latency-7aa48ecbe8f7 [49] TomaszOsińskiandCarmeloCascone.2021. Achievingend-to-endnetwork
visibilitywithhost-int.InProceedingsoftheSymposiumonArchitecturesfor
| [22] 2022.perf-PerformanceanalysistoolsforLinux. |     | https://man7.org/linux/man- |     |     |
| ------------------------------------------------ | --- | --------------------------- | --- | --- |
NetworkingandCommunicationsSystems.140–143.
pages/man1/perf.1.html
[23] 2022.stress-ng-atooltoloadandstressacomputersystem. Retrieved"December [50] BenjaminHSigelman,LuizAndréBarroso,MikeBurrows,PatStephenson,Manoj
Plakal,DonaldBeaver,SaulJaspan,andChandanShanbhag.2010. Dapper,a
2023"fromhttps://manpages.ubuntu.com/manpages/jammy/man1/stress-ng.1.
html large-scaledistributedsystemstracinginfrastructure.(2010).
[51] WeitaoWang,XinyuCrystalWu,PraveenTammana,AngChen,andTSEugene
| [24] 2022. wrk2. | Retrieved"December2023"fromhttps://github.com/delimitrou/ |     |     |     |
| ---------------- | --------------------------------------------------------- | --- | --- | --- |
Ng.2022. Closed-loopnetworkperformancemonitoringanddiagnosiswith
| DeathStarBench/tree/master/wrk2              |     |                             |     | {SpiderMon}.InUSENIXNSDI. |
| -------------------------------------------- | --- | --------------------------- | --- | ------------------------- |
| [25] 2023. perf-intel-pt(1)—Linuxmanualpage. |     | Retrieved"December2023"from |     |                           |
[52] LiWu,JohanTordsson,ErikElmroth,andOdejKao.2020.Microrca:Rootcause
https://man7.org/linux/man-pages/man1/perf-intel-pt.1.html localizationofperformanceissuesinmicroservices.InIEEE/IFIPNOMS.
| [26] 2024. TheStateofeBPF. | Retrieved"November2024"fromhttps://www. |     |     |     |
| -------------------------- | --------------------------------------- | --- | --- | --- |
[53] MinlanYu,AlbertGreenberg,DaveMaltz,JenniferRexford,LihuaYuan,Srikanth
linuxfoundation.org/hubfs/eBPF/The_State_of_eBPF.pdf
Kandula,andChanghoonKim.2011.Profilingnetworkperformanceformulti-tier
[27] BehnazArzani,SelimCiraci,LuizChamon,YiboZhu,HongqiangHarryLiu,Jitu datacenterapplications.InUSENIXNSDI.
Padhye,BoonThauLoo,andGeoffOuthred.2018.007:Democraticallyfinding
thecauseofpacketdrops.InUSENIXNSDI.
[28] BehnazArzani,SelimCiraci,BoonThauLoo,AssafSchuster,andGeoffOuthred.
2016.Takingtheblamegameoutofdatacentersoperationswithnetpoirot.In
ACMSIGCOMM.
[29] HongZhang1JunxueZhang1WeiBaiandKaiChen1MosharafChowdhury.
2017.ResilientDatacenterLoadBalancingintheWild.(2017).
[30] JessicaBerg,FabianRuffy,KhanhNguyen,NicholasYang,TaegyunKim,Anirudh
Sivaraman,RaviNetravali,andSrinivasNarayana.2021.Snicket:Query-driven
distributedtracing.InACMHotNetsWorkshop.
[31] QizheCai,ShubhamChaudhary,MidhulVuppalapati,JaehyunHwang,andRachit
Agarwal.2021.Understandinghostnetworkstackoverheads.InACMSIGCOMM.
[32] XiaoqiChen,HyojoonKim,JavedMAman,WillieChang,MackLee,andJennifer
Rexford.2020.MeasuringTCPround-triptimeinthedataplane.InProceedings
oftheWorkshoponSecureProgrammableNetworkInfrastructure.
| [33] MathieuDesnoyersandMichelRDagenais.2006. |     | Thelttngtracer:Alowim- |     |     |
| --------------------------------------------- | --- | ---------------------- | --- | --- |
pactperformanceandbehaviormonitorforgnu/linux.InOLS(OttawaLinux
Symposium).Citeseer.
[34] LizFong-JonesandAdamMckaig.2018.ResolvingOutagesFasterwithBetter
DebuggingStrategies.(2018).
[35] RodrigoFonseca,GeorgePorter,RandyHKatz,andScottShenker.2007.X-trace:
Apervasivenetworktracingframework.InUSENIXNSDI.
[36] YuGan,YanqiZhang,DailunCheng,AnkithaShetty,PriyalRathi,NayanKatarki,
| ArianaBruno,JustinHu,BrianRitchken,BrendonJackson,etal.2019. |     |     | An  |     |
| ------------------------------------------------------------ | --- | --- | --- | --- |
open-sourcebenchmarksuiteformicroservicesandtheirhardware-software
442