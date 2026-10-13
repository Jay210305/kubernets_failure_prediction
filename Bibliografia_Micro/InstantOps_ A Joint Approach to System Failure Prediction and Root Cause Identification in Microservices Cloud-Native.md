InstantOps: A Joint Approach to System Failure Prediction and
| Root Cause | Identification |     | in Microservices | Cloud-Native |
| ---------- | -------------- | --- | ---------------- | ------------ |
Applications
| RaphaelRouf          |     | MohammadrezaRasolroveicy |                 | MarinLitoiu      |
| -------------------- | --- | ------------------------ | --------------- | ---------------- |
| raphaelr@my.yorku.ca |     |                          | roveicy@ibm.com | mlitoiu@yorku.ca |
| YorkUniversity       |     |                          | IBMCanadaLab    | YorkUniversity   |
Toronto,Ontario,Canada Markham,Ontario,Canada Toronto,Ontario,Canada
| SeemaNagar |     | PrateetiMohapatra |     | PranjalGupta |
| ---------- | --- | ----------------- | --- | ------------ |
senagar3@in.ibm.com pramoh01@in.ibm.com Pranjal.Gupta2@ibm.com
| IBMResearch     |     |     | IBMResearch     | IBMResearch     |
| --------------- | --- | --- | --------------- | --------------- |
| Bangalore,India |     |     | Bangalore,India | Bangalore,India |
IanWatts
ifwatts@ca.ibm.com
IBMCanadaLab
Markham,Ontario,Canada
| ABSTRACT |     |     | CCSCONCEPTS |     |
| -------- | --- | --- | ----------- | --- |
Asmicroserviceandcloudcomputingoperationsincreasinglyadopt •Computingmethodologies→Distributedcomputingmethod-
automation,theimportanceofmodelsforfosteringresilientand ologies;Featureselection;Regularization;•Informationsys-
efficientadaptivearchitecturesbecomesparamount.Thispaper tems→Clustering;•Networks→Networkperformanceanaly-
| presentsInstantOps,anovelapproachtosystemfailurepredic- |     |     | sis. |     |
| ------------------------------------------------------- | --- | --- | ---- | --- |
tionandrootcauseanalysisleveragingathree-foldmodalityofIT
| observabilitydata:logs,metrics,andtraces.Theproposedmethod- |     |     | KEYWORDS |     |
| ----------------------------------------------------------- | --- | --- | -------- | --- |
ologyintegratesGraphNeuralNetworks(GNN)tocapturespatial CloudComputing,AnomalyPrediction,ResourceOverload,Ma-
informationandGatedRecurrentUnits(GRU)toencapsulatethe chineLearning,RootCauseAnalysis
temporalaspectswithinthedata.Akeyemphasisliesinutilizinga
ACMReferenceFormat:
stitchedrepresentationderivedfromlogs,microservicesevents(e.g.
RaphaelRouf,MohammadrezaRasolroveicy,MarinLitoiu,SeemaNagar,
ImagePullBackOff,PVCPending),andresourcemetricstopredict
PrateetiMohapatra,PranjalGupta,andIanWatts.2024.InstantOps:AJoint
systemfailuresproactively.Thetracesareaggregatedtoconstruct
ApproachtoSystemFailurePredictionandRootCauseIdentificationinMi-
acomprehensiveservicecallflowgraphandrepresentedasady- croservicesCloud-NativeApplications.InProceedingsofthe15thACM/SPEC
namicgraph.Furthermore,permutationtestingisappliedtoharness InternationalConferenceonPerformanceEngineering(ICPE’24),May7–
nodescores,aidingintheidentificationofrootcausesbehindthese 11,2024,London,UnitedKingdom.ACM,NewYork,NY,USA,11pages.
| failures.                 |                               |     | https://doi.org/10.1145/3629526.3645047 |     |
| ------------------------- | ----------------------------- | --- | --------------------------------------- | --- |
| Toevaluatetheefficiencyof | InstantOps,weutilizedin-house |     |                                         |     |
1 INTRODUCTION
datafromtheopen-sourceapplicationQuoteoftheDay(QoTD)as
wellastwopubliclyavailabledatasets,MicroSSandTrainTicket. Withthegrowinguseofcloudcomputing,enhancedsystemsta-
TheF1scoresobtainedinpredictingthesystemfailuresfromthese bilityandreliabilityhavebecomecriticalduetoincreaseddepen-
datasetswere0.96,0.98,and0.97,respectively,beatingthestate- denceoncloudserversfordatastorageandprocessing.Anomalies–
of-the-art.Additionally,wefurtherevaluatedtheefficiencyofroot unusualdeviationsfromexpectedsystembehavior,cansignifypo-
causeanalysisusingMARandMFR.Theseresultsalsooutperform tentialsecuritybreachesormalfunctions,posingriskstosystem
thestateoftheart. availabilityandintegrity[2,13].AnomalyDetectionandprediction
arecrucialinserverandcloudenvironmentsfortheimmediateiden-
tificationofabnormalactivities,therebypreventingtheseissues
fromescalatingintoseriousproblems[7,35].
Theautomaticdetectionandpredictionofanomaliesandfail-
uresinmicroserviceapplicationshavegarneredsignificantinterest
ThisworkislicensedunderaCreativeCommonsAttribution
International4.0License. amongresearchersinrecentyears.Historically,anomalydetection
hasbeenafocusofextensivestudy.Techniquessuchasstatistical
ICPE’24,May7–11,2024,London,UK methods,clustering,andrule-basedsystemshavebeenemployed
©2024Copyrightheldbytheowner/author(s). forthispurpose[1,5,9,11,12,24,25,28].However,asmodern
ACMISBN979-8-4007-0444-4/24/05.
https://doi.org/10.1145/3629526.3645047 systemshavebecomemoreinterconnectedandintricate,therehas
119

ICPE’24,May7–11,2024,London,UK RaphaelRoufetal.
beenapalpableshifttowardsleveragingmachinelearningmodels dependencygraphthatdelineatestheinterconnectionsamongser-
to achieve enhanced efficiency and accuracy in anomaly detec- vices—whereinnodesrepresentservicesandtheirinteractionsare
tion[6,7,18,26]. depictedasedges.
Togainaholisticperspectiveofthesystem’shealth,research Moreover,weenrichthisdependencygraphbymergingboth
hasparticularlyemphasizedvarioussingle-modaldatasources: logsandresourcemetricsasattributesassignedtoitsnodes.This
Tracesin[16,32,38]:Tracesofferinsightsintotheflowofre- augmentationenhancestherepresentationofthesystem’sspatial
questsandtheinteractionsamongdifferentmicroservices.Anom- features at specific points in time. To analyze and comprehend
aliesintraces,suchasunexpectedlatenciesorfailedrequests,can thesespatialfeatures,weemployGraphNeuralNetworks(GNN),
berevealing.Forinstance,adeviationfromausual10-millisecond recognizingthatasystem’sfailureisn’tasingle-pointoccurrence
responsetimetoafullsecondindicatespotentialconcerns. butalifecyclethatgraduallyprogressestowardasystemcrash.
Logsin[4,8,23,29]:Logs,thetextualrecordsgeneratedbyap- Understandingthetemporalevolutionofthesespatialfeaturesis
plicationsandinfrastructurecomponents,provideacomprehensive imperative.Toaddressthis,weutilizeGatedRecurrentUnit(GRU)
contextaboutevents,errors,andwarnings.Asurgeinerrormes- models,acknowledgingtheimportanceofcapturingthesystem’s
sagesoremergentwarningpatternsthatdeviatefromthestandard changingdynamicsovertime.
canpinpointanomalies. Ourfocusliesnotonlyintrainingamulti-modalGNN-GRU
ResourceandPerformanceMetricsin[19,21,27,33]:Monitoring modelforpredictingsystemfailuresbutalsoinutilizingthelearned
variousmetrics,includingCPUusage,memoryallocation,network nodescorestolocalizetherootcause.Thisapproachallowsusto
activity,responsetime,andthroughput,offerspivotalinsightsinto repurpose the trained model for the specific task of root cause
thesystem’sperformanceandhealth.Unforeseenspikes,drops,or analysis.Byleveragingtheinsightsgainedfromfailureprediction,
inconsistenciesinthesemetricsmightbeindicativeofperformance particularlythenodescores,weaimtoguidetherootcauseanalysis
bottlenecks,inefficiencies,orotherhealth-relatedconcernswithin process.Webelievethatthepredictivelearningcapturedinfailure
aservice. predictioncansignificantlyaidinrootcauselocalization,thereby
However,recentstudies[14,15,36]suggestthatrelyingsolely aligningourmethodologiesforamorecomprehensiveunderstand-
onsingle-modaldataforfailurelocalizationmaynotbeadequately ingofsystembehaviorandfailureanalysis.
efficient.Oneprimaryreasonisthatasinglefailurecanhavecascad- Thecontributionsofthispapercanbesummarizedasfollows:
ingeffectsonmultiplefacetsofmicroservices.Suchafailuremight
manifestitselfinvariousmodalities,leadingtomultipleanomaly
patterns.Forinstance,adatabaseslowdownmightresultinboth • Novel System Failure Prediction: We introduce a unique
extendedresponsetimes(observableintraces)andasurgeinerror approachtopredictsystemfailuresbyfusingmultimodal
logs. observabilitydatainanovelfashionwhereinweoverlay
Furthermore,thereexistcertainfailuresthatmightnotbeevident thelogsandmetricsdataasnodeattributesinthegraph
inspecificmodalities.Ifdetectionmethodsrelysolelyononemodal- constructedusingthetraces.
ity,theyriskmissingoutontheseanomalies.Aclassicexample • Weproposetocapturebothtemporalandspatialaspectsin
mightbeaninternallogicerrorinaservicethatdoesn’tnecessarily effectivefailureprediction.
resultinincreasedresourceusageorevidenttraceanomaliesbut • InnovativeRootCauseAnalysisMethod:Weusethemulti-
couldstillproduceerroneousoutputs. modalsystemfailurepredictionmodelforpinpointingthe
Giventhesecomplexities,there’sagrowingconsensusinthe rootcausesoffailuresatthenodelevel.
researchcommunityaboutthenecessityofamulti-modalapproach, • ComprehensiveExperimentalStudy:Weconductanexten-
combiningdatafromvarioussourcestocreateaholisticandmore siveexperimentalanalysistoevaluatetheefficiencyofour
accuratepictureoftheapplication’shealth. modelintermsofbothpredictionaccuracyandrootcause
Inthispaper,throughtheintroductionof InstantOps,weaug- analysis.Thisassessmentisbasedontwoopen-sourceand
menttheexistingstate-of-the-artresearch[14–16,34,36]byfusing oneproprietarydatasetderivedfromopen-sourcemicroser-
multimodaldatasourceincludinglogs,traces,resourcemetrics,and vicesystems.
microservicesevents(e.g.ImagePullBackOff,PVCpending)ina
timeseriesformattopredictsystemfailuresattheservice(node)
level.Inthispaper,wecharacterizea‘node’asanindividualservice Theremainderofthepaperisorganizedasfollows:Section2
withinthemicro-servicearchitecture.Specifically,ourobjectiveis describes the motivation behind our experiments and study. In
topredict,identify,andlocalizethenodesinthesystemthatmight Section3,wediscussrecentrelatedworksinfailurepredictionsand
beresponsibleforimminentsystemfailures.Bypinpointingand anomalydetectioninmicroservices,specificallyfocusingonthe
localizingtheproblematicnodewithinthemicroservicearchitec- useofmultimodaldatasets.Section4detailsourmethodologyand
ture,wecanstrategizeappropriateremediationmeasures,suchas elaboratesonourGNN-GRUbasedalgorithmfordetectingfailures
nodescalingorresourceconfiguration. inmicroservices.Section5delvesintoourapproachtotemporal
Westitchthemulti-modaldataforatimewindowinanovel failurepredictionandrootcauseanalysisincludinganexplanation
fashion, where traces act as a thread. We serialize logs, traces, ofthealgorithms.InSection6,wediscusstheevaluationofour
andmetricsforeachtimewindow.Inthisprocess,weintertwine experimentalstudy.Section7addressesthepotentialthreatsto
tracesasthestitchingthread,serializinglogs,andmetricsforeach validity.Finally,inSection8,weconcludeourfindingsandpresent
timewindow.Thisserializeddataaidsinconstructingadynamic potentialavenuesforfutureresearch.
120

InstantOps:AJointApproachtoSystemFailurePredictionandRootCauseIdentificationinMicroservicesCloud-NativeApplications ICPE’24,May7–11,2024,London,UK
2 MOTIVATION: Li et al. [16] proposed TraceRCA, a root cause microservice
Theanalysisofsystemfailuresnecessitatesathoroughexamina- localizationapproachdesignedfortraceanomalydetectionand
tionofdiversedatamodalities.Priorresearchindicatesthatrelying flaggingabnormaltracestopredicttherootcause.Zhouetal.[38]
solelyonsingle-modaldataisinadequateforcapturingtheintri- presentedMEPFL,amodeldesignedtopredictlatenterrorsthat
caciesoffailurepatterns,especiallyinmicroserviceapplications. possessthepotentialtoprecipitatefailures,especiallyduringthe
Inthispaper,weutilizethreedistinctdatasets:Anafusion’sMi- runtimeinproductionenvironmentsofmicroserviceapplications.
croSS[36],TraceRCA’sTrainTicket[16],andanin-housedataset Thisapproachisrealizedthroughthecomprehensiveanalysisof
forthe“QuoteoftheDay(QOTD)"open-sourceapplication.These systemtracelogsandthetrainingofpredictionmodelsutilizingfea-
datasetscomprisedifferentcombinationsoflogs,traces,events, turesdistilledfromtheselogs.Inessence,MEPFLaimstoempower
andmetrics,dependingonthespecificexperiment.Forinstance, developersbyprovidingthemwiththecapacitytoidentifyand
theQOTDdatasetincorporateslogs,traces,events,andresource rectifyfaultsbeforetheirmanifestationasfailuresinaproduction
metrics,whiletheTrainTicketdatasetemphasizestracesandmet- setting.Themodelspecificallyaddressesthreepredominanttypes
rics.Toensureacomprehensiveevaluation,alldatasetsencompass offaultsinmicroserviceapplications:systemoverload,memory
recordsofeveryfailureinjection.Ourprimaryobjectiveistodeter- leak,andsuddennodecrash.Thesefaulttypesconstitutenearly
minetheprecisionofsystemfailurepredictionswhenleveraging halfofallmicroserviceapplicationfaults,substantiatedbyexisting
supervisedlearning.Distinctlyfrompreviousmodels,weincorpo- empiricalstudies,underscoringthepivotalroleandapplicabilityof
rateedgesintothesystemtosystematicallyassesstheimpacton MEPFLinfortifyingthereliabilityofmicroserviceapplications.The
specificnodes.Furthermore,inthispaper,theedgesareconstructed TraceRCAandMEPFLapproachesaredesignedtotakenotonly
bythecommunicationsamongtheservicesinthemicroserviceap- accounttracesbutmetrics,logs,andeventsusingedgeinteractions
plication. ofthenodestolocalizethefaultsattheservicelevel.
Theanalysisoftheseinteractionsofferscriticalinsightsinto Leeetal.[15]introducedanovelapproachnamedHades,de-
whichnodesrequireinterventions,suchasscaling,restarting,or signedfordetectingsystemanomaliesinsoftwaresystems.Hades
remediationofvariousfailures. seamlesslyintegratesheterogeneousdatasources,includinglogs
Forsystemfailureprediction,multipleneuralnetworkmodels andmetrics,toproficientlyidentifysystemanomalies.Theseanom-
aretestedtoascertainthemostefficientpredictivemethodology. alies,whichencompasssystemfailures,performancedegradation,
Theeffectivenessof InstantOpsissubsequentlyquantifiedusing andotherunanticipatedbehaviors,aredetectedpromptly,thereby
metricsincludingaccuracy,precision,recall,andtheF1Score.To enablingsystemadministratorstoenactcorrectiveactionsswiftly.
benchmarkitsperformance,InstantOpsiscomparedagainsttwo Tofacilitatethepredictionofsystemanomalies,theauthorsemploy
establishedmethods,AnafusionandTraceRCA. abinaryclassificationapproach,whereineachdatachunkislabeled
aseither’normal’or’anomalous.’Leeetal.[14]proposedEadro,
anapproachforanomalydetectionwithinmicroservices.Eadro
operatesbymodelingthestandardbehaviorofmicroservicesand
3 RELATEDWORKS identifyingdeviationsfromthisestablishednormalcy.Specifically,
Recentworkshavesignificantlyleanedintoexploringmethodsfor itemploysadeepneuralnetworktoderivediscriminativerepre-
anomalyandfailuredetectionwithinmicroservicesandcloudap- sentationsofmicroservicestatusesthroughmulti-modallearning,
plications,leveragingvariousdata-orientedandmachine-learning compellingthemodeltoapprehendfundamentalfeaturesindica-
approaches. tiveofanomaliesthroughmulti-tasklearning.Themodel,which
Zhaoetal.[36]proposedanovelapproachcalledAnoFusion ingestsmulti-sourcemonitoringdata—includingtraces,logs,and
forunsupervisedfailuredetectionthroughmultimodaldatafor KeyPerformanceIndicators(KPIs)—generatesascoreforeachmi-
microservicesystems.AnoFusionusesGTNtolearnthecorrelation croservice,reflectingthelikelihoodofananomaly.Ahigherscore
oftheheterogeneousmultimodaldataandconstructsaheteroge- indicatesagreaterprobabilityofthemicroserviceencounteringan
neousgraphstructure.Then,GATisutilizedtocapturesignificant anomaly.Eadro’sanomalydetectionmoduleiscapableofidenti-
featuresandupdatetheheterogeneousgraph.Finally,GRUisused fyingvarioustypesofanomalies,suchasnetwork-relatedissues,
topredictthedatapatternatthenextmoment.However,while resourceexhaustion,andsoftwarebugs.Bypinpointingtheroot
AnoFusionlooksatthesystemleveltopredictthefailuresofthe causesofanomalies,Eadroassistssystemadministratorsanddevel-
microservice,wefocusourattentionontheserviceleveltolocalise opersinpromptlytroubleshootingandaddressingissues.Research
whichnodesaretheleadingcauseinpredictingthesystemfailures workssimilartoHadesandEardoaimtodetectsystemanomalies
andtakethatintoaccountinoursystemfailureprediction.InAna- andfailure,ourintentionisnottodetectsystemanomaliesbutto
fusion,theauthorsmodelonenode,inthispaper,wemodelthe predicttheanomaliesatthenextminutebasedonthelast5minute
entiremicroserviceapplication.Furthermore,ourmodelisbuilt timewindow.
withmultipledatasourcessuchaseventsfromeachmicroservices.
Zhangetal.[34]proposedanalternativemethodknownasDi-
agFusion. This approach leverages multimodal data to enhance 4 METHODOLOGY
faultdetectionbyemployingadvancedembeddingtechniquesfast- Inthissection,weprovideasystematicapproachdesignedtopre-
Textanddataaugmentation.Itconstructsadependencygraphand dictsystemfailuresandfacilitatesubsequentrootcauseanalysis
employsagraphneuralnetworktopinpointtherootcauseand usingGraphNeuralNetworks(GNNs)inaMicroserviceapplication.
identifythetypeoffailure. Weinitiatewiththestandardizationoffeaturesandthenproceed
121

ICPE’24,May7–11,2024,London,UK RaphaelRoufetal.
Figure1:InstantOpsOfflineTrainingModel
tothesystematicconstructionofagraph.Inthisrepresentation, First,wepreprocessandserializethemulti-modaldata-setwithin
nodessymbolizesystemcomponents,whileedgescorrespondto acontrolledtime-frame.Foreachdatasource,wedefinetimewin-
theinteractionsbetweenthesecomponents,quantifiedonaper- dowswiththesamesize.Thesequenceofthetimewindowsdefines
minutebasis.Toquantifythefrequencyoftheseinteractions,we thestreamofgraphsforourmodel.Next,weconstructtheGraph
incorporatetheconceptof‘weights’. NeuralNetworksusingedgesandnodes.Foreachtimewindow,we
Whenaninteractionbetweenorservicesisobservedforthefirst addthefeaturestothenodesinthegraph.ThelayersoftheGNN
timewithinaspecifiedduration,wecreateanedgebetweenthetwo aggregateinformationfromneighborsinagraph.Wethenfilter
correspondingnodesinGNN,andtheweightoftheedgesis1.Ifan featuresbyselectingimportantkeywordsfromlogsandeventsthat
edgebetweenthesenodesalreadyexistswithinthistimeframe,its serveasfeaturesandcorrelatingthemwithresourcemetrics.The
weightisincrementedby1,markinganadditionalrecordedinter- firstlayertakesthefeatures,whilethesecondlayeracceptsthe
action.Essentially,thisweightservesasametric,representingthe outputfromthefirstandproducesadditionalgraphneuralnetwork
numberofinteractionsbetweentwonodeswithinthedesignated features.
interval.Forexample,iftheweightofanedgebetweennodeAand AfterprocessingthenodefeatureswiththeGNNlayers,thenode
nodeBis10,itindicatesthatServiceAinteractedwithServiceB embeddingsarefurtherrefinedthroughaGRUcell.Forfailurepre-
10timeswithinthespecifiedobservationperiod. diction,weconsiderboththefeaturesandtemporalaspectsacross
Further,aGNNmodelisdeveloped,integratingnodefeature differenttimestampstopredictsystemfailuresinthesubsequent
information and graph topology to generate node embeddings. timemoment,whichinourcaseis𝑡 +1.Thislayercancapture
Themathematicalframeworkdefinestheforwardpropagationand temporaldependenciesinthenodeembeddingsproducedbythe
convolutionoperationswithintheGNNandGraphConvolutional GNNlayers.WhileGRUmodelsaretraditionallyusedforsequence
Network(GCN)layers.Additionally,themodelisextendedtoincor- data,inourapproach,weuseitasanadditionaltransformationfor
porateedgefeatures,enhancingtherepresentationofinteractions. nodeembeddings.
Temporalaspectsanddependenciesofthesystemareincorporated Wefurtherelaborateonourstepsbelow:
byusingaGatedRecurrentUnit(GRU)model.Duringthetrain-
ingphase,thecross-entropylossfunctionisemployedtooptimize 4.1 DataPreprocessingandGraphConstruction
modelparameterstominimizethedifferencebetweenpredicted
Datanormalizationisconductedtomaintainconsistencyamong
outputsandactuallabels.Wepredictsystemfailurewhentheentire
thedatasetfeatures,expressedmathematicallyas:
applicationcrashesoriftheapplicationreceives500errorsmore
p
th
r
a
e
n
di
9
ct
9
i
%
ve
o
a
f
c
t
c
h
u
e
r
t
a
i
c
m
y,
e
a
in
qu
th
a
e
nt
𝑡
ifi
+
a
1
bl
t
e
im
m
e
e
w
tri
i
c
nd
th
o
a
w
t
s
m
.F
e
i
a
n
s
a
u
l
r
ly
e
,
s
t
t
h
h
e
e
m
pr
o
o
d
p
e
o
l’
r
s
-
𝑥 std=
𝑥
𝜎
−𝜇
tionofcorrectpredictionsrelativetothetotal,isusedtoevaluate where𝑥 istherawfeature,𝜇 isthemean,and𝜎 isthestandard
itsabilitytopredictsystemfailuresandenablerootcauseanalysis. deviationofthefeatureacrossalldatapoints.
AsshowninFigure1,theworkflowof InstantOpsisdivided Agraph𝐺isthendefinedas𝐺 =(𝑉,𝐸),where𝑉 isasetofnodes
intomultiplestages: representingmicroservices,and𝐸 isasetofedgesrepresenting
122

InstantOps:AJointApproachtoSystemFailurePredictionandRootCauseIdentificationinMicroservicesCloud-NativeApplications ICPE’24,May7–11,2024,London,UK
| interactionsbetweenservices.Theadjacencymatrix𝐴 |     |     |     |     |              | ∈ R𝑛×𝑛 | expressedas: |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | ------------ | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
| encapsulatesthenumberofinteractions,where𝐴      |     |     |     |     | =1ifaninter- |        |              |     |     |     |     |     |     |     |
𝑖𝑗
| a c ti o n e xi | s t s b et w | ee n se r v | i c e s r e p r e se | n t e d b y n o | d e s 𝑣 a nd | 𝑣 , a n d |     |     |     |                    |           |      |                  |     |
| --------------- | ------------ | ----------- | -------------------- | --------------- | ------------ | --------- | --- | --- | --- | ------------------ | --------- | ---- | ---------------- | --- |
|                 |              |             |                      |                 | 𝑖            | 𝑗         |     |     | ℎ   | (𝑙 +1) =𝜎(cid:169) | ∑︁        | 𝑊(𝑙) | ·ℎ (𝑙 )(cid:170) |     |
|                 |              |             |                      |                 |              |           |     |     |     | 𝑣                  | (cid:173) |      | 𝑣 (cid:174)      |     |
0 o t h er w i s e . In o th e rp a p e r , a u t h o r s d e fi n e E d g e s 𝑒 𝑖𝑗 ∈ 𝐸 ca n a l so 𝑖 𝑗
𝑣𝑗∈𝑁(𝑣𝑖)
| bedefinedbasedonmetricsbetweennodes: |     |           |          |     |     |     |           |                              |                                   |     | (cid:171) |     | (cid:172) |              |
| ------------------------------------ | --- | --------- | -------- | --- | --- | --- | --------- | ---------------------------- | --------------------------------- | --- | --------- | --- | --------- | ------------ |
|                                      |     |           |          |     |     |     | whereℎ(𝑙) |                              | representsthefeaturevectorofnode𝑣 |     |           |     |           | atlayer𝑙 and |
|                                      |     | 𝑒 =𝑓(logs | ,metrics | 𝑖𝑗) |     |     |           | 𝑣𝑖                           |                                   |     |           |     |           | 𝑖            |
|                                      |     | 𝑖𝑗        | 𝑖𝑗       |     |     |     |           |                              |                                   |     |           |     |           |              |
|                                      |     |           |          |     |     |     | 𝑁(𝑣       | 𝑖)isthesetofneighborsofnode𝑣 |                                   |     |           | 𝑖 . |           |              |
where𝑓 representsafunctiondetermininginteractionsbetween
TheoperationinaGraphConvolutionalNetwork(GCN)layer
| nodesbasedonlogsandmetrics. |     |     |     |     |     |     | canbeexpressedas: |     |        |     |                |                  |     |          |
| --------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | --- | -------------- | ---------------- | --- | -------- |
|                             |     |     |     |     |     |     |                   |     | 𝐻(𝑙+1) |     | (cid:16) 𝐷˜− 1 | 𝐴˜𝐷˜− 1 𝐻(𝑙)𝑊(𝑙) |     | (cid:17) |
| 4.2 LogParsing              |     |     |     |     |     |     |                   |     |        | =𝜎  | 2              | 2                |     |          |
Topredictsystemfailureandtheirrespectivecauses,serialization where𝐴˜ and𝐷˜ isthedegreematrixof𝐴˜.
=𝐴+𝐼
ofthelogsisanintegralpartofourwork.Thearchitecturaldesign
EnhancingtheGCNmodeltoincludeedgefeatures,thenode
| of this project | is  | inspired | by our previous | work, | BERTOps | [8], |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | --------------- | ----- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
representationbecomes:
whichutilizestheDrain[10]toextractstructuredinformationfrom
rawlogdatabyclusteringloglinesintotemplatesbasedontheir
|     |     |     |     |     |     |     |     |     | (𝑙 +1) | ∑︁  | 𝑊(𝑙) |     | (𝑙 ) +𝑈(𝑙) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- | ---------- | --- |
structuralsimilarityandBERT[3]forbuildinganencoderbased ℎ 𝑣 =𝜎(cid:169) ·ℎ 𝑣 ·𝑒 𝑖𝑗(cid:170)
|     |     |     |     |     |     |     |     |     | 𝑖   | (cid:173) |     |     | 𝑗   | (cid:174) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- |
LargeLanguageModel(LLMs)forthelogdata.Byfine-tuningthe 𝑣𝑗∈𝑁(𝑣𝑖)
|     |     |     |     |     |     |     |     |     |     | (cid:171) |     |     |     | (cid:172) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- |
pre-trainedBERTOpsmodelonlabeleddatafromdownstreamtasks
|     |     |     |     |     |     |     | where𝑈(𝑙) |     | isatrainableweightmatrixforedgerepresentationsat |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
suchaslogclassificationandfaultcategoryprediction,BERTOps
layer𝑙.
canlearntoaccuratelyrepresentlogdataandperformvariouslog
analysistaskswithhighaccuracy.WhileBertOpsaimstoclassifya
|     |     |     |     |     |     |     | 5   | TEMPORALFAILUREPREDICTIONAND |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
logline,inthispaper,weclassifyeachnodeandextractvitalfeatures
fromthelogs,suchasthenumberoferrorsanodereceiveswithin ROOTCAUSEANALYSIS
the specific time window. For instance, given the log structure Inthissection,wediscusstheapproachesforfailurepredictionand
| “[2023-08-22T17:20:12.083][Error]default-[418241]Quoterequest |     |     |     |     |     |     | rootcauseanalysis. |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
timeout",weextractthefollowingfeatures:timestamp,nodeid,
numberoferrors.Thesefeatureswillbeaddedtothenodesfora 5.1 TemporalFailurePrediction
correspondingtimewindow.
Inourapproach,weintegratethepowerofGraphNeuralNetworks
(GNN)withGatedRecurrentUnits(GRU)topredicttemporalfail-
4.3 GNNModelFormulation ures.TheGNNcapturesthespatialstructureofthedatabyoperat-
LeveragingtheabilityofGNNstocapturelocalizedgraphstruc- ingonagraph,encapsulatinglocalneighborhoodinformationof
turesandenableaccuratepredictions,theformulationandforward eachnodethroughiterativefeatureaggregationfromitsneighbors.
˜
propagationwithinaGNNlayerincludethetransformationand ThepropagationinGNNissteeredbytheadjacencymatrixA and
aggregationofnodefeaturesacrosssuccessivelayers,adheringto: itsdiagonaldegreematrixD ˜,formalizedas:
𝐻(𝑙+1) (cid:16) 𝐷˜−1 2𝐴˜𝐷˜−1 2𝐻(𝑙)𝑊(𝑙) (cid:17) X(𝑙+1) (cid:16) ˜−1 ˜ ˜− 1 X(𝑙)W(𝑙) (cid:17)
|        |     | =𝜎  |     |     |     |     |     |                                                       |     | =𝜎  | D 2A | D 2 |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | ---- | --- | --- | --- |
| where: |     |     |     |     |     |     |     | TheGatedRecurrentUnit(GRU)capturesthetemporaldynamics |     |     |      |     |     |     |
• 𝐻(𝑙) isthematrixofnodefeaturesatlayer𝑙, acrosssequences.TheGRUdiscernssequentialpatternsusingits
𝐴˜ 𝐴+𝐼 includestheadjacencymatrix𝐴fortifiedwith intrinsicupdateandresetgates.Thevitalcomputationswithinthe
• =
GRUinclude:
self-loops𝐼,
𝐷˜ representsthedegreematrixof𝐴˜,
| •                                       |                                 |     |     |     |     |     | 𝑟   | =𝜎(𝑊 | 𝑥 +𝑈 | ℎ 𝑡−1+𝑏 |     |     |     | (Resetgate)  |
| --------------------------------------- | ------------------------------- | --- | --- | --- | --- | --- | --- | ---- | ---- | ------- | --- | --- | --- | ------------ |
|                                         |                                 |     |     |     |     |     | 𝑡   | 𝑟    | 𝑡 𝑟  |         | 𝑟)  |     |     |              |
| • 𝑊(𝑙)                                  | denotestheweightmatrixatlayer𝑙, |     |     |     |     |     |     |      |      |         |     |     |     |              |
|                                         |                                 |     |     |     |     |     | 𝑧   | =𝜎(𝑊 | 𝑥 +𝑈 | ℎ 𝑡−1+𝑏 | 𝑧)  |     |     | (Updategate) |
| 𝜎embodiesanon-linearactivationfunction. |                                 |     |     |     |     |     | 𝑡   | 𝑧    | 𝑡 𝑧  |         |     |     |     |              |
•
|                                                        |     |     |     |     |     |     | ℎˆ  | =tanh(𝑊𝑥 | +𝑈(𝑟 | ⊙ℎ  | 𝑡−1)+𝑏) |     | (Newpotentialhidden |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | ------- | --- | ------------------- | --- |
| ThisstructuralformulationofGNNsimultaneouslyensuresthe |     |     |     |     |     |     | 𝑡   |          | 𝑡    | 𝑡   |         |     |                     |     |
preservationofspatialrelationsbetweennodesandfacilitatesan state)
|     |     |     |     |     |     |     | ℎ   | =(1−𝑧 | 𝑡)⊙ℎ 𝑡−1+𝑧 |     | ⊙ℎˆ |     | (Actualhiddenstate |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | ------------------ | --- |
iterativeenhancementofnoderepresentationsthroughtheaggre- 𝑡 𝑡 𝑡
gationofneighboringinformation.Thismechanismisinstrumental update)
indecodingintricatepatterns,whicharecrucialforthepredictive
Foreachsequenceanditsrespectivetimestep,theGNNfirst
analysisofsystemfailures,andprovidesarobustfoundationfor
imbibesspatialinformationderivedfromthegraph.Theconjoined
subsequentrootcauseanalysis.
featuresfromtheGNNforeverytimesteparesubsequentlyfun-
neledintotheGRU,whichmodifiesitshiddenstateaccordingto
4.4 GraphNeuralNetworkModelDevelopment itsprecedingstateandthecontemporaryinput.Theculminating
TheGNNmodelleveragesbothnodefeatureinformationandtopo- outputoftheGRUformsthebasisoftheprediction.Theassociated
logicalstructure.TheforwardpropagationofaGNNmodelisoften lossiscomputedrelativetothetruelabels,followedbyabackward
123

ICPE’24,May7–11,2024,London,UK RaphaelRoufetal.
passtorefinethemodelparameters.Upontraining,thismodelcan NeuralNetwork(GNN)withaGatedRecurrentUnit(GRU)model.
beemployedtoprognosticatefailuresforimminenttimesteps. TheGNNcomponentisresponsibleforcapturingtheinteractions
amongmicroservicenodes,effectivelylearningfromthetopologi-
Algorithm1TemporalFailurePredictionusingGNNwithGRU
calstructureofthemicroservicesnetwork.EachnodeintheGNN
procedureGNN_TemporalFailurePrediction(nodes,edges, representsamicroservice,andtheedgesreflecttheinteractions
1:
| y)  |     |     |     |     | betweentheseservices. |
| --- | --- | --- | --- | --- | --------------------- |
TheGRUpartofthemodelhandlesthetemporalaspectsofthe
2: Standardizenodes
system’sfeatures,suchasresourceutilizationanderrorrates,which
3: Mapnodenamestointegersinedgesandnodes
arecriticalforunderstandingthestateofthesystemovertime.The
4: Convertnodes,edges,ytodata
InitializeGNN-GRUmodelwith2GCNlayersandaGRU GRU’sabilitytomaintaininformationacrosstimestepsmakesit
5:
layer particularlysuitableforthistask,asitcanrecognizepatternsthat
precedeasystemfailure.
6: foreachepochdo
Thefigureillustratesnodesrepresentingdifferentlayersand
7: foreachtimewindowintrain_loaderdo
operationswithintheneuralnetwork,suchasconvolutionallayers
| 8:  | Gettemporalsequenceofnodesforthetimewindow |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- |
9: foreachtime-step𝑡 (conv1.lin.weight, conv2.lin.weight), which are used in process-
do
X(𝑙+1) (cid:16) ˜−1 ˜ ˜− 1 (cid:17) ingnodesinteractions,andGRUcomponents(gru_cell.weight_ih,
| 10: |     | ←𝜎  | D 2A D 2 X(𝑙)W(𝑙) |     |     |
| --- | --- | --- | ----------------- | --- | --- |
gru_cell.weight_hh),whichareadeptathandlingtemporalaspects.
|     | 𝑟 ←𝜎(𝑊 | 𝑥   | +𝑈 ℎ 𝑡−1+𝑏 |     |     |
| --- | ------ | --- | ---------- | --- | --- |
11: 𝑡 𝑟 𝑡 𝑟 𝑟) TheAccumulateGradnodessuggesttheaccumulationofgradient
12: 𝑧 𝑡 ←𝜎(𝑊 𝑧 𝑥 𝑡 +𝑈 𝑧 ℎ 𝑡−1+𝑏 𝑧) valuesforeachparameteracrossmultiplebatchesortimesteps.
ℎˆ
| 13: | ←tanh(𝑊𝑥 |     | +𝑈(𝑟 ⊙ℎ    | 𝑡−1)+𝑏) |                                                     |
| --- | -------- | --- | ---------- | ------- | --------------------------------------------------- |
|     | 𝑡        |     | 𝑡 𝑡        |         | Inthecomputationalgraphshown,weseethebackwardpropa- |
|     | ℎ ←(1−𝑧  |     | 𝑡)⊙ℎ 𝑡−1+𝑧 | ⊙ℎˆ     |                                                     |
14: 𝑡 𝑡 𝑡 gationflow,whichispartofthetrainingphasewherethemodel’s
15: Useℎ 𝑡 forprediction parametersareadjusted.Thebackwardnodesrepresentthederiva-
16: ComputelosswithCrossEntropy tivesofthelossfunctionwithrespecttothemodel’sparameters,
17: Backwardpass andthearrowsindicatethedirectionofthegradients’flow.
Updatemodelparameters
18:
19: Evaluateonthevalidationset
20: Computemetrics(Accuracy,Precision,Recall,F1Score)
Predictfailurefor𝑡+1usingcurrentmodelstate
21:
22: returnTrainedGNN-GRUmodel
Table1:ConjoinedfeaturesfromtheGNN
| Features            |     | Traces | Metrics | Logs Events |     |
| ------------------- | --- | ------ | ------- | ----------- | --- |
| #ofNodeInteractions |     |        | ✓       |             |     |
| CPUUsage            |     |        | ✓       |             |     |
| MemoryUsage         |     |        | ✓       |             |     |
| DiskI/O             |     |        | ✓       |             |     |
| NetworkI/O          |     |        | ✓       |             |     |
| 5XXErrors           |     |        |         | ✓           |     |
| 2XXRequests         |     |        |         | ✓           |     |
| 4XXErrors           |     |        |         | ✓           |     |
| APILatency          |     |        |         | ✓           |     |
| CrashLoopBackOff    |     |        |         | ✓           |     |
| ImagePullBackOff    |     |        |         | ✓           |     |
| NodeNotReady        |     |        |         | ✓           |     |
| PodScheduled        |     |        |         | ✓           |     |
| NodeReady           |     |        |         | ✓           |     |
| Unhealthy           |     |        |         | ✓           |     |
| VolumeMount         |     |        |         | ✓           |     |
Failed(ImagePull) ✓ Figure2:TheDiagramforGNN+GRUNeuralNetworkModel
| ResourceConstraints |     |     |     | ✓   |     |
| ------------------- | --- | --- | --- | --- | --- |
Figure2depictsthemodelarchitectureofasystemdesignedfor 5.2 RootCauseAnalysis
predictingsystemfailureatthenodelevelinamicroserviceapplica- Incomplexmicroserviceapplications,identifyingtherootcausesof
tion.Thissystememploysahybridapproach,integratingaGraph faultsiscriticalformaintainingoperationalefficiencyandreliability.
124

InstantOps:AJointApproachtoSystemFailurePredictionandRootCauseIdentificationinMicroservicesCloud-NativeApplications ICPE’24,May7–11,2024,London,UK
Tosystematicallyanalyzeanddiagnosefaultsinoursystem,we MicroSS,alsoknownastheGeneticAIOpsAtlas(GAIA)dataset1,
employatwo-foldmetric-basedapproach.Thisapproachfocuses contains10microservices,twodatabases(MYSQLandRedis),and
onevaluatingtheeffectivenessofInstantOpsrootcauselocalization issupportedbyfivehostmachines.Itisdesignedtocatertoboth
processesatthenodelevel.Specifically,weutilizeMeanFirstRank mobileandPCusers.TheGAIAdatasetencompassesfivedistinct
(MFR)andMeanAverageRank(MAR)asourprimarymetrics. faults:systemhang-ups,processcrashes,systemfailureslikelogin
MeanFirstRank(MFR):MFRfocusesonthepositionwhere issues,missingfiles,andaccessdenials.Arecorddetailingthein-
thefirstcorrectitem(fault)appearsinarankedlist.Inthecontext jectionofthesefailuresisprovidedalongsidethedata.Thisdataset
offaultanalysis,thismeansidentifyingthemostlikelyrootcause hasbeenwidelyusedforpredictingsystemfailureandrootcause
ofaproblemasquicklyaspossible.Thequickeraprimaryfaultis localizationin[36]and[34].
identified,thefasterremedialactionscanbetaken.Thisiscrucial TheQoTDopen-sourceapplication3consistsofeightdistinct
insystemswherepromptfaultresolutionisessentialtominimize microservices.WedeployedQoTDonIBMOpenShiftclustersand
downtimeorpreventcascadingissues.Inpractice,MFRiscalculated introducedavarietyoffaultsusingChaos-Mesh4.Thesefaults
byaveragingtheranksatwhichthefirsttruefaultappearsacrossall includedisruptionsinCPU,memory,andDNS.
instancesinadataset.AlowerMFRvalueindicateshigherefficiency Formonitoringpurposes,weemployedInstana5,whichprovided
inpinpointingtheprimaryfaultquickly. datapointssuchasAPIresponsetimes,errorcodes,andvarious
Mean Average Rank (MAR): MAR extends the analysis to resourceutilizationmetrics:CPU,memory,disk,andnetwork.We
considertheaveragerankofallrelevantitemsintherankedlist. utilizedLogDNA6 toextractapplicationlogs.Furthermore,we
Thisisparticularlyimportantinscenarioswheremultiplepotential devisedacustomscripttocaptureeventsperminuteatthenode
faultsmightcontributetoaproblem.MARprovidesabroaderview level.Thisscriptmonitoredeventslike“Scheduled",“Unscheduled",
ofthesystem’sdiagnosticaccuracy.Itisessentialforcomprehensive “Pulled", “Failed", “Started", etc. These events were retrieved by
faultidentification,especiallyincomplexsystemswheremultiple querying‘ocdescribe<resource><resource-name>’.
issuescancoexistorbeinterrelated.MARiscalculatedbyaveraging
theranksofallrelevantfaultsacrosseachinstanceinthedataset. 6.2 EvaluationMetrics
Itinvolvesmoreintricatecomputationsasittakesintoaccountthe 6.2.1 FailurePrediction: ThemodelistrainedusingCrossEntropy
positionofeachrelevantitem,notjustthefirstone. loss,formulatedas:
Toimplementthesemetrics,weutilizedthreedifferentdatasets,
𝑁
eachcomprisingarankedlistofpotentialfaultsforeachnodegen- 1 ∑︁
erateduponthedetectionofafaultinthesystem.Forinstance,in 𝐿=− 𝑁 𝑦 𝑖 log(𝑦ˆ 𝑖)+(1−𝑦 𝑖)log(1−𝑦ˆ 𝑖)
𝑖=1
thecaseoftheQoTDdatasets,weencounteredthreedistinctfaults:
where𝑦 and𝑦ˆ arethetruelabelandpredictedprobabilityfor
CPU,Memory,andDNS.Therankedlistsfromthesedatasetsare 𝑖 𝑖
sample𝑖,respectively.
thenscrutinizedusingtheMFRandMARmetrics,allowingusto
Toassessthemodel,accuracyandF1Scorearecomputed.Accu-
quantifytheaccuracyandefficiencyofourfaultidentificationpro-
racyisgivenas:
cess.Thismethodologyensuresarobustanalysisofthediagnostic
capabilitiesatthenodelevelwithinoursystem. NumberofCorrectPredictions
Accuracy=
TotalNumberofPredictions
F1 Score is calculated using precision and recall, which con-
6 EVALUATION siderthemodel’sperformanceregardingfalsepositivesandfalse
Here,wepresentthedataforevaluation,evaluateourmethodsfor negatives.F1Scoreisexpressedas:
failurepredictionandrootcauseanalysis,andpresenttheperfor- Precision×Recall
manceofthemodelsonvariousdatasetsandbaselines.
𝐹1=2×
Precision+Recall
with
TruePositives
Precision=
6.1 Datasets TruePositives+FalsePositives
Inthispaper,weutilizedtwoopen-sourcemicroservicedatasets: and
TruePositives
Train-TicketandMicroSS,andQuoteoftheDay(QoTD)application Recall=
thatwasdeployedin-houseonIBMOpenShiftClustersV4.12.36
TruePositives+FalseNegatives
with16CPUcores,and32GBRam. 6.2.2 RootCauseAnalysis: Tovalidateandunderstandtheimpact
Train-Ticket[37]whichcomprises41microservices,isfrequently ofcrucialnodesfortherootcause,weemployedafunctionfor
usedbyresearchersforrootcauseidentificationandlocalization. evaluatingtheaccuracywithoutknodes.Thisfunctiondeliberately
WeaccessedthisapplicationmadeavailableonlinebyLietal.,[16] nullifiesthetopknodes(basedontheirimportance)andevaluates
toenablecomparativeanalysiswiththeirfindings.Threetypesof howthemodel’saccuracyisaffectedwithouttheirpresence:
faultswereintroduced[16]:applicationbugs,CPUexhaustion,and
networkcongestion.Whilethesefaultswereintroducedatvarious 12
systemlevels,wespecificallyfocusedonthoseinjectedintothe 3https://gitlab.com/quote-of-the-day/quote-of-the-day/-/tree/master
4https://chaos-mesh.org/
microservices,aligningthemforcomparisonwiththeothertwo
5https://www.ibm.com/products/instana
datasets. 6https://www.ibm.com/case-studies/logdna-cloud
125

ICPE’24,May7–11,2024,London,UK RaphaelRoufetal.
• RankingNodes: Nodesarerankedindescendingorder • RQ3:HowdoesInstantOpsperformrootcauseanalysisas
basedontheircomputedimportance. comparedtootherneuralnetworkalgorithms?
• NullificationofTopNodes:Featuresofthetopknodes • RQ4:HowdoesInstantOpsperformintermsofrootcause
aresettozero,effectivelyremovingtheirinfluencefromthe nodelocalizationcomparedtoexistingmethods?
network.
• ModelEvaluation:Withthesenodesnullified,themodel’s 6.3.1 RQ1:HowefficientisInstantOpsforsystemfailurepredic-
accuracyisgaugedagain,highlightingtheimpactofthese tioncomparedtootherneuralnetworkalgorithms? Toassessthe
efficiencyof InstantOps,threedistinctdatasetswereutilized,as
crucialnodesonthenetwork’soverallperformance.Apro-
showninTable2.Thefirst,MicroSS,isanopen-sourcedataset
nounceddropintheseaccuraciescomparedtothebaseline
comprising419,959data.Thisdatawasdividedintotrainingand
underscoresthecriticalnatureofthesenodeswithinthe
testingsetswith84,026and335,933,respectively.TheTrainTicket
network.
open-sourcedatasetencompasses24,492data,whicharefurther
Top-kaccuracyisametriccommonlyusedinretrievalandrec-
dividedinto19,337fortestingand5,085fortraining.Lastly,ourin-
ommendationtasks.Itmeasureshowoftenthetrueitem(oroneof
housedatasetincludes450,000data,withadistributionof360,000
thetrueitems)appearsinthetop𝑘itemsoftherankedlistandis
fortestingand90,000fortraining.
definedas:
𝐴@𝑘 = 1 ∑︁ (cid:26) 1 if𝑅𝐶 𝑖 𝑎 ∈𝑅𝐶 𝑠 𝑎[𝑘] Table2:DataOverviewforApplications
|𝐴| 0 otherwise
𝑎∈𝐴 Application TotalSamples Test_data train_data
where,
MicroSS 419959 335933 84026
• 𝐴isthesetoftestsamples.
TrainTicket 24492 19337 5085
• 𝑅𝐶𝑎isthetruerootcauseinstanceforsample𝑎.
𝑖 QoTD 450000 360000 90000
• 𝑅𝐶 𝑠 𝑎[𝑘]isthesetoftop-kpredictedinstancesforsample𝑎.
MeanFirstRank(MFR)evaluatestheaveragerankatwhichthe
firstcorrectitemisfoundintherankedlistandisdefinedas: Foreachdataset,severalapplicationsmetricswereconsidered
whichwedefinedasfeatures:applicationresourceutilization,logs
𝑁 detailingerrorsforeachnodewithinspecifictimeframes(e.g.,1
1 ∑︁
MFR= rank 𝑖 minute), edge constructions that link nodes with traces within
𝑁
𝑖=1 certaintimewindows,andthefrequencyofinteractionsbetween
where, nodes.Thesemetricsassistinidentifyinganomaliesbyobserving
• 𝑁 isthetotalnumberofrankedlists. deviationsinstandardnodeinteractions.SpecificallyfortheQoTD
• rank 𝑖 istherankofthefirsttrueiteminthe𝑖𝑡ℎ rankedlist. dataset,wealsoincorporatedeventmetrics,capturingeventssuch
asoutofmemory,scheduledactivities,pullevents,failedcreation
MeanAverageRank(MAR)measurestheaveragerankofall
events,andimagepullback-offsonaper-nodebasis.Usingthis
relevantitemsintherankedlist.It’sasmetricwhenthereare
data,weaimedtopredictsystemicfailures.
multiplerelevantitemsperquery,andyouwanttoassesshowwell
WeadheredtoastandardServiceLevelAgreement(SLA)that
thesystemranksallofthemonaverageandisdefinedas:
designatesasystemas“failed"if99.9%ofthetotalrequestsreceived
ontheserverresultedinerrors,suchasa503error,withinaspecific
𝑁
MAR=
𝑁
1 ∑︁
𝑖=1
(cid:169)
(cid:173)|𝑅
1
𝑖| 𝑟
∑︁
∈𝑅𝑖
rank 𝑖,𝑟(cid:170)
(cid:174) v
ti
a
m
li
e
d
f
a
r
t
a
e
m
th
e
e
(e
a
.
c
g
c
.,
u
1
ra
m
cy
in
o
u
f
t
o
e
u
).
r
T
p
h
re
e
d
l
i
a
c
b
ti
e
v
le
e
d
eff
d
o
a
r
ta
ts
s
.
etwasemployedto
(cid:171) (cid:172) Further validation was sought by leveraging multiple neural
where,
networkmodels,asdelineatedinTable3.Thesemodels,previously
• 𝑁 isthenumberofrankedlists.
utilizedbyotherresearchers[34,36],wereexaminedtocompare
• • 𝑅 ra 𝑖 n i k s 𝑖 t ,𝑟 he is s t e h t e o r f a r n e k lev o a f n re t l i e t v em an s t f i o te r m th 𝑟 e i 𝑖 n 𝑡ℎ th ra e n 𝑖 k 𝑡ℎ ed ra l n is k t. edlist. t G h r e ap eff h e N ct e i u v r e a n l e N ss e o tw f o I r n k st (G an N t N Op ) s to .N st o r t u a c b t l u y r , e In t s h t e an r t e O la p ti s o e n m sh p i l p o s ys be a -
tweenfeaturesandnodes.Additionally,aGatedRecurrentUnit
6.3 ResultsandDiscussions
(GRU)capturestemporalaspectsofeachnodeinthesystem,such
In this paper, we focus on the resources’ over-utilization (also astimelagsoft-2andt-5.
knownasoverload)usecaseasthecauseofanomalies.Theassump- TheperformancemetricsrevealedthatInstantOpsachieved
tionisthatresourceutilizationhappensduetocausesexternalto thehighestF1scoreforMicroSSat0.98,witharecallof0.98anda
theapplicationswemonitor.Withinthisparticularusecase,ourex- precisionof0.97.SimilarscoreswereobservedfortheTrainTicket
perimentsareorganizedaroundseveralresearchquestions,which dataset.FortheQoTDdataset,theF1scorewas0.96,witharecall
arediscussedbelow. andprecisionbothmeasuring0.96.Whencomparingotherneural
• RQ1:HowefficientisInstantOpsforsystemfailurepredic- networkalgorithmsusingtheMicroSSdataset,thecombinationof
tioncomparedtootherneuralnetworkalgorithms? GTNwithGRUandLSTMyieldedanF2scoreof0.94.TheTrain
• RQ2: How does the efficiency of InstantOps for failure Ticketdatasetregisteredascoreof0.92fortheintegrationofGTN
predictioncomparetostate-of-the-artmethods? andLSTM,whileGNNandLSTMachieved0.94.
126

InstantOps:AJointApproachtoSystemFailurePredictionandRootCauseIdentificationinMicroservicesCloud-NativeApplications ICPE’24,May7–11,2024,London,UK
| Table 3: Comparison |     | of  | different | algorithms | for | MicroSS, |     |     |     |     |     |
| ------------------- | --- | --- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
TrainTicket,andQoTDdatasets RQ2:Weshowedthatbyconstructingadependency
graphbasedontracestodepicttheserviceinterac-
tionsofthefaultyserviceusingGNNandGRUto
|     | MicroSS |     | TrainTicket |     |     | QoTD |     |     |     |     |     |
| --- | ------- | --- | ----------- | --- | --- | ---- | --- | --- | --- | --- | --- |
Algorithm Acc. Prec. Rec. F1 Acc. Prec. Rec. F1 Acc. Prec. Rec. F1 incorporatetemporalaspects,InstantOpsachieves
higherprecision,recallandF1scorethanthestate-
| InstantOps | 0.97 0.97 | 0.980.980.98 | 0.97 | 0.980.980.97 | 0.96 | 0.960.96 |     |     |     |     |     |
| ---------- | --------- | ------------ | ---- | ------------ | ---- | -------- | --- | --- | --- | --- | --- |
GNN+LSTM 0.93 0.93 0.93 0.93 0.91 0.87 0.91 0.89 0.91 0.94 0.94 0.94 of-the-artmethods.
| GNN | 0.90 0.93 | 0.90 0.91 | 0.87 0.83 | 0.87 0.85 | 0.92 0.93 | 0.92 0.93 |     |     |     |     |     |
| --- | --------- | --------- | --------- | --------- | --------- | --------- | --- | --- | --- | --- | --- |
| GTN | 0.73 0.93 | 0.73 0.81 | 0.92 0.86 | 0.92 0.89 | 0.88 0.89 | 0.88 0.88 |     |     |     |     |     |
GTN+LSTM 0.95 0.93 0.96 0.94 0.93 0.92 0.96 0.92 0.91 0.90 0.94 0.93 6.3.3 RQ3:HowdoesInstantOpsperformrootcauseanalysisas
GTN+GRU 0.96 0.92 0.96 0.94 0.93 0.86 0.93 0.90 0.92 0.94 0.89 0.92 Toassesstheeffi-
comparedtootherneuralnetworkalgorithms?
ciencyof InstantOpsinrootcauselocalizationatthenodelevel,
weusedtwometrics:MFR(MeanFirstRank)andMAR(MeanAver-
ageRank)describedearlieronthreedatasets:MicroSS,TrainTicket,
andQoTDasshowninTable5.
RQ1:Weshowedthatbyfusingtraces,logs,andmet- Ascanbeseenfromthetable,InstantOpsachievesanMFR
ricsandcapturingtemporalaspectsusingGRUsto scoreof1.49andaMARscoreof1.51ontheQoTDdataset.Onthe
MicroSSdataset,InstantOpsachievesascoreof1.51forbothMFR
| identify | anomalies | by  | observing | deviations |     | in the |     |     |     |     |     |
| -------- | --------- | --- | --------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
interactionsbetweenservices,InstantOpsobtained andMAR.OntheTrainTicketdataset,InstantOpsachievesascore
higherprecision,recallandF1scoresincomparison of1.06forbothMARandMFR.Wealsoobservedthatthecombina-
tootherneuralnetworkalgorithmsonthreedata- tionofGNNandLSTMexhibitedsimilarstrongperformance.For
sets:QoTD,MicroSSandTrainTicket. theQoTDdataset,GNN+LSTMachievedascoreof1.51forboth
MARandMFR.OntheMicroSSdataset,GNN+LSTMachieveda
scoreof1.06forMARandascoreof1.07forMFR.OntheTrain
| 6.3.2 RQ2:Howdoestheefficiencyof |     |     |     | InstantOpsforfailurepre- |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
Ticketdataset,GNN+LSTMachievedascoreof1.6forbothMAR
Table4illustratesa
| dictioncomparetostate-of-the-artmethods? |     |     |     |     |     |     | andMFR. |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
comparisonstudybetweenInstantOps,JLTandAnafusiontoes-
tablishamultimodalbaseline.
Table5:Effectivenessoffailuretypedeterminationatthe
TheJLTmethodaggregatestheresultsfromJumpStarter[22],
nodelevel
LogAnomaly[23],andTraceanomaly[20].Itemploysmajorityvot-
ing,markingafailureiftwoormoremodalitiesfailsimultaneously.
AnotableobservationaboutJLTisthatitdisregardsthecorrelation QoTD MicroSS TrainTicket
Algorithm
amongdifferentmodalities.FortheMicroSSdataset,whichinte- MAR MFR MAR MFR MAR MFR
gratesmetrics,logs,andtraces,JLTachievesanF1scoreof0.61,a InstantOps 1.51 1.49 1.06 1.06 1.06 1.06
recallof0.94,andaprecisionof0.46. GNN+LSTM 1.51 1.51 1.06 1.07 1.06 1.06
TofurtherimproveJLT’sperformanceforfaultprediction,Zhao GNN 1.51 1.51 1.59 1.59 1.06 1.19
| et [36]. proposed | Anafusion, |     | an unsupervised |     | failure | detection |     |           |      |      |           |
| ----------------- | ---------- | --- | --------------- | --- | ------- | --------- | --- | --------- | ---- | ---- | --------- |
|                   |            |     |                 |     |         |           | GTN | 1.67 1.62 | 1.15 | 1.24 | 1.47 1.47 |
techniquethatintegratesmultimodaldataformicroservices.Ituses
|     |     |     |     |     |     |     | GTN+LSTM | 1.89 1.89 | 1.18 | 1.11 | 1.37 1.47 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ---- | --------- |
agraphneuralnetworktolearnthecorrelationsintheheteroge- GTN+GRU 1.89 1.56 1.06 1.14 1.90 1.95
neousmultimodaldataset.ForthesameMicroSSdataset,Anafusion
achievedanF1scoreof0.85,arecallof0.94,andaprecisionof0.79.
InInstantOps,wehavefurtherrefinedtheAnafusionmodelby
constructingagraphbasedontraces,whichdisplaysinteractions
RQ3:Weshowedbylocalizingtherootcausesatthe
amongthenodesinrealtime.InstantOpsemploysbothGNNand
nodelevel,theInstantOpsapproachperformsbetter
GRUtoaccountforthesystem’stemporalaspects.Ourexperimental
intermsofMARandMFRincomparisontoother
| results indicate | that | InstantOps, | when | applied | to  | the MicroSS |     |     |     |     |     |
| ---------------- | ---- | ----------- | ---- | ------- | --- | ----------- | --- | --- | --- | --- | --- |
neuralnetworkalgorithmsinitseffectivenessofde-
dataset,achievesanF1scoreof0.98,aprecisionof0.97,andarecall
|     |     |     |     |     |     |     | termining | failure type | at the node | level | on three |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ----------- | ----- | -------- |
of0.98.
datasets:QoTD,MicroSSandTrainTicket.
RQ4:HowdoesInstantOpsperformintermsofrootcause
6.3.4
Table4:TheAveragePercentageAmongPrecision,Recall, Inthisexperiment,
nodelocalizationcomparedtoexistingmethods?
andF1-ScoreofDifferentApproachesonMicroSSDataset
wecompareInstantOpswithsevenalgorithms.Microscopeand
MEPFLaremicroserviceanomalydetectionapproacheswhereMi-
|     |     | Modality |     | MicroSSDataset |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
croscopecollectsnetworkandSLOmetricstoinferrootcauses
| Approach | Metric | Log | Trace | Prec. | Rec. | F1  |                       |       |                |        |            |
| -------- | ------ | --- | ----- | ----- | ---- | --- | --------------------- | ----- | -------------- | ------ | ---------- |
|          |        |     |       |       |      |     | during SLO violations | while | MEPFL predicts | latent | errors and |
InstantOps ✓ ✓ ✓ 0.970 0.980 0.980 faultymicroservicesbyintegratingtracelogsandinjectingfaults.
AnoFusion ✓ ✓ ✓ 0.795 0.945 0.857 TraceAnomaly,anunsupervisedapproach,learnstracepatterns
| JLT |     | ✓   | ✓ ✓ | 0.461 | 0.940 | 0.618 |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | ----- | --- | --- | --- | --- | --- |
todetectabnormaltracesandlocaliserootcauses.MonitorRank
127

ICPE’24,May7–11,2024,London,UK RaphaelRoufetal.
employsRandomWalk,whichcombineshistoricalandreal-time processwassupplementedbyobservationsofmicroservicecrashes
metricsforrootcauserankinginservice-orientedwebarchitectures. inOpenShiftclusters.Nevertheless,anypotentialmislabelingor
RCSF,designedforenterprisesystems,analysesperformancelogs misinterpretationoftheseeventscouldcompromisetheintegrity
anddependencymodelstoidentifyfaultpropagationsequences. ofourfindings.
InstantOpsisdesignedtofusefeaturessuchasresourceutiliza- Furthercomplicatingourvalidityisthediversityofourdata
tion,eventsandlogsandconstructgraphneuralnetworkbasedon sources.We’veutilizedthreedatasets,includingtwoopen-source
theinterationsamongthenodesinmicroservice.anditlocalizethe ones,tosupportthegeneralizabilityofourresults.However,the
faultynodethatcorrespondstosystemfailure. varianceinsizeandscopebetweenourexperimentaldataandthe
Table6providesaquantitativecomparisonofInstantOpswith real-worldcomplexityofmicroserviceoperationscouldlimitthe
sevenalgorithmssuchasTraceRCA[16],MicroScope[17],MEPFL applicabilityofourconclusions.
(RF)[38],TraceAnomaly[20],Random-Walk[31],andRCSF[30] Anothersignificantvaliditythreatarisesfromthegranularity
benchmarkedagainstothermethodssourcedfrom[16].Themetrics ofourdatacollection.Bycapturingawidearrayofmetrics—from
𝐴@1,𝐴@2,and𝐴@3areutilizedasevaluativestandards. resourceusagetonodeinteractions—onaone-minuteinterval,we
Asisevidentfromthetable,InstantOpsdemonstratesahigh assume that this level of granularity is sufficient for predicting
degreeofeffectiveness.Withan𝐴@1scoreof0.92,itsurpasses imminentsystemfailures.Yet,thereisariskthatmorenuanced
themajorityofthealgorithmsinthelistandmaintainsconsistent orgranulardatacouldyielddifferentinsights,whichmeansour
performanceacross𝐴@2and𝐴@3.Thisconsistenthighperfor- currentapproachmayoverlookcertainsubtleties.
manceacrossmetricssuggeststhereliabilityandrobustnessofthe Lastly,thescopeofourdatasets,whicharesmallerincomparison
InstantOpsalgorithm. tothoseusedinextensiveindustrialmicroservicesystems,could
AlgorithmssuchasRandom WalkandRCSF,althoughdisplaying underminethescalabilityofouralgorithm.Whilewebelieveour
commendablevaluesin𝐴@2and𝐴@3,haverelativelylower𝐴@1 algorithmshouldfunctioneffectivelyevenwithcoarser-grained
values.Thisdifferencecouldindicatepotentialvariabilityintheir datasets,thetruetestofitsapplicabilitywillcomewhenitisapplied
performanceacrossdifferentstagesorconditions. tothelargerandmorecomplexdatasetsthatweplantoobtainfrom
Conversely, TraceAnomaly and MicroScope consistently per- ourclientsinfuturework.Thisstepiscrucialforustovalidate
formworse,furtherdelineatingtheperformancegapbetweenthese theefficiencyofourmodelandensurethatitcanwithstandthe
methodsandInstantOps. demandsofafull-scaleindustrialenvironment.
8 CONCLUSION
Table6:Comparisonofrootcauselocalizationonfaultsof
differentlevelsonA In thiswork,weproposed InstantOps, an approachthat takes
inmulti-modaldatatoconstructagraphusingtraceswithlogs
andmetricdataasnodeattributes.Throughthis,weuseourmulti-
Algorithm A@1 A@2 A@3
modalsystemfailurepredictionapproachandcapturetemporal
InstantOps 0.92 0.95 0.98 andspatialaspectstopreciselyandeffectivelypredictfailuresand
TraceRCA 0.83 0.93 0.97 determinetherootcausesoffailuresatthenodelevel.Inaddition
MicroScope 0.56 0.62 0.7 tousingourin-housedataset:QoTD,weusedtwoopensource
MEPFL(RF) 0.94 0.97 0.97 datasets:MicroSSandTrain-Ticket.Inourexperimentalstudies,we
RandomWalk 0.51 0.86 0.94 haveshownhowInstantOpscanidentifyandlocalizethefaulty
RCSF 0.52 0.86 0.93 nodeinmicroservicewhichcanfacilitatetherootcauseanalysisof
TraceAnomaly 0.49 0.59 0.63 thesystemfailure.WebelievethattheuseofaGraphNeuralNet-
worktoconstructtopologyandinteractionamongthenodesand
incorporatingtemporalinformationusingtheGRUmodelimproves
thepredictionofsystemfailure.WeaimtoevolveInstantOpsinto
RQ4:Weshowedbylocalizingtherootcausesatthe anonlinelearningsystemcapableofupdatingitsmodelsinreal
nodelevel,InstantOpsoutperformsintermsofthe time.Thiscontinuouslearningapproachwouldallowforimmediate
evaluativestandardsA@1,A@2andA@3incompar- adjustmentsbasedonthelatestsystembehavior,therebyenhancing
isontootherexistingmethodsinrootcauselocaliza- predictiveaccuracyovertime.
tiononfaultsofdifferentlevelsonA,demonstrating
highereffectivenessthanexistingmethods. 9 ACKNOWLEDGMENT
We would like to thank IBM Center for Advanced Studies and
OntarioORF-REfortheirsupport.
7 THREATSTOVALIDITY
Inourresearch,we’veidentifiedseveralthreatstovaliditythat
warrantcarefulconsideration.Thefirstthreatpertainstotheaccu-
racyoffailurelabelingwithinourmicroservicesstudy.Specifically,
whileexaminingthe’QuoteoftheDay’(QoTD)application,we
establishedaperformancebaselinewithJMeterandsubsequently
annotatedfailureeventsusingChaosMeshforfaultinjection.This
128

InstantOps:AJointApproachtoSystemFailurePredictionandRootCauseIdentificationinMicroservicesCloud-NativeApplications ICPE’24,May7–11,2024,London,UK
REFERENCES networks.In2020IEEE31stInternationalSymposiumonSoftwareReliability
[1] RafiulAhad,EricChan,andAdrianoSantos.2015. Towardautonomiccloud: Engineering(ISSRE).IEEE,48–58.
Automaticanomalydetectionandresolution.In2015InternationalConferenceon [21] MengMa,WeilanLin,DishengPan,andPingWang.2020. Self-adaptiveroot
causediagnosisforlarge-scalemicroservicearchitecture.IEEETransactionson
CloudandAutonomicComputing.IEEE,200–203.
[2] VildeChristiansen,MoutazHaddara,andMariusLangseth.2022.Factorsaffecting ServicesComputing15,3(2020),1399–1410.
|     |     |     |     |     | [22] MinghuaMa,ShenglinZhang,JunjieChen,JimXu,HaozheLi,YongliangLin, |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- |
cloudERPadoptiondecisionsinorganizations.ProcediaComputerScience196
(2022),255–262. XiaohuiNie,BoZhou,YongWang,DanPei,etal.2021.Jump-Startingmultivariate
timeseriesanomalydetectionforonlineservicesystems.In2021USENIXAnnual
[3] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2018.Bert:
|     |     |     |     |     | T e ch n ica | l C o n f er e n c e ( U S | E N I X A T C 2 1 ). 4 1 3 | – 42 6 . |     |
| --- | --- | --- | --- | --- | ------------ | -------------------------- | -------------------------- | -------- | --- |
Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding.arXiv [23] W e ib in M e n g , Y i n g L i u , Y ic h e n Z h u, S h e n g l in Z h ang,DanPei,YuqingLiu,Yihao
preprintarXiv:1810.04805(2018).
Chen,RuizhiZhang,ShiminTao,PeiSun,etal.2019.Loganomaly:Unsupervised
[4] YingFu,MengYan,JianXu,JianguoLi,ZhongxinLiu,XiaohongZhang,andDan
Yang.2022.Investigatingandimprovinglogparsinginpractice.InProceedings de t e c t io n o f s e q u e n tialandquantitativeanomaliesinunstructuredlogs.InIJCAI,
|     |     |     |     |     | V o l . 1 9 | .4 7 3 9 – 4 7 4 5 . |     |     |     |
| --- | --- | --- | --- | --- | ----------- | -------------------- | --- | --- | --- |
ofthe30thACMJointEuropeanSoftwareEngineeringConferenceandSymposium
|     |     |     |     |     | [24] JoydeepMukherjee,AlexandruBaluta,MarinLitoiu,andDiwakarKrishnamurthy. |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------------------------------------------------- | --- | --- | --- | --- |
ontheFoundationsofSoftwareEngineering.1566–1577. 2020.RAD:Detectingperformanceanomaliesincloud-basedwebservices.In
[5] SahilGarg,KuljeetKaur,NeerajKumar,ShaliniBatra,andMohammadSObaidat.
2020IEEE13thInternationalConferenceonCloudComputing(CLOUD).IEEE,
2018. HyClass:Hybridclassificationmodelforanomalydetectionincloud
| environment.(2018). |     |     |     |     | 493–501.                                                           |     |     |     |     |
| ------------------- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- |
|                     |     |     |     |     | [25] NPandeeswariandGaneshKumar.2016.Anomalydetectionsystemincloud |     |     |     |     |
[6] SahilGarg,KuljeetKaur,NeerajKumar,GeorgesKaddoum,AlbertYZomaya,and
environmentusingfuzzyclusteringbasedANN.MobileNetworksandApplications
| RajivRanjan.2019.Ahybriddeeplearning-basedmodelforanomalydetectionin |     |     |     |     | 21(2016),494–505. |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
clouddatacenternetworks.IEEETransactionsonNetworkandServiceManagement
|     |     |     |     |     | [26] DanielPop.2016.Machinelearningandcloudcomputing:Surveyofdistributed |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------------------------ | --- | --- | --- | --- |
16,3(2019),924–935. andsaassolutions.arXivpreprintarXiv:1603.08767(2016).
[7] LGirishandSridharKNRao.2021.Anomalydetectionincloudenvironment
|           |                                   |                             |                                   |     | [27] YRouf,JMukherjee,andMLitoiu.2023.TowardsaRobustOn-linePerformance |     |     |     |     |
| --------- | --------------------------------- | --------------------------- | --------------------------------- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- |
| u s i n g | a r ti fi ci a l i n te l l ig en | c e te c h ni q u e s . C o | m p u ti n g (2 02 1 ) , 1– 1 4 . |     |                                                                        |     |     |     |     |
ModelIdentificationforChangeImpactPrediction.In2023IEEE/ACM18thSym-
[8] P r a n ja l G u p t a , H a r s h it K u m a r ,D e b a n j a n a K a r, K a ra n B h u k ar , P oojaAggarwal, posiumonSoftwareEngineeringforAdaptiveandSelf-ManagingSystems(SEAMS).
| andPrateetiMohapatra.2023. |     | LearningRepresentationsonLogsforAIOps. |     |     |                            |     |                                               |     |     |
| -------------------------- | --- | -------------------------------------- | --- | --- | -------------------------- | --- | --------------------------------------------- | --- | --- |
|                            |     |                                        |     |     | Melbourne,Australia,68–78. |     | https://doi.org/10.1109/SEAMS59076.2023.00018 |     |     |
In2023IEEE16thInternationalConferenceonCloudComputing(CLOUD).IEEE, [28] JacopoSoldaniandAntonioBrogi.2022.Anomalydetectionandfailurerootcause
155–166.
analysisin(micro)service-basedcloudapplications:Asurvey.ACMComputing
[9] TanjaHagemannandKaterinaKatsarou.2020.Asystematicreviewonanomaly
|     |     |     |     |     | S u r v e y | s (C S U R ) 5 5 , 3 ( 2 02 | 2 ), 1 – 3 9 . |     |     |
| --- | --- | --- | --- | --- | ----------- | --------------------------- | -------------- | --- | --- |
detectionforcloudcomputingenvironments.In20203rdArtificialIntelligence [29] A r t h u r V er v a e t. 2 0 2 1 . M o n iL o g : A nAutomatedLog-BasedAnomalyDetection
| a n d C | l ou d C o m p u ti n g C | on fe re nc e . 8 3 – 9 6 . |     |     |     |     |     |     |     |
| ------- | ------------------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
SystemforCloudComputingInfrastructures.In2021IEEE37thInternational
[10] P in ji a H e ,J ie m i n g Z h u ,Z ib in Z h e n g , a n d MichaelRLyu.2017.Drain:Anonline ). IE E E , 27 3 9 – 2 7 43 .
logparsingapproachwithfixeddepthtree.In2017IEEEinternationalconference C o n f er en c e o n D a t a E n g i ne e r in g ( IC D E
|     |     |     |     |     | [30] K u i W | a n g , C ar o l F u n g , C | h a o D i n g ,P o lo P | e i, S h a o h a n H uang,ZhongzhiLuan, |     |
| --- | --- | --- | --- | --- | ------------ | ---------------------------- | ----------------------- | --------------------------------------- | --- |
onwebservices(ICWS).IEEE,33–40.
[11] JordanHochenbaum,OwenSVallis,andArunKejariwal.2017.Automaticanom- andDepeiQian.2015. Amethodologyforroot-causeanalysisincomponent
|     |     |     |     |     | b a se d | sy s t e m s . In |     |     |     |
| --- | --- | --- | --- | --- | -------- | ----------------- | --- | --- | --- |
a ly d e t ectioninthecloudviastatisticallearning.arXivpreprintarXiv:1704.07706 2 0 1 5 I EEE23rdInternationalSymposiumonQualityofService
|     |     |     |     |     | ( I W Q oS | ). I E E E , 2 43 – 2 4 8 . |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --------------------------- | --- | --- | --- |
( 2 01 7 ) . [31] PingWang,JingminXu,MengMa,WeilanLin,DishengPan,YuanWang,and
[12] MohammadSIslam,WilliamPourmajidi,LeiZhang,JohnSteinbacher,Tony
|     |     |     |     |     | PengfeiChen.2018. | Cloudranger:Rootcauseidentificationforcloudnative |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | ------------------------------------------------- | --- | --- | --- |
Erwin,andAndriyMiranskyy.2021.Anomalydetectioninalarge-scalecloud
p la t fo rm . In s y s te m s .I n 2 0 1 8 1 8 t h I E E E / A C M In t e r n a t i o n a l S y m p o s iu m o n C lu st e r, C l o u d a n d
2 0 2 1 I E E E/ A C M 4 3 r d I n te r n a t io n a l C o n f er e n c e o n S oftwareEngineering: G r i d C o m p u ti n g ( C C G R I D ) . IE E E , 4 9 2 – 5 0 2 .
| So ft w a | re E ng i n e e r in g i n | P rac t i c e ( IC S E - S E I | P ). I E E E , 1 5 0 – 1 5 9 . |     |                |                               |                             |                               |                           |
| --------- | -------------------------- | ------------------------------ | ------------------------------ | --- | -------------- | ----------------------------- | --------------------------- | ----------------------------- | ------------------------- |
|           |                            |                                |                                |     | [32] G u a n g | b a Y u , P e n g f e i C h e | n , H o n g y a n g C h e n | , Z i ji e G u a n , Zic h en | g H u a n g , L i nx i ao |
[13] AbulKhayer,NusratJahan,MdNahinHossain,andMdYahinHossain.2021. Jing,TianjunWeng,XinmengSun,andXiaoyunLi.2021. Microrank:End-to-
Theadoptionofcloudcomputinginsmallandmediumenterprises:adeveloping
endlatencyissuelocalizationwithextendedspectrumanalysisinmicroservice
| c o u n try | p e r sp e c t i v e . V IN | E JournalofInformationandKnowledgeManagement |     |     |     |     |     |     |     |
| ----------- | --------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
s5 1 , 1 ( 2 0 2 1 ) , 6 4– 9 1. e n v i ro n m en t s . In P ro c e e d i ng s o f th e W e b C o n fe re n c e 2 0 21 . 3 0 8 7 – 3 0 98 .
S y st em [33] H o n g w e iZ h a n g ,Y u a n q i n g X ia , T ij in Y a n ,a n d G u i y a n g L iu . 2 0 2 1 . U n supervised
[14] CherylLee,TianyiYang,ZhuangbinChen,YuxinSu,andMichaelRLyu.2023.
anomalydetectioninmultivariatetimeseriesthroughtransformer-basedvaria-
Eadro:AnEnd-to-EndTroubleshootingFrameworkforMicroservicesonMulti- t io n a l a u t oe n c o der.In202133rdChineseControlandDecisionConference(CCDC).
SourceData.arXivpreprintarXiv:2302.05092(2023).
|     |     |     |     |     | IE E E , | 2 8 1 – 2 8 6 . |     |     |     |
| --- | --- | --- | --- | --- | -------- | --------------- | --- | --- | --- |
[15] CherylLee,TianyiYang,ZhuangbinChen,YuxinSu,YongqiangYang,and
MichaelRLyu.2023.Heterogeneousanomalydetectionforsoftwaresystemsvia [34] ShenglinZhang,PengxiangJin,ZihanLin,YongqianSun,BichengZhang,Sibo
|             |                           |                             |                                             |                  | Xia,ZhengdanLi,ZhenyuZhong,MinghuaMa,WaJin,etal.2023.      |     |     |     | Robust |
| ----------- | ------------------------- | --------------------------- | ------------------------------------------- | ---------------- | ---------------------------------------------------------- | --- | --- | --- | ------ |
| s e m i- su | p er vi s e d cr o s s- m | o d a l a t te n t io n . a | rX iv p r ep r in t a rX iv : 2 30 2 . 0 69 | 1 4 ( 20 2 3 ) . |                                                            |     |     |     |        |
|             |                           |                             |                                             |                  | FailureDiagnosisofMicroserviceSystemthroughMultimodalData. |     |     |     | arXiv  |
[16] Z e ya n L i, Ju n j i eC h e n , R u i Ji a o , N e n g w e n Z ha o , Z h ij u n W a n g , S h u w e i Z h a n g , preprintarXiv:2302.10512(2023).
YanjunWu,LongJiang,LeiqinYan,ZikaiWang,etal.2021.Practicalrootcause
|     |     |     |     |     | [35] XuZhang,QingweiLin,YongXu,SiQin,HongyuZhang,BoQiao,Yingnong |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- |
localizationformicroservicesystemsviatraceanalysis.In2021IEEE/ACM29th Dang,XinshengYang,QianCheng,MuraliChintalapati,etal.2019.Cross-dataset
|     |     |     | . I E E E , 1 – 1 0. |     |     |     |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
I n te r na ti o n a l S y m p o si um on Q ua l i ty of S e r v ic e ( IW Q O S) TimeSeriesAnomalyDetectionforCloudSystems.InUSENIXAnnualTechnical
| [17] J in Ji n | L i n , P e n g fe i C h en, | an d Z i b in Z h e | n g . 2 0 18 . M i c r o sc o p e : P inpointper- |     |              |                          |     |     |     |
| -------------- | ---------------------------- | ------------------- | ------------------------------------------------- | --- | ------------ | ------------------------ | --- | --- | --- |
|                |                              |                     |                                                   |     | C o n f e re | nc e . 1 06 3 – 1 0 7 6. |     |     |     |
formanceissueswithcausalgraphsinmicro-serviceenvironments.InService- [36] C h e n y u Z h a o , M i n g h uaMa,ZhenyuZhong,ShenglinZhang,ZhiyuanTan,
OrientedComputing:16thInternationalConference,ICSOC2018,Hangzhou,China,
|     |     |     |     |     | XiaoXiong,LuLuYu,JiayiFeng,YongqianSun,YuzhiZhang,etal.2023. |     |     |     | Ro- |
| --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- |
N o v e m b e r 1 2 - 1 5 , 20 18 , P r o ce e di n g s, V o l. 1 6 . Sp r i n g e r , 3 – 20 . bustMulti-ModalFailureDetectionforMicroserviceSystems.InarXivpreprint
| [18] M a r i n | L it o i u , I a n W a t ts | , a n d J o e W i g g le s | w o r t h . 2 0 2 1 . T he13thcasconwork- |     |             |                  |     |     |     |
| -------------- | --------------------------- | -------------------------- | ----------------------------------------- | --- | ----------- | ---------------- | --- | --- | --- |
|                |                             |                            |                                           |     | a r X iv :2 | 3 0 5. 1 8 98 5. |     |     |     |
shoponcloudcomputing:engineeringaiops.InProceedingsofthe31stAnnual
|     |     |     |     |     | [37] X i an g | Z h o u , X in Peng,TaoXie,JunSun,ChaoJi,WenhaiLi,andDanDing.2018. |     |     |     |
| --- | --- | --- | --- | --- | ------------- | ------------------------------------------------------------------ | --- | --- | --- |
InternationalConferenceonComputerScienceandSoftwareEngineering.280–281. Faultanalysisanddebuggingofmicroservicesystems:Industrialsurvey,bench-
[19] DapengLiu,YoujianZhao,HaowenXu,YongqianSun,DanPei,JiaoLuo,Xi-
marksystem,andempiricalstudy.IEEETransactionsonSoftwareEngineering47,
| aoweiJing,andMeiFeng.2015.Opprentice:Towardspracticalandautomatic |     |     |     |     | 2(2018),243–260. |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
anomalydetectionthroughmachinelearning.InProceedingsofthe2015internet
|     |     |     |     |     | [38] XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,and |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- |
measurementconference.211–224.
[20] PingLiu,HaowenXu,QianyuOuyang,RuiJiao,ZhekangChen,ShenglinZhang, ChuanHe.2019.Latenterrorpredictionandfaultlocalizationformicroservice
applicationsbylearningfromsystemtracelogs.InProceedingsofthe201927th
| JiahaiYang,LinlinMo,JiceZeng,WenmanXue,etal.2020. |     |     | Unsupervised |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
ACMJointMeetingonEuropeanSoftwareEngineeringConferenceandSymposium
detectionofmicroservicetraceanomaliesthroughservice-leveldeepbayesian ontheFoundationsofSoftwareEngineering.683–694.
129