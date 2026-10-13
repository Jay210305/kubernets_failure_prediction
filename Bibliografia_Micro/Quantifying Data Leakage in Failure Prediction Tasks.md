PDF Download
3676151.3719368.pdf
17 March 2026
Total Citations: 0
. Total Downloads: 393
.
Latest updates: hps://dl.acm.org/doi/10.1145/3676151.3719368 .
.
.
.
RESEARCH-ARTICLE
antifying Data Leakage in Failure Prediction Tasks .
.
Published: 05 May 2025
.
DANIEL GRILLMEYER, Julius-Maximilian University of Würzburg, Wurzburg, Bayern, . Citation in BibTeX format
Germany .
.
ICPE '25: 16th ACM/SPEC International
. MARIUS HADRY, Julius-Maximilian University of Würzburg, Wurzburg, Bayern, Germany Conference on Performance Engineering
May 5 - 9, 2025
. VERONIKA LESCH, Baden-Wueremberg Cooperative State University, Friedrichstraaye 14, Toronto ON, Canada
hps://www.dhbw.de/startseite.html, Stugart . .
Conference Sponsors:
. SIGSOFT
VANESSA BORST, Julius-Maximilian University of Würzburg, Wurzburg, Bayern, Germany
SIGMETRICS
.
ROBERT LEPPICH, Julius-Maximilian University of Würzburg, Wurzburg, Bayern, Germany
.
ANDRÉ BAUER, Illinois Institute of Technology, Chicago, IL, United States
.
View all
.
.
Open Access Support provided by:
.
Julius-Maximilian University of Würzburg
.
Illinois Institute of Technology
.
Baden-Wueremberg Cooperative State University
.
ICPE '25: Proceedings of the 16th ACM/SPEC International Conference on Performance Engineering (May 2025)
hps://doi.org/10.1145/3676151.3719368
ISBN: 9798400710735
.

Quantifying Data Leakage in Failure Prediction Tasks
DanielGrillmeyer MariusHadry VeronikaLesch
UniversityofWürzburg UniversityofWürzburg Baden-WuerttembergCooperative
Würzburg,Germany Würzburg,Germany StateUniversityMosbach
Daniel.Grillmeyer@uni- Marius.Hadry@uni-wuerzburg.de Mosbach,Germany
wuerzburg.de Veronika.Lesch@dhbw.de
VanessaBorst RobertLeppich AndréBauer
UniversityofWürzburg UniversityofWürzburg IllinoisInstituteofTechnology
Würzburg,Germany Würzburg,Germany Chicago,USA
Vanessa.Borst@uni-wuerzburg.de Robert.Leppich@uni-wuerzburg.de Andre.Bauer@iit.edu
SamuelKounev
UniversityofWürzburg
Würzburg,Germany
Samuel.Kounev@uni-wuerzburg.de
Abstract Keywords
Withtheeverincreasingimportanceofcloudcomputinganda MachineLearning,DeepLearning,HDDFailurePrediction,Data
strongfocusonreliabledatacenters,ahighamountofresearch LeakageMeasure,DataSplitting,PerformanceOptimism
hasbeendoneonfailurepredictionforharddiskdrives.Thecollec-
ACMReferenceFormat:
tionofmonitoringdata,suchasSMARTstatistics(Self-Monitoring,
DanielGrillmeyer,MariusHadry,VeronikaLesch,VanessaBorst,Robert
Analysis,andReportingTechnology)fromoperationalHDDs,en-
Leppich,AndréBauer,andSamuelKounev.2025.QuantifyingDataLeak-
ablesoperatorstoobtainpredictionsabouttheexpectedremaining
ageinFailurePredictionTasks.InProceedingsofthe16thACM/SPECIn-
usefullife.NumerousmethodsforHDDfailurepredictionhave ternationalConferenceonPerformanceEngineering(ICPE’25),May5–9,
beenpublishedinrecentyears,andtheirevaluationhasshown 2025,Toronto,ON,Canada.ACM,NewYork,NY,USA,13pages.https:
decentresults.However,anaivesplittingintotrainingandtest //doi.org/10.1145/3676151.3719368
setscanleadtodataleakageand,thus,over-optimisticresultsthat
cannotbeachievedonthedataofscientificinterest.Inthispa- 1 Introduction
per,weproposeanoveldataleakagemeasureforquantifyingthe
Thegrowinguseofcloudcomputinginthelastdecadesispro-
amountofdataleakageintrainingandtestdatasets.Further,we
jected to continue in the next years, especially with generative
definefoursplittingtechniquesandevaluateourmeasureinterms
artificialintelligencebecomingmoreandmorecommon.According
oftheperformanceoptimismofclassificationmodelswithrespect
toGartner,theend-userspendingforecastofworldwidepublic
tothesedifferentsplittingstrategies.Ourresultsconsistentlyshow
cloudserviceswillincreasefrom561,104millionU.S.Dollarsin
thatsplittingtechniquespronetodataleakageinduceanoveresti-
2023to824,763millionU.S.Dollarsin2025[6].Smoothoperation
mationofpredictiveperformance.Overall,wewereabletoshow
ofdatacentersisthereforeakeycomponentforthecontinued
theusefulnessofthedefineddataleakagemeasure,aswellasits
successoftheseconcepts.Besidesotherdatacenter-relatedtasks,
connectionwithdifferentsplittingtechniquesandtheperformance
monitoringandmaintenanceofHardDiskDrives(HDDs)isimpor-
optimismofpredictionmodels.
tanttoensurereliableoperation.Collectedmonitoringdatafrom
HDDscanalsobeusedtoperformfailurepredictiontasks,enabling
CCSConcepts
proactivereplacementoffailingharddrives.
•Computingmethodologies→Machinelearning;•Computer Intheliterature,variousapproachesareproposedtopredictfail-
systemsorganization→Reliability. uresofHDDs.Forexample,Pereiraetal.[17]madeuseofone-class
classifiersandfoundthatPrincipalComponentAnalysis(PCA),
𝑘-Means,andbottleneckneuralnetworks(autoencoders)achieved
thebestresults.Themajorityofpapersproposemodelsfromthe
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
categoryofRecurrentNeuralNetworks(RNNs),suchasLongShort-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation TermMemories(LSTMs)[4,7,20,23],toextractinformationfrom
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe longinputsequences.Additionally,furthervariationscanbeiden-
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
tified,likeConvolutionalNeuralNetwork(CNN)layersaddedto
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. the front of the LSTM layers, resulting in a CNN-LSTM [8, 12],
ICPE’25,May05–09,2025,Toronto,Canada andLSTMscombinedwithattentionmechanisms[21].Mostofthe
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
proposedapproachesdiffersignificantlyintermsofdatasetand
ACMISBN979-8-4007-1073-5/2025/05
https://doi.org/10.1145/3676151.3719368 preprocessing,especiallysplittingmechanismsfortestandtraining
334

ICPE’25,May05–09,2025,Toronto,Canada DanielGrillmeyeretal.
dataset.Acommonissueregardingthereproducibilityoftheresults group-basedandtemporalsplit,theresultsareconsistentlyworse.
isthatitisoftennotevidentwhethercarewastakentoensurethat Theevaluationonanindependenttestsetusingthepre-trained
nodatawasleakedbetweentestandtrainingdata.Wedefinedata modelsshowsaclearperformancedeteriorationfortheno-splitand
leakage,inlinewithKaufmanetal.[10],as“theintroductionof randomsplittingtechniques.Additionally,theDLmethodsshow
informationaboutthetargetofadataminingproblemthatshould a slightly better performance for the temporal and group-based
notbelegitimatelyavailabletominefrom.” splittingtechniques,whiletheensemblemethod’sperformanceis
The effect and existence of data leakage in publications has barelyaffectedbythesplittingmethodchoice.Wefindthatthe
alreadybeeninvestigated.Forexample,Lyuetal.[13]analyzed differencesbetweenperformanceonthetestsetfromtherespective
theimpactofdifferentdatasplittingtechniquesusingtheBack- splitandontheindependentfutureset,thatis,thePerformanceOp-
blaze disk stats dataset [2] and identified a significant effect of timism(PO),stronglydependonthesplittingmethodused.Overall,
theexecutedsplittingstrategyonthemodelperformance.Besides, wewereabletoshowtheusefulnessofthedefineddataleakage
Kaufmanetal.[10]analyzedleakageindataminingingeneral, measureaswellasitsconnectionwithdifferentsplittingtechniques
identifieduncleanpracticesintheliterature,andpresentedafor- andPOofpredictionmodels.
malizationofdataleakage.KapoorandNarayanan[9]surveyed Theremainderofthispaperisstructuredasfollows:First,wedis-
17predictiontaskdisciplinesandfound294publicationsaffected cussrelatedworkinSection2.Afterwards,wefullyintroducethe
bydataleakage.Theypresentedataxonomyfortheclassification termdataleakage,proposeanoveldataleakagemeasure,anddis-
ofdataleakage.Despitetheincreasingresearcheffortstoidentify cussassumptionsmadeinSection3.InSection4,weintroducethe
andformalizedataleaks,therearenomeasurementmethodsand conductedexperiments:Theusedsplittingtechniques,thedataset
metricstoquantifytheseverityofdataleakage.Asaconsequence, anditspreprocessing,theusedpredictivemodelsandtheiropti-
therearenostudiesthatmeasuretheinfluenceofdataleakageon mization,thetermperformanceoptimism,andthehardwarecon-
theperformanceofpredictionmodels. figuration.InSection5,wepresenttheresultsofourexperiments
Withthispaper,weaimtofillthisgapbyposinganddiscussing anddiscussimportantfindings,followedbyadiscussiononthreats
thefollowingresearchquestions: tovalidityinSection6.Finally,weconcludethepaperinSection7.
RQ1: Howtomathematicallydefineameasureforquantifyingdata
leakage? 2 RelatedWork
RQ2: Whichdatasplittingtechniquesexistandhowsevereisthe
Thetopicofthispaperisrelatedtomultipleresearchareas:(i)data
dataleakageaccordingtothedefinedmeasure?
leakage,(ii)machinelearningmodelsusedforHDDfailurepredic-
RQ3: Howdoestheconsistencyofthemodels’predictiveperformance
tion,and(iii)metricsforquantifyingdataleakage.However,we
changewithdifferentsplittingtechniquesandthusdifferent
wereunabletoidentifyanyrelatedworkonthethirdaspect.Inthe
severityofdataleaks?
following,wediscussthefirsttwopoints.
Toanswertheseresearchquestions,wefirstdefineanovelmea-
sure for quantifying data leakage and discuss the assumptions
2.1 DataLeakage
made(RQ1).Themeasureaddressesthemismatchbetweenthe
testdistributionandthedistributionofscientificinterestasout- The effect and existence of data leakage in publications has al-
linedbyKapoorandNarayanan[9].Ourmeasureisnormalized readybeeninvestigated.Lyuetal.[13],forinstance,analyzedthe
totheinterval [0,1] andprovidesaparameter𝛼 thatallowsfor impactofdifferentdatasplittingtechniquesusingtheBackblaze
distinguishingthebehaviorofthemeasurerelatedtothegivenpre- diskstatsdataset [2].Theycriticizedpriorstudiesforoftenran-
dictiontask.Second,wepresentfourdifferentsplittingtechniques domlysplittingdataintotraining,validation,andtestdata.Intheir
withvaryingdegreesofdataleakagetodividedataintotraining study,Lyuetal.[13]comparedmodelstrainedusingrandomand
andtestdatasets(RQ2):(i)nosplit,(ii)randomsplit,(iii)temporal time-basedsplittingtoseparatetheavailabledataintotrainingand
split,and(iv)group-basedsplit.Whilethenosplitstrategyusesthe testingsets.Theyshowthatrandomsplittingcanintroducedata
fulldatasetfortrainingandtest,therandomsplitstrategyassigns leakage,causingmodelstoperformsignificantlyworseonunseen
measurementsrandomlytothetrainingandtestset.Thetemporal testdatawhencomparedtotheresultsforvalidationdata.Fur-
andgroup-basedsplittingtechniquesaimatacleansplitwithno ther,theyalsoshowedthatthiseffectislimitedwhenemployinga
dataleakage.Finally,inordertoanswerRQ3,weconductexperi- time-basedsplittingapproach.
mentsforallsplittingtechniquesontheBackblazedataset[2].We Thedataleakageproblemisnotonlypresentinthedomainof
applyavarietyofmulticlassclassificationmodelscommonlyused harddiskfailureprediction.Kaufmanetal.[10]analyzedleakagein
inrelatedwork,includingtheensembleMachineLearning(ML) dataminingingeneral.Theyfocusedondataminingcompetitions
methodsHistogram-basedGradientBoostingClassifier(HGBC)and andstudiesandinvestigatedthepublishedapproachesfordataleak-
RandomForest(RF),andtheDeepLearning(DL)modelsMultilayer age.Kaufmanetal.[10]founduncleanpracticesandformalized
Perceptron(MLP)andLSTM. dataleakageanditsdetectionthroughmodelingrelationsbetween
Ourevaluationshowsthatensemblemethodsachievealmost variablesinthedataset.Whilethisapproachallowsdetectingdata
perfectresultswhenusingthenosplittechnique,whileDLmethods leakage,itdoesnotprovideameaningfulwayofquantifyingthe
performslightlyworse.Thisallowstheassumptionthatthemodels amountofleakagepresent.IncontrasttoLyuetal.[13],theycon-
memorizethewholedatasetwell.Whenusingtherandomsplittech- siderednotonlydataleakagethroughtimebutalsootheraspects
nique,allmodelsperformslightlyworsebutstillfairlywell.With likedeanonymizationandusingunavailableexternalinformation.
335

QuantifyingDataLeakageinFailurePredictionTasks ICPE’25,May05–09,2025,Toronto,Canada
KapoorandNarayanan[9]surveyed17disciplineswherema- Thesecondcasereferstousingillegitimatefeatures,forinstance,
chinelearningalgorithmswereemployedforpredictiontasksand featuresactingasaproxyfortheoutcomevariable[10]thatwould
found294publicationsaffectedbydataleakage.Theypresented notbeavailableforinferenceonnoveldata.Forexample,inabinary
ataxonomyfortheclassificationofdataleakageandproposeda rainpredictiontask,theinformationifpeoplecarriedumbrellason
modelinfosheetconsistingof21questionstodetectandprevent aspecificdaycouldbeaproxyfortheoutcomevariable.
faultymethodologies.KapoorandNarayanan[9]claimthatarepro- Thelastcaseisadistributionmismatchbetweenthedistribution
duciblepublicationrequiresacleantrain-testseparation,reasoning ofscientificinterestandthetestdatasetdistribution.Forinstance,
whyeachfeatureislegitimate,andatestsetthatisdrawnfrom modelsdesignedtopredictafutureoutcomemustnotbeevaluated
thedistributionofscientificinterest,sothatthereisnoselectionor onobservationspriortothoseinthetrainingsettopreventtem-
samplingbias. poralleakage.Further,toavoidleakage,trainingandtestsamples
WhileLyuetal.[13]analyzedtheimpactofdataleakage,we mustbeindependent,oratleastthedependencestructuremust
additionallyfocusonquantifyingtheleakageandanalyzeifour alignwiththeunderlyingscientificclaim.Forinstance,ifthesci-
metricallowsustoverifytheclaimsmade.Insteadofonlycom- entificclaimisabouttheabilityofaspeechrecognitionmodelto
paringtemporaltorandomsplitting,wealsoconsidergroup-based transcriberecordingsofunseenspeakers,theevaluationmustnot
splitting,whereeachHDDserialnumberdefinesagroup.Inaddi- beperformedonrecordingsfromspeakersincludedinthetraining
tion,weincludethecaseofamissingtestdataset,wheretraining set.Lastly,samplingbiasmightbeintroducedifthetestsampleis
andtestingareperformedonthesamedata,asabaselinemethod. notrepresentativeofthedataofinterest.Forexample,aweather
forecastingmodelintendedtobeusedinNorthAmericanregions
| 2.2 Models |              |                          |               | shouldnotbeevaluatedondatafromAustralia. |     |     |     |     |
| ---------- | ------------ | ------------------------ | ------------- | ---------------------------------------- | --- | --- | --- | --- |
| When it    | comes to HDD | failure prediction using | the Backblaze |                                          |     |     |     |     |
diskstatsdataset[2],severalapproacheshavealreadybeenused. 3.1 DataLeakageMeasureDefinition
Pereiraetal.[17]madeuseofone-classclassifiers.Theyfoundthat
Inthispaper,wefocusontheproblemofthedistributionmismatch
reconstructionmethodslikePrincipalComponentAnalysis(PCA), as outlinedby Kapoor andNarayanan [9]. To assess the extent
𝑘-Meansandbottleneckneuralnetworks(autoencoders)achieve
|     |     |     |     | of the present | data leakage | and to propose | an answer | to RQ1, |
| --- | --- | --- | --- | -------------- | ------------ | -------------- | --------- | ------- |
thebestresults.EnsemblemodelslikeRFalsocommonlyachieved wedefinethenormalizeddataleakagemeasureL˜ asderivedin
goodresults[1,19,24]. Equations1to3.ThesetsM andM denotethetestand
|     |     |     |     |     |     | test | train |     |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --- |
DL-basedmethodshavealsobeenemployedforHDDfailure trainingdatasets.TheirunionM ∪M
|     |     |     |     |     |     | test | trainistheentiredataset. |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------------------ | --- |
prediction.RNNslikeLSTMsoffertheabilitytoextractinformation Disthesetofgroupsinthedataset,forinstance,definedbyspecific
fromlonginputsequences[4,7,20,23].Authorshavealsoused HDDs.𝑿𝑖,𝑡 denotesthedatasampleattimestep𝑡 ingroup𝑖,where
variationsoftheLSTM,liketheCNN-LSTM[8,12],whichcombines 𝑡 ∈ N and𝑖 ∈ {1,...,|D|}. 𝛼 ∈ R+ is a parameter indicating
0
CNNsandLSTMs.Furthermore,Wangetal.[21]combinedLSTMs theleakageimpactoftrainingsamplesprecedingtestsamples,as
withanattentionmechanism.
explainedbelow(Case2).
Opposedtothepresentedpublicationsinthissection,wedonot
focusonimplementingnewmodelsorincreasingtheaccuracyof
| currentmodelsforthetask.Instead,weshowtheimpactofdata |     |     |     |     |     | |D|      |              |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | -------- | ------------ | --- |
|                                                       |     |     |     |     | ,M  | ∑︁ ∑︁ ∑︁ | 𝑙(𝑿𝑖,𝑡 ,𝑿𝑖,𝑡 |     |
leakageusingasubsetofthesemodelsandverifytheexpressiveness L(M test train ):= ) (1)
1 2
ofourproposedmetric.WeusetheworkofDeSantoetal.[4] 𝑖=1 𝑿𝑖,𝑡1 𝑿𝑖,𝑡2
|           |                     |                      |              |     |     | ∈M test ∈M              | train |     |
| --------- | ------------------- | -------------------- | ------------ | --- | --- | ----------------------- | ----- | --- |
| and Lu et | al. [12] as a basis | for our experiments. | They provide |     |     |                         |       |     |
|           |                     |                      |              |     |     | (cid:40) 𝑒 − (𝑡 − 𝑡 ) , | 𝑡 𝑡   |     |
in f o r m a tio n o n th e m o d e l i n p u t s a nd outputs to use regarding 2 1 i f 2 ≥ 1
|     |     |     |     |     | 𝑙(𝑿𝑖,𝑡 ,𝑿𝑖,𝑡 | ):= |     | (2) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
s e q u e n ce le ng t hs a nd f ea t u r e s u s e d . 1 2 𝛼 𝑒− ( 𝑡 − 𝑡 ), i f 𝑡 < 𝑡
|               |     |     |     |     |     | 1 2          | 2 1         |     |
| ------------- | --- | --- | --- | --- | --- | ------------ | ----------- | --- |
|               |     |     |     |     |     | L(M ,M       | )           |     |
|               |     |     |     |     | L˜  | = test train | ,L˜ ∈ [0,1] |     |
| 3 DataLeakage |     |     |     |     |     | ,M           |             | (3) |
|               |     |     |     |     |     | L(M test     | test )      |     |
Inthiswork,weadoptthegeneraldefinitionofdataleakagepro-
𝑖,
vided by Kaufman et al. [10]: “Leakage [in data mining] is the In Equation 1, for each group the leakage contribution of
introductionofinformationaboutthetargetofadataminingprob- eachpairoftestdatapoints𝑿𝑖,𝑡 ∈ M andtraindatapoints
|     |     |     |     |     |     | 1 test |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- |
lemthatshouldnotbelegitimatelyavailabletominefrom.”[10] 𝑿𝑖,𝑡 ∈M trainissummedup.Thepair-wiseleakagecontribution
2
Further,webuilduponthecomprehensivetaxonomyproposedby 𝑙(𝑿𝑖,𝑡 ,𝑿𝑖,𝑡 ) isdefinedinEquation2.Itisdesignedsuchthata
1 2
KapoorandNarayanan[9]thataccountsformultiplecategoriesof smalltemporalproximitybetweentrainandtestdatapointshasa
dataleakage.Itoriginatesfromthefindingsintheirextensivesur- largeimpactontheoveralldataleakage,whiletheimpactdecreases
veyoncommonpitfallsinapplyingandevaluatingML/DLmodels. exponentiallyforincreasingtimedifferences.Anexampleforthe
Inthefollowing,wesummarizethethreemaincases. calculationofthepair-wiseleakagecontributionisillustratedin
Thefirstcase,alackofcleanseparationoftrainingandtestdata,is Figure1.Equation2distinguishestwocases:
≥
mainlyrelatedtopitfallsinthepreprocessingpipelines,forinstance, Case1(𝒕2 𝒕1)Thetestsampleprecedesthetrainingsample.
thatfeatureselectionorthefittingofscalersisperformedonthe ThisintroducestemporalleakageasdescribedinSection3.
entiredatasetinsteadofonlythetrainingdata,orthatduplicates Case2(𝒕2 <𝒕1)Theimpactofthesecondcasewherethetest
arenotdropped. sampleproceedsthetrainingsampleiscontrollablebyparameter𝛼.
336

ICPE’25,May05–09,2025,Toronto,Canada DanielGrillmeyeretal.
...
.
.
.
.
.
.
applicationofpreprocessingtechniques,forinstance,fitting
Train Set
scalerstotheentiredatainsteadofjustthetrainingdata,is
Test Set
outofscope.Therefore,theunderlyingassumptionisthat
thesepitfallsareavoidedwhenpreprocessingthedatabefore
applyingthemeasure.
(5) Theleakagemeasurereliesongrouplabelsassignedtothe
datasamples.Itisassumedthatthereisatleastonegroupand
thattemporaldependenciesbetweendatasampleswithin
thesamegroupexist.
4 Experiments
Figure1:Exampleforthecalculationoftheleakagecontri-
butionfortwopairsoftestandtrainobservations. Inthissection,wedescribethedesignofourexperimentstowards
answeringRQ2andRQ3indetail.Section4.1presentsthedifferent
datasplitstrategies. Section4.2introducesthedataset usedfor
Theparameter𝛼 shouldbechoseninalignmentwiththetask the experiments and defines the classification task. Section 4.3
forwhichaclaimisbeingmade.Ifthescientificclaimreferstothe explainstheconductedpreprocessingsteps.Section4.4addresses
predictiveperformanceonnovelgroupsnotseeninthetraining theadoptedML/DLmethods,hyperparameteroptimization,model
data,itshouldbesetto𝛼 >0suchthattrainingdataofthesame training,andevaluationprocess.Section4.5explainshowthePO
group,eveniflyinginthepast,hasacontributiontotheleakage measurementsareconducted.Section4.6providesdetailsabout
valueL.For𝛼 =1,precedingtrainingsamples(Case2)andpro- thehardwareandsoftwareconfiguration.Theoverallexperiment
ceedingtrainingsamples(Case1)ofthesamegroupcontribute workflowisillustratedinFigure2.
equallytoL.
Ifthescientificclaimreferstothepredictiveperformanceon 4.1 SplitStrategies
dataofgroupsalsousedtominefrom,itshouldbesetto𝛼 = 0. InaccordancewithRQ2,wepresentfourdifferentstrategiestosplit
Thus,precedingtrainingdataofthesamegroupislegitimateand adatasetintotrainingandtestsets.Ineachofthesplitstrategies
accordinglydoesnotcontributetoL.
exceptnosplit,weemployatrain/testsplitratioof70/30,asthisisa
Lastly,toobtainthefinalnormalizedleakagevalueL˜ ∈ [0,1]in
commonchoiceinpriorstudies[17,19,23].Theexaminationofthe
Equation3,wenormalizethesumofallpair-wiseleakagecontri- impactofdifferentsplittingratiosasafurtherdegreeoffreedomis
butionsbyfactorL(M
test
,M
test
).Thenormalizationfactorcorre-
beyondthescopeofthispaper.Rather,weaimtoinvestigatethe
spondstothecasethatallavailabledataisusedbothfortraining impactofdifferentsplitstrategiesontheresultingtestperformance
andtesting,yieldingthemaximumsumofleakagecontributions.In andtheirrespectiveextentofdataleakage.
theexperimentsinSection4.5,weapplythedataleakagemeasure ThestrategiesareillustratedinFigure3,whereeachhorizontal
L˜ ontheBackblazediskstatsdataset[2]. barillustratesthesequenceofallavailableobservations𝑶𝑖 fora
specificHDD𝑖.Thecolorsindicatetheportionsassignedtothe
3.2 Assumptions
trainingset(red)andthetestset(blue).Thefirststrategy,nosplit,
Althoughourproposeddataleakagemeasureisnotlimitedtoa isintendedtoserveasabaselinewherethewholedatasetisused
specifictaskordataset,itdependsonmultipleassumptions,which bothfortrainingandevaluatingthemodel’spredictiveperformance.
areaddressedbelow. Thesecondstrategy,randomsplit,separatesthedatarandomlyinto
trainandtestsets,regardlessofthetemporalorgroupinformation.
(1) Asthemeasureisbasedonthedifferenceoftimestamps,it
Thethirdstrategy,temporalsplit,isdesignedtopreventtemporal
requiresthatthecorrecttimestampsforallobservationsin
leakage.Allavailabledatabeforeandafter𝑡 isusedastraining
thedatasetareavailable.Iftimestampsareabsent,thedata split
andtestdata,respectively.Thelaststrategy,group-basedsplit,is
must instead consist of ordered sequences of equidistant
basedongroupsthatdependonthespecificdomain,forinstance,
observations,allowingtheascendingenumerationtoserve
definedbydifferentHDDspresentinthedataset.Eachgroupand
asaproxyfortimestamps.
itsassociateddataareassignedtothetrainingortestdata,but
(2) AccordingtoEquation1,onlypairsoftrainandtestsamples
notboth.Thus,thismethodisdesignedtoavoidleakagedueto
withinthesamegroupcontributetotheleakagevalueL.
non-independencebetweentrainingandtestsamples.
Thus,theunderlyingassumptionisthatpairsofsamplesof
Pleasenotethatthetrainingdataisfurthersplitintooneportion
differentgroupsareindependentandarethusnotsusceptible
usedforfittingthetrainableparameterswiththeoptimizer,and
toleakage.
onevalidationsetusedtotrackthemodel’spredictiveperformance
(3) Theleakagecontributionsareindependentofthefeature
andapplyearlystoppingwhenthevalidationlossstopsdecreasing.
values,butsolelydependonthetimedifference.
Forthissplit,thesamemethodisusedasforthepriorsplit,thatis,
(4) Themeasurecanonlyrepresentleakageintroducedbythe
wefurthersubdividethetrainingpartrandomly(b),splititintotwo
lastcategoryinthetaxonomybyKapoorandNarayanan[9],
thatis,amismatchbetweenthedistributions.Leakagecaused
temporalcomponentsbasedonanother𝑡(𝑣)
(c),orsub-selectsome
split
bytheuseofillegitimatefeatures,featureselectionontrain- harddisksasthevalidationpart(d).Fortheactualsplitstrategies,
ingandtestdata,duplicatesinthedataset,ortheincorrect weemployatrain/validation/testratioof60/10/30.Forthesakeof
337

QuantifyingDataLeakageinFailurePredictionTasks ICPE’25,May05–09,2025,Toronto,Canada
ML/DL models
BackblazeHDD HGBC RF MLP LSTM
Training data
statsdataset
Data Hyperparameter search
Split
leakage
strategy
measure Model training n=10 times
fordifferent
seeds
Test data Optimized& fittedModels
2014/2015
Pre-
processing Model evaluation
PO
Independent future evaluation
2016
testdata Model evaluation
Figure2:Overviewoftheexperimentworkflow.TheBackblaze[2]HDDdatasetsfrom2014/15and2016undergopreprocessing
independently.The2014/15datasetisthensplitintotrainingandtestdatausingfourdifferentsplitstrategies,onwhichour
dataleakagemeasureisapplied.ForeachsplitstrategyandeachML/DLmodel,ahyperparametersearchisconducted,followed
by𝑛=10trainingrunswithdifferentrandomseedsandsubsequentmodelevaluation.Additionally,thetrainedmodelsare
evaluatedontheindependentlyprocessed2016dataset.Basedontheseevaluations,performanceoptimismisanalyzed.
t
DDH
a) No split
t
DDH
b) Random split
t
DDH
c) Temporal split
t_split
t
DDH
Thedatasplittingstrategiesusedintheexperimentsareapplied
totheHDDdatafrom2014and2015,eventhoughmorerecent
releasesareavailable.Wemakethischoicetoenablecomparability
withrelatedworkusingthistimeperiod[1,4,17,19].Notethatmore
up-to-dateresultsareprovidedinapubliclyavailablerepository1.
Similarly,welimitourselvestothecommonlyusedHDDmodel
ST4000DM000[4,7,8,17,19].Itshowscomparablymanyfailures
(823)duringtheobservationperiod,ahighannualizedfailurerate
(2.96%),andthehighestnumberofdrivedays(10,154,343)inthe
Train Test
dataset.Theoretically,annualizedfailureratescanbelargerthan
d) Group-based split
100%.Valueslargerorequalto100%wouldimplythatadrivelasts
oneyearorlessonaverage[2].
ThesetofallavailableHDDsDcanbedisjunctlydividedintothe
setsD andD ofHDDsfailingintheobservationperiod
fail healthy
andthosethatdonot,respectively.Theformerareunderrepre-
sentedinthedataasreflectedbytheratio|D |/|D|=2.75%.For
fail
eachHDD𝑑 𝑖,thereisasequenceofobservations𝑶𝑖 =𝒐𝑖,1 ,...,𝒐𝑖,𝜏𝑖 ,
where𝜏 𝑖 denotesthelastrecordedday.Inthecaseof𝑑 𝑖 ∈ D fail ,
𝜏 𝑖 isthelastoperationalday.
Figure3:Illustrationofthedatasplitstrategies. WedefinetheRemainingUsefulLife(RUL)asthenumberof
remainingoperationaldaysfromtime𝑡 forHDD𝑑 𝑖,includingthe
currentday,asdepictedinEquation4.
simplicity,werefertothetrainingandvalidationsetstogetheras
(cid:40)
t
p
h
u
e
rp
tr
o
a
s
i
e
ni
o
n
f
g
o
s
p
e
t
t
im
in
iz
th
in
e
g
re
th
m
e
a
m
in
o
d
d
e
e
r
l
o
s.
fthispaper,sincebothservethe RUL(𝒐𝑖,𝑡)=
𝜏
∞
𝑖 −𝑡+1 i
i
f
f
𝑑
𝑑
𝑖
𝑖
∈
∈
D
D
f
h
a
e
i
a
l
lthy (4)
4.2 DatasetandProblemDefinition Toassigntheobservationsalabelformulticlassclassification,
fourhealthstatesbasedontheRULaredefinedinEquation5.We
ThispaperutilizesthewidelyusedBackblazediskstatsdataset[2]
definethecriticalclassbyaRULofsevendaysorless.Thisaligns
thathasbeenpubliclyavailablewithregularreleasessince2013.
withaBackblazearticlebyWilson[22],whichstatesthatseven
ForeachavailableHDD,uniquelyidentifiablebyitsserialnumber,
daysof“datarebuildtime”issufficientforafailed4TBHDD.Four
thereare124columnsofSelf-Monitoring,AnalysisandReporting
weeksorlessRULshouldyieldawarning.AhigherRULvalue
Technology(SMART)statistics,62columnseachforrawandnor-
indicatesafairorgoodhealthstate.
malizedvalues,andafailurecolumnwithabinaryhealthstatus
indicatingwhetheritisstilloperationalonthenextdayornot. 1https://github.com/DescartesResearch/Data-Leakage-HDD-Failure-Prediction
338

| ICPE’25,May05–09,2025,Toronto,Canada |     |     |     |     |     |     |     | DanielGrillmeyeretal. |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- |
Table1:SelectedSMARTfeaturesforHDDfailureprediction.
7
10
Original
| ID  | AttributeDescription |     | ID AttributeDescription |     |     |     |     |     |     |
| --- | -------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
Sampled
| 1   | Spin-UpTime |     | 189 UltraDMACRCErrorCount |     |     |     |     |     |     |
| --- | ----------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
6
| 3   | ReallocatedSectorsCount |     | 192 ReadErrorRate               |     |           | 10  |     |     |     |
| --- | ----------------------- | --- | ------------------------------- | --- | --------- | --- | --- | --- | --- |
| 4   | SeekErrorRate           |     | 193 Start/StopCount             |     | ycneuqerF |     |     |     |     |
| 5   | Power-OnHours           |     | 194 SpinRetryCount              |     |           |     |     |     |     |
| 7   | PowerCycleCount         |     | 195 ReportedUncorrectableErrors |     |           |     |     |     |     |
| 9   | HighFlyWrites           |     | 197 LoadCycleCount              |     |           | 5   |     |     |     |
10
| 10  | Power-offRetractCount |     | 198 HardwareECCRecovered      |     |     |     |     |     |     |
| --- | --------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
| 12  | Temperature           |     | 199 CurrentPendingSectorCount |     |     |     |     |     |     |
187 UncorrectableSectorCount
10 4
|          |           |          |                      |     |     |     | critical warning | fair    | good |
| -------- | --------- | -------- | -------------------- | --- | --- | --- | ---------------- | ------- | ---- |
|          | " g o o   | d" i f R | U L ( 𝒐 ) = ∞        |     |     |     |                  |         |      |
|          |    |          | 𝑖 , 𝑡                |     |     |     |                  | Classes |      |
|          | " fa i r" | i f R    | U L ( 𝒐 𝑖 , 𝑡 ) > 28 |     |     |     |                  |         |      |
| 𝑐(𝒐𝑖,𝑡)= |           |          |                      | (5) |     |     |                  |         |      |
>
|     |  " w a r | n in g" i f R | U L ( 𝒐 𝑖 , 𝑡 ) 7 andRUL(𝒐𝑖,𝑡) | ≤28 |        |          |              |                  |           |
| --- | ------------- | ------------- | ------------------------------ | --- | ------ | -------- | ------------ | ---------------- | --------- |
|     |               |               |                                |     | Figure | 4: Class | distribution | of the Backblaze | HDD stats |
|     | "c r it       | i ca l" i f R | U L ( 𝒐 𝑖 , 𝑡 ) ≤ 7            |     |        |          |              |                  |           |

dataset(2014/15)withlogarithmicfrequencyscale.
| We  | define the | multiclass | HDD failure prediction | problem as |     |     |     |     |     |
| --- | ---------- | ---------- | ---------------------- | ---------- | --- | --- | --- | --- | --- |
|     |            |            | associatedwithHDD𝑑     | 𝑖andtime𝑡, |     |     |     |     |     |
follows.Givenobservations𝑿𝑖,𝑡
thegoalistoinferthecorrespondinghealthstate𝑐(𝒐𝑖,𝑡)from𝑿𝑖,𝑡
whichisasequenceof𝑇 equidistantobservationsasdepictedin morefeasible,wereducetheportionofthemajorityclassinthe
secondpreprocessingstepbyrandomuniformsamplingof2.5%of
| Equation6.Weset𝑇 |     | = 8throughouttheexperiments,whichis |     |     |     |     |     |     |     |
| ---------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
similartothestudybyLyuetal.[13],whouseaone-weekhistory. thegood HDDs.Thedataset’sclassdistributionbeforeandafter
samplingisshowninFigure4.Withoutsampling,itrevealsaclear
,...,𝒐𝑖,𝑡−1 ,𝒐𝑖,𝑡 imbalance.Theclassgoodmakesup97.6%ofthedata,whilethe
|     |     | 𝑿𝑖,𝑡 =𝒐𝑖,𝑡−𝑇+1 |     | (6) |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
accountsforonly0.0557%ofthedata.
InadditiontotheclassesdefinedinEquation5thatareused mostcrucialclasscritical
Aftersampling,thedatasetsizeisdecreasedby95.28%,andtheclass
formodeltraining,similartopriorwork[4],wedefineacoarse-
grainedpartitioning𝑐 imbalanceisreduced.Despitethepossibilityoftherebyintroducing
cgintotwoclassesforbinaryclassification
asamplingbias,weassumethegoodclass,stillbeingthelargest
evaluation,asformalizedinEquation7.Thefailureclassindicates
class,remainssufficientlyrepresentedinthedataset.
animpendingfailurewithinoneweek,whiletheoperationalclass
Third,theSMARTfeaturesareselectedbasedonpriorwork[4,
indicatesaRULofmorethanoneweek.
12]onHDDfailurepredictionandSMARTfeatureselection.In
(cid:40) >7 addition,featureswithamissingdatarateofmorethan20%are
|     |     | "operational" | ifRUL(𝒐𝑖,𝑡) |     |     |     |     |     |     |
| --- | --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- |
𝑐 cg (𝒐𝑖,𝑡)= (7) discarded,asweaimtorelyonreliablyrecordedfeaturesonly.The
|     |     | "failure" | ifRUL(𝒐𝑖,𝑡) | ≤7  |     |     |     |     |     |
| --- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
adoptedfeaturesarelistedinTable1.Thisincludesboththeraw
Weintendtousethefine-grainedlabels𝑐 formodelfittingto and normalized versions of these features as provided by Back-
enabletheMLandDLmethodstoobtainmoredetailedsupervi-
blaze[2].Weassumethatthewell-knownandestablishedSMART
sionandfeedbackinthetrainingprocessandfacilitatelearning
measurementsarelegitimatefeaturessincethesecanbecontinu-
moresubtledifferencesbetweendifferenthealthstates.Thecoarse- ouslymeasured.Thus,theiravailabilityforinferencecanbepre-
grainedlabels𝑐
cg,ontheotherhand,allowabetterunderstandable sumed.Further,tothebestofourknowledge,noneofthefeatures
andinterpretableevaluationofthepredictiveperformance,asestab- isaproxyfortheoutcomevariable,asitwouldpossiblybethecase
lishedbinaryclassificationmetricscanbeapplied.Thepartitioning
fortheSMART231feature(LifeLeft)forSolidStateDrives(SSDs).
| is based | on practical | considerations | in the Backblaze | article by |     |     |     |     |     |
| -------- | ------------ | -------------- | ---------------- | ---------- | --- | --- | --- | --- | --- |
Inthefourthpreprocessingstep,missingvaluesarehandled.
Wilson[22]. Observations𝑿𝑖,𝑡 withatleastonemissingSMARTfeaturevalue
aredropped.Weperformthisstepafterthefeatureselectionto
4.3 DataPreprocessing avoiddroppingobservationswithmissingvaluesoffeaturesthat
Thepreprocessingpipelineusedthroughouttheexperimentscon- arediscardedanyway.
sistsofmultiplesteps,asexplainedinthefollowing: Fifth,zero-variancefeaturesarediscardedsincetheypossessno
In the first preprocessing step, we identify and, if necessary, predictivepower.Sixth,thedataissplitintotrainingandtestdata,
removepossibleduplicateobservationsinthedatasettoensure dependingonwhichofthesplitstrategiesproposedinSection4.1
| thateachsequence𝑿𝑖,𝑡 |     | isunique.However,fortheaforementioned |     |     | isselected. |     |     |     |     |
| -------------------- | --- | ------------------------------------- | --- | --- | ----------- | --- | --- | --- | --- |
HDDmodelandtimeperiods,wedidnotfindduplicatesinthe Lastly,thedataisscaled.EachofthelistedfeaturesinTable1isin-
dataset. cludedwithrawandnormalizedvaluesasprovidedbyBackblaze[2].
Duetothelargedatasetsize,thetrainingofDLmodelsiscompu- WescaletherawSMARTfeatureswiththeQuantileTransformer
tationallyexpensiveandtime-consuming.Tomaketheexperiments byscikit-learn[16]becauseitisrobustagainstextremeoutliers
339

QuantifyingDataLeakageinFailurePredictionTasks ICPE’25,May05–09,2025,Toronto,Canada
presentinsomerawfeatures.Additionally,westandardizethenor- thefailurelabel,whilenegativescorrespondtooperationalsamples
malizedSMARTfeatureswiththeirmeanandstandarddeviation. (seeEquation7).
Topreventdataleakageinthescalingprocess,weexclusivelyfit
thescalersonthetrainingdata. 4.5 PerformanceOptimism
4.4 ModelValidation AsdiscussedinSection3,thetestsetonwhichMLandDLmodels
areevaluatedtoproveascientificclaimmustberepresentativeof
PredictiveModelsWechooseavarietyofmulticlassclassification
thedatatheclaimisstatedfor.Otherwise,amodel’sabilitiesonthe
modelsthatarecommonlyusedinrelatedwork,includingMLen-
testsetmightstronglydeviatefromtheperformanceinareal-world
sembleandDLmodels.TheselectionofmethodsincludesHGBC,
scenario,possiblyleadingtounrealisticandover-optimisticresults
RF,MLP,andLSTM.FortheHGBCandRF,wechoosetheimple-
andexpectations,denotedasPerformanceOptimism(PO).Tofind
mentationinthescikit-learn[16]Pythonpackage.TheMLPand
ananswertoRQ3,wemeasureandcomparethePOofdifferent
LSTMareimplementedinPyTorch[15].Forthetrainingprocedure,
splittingstrategiesandMLandDLmodels.Therefore,inaddition
thePyTorchLightning[5]frameworkisusedwiththeAdamW [11]
tothetestsetsobtainedbythedifferentsplittingstrategies,we
optimizer,weightedCrossEntropy(CE)lossandearlystopping.The
defineaseparateandindependenttestsetthatisassumedtobe
weightsoftheCElossareproportionaltotheinversefrequency
representativeofthedataofscientificinterest.
ofthelabelsinthetrainingdata.Thebatchsizeis32,theearly
The independent test set consists of the Backblaze disk stats
stoppingpatienceis15andtheminimumdeltais0.01,whilethe
dataset[2]fortheyear2016.Thus,itisguaranteedthatalltraining
bestlearningrateisdeterminedviahyperparameteroptimization.
andtestdatausedinthepreviousexperimentstepsisolderthan
HyperparameterOptimizationToensureafaircomparison
thisdataset.
ofthedifferentMLandDLmethods,theBayesianoptimizerHy-
ThePOisdefinedasthedifferencebetweenthemodels’predic-
peropt[3]isusedtoexplorethehyperparameterspaceandfindthe
tiveperformanceonthetestsetthatisobtainedviatherespective
configurationwiththebestvalidationlossforeachmodelanddata
splittingstrategyappliedtotheHDDstatsdatafrom2014/2015,
splitstrategy.Thenumberofrequiredtrialsisestimatedbyfollow-
andtheperformanceontheindependenttestsetfrom2016.
ingtheguidancebyOwen[18].Theconfigurationsfoundtodeliver Further,tovalidateourproposeddataleakagemeasureL˜,weap-
thebestvalidationlossareusedinthefollowingexperiments.More
plyEquation3tothetrainingandtestsetsobtainedbythedifferent
detailscanbefoundintheappendixinSectionB.
splittingstrategies.Weexaminewhetherourproposedmeasure’s
TrainingandEvaluationInthenextstepoftheexperiments,
valuesalignwiththemeasuredPO.
thetrainingisrepeated𝑛=10timesforeachmodelandsplitting
strategy,varyingtherandomseedforeachoftheruns.Thisproce-
4.6 HardwareandSoftwareConfiguration
dureallowsreliablestatementsabouttheperformanceofthemulti-
classpredictionmethodsonthetestsetbyeliminatingstatistical TheexperimentsareconductedonaserverfeaturingtwoAMD
fluctuationsduetorandomnessinthemodelweightinitialization EPYC 7763 64-core processors @2.45 GHz and 256GB of RAM.
orthedatasplitting,forexample.Thisenablesanaccurateevalua- Additionally,theserverhousestwoNVIDIAA100GPUswith80GB
tionofthepredictiveperformanceandafaircomparison.Thetest VRAM.EachGPUissplitintothreevirtualdeviceswithdifferent
resultsfrommultiplerunsareaggregatedbycomputingthemean VRAMcapacities.FortheDLexperiments,a40GBinstanceofGPU2
andsamplestandarddeviation.Thelatterispreferredovertheusual isused.TheserverrunsUbuntu22.04.2.
populationstandarddeviation,astheresultsofthe𝑛 = 10runs TheprojectcodeiswritteninPythonandpubliclyavailableto
representarandomsampleofallpossiblerandominitializations. fosterreproducibility2.WeusePython3.11toruntheexperiments.
DetailsabouttheusedPythonpackagesandtheirversionsarelisted
TP intheappendixinSectionA.
precision:=
TP+FP
TP 5 Evaluation
recall:=
TP+FN
InSection5.1,weapplyourproposedmeasureforquantifyingdata
TN
specificity:= leakage(RQ1)onthesplittingstrategiespresentedinSection4.1
TN+FP
(8) toevaluatetheirextentofdataleakageandanswerRQ2.InSec-
precision×recall
F1:=2 tion5.2,weassessthemodels’predictiveperformancebasedon
precision+recall
differentsplittingstrategiesandadditionallyonanindependent
√︁
Gmean:= recall×specificity futuretestdataset.InSection5.3,weevaluatetheconsistencyof
TP×TN−FP×FN themodels’predictiveperformance,thatis,examinetheexistence
MCC:=
√︁ ofPOconcerningdifferentsplittingstrategiesandclassification
(TP+FP)(TP+FN)(TN+FP)(TN+FN)
metrics(RQ3).Further,werelatetheseresultstotheextentofdata
Wequantifythepredictiveperformancebystandardclassifica- leakageindicatedbyourproposedmeasure.
tionmetrics.TheseincludeF1score,GmeanandMatthewsCorrela-
tionCoefficient(MCC).Thedefinitionofthesemetricsisprovided
inEquation8.TPandFPdenotetrueandfalsepositives,TNand
FNtrueandfalsenegatives,respectively.Positivescorrespondto 2https://github.com/DescartesResearch/Data-Leakage-HDD-Failure-Prediction
340

ICPE’25,May05–09,2025,Toronto,Canada DanielGrillmeyeretal.
5.1 DataLeakageMeasure (usecase2),wherealsotrainingsamplesthatprecedetestsamples,
Toevaluateourproposeddataleakagemeasure,weemploythe ifinthesamegroup,contributetotheleakagevalue.
fourpresenteddatasplittingtechniquesontheBackblazediskstats The temporal split technique (Figure 3 - c) performs a clean
dataset[2]from2015/2016.Then,weapplyourmeasure(Equation3) temporalseparationatacertainpointintime𝑡 split .Thisprevents
onthedifferentsplitstoanswerRQ2.Asdescribedattheendof temporalleakageasitguaranteesthatnofuturetrainingexamples
Section4.1,thetrainingsetalsoincludesthevalidationsetforthe
existforeachtestsample.Correspondingly,inthecaseof𝛼 =0,the
computation.Table2showsthenormalizeddataleakagevalueL˜ leakagemeasurevalueis0.0.However,thetemporalsplitdoesnot
forthedifferentdatasplittingtechniquesandtwodifferent𝛼values respectthedependencestructureofthestrictertaskofpredicting
failuresfornovelunknowngroups.Thisisbecausethetestdatacon-
0and1.AsdescribedinSection3.1,thesetwovaluescorrespond
todifferentpredictiontasks.For𝛼 =0,trainingsamplesthatare tainsdataofthesamegroupsasthetrainingdata.Correspondingly,
themeasureyieldsavalue>0(thirdrowinTable2).
lyingtemporallybeforeatestsampleofthesamegrouparenot
Lastly,thegroup-basedsplitstrategy(Figure3-d)guarantees
consideredleaks.Therefore,itcorrespondstoapplicationscenarios
thatdatabelongingtothesamegroupisnotsplitbetweentrain
wherepredictionsinthefuturearemadeforgroupsthatarealso
usedtotrainthemodel(usecase1).For𝛼 > 0,onthecontrary, andtestset.Undertheassumptionthatnodependenciesbetween
thedifferentgroupsexist(seeSection3.2),forinstance,thateach
theseaforementionedtrainingsamplesareconsideredleaks.This
HDDwearsoutindependentlyovertime,thisensuresindependence
correspondstomakingpredictionsfornovelgroupsnotseenduring
training(usecase2).Wechoose𝛼 =1sothatthesesamples’leakage betweentrainandtestsamples.Consequently,nofuturetraining
sampleinthesamegroupcanexistforeachtestsample,ruling
contribution is weighted equally to temporally leaked training
out temporal leakage. This is reflected by a zero leakage value,
samples.Ourgoalistovalidatethemeasureconceptually.Thetwo
selected𝛼 valuesdemonstrateitsapplicabilityandbehavior,while independentofthechoiceof𝛼 (lastrowinTable2).
anexhaustiveparameterstudyisbeyondthescopeofthispaper,
asfurtherdiscussedinSection6. 5.2 ModelValidation
Inthebaselinestrategynosplit(Figure3-a),allavailabledata Themeanvalueandsamplestandarddeviationfrom𝑛=10runs
isusedbothastrainingandtestsets.Thisimpliesthatforeachtest withdifferentrandomseedswerecalculatedforreliableresults.
sample,allexistingfutureobservationsmustbeinthetrainingset, Table3showstheevaluationresultsforthedifferentmodels,split-
thusleadingtomaximumtemporalleakage.Further,themaximum tingtechniques,andclassificationmetrics.Thevaluesinthefirst
dependencybetweentrainandtestsamplesexistssinceeachtest fourrowsrefertothetestperformanceonthetestsetsobtained
sample is also present in the training set. These properties are bythesplittingtechniques(Section4.1)appliedtothe2014/2015
reflectedbythemaximumnormalizedleakagevalueof1.0,since
HDDstatsdata.Forthenosplit baseline,theensemblemethods,
themetricisnormalizedonthisextremecase(firstrowinTable2). especiallyRF,reachsuperiorresults,indicatingthattheyperfectly
Intherandomsplitstrategy(Figure3-b),allavailabledatais memorizedthetrainingdataset.TheDL-basedmethodsalsoshow
splitregardlessoftemporalorgroupinformation.Thismightlead near-perfectscores;however,withdeductionsforF1andMCCfor
totemporalleakage,sinceforeachtestsample,atatrain/testratio theMLPmodel.Fortherandomsplit,themodelsstillshowpromis-
of70/30,70%ofallexistingfutureobservationsarestatisticallyex- ingresults,especiallyRFwithanGmeanof0.91±0.01,whileLSTM
pectedtobeinthetrainingset.Further,non-independencebetween andMLPareslightlyworsewith0.86±0.01and0.81±0.05,re-
trainandtestsamplesmightbeintroducedduetoclosetemporal spectively.Fortheremainingsplittingtechniquestemporal
proximityofsampleswithingroups.Thisleadstoadependence andgroup-based,acleardropintestperformanceisevident
structurethatdoesnotexistbetweentrainingdataandnovelfuture acrossallmodelsandmetrics.Particularlynoteworthyisthe
data.Thenormalizedleakagevaluereflectstheseleakageissues deteriorationoftheMCCforRFandthetemporalsplit,whichis
withavalueof0.34for𝛼 = 0and0.59for𝛼 = 1(secondrowin reducedby0.75comparedtotherandomsplit.Incomparison,the
Table2).Thevalueislowerfor𝛼 = 0becauseitisbasedonthe differencesbetweentemporalandgroup-basedsplitareratherneg-
assumptionthatdatafromagroupisallowedtobesplitbetween ligible.
trainingandtestdata(usecase1).For𝛼 = 1,ontheotherhand, Next,thetrainedmodelsoptimizedforthedifferentsplitstrate-
thevalueishigherbecausethiscorrespondstothestricterscenario giesaretestedontheindependentlyprocessedfuturetestdatawith
HDDstatsdatafrom2016.LetD 2016bethecorrespondingsetof
HDDsofthesameHDDmodelST4000DM000asbefore.Acompari-
sonwiththesetofHDDsD 2014/2015 inthe2014/2015datasetshows
Table2:Dataleakagemeasureresults. that |D 2014/2015 ∩D 2016 | =81.5%oftheHDDswerealreadypresentin
|D |
2016
thepreviousdataset.
DataLeakageL˜
Split Theresultsonthe2016dataareshowninthelatterfourrowsin
𝛼 =0 𝛼 =1 Table3.FortheDL-basedmodelsMLPandLSTM,theperformance
ofthemodelstrainedwiththenosplitandrandomsplitstrategies
Nosplit 1.0 1.0
showanoverallworseperformancethanthosefromtheothertwo
Random 0.34 0.59
Temporal 0.0 2.0×10−3 strategies.Thismeetstheexpectationbecausethemodelstrained
withthetemporalorgroup-basedstrategiesmightbemorelikely
Group-based 0.0 0.0
optimizedtogeneralizetounknownfutureperiodsorHDDsdue
341

QuantifyingDataLeakageinFailurePredictionTasks ICPE’25,May05–09,2025,Toronto,Canada
Table3:Performanceofmodelstrainedandtestedwithdifferentsplitstrategiesappliedtothe2014/15datasetandperformance
ontheheld-outfuturetestdatafrom2016.
HGBC RF MLP LSTM
Split F1 Gmean MCC F1 Gmean MCC F1 Gmean MCC F1 Gmean MCC
2014/2015
(Train&Test)
Nosplit 0.94±0.07 0.99±0.00 0.94±0.06 1.00±0.00 1.00±0.00 1.00±0.00 0.71±0.03 0.96±0.01 0.73±0.03 0.93±0.03 0.99±0.00 0.93±0.02
Random 0.59±0.05 0.75±0.01 0.59±0.05 0.87±0.01 0.91±0.01 0.87±0.01 0.39±0.09 0.81±0.05 0.42±0.08 0.53±0.02 0.86±0.01 0.55±0.02
Temporal 0.17±0.01 0.42±0.03 0.16±0.01 0.12±0.01 0.34±0.02 0.12±0.01 0.09±0.02 0.64±0.03 0.12±0.02 0.10±0.03 0.63±0.05 0.13±0.02
Group-based 0.14±0.02 0.48±0.02 0.14±0.01 0.14±0.02 0.43±0.03 0.14±0.02 0.13±0.02 0.67±0.02 0.17±0.01 0.14±0.01 0.67±0.02 0.17±0.01
2016
(Testonly)
Nosplit 0.14±0.04 0.54±0.04 0.15±0.04 0.15±0.02 0.54±0.02 0.15±0.01 0.10±0.01 0.58±0.02 0.12±0.01 0.12±0.01 0.56±0.02 0.13±0.01
Random 0.16±0.02 0.55±0.02 0.16±0.01 0.15±0.02 0.53±0.02 0.16±0.02 0.09±0.01 0.62±0.02 0.12±0.01 0.11±0.01 0.60±0.03 0.13±0.01
Temporal 0.14±0.02 0.50±0.06 0.14±0.03 0.14±0.02 0.47±0.01 0.14±0.01 0.12±0.04 0.67±0.02 0.15±0.03 0.12±0.05 0.66±0.02 0.15±0.05
Group-based 0.11±0.02 0.51±0.06 0.11±0.02 0.14±0.02 0.55±0.03 0.15±0.02 0.13±0.04 0.69±0.01 0.17±0.04 0.17±0.02 0.70±0.01 0.21±0.02
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
FalsePositiveRate(FAR)
)RDF(etaRevitisoPeurT
MeanROCCurve(AUC=0.99±0.00)
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
FalsePositiveRate(FAR)
(a) Randomsplit
2014/15(Train&Test)
)RDF(etaRevitisoPeurT
MeanROCCurve(AUC=0.70±0.01)
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
FalsePositiveRate(FAR)
(b) Randomsplit
2016(Testonly)
)RDF(etaRevitisoPeurT
MeanROCCurve(AUC=0.75±0.01)
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
FalsePositiveRate(FAR)
(c) Temporalsplit
2014/15(Train&Test)
)RDF(etaRevitisoPeurT
MeanROCCurve(AUC=0.73±0.01)
(d) Temporalsplit
2016(Testonly)
Figure5:ROCcurvesofLSTMtrainedandtestedwithtwosplittingstrategiesappliedtothe2014/15datasetandrespective
performanceontheheld-outfuturetestdatafrom2016.Theshadedareasindicatethesamplestandarddeviation.
tothesplitchoiceandthecorrespondingnatureofthevalidation thetest(AUC=0.75±0.01)ismuchmoreconsistentwiththeresult
data. ontheindependentfuturedataset(AUC=0.73±0.01).Theuseof
Incontrast,theensemblemethodsHGBCandRFhavetheten- therandomsplit,therefore,leadstoadrasticoverestimation,that
dencytoachievebetterresultsonthe2016datasetwhentrained is,PerformanceOptimism(PO),ofthemodel’scapabilities.This
onthewhole2014/2015dataset,thatis,withthenosplitstrategy. willbefurtherinvestigatedinSection5.3.
Consequently,theyshowmorerobustnessagainstoverfittingthan
theDLmethodsandseemtoprofitfrommoretrainingexamples. 5.3 PerformanceOptimism
Overall,theensemblemethods’performanceontheindependent
ThegoalofthissectionistofindananswertoRQ3bycomparing
test data isbarelyaffected by the choiceof splitting method in
thepredictiveperformanceofmultipleML/DLmodelsfordifferent
thetrainingprocedure.Nevertheless,dependingonthecho-
splittingstrategiesandonanindependentheld-outdataset.
sensplitmethod,thepredictivepowermightbedrastically
Table4providesthePOofthedifferentsplittingstrategiesacross
overestimated,asfurtherdiscussedbelow.
multiplemodels.Basedonpriorwork[13],thePOforacertain
Mostimportantly,theconsistencyoftheperformancebe-
metricisdefinedasthedifferencebetweenthemetricvaluesfrom
tweentheindependentevaluationonthe2016datasetand
theevaluationonthetestsetfromthesplittingstrategyandthe
the2014/15datasetstronglydependsontheadoptedsplitting
independentlyprocessedfuturetestdata,respectively.Therefore,
strategy.ThiscanalsobeseenincomparingtheROCcurvesof
positivePOvalues(inred)indicatetheoverestimationofamodel’s
themodels.Toexemplify,weshowtheROCcurvesoftheLSTMin
predictive capabilities, while zero or negative values (in green)
Figure5.Iftherandomsplitisused,analmostperfectperformance
indicatearealisticorunder-estimation.
withAUC=0.99isobtainedonthetestdataset.However,thisout-
ThefirsttworowsinTable4showclearlythattheresultsob-
standingresultcannotbeconfirmedontheindependentfuture
tained from no split and random split cannot hold on the inde-
dataset,whereweobserveasignificantdroptoAUC=0.70±0.01.
pendenttestset.Forthebaselinetechniquenosplit,theF1/MCC
Ontheotherhand,ifthetemporalsplitisused,theperformanceon andGmean optimismisupto0.85and0.46,respectively.These
342

| ICPE’25,May05–09,2025,Toronto,Canada |     |     |     |     |     |     |     |     |     | DanielGrillmeyeretal. |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- |
Table4:PerformanceOptimism(PO)ofdifferentsplitstrategies.Redvaluesindicateanoverestimationofthepredictivepower,
greenvaluesindicatearealisticorunderestimation.
|       | HGBC     |     |     | RF    |     |     | MLP   |     |     | LSTM  |     |
| ----- | -------- | --- | --- | ----- | --- | --- | ----- | --- | --- | ----- | --- |
| Split | F1 Gmean | MCC | F1  | Gmean | MCC | F1  | Gmean | MCC | F1  | Gmean | MCC |
2014/2015
Nosplit 0.80±0.08 0.45±0.04 0.80±0.07 0.85±0.02 0.46±0.02 0.85±0.01 0.61±0.03 0.38±0.03 0.61±0.03 0.81±0.03 0.43±0.02 0.80±0.03
0.43±0.05 0.21±0.03 0.42±0.06 0.71±0.02 0.38±0.02 0.71±0.02 0.30±0.09 0.19±0.05 0.31±0.08 0.43±0.03 0.27±0.03 0.42±0.03
Random
Temporal 0.03±0.03 −0.08±0.06 0.02±0.03 −0.02±0.02 −0.13±0.03 −0.02±0.02 −0.02±0.04 −0.04±0.03 −0.03±0.04 −0.03±0.06 −0.03±0.05 −0.03±0.05
0.04±0.03 −0.03±0.06 0.03±0.03 0.00±0.02 −0.12±0.04 −0.01±0.02 0.00±0.04 −0.02±0.02 0.00±0.04 −0.04±0.03 −0.02±0.03 −0.03±0.02
Group-based
|     | Nosplit Temporal |     |     |     | Nosplit | Temporal |     |     | Nosplit | Temporal |     |
| --- | ---------------- | --- | --- | --- | ------- | -------- | --- | --- | ------- | -------- | --- |
1.0 Random Group-based 1.0 Random Group-based 1.0 Random Group-based
| 0.8            |            |      | 0.8           |      |          |     |      | 0.8         |         |     |      |
| -------------- | ---------- | ---- | ------------- | ---- | -------- | --- | ---- | ----------- | ------- | --- | ---- |
|                |            |      | msimitponaemG |      |          |     |      | msimitpoCCM |         |     |      |
| msimitpo1F 0.6 |            |      | 0.6           |      |          |     |      | 0.6         |         |     |      |
| 0.4            |            |      | 0.4           |      |          |     |      | 0.4         |         |     |      |
| 0.2            |            |      | 0.2           |      |          |     |      | 0.2         |         |     |      |
| 0.0            |            |      | 0.0           |      |          |     |      | 0.0         |         |     |      |
| 0.2            |            |      | 0.2           |      |          |     |      | 0.2         |         |     |      |
| − HGBC         | RF MLP     | LSTM | −             | HGBC | RF       | MLP | LSTM | −           | HGBC RF | MLP | LSTM |
|                | (a)F1score |      |               |      | (b)Gmean |     |      |             | (c)MCC  |     |      |
Figure6:PerformanceOptimism(PO)formultipledatasplittingtechniquesandML/DLmodels.
resultsforthenosplitmethodconfirmtheexpectationsthat • Asexpected,thebaselinestrategynosplitconsistentlyshows
aML/DLmodelperformsbetteronthetrainingdatathanon the highest PO, which is in line with the corresponding
|     |     |     |     |     |     | maximumleakagevalueL˜ |     |     | =1.0. |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ----- | --- | --- |
held-outtestdata.
Forthecommonlyusedrandomsplittechnique,thePOiscon- • Therandomsplitstrategyshowstobesusceptibletoover-
sistently lower than for no split. However, it is still remarkably estimatingthemodel’sperformance.Thetemporalleakage
high.Mostofall,theRF’sF1/MCCandGmeanoptimismamountsto andnon-independencebetweentrainandtestsamplesin-
0.71±0.02and0.38±0.02,respectively.Foralltestedmodelsand
ducedbythissplittingstrategyisaviableexplanation,and
|     |     |     |     |     |     | isreflectedbyavalueofL˜ |     |     | =0.34for𝛼 | =0andL˜ | =0.59 |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --------- | ------- | ----- |
classificationmetrics,theusageoftherandomsplitleadsto
adrasticoverestimationofthepredictiveperformance. for𝛼 =1,respectively.
Incontrast,thetemporalsplitshowsconsiderablylowerPOval- • Theremainingtwosplitstrategiestemporalandgroup-based
ues(thirdrowinTable4).Withinthestandarddeviation,allvalues splitshowedtoallowforarealisticestimationofthemodel
areequaltoorevensmallerthan0.Thisisalsotrueforthegroup-
performance.Weareconfidenttoconcludethisfromthefact
basedsplit(lastrowinTable4),exceptforoneoutlier,namelythe thatthesestrategiesavoidtemporalleakagebydesign.Thus,
F1optimismof0.04±0.03fortheHGBC.However,thePOval-
theirtestdatasetbetterrepresentsthedistributionofthe
uesfortemporalandgroup-basedsplitareconsistentlycompatible samplesintheindependentfuturedatasetthatweassume
withinthelimitsofthestandarddeviation.Consequently,for toberepresentativeofthedistributionofscientificinterest.
alltestedmodelsandclassificationmetrics,theusageofthe ThisalignswiththeleakagevalueofL˜ =0.0for𝛼
=0.
=1,theL˜
temporalorgroup-basedsplitleadstoarealisticestimation • For𝛼 valueslightlydiffersbetweenthetemporal
ofthepredictiveperformance. andgroup-basedsplitstrategy,whichisnotreflectedinthe
For all metrics, the PO is plotted in Figure 6, illustrating the POevaluationresults.Thismightbeduetothefactthatthe
muchhigherPOfornosplitandtherandomsplitcomparedtothat
independentfuturetestdatasetfrom2016correspondsto
ofthetemporalorgroup-basedsplit,whichismostlyequaltoor thetaskrelatedto𝛼
= 0,thatis,predictingondatafrom
evensmallerthanzero.Acrossallmodels,theGmeanoptimismis alreadyknowngroupsorHDDs,asdiscussedinSection5.1.
lowercomparedtotheothermetrics.FortheRFmodelandthe
| temporal andgroup-based | split,itevenexhibitsnegativevalues |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of−0.13±0.03and−0.12±0.04,respectively,indicatingaclear
|     |     |     |     |     |     | Overall, | the extent | of data | leakage | as indicated | by our |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | ------- | ------------ | ------ |
underestimationofthemodel’spredictivecapabilitiesintermsof
proposedmeasureL˜
| Gmean. |     |     |     |     |     |     |     | alignswiththeexperimentalresults, |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- |
offeringaviableexplanationforthedifferencesbetweenthe
Weconcludethissectionbyrelatingthesefindingstothevalues
PerformanceOptimism(PO)inducedbydifferentsplitting
ofourpresentedleakagemeasureinSection5.1.
strategies.
343

QuantifyingDataLeakageinFailurePredictionTasks ICPE’25,May05–09,2025,Toronto,Canada
6 ThreatstoValidity information.Nevertheless,weareconfidentthatforsimilarorequal
Inthefollowing,weidentifypossiblethreatstothevalidityofthe datasetproperties,likeintheexperimentsconductedinthispaper,
experimentalresultsdiscussedinSection5. themeasureallowsforaquantifiableassessmentofdataleakage.
Comparingpredictionsforlong-termfuturedatasetscarriesthe
7 Conclusion
inherentriskofconceptdrift.However,sinceweassessmodelper-
formanceonadatasetfromjustoneyearlater,wheremostlythe Cloudcomputing’sgrowingimportanceinrecentyearswillcon-
sameHDDsarestillinuse,weareconfidentthatanyobserved tinueinthefuture,especiallyasgenerativeAIbecomesmorecom-
changesinmodelperformanceareunlikelytobeimpactedbycon- mon.Akeyfactorinthesuccessofcloudcomputingisareliable
ceptdrift. operationtowhichHDDshaveasignificantimpact.Monitoreddata
TheSMARTfeatureLifeLeft,availableonlyforSSDs,couldserve ofHDDscanbeusedtopredictfailuresandproactivelyreplace
asaproxyforpredictingRUL.However,sinceourfocusissolely affectedelements.Failurepredictionisanalreadywell-researched
onHDDs,andtheobjectiveofthispaperisnottoidentifythebest field.However,cleanpreprocessingandtheavoidanceofdataleak-
model,usingonlySSDsandincorporatingthisfeaturewouldmost agecannotbeverifiedforallpublications.Inthispaper,wepropose
likelynotaltertheobservedeffectofPO. anovelmeasureforquantifyingdataleakageinpredictiontasks.
Tobalanceandreducethesizeofthedataset,wedown-sampled Further, we present four techniques for splitting a dataset into
thegoodHDDsto2.5%.Thissamplingapproachmayhaveintro- trainingandtestdatawithdifferentamountsofdataleakage.We
ducedsomebias,potentiallyimpactingtheresults.However,ran- evaluatetheimpactofdataleakagequantifiedwithourproposed
domsamplingwasused,andthegoodclassremainedthelargest measureontheperformanceofasetofcommonlyusedclassifica-
classand,therefore,sufficientlyrepresented.Moreover,thegoalof tionmodels.Ourresultsconsistentlyshowthatsplittingtechniques
thispaperisnottofindthebest-performingmodelbuttodemon- pronetodataleakageinduceanoverestimationofpredictiveperfor-
stratetheimpactofdatasplittingonpredictivepower,dataleakage, mance.They,therefore,suggestthattheevaluationofdeeplearning
andPO.Thus,eveniftrainingbiaswerepresentandaffectedmodel experiments,inparticularthechoiceofsplittingtechnique,should
performance,itwouldnotinfluencetheeffectofperformanceopti- becarriedoutwiththeutmostcareandinalignmentwiththespe-
mism,asevenalessaccuratemodelcanexhibitoverconfidence. cificpredictiontasktoavoidleakage.Overall,wewereabletoshow
Selectingtheoptimalhyperparametersforamodelisessential. theusefulnessofthedefineddataleakagemeasureaswellasits
Althoughweaimedtodefinethehyperparametersearchspaceas connectionwithdifferentsplittingtechniquesandperformance
effectivelyaspossible,thereremainsariskthatthesearchprocess optimismofpredictionmodels.
wassuboptimal.However,evenifthebesthyperparametersforeach Inthefuture,weplantoassessthecapabilitiesofourdataleakage
modelwereidentified,thesemodelswouldstillbeaffectedbyPO measureonusecasesotherthantheHDDdataset,suchasfurther
althoughthemodelsmayhavebeenslightlybetteringeneralizing predictivemaintenancedatasets.Currently,thedefinitionofthe
thedata. measure’s𝛼valueisnotstraightforward.Hence,weplantoconduct
Inthiswork,wefocusedspecificallyontemporalleakageand acomprehensiveparameterstudyonadiversesetofusecasesto
leakageinducedbythenon-independencebetweentrainandtest showcasebestpracticesinselectingthevalue.Wealsointendto
samples.Thus,theproposedmeasureaddressesonlythistypeof refineourdataleakagemeasuresothatitalsotakesintoaccount
leakage.Otherformsofleakagearenotcapturedbyourmeasure. thelengthoftheinputsequencefortheprediction.Further,we
However,asoutlinedinprevioussections,wemitigatedvarious plantoextendtheexperimentstoamorediversesetofsplitting
potentialsourcesofleakageduringpreprocessing(forinstance, methods,forinstance,variationsoftherandomsplitwithvarying
fittingthescalerusingonlytrainingdata). degreesofdataleakage.Finally,wecurrentlyfocusondataleakage
Theassumptionsofourproposedmeasureincludetheindepen- withinagroup,forexample,aspecificHDDinstance.Weplanto
dencebetweenmeasurementsfordifferentHDDs,eventhough,in investigatehowdataleakagecanalsobemeasuredoutsidethese
general,itispossiblethatdependenciesmightexist,forinstance, group-typeboundaries.
mutualinterferenceduetoexcessiveheatdevelopmentofaHDD.
References
However,wepresumethattheseeffects,ifexisting,arenegligible.
Ourproposeddataleakagemeasureallowscontrollingtheim- [1] NicolasAussel,SamuelJaulin,GuillaumeGandon,YohanPetetin,ErizaFazli,
pactoftrainingsamplesprecedingtestsamplesbyparameter𝛼. andSophieChabridon.2017. PredictiveModelsofHardDriveFailuresBased
onOperationalData.In16thIEEEInternationalConferenceonMachineLearning
Theintentionistomakethemeasureadjustabletodifferenttasks, andApplications,ICMLA2017,Cancun,Mexico,December18-21,2017,Xue-wen
thatis,predictiononpreviouslyunknown,novelgroups(𝛼 >0) Chen,BoLuo,FengLuo,VasilePalade,andM.ArifWani(Eds.).IEEE,619–625.
https://doi.org/10.1109/ICMLA.2017.00-92
vs. prediction on data from groups already encountered during
[2] Backblaze.2024.HardDriveTestData.Backblaze. RetrievedOct29,2024from
training(𝛼 =0).Wechose𝛼 ∈{0,1}todemonstratetheconceptual https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data
behaviorforthetwocases.However,selectingtheright𝛼 valueis [3] JamesBergstra,DanielYamins,andDavidD.Cox.2013. MakingaScience
ofModelSearch:HyperparameterOptimizationinHundredsofDimensions
notstraightforwardandrequiresfurtherresearch. forVisionArchitectures.InProceedingsofthe30thInternationalConferenceon
ThecomparabilityoftheleakagevalueL˜mightbeaffectedwhen MachineLearning,ICML2013,Atlanta,GA,USA,16-21June2013(JMLRWorkshop
andConferenceProceedings,Vol.28).JMLR.org,115–123. http://proceedings.mlr.
comparingdatasetswithdifferentsizesandsequencelengths.In
press/v28/bergstra13.html
addition,theactualamountofleakagemightalsodependonthe [4] AnielloDeSanto,AntonioGalli,MichelaGravina,VincenzoMoscato,andGi-
underlyingdependencystructureofthedataaswellasotherfactors ancarloSperli.2022. DeepLearningforHDDHealthAssessment:AnAppli-
cationBasedonLSTM. IEEETrans.Comput.71,1(jan2022),69–80. https:
notcapturedbyourmeasuresinceitisbasedontimeandgroup
//doi.org/10.1109/TC.2020.3042053
344

| ICPE’25,May05–09,2025,Toronto,Canada |     |     |     |     | DanielGrillmeyeretal. |     |
| ------------------------------------ | --- | --- | --- | --- | --------------------- | --- |
[5] WilliamFalconandThePyTorchLightningteam.2019.PyTorchLightning.Light- [19] JingShen,JianWan,Se-JungLim,andLifengYu.2018.Random-forest-basedfail-
ningAI. https://doi.org/10.5281/zenodo.3828935 urepredictionforharddiskdrives.InternationalJournalofDistributedSensorNet-
[6] Gartner.2024. GartnerForecastsWorldwidePublicCloudEnd-UserSpending works14,11(2018),1550147718806480.https://doi.org/10.1177/1550147718806480
to Surpass $675 Billion in 2024. Gartner. Retrieved Oct 31, 2024 from arXiv:https://doi.org/10.1177/1550147718806480
https://www.gartner.com/en/newsroom/press-releases/2024-05-20-gartner- [20] Chuan-JunSuandYiLi.2022.Recurrentneuralnetworkbasedreal-timefailure
forecasts-worldwide-public-cloud-end-user-spending-to-surpass-675-billion- detectionofstoragedevices.MicrosystemTechnologies28,2(01Feb2022),621–633.
| in-2024 |     |     | https://doi.org/10.1007/s00542-019-04454-8 |     |     |     |
| ------- | --- | --- | ------------------------------------------ | --- | --- | --- |
[7] LihanHu,LixinHan,ZhenyuanXu,TianmingJiang,andHuijunQi.2020. A [21] GuochaoWang,YuWang,andXiaojieSun.2021.Multi-InstanceDeepLearning
diskfailurepredictionmethodbasedonLSTMnetworkduetoitsindividual BasedonAttentionMechanismforFailurePredictionofUnlabeledHardDisk
specificity. ProcediaComputerScience176(2020),791–799. https://doi.org/ Drives.IEEETransactionsonInstrumentationandMeasurement70(2021),1–9.
10.1016/j.procs.2020.09.074 Knowledge-BasedandIntelligentInformation& https://doi.org/10.1109/TIM.2021.3068180
EngineeringSystems:Proceedingsofthe24thInternationalConferenceKES2020. [22] BrianWilson.2018. CloudStorageDurability:WhatDoAllThose9sMean?
[8] JosuIrcio,AizeaLojo,JoseA.Lozano,UsueMori,andJoseA.Lozano.2022.A Backblaze. RetrievedSep24,2024fromhttps://www.backblaze.com/blog/cloud-
| MultivariateTimeSeriesStreamingClassifierforPredictingHardDriveFailures |     |     | storage-durability/ |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | ------------------- | --- | --- | --- |
[ApplicationNotes]. IEEEComputationalIntelligenceMagazine17,1(2022), [23] ChangXu,GangWang,XiaoguangLiu,DongdongGuo,andTie-YanLiu.2016.
102–114. https://doi.org/10.1109/MCI.2021.3129962 HealthStatusAssessmentandFailurePredictionforHardDriveswithRecurrent
[9] SayashKapoorandArvindNarayanan.2023.Leakageandthereproducibility NeuralNetworks.IEEETrans.Comput.65,11(2016),3502–3508. https://doi.org/
| crisisinmachine-learning-basedscience. | Patterns4,9(2023),100804. | https: | 10.1109/TC.2016.2538237 |     |     |     |
| -------------------------------------- | ------------------------- | ------ | ----------------------- | --- | --- | --- |
//doi.org/10.1016/j.patter.2023.100804 [24] QiboYang,XiaodongJia,XiangLi,JiansheFeng,WenzheLi,andJayLee.2021.
[10] ShacharKaufman,SaharonRosset,ClaudiaPerlich,andOriStitelman.2012. EvaluatingFeatureSelectionandAnomalyDetectionMethodsofHardDrive
Leakageindatamining:Formulation,detection,andavoidance. ACMTrans. FailurePrediction.IEEETransactionsonReliability70,2(2021),749–760. https:
Knowl.Discov.Data6,4,Article15(dec2012),21pages. https://doi.org/10.1145/ //doi.org/10.1109/TR.2020.2995724
2382577.2382579
[11] IlyaLoshchilovandFrankHutter.2019.DecoupledWeightDecayRegularization.
|     |     |     | A SoftwareConfiguration |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- |
In7thInternationalConferenceonLearningRepresentations,ICLR2019,NewOr-
leans,LA,USA,May6-9,2019.OpenReview.net. https://openreview.net/forum? ThemostrelevantPythonpackagesusedfortheexperimentsare
id=Bkg6RiCqY7
|     |     |     | listed in Table | 5. We used Neptune | [14] for experiment | track- |
| --- | --- | --- | --------------- | ------------------ | ------------------- | ------ |
[12] SidiLu,BingLuo,TirthakPatel,YongtaoYao,DeveshTiwari,andWeisongShi.
2020. MakingDiskFailurePredictionsSMARTer!.In18thUSENIXConference ingandmonitoring.Forfurtherdetails,pleaserefertothewell-
onFileandStorageTechnologies,FAST2020,SantaClara,CA,USA,February24-
27,2020,SamH.NohandBrentWelch(Eds.).USENIXAssociation,151–167. documentedprojectcodeinthefollowingrepository:https://github.
https://www.usenix.org/conference/fast20/presentation/lu com/DescartesResearch/Data-Leakage-HDD-Failure-Prediction
[13] YingzheLyu,HengLi,MohammedSayagh,ZhenMing(Jack)Jiang,andAhmedE.
Hassan.2021.AnEmpiricalStudyoftheImpactofDataSplittingDecisionson
|                                                             |                                   |     | B HyperparameterTuningResults |     |     |     |
| ----------------------------------------------------------- | --------------------------------- | --- | ----------------------------- | --- | --- | --- |
| thePerformanceofAIOpsSolutions.                             | ACMTrans.Softw.Eng.Methodol.30,4, |     |                               |     |     |     |
| Article54(jul2021),38pages. https://doi.org/10.1145/3447876 |                                   |     |                               |     |     |     |
Thisappendixsectionprovidesdetailsaboutthehyperparameter
| [14] neptune.ai.2024.neptune.ai:experimenttracker.neptune.ai. | https://neptune.ai |     |     |     |     |     |
| ------------------------------------------------------------- | ------------------ | --- | --- | --- | --- | --- |
rangesusedforthehyperparametersearchandthebesthyperpa-
[15] AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,Gre-
goryChanan,TrevorKilleen,ZemingLin,NataliaGimelshein,LucaAntiga, rametersfoundforthedifferentMLandDLmodelsandsplitting
AlbanDesmaison,AndreasKöpf,EdwardZ.Yang,ZacharyDeVito,MartinRai- strategies.ThesearelistedinTables6to9.
son,AlykhanTejani,SasankChilamkurthy,BenoitSteiner,LuFang,JunjieBai,
andSoumithChintala.2019.PyTorch:AnImperativeStyle,High-Performance
DeepLearningLibrary. InAdvancesinNeuralInformationProcessingSystems Table5:AdoptedPythonpackagesandversions.
32:AnnualConferenceonNeuralInformationProcessingSystems2019,NeurIPS
2019,December8-14,2019,Vancouver,BC,Canada,HannaM.Wallach,Hugo
Larochelle,AlinaBeygelzimer,Florenced’Alché-Buc,EmilyB.Fox,andRoman
Garnett(Eds.).8024–8035. https://proceedings.neurips.cc/paper/2019/hash/ Package Version
bdbca288fee7f92f2bfa9f7012727740-Abstract.html
[16] Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, lightning 2.2.4
Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron lightning-utilities 0.11.2
Weiss,VincentDubourg,JakeVanderPlas,AlexandrePassos,DavidCourna-
|     |     |     |     | neptune | 1.10.4 |     |
| --- | --- | --- | --- | ------- | ------ | --- |
peau,MatthieuBrucher,MatthieuPerrot,andEdouardDuchesnay.2011.Scikit-
|                                         |                                      |     |     | numpy  | 1.26.4 |     |
| --------------------------------------- | ------------------------------------ | --- | --- | ------ | ------ | --- |
| learn:MachineLearninginPython.          | J.Mach.Learn.Res.12(2011),2825–2830. |     |     |        |        |     |
| https://doi.org/10.5555/1953048.2078195 |                                      |     |     | pandas | 2.2.2  |     |
[17] FranciscoPereira,DanielTeixeira,JoãoPauloPordeusGomes,andJavamC.
Machado.2019. EvaluatingOne-ClassClassifiersforFaultDetectioninHard ray 2.20.0
DiskDrives.In8thBrazilianConferenceonIntelligentSystems,BRACIS2019, scikit-learn 1.4.2
Salvador,Brazil,October15-18,2019.IEEE,586–591. https://doi.org/10.1109/ scipy 1.13.0
BRACIS.2019.00108
|     |     |     |     | torch | 2.3.0 |     |
| --- | --- | --- | --- | ----- | ----- | --- |
[18] SeanOwen.2021.UseHyperoptOptimallyWithSparkandMLflowtoBuildYour
BestModel.Databricks. RetrievedAug19,2023fromhttps://www.databricks. torchmetrics 1.3.2
com/blog/2021/04/15/how-not-to-tune-your-model-with-hyperopt.html
345

QuantifyingDataLeakageinFailurePredictionTasks ICPE’25,May05–09,2025,Toronto,Canada
Table6:BesthyperparametersfoundpersplittypeforHGBC.
|     | learningrate | maxiter | maxleafnodes | maxfeatures | classweight |
| --- | ------------ | ------- | ------------ | ----------- | ----------- |
ParameterRanges [0.01,1.0) [50,500) [5,100) [0.1,1.0) {balanced,None}
| Nosplit     | 0.2196 | 321 | 92  | 0.8873 | balanced |
| ----------- | ------ | --- | --- | ------ | -------- |
| Random      | 0.2162 | 208 | 70  | 0.7093 | balanced |
| Temporal    | 0.3217 | 162 | 98  | 0.8587 | balanced |
| Group-based | 0.4473 | 200 | 36  | 0.8500 | balanced |
Table7:BesthyperparametersfoundpersplittypeforRF.
|     |                 | nestimators | maxdepth | maxfeatures |     |
| --- | --------------- | ----------- | -------- | ----------- | --- |
|     | ParameterRanges | [50,500)    | [5,100)  | [0.1,1.0)   |     |
|     | Nosplit         | 437         | 92       | 0.1064      |     |
|     | Random          | 237         | 77       | 0.1034      |     |
|     | Temporal        | 375         | 48       | 0.1240      |     |
|     | Group-based     | 55          | 21       | 0.1246      |     |
Table8:BesthyperparametersfoundpersplittypeforMLP.
|     |                 | learningrate | hiddensizes      |     |     |
| --- | --------------- | ------------ | ---------------- | --- | --- |
|     | ParameterRanges | [1e-6,1e-3)  | {64,96,...,256}3 |     |     |
|     | Nosplit         | 0.000209     | [224,128,224]    |     |     |
|     | Random          | 0.000045     | [192,256,192]    |     |     |
|     | Temporal        | 0.000012     | [96,224,64]      |     |     |
|     | Group-based     | 0.000005     | [160,128,192]    |     |     |
Table9:BesthyperparametersfoundpersplittypeforLSTM.
|     |                 | learningrate | hiddensize      | numlayers |     |
| --- | --------------- | ------------ | --------------- | --------- | --- |
|     | ParameterRanges | [1e-6,1e-3)  | {64,96,...,256} | {1,2}     |     |
|     | Nosplit         | 0.000109     | 256             | 2         |     |
|     | Random          | 0.000279     | 128             | 2         |     |
|     | Temporal        | 0.000218     | 192             | 1         |     |
|     | Group-based     | 0.000005     | 224             | 1         |     |
346