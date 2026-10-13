2.6 6.1
Article
A Rule-Based Method for
Enhancing Burst Tolerance in
Stateful Microservices
Kęstutis Pakrijauskas and Dalius Mažeika
Special Issue
New Advances in Cloud Computing and Its Latest Applications
Edited by
Dr. Pablo Alejandro Quezada-Sarmiento
https://doi.org/10.3390/electronics14142752

Article
A Rule-Based Method for Enhancing Burst Tolerance in
Stateful Microservices
Ke˛stutisPakrijauskas*andDaliusMažeika
DepartmentofInformationSystems,FacultyofFundamentalSciences,VilniusGediminasTechnicalUniversity,
SauletekioAvn.,11,10223Vilnius,Lithuania;dalius.mazeika@vilniustech.lt
* Correspondence:kestutis.pakrijauskas@vilniustech.lt
Abstract
Microservicearchitectureenablesthedevelopmentofflexible,looselycoupledapplications
thatsupportelasticityandadaptability. Asdataavailabilityiscriticalinanyapplication,
maintainingconsistentaccessbecomesatoppriority. However,thisintroducescomplexity,
particularlyforstatefulmicroservices,whichareslowertoadapttosuddenchangesand
canleadtodataavailabilitydegradation. Resourceoverprovisioningmaypreparesystems
forpeakloads;however,itisaninefficientmethodofproblem-solving. Similarly,dynamic
scalingbasedonmachinelearningcanunderperformduetoinsufficienttrainingdataor
inaccuratepredictionmethods. Thispaperproposesarule-basedmethodthatcombines
write-scaling and load balancing to distribute burst workloads across multiple stateful
microservice nodes while also vertically scaling a single node to meet rising demand.
Thisapproachreducesfailureratesandextendsoperationaltimeunderburstconditions,
effectively preserving the application’s availability by providing more time for scaling.
An experiment was performed to validate the proposed method of burst tolerance by
workloaddistribution. Theresultsshowedthattheproposedmethodenablesastateful
microservicethatsustainstheburstloadfornearlytwiceaslongwhilefurtherreducing
therateoffailure.
Keywords: statefulmicroservice;availability;database;cluster;Kubernetes;failover;burst;
AcademicEditors:George write-scaling
AngelosPapadopoulosandPablo
AlejandroQuezada-Sarmiento
Received:5June2025
Revised:1July2025 1. Introduction
Accepted:4July2025
Microservices,aformofService-OrientedArchitecture,arespecialized,looselycou-
Published:8July2025
pled,andautonomousservicesthatmakeupanapplication. However,withlowcoupling
Citation: Pakrijauskas,K.;Mažeika,
andindependencefromotherservicescomesanincreasedpaceofcodedeploymentand
D.ARule-BasedMethodfor
scalability,andthereareinheritedchallengessuchastheFederatedMultidatabase[1,2]
EnhancingBurstToleranceinStateful
Microservices.Electronics2025,14, andBackupAvailabilityConsistency[3]. Thecomponentsofmicroservicesaredesigned
2752. https://doi.org/10.3390/ tomanagefailuresratherthanpreventthem[4,5]. Duetotheirdesignwithindependence
electronics14142752 andscalabilityinmind,individualcomponentsofamicroservice-basedapplicationcan
Copyright:©2025bytheauthors. scale independently to match incoming workloads [4]. However, allocating excessive
LicenseeMDPI,Basel,Switzerland. computingresourcescanleadtounnecessarycosts,whileinsufficientprovisioningmay
Thisarticleisanopenaccessarticle negativelyimpactthequalityofservice. Thehighlydynamicnatureofworkloadsfurther
distributedunderthetermsand
complicatesthechallengeofefficientresourceallocation. Asuddentemporaryworkload
conditionsoftheCreativeCommons
increase,commonlyreferredtoasaburst,mightimpactthequalityofservicesprovided
Attribution(CCBY)license
andreduceavailabilitymetricsifnothandledeffectively. Thereisachallengerelatedto
(https://creativecommons.org/
licenses/by/4.0/). schedulingstatefulcontainers,whichfurtherhinderstheresponsetoburstworkloads. The
Electronics2025,14,2752 https://doi.org/10.3390/electronics14142752

Electronics2025,14,2752 2of19
schedulingorreschedulingofstatefulworkloadsmightrequiredatatobemoved,which
takesadditionaltimebeforeacontainerishealthyandreadytoacceptconnections[6].
Giventhedynamicnatureofmodernapplications,adilemmaexistsastowhethercom-
putingresourcesshouldbeoverprovidedtomeetoccasionalworkloadburstsorconserved,
providingonlyenoughtoaccommodateaverageworkloads[7–9]. Whileoneapproach
reduces the number of Serve Level Objective (SLO) breaches, the other conserves com-
putingresourcesandreducesbothcostsandcarbonfootprint. Adynamic, data-driven
approach would involve using machine learning (ML) to forecast workloads and scale
microservicesaccordingly[10,11]. However,ML-basedalgorithmsrequirebothsufficient
dataandtrainingtimetodevelopmodelscapableofpredictingfutureresourcedemands.In
thecaseofhighlydynamicworkloads,thesepredictionsmaylackthenecessaryprecision,
leadingtosuboptimalscalingdecisions.
Furthermore,relationaldatabasemanagementsystems(RDBMSs)introduceadditional
challengeswhenhandlingburstworkloads,astheyinvolvemanagingthestate,thatis,
throughpersistentdata. Scalingsuchsystemstypicallyrequiresreadingdatafromadisk,
and in all scenarios involving highly available stateful microservices, data replication
acrossnodesbecomesessential[12,13]. Secondly,ifaburstworkloadcannotbeproperly
handled,databasenodesthatexceedtheirallocatedmemoryareterminated. Thisleadsto
thelossofclientconnectionstothedatabaseclusterand,inmostcases,theterminationof
in-progressqueries,resultinginabreachofservicelevelobjectives(SLOs).Additionally,the
failuretriggersare-electionprocesstodesignateanewprimarynodeamongtheremaining
databasenodes,potentiallycausingfurtherdisruptionstoavailability.
ML-based workload prediction methods can enable the more accurate, proactive
scalingofstatefulmicroservicesinanticipationofworkloadspikesanddrops. However,if
scalingistriggeredtoolateorifinsufficientresourcesareallocated,themicroservicemay
underperform,potentiallyleadingtoabreachofavailabilityservice-levelobjectives(SLOs).
Inthisresearch,weproposearule-basedmethodtoenhanceresilienceagainstburst
workloads. Specifically,weevaluatedwhetherthewrite-scalingandrequest-routingca-
pabilities of a load balancer can be adapted to improve the burst tolerance of stateful
microserviceswhileoneofthenodesisscaledverticallytomeettheincreaseddemand.
Additionally,ourpreviousresearchhasdemonstratedthatitispossibletoperformmainte-
nance,includingtheverticalscaling,ofMulti-Primarydatabaseclustersinanorchestrated
containerenvironment[14]. Theresultsdemonstratethatadatabaseclustercansuccess-
fully handle sudden and significantly increased workloads, both in terms of sustained
processingtimeandreducederrorrates. Theaddedcapacity—particularlytheextended
timeunderload—enablesmoretimetoperformverticalscalingtoprocessburstworkloads,
consequentlyallowingtheavoidanceofunnecessarydipsintoavailabilitybudgets.
Thispaperisorganizedasfollows: Section2presentsaliteraturereviewonthetopics
ofstatefulmicroserviceavailabilityandreliabilityandtheprinciplesthattheproposed
methodisbasedupon;Section3describesthemethodwepropose;Section4outlinesthe
investigatedarchitecture;Section5describestheexperimentalsetup;Section6contains
resultsoftheexperiment;andconclusionsarepresentedinSection7.
2. BackgroundandRelatedWork
Traditionally,asuddenandsignificantincreaseinrequestsforaserviceisknownas
aburst. Aburstisusuallycausedbyasuddenincreaseinuseractivityduetounpredicted
events. AnexampleinFigure1illustratestheincreaseddemand—aburst—onMichael
Jackson’s Wikipedia entry, both days in advance and after his death [15]. It is worth
mentioningthataburstmaybecausedbyaDenialofServiceattackaswell[15]. Such
workloadmayleadtoadecreasedqualityofserviceandviolationofSLOs,includingaloss

Electronics2025,14,2752 3of19
ofavailability. Aburstcanbeunpredictableintermsofloadvolumeandasaneventin
time[15].Thetwoprimarypropertiesofaburstareintensityandduration[15,16].Intensity
definesthenumberofrequests,whiledurationdefinesthelengthoftimethataservice
experiencestheadditionalworkload.
Figure1.Anexampleofrequests.Whenastatefulservice,notnecessarilyamicroservice,isinvolved,
aburstcanhaveanadditionalpropertyofdataspikes,includinganincreaseddemandforaparticular
setofdata.Forexample,inascenariowherethedataaredistributedacrossapartitioneddatabase,
asignificantincreaseindemandforaparticularsubsetofdatacanbeconsideredaburst,whileon
theaccesslayer,thenumberofoverallrequestsremainsthesame[16].
Therearedifferentwaystomeasureburstworkloads,forexample,bycalculatingthe
standarddeviationfromthemovingaverage,normalizedentropy,orsampleentropy[15].
Forourexperiment,weaimedtogeneratealinearsyntheticburst. Thus,asWoodrufetal.
suggested,wedefinedaburstasasequenceofxrequestsarrivingwithinytimeofeach
other[17].
An application or a service may scale up or undertake other means to process the
loadifburstsarepredictedorperiodic. However,workloadburstsbecomeachallenge
ifunpredictable: asystemmightnotbeabletooperateproperlyunderstress. Generally,
twoapproachescanbetakentomanageburstworkloads: staticordynamic.
Thestaticapproachisquitesimple:allocateasufficientnumberofcomputingresources
tohandleapotentialburstworkload. Thisapproachismoreexpensive;however,allocating
enoughcomputingresourcestohandleburstworkloadsmayleadtotheoverprovision
ofresources. Resourcesforservicescanbeoptimallyallocatedtomicroserviceswithout
impacting the latency of user requests [18]. Baarzi and Kesidis were able to improve
resourceallocationby22%whileimprovingrequestlatencyby20%. However,itisthe
unpredictabilityofburstworkloadsthatposesariskregardlessofhowoptimaltheresource
allocationis.
Thedynamicapproachisdata-driven: aburstispredicted,andasystemscalesup
accordinglytohandletheload.Thesecondapproachrequiresanelasticsystemanddifferent
mechanismstopredictupcomingbursts[11,19,20].Lassnigetal.presentanaverages-based

Electronics2025,14,2752 4of19
modelthatprovidesanestimatedprobabilitythataburstisgoingtohappen. However,
astheauthorssay,themodelneedsoptimization[11]. Iqbaletal. usedtheexpectation-
maximizationmethodandScale-WeightedKmeanstopartitionservicerequestlogsinorder
tocaptureworkloadcharacteristics. Thedistributionofthecharacteristicswasthenused
tocomputetheprobabilityvectordescribingthedistributionofincomingrequests. Itwas
thenusedtoproactivelyauto-scaleapplications[19]. PBScaler,asproposedbyXieetal.,
collectsthereal-timeperformancemetricsofapplicationsandbuildsacorrelationgraph
betweenmicroservices. Theproposedscalingmethodachievesprecisionupto0.92using
the Random Forest algorithm, and TopoRank, a random walk algorithm, was able to
identifythelikelybottlenecks[20].
Aburstmayexhaustvarioussystemresources,suchastheCentralProcessingUnit
(CPU), memory, network bandwidth, disk throughput, etc. While a lack of sufficient
computingpower,slownetwork,andlowdiskreadspeedshaveanimpactontheSLO,itis
memoryexhaustionthathasthemostsignificantimpactonstatefulmicroserviceavailability.
Acontaineristerminatedwhenitreachesthelimitofallocatedmemory[21]. Relational
databasemanagementsystems,forexample,MySQL,usememorytocachedata,query
executionplans,monitordata,storeclientconnectionbuffersandthreadstacks,etc.[22].
Thus,duringaburst,memoryisexhaustedbothbytheadditionalclientconnectionsand
theincreaseddemandtoaccesscachedata.
All nodes of Multi-Primary database management systems are equal, and all can
processreadandwriterequestsatthesametime. However,writescaling,whichrefersto
theprocessofincreasingthecapacityorcapabilityofasystemtohandlealargervolumeof
writeoperations,isnotrecommended: theimprovementinwritethroughput,evenwith
onlytwowriternodes,isusuallylimited[23]. Thewriteonadatabasenodeisprocessed,
andonlythestateupdateistransferredtotheothernodes,sothereisnoneedtoreprocess
the write again [24]. If one node is designated for processing write requests, only its
memoryisusedtocacheprocessing-relateddata,suchasexecutionplans.
3. TheMethodofBurstTolerance
Inthissection,wepresenttheproposedmethodusedtoenhancethebursttolerance
ofstatefulmicroservices. Inorchestratedenvironments,containersareassignedlimited
computingresources,makingthemsusceptibletoexhaustionunderhighloads. Thisrisk
isfurtheramplifiedbytheburst-typeworkload. Statefulmicroservicesrequirememory
to process incoming requests, which are utilized for various purposes such as caching,
connectionbuffering,andqueryexecution. Consequently,thereisalimittothenumberof
concurrentrequestsandclientsasinglenodecanhandle. Inclusteredstatefulsystemssuch
asdatabases,multiplenodesareavailabletosharetheworkload.
Wearguethatwritescalingmayhaveabenefitinincreasingtheoverallcapacityfor
bothreadandwriterequests. Requestsareprocessedonlyononenode;onlythenewstate
ofdataistransferredtotheSecondarynodes. ThememoryutilizationontheSecondary
nodes is lower. Thus, there is room to process queries as the cache has space to keep
queryplansandtemporarydata. Ontheotherhand,thereisariskofreducedthroughput
andreplicationconflictsasdatabasenodesarelikelytoperformattheedgeofcapacity.
However,ifastatefulmicroserviceisnotcapableofhandlingaburstworkload,thechoice
hastobemadeastowhichSLOsaretobebreached: eitheracceptthelossofthroughput
whileminimizingornegatingthelossofavailabilityaltogetheroronlyacceptthelossof
availabilitybutatahigherscale.
Theproposedmethodaimstodistributetheburstworkloadwhilestatefulmicroservice
nodesarescaledupverticallytomatchtheincreaseddemandforresources(Figure2).

Electronics2025,14,2752 5of19
(a) (b)
Figure2.Flowdiagramofproposedbursttolerancemethod(a)andalternativeapproach(b).
A stateful microservice cluster with a minimum of three nodes is required for the
proposedmethodtofunction. Weconsideredaclusterwiththreenodesdb-nodes-[0−n],
where n ≥ 2. The flow of the proposed rule-based method is shown in Figure 2a. The
orchestrator,inthecaseoftheKubernetesoperator,monitorsresourceusageonthestateful
microservicenodes. OncethememoryonthePseudo-Primarynode,db-node-0,isabovethe
threshold,newconnectionsaremadeforthedb-node-mnode,wherem≥2,anddb-node-0
isdisallowedbythedatabaseproxy. Thedb-node-mnode,wherem ≥ 2,ispreparedfor
increaseddemand,whileanadditionalloadisdirectedtotheremainingnode,db-node-1.
The orchestrator starts the vertical scaling of the db-node-m, where m ≥ 2. Then, the
balancingbetweentheremainingtwoormorenodes,thePseudo-Primarydb-node-0and
db-node-1,begins:theorchestratormonitorsmemoryusageonthesetwonodesandinstructs
thedatabaseproxytodisallownewconnectionstothenodewithhighermemoryutilization,

Electronics2025,14,2752 6of19
effectivelybalancingtheloadbetweentwoormorenodes.Newconnectionsareestablished
withnodesthathavemoreavailablememory. Asmemoryutilizationonthedatabasenodes
db-node-0anddb-node-1changes, sodoesthenodewherenewconnectionsaredirected.
Alreadyestablishedconnectionsareleftintact. Oncedb-node-misused,wherem≥2,has
been scaled, the orchestrator instructs the database proxy to allow new connections to
beestablishedtowardsthatnodeandexistingonesaregracefullymovedfromdb-node-0
anddb-node-1: clientconnectionsareterminatedbythedatabaseengineandreestablished
towardsnodedb-node-m, wherem ≥ 2Thegracefultransferofconnectionstothenode
thatjustfinishedscalingverticallyisperformedwithnegligibleimpactonavailability. The
remainingnodesarethenscaledverticallyinsequencebytheorchestrator.
Thethresholdvaluesandthenewmemorylimitfortheclustercanbeselectedintwo
ways. First,thevaluescanbebasedonexpertknowledgeandwouldlikelyvarybased
ontheindividualortheteam. Dependingontheclustersize,thethresholdcouldbe85to
95percent,whilethememorylimitcouldbeincreasedbyanadditional10to25percent.
ML-basedpredictionvaluescouldfurtheroptimizeresourceusageasthethresholdand
newmemorylimitscouldbesetdynamicallybasedonhistoricalusagepatterns.
Although there are more metrics that could be used to measure the utilization of
astatefulmicroservice, thedecisionofwhethertobalancetheloadandinitiatevertical
scalingisbasedonmemoryusage. Othermetrics,suchasCPUutilizationpercentage,the
numberofrequests,responselatency,etc.,couldbeusedaswell. However,consideringthe
effectsofcontainermemoryexhaustion,thedegradationoftheaforementionedmetricsis
notasimpactfulonavailabilitySLO.
As an alternative, only new connections can be directed to a Secondary node. If
only one node is designated as the Pseudo-Primary, the other nodes only handle the
workload related to state transfer. Thus, their memory consumption is lower than that
ofaPseudo-Primarynode. Thereisnoneedtocachequeryexecutionplans,temporary
data,etc. Therefore,asimplerapproachwouldbetotransferonlythenewconnections
tothesecondarynode(Figure2b). However,wedonotexpectthismethodtobeonpar
withworkloadbalancing. Whenonlynewconnectionsareredirected,theremainingfree
memoryontheoriginalPseudo-Primarynodewillnotbeutilized.
4. ImplementationoftheMethod
Theproposedmethodallowedustotemporarilydistributetheloadacrossdatabase
clusternodesintheeventofaworkloadburst. Asshowninourpreviouswork,workloads
canbetransferredbetweendatabasenodeswithnegligibleimpactonavailability[8]. As
showninFigure3,thefoundationalcomponentsnecessaryforastatefulburstprotectorto
workarethefollowing:
1. AdatabaseclustersetupforMulti-Primaryreplication;
2. Aproxylayerthatcandirectclientrequeststoaspecificnode;
3. Aconnectionpooltoenablelow-latencydatabaseconnections.
Thecomponentsnecessaryfortransparentfailoverofclientsessionsbetweendatabase
nodesareasfollows:
4. Clientconnectionterminationmechanismconnections(astoredprocedure);
5. Aretrymechanismontheclient’ssidetohandletermination.
Thecomponentsnecessaryforastatefulburstprotectorareasfollows:
6. Aburst-protectormechanismfortriggeringafailoverandnodescale-upintheevent
ofaburst;
7. Amodifiedfailoverorchestratortooverseethescale-upandtransferworkloadtoan
appropriatelysizednodewithnegligibleimpactonavailability.

Electronics2025,14,2752 7of19
Figure3.Componentsthatarerequiredtoimplementtheproposedmethod.
Using Multi-Primary replication, a distributed database cluster maintains unin-
terrupted service for clients during an unplanned failover of connections between
database‘nodes.
Theproxylayerwiththecapabilitytoinspectthecomingqueriesenablesthebalancing
ofrequestsbetweennodeswhiletheburstworkloadisbeinghandled. Inaddition,itwill
beusedtotransferrequeststoascaled-upnodewithanear-zerolossofavailability. This
wastakenfromourpreviousworkandisshowninAlgorithm1.
Algorithm1: DirectDatabaseConnections
Input:dbNode,connectionAction
Output:returnMsg
1: proceduredirectDBConnections
2: /*higherweightincreasesthenodepriority*/
3: defaultNodePriority←10
4: ifconnectionAction=‘disallow’then
5: //weightvalued0disallowsnewconnectionstowardsthenode
6: nodePriority←0
7: setNodePriority(dbNode,nodePriority)
8: returnMsg←‘connectionsDisallowed’
9: endif
10: ifconnectionAction=‘allow’then
11: setNodePriority(dbNode,defaultNodePriority)
12: returnMsg←‘connectionsAllowed’
13: endif
14: returnreturnMsg
Thefailoverorchestrator,introducedinourpreviouswork,mustbemodifiedtomake
surethatthenodesarescaledupinacertainorder. Itisupdatedtoperformafailoverand
drainconnectionsonasinglenode. ItsalgorithmisdepictedinAlgorithm2.

Electronics2025,14,2752 8of19
Algorithm2: PrepareNodeforScaling
Input:dbNode,proxyNode
Output:exitStatus
1: procedureprepareNodeForScaling
2: clientConnectionState←proxyNode.directDBConnections(dbNode,‘disallow’)
3: ifclientConnectionState=’connectionsDisallowed‘then
4: terminateClientConnections.state←dbNode.terminateClientConnections()
5: endif
6: ifterminateClientConnections=‘connectionsDrained’
7: returnSUCCESS
8: endif
Giventhatthereareatleastthreenodesinthecluster,onenodeisscaledup,while
the workload is balanced between the other two nodes. As shown in Algorithm 3, the
nodetodirecttheburstworkloadisselectedbasedonthememoryutilizationofthenodes.
Theworkloadisdirectedtothenodewithlowermemoryutilization. Thebalancingofthe
workloadbetweenthetwonodesisperformedwhilethethirdnodeisbeingscaledup.
Oncethethirdnodeisscaledandreadytoacceptconnections,thebalancingprocessreturns
amessageindicatingsuccess,andtheburstprotectorprocedurecontinuesmanagingthe
databaseclusterandworkload.
Algorithm3: BalanceWorkload
Input:dbNodeList,scaledDBNode,proxyNode,memoryThreshold
Output:exitStatus
1: procedureworkloadBalancer
2: /*callagenericproceduretogetinitialscalednodestatus*/
3: scaledNodeStatus←getNodeStatus(scaledDBNode)
4: /*balancetheconnectionswhilethenodescalingisnotcomplete*/
5:
whilescaledNodeStatus̸=
‘scalingComplete’
6: foreach: dbNode∈dbNodeList
7: /*callagenericproceduretogetmemoryusageandaddittoalist*/
8: dbNodesMemUsage[]←getNodeMemUsage(dbNode)
9: endfor
10: /*findthenodewiththehighestmemoryutilizationbyiteratingthelist*/
11: dbNodeMemHigh←dbNodesMemUsage[0]
12: foreach: dbNodeMemUsage∈dbNodesMemUsage[]
13: ifdbNodeMemHigh.memUtilization<dbNodeMemUsage.memUtilizationthen
14: dbNodeMemHigh←dbNodesMemUsage
15: endif
16: endfor
17: nodeConnectivityState←proxyNode.directDBConnections(dbNodeMemHigh,nodeName‘disallow’)
18: ifnodeConnectivityState=‘connectionsDisallowed’then
19: /*callagenericproceduretocheckscalednodestatus*/
20: scaledNodeStatus←getNodeStatus(scaledDBNode)
21: endif
22: endwhile
23: returnSUCCESS
Theburstprotectionmechanism,showninAlgorithm4,tracksmemoryusageandtrig-
gersboththebalancingofclientsessionsandscale-upoperationwhenacertainthreshold

Electronics2025,14,2752
9of19
ofmemoryutilizationisreachedonthePseudo-Primarydatabasenode. Oncethethreshold
is reached, the burst protector initiates the vertical scaling operation of the Secondary
nodewiththehighestmemoryutilizationandclientconnectionbalancingbetweenthe
Pseudo-Primarydatabasenodeandtheremainingnode. Thedatabasecluster,orratherthe
twobalancednodes,hasmorememorywithwhichtohandletheburstiftheSecondary
nodewiththehighestmemoryutilizationisscaledfirst. Whenthescalingupisfinished,
allclientconnectionsaretransferredtothenodewithmorecomputingresourcesfromthe
remainingtwonodes. Thesetwonodesarethenscaleduptomatchtheincreaseddemand.
| Algorithm4: | BurstProtectionMechanism |     |
| ----------- | ------------------------ | --- |
Input:dbNodeList,pseudoPrimaryNode,memoryThreshold
Output:exitStatus
1: procedureburstProtector
2: /*callagenericproceduretogetmemoryusageonpseudo-primarynode*/
3: dbNodeMemUsage←getNodeMemUsage(dbNode)
4: /*loopisexitedoncememoryutilizationonpseudo-primarynodeisabovethethreshold*/
whiledbNodeMemUsage≤memoryThreshold
5:
| 6:  | /*onlycheckmemoryutilizationonpseudo-primarynode*/ |     |
| --- | -------------------------------------------------- | --- |
| 7:  | /*whilememoryutilizationisbelowthethreshold*/      |     |
| 8:  | dbNodeMemUsage←getNodeMemUsage(pseudoPrimaryNode)  |     |
9: endwhile
10: /*collectmemoryusageonthenodes*/
| 11: foreach: | dbNode∈dbNodeList                         |                            |
| ------------ | ----------------------------------------- | -------------------------- |
| 12:          | ifdbNode.name̸=                           | pseudoPrimaryNode.namethen |
| 13:          | /*callagenericproceduretogetmemoryusage*/ |                            |
| 14:          | dbNodesMemUsage[]←getNodeMemUsage(dbNode) |                            |
| 15:          | endif                                     |                            |
16: endfor
17: /*findthenodewiththehighestmemoryutilizationbyiteratingthelist*/
18: dbNodeMemHigh←dbNodesMemUsage[0]
| 19: foreach: | dbNodeMemUsage∈dbNodesMemUsage[] |     |
| ------------ | -------------------------------- | --- |
20: ifdbNodeMemHigh.memUtilization<dbNodeMemUsage.memUtilizationthen
| 21: | dbNodeMemHigh←dbNodesMemUsage |     |
| --- | ----------------------------- | --- |
| 22: | endif                         |     |
23: endfor
24: /*callagenericproceduretoscalethenodeup*/
25: callperformDBNodeMaintenance(dbNodeMemHigh)
26: /*startbalancingsessionsbetweentworemainingnodes*/
27: balancedNodesList←dbNodeList.removeItem(dbNodeMemHigh)
28: callworkloadBalancer(balancedNodesList,dbNodeMemHigh,proxyNode,memoryThreshold)
29: returnSUCCESS
Thereareacoupleofadvantagestotheproposedmethodcomparedtoothertech-
niquestohandleaburst:
• Norelianceonhistoricaldata. Undoubtedly,workloadpredictionusingMLisapow-
erfulwaytoprepareforaburst. However,thepredictionmaybeimpreciseifthereis
notenoughdatatopredictaburst. Theproposedmethodgivesanadditionallayerof
protectionagainstincidentsrelatedtostatefulmicroservicesthatdonothandleaburst
properly. Expertknowledgeoradviceissufficienttosetthememoryusagethreshold.

Electronics2025,14,2752 10of19
• Themethodispredictable. Arule-basedapproachistransparentastheoutcomeis
predefinedbyanunderstandablesetofrules. Inaddition,suchanapproachdoesnot
requiretheadditionalcomputingresourcesthatanML-basedapproachwouldneed.
• Appropriateresourceallocation. Statefulmicroserviceshavesufficientresourcesto
handlethebaselineload. Additionalresourcesareallocatedonlywhenthereisaneed
tohandlemoreload.
Ifnohistoricaldataareavailable,thenthe“traditional”approachisusedtoacceptthe
lossofavailabilitywhileastatefulmicroserviceisscaledup. Theproposedmethodallows,
toacertainextent,thelossofavailabilitytobeminimizedasastatefulmicroservice,evenif
itrunsoutofmemory,asitcanoperateunderincreasedloadsforlongerdurationsoftime.
Theotherapproachisthrottlingtheclients[25]. However,themethodwepropose
doesnotrequireanyactiontobetakenontheclient’ssideofastatefulmicroserviceunder
burstconditions. This,inturn,followsthemicroserviceparadigmofreducedcoupling.
Ofcourse,ifaburstworkloadcannotbebalancedbetweenthedatabasenodesdueto
resourceconstraints,therearenotmanychoicesbuttoacceptthelossofavailability.
AprototypeoftheproposedmethodisavailableonGitHub[26].
5. EvaluationoftheMethod
Anexperimentwasconductedtoevaluatetheeffectivenessoftheproposedmethod
underburstconditions,andthiswascomparedagainsttheout-of-the-boxfunctionalityof
aMySQLGaleraclusterinhandlingburstworkloadbalancing. Aprototypeenvironment
wasbuilt,incorporatingthefollowingnecessarycomponents: adatabaseproxy,adatabase
cluster, a burst protection orchestrator, and a client. A synthetically generated dataset,
alongwithasyntheticworkload,wasusedtosimulateburstscenariosandassesssystem
behavior. Inourexperiment,wefocusedonthefollowingpoints:
• Operational time under burst—this is the time in which the nodes, other than the
onebeingscaledup,areabletohandleaburstworkload. Inotherwords,thetime
memoryutilizationincreasesfromthesetbalancingthresholdtothelimit.
• Thenumberoffailedrequestsifscalingissuccessful.Wepresumethatifoneofthenodes
doesnotscaleontime,thelossofavailabilityistoogreat.Inaddition,thewayrequests
arehandledduringaburstoperationisimportant. AssuggestedbyHaueretal.,the
percentageratiooffailedandsuccessfulrequestswillbethemeasureofavailability[27].
The investigated architecture of the cluster is shown in Figure 4. The prototype
environment,basedontheinvestigatedarchitecture,wassetuponathree-nodeKubernetes
cluster in the Google Cloud Platform (GCP). The three nodes were identical: E2 cost-
optimizedinstanceswith6GBofmemory,4CPUs,and50GBofstandardpersistentdisk
(PD).TheMySQLGaleraclusterwaschosenasthisdatabasemanagementsystemhasthe
capabilityofmulti-masterreplication. ProxySQLwasusedasthedatabaseproxy.
The database client was setup on a virtual machine (VM) in GCP. The VM was an
E2cost-optimizedinstancewith4CPUsand8GBofRAM,runningUbuntu22.04. The
failoverorchestratorwassetuponanE2cost-optimizedinstancewith1CPUand1GBof
RAM,runningUbuntu22.04. SoftwareversionsandresourceallocationfortheMySQL
GaleraclusterandProxySQLnodesarelistedinTable1.
Table1.Softwareversionsandresourceallocation.
SoftwareandVersion NumberofPods CPULimit MemoryLimit
MySQLGaleraCluster
3 500m 1024MB
8.0.36
ProxySQL2.2.5 2 400m 256MB

Electronics2025,14,2752 11of19
Figure4.Thearchitectureofthemulti-masterdatabaseclusterinvestigated.
TheYahoo! CloudServingBenchmark(YCSB)wasusedtogenerateboththesynthetic
data and the workload [28]. A table of 100,000 records was loaded into the database
cluster. Tokeeptheexperimentasconsistentaspossible,weusedthesamedataacross
the experiment runs. The workload generated was read-focused, with 83% of selects,
15% of updates, and 2% of inserts. Request distribution was set to uniform. Although
thefunctionalityofYCSBallowedrequeststobegeneratedinmorerealisticpatternsand
differentworkloadratios,theuniformrequestdistributionandtheread-focusedworkload
weresufficientenoughforvalidationifrequestscanbebalancedacrossdatabasenodes.
Thedatabasedriverontheclientsidewassettomakethreeattemptstoreconnectevery2s.
Althoughdataspikesareapropertyofabursttowardsastatefulmicroservice,wedid
notconsideritinourexperiment. Sincethedatabaseclusterusedintheexperimentwas
relativelysmallandthedatawerefullyreplicatedacrossthenodes,theincreaseinrequests
onlyforasubsetofdatahadanegligibleimpactontheoverallresults.
ThebaseworkloadgeneratedbyYCSBincluded10,000operationsand160threads
withathroughputtargetoffiveoperationspersecond. Insertquerieswereincludedin
thebaseworkload. Itwasintendedtohavethisworkloadrunningforatleast120s. The
parameters for the base workload were selected to reach the memory utilization of the
Pseudo-Primarydatabaseto600MB.However,inpractice,duetolimitedcontroloverhow
MySQLutilizesthememory,thebaseworkloadmaypeakbetween580MBand620MB.
Asmentionedearlier,thedurationandintensityarethemainfeaturesofaburst. Since
thedurationpropertyisexpectedtobemitigatedbyscalingandsessionbalancing,wewill
evaluatetheproposedmethodunderdifferentintensities.
Theburstworkloadstarted10safterthebaseworkload. Anewclientoffivethreads
wasaddedevery0.25or0.5s,withtargetoperationspersecondof15,aimedatcompleting
2500operations. Eachclientwasintendedtorunforaround33s. Intotal,30clientswith

Electronics2025,14,2752 12of19
150burstthreadswerestarted.Withanewclientaddedevery0.25s,thepeakof150threads
isreachedin,consideringtheoverheadofcodeexecution,approximately7.5s. Withanew
clientaddedevery0.5s,thepeakisreachedatroughly15s. Asforthetotalnumberof
requests,2500operationsforover30clientthreadswillamounttoaround75,000requests.
TheintensityoftheburstisillustratedinFigure5. Withtheaforementionedparametersof
operationspersecond,threadandtargetoperationparametersweresufficienttogenerate
aburstthatpeaksthememoryutilizationataround800MB.
150
120
90
60
30
0
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031323334353637383940
stseuqer
lellarap
fo
rebmuN
Time to burst peak: 15s Time to burst peak: 7.5s
Time into burst (s)
Figure5.Intensityofgeneratedburstworkloads.
Onceworkloadsstart,theorchestratormonitorstheclusterasdescribedpreviously,
initiatingclientconnectiontransferbetweenappropriatenodesatappropriatememory
utilizationlevels. Memoryutilizationonthepodsismonitored. Tosimulatesuccessful
scaling, upon reaching 750 MB of memory utilization on either of the two operational
nodes,theexistingconnectionsaregracefullytransferredtothethirdnode.
Theclientsessionsarehandledinthreedifferentways:
1. No action taken due to the out-of-box functionality of the MySQL Galera Cluster
andProxySQL
2. Redirectingallnewsessionstothesecondnode
3. Balancingallsessionsbetweentwonodes
Tosummarize,wewillevaluateourmethodwiththeparametersshowninTable2.
Table2.Parametersoftheexperiment.
WorkloadTypeDistribution,%
BurstHandlingType TimetoBurstPeak(s)
Reads Updates Inserts
7.5
Noaction
15
7.5
83 15 2 Redirect
15
7.5
Balance
7.5
The YCSB collects quite an extensive list of statistics for each experiment run. We
selectedandaggregatedthestatisticsnecessarytomeasureavailability: thenumberoftotal
operationsandthenumberoffailedoperations.

Electronics2025,14,2752
13of19
Thetotalnumberofrequestsissuedagainstthedatabasehasaconsistentpattern;for
example,theaverageforreadrequestsis85,976. However,thereisaslightvariationineach
experiment;thetotalnumberofrequestsdeviatesfromtheaverageacrossallexperiments
by 2%. We did not consider this deviation to make an impact on the end results as we
measuredthefailureratepercentage.
|             | = numberof | failedrequests    |      |     |
| ----------- | ---------- | ----------------- | ---- | --- |
| failurerate |            |                   | ∗100 | (1) |
|             | total      | numberof requests |      |     |
Werantheexperimentfivetimeswitheachparametersettocomparetheerrorratio
andtimeunderburst.
6. ResultsandDiscussion
Thefirstthingwenoticedwhenanalyzingtheresultsoftheexperimentisthat,despite
theoverallpattern,thedeviationisquitesignificant. Thus,medianvaluesareimportant
aswell. Theresultsshowanon-negligibledeviation,although,onaverage,thereisanim-
provementinhandlingaburstconditioniftheproposedmethodisused. Eventhough
theworkloadissyntheticandquitesimple, withoutcomplexcalculations, thememory
utilization pattern lacks consistency. We were unable to control the inner workings of
theXtraDBengine,whichisareplacementforMySQLInnoDB.Therefore,insomeofthe
experimentalruns,theproposedmethoddidnotperformasexpected. Ontheotherhand,
insomeexperimentalruns,theclustercrashedalmostimmediatelyifnoactionwastaken.
Asexpected,theproposedmethodofwrite-scalingforburstprotectionhadanimpact
onavailabilityintermsofsuccessfulrequestsandtimecomparedtousingjustasinglenode
forwriterequests. Tobeginwith,themeanfailureratepercentage,ifnoactiontobalance
theworkloadwastaken,rangedfrom0.78to1.4percent;ifnewsessionswereredirectedto
anothernode,itrangedfrom0.35to1.09percent,dependingonburstintensity(Figure6).
However,theproposedmethodallowed,forcertainburstintensities,areductioninthe
failureratepercentagetozero,andthemeanratereachedamere0.04percent.
14
 Mean ± 0.5 SD
 Mean
 Median
12
 Outliers
10
% ,etaR eruliaF llarevO
8
6
4
2.52
| 2   |     |     | 1.80 |     |
| --- | --- | --- | ---- | --- |
1.04
|           | 0.52     |                   | 1.15 1.09 |         |
| --------- | -------- | ----------------- | --------- | ------- |
|           | 0.78     | 0.09              |           | 0.00    |
|           |          | 0.35              | 0.49      |         |
| 0         | 0.52     | 0.04              |           | 0.00    |
|           | 0.19     |                   | -0.33     |         |
|           |          | -0.00             |           | 0.00    |
| No action | Redirect | Balance No action | Redirect  | Balance |
|           | 7.5      |                   | 15        |         |
Figure6.Dependencyofoverallfailurerateonbursthandlingtypeandburstintensity.
Forreadrequests(Figure7),theproposedmethodreducedtheimpactofburstonthe
failureratesignificantly. Ifnoactionwastakenoronlytheburstworkloadwasredirected,

Electronics2025,14,2752 14of19
themeanfailureratewasbetween0.33and0.61percent. Ifsessionswerebalanced,the
failureratedroppedto0.04percent.
2
1
0.73
0.61 0.66 0.62
0.50 0.45 0.49
0.38
0.33
0.25 0.27
0.09
0.00
0.05 0.05
0 0.00
0.00
0.00
No action Redirect Balance No action Redirect Balance
7.5 15
%
,etaR
eruliaF
daeR
Mean ± 0.5 SD
Mean
Median
Outliers
Figure7.Dependencyofreadfailurerateonbursthandlingtypeandburstintensity.
Aswithreadrequests,theproposedmethodallowedforareductionintheimpactof
burstonthefailurerateofupdatesaswell(Figure8).Ifnoactionwastakenoronlytheburst
workloadwasredirected,themeanfailureratewouldbebetween0.17and2.36percent.
Thehighestupdateofthemeanfailureratewasforredirectedupdaterequestsunderlower
intensity. However,thestandarddeviationwasquitesignificantduetoonlyoneoutlier. If
sessionswerebalanced,thefailureratewouldbereducedto0.01percent.
14
12
10
8
6
4.92
4 3.90
2.39 2.36
2
1.50
0.89 0.21 0.03 0. 1 6 . 0 05 0.00
0 0. 0 1 . 4 17 -0 0 .0 .0 0 2 -0.20 0. 0 0 . 0 00
No action Redirect Balance No action Redirect Balance
7.5 15
%
,etaR
eruliaF
etadpU
Mean ± 0.5 SD
Mean
Median
Outliers
Figure8.Dependencyofupdatefailurerateonbursthandlingtypeandburstintensity.
Thefailurerateofrequestsfordatainsertion(Figure9)wasreducedbytheproposed
method. Compared to a range of 0.33 to 2.77 percent of failed requests, the balanced

Electronics2025,14,2752
15of19
sessionsallowedthefailureratetoreduceto0.61percent. Acoupleofoutliersskewedthe
resultsaswell,butthetrendremainedthesame.
8
 Mean ± 0.5 SD
 Mean
 Median
 Outliers
6
% ,etaR eruliaF tresnI
4
3.55
|     |     |      |     | 2.77 | 2.76 |     |
| --- | --- | ---- | --- | ---- | ---- | --- |
|     |     | 2    |     | 1.99 |      |     |
|     |     | 1.10 |     |      | 1.34 |     |
0.96
0.45
0.81
|     |     |           | 0.33 0.13                  |     |                  | 0.00 |
| --- | --- | --------- | -------------------------- | --- | ---------------- | ---- |
|     |     | 0         | 0.21 0.06                  |     | -0.08            | 0.00 |
|     |     |           | -0.01                      |     |                  | 0.00 |
|     |     | No action | Redirect Balance No action |     | Redirect Balance |      |
|     |     |           | 7.5                        |     | 15               |      |
Figure9.Dependencyofinsertfailurerateonbursthandlingtypeandburstintensity.
Tosummarize,sessionbalancingsignificantlyreducestheamountoffailurecompared
to taking no action or redirecting client sessions. As seen in Table 3, the failure rate
decreasedbyatleast81.82%. Presumably,thelowerloadonadatabasenodeallowedthe
numberoffailedrequeststobeminimizedwhenperformingagracefulconnectiontransfer
toothernodesinthecluster. Thisfindingconfirmstheresultsofourearlierresearch.
Table3.Summaryoffailurerate.
ComparativeDecreaseinFailure
TimetoBurst AverageFailureRatebyBurstHandlingType
RateUsingBalancing(%)
Workload
Peak(s)
|         | NoAction | Redirect | Balance | NoAction |     | Redirect |
| ------- | -------- | -------- | ------- | -------- | --- | -------- |
| Reads   | 0.61     | 0.45     | 0.05    | 91.80    |     | 88.89    |
| Updates | 2.39     | 0.17     | 0.02    | 99.16    |     | 88.24    |
7.5
| Inserts | 0.96 | 0.33 | 0.06 | 93.75 |     | 81.82 |
| ------- | ---- | ---- | ---- | ----- | --- | ----- |
| All     | 0.78 | 0.35 | 0.04 | 94.87 |     | 88.57 |
| Reads   | 0.38 | 0.33 | 0    | 100   |     | 100   |
| Updates | 1.05 | 2.36 | 0    | 100   |     | 100   |
15
| Inserts | 2.77 | 1.34 | 0   | 100 |     | 100 |
| ------- | ---- | ---- | --- | --- | --- | --- |
| All     | 1.15 | 1.09 | 0   | 100 |     | 100 |
The time needed for any of the nodes to reach 750 MB in memory utilization was
improved alongside the proposed method (Figure 10). The time under burst increased
to42.4and40.8sunderburstconditionscomparedto23and25sifnoactionwastaken.
Redirectingburstsessionsonlyalsoresultedinanincreasedtimeunderburstcompared
totakingnoaction. However,theincreaseintimeunderburstathigherloadintensities
whenusingbalancingcomparedtoredirectingwasinsignificant. Whileredirectedsessions
allowed the cluster to operate under burst for 42.2 s on average, when sessions were
balanced,theaveragetimeunderburstwas40.8s. Judgingbytheoutliers,thetimeunder
burstmayvaryforeachoftheapproaches.

Electronics2025,14,2752 16of19
90
80
70
60
54.54
52.54
50
47.19
42.40 42.40
40 40.80
36.77 37.61 38.75
35.46
30 29.06 30.26
27.60
25.25
23.00
20
16.45
15.04
10
9.23
0
No action Redirect Balance No action Redirect Balance
7.5 15
)s(
tsruB
rednU
emiT
Mean ± 0.5 SD
Mean
Median
Outliers
Figure10.Dependencyoftimeunderburst-on-bursthandlingtypesandburstintensity.
Despitetheoutliers,thereisstillapositivetrendfortimeunderburstchangeswhen
balancingisused(Table4).Thecombinationoflowerfailureratepercentagesandincreased
orslightlydiminishedtimesunderburst,dependingonthemethodscompared,showed
thatsessionbalancingisaviableapproachtoincreasestatefulserviceavailabilityunder
burstconditions.
Table4.Summaryoftimeunderburst.
ComparativeIncreaseinTimeUnder
AverageTimeUnderBurst
TimetoBurst BurstwhenUsingBalancing(%)
Peak(s)
NoAction Redirect Balance NoAction Redirect
7.5 23 42.2 40.8 177.39 96.68
15 25.25 27.6 42.4 167.92 153.62
Onethingincommonbetweenalltypesofworkloadsisthenumberofoutliers. In
somecases,theoutliersshowasignificantdeviationfrommeanvaluesandtheoveralltrend,
which,despitetheoutliers,ispersistentacrosstheexperiments. AsMySQLmemoryusage
dependsonmanyfactors, incertaincases, itmayvaryfromthebaseline. Forexample,
if a new set of data or query plans are added to the cache. The disadvantages of the
proposedmethodstemfromtheuseofaMulti-Primaryrelationaldatabasemanagement
system. Itexhibitsdiminishedperformanceduetoadditionalcomplexityandtheincreased
communicationslatencycomparedtoSingle-Primaryreplicationconfigurations. Unlikethe
Single-Primaryreplicationsetup,latencyisfurtherincreasedbyburstworkloads. Conflict
resolutionaddsanadditionaldegreeoflatencyinaMulti-Primaryreplicationsetupwhen
underpeakloads. ThisispartiallymitigatedbysettinguponenodedesignatedasPseudo-
Primary. Thisapproachwouldreducethenecessityforconflictresolution,asonlyasingle
databasenodewouldberesponsibleforhandlingthewriteoperations.AsseeninFigure11,
average latency is increased when workloads are balanced between two nodes. The
additionallatencyisintroducedduetotheincreasedvolumeofbi-directionalreplication
asmultiplenodesbecomeprocessingwritesandalsoattheendwhenclientconnections
aretransferredtothethirdnode. Eventhoughthelatencyishighercomparedtowhenno

Electronics2025,14,2752 17of19
actionistaken,itonlyincreaseswhenclientsessionsarebalanced;thus,theSLOsrelated
toastatefulmicroservicelatencyaredegradedforalimiteddurationoftime.
Figure11.Dependencyofaveragelatency(µs)onbursthandlingtypeandburstintensity.
However,intermsofhandlingaburst,theproposedmethodusingtheMulti-Primary
databaseoffersseveralbenefits. Tobeginwith,astatefulmicroserviceoperatorcanhandle
a burst independently with no changes needed on the client side. It is a predictable
as well as transparent rule-based approach, and the reasons for these actions taken are
clearandunderstandable. Althoughtobeunbiased,thereisstilluncertaintyastohow
MySQL,oranyotherRDBMSforthatmatter,wouldoperateandusememoryunderpeak
workloadconditions. Finally,theproposedmethodwasproventoworkusingopen-source
components,andtherewereothersoftwarecombinationsthatwerelikelytofunctionin
thesameoranevenbettermannerasanimplementationoftheproposedmethod.
Thereareacoupleofavenuesforfurtherresearch. Tobeginwith,thereareanumber
ofotherdatabasemanagementsystemsthatsupportMulti-Primaryreplication,forexam-
ple,PostgreSQLwithBi-DirectionalReplicationextension,CockroachDB,CouchDB,and
Cassandra. PostgreSQLisoneofthe“classic”RDBMSs;thus,itislikelythattheproposed
methodcouldachieveresultssimilartotheMySQLGaleraCluster. CockroachDBisamore
modernRDBMS,builtasadistributeddatabasewithamodernconsensusprotocoland
automatic sharding. Although a more modern tool, CockroachDB still relies on third-
partyproxysolutionstobalancetheworkload,whichallowstheproposedmethodtobe
employedtohandlebursts. CassandraandCouchDB,twoNoSQLalternativesenabling
Multi-Primaryreplications,arebuiltwithdatadistributioninmind. However,promoting
a Cassandra node to a writer requires additional reconfiguration, while the CouchDB
nodemustbeconfiguredinadvancetoacceptwrites. Thiswouldlikelycausedifficulties
withCassandraandCouchDBincasetheproposedmethodistobeusedtohandlebursts.
Aninquirycouldbemadeintotheefficiencyoftheproposedmethodusingadatabase
managementsystemotherthanMySQLGaleraCluster.
Additionally, the integration of the proposed rule-based method with ML-based
techniquescanenhancethewayburstworkloadsarehandledwhileoptimizingresource
usage. Itmayactasafailsafemeasuregiventhatworkloadpredictionmaybeimprecise
andastatefulmicroserviceisnotproperlyadaptedtotheactualdemand. Tobeginwith,

Electronics2025,14,2752 18of19
theproposedrule-basedmethodcanextendtheoperationaltimeofastatefulmicroservice
ifverticalscalingisnotinitiatedontime. Theextratimeunderburstwould,hopefully,be
sufficientforthestatefulmicroservicetoscale. Secondly,thebalancingoftheworkload
maybeinitiatedwhilethemicroservicescalesvertically.
7. Conclusions
Theproposedmethodofusingwrite-scalingandloadbalancingtoprotectastateful
microserviceunderanoverwhelmingburstworkloadallowedustoincreaseitsavailability.
Theadditionaltimeunderburst,althoughmodest,incertaincasescouldbesufficientto
allowverticalscalingtocompleteandthuswouldenablethestatefulmicroservicetohandle
theextraworkload.
Our experiments have shown that stateful microservices can operate under burst
for a longer duration. Burst intensity does make an impact on availability. If the burst
intensityislowenough, theloadcanbebalancedandwritescanbescaledtothepoint
wherethestatefulmicroservicescalesintimetomatchtheincreaseddemand. Ontheother
hand, if the burst is sufficiently intensive, a stateful microservice crashes regardless of
whetherornottheproposedmethodisused. However,thefailureratepercentageisstill
lower,andtheserviceisunavailableforshorteramountsoftime. Theproposedmethod
allowedastatefulmicroservicetooperateunderaburstforalmosttwiceaslongcompared
tostandardfunctionality. Althoughthereisaresponselatencyincreaseiftheproposed
methodisused,thestatefulmicroserviceisaffectedbyitonlyforalimitedamountoftime.
Inenvironmentswhereresourcesareconstrained,astatefulmicroservicecanbesized
toprocessthepresumedstandardworkloadandscaleduptomeettheincreaseddemand.
Inaddition,theproposedmethodcanbeusedasafailsafeifemployedworkloadprediction
algorithmsareimpreciseinworkloadforecast.
Inthispaper,wehaveshownthatstatefulmicroservicescanoperateunderasudden
andsignificantworkload,whichwouldotherwisepotentiallycausethesystemtocrashfor
longerdurations.
AuthorContributions: Methodology,D.M.;Software,K.P.;Investigation,K.P.;Writing—original
draft,K.P.;Writing—reviewandediting,D.M.;Supervision,D.M.Allauthorshavereadandagreed
tothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Dataarecontainedwithinthearticle.
Acknowledgments:TheauthorswouldliketoexpresstheirsinceregratitudetoJonathanStephen
Salterforhisinvaluableassistanceandinsightfulsuggestionsthatgreatlyimprovedthequalityof
thismanuscript.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Manouvrier,M.;Pautasso,C.;Rukoz,M.MicroserviceDisasterCrashRecovery: AWeakGlobalReferentialIntegrityManagement;
SpringerInternationalPublishing:Cham,Switzerland,2020;Volume12138.[CrossRef]
2. Truyen, E.; Van Landuyt, D.; Lagaisse, B.; Joosen, W. Performance Overhead of Container Orchestration Frameworks for
ManagementofMulti-TenantDatabaseDeployments. InProceedingsofthe34thACMSymposiumonAppliedComputing,
Limassol,Cyprus,8–12April2019;pp.156–159.
3. Pardon,G.;Pautasso,C.;Zimmermann,O.ConsistentDisasterRecoveryforMicroservices: TheBACTheorem. IEEECloud
Comput.2018,5,49–59.[CrossRef]
4. Pereira,P.A.;Bruce,M.MicroservicesinAction;Manning:ShelterIsland,NY,USA,2019.
5. Newman,S.BuildingMicroservices:DesigningFine-GrainedSystems,1sted.;O’ReillyMedia:Sebastopol,CA,USA,2015.

Electronics2025,14,2752 19of19
6. Kubernetes. RunaReplicatedStatefulApplication. Kubernetes.io. Availableonline: https://kubernetes.io/docs/tasks/run-
application/run-replicated-stateful-application/(accessedon6March2021).
7. Kannaiah, G.M.KubernetesAnti-Patterns: OvercomeCommonPitfallstoAchieveOptimalDeploymentsandaFlawlessKubernetes
Ecosystem,1sted.;PacktPublishing:Birmingham,UK,2024.
8. Shen,H.;Chen,L.ResourceDemandMisalignment:AnImportantFactortoConsiderforReducingResourceOver-Provisioning
inCloudDatacenters.IEEE/ACMTrans.Netw.2018,26,1207–1221.[CrossRef]
9. Rubak,A.;Taheri,J.MachineLearningforPredictiveResourceScalingofMicroservicesonKubernetesPlatforms.InProceedingsof
the16thIEEE/ACMInternationalConferenceonUtilityandCloudComputing,UCC2023,Orlando,FL,USA,4–7December2023;
AssociationforComputingMachinery,Inc.:NewYork,NY,USA,2023.[CrossRef]
10. Dang-Quang,N.M.;Yoo,M.Deeplearning-basedautoscalingusingbidirectionallongshort-termmemoryforKubernetes.Appl.
Sci.2021,11,3835.[CrossRef]
11. Lassnig,M.;Fahringer,T.;Garonne,V.;Molfetas,A.;Branco,M.Identification,modellingandpredictionofnon-periodicburstsin
workloads.InProceedingsofthe10thIEEE/ACMInternationalConferenceonCluster,Cloud,andGridComputing,Melbourne,
Australia,17–20May2010;pp.485–494.[CrossRef]
12. Deshpande,U.Caravel: BurstTolerantSchedulingforContainerizedStatefulApplications. InProceedingsofthe39thIEEE
InternationalConferenceonDistributedComputingSystems,Dallas,TX,USA,1–4July2019;pp.1432–1442.[CrossRef]
13. Campbell,L.;Majors,C.DatabaseReliabilityEngineering,1sted.;O’ReillyMedia:Sebastopol,CA,USA,2017.
14. Pakrijauskas,K.;Mažeika,D.AMethodofTransparentGracefulFailoverinLowLatencyStatefulMicroservices.Electronics2022,
11,3936.[CrossRef]
15. Ali-Eldin,A.;Seleznjev,O.;Sjostedt-deLuna,S.;Tordsson,J.;Elmroth,E.MeasuringCloudWorkloadBurstiness.InProceedings
ofthe7thIEEE/ACMInternationalConferenceonUtilityandCloudComputing,London,UK,8–11December2014; IEEE:
Piscataway,NJ,USA,2024;pp.566–572.[CrossRef]
16. Bodik,P.;Patterson,D.A.;Jordan,M.I.;Franklin,M.J.;Fox,A.Characterizing,modeling,andgeneratingworkloadspikesfor
statefulservices.InProceedingsofthe1stACMSymposiumonCloudComputing,Indianapolis,IN,USA,10–11June2010;ACM
DigitalLibrary:NewYork,NY,USA,2010;pp.241–252.
17. Woodruff,J.;Moore,A.W.;Zilberman,N.MeasuringBurstinessinDataCenterApplications.InProceedingsofthe2019Workshop
onBufferSizing,NewYork,NY,USA,9December2019;ACM:NewYork,NY,USA,2019;pp.1–6.[CrossRef]
18. Baarzi,A.F.;Kesidis,G.SHOWAR:Right-sizingandefficientschedulingofmicroservices. InProceedingsofthe2021ACM
Symposium on Cloud Computing (SoCC 2021), Seattle, WA, USA, 1–4 November 2021; ACM: New York, NY, USA, 2021;
pp.427–441.[CrossRef]
19. Iqbal,W.;Erradi,A.;Mahmood,A.Dynamicworkloadpatternspredictionforproactiveauto-scalingofwebapplications.J.Netw.
Comput.Appl.2018,124,94–107.[CrossRef]
20. Xie,S.;Wang,J.;Li,B.;Zhang,Z.;Li,D.;Hung,P.C.K.PBScaler:ABottleneck-AwareAutoscalingFrameworkforMicroservice-
BasedApplications.IEEETrans.Serv.Comput.2024,17,604–616.[CrossRef]
21. Kubernetes.AssignMemoryResourcestoContainersandPods.Availableonline:https://kubernetes.io/docs/tasks/configure-
pod-container/assign-memory-resource/(accessedon7May2025).
22. Oracle.HowMySQLUsesMemory.MySQL.com.Availableonline:https://dev.mysql.com/doc/refman/8.0/en/memory-use.
html(accessedon7May2025).
23. PerconaLLC.PerconaXtraDBClusterDocumentation;PerconaLLC.:Durham,NC,USA,2020.
24. CodershipLtd.ReplicationAPI.Availableonline:https://galeracluster.com/library/documentation/architecture.html#wsrep-
api(accessedon7May2025).
25. Wang,Z.Autothrottle:APracticalBi-LevelApproachtoResourceManagementforSLO-TargetedMicroservices.Availableonline:
https://www.usenix.org/conference/nsdi24/presentation/wang-zibo(accessedon12May2025).
26. GitHub.BurstToleranceforStatefulMicroservices.Availableonline:https://github.com/kespak/burst-tolerance-for-stateful-
microservices(accessedon1July2025).
27. Hauer, T.; Hoffman, P.; Lunney, J.; Ardelean, D.; Diwan, A. Meaningful Availability. In Proceedings of the 17th USENIX
Symposium on Networked Systems Design and Implementation (NSDI 20), Santa Clara, CA, USA, 25–27 February 2020;
pp.545–557.Availableonline:https://www.usenix.org/conference/nsdi20/presentation/hauer(accessedon24May2025).
28. Cooper,B.F.;Silberstein,A.;Tam,E.;Ramakrishnan,R.;Sears,R.BenchmarkingcloudservingsystemswithYCSB.InProceedings
ofthe1stACMSymposiumonCloudComputing,inSoCC’10,Indianapolis,IN,USA,10–11June2010;AssociationforComputing
Machinery:NewYork,NY,USA,2010;pp.143–154.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.