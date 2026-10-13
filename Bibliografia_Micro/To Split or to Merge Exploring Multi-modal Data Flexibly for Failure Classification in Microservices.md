PDF Download
3755881.3755891.pdf
18 March 2026
Total Citations: 0
. Total Downloads: 235
.
Latest updates: hps://dl.acm.org/doi/10.1145/3755881.3755891 .
.
Published: 27 October 2025
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
To Split or to Merge? Exploring Multi-modal Data Flexibly for Failure
.
.
Classification in Microservices Internetware 2025: the 16th International
Conference on Internetware
June 20 - 22, 2025
XIUHONG TAN, Changsha University of Science and Technology, Changsha, Hunan, China Trondheim, Norway
.
. .
YUAN YUAN, National University of Defense Technology China, Changsha, Hunan, China Conference Sponsors:
SIGSOFT
.
TONGQING ZHOU, National University of Defense Technology China, Changsha, Hunan,
China
.
SHIMING HE, Changsha University of Science and Technology, Changsha, Hunan, China
.
YUQI LI
.
JIAN ZHANG
.
.
.
Open Access Support provided by:
.
National University of Defense Technology China
.
Changsha University of Science and Technology
.
Internetware '25: Proceedings of the 16th International Conference on Internetware (June 2025)
hps://doi.org/10.1145/3755881.3755891
ISBN: 9798400719264
.

To Split or to Merge? Exploring Multi-modal Data Flexibly for
Failure Classification in Microservices
XiuhongTan∗ YuanYuan∗ TongqingZhou†
ChangshaUniversityofScienceand NationalUniversityofDefense NationalUniversityofDefense
Technology Technology Technology
Changsha,China Changsha,China Changsha,China
tanxh@stu.csust.edu.cn yuanyuan@nudt.edu.cn zhoutongqing@nudt.edu.cn
ShimingHe YuqiLi JianZhang
ChangshaUniversityofScienceand NationalSupercomputerCenterin NationalSupercomputerCenterin
Technology Tianjin Tianjin
Changsha,China Tianjin,China Tianjin,China
smhe_cs@csust.edu.cn liyq@nscc-tj.cn zhangjian@nscc-tj.cn
Abstract ACMReferenceFormat:
Classifyingfailuresforautomateddiagnosisiscriticalformaintain- XiuhongTan,YuanYuan,TongqingZhou,ShimingHe,YuqiLi,andJian
Zhang.2025.ToSplitortoMerge?ExploringMulti-modalDataFlexiblyfor
ingthereliabilityofever-increasingmicroservicesystems.Existing
FailureClassificationinMicroservices.Inthe16thInternationalConference
failureclassificationmethodsfocussolelyonanalyzingonespecific
onInternetware(Internetware2025),June20–22,2025,Trondheim,Norway.
datamodality(e.g.,metrics)orfeedingmulti-modaldata(e.g.,logs
ACM,NewYork,NY,USA,10pages.https://doi.org/10.1145/3755881.3755891
andtraces)inaone-fit-allmodel.Thiswouldleadtobiasedinference
asdifferentmodalitieshavedifferentiatedproportionsandmanifest
1 Introduction
distinctsensitivitiesandpatternsinfailuresofvariedruntimecon-
texts.Thisworkproposesanovelfailureclassificationframework Withthepopularityofcloud-nativeapplications,microservicear-
formicroservices,namedAgileMFC,withthebasicideaofflexibly chitecturehasbeenwidelyadoptedtodecoupleeverlargersystems
learningandassemblingtheexpertiseofmulti-modalmonitoring intoindependentunitsforagiledevelopment[5,19].Amicroservice
data.Theflexibilityisattainedwiththesplit-and-mergedesignof systemistypicallypresentedasalarge-scaledistributedarchitec-
datarepresentation,whereitassignseachmodalityadifferentgate turecomprisinglooselycoupledinstances(e.g.,physicalmachines
thatroutesittodedicatedexpertnetworksandusesasharinggate orcontainers).However,asthenumberofinstancesincreasesto
tofacilitatecontrollableknowledgeinteractionamongmodalities. catertogrowinguserdemand,theinvocationrelationshipamong
Meanwhile,AgileMFCtrainstherepresentationnetworksanda instances becomes increasingly complex. This would aggravate
classifierinconsecutivestageswithconcatenatedandweightedfea- thepropagationoffailuresanddecreasethestabilityofthewhole
turefusion,thusdecouplingtask-agnosticfeatureextractionwith system,causingterribleuserexperiencesoreveneconomicdam-
task-specificclassification.Experimentsonthreedatasetsshowthat age[13].Hence,effectivelydiagnosingfailuresiscriticalfortrou-
AgileMFCoutperformsfourbaselinesw.r.t.,precision,recall,and bleshootingandmaintainingashortMeanTimetoRepair(MTTR).
F1-scoreonfailureclassification. In the failure diagnosis spectrum, failure classification (a.k.a,
failuretriage)isusedtoidentifythetypeofpotentialproblemsfor
CCSConcepts dedicateddownstreammitigation[17],thusbeingconsideredan
•Computersystemsorganization→Reliability;•Software essentialstep.Forexample,byidentifyingafailuretypeofintensive
and its engineering → Maintaining software; • Computing workload(e.g.,I/Osaturation),theoperatorcouldcomplementa
methodologies→Machinelearning. load balancer for corresponding instances. Technically, failures
canbeclassifiedbyparsingandanalyzingthemonitoringdataof
Keywords microservice systems, which mainly includes the chronological
recordsofsystemeventsandtransactions(i.e.,logs),quantitative
Microservicesystems,failureclassification,multi-modaldataanal-
indicatorsofsystemperformance(i.e.,metrics),andtheflowof
ysis
requeststhroughmicroservices(i.e.,traces).Thesemodalitiesof
dataareusuallyrepresentedasevents1indifferentstructuresand
∗Bothauthorscontributeequallytothisresearch.
forms,e.g.,textsforlogs,timeseriesformetrics,andtuplesfor
†Correspondingauthor.
traces,asshowninTable.1.
Existingfailureclassificationmethodsrelyoneitherisolated
single-modalanalysis(i.e.,split)orone-fit-allmulti-modalanalysis
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. (i.e.,merge),fallingintotwoextremes.Ontheonehand,single-
Internetware2025,Trondheim,Norway modalclassification[1,11,23],basedonparsingtexts,anomaly
©2025Copyrightheldbytheowner/author(s).
ACMISBN979-8-4007-1926-4/25/06
https://doi.org/10.1145/3755881.3755891 1Weusethetermeventforalog/metric/tracerecordduringfailure.
568

Internetware2025,June20–22,2025,Trondheim,Norway Tanetal.
detection,andcorrelationanalysisoflogs,metrics,andtracesre- waymayforcerepresentationsfordifferentmodalitiestosharethe
spectively,isanintuitivechoiceasdifferentmodalitiesarecollected sameclassificationloss,gainedfromthetrainingsamples,during
independently.However,relyingonasingletypeofdatamayfail optimization,implicitlydeprivingtheirsensitivities.
tocapturethefullcharacteristicsoffailures,leadingtoincomplete ThisworkproposesAgileMFC,anovelframeworkthatleverages
analysis.Furthermore,heterogeneousmicroservicesystemsmean thestrengthsofeachmodalityofmonitoringdataformicroservice
thatfailurescanmanifestinavarietyofways,sosingle-modaldata failureclassification.Specifically,forchallenge1,AgileMFCuses
maynotadequatelyreflectthisdiversity.Ontheotherhand,there aseriesofparallelizedandstructural-adaptivechannels(deepnet-
havebeenattemptstointegratedifferentmodalitiesofmonitoring works)forrepresentinglog,metric,andtraceevents,andregards
datainfailureclassificationrecently[13,24,26].Althoughexisting thesechannelsasmodality-sensitiveexperts.Itthenmergesthese
multi-modalclassificationmethodsovercomesingle-modal’sin- expertstogetherthroughaMulti-gateMixture-of-Experts(MMoE)
completenessdrawbackwithcomplementarydata,thisworknotes architecture,whereeachmodalityismappedtoonemodalitygate
thattheygotoanotherextremebyfittingtherepresentationof thattellsithowmuch(i.e.,weight/attention)itcantrustinthe
differentmodalitiesinonemodel. representationofeachnetwork.Meanwhile,AgileMFCintroduces
Forexample,astheState-of-The-Art(SoTA)designalongthe asharinggateforinteractinggeneralrepresentationknowledge
multi-modalline,diagFusion[24]usesfasttextforembeddingsof amongexperts.Suchaflexiblesplit&mergedesignguarantees
logs,metrics,andtraces,andintroducesGraphNeuralNetwork thatthelearningofdifferentexpertsisagnostictotheeventcom-
(GNN)forfeaturerepresentationtowardsclassification.Represent- ponentsduringmicroservicefailuresandavoidstheoverwhelming
ing each modality in the same form would facilitate a biased effects(inexistingmulti-modalmethods)intherepresentationsof
modelgiventhatdifferentmodalitieshavedistinctsensitivi- somemodalitiestoothers.Astochallenge2,AgileMFCadoptsa
tiesanddifferentnumberofeventsonaspecificfailure.As two-stagetrainingstrategytodecouplerepresentationandclassi-
intheexampleofTable.1,empirically,anoperatorwouldidentify ficationlearning.First,theexpert-outputfeaturesofmulti-modal
thefailuretype“Accessdenied”bytheloginformationat17:38. eventsarefusedviaconcatenationandlinearlymappedtothela-
Forcingtherepresentationoflog“accesspermissionexception”to belvectorsizeforcalculatingrepresentationlossesandtuningthe
bealignedwithmetric“CPU”andtrace“s1→s2”woulddegradeits representationnetworks.Second,aclassifiernetworkisconnected
indicativecapability.Meanwhile,diagFusion’suseofGNNrequires tothelearnedexpertsandtunedwithaclassificationloss,during
thepresentationofeventsfromallmicroserviceinstanceswhen whichstagetheexpertnetworksarefrozen.
afailureoccurs,whichwouldfailinpracticebecausenoevents TheflexibledesignofAgileMFCendowsitwithSoTAperfor-
wouldbetriggeredforthosenormalinstances.Hence,thisworkis mance in failure classification2, which is validated on three
motivatedtodesignaflexibleassemblingofdifferentmodal- datasets(onefromareal-worldmicroservicesystemandtwofrom
ity knowledge for unbiased classification of microservice open-sourceplatforms).Themajorcontributionsareasfollows:
failure.
• TheproposedAgileMFCframeworkadaptsMMoEwithboth
Table1:Anexampleofthemulti-modalevents/dataduring modality-awareandsharinggatingmechanismsforunbi-
afailure.𝑅𝑇 𝑆
1
→𝑆
2
denotestheresponsetimewhen𝑆 1calls𝑆 2, asedeventsfeatureextractioninmicroservicefailure,pre-
“–”meansnoanomalyisfoundordataislostinthatmodality, sentingaflexibletrade-offbetweensplittingandmerging
and“↑”and“↓”indicatethevalueisoutofthestandardrange. datamodalitiesinrepresentation.
• This work adopts a two-stage training design for the
consecutive-yet-decoupledlearningoftherepresentation
Time Log Metric Trace
networksandtheclassifierinAgileMFC.Concatenatedand
17:12 - Mem↑ 𝑅𝑇 𝑆 →𝑆 =1.8𝑠 weightedfusionstrategiesareadoptedfordifferenttraining
1 2
17:31 - CPU↓ - stages,respectively.
INFO|UserwithID** • TheeffectivenessandperformanceofAgileMFCareevalu-
17:32
hasbeen...
- 𝑅𝑇 𝑆
2
→𝑆
3
=1.9𝑠
atedbycomparingwithfourfailureclassificationbaselines
ERROR|...access onthreedatasets.ExperimentalresultsshowthatAgileMFC
17:38 - -
permissionexception... achievestheSoTAperformanceonclassificationprecision,
17:44 - Net↓ 𝑅𝑇 𝑆 →𝑆 =3.5𝑠 recall,andF1-scorewithanaverage(w.r.t.,threedatasets)
1 4
improvementof12.4%,9.1%,and11.8%overthe2nd-best
baseline.
For this goal, we have to handle two aspects of challenges:
1)Howtotakebalancebetweensplitandmerge? Intermsofmi-
2 RelatedWork
croservicemonitoringdatarepresentationfordifferentmodalities,
split/independencymaintainsmodalitysensitivitybutisincomplete Failuretypeclassificationisacrucialtaskoffailurediagnosisin
indepictingthefailure,whilemergefacilitatescomprehensiveun- large-scalemicroservicesystems.Manyresearchpapersfocuson
derstandingatthecostofweakeningmodalities’differentialinflu- thisdomain[1,13,16,22–24],whichcanbecategorizedintosingle-
ences.Aflexibledesignisexpectedtoretaintheadvantagesofboth. modal-basedandmulti-modal-basedmethods.
2)Howtoaccommodaterepresentationandclassification?Represen-
tationforfeatureextractionistask-agnosticwhileclassification,as
itssubsequentstep,isnot.Learningthemtogetherinanend-to-end 2Codeisavailableathttps://github.com/aiopsUser1012/AgileMFC
569

ToSplitortoMerge?ExploringMulti-modalDataFlexiblyforFailureClassificationinMicroservices Internetware2025,June20–22,2025,Trondheim,Norway
2.1 Single-modal-basedFailureClassification microservicefailuresbasedonsingle-modaldataoftheGeneric
Log-basedfailureclassification:Semi-structuredlogsrecordevent AIOpsAtlasdataset.ThentheypresentDiagFusion,whichencodes
informationduringtheruntimeofasystem.Existingmethodsparse logs,traces,andmetricswithfasttext,representseachinstancewith
andclassifythepotentialfailuresinlogrecordsbyvectorizingand GNN,andfeedstherepresentationstoanMLPforfailureclassifi-
templatinglogsintofeatures.Amongthem,LogCluster[11]parses cation.Althoughmulti-modaldataareinvolved,theirembedding
loginformationintologevents,andgroupsthemusingtheAg- intovectorsishandledbyauniversalmodel,whichimplicitlyen-
glomerativeHierarchicalclusteringtechnique.Itthendetermines forcestherepresentationofmulti-modaldatatofailuresinthesame
thefailuretypeofanincomingeventbasedonthecosinesimilarity featurespace.
betweenitandtheclusters.Cloud19[23]trainsaword2vecmodel
3 Preliminaries
tovectorizelogsandadoptsasupervisedclassifierforfailuretype
classification.Althoughthelogentailssemanticeventsinthesys- Inthissection,wefirstintroducethebackgroundofthemicroser-
tem,therecordingprotocolscannotprovidetheinvocationand vicesystemandsomepreliminariesonfailureclassification.Then
systemcontext,whichmayleadtomissingormisclassification. wedefinetheproblemoffailureclassificationwithmulti-modal
Metric-basedfailureclassification:Metricscarryfine-grainedin- inputs.
formation,especiallyresourceusage,abouttheoperationalstate
ofasystem,soarewidelyusedtomonitorsystemhealthandper- 3.1 MonitoringtheMicroserviceSystem
formance.DBSherlock[22]combinesdomainknowledgeanduser
Amicroservicesystemconsistsofindependentlydeployableser-
feedbackinanalyzinghistoricalmetricsdataandidentifyingproba-
vices,eachresponsibleforaccomplishingaspecifictask.Onemi-
blefailuretypes.BybuildingaKNNmodelforthenormalbehavior
croservicecouldbelaunchedmanytimesandeachoftheserunning
ofmetrics,CloudPD[15]generatessignaturesfordifferentonline
entitiesiscalledaninstance.Theseinstancescommunicatewith
failuretypesbasedonexpertknowledgeanddeterminesthefailure
eachotherusinglightweightprotocols,typicallyHTTPormessage
typeofincomingmetricsbycomparingthemwiththeexistingsig-
queues[9].Sinceeachservicecanbeupdatedorextendedindivid-
natures.Arvalus[14]regardsinstancesubseriesasnodesandtheir
ually,themicroservicearchitectureallowsdeveloperstodevelop,
dependenciesasedges,usesgraphconvolutionalneuralnetworks
test,anddeployfreely(a.k.a.,DEVOps).Inpractice,microservice
(GCNNs)tolearnnodeandedgefeatures,andclassifiesfailures
systemsrefertothreemaintypesofdatatomonitorthehealth
based on the graph representation. However, metrics alone are
status:
susceptibletounexpectedvariations(unstableinnature)andlack
Log:Alogmessageusuallyconsistsoffieldssuchastimestamp,
contextsemantics,whichwouldmisleadfailuretriage.
verbositylevel,andrawinformation[6].Wherein,verbositylev-
Trace-basedfailureclassification:Thetrace-basedmethodsac-
els are usually categorized into INFO, WARN, DEBUG, and ER-
complishfailuretracingandclassificationbyanalyzingthecalling
ROR,indicatingtheseverity.Logtemplateparsingtechnology(e.g.,
ordeploymentdependenciesbetweenmicroserviceinstances.Mi-
Drain[6])andvisualmanagementtoolssuchasELK(Elasticsearch,
croHECL[12]designsspecializeddetectionmodelsfordifferent
Logstash,andKibana)canhelpoperatorstounderstandlogmes-
typesofanomalies(performance,reliability,andtraffic),eachof
sagesmoreefficiently.
whichcorrespondstoaspecificqualityofservicemetricandadiffer-
Metric:Metricsarereal-numbervaluesthatdepictthestatusof
entdirectionofanomalypropagation.MicroHECLthencategorizes
microserviceinstances.Well-knownmetricsincludeCPUusage,
failuretypesbasedontheidentifiedanomalies.Tracesentailthe
memoryconsumption,requestrates,errorrates,etc.Theyarecol-
inter-microservicerelationship,whosefeaturesaremoreeffective
lectedatpredeterminedintervalstoformtimeseries.Whenspecific
inunderstandingcoarse-levelfailureswithexplicitpropagation
metricsdeviatefromtheexpectedcriteria,automatedalertswould
chainsthanthoserootedinoneservice.Hence,merelyreferringto
betriggered.
thetraceswouldleadtoanincompleteunderstandingoffailures.
Trace:Atracetrackstheflowofrequestsamonginstancesofa
microservicesystem.Itcanbeformulatedasatreestructure,with
2.2 Multi-modal-basedFailureClassification instancesasnodesandinvocationsasedges.Givensuchatree,
itiseasytodeterminethelocationofthecurrentrequestinthe
Single-modal-basedmethodsmayomitcertaintypesofinformation
invocationhierarchy,aswellasitsupstreamanddownstreamnodes.
andthusaremorelikelytoincreasetheriskoffailure.Incontrast,
Typically,besidesthecallersandcallees,atracecarriesinformation
combiningmulti-modaldataoffersamorecompleteviewforcheck-
abouttheinvocationtime,requeststatus,latency,statuscodes,etc.
ingthemicroservicesystem,allowingformoreaccuratefailure
classification[27].CloudRCA[26]buildsaKnowledgeInformation
3.2 FailureClassification
HierarchicalBayesianNetwork(KHBN)toidentifyanomaliesin
bothmetricsandlogsandcorrelatethemwithspecificpredefined Decouplingservicesintounitsaggravatesfailurepropagation[2],
failuretypes.Meanwhile,MicroCBR[13]usesmetrics,logs,and in particular for ever-larger microservice systems, where small
tracestobuildaspatio-temporalfailureknowledgegraphandgen- failurescanhaveacascadingeffect,makingdiagnosisandrecovery
eratesfeaturefingerprintsforeachhistoricalfailure.Subsequently, morecritical.
duringtheonlinephase,thefeaturesofnewfailuresarecompared Failureclassificationdenotestheprocessofcategorizingfailures
withthefingerprintsofknownfailuresthroughahierarchicalin- accordingtothetype,severity,orinfluenceonsystemperformance.
ferencemechanismtodeterminetheircategories.Zhangetal.[24] Itisessentiallyusedasanupstreamtaskfordevelopingeffective
providesobservationsforthemodestperformanceofidentifying failurediagnosisandrecoverystrategies.Whenasystemreportsa
570

| Internetware2025,June20–22,2025,Trondheim,Norway |     |     |     |     |     |     |     | Tanetal. |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- |
failure,theoperatorwouldfirstrefertothecontext(manifestedin togainaparameterizedmodelthatpredictsthediscretecategory
| monitoringdata)andthendecidethegeneraldiagnosticdirection |     |     |     |     | ofafailure: |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
fortroubleshootingusingthefailureclassificationmodel.Hence,
|     |     |     |     |     |     | F(𝜃):F[𝑡−𝑤,𝑡] | →𝑦. |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
effectivefailureclassificationiscriticalforefficientdiagnosis.
W.l.o.g.,thisworkstudiesfailuretypeclassification.Large-scale
microservicesystemsmaysufferfrommanydifferenttypesoffail- 4 DesignofAgileMFC
ures,whichcanberoughlyclassifiedashardwarefailures,software ThissectionpresentsAgileMFC’sdesignonevent(monitoringdata)
errors,andnetworkproblems[25].Hardwarefailuresoftenarise pre-processing,featureextraction(representation),andclassifica-
fromresourceschedulingproblems,whereincorrectresourceal- tion.Italsodescribesthetwo-stagetrainingdetails.
| location or | heavy system | loads can make | a service | run low on |     |     |     |     |
| ----------- | ------------ | -------------- | --------- | ---------- | --- | --- | --- | --- |
CPU,memory,ornetworkresources,furthercausingservicein-
4.1 FrameworkOverview
terruptionsorcrashes.Softwareerrorsgenerallyincludesystem
AnoverviewoftheAgileMFCframeworkisshowninFig.2.Af-
bottlenecks,poorlyquerystatements,orcodebugs.Networkprob-
tercapturingafailure,itidentifiesmulti-modaleventsfromraw
lemsinvolveissuessuchaslatencyandconnectionfailuresthatcan
monitoringdataandsubmitsthemtopre-processing,representa-
disruptinter-servicecommunicationandcausecascadingfailures
tion,andclassificationinphases.Duringpre-processing,AgileMFC
inhighlyinterdependentmicroservices.Notethatthefailuretypes
embedseventsintoavectorspace,wherepositionalencodingis
couldbefurtherrefinedaccordingtotheneedsofimplementation
addedtoeachevent’sembeddingtoencodetheirsequentialre-
andtheavailabilitiesoflabels,i.e.,thetypeofhardwarefailure
lationships.Then,theembeddingvectorsofeventsarefedinto
couldberefinedasmisconfiguration,systemcomponentdamage,
|     |     |     |     |     | a modality-aware | representation | network, | which uses multiple |
| --- | --- | --- | --- | --- | ---------------- | -------------- | -------- | ------------------- |
intensiveworkload,resourceexhaustion,andetc.
expertstoextractfeaturesforeacheventandcombinestheiropin-
ionsbasedontheweightestimationofbothasharinggateanda
modality-specificgate.Afterthisphase,eacheventwillhaveone
log event featurevector.Finally,thefusion-basedclassificationnetworkfuses
metric event
trace event theeventfeaturesbasedoneventweightsw.r.t.recordsinhistorical
| R1 722b1e17 |     | R1 mem_usage_pct |     | R1 cpu_core_pct |     |     |     |     |
| ----------- | --- | ---------------- | --- | --------------- | --- | --- | --- | --- |
failuresanddeterminesthefailuretypeofthefusedvectorviaa
|             | R1 W1 |                   | R1 d071a2a6 |       | classifier.                      |                     |                                |                    |
| ----------- | ----- | ----------------- | ----------- | ----- | -------------------------------- | ------------------- | ------------------------------ | ------------------ |
|             |       | Group by modality |             |       | 4.2 MonitoringDataPre-processing |                     |                                |                    |
|             |       |                   |             |       | 4.2.1 EventFormalization.        |                     | AgileMFCobtainsthethreetypesof |                    |
| R1 722b1e17 |       | R1 mem_usage_pct  |             |       |                                  |                     |                                |                    |
|             |       |                   |             | R1 W1 | monitoring                       | data by identifying | events from                    | the raw data using |
| R1 d071a2a6 |       | R1 cpu_core_pct   |             |       |                                  |                     |                                |                    |
anomalydetectionandtemplateparsing,andattachingthemwith
| log events sequence |     | metric events sequence |     | trace events sequence |     |     |     |     |
| ------------------- | --- | ---------------------- | --- | --------------------- | --- | --- | --- | --- |
timestamps.
Figure1:Theprocessofeventsequencegeneration.Theicon LogEventParsing.WeapplytheDrain[6]tool,whichhas
ofeachmodalityrepresentstherawdata,theiconat𝑡 demonstrateditsefficacyinreal-worldscenarios,toextractlog
indi-
catesafailureand𝑤isthelengthoftheobservationwindow. events in the time window of failure. Drain constructs a fixed-
depthparsetreetoseparatestaticanddynamiccomponentsoflog
messages.Forexample,giventhelogmessage“TravelServiceImpl:
[TravelService][GetRouteById]RouteIDuff1a92708982-77af-
3.3 ProblemFormulation
4318-be25-57ccb0ff69ad”,“TravelServiceImpl:[TravelService][Get
Failuresinmicroservicesystemscouldcauseaseriesofeventsgiven RouteById]RouteID******”isthestatictemplate,“uff1a92708982-
thecascadinginvocationcharacteristics.Meanwhile,thesymptom 77af-4318-be25-57ccb0ff69ad”isthedynamicportion.Afterisolat-
eventsandmodalitymayvaryincontextsasmicroservicesare ingthestatictemplatefromthedynamicvariables,wegeneratea
developedandmaintainedindependentlywithhardlyconsistent
uniqueidentifier(i.e.,templateid)foreachlogtemplatebyapplying
runningpatternsandrecordingprotocol.Toavoidbiasedlyrelying
ahashfunctiontothetemplatestring.Thefinallogeventsarestored
onpartialmodalitiesandinstances,thisworkattemptstousemulti- astuples intheform of < timestamp,instance-id,template-id >,
modalmonitoringdatainthefailuresceneforsupervisedlearning witheachentryrepresentingaspecificinstanceevent.
offailureclassification. MetricEventParsing.Formonitoringtheoperatingstateof
Specifically,weconsideralarge-scalemicroservicesystemwith
instances,metricsaremeticulouslytrackedandrecordedattheindi-
𝑄instances,andlogs,metrics,andtracesareaggregatedforeach
vidualinstancelevel.Weusethe3-sigmatechniquetodetectabnor-
| instance.ForafailureF𝑡 |     | thatoccursattime𝑡 | anda𝑤-lengthob- |     |     |     |     |     |
| ---------------------- | --- | ----------------- | --------------- | --- | --- | --- | --- | --- |
malmetricsinthetimewindow.Whenametric’svaluesurpasses
servationwindowahead,wecanattainitscontextualmulti-modal theupperthreshold,itisclassifiedasan“upward”anomaly,indicat-
|     | L,𝑋 | M,𝑋 T)} 𝑄 | L   | M,𝑋 T |     |     |     |     |
| --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
data,F[𝑡−𝑤,𝑡] ={(𝑋 ,where𝑋 ,𝑋 arethe ingasignificantincrease.Conversely,ifthemetricvaluedropsbe-
|     | 𝑖   | 𝑖 𝑖 𝑖=1 | 𝑖   | 𝑖 𝑖 |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- |
eventsetsofcorrespondingmodalities(i.e.,logs,metrics,traces)
lowthelowerbound,itisflaggedasa“downward”anomaly,reflect-
forthe𝑖-thinstance.AsshowninFig.1,themulti-modalevent
inganotabledecrease.Theextractedmetriceventsarestoredinatu-
sequencesforinstance𝑅
1inthewindowbeforefailurearegrouped pleformat<timestamp,instance-id,metric-name,anomaly-type>,
|     | L   | M,and𝑋 T.Thetargetedframeworkisthus |     |     |     |     |     |     |
| --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
bymodalityinto𝑋 ,𝑋 capturingthespecificeventanditsanomalytypeforanalysis.
|     | 𝑅 1 | 𝑅 1 𝑅 1 |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- |
571

ToSplitortoMerge?ExploringMulti-modalDataFlexiblyforFailureClassificationinMicroservices Internetware2025,June20–22,2025,Trondheim,Norway
Data Pre-processing Modality-aware Representation Fusion-based
Classification
Template-based
Parsing
Log
Anomaly
Detection
Metric Expert 2
Trace
daeH-itluM noitnettA mroN
&
ddA
drawroF
deeF
mroN
&
ddA
Expert 1
Classifier
...
Expert M
gnidocnE
lanoitisoP
&
gniddebmE
Weighted ataD
gnirotinoM
lacirotsiH
Fusion
Softmax
Anomaly
Detection
-tsoP
gnissecorp
Figure2:TheframeworkofAgileMFC.Wherein,therepresentationmoduleextractsafeaturevectorforeacheventinturn
withtheswitchconnectingtothemodalitygatecorrespondingtotheeventmodality.
TraceEventParsing.Tracesareimportantforreconstructing positionalencodingtotheembeddingvectorforeachevent.Specif-
thecausalityandflowofoperationswithinamicroservicesystem. ically,foraneventatposition𝑝𝑜𝑠inthesequence,wegeneratea
Instanceswillbecalledwhentheserviceprocessesarequestfrom positionalencodingvector𝑃𝐸(𝑝𝑜𝑠)usingsinusoidalfunctions:
theuserandthetiminggapbetweenaninstancebeinginvoked
and getting a response is called response time. Meanwhile, the 𝑃𝐸(𝑝𝑜𝑠,2𝑖)=sin(𝑝𝑜𝑠/100002𝑖/𝑑𝑖𝑚 )
systemwillreturnastatuscodetorecordtheresultofarequest.
Weformtheresponsetimeandthenumberofeachstatuscode 𝑃𝐸(𝑝𝑜𝑠,2𝑖+1)=cos(𝑝𝑜𝑠/100002𝑖/𝑑𝑖𝑚 ), (1)
astwotimeseries,andthenapply3-sigmaforanomalydetection
onthem.Thatis,wedeterminesuchasetofcallerandcalleein- where𝑖isthedimensionindexand𝑑𝑖𝑚istheembeddingdimension.
stancesasanomalouswhentheresponsetimeorthenumberof Thus,wecanobtainacombinedrepresentationthatpreservesboth
statuscodesexceedsthreestandarddeviationsfromtheirmean semanticandpositionalinformation.
values.Theextractedtraceeventsarerecordedintheformoftu-
ples<timestamp,caller-instance-id,callee-instance-id>,providing
4.3 Modality-awareRepresentation
astructuredrepresentationoftheeventflowbetweeninstances.
Withmonitoringdatapre-processing,AgileMFChasmappedevents
Theaboveextractionprovideseventsfromdifferentmodalities.
withdifferentmodalitiesintoauniformformofembedding.How-
Wegroupeventsbyinstance-id,thenreordertheeventsfromdiffer-
ever,theseembeddingsareinherentlyheterogeneousduetothe
entmodalitiesinthesameinstancebytimestamp,andfinallyobtain
diversityofmodalities,makingitchallengingtocollectivelycorre-
theeventsequence.Fig.1showstheprocessingfromeventstoevent
lateeventsfordiagnosingthefailure.Inthispart,weproposeto
sequences.The𝑗-thmulti-modaleventisrepresented𝑑
𝑗
L ,𝑑
𝑗
M,and
usedeepfeaturestoelaborateonhomogeneousrepresentationsfor
𝑑
𝑗
T.Theeventsequenceconsistingofthesamemodality(e.g.,log)
differentmodalities.
isdenotedby𝑋L ={𝑑
1
L,...,𝑑
𝑗
L}.Subsequently,wecanobtainthe Forthis,AgileMFCuseseventswithfailuretypeslabelsinhis-
eventsequenceoftheinstance𝑖,which𝑋 𝑖 = [𝑋 𝑖 L,𝑋 𝑖 M,𝑋 𝑖 T]. t r o es ri e c n a t l a f t a io il n ur n e e s tw fo o r r s k u . p C e o r n vi s s i e d d er l i e n a g rn th in a g td o i f ff a er m en o t d m ali o t d y a -a li w ti a e r s e h r a e v p e -
differentsensitivitiesforspecificfailures,AgileMFCinvolvesmul-
4.2.2 EventEmbedding. Theraweventtexts,althoughunifiedinto tipleexpertnetworks,eachofwhichisbelievedtohavedifferential
asimilartupleformat,arestillunstructuredandsparseinrepre- expertiseindiagnosingdifferentmodalities.Alongsidethissplit
sentations. Therefore, we need to transcode the event texts for opinionexpressingstep(§4.3.1),itfurtherdeterminesthereliance
furtherrepresentationlearning.AgileMFCconvertsthesetextsinto andconfidenceofdifferentexperts’suggestionsandmergesthem
continuousandstructuredrepresentationsthrougheventsemantic withdeliberategatingnetworks(§4.3.2).
embeddingandpositionalcoding.
SemanticEmbedding.Weuseaneuralnetworklayertocon- 4.3.1 ExpertNetworks. InspiredbytherecentadvancesofMoE
verttheone-hotvectorofeacheventtextintoadensevector.This architectureandthemulti-channelinputcharacteristics,AgileMFC
processmapsdiscreteeventsintoacontinuousvectorspacewhere uses𝑚expertnetworks(thenumberofexpertsistunable)inrepre-
semanticallysimilareventsareclosetoeachother.Forexample,for sentation.Fornetworkstructure,recurrentneuralnetworks(RNNs)
theeventsequenceoflog𝑋L,weapplytheembeddingfunctionto
havebeenwidelyusedtocapturethetemporalpatterninprevi-
obtainthecorrespondingembeddingvector𝐸L ={𝑒 1 L,...,𝑒 𝑗 L}.The ous work, [3, 10], while convolutional neural networks (CNNs)
embeddinglayerisinitializedusingrandomweightsandfine-tuned arecommonlyusedtoextractlocaltraits[20,21].However,RNNs
duringtraining. sufferfromcomputationalinefficiencyduetotheirsequentialpro-
PositionalEncoding.Toenablethemodeltodistinguishbe- cessingnature,whileCNNsarelimitedinmodelinglong-range
tweeneventsbasedontheirpositionsinthesequence,weapply dependenciesacrossmultiple.
572

| Internetware2025,June20–22,2025,Trondheim,Norway |     |     |     |     |     |     |     |     |     |     |     |     |     | Tanetal. |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
Inthisdesign,AgileMFCemploysTransformerblocks[18]asthe where⊙denotestheHadamardproduct(i.e.,element-wiseproduct).
realizationofanexpert.TheTransformerarchitecture,unlikese-
|     |     |     |     |     |     |     |     | 4.4 FusionforClassification |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
quentialprocessingofRNNs,computesallpositionssimultaneously,
whichcouldacceleratetrainingandinference.Theself-attention
Basedontheeventrepresentationlearnedin§4.3,theclassification
mechanismallowseachexperttofocusonthefailure-sensitiveparts
networksubsequentlyfusestherepresentationsinthesequenceto
ofaneventvector.Meanwhile,theusingofmultipleexpertsimplic-
attainanoverallfailurerepresentationfortypeclassification.
itlyreducetheriskthatone(ormore)expert(s)cannotproperly Inparticular,thisphasefirstcalculatesweightscoresforevents
understandanevent(i.e.,withoutexpertise)liketheothers. inthesequencebyusingTF-IDFonhistoricalfailureeventsand
|     |     |     | 𝑓   | consistsof𝐿 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Specifically,eachexpert stackedTransformer currentevents.Givenacollectionofeventsabout𝑃 historicalfail-
encoderlayers(thenumberistunable).Givenaninputlogevent ures𝑇 {𝑡 ,𝑡 ,...,𝑡 𝑝},each𝑡
|            |     |                                        |     |     |       |     |     | =                                    | 1 2 |     | 𝑖 representsaneventsequence,we |        |     |     |
| ---------- | --- | -------------------------------------- | --- | --- | ----- | --- | --- | ------------------------------------ | --- | --- | ------------------------------ | ------ | --- | --- |
| embedding𝑒 | L   | ,theoutputofthe𝑚-thexpertiscomputedas: |     |     |       |     |     |                                      |     |     |                                | ∈R𝑃×𝑉  |     |     |
|            | 𝑗   |                                        |     |     |       |     |     | firstconstructaterm-frequencymatrix𝑋 |     |     |                                |        | :   |     |
|            |     | L)=TransformerBlock                    |     |     | 𝐿 L), |     |     |                                      |     |     |                                |        |     |     |
|            |     | 𝑓 𝑚(𝑒                                  |     |     | (𝑒    |     | (2) |                                      |     | 𝑋   | =count(𝑡                       | ,𝑣 𝑗), |     | (7) |
|            |     | 𝑗                                      |     |     | 𝑗     |     |     |                                      |     | 𝑖,𝑗 |                                | 𝑖      |     |     |
whereeachTransformerblockcomprisesmulti-headself-attention where𝑉 isthesizeofthevocabulary,𝑣 𝑗-thvocabulary
|     |     |     |     |     |     |     |     |     |     |     |     | 𝑗 isthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
andfeed-forwardsublayerswithlayernormalizationandresidual
|     |     |     |     |     |     |     |     | termandcount(𝑡 | 𝑖   | ,𝑣 𝑗)countsitsoccurrencesin𝑡 |     |     | 𝑖.Wethenapply |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------------------- | --- | --- | ------------- | --- |
connections[18].Theoutputsofall𝑀expertsareintheformof:
|     |     |     |     |     |     |     |     | TF-IDFweightingtoobtaintheimportancematrix𝑊 |     |     |     |     |     | =TF-IDF(𝑋). |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ----------- |
expertOut(𝑒 L)= [𝑓 (𝑒 L),𝑓 (𝑒 L),...,𝑓 𝑀(𝑒 L)]. Thisweightingschemeemphasizeseventsthatarefrequentinthis
|     |     |     | 𝑗   | 1 𝑗 2 | 𝑗   | 𝑗   | (3) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
failureandrareacrosstheentiredataset,effectivelycapturingthe
Notethatexpertsperformencodinginanevent-wisemanner
specificcharacteristicsofthefailure.
(e.g.,Equation3outputsthe𝑖-thlogeventinthesequence),which
Afailureinvolvesmultipleinstances,eachcontainingseveral
handlestheinputsequenceofeventsinturn.Suchasplitdesign
eventsfromdifferentmodalities.Hence,wecomputethefailure
allowsdifferentexpertstogaindifferentialrepresentationexpertise representation𝐻 byaggregatingalleventrepresentationsinall
ondifferentmodalities,e.g.,temporaldependenceinlogsandspatial instancesweightedbytheirTF-IDFscores:
correlationinmetrics.
𝑁 𝐾
∑︁∑︁
4.3.2 Modality&SharingGate. Afterthesplitencodingofexperts, 𝐻 = 𝑤 ·𝑧 ,
|     |     |     |     |     |     |     |     |     |     |     |     | (𝑖,𝑘) (𝑖,𝑘) |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
AgileMFCusesgatenetworkstointegrateexpertoutputsforeach
𝑖=1𝑘=1
event.TheoriginalMMoEnetworkemploysasinglegatepertask where𝑁 isthenumberofinstances,𝐾 isthenumberofevents,
toblendexpertoutputs,whichstrugglestobalancesingle-modal 𝑤 (𝑖,𝑘)(anelementin𝑊)istheTF-IDFweightforevent𝑘ofinstance
andcross-modalfeaturesinthemulti-modalcontext.Giventhis,we 𝑖,and𝑧 istherepresentationforevent𝑘ofinstance𝑖,gained
(𝑖,𝑘)
designaquadruplegatingmechanismthatmaintainsanindividual
fromEqu.6.
| gateforeachmodality(i.e.,𝐺 |     |     |     | L forlog,𝐺 | M formetric,and𝐺 |     | T   |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m m m Thispolymerizationensuresthat𝐻 capturesthefullcontextof
fortrace),andsharesoneglobalcross-modalgate(𝐺
|     |     |     |     |     |     | s).Aswitch |     | afailure,assemblinginformationaboutallrelevanteventsfrom |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
isusedbeforethegatingnetworks,whichconnectsthesharing
|     |     |     |     |     |     |     |     | different | instances | and modalities. |     | Finally, | the predicted | failure |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------------- | --- | -------- | ------------- | ------- |
gatewiththemodalitygatethatcorrespondstotheinputevent’s typeisobtainedthroughathree-layerneurallinearclassifier:𝑦ˆ=
modality,i.e.,onlyonemodalitygateisactivatedformergingan
LinearClassifier(𝐻).
event’sexpertoutputs.Thegatingprocessofthesetwotypesof
gatesiscalculatedasfollows: 4.5 Two-stageTrainingforDecoupledLearning
|     | 𝐺   | (𝑒 L)=𝑊 | ·𝑒  | L, 𝐺 L(𝑒 L)=𝑊 | L·𝑒 | L,  |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s 𝑗 s 𝑗 m 𝑗 m 𝑗 (4) Consideringthatrepresentationisagnostictotaskwhileclassifi-
|        |      |         |        |       |                        |     |     | c a ti o n is | , w e p r op | o se to | t r a i n th | e s e tw o m | o d u l e s in | d e p e n de n t l y |
| ------ | ---- | ------- | ------ | ----- | ---------------------- | --- | --- | ------------- | ------------ | ------- | ------------ | ------------ | -------------- | -------------------- |
| where𝑊 | ,𝑊 L | ∈R𝑑𝑖𝑚×𝑀 | ,both𝑊 | sand𝑊 | maretrainablematrices. |     |     |               |              |         |              |              |                |                      |
|        | s m  |         |        |       |                        |     |     |               |              |         |              |              |                |                      |
Similarly,itusesmatrices𝑊Mand𝑊Tforgatingmetricandtrace b y fi r st t r ain i n g th e re pr e s e n ta ti o n w it h sh o r t c u t lo s s a n d t h e n
|     |     |     | m   | m   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
freezingittotraintheclassifiersecondly.
events,respectively.Thefinalgatingweightsforthelogmodality
arecomputedas: 4.5.1 TuningtheRepresentationNetwork. Wedirectlyconnectthe
|     |           |                |     |     |          |     |     | o u tp u t o   | f th e re p r | e se n t a t io | n ne t w | o r k t o a s ho   | rt c u t o  | u tp u t f or lo s s |
| --- | --------- | -------------- | --- | --- | -------- | --- | --- | -------------- | ------------- | --------------- | -------- | ------------------ | ----------- | -------------------- |
|     | gateOut(𝑒 | L)=softmax(𝛼·𝐺 |     |     | +(1−𝛼)·𝐺 | L), | (5) |                |               |                 |          |                    |             |                      |
|     |           | 𝑗              |     | s   |          | m   |     |                |               |                 |          |                    |             |                      |
|     |           |                |     |     |          |     |     | ev a lu a ti o | n an d o p t  | im i z a ti o   | n .A c o | n c a te n at io n | is a p p li | e d to t h e th re e |
where𝛼 istheweightcoefficientofthesharinggateandthe 𝑗- modalityfeatures(i.e.,𝑧L,𝑧Mand𝑧T)toobtainaflatfeature.Then,
| thelementingateOut(𝑒   |     |     | L)countsfortheweight/relianceofthe |     |     |     |     |                                                         |     |     |     |     |     |     |
| ---------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                        |     |     | 𝑗                                  |     |     |     |     | alineartransformationisusedtomapthemintoacompactfailure |     |     |     |     |     |     |
| outputofthe𝑗-thexpert. |     |     |                                    |     |     |     |     | classificationprediction.                               |     |     |     |     |     |     |
Thetransformationprocesscanbedescribedasfollows:
| 4.3.3 | Post-processing. |     | Post-processingmergestheexpertfeatures |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ---------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
·[𝑧L∥𝑧M∥𝑧T]+𝑏
viaweightedsumandtransformsthemthroughlinearprocessing. 𝑍 =𝑊 𝑓 𝑓 , (9)
Specifically,weuseasimpleMLPstructurethatconsistsoftwofully
|     |     |     |     |     |     |     |     | where[·∥·]representstheconcatenationoperation,𝑊 |     |     |     |     |     | and𝑏 are |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | -------- |
connectedlayerswithReLUactivationanddropoutregularization 𝑓 𝑓
inbetween.Thepost-processingmodalityfeatures𝑧 L of𝑗-thevent the m ap p i ng w e igh t m a t ri x a n d bi as , re s p e c t i v e l y.
|     |     |     |     |     |     | 𝑗   |     |        |             |             |             | 𝑍             |                          |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----------- | ----------- | ------------- | ------------------------ | --- |
|     |     |     |     |     |     |     |     | T he c | o m bi ne d | re p re s e | n ta t io n | e n c a p s u | l a t e s thejointunder- |     |
iscomputedasfollows:
standingofalleventsinafailure.Next,weindependentlyoptimize
|     | L   |     |     | L)⊙gateOut(𝑒 |     | L)), |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑧 =M𝑜𝑢𝑡(expertOut(𝑒 (6) themodality-awarerepresentationnetworktoensureitcaptures
|     | 𝑗   |     |     | 𝑗   |     | 𝑗   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
573

ToSplitortoMerge?ExploringMulti-modalDataFlexiblyforFailureClassificationinMicroservices Internetware2025,June20–22,2025,Trondheim,Norway
discriminativecross-modalpatterns.Thistuningprocessisguided TTreflectsthecomplexinteractionsandhightransactionvolumes
byanauxiliaryrepresentationloss: typicalofreal-worldservicesystems.
|     | 𝑃      | 𝐶   |     |     | SocialNetwork[4](SN):TheSNdatasetsimulatesasocialnet- |     |     |     |     |     |
| --- | ------ | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
|     | 1 ∑︁∑︁ |     |     |     |                                                       |     |     |     |     |     |
L𝑟𝑒𝑝 =− 𝑦 ·log (cid:0)𝑍 (cid:1), workingplatformwith21microservices,with12dedicatedtocore
|     | 𝑃   | 𝑖,𝑐 | 𝑖,𝑐 | (10) |           |             |             |          |             |           |
| --- | --- | --- | --- | ---- | --------- | ----------- | ----------- | -------- | ----------- | --------- |
|     |     |     |     |      | business. | SN contains | 2.4 million | metrics, | 1.5 million | logs, and |
𝑖=1𝑐=1
126,000traces,withthreeinjectedfailuretypes.Thisdatasetisused
| where𝑃 isthenumberofhistoricalfailures,𝐶 |     |     | isthenumberof |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
failuretypes,and𝑦isthefailuretype.Thisindependentlyoptimized foranalyzinguserinteractions,contentcreation,etc,makingit
idealforstudyingmicroserviceinteractionandfailureprediction.
procedureallowsfordistinguishablefeaturesfordifferentfailure
typesandunbiasedtrainingofexpertsandmodalitygates.
Table2:DetailedinformationofDatasets
Inthisstage,withtherepresentation
4.5.2 TuningtheClassifier.
networkfrozen,theclassifiernetworkisoptimizedbyminimizing
|     |     |     |     |     |     | #Instances | #Failuretypes |     | Modality | #Samples |
| --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | -------- | -------- |
thefollowingcross-entropyloss:
|     |     |     |     |     |     |     |     |     | Metric | 56,684,196 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- |
𝑃 𝐶
|      | 1 ∑︁∑︁ |            | (cid:0)𝑦ˆ𝑖,𝑐 (cid:1), |      | GAIA | 10  |     | 5   | Log   | 87,974,577 |
| ---- | ------ | ---------- | --------------------- | ---- | ---- | --- | --- | --- | ----- | ---------- |
| L𝑐𝑙𝑓 | =−     | 𝑦 𝑖,𝑐 ·log |                       | (11) |      |     |     |     |       |            |
|      | 𝑃      |            |                       |      |      |     |     |     | Trace | 2,321,280  |
𝑖=1𝑐=1
Inaddition,AgileMFCincorporatesgridsearchduringtraining Metric 127,171,863
todeterminetheoptimizedhyperparametersforthenumberof TT 27 3 Log 6,768,927
expertsandthenumberofblocks.Byexhaustivelysearchingand Trace 48,296
evaluatingallpossiblecombinationsofhyperparameters,themodel
|     |     |     |     |     |     |     |     |     | Metric | 2,439,072 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- |
isadaptivelyassignedaneffectivehyperparameterconfiguration. SN 12 3 Log 1,468,692
|     |     |     |     |     |     |     |     |     | Trace | 126,384 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- |
5 Evaluation
Inthissection,weevaluatetheperformanceofAgileMFCusing
threereal-worlddatasets.Weaimtoanswerthefollowingresearch
|     |     |     |     |     | 5.1.2 | Metrics. Weemploytheweightedaverageprecision,recall |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --------------------------------------------------- | --- | --- | --- | --- |
questions(RQs):
andF1-scoretoevaluatetheperformanceofAgileMFCandbase-
• RQ1:HowdoesAgileMFCperformonfailureclassification? lines. The precision, recall and F1-score are calculated based on
• RQ2:DoeseachcomponentcontributetoAgileMFC’sper- TruePositives(TP),FalsePositives(FP),andFalseNegatives(FN).
| formance? |     |     |     |     |     |                |                   |     | 2·𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛·𝑟𝑒𝑐𝑎𝑙𝑙 |         |
| --------- | --- | --- | --- | --- | --- | -------------- | ----------------- | --- | ------------------ | ------- |
|           |     |     |     |     | The | calculation is | given by F1-score | =   |                    | , where |
• RQ3:Whatistheimpactofdifferenthyperparameters? 𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙
|     |     |     |     |     | 𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= | 𝑇 𝑃 𝐹𝑃,𝑟𝑒𝑐𝑎𝑙𝑙 |      | 𝑇 𝑃 |     |     |
| --- | --- | --- | --- | --- | ---------- | ------------- | ---- | --- | --- | --- |
|     |     |     |     |     |            | 𝑇𝑃            | = 𝑇𝑃 | 𝐹𝑁. |     |     |
|     |     |     |     |     |            | +             |      | +   |     |     |
Theweightedaverageofthesemetricsisintendedtoensurea
5.1 Settings
comprehensiveassessmentofperformance.Also,tominimizethe
5.1.1 Datasets. ToevaluatetheperformanceofAgileMFC,wecon- effectofrandomness,eachexperimentwasrepeatedfivetimesand
ductextensiveexperimentsonthreedatasetscollectedfromthree
theresultswereaveraged.
microservicesystemsunderdifferentbusinessbackgroundsand
architectures.Wesplitthedatasetsintotrainingandtestingsets 5.1.3 Baselines. Weusefourbaselineapproachesforcomparison,
basedontemporalprecedence,whereearlierdataisusedfortrain- includingtwosingle-modal-basedapproachesandtwomulti-modal-
ingandlaterdataservesasthetestset.Detaileddatasetinformation basedapproaches.
islistedinTable2.Thedatasetsusedinthisstudyareasfollows: Cloud19[23]isasupervisedframeworkdesignedtoidentify
GenericAIOpsAtlas(GAIA)3:GAIAiscollectedfromasimu- failuretypesusingsystemlogs.
lationenvironmentconsistingof10microservices,twodatabase LogCluster[11]employsunsupervisedclusteringtechniquesto
services(MySQLandRedis),andfivehostmachines.Operators identifyfailuretypesbygroupingthelogeventbasedonsimilarity.
injectedfivetypesoffailures,includingsystemfailures(System CloudRCA[26]isarootcauseanalysisapproachthatleverages
stuckandProcesscrash)andservicefailures(Loginfailure,File cloudservicemetricsandlogstodiagnosefailure.
missing,andAccessdenied).Thedatasetincludesmorethan56 DiagFusion[24]integratesmulti-modaldataincludinglogs,met-
millionmetrics,87millionlogs,and2.3milliontraces.GAIAis rics,andtracesthroughfasttext,andadoptsaGNNforaccurate
ahigh-qualitybenchmarkdatasetthatsupportsawiderangeof failurediagnosis.DiagFusionpresentstheSoTAperformancein
OperationandMaintenance(O&M)automationtasks. existingworks.
TrainTicket[28](TT)4:TheTTdatasetiscollectedfromaticket-
|     |     |     |     |     | 5.1.4 | Implementation. | AgileMFCisimplementedinPyTorchand |     |     |     |
| --- | --- | --- | --- | --- | ----- | --------------- | --------------------------------- | --- | --- | --- |
ingsystemwith41microservices,ofwhich27engageinfrequent
alloftheexperimentsareconductedonaserverwithoneIntel(R)
interactions.Itsupportsoperationsincludingticketbooking,check-
Core(TM)i7-9700CPU@3.00GHz,and32GBRAM.Forhyper-
ing,andpaymentprocessing.Withthreetypesofinjectedfailures
andover127millionmetrics,6.7millionlogs,and48,000traces, parameterconfiguration,thenumberofexpertsis8forGAIA,3
forTT,and5forSN,thenumberofTransformerblocksis4for
3https://github.com/CloudWise-OpenSource/GAIA-DataSet GAIA,1forTT,and2forSN.WeapplytheAdam[7]optimizerand
4BothTTandSNwerecollectedbyEadro[8] ReduceLROnPlateautoadjustthelearningratedynamically.The
574

Internetware2025,June20–22,2025,Trondheim,Norway Tanetal.
Table3:Theaverageprecision,recall,andF1-scoreofdifferentapproachesonthreedatasets.
GAIA TT SN
Approach
Precision Recall F1-score Precision Recall F1-score Precision Recall F1-score
Cloud19[23] 0.774 0.774 0.756 0.230 0.353 0.277 0.396 0.375 0.375
LogCluster[11] 0.615 0.477 0.336 0.435 0.450 0.441 0.186 0.300 0.220
CloudRCA[26] 0.436 0.453 0.357 - - - 0.692 0.462 0.478
DiagFusion[24] 0.806 0.829 0.839 0.710 0.700 0.696 0.455 0.300 0.325
AgileMFC 0.958 0.924 0.939 0.751 0.720 0.728 0.872 0.620 0.701
‘-’denotes“outofmemory”error.
initiallearningrateissetto0.001,withabatchsizeof16and10 AgileMFC using CNN: This variant replaces the Transformer
epochsfortraining. blockwithaCNNtoinvestigatetheeffectofmulti-headattention
onoverallperformance.
5.2 RQ1:PerformanceofAgileMFC AgileMFCw/ogating:Inthisvariant,weremovethegatingmech-
anismtoexamineitscontributiontoAgileMFC’sperformance.
Table3liststheaverageprecision,recall,andF1-scoreofAgileMFC
AgileMFCw/osharing-gate:Thisvariantremovesthesharing-
andfourbaselineapproachesonthethreedatasets.AgileMFCcon-
gatewhileretainingthemodality-gate,allowingustoassessthe
sistentlyoutperformsallbaselinesonalldatasets,achievingthe
roleofcross-modalfeaturesharinginthegatingmechanism.
highestaverageF1-scoreof0.939,0.728,and0.701,respectively.
AgileMFCw/omodality-gate:Byeliminatingthemodality-gate
OnGAIA,AgileMFCshowsexceptionalperformancewiththe
whileretainingthesharing-gate,wecanbetterunderstandhow
averageprecision,recall,andF1-scoreall-surpassing0.92,demon-
modalityfeaturesinfluencethegatingprocessandperformance.
stratingitsrobustnessinhandlinglarge-scaledatawithdiverse
AgileMFCw/oTF-IDFweighting:Tostudytheimportanceofevent
failuretypes.OnTTandSN,AgileMFCexceedsthebaselineap-
weighting,weremovetheTF-IDFweightingmodule,whichisused
proaches by at least 0.2 in terms of the average F1-score. The
tohighlightimportanteventsinthemodel.
superior performance of AgileMFC can be attributed to the ef-
AgileMFCusingKNN:Toobservehowthedenserepresentations
forts of the modality-aware representation network, where the
affectclassificationperformance,wereplacethefullyconnected
Transformerblock-basedexpertnetworkcanfocusonthefailure-
layerwithaKNNmodel.
sensitive events through the self-attention mechanism, and the
AgileMFCusingRandomForest:Thissetupofvariantreplacesthe
gatingmechanismflexiblymergestheoutputsoftheexpertsac-
fullyconnectedlayerwithaRandomForestmodeltoinvestigate
cordingtothedifferentmodalities.TheAgileMFC’sperformance
whetheratree-basedensembleapproachcouldperformbetterin
onTTandSNtrailsGAIAslightly,whichisunderstandablegiven
thedecisionprocess.
thatthesamplesizesofTTandSNaremuchsmallerthanGAIA.
Table4summarizestheresults,demonstratingthatAgileMFC
Itisalsonoteworthythatmulti-modal-basedapproachesgener-
achieveshigherperformancethanallvariantsacrossthedatasets.
allyoutperformsingle-modal-basedbaselines,astheyintegrate
Clearly,eachcomponentcontributestotheperformanceofAg-
diverse sources of data, leading to better classification perfor-
ileMFC.PerformancedeclineswhentheTransformerblockisre-
mance.However,incertaincases,suchasCloud19outperforming
placed,asself-attentionmechanismsareparticularlyeffectiveat
CloudRCAonGAIA,single-modalapproachescanbebetter,es-
capturingfailure-sensitiverepresentations,whereasCNNsstruggle
peciallywhenonemodalitycarriesmoreweightinthesystem’s
toextractsuchcomplexandnuancedfeatures.Whenthegating
failure.Thisreinforcestheimportanceofflexibletrade-offsbetween
mechanismisremoved,includingthesharing-gateorthemodality-
thecharacteristicsofdifferentmodalitiesinmicroservicefailure
gateindividually,theperformancedeclines,highlightingthecrucial
classification.
roleofthegatingmechanismindynamicallyassigningexpertout-
Inbrief,AgileMFCdemonstratesefficientperformanceinthe
puts.Specifically,removingthesharing-gatehindersthemodel’s
failureclassificationtaskacrossalldatasets,improvingtheaver-
ability to share cross-modal information, while eliminating the
ageF1-score(acrossthethreedatasets)by12.4%,9.1%,and11.8%
modality-gatedisruptsthecorrectallocationofweightstodifferent
comparedtothe2nd-bestbaseline.Theseimprovementshighlight
modalities.Furthermore,excludingtheTF-IDFweightingmodule
AgileMFC’s value as a reliable tool for supporting downstream
impairedperformance,asitlimitedthemodel’scapacitytomerge
tasksinmicroservicesystemO%M,suchasrootcauselocalization
rich semantic embeddings, thereby weakening its ability to un-
andtroubleshooting.
derstandcontext.Finally,replacingthefullyconnectedlayerwith
KNNandRandomForestresultsinlowerperformance,asboth
5.3 RQ2:AblationStudy approacheslacktheabilitytolearnhierarchicalrepresentations
Thispartconductsacomprehensiveablationstudytoevaluatethe andoptimizeparametersthroughbackpropagation.
contributionofeachcomponentofAgileMFC.Wecreatesevenvari-
antsofAgileMFCandperformaseriesofcontrolledexperiments.
Thevariantsaredescribedasfollows:
575

ToSplitortoMerge?ExploringMulti-modalDataFlexiblyforFailureClassificationinMicroservices Internetware2025,June20–22,2025,Trondheim,Norway
Table4:Theaverageprecision,recall,andF1-scoreofAgileMFCanddifferentmodelvariants
GAIA TT SN
Approach
Precision Recall F1-score Precision Recall F1-score Precision Recall F1-score
useCNN 0.928 0.894 0.908 0.662 0.610 0.624 0.695 0.500 0.538
w/ogating 0.941 0.913 0.926 0.590 0.570 0.568 0.695 0.500 0.536
w/osharing-gate 0.930 0.896 0.910 0.687 0.660 0.668 0.703 0.500 0.546
w/omodality-gate 0.937 0.903 0.917 0.680 0.650 0.656 0.710 0.560 0.590
w/oTF-IDFweighting 0.886 0.833 0.857 0.710 0.640 0.657 0.710 0.580 0.588
useKNN 0.815 0.845 0.829 0.590 0.400 0.372 0.471 0.400 0.368
useRandomForest 0.844 0.882 0.857 0.451 0.450 0.450 0.300 0.300 0.300
AgileMFC 0.958 0.924 0.939 0.751 0.720 0.728 0.872 0.620 0.701
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
1 2 3 4 5 6 7 8 9 10
# Experts
erocs-1F
1 2 3 4 5 6 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 0 50 500 1000 2000 4000
# Transformer Blocks # Argumented Samples
GAIA TT SN
Figure3:TheperformanceofAgileMFCunderdifferenthyperparameters.
5.4 RQ3:HyperparametersSensitivity eitherhigher(closerto1)orlower(closerto0)of𝛼,leadtosub-
WediscusstheeffectoffourhyperparametersofAgileMFC.Fig.3 optimalperformance,consistentwiththefindingsin§5.3.
showshowtheaveragebestF1-scorechangeswithdifferenthyper-
5.4.4 TheNumberofAugmentedSamples. InAgileMFC,weaug-
parameters.
mentthesamplesizeofthedatasetbasedontextualsemantics,and
5.4.1 TheNumberofExperts. Thenumberofexpertsaffectsthe experimentsindicatethatthisimprovesAgileMFC’sperformance.
featurelearningabilityoftheMMoEnetwork.NotethattheMMoE However,textualaugmentationmustbesubtletocapturesemantic
isdegradedtoashared-bottommodelwithonlyoneexpert.As coherenceandlinguisticnuancescomparedtoimagedataaugmen-
thenumberofexpertsincreases,MMoEhasagreatercapacityto tation.TheresultsonTTandSNdemonstratethatinappropriate
capturethecomplexfeaturesofthemodality,whilemoreexperts augmentationcanleadtononsensicalormisleadingdata,thereby
sacrificethesimplicityofthemodel,spendingextratimeintraining. potentiallyimpairingmodelperformance.
Basedonourexperiments,werecommendsettingthenumberof
expertsbetween3and8tostrikeagoodbalancebetweenrepresen- 6 Discussion
tationperformanceandcomputationalefficiency. Limitations.AgileMFCrequireslabeledfailuredata,i.e.,typical
typesobservedinlarge-scalemicroservicesystems,toclassifyfail-
5.4.2 TheNumberofTransformerBlocks. Astheblocknumberof
ures.Attainingsuchannotationcouldbeexpensiveandmayrequire
Transformervariesfrom1to6,theperformanceofAgileMFCon
long-termoperationrecording.Thischallengemightberelievedby
GAIAisrelativelystablewithaslightincrease,peakingatthefourth
exploringsemi-supervisedlearningtechniques,whicharecapable
block.Incontrast,theperformanceofTTandSNfluctuatesmore
ofreducingtherelianceonlarge-scalelabeleddata.Ontheother
prominently,withanotabledeclineobservedafterreachingtheir
hand,althoughtypicalfailurescancoveravastmajorityofreal-
respectiveoptimalblocknumbers(1forTTand2forSN).These
worldscenarios,therearestillunknownandunseenfailuretypes
observationssuggestthatwhileaddingmoreblockscanenhance
duringthedevelopmentofnewmicroservices.Wenotethatthisis
featurelearningincertaincases,excessivecomplexitymayleadto
acommondrawbackofsupervisedlearning,andonecouldreferto
overfittingorreducedgeneralization.
transferlearningformitigatingsuchcoldstartpitfallindiagnosing
5.4.3 TheCoefficientofSharingGate. InEqu.5,MMoEregulates newsystemsandunseenissues.
theparticipationofsharing-gateviaacoefficient𝛼.Weconducted Implications.TheMoEstructureisevaluatedinthisworktobe
experimentsbyvarying𝛼 from0.1to0.9toobserveitseffecton effective,showingtheSoTAperformanceforfailureclassification,
performance.AsdepictedinFig.3,AgileMFCattainsitsoptimal inanalyzingmulti-modalmonitoringdatafrommultiplesources.
performancewhen𝛼 isequalto0.7.Deviationsfromthisvalue, Theunderlyingfactorsaredealingwithheterogeneousdatawith
576

Internetware2025,June20–22,2025,Trondheim,Norway Tanetal.
morethanoneexpert,thusimplicitlymatchingtunableexpertswith [9] AlexanderLercher,JohannGlock,ChristianMacho,andMartinPinzger.2024.
differenttaskcases.Webelievesuchattemptscouldshedlighton MicroserviceAPIEvolutioninPractice:AStudyonStrategiesandChallenges.
JournalofSystemsandSoftware215(2024),112110.
anomalydetectionandrootcauseidentificationinAIOpsoflarge
[10] XiaoyunLi,PengfeiChen,LinxiaoJing,ZilongHe,andGuangbaYu.2022.Swiss-
systemsbyassemblingthewisdomofabunchofexperts.Since log:Robustanomalydetectionandlocalizationforinterleavedunstructured
high-volumemicroservicesareexpectedfollowingtheincreasing logs.IEEETransactionsonDependableandSecureComputing(TDSC)20,4(2022),
2762–2780.
deploymentofmicroservices,futureworkmayfocusonincorporat- [11] QingweiLin,HongyuZhang,Jian-GuangLou,YuZhang,andXueweiChen.
ingmoredatamodalitiesanddynamicmodelupdatingstrategies 2016. Logclusteringbasedproblemidentificationforonlineservicesystems.
InProc.ofthe38thInternationalConferenceonSoftwareEngineeringCompanion
toaccommodatethedynamicnatureofmicroserviceinteractions.
(ICSE-Companion).102–111.
[12] DeweiLiu,ChuanHe,XinPeng,FanLin,ChenxiZhang,ShengfangGong,Ziang
Li,JiayuOu,andZheshunWu.2021.Microhecl:High-efficientrootcauselocaliza-
7 Conclusion tioninlarge-scalemicroservicesystems.InProc.ofIEEE/ACM43rdInternational
ConferenceonSoftwareEngineering:SoftwareEngineeringinPractice(ICSE-SEIP).
Automaticfailureclassificationiscriticaltomaintainingtherelia-
338–347.
bilityofmicroservicesystems.Inthiswork,weproposeAgileMFC, [13] FengruiLiu,YangWang,ZhenyuLi,RuiRen,HongtaoGuan,XianYu,Xiaofan
a novel framework that flexibly combines the deep features of Chen,andGaogangXie.2022. MicroCBR:Case-BasedReasoningonSpatio-
temporalFaultKnowledgeGraphforMicroservicesTroubleshooting.InInterna-
multi-modalmonitoringdataformicroservicefailureclassification. tionalConferenceonCase-BasedReasoning(ICCBR).224–239.
Indesign,itnovellyadoptsamodality-awarerepresentationnet- [14] DominikScheinert,AlexanderAcker,LauritzThamsen,MorganKGeldenhuys,
andOdejKao.2021.Learningdependenciesindistributedcloudapplicationsto
workthatbothindependentlyextractsdifferentialexpertiseand
identifyandlocalizeanomalies.InProc.of2021IEEE/ACMInternationalWorkshop
jointlycombinesthemtowardsevent-wisefeatures.Thesplitand onCloudIntelligence(CloudIntelligence).7–12.
mergedesignallowsthismoduletoretainthefailuresensitivity [15] BikashSharma,PraveenJayachandran,AkshatVerma,andChitaRDas.2013.
CloudPD:Problemdeterminationanddiagnosisinshareddynamicclouds.InProc.
ofeventswithdifferentmodalities.Italsoprovidesatwo-stage
of201343rdAnnualIEEE/IFIPInternationalConferenceonDependableSystemsand
trainingmechanismforlearningtherepresentationandclassifica- Networks(DSN).1–12.
tionindependently.Experimentsonthreedatasetsdemonstratethe [16] YichengSui,YuzheZhang,JianjunSun,TingXu,ShenglinZhang,Zhengdan
Li,YongqianSun,FangruiGuo,JunyuShen,YuzhiZhang,etal.2023. LogKG:
effectivenessofdifferentcomponentsofAgileMFCandshowthat LogFailureDiagnosisthroughKnowledgeGraph.IEEETransactionsonServices
itoutperformsfourbaselinesinallthetestcases. Computing(TSC)(2023).
[17] YongqianSun,BinpengShi,MingyuMao,MinghuaMa,SiboXia,ShenglinZhang,
andDanPei.2024.ART:AUnifiedUnsupervisedFrameworkforIncidentManage-
Acknowledgments mentinMicroserviceSystems.InProceedingsofthe39thIEEE/ACMInternational
ConferenceonAutomatedSoftwareEngineering.1183–1194.
ThisworkissupportedbytheScienceandTechnologyInnova- [18] AVaswani.2017. Attentionisallyouneed. AdvancesinNeuralInformation
ProcessingSystems(2017).
tion Program of Hunan Province under Grant 2023RC3027 and
[19] RuiboWang,KaiLu,JuanChen,WenzheZhang,JinwenLi,YuanYuan,Pingjing
2023RC3139,theGraduateResearchInnovationProjectofHunan Lu,LiboHuang,ShengguoLi,andXiaokangFan.2021. Briefintroductionof
ProvinceunderGrantCX20230912,theNationalNaturalScience TianHeexascaleprototypesystem.TsinghuaScienceandTechnology26,3(2021),
361–369.
FoundationofChinaunderGrant62272062,andtheNaturalScience [20] CanhuaWu,NengwenZhao,LixinWang,XiaoqinYang,ShiningLi,MingZhang,
FoundationofHunanProvinceunderGrant2025JJ50373. XingJin,XidaoWen,XiaohuiNie,WenchiZhang,etal.2021.Identifyingroot-
causemetricsforincidentdiagnosisinonlineservicesystems.In2021IEEE32nd
InternationalSymposiumonSoftwareReliabilityEngineering(ISSRE).91–102.
References [21] YuxiaXie,KaiYang,andPanLuo.2021.Logm:Loganalysisformultiplecompo-
nentsofhadoopplatform.IEEEAccess9(2021),73522–73532.
[1] YangCai,BiaoHan,JinshuSu,andXiaoyanWang.2021.Tracemodel:Anauto- [22] DongYoungYoon,NingNiu,andBarzanMozafari.2016.Dbsherlock:Aperfor-
maticanomalydetectionandrootcauselocalizationframeworkformicroservice mancediagnostictoolfortransactionaldatabases.InProc.ofthe2016international
systems.InProc.of17thInternationalConferenceonMobility,SensingandNet- conferenceonmanagementofdata.1599–1614.
working(MSN).512–519. [23] YueYuan,WenchangShi,BinLiang,andBoQin.2019.Anapproachtocloud
[2] YuhuaChen,DongqiXu,NingjiangChen,andXuWu.2023. FRL-MFPG: executionfailurediagnosisbasedonexceptionlogsinopenstack.InProc.ofthe
Propagation-awarefaultrootcauselocationformicroserviceintelligentoperation 12thInternationalConferenceonCloudComputing(CLOUD).124–131.
andmaintenance.InformationandSoftwareTechnology153(2023),107083. [24] ShenglinZhang,PengxiangJin,ZihanLin,YongqianSun,BichengZhang,Sibo
[3] MinDu,FeifeiLi,GuinengZheng,andVivekSrikumar.2017.Deeplog:Anomaly Xia,ZhengdanLi,ZhenyuZhong,MinghuaMa,WaJin,etal.2023.Robustfailure
detectionanddiagnosisfromsystemlogsthroughdeeplearning.InProc.ofthe diagnosisofmicroservicesystemthroughmultimodaldata.IEEETransactionson
2017ACMSIGSACconferenceoncomputerandcommunicationssecurity.1285– ServicesComputing(TSC)16,6(2023),3851–3864.
1298. [25] ShenglinZhang,SiboXia,WenzhaoFan,BinpengShi,XiaoXiong,ZhenyuZhong,
[4] YuGan,YanqiZhang,DailunCheng,AnkithaShetty,PriyalRathi,NayanKatarki, MinghuaMa,YongqianSun,andDanPei.2024.FailureDiagnosisinMicroservice
ArianaBruno,JustinHu,BrianRitchken,BrendonJackson,etal.2019. An Systems:AComprehensiveSurveyandAnalysis.arXivpreprintarXiv:2407.01710
open-sourcebenchmarksuiteformicroservicesandtheirhardware-software (2024).
implicationsforcloud&edgesystems.InProc.ofthe24thInternationalConference [26] YingyingZhang,ZhengxiongGuan,HuajieQian,LeiliXu,HengboLiu,Qingsong
onArchitecturalSupportforProgrammingLanguagesandOperatingSystems.3–18. Wen,LiangSun,JunweiJiang,LuntingFan,andMinKe.2021.CloudRCA:Aroot
[5] XiaofengGuo,XinPeng,HanzhangWang,WanxueLi,HuaiJiang,DanDing, causeanalysisframeworkforcloudcomputingplatforms.InProc.ofthe30th
TaoXie,andLiangfeiSu.2020. Graph-basedtraceanalysisformicroservice ACMInternationalConferenceonInformation&KnowledgeManagement(CIKM).
architectureunderstandingandproblemdiagnosis.InProceedingsofthe28th 4373–4382.
ACMJointMeetingonEuropeanSoftwareEngineeringConferenceandSymposium [27] NaZhao,BiaoHan,RuidongLi,JinshuSu,andCongZhou.2023.AMultivariate
ontheFoundationsofSoftwareEngineering.1387–1397. KPIsAnomalyDetectionFrameworkWithDynamicBalancingLossTraining.
[6] PinjiaHe,JiemingZhu,ZibinZheng,andMichaelRLyu.2017.Drain:Anonline IEEETransactionsonNetworkandServiceManagement20,2(2023),1418–1429.
logparsingapproachwithfixeddepthtree.InProc.ofIEEEinternationalconference [28] XiangZhou,XinPeng,TaoXie,JunSun,ChenjieXu,ChaoJi,andWenyunZhao.
onwebservices(ICWS).33–40. 2018.Benchmarkingmicroservicesystemsforsoftwareengineeringresearch.
[7] DiederikPKingmaandJimmyBa.2014.Adam:Amethodforstochasticopti- InProc.ofthe40thInternationalConferenceonSoftwareEngineering:Companion
mization.arXivpreprintarXiv:1412.6980(2014). Proceedings(ICSE-Companion).323–324.
[8] CherylLee,TianyiYang,ZhuangbinChen,YuxinSu,andMichaelRLyu.2023.
Eadro:Anend-to-endtroubleshootingframeworkformicroservicesonmulti-
sourcedata.InProc.ofIEEE/ACM45thInternationalConferenceonSoftware
Engineering(ICSE).1750–1762.
577