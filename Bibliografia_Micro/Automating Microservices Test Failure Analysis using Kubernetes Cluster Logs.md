Automating Microservices Test Failure Analysis using
Kubernetes Cluster Logs
PawanKumarSarika DeepikaBadampudi
EricssonAB BlekingeInstituteofTechnology
Stockholm,Sweden Karlskrona,Sweden
pawan.sarika@ericsson.com deepika.badampudi@bth.se
SaiPrashanthJosyula MuhammadUsman
BlekingeInstituteofTechnology BlekingeInstituteofTechnology
Karlskrona,Sweden Karlskrona,Sweden
sai.prashanth.josyula@bth.se muhammad.usman@bth.se
Abstract cloud.Toincreasedevelopmentefficiency,Ericssondevel-
Kubernetesisafree,open-sourcecontainerorchestrationsys- opedtheApplicationDevelopmentPlatform(ADP)ecosys-
temfordeployingandmanagingDockercontainersthathost tem[4],whichamongotherthings,includesamarketplace
microservices.Kubernetesclusterlogshelpindetermining that hosts over 280 microservices. Among these, 50+ mi-
thereasonforthefailure.However,assystemsbecomemore croservicesarecommonmicroservicesthatcanbereused
complex,identifyingfailurereasonsmanuallybecomesmore andintegratedacrossallapplicationswithintheorganiza-
difficultandtime-consuming.Thisstudyaimstoidentifyef- tion.ThemicroservicesintheADPecosystemarehostedin
fectiveandefficientclassificationalgorithmstoautomatically DockercontainersandmanagedbyKubernetes.
determinethefailurereason.Wecomparefiveclassification Some applications need a specific set of microservices
algorithms,SupportVectorMachines,K-NearestNeighbors, that may differ from others. In addition, the applications
RandomForest,GradientBoostingClassifier,andMultilayer maydeploymicroservicesindifferentenvironments,suchas
Perceptron. Our results indicate that Random Forest pro- AmazonWebService(AWS),orMicrosoftAzureCloud.To
ducesgoodaccuracywhilerequiringfewercomputational ensurehighquality,theADPecosystemincludesaContinu-
resourcesthanotheralgorithms. ousIntegrationandContinuousDeployment(CICD)team,
whichsimulatesthedifferentapplicationenvironmentsand
Keywords: Kubernetesclusterlogs,microservices,machine performsvarioustests,includingtestingscalability,robust-
learning ness,andresilience.
ACMReferenceFormat: Whenever a test fails, the developers must classify the
PawanKumarSarika,DeepikaBadampudi,SaiPrashanthJosyula, failureintothefollowingcategories-anissueinthecluster,
andMuhammadUsman.2023.AutomatingMicroservicesTestFail- artifactory,microservice,CICDtestsitself,orenvironment.
ureAnalysisusingKubernetesClusterLogs.InProceedingsofthe Theclassificationisdonetoreportthefailuretotherelevant
InternationalConferenceonEvaluationandAssessmentinSoftware team. For example, microservice bugs are assigned to the
Engineering(EASE’23),June14–16,2023,Oulu,Finland.ACM,New relevantmicroserviceteam,whileCICDbugsarereported
York,NY,USA,4pages.https://doi.org/10.1145/3593434.3593472
totheCICDteamforresolution.Inaddition,knowingthe
failurereasoncanprovideEricssoninsightsonwhatthey
1 Introduction
shouldimprove.Thesetestsgenerateanaverageof450MBof
Ericsson,aleadingInformationandCommunicationTechnol- logdata.Developersusetheirknowledgeandexperienceto
ogy(ICT)serviceprovider,isattheforefrontofpioneering classifythefailure,whichmaytakeuptotwohoursforinitial
cloudRAN1,atechnologythathandlesnetworktrafficinthe analysis.Asthenumberofmicroservicesandteamsusing
themgrows,itbecomesincreasinglychallengingandtime-
1https://www.ericsson.com/en/ran/cloud
consumingfordeveloperstoclassifythesefailuresmanually.
Thispaperreportstheexperienceofautomatingtheclas-
Permissiontomakedigitalorhardcopiesofpartorallofthisworkfor
personalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesare sificationoffailuresusingmachinelearningtechniquesat
notmadeordistributedforprofitorcommercialadvantageandthatcopies Ericsson.Thegoalofautomationistoidentifyanefficient
bearthisnoticeandthefullcitationonthefirstpage.Copyrightsforthird- andcost-effectivemethodtodecreasethetimerequiredfor
partycomponentsofthisworkmustbehonored.Forallotheruses,contact
manualanalysis.Toachievethisgoal,weutilizeddevelopers’
theowner/author(s).
knowledgeandexperiencestobetterunderstandthework-
EASE’23,June14–16,2023,Oulu,Finland
flowsandinformationnecessaryforclassifyingthefailure.
©2023Copyrightheldbytheowner/author(s).
ACMISBN979-8-4007-0044-6/23/06. Based on this understanding, we extracted important log
https://doi.org/10.1145/3593434.3593472
3202
nuJ
31
]ES.sc[
1v35670.6032:viXra

EASE’23,June14–16,2023,Oulu,Finland SarikaandBadampudi,etal.
datatotrainamachine-learningmodelcapableofaccurately likelytocontainthefailurereason.Thisstepallowedusto
predictingthefailure’scause. identifythemostfrequentlyvisitedKubernetesclusterlogs.
Theintervieweeswereaskedtowalkthroughthedifferent
2 StudyDesign stepstheyfollowed,alongwiththeinputsconsideredandthe
outputsofeachstep.Throughthisprocess,weidentifiedthe
Figure1representsthestepsfollowedinthisstudy.Inthis
cruciallogpartsforfailureclassificationandhowdevelopers
section,wedescribetheprocessfollowedineachstep.
identifiedfailurereasons.
Methods 2.2 DataCleaning
Kubernetes Logs
Inthisstudy,weutilizedimportantdataidentifiedfromthe
Classification
TF-IDF algorithms interviewforclassification.Followingdataselection,data
cleaningwasconducted(Figure1).Weensureddatacleanli-
Expert knowledge
nessbyremovinginaccurate,incomplete,orirrelevantdata.
Data selection Human-readableelements(e.g.,punctuation,newlinechar-
acters) were removed to reduce computational costs. We
Feature Training convertedalllogelementstolowercaseletterstoavoidambi-
Extraction
guities,anduniqueelements(e.g.,timestamps,IPaddresses,
Data cleaning
linenumbers)wereremoved.Stopwordsandstemmingmeth-
odswerenotusedastheyrelyontheEnglishdictionaryand
Training
data maynotworkfornon-Englishwordslike’requesthandler-
class.’
Log data Vocabulary
2.3 FeatureExtraction
Machine learning
Test data After cleaning the Kubernetes cluster logs data, the text
Model
formatmustbeconvertedintoanumericalformusingFea-
tureExtraction(FE)foralgorithmstoprocessit.Although
Figure1.Overallresearchprocess.
word-to-vector(word2vec)isapopularmethodforfeature
extraction,itwasnotconsideredappropriateduetothewide
variation in the size of each log. Instead, we utilized the
2.1 DataSelection
TF-IDFmethod,acommonfeatureextractionprocedurefor
AsdepictedinFigure1,expertknowledgewasutilizedto sentencesanddocuments.TF-IDFwasmoresuitableforlogs
identifythemostinformativesectionsofKubernetescluster sincethewordsrelatedtotheerrorgenerallyoccuronceor
logs,whichreducedtheoveralldataprocessingrequirements. twiceintheentirelog.Thismethodhighlightswordsdis-
Moreover,beforeautomation,itisimportanttocomprehend tinctivefromthetext,allowingtheextractionofessential
themanualprocessoffailureclassification.Thefirstauthor, datafeaturesrequiredforclassification.UsingTF-IDF,we
a team member responsible for testing and deploying mi- generate vocabulary, which is used to extract the feature
croservices, noted that each team member had their own vectorsofthelogdata.
approachtoanalyzingfailures.Toestablishaconsensus,we
2.4 Classification
conductedfourin-depthinterviewstobetterunderstandthe
manualfailureclassificationprocess.Theintervieweeshad Finally,themostcrucialstep,i.e.,logclassification,involves
varyinglevelsofexperienceinidentifyingreasonsforfailure, usingclassificationalgorithmstoconstructmodelsthatcan
rangingfrom1.5to4years.Furthermore,theinterviewees makeaccuratepredictions.Thisstudyemployssupervised
havespecializedexpertiseinseveralareasrelatedtoman- learning, as it is necessary to make predictions for speci-
ualfailureanalysis,suchastestenvironments,end-to-end fiedclasses.Non-parametricalgorithmsareselectedforthis
testing, and coordination with microservice development studybecausetheydonotrequirepriorknowledgeandare
teams.Asaresult,theparticipantshavediverseskillsand particularlysuitablewhenworkingwithlargedatasets[2].
knowledge that were valuable in the failure classification ThechosenalgorithmsforthisstudyincludeSupportVector
process. Machines(SVM),K-NearestNeighbors(KNN),RandomFor-
Westartedtheinterviewbyexplainingthestudyobjective. estClassifier,GradientBoostingClassifier,andMultilayer
Wethenpresentedascenarioinwhichafailureoccurredand Perceptron(MLP).
askedtheintervieweestoclassifythefailureusingthesame
2.5 Training
stepstheywoulduseinareal-worldsituation.Theintervie-
weeisfreetouseanylogasanexample.Anexperienced Weproceededwithtrainingtheselectedclassificationalgo-
developertypicallyexaminesthesectionsofthelogthatare rithmsusingthefeaturevectorsofthetrainingdata.Weused

AutomatingMicroservicesTestFailureAnalysisusingKubernetesClusterLogs EASE’23,June14–16,2023,Oulu,Finland
thescikit-learnlibrarytoobtainthetrainedmodels.The Table1.ModelaccuracyandF1-scoreforeachalgorithm
SVC() is trained with a linear kernel (SVM). The Random-
ForestClassifier()istrainedwith1000trees.Allother Algorithm Accuracy F1-score
functionparametersofKNeighborsClassifier()andGra-
SVM 0.6905 0.6580
dientBoostingClassifier()aresettodefaultvaluesused
KNN 0.6576 0.6580
by scikit-learn. MLP was built using keras sequential
RandomForest 0.7279 0.7106
model consisting of three dense layers and two Dropout
GradientBoosting 0.7302 0.7071
layers.TheF1Scoreweightedmetricisusedforevaluation
MLP 0.7086 0.6911
alongwiththeAdamoptimizersettoalearningrateof0.001,
andcategoricalcross-entropyisusedasthelossmetric.
Followingthetrainingofthealgorithms,weutilizedthem Table2.PairwiseP-valuesforaccuracy
topredictclasslabelsforeveryloginthetestdata.Wecol-
lectedvariousmetrics,suchasaccuracy,F1-score,training Random Gradient
SVM KNN MLP
time,andpredictiontime,tocomparetheclassificationalgo- Forest Boosting
rithms’performancesforpredictingfailurereasons.Wemea- SVM 1.0000 0.3517 0.4374 0.2418 0.9000
suredtrainingandpredictiontimestoassesscomputational KNN 1.0000 0.0037 0.0010 0.1143
Random
cost,whichcanbeabettermetricforreal-worldperformance 1.0000 0.9000 0.7633
Forest
thantimecomplexity[3].Stratified10-foldcross-validation
Gradient
wasemployedasthesamplingstrategy.Thisapproachhelped 1.0000 0.5626
Boosting
identifythealgorithmwiththebestpredictiveaccuracyand
MLP 1.0000
computationalcostforagivenhardwareandsoftwarecon-
figuration.
Wecomparedthechosenclassificationalgorithmsstatis-
ticallybasedontherecommendationsbyDemšar[1].We
3 Expertopinionfindingsonanalyzing
appliedtheFriedmantesttotestthenull-hypothesisthatall
failurereasons
algorithmsareequivalent.Ifthishypothesiswasrejected,
Duringtheinterviews,developersscrutinizedafailedtest weconductedapost-hocNemenyitesttocomparethealgo-
caseandanalyzedtheKubernetesclusterlogstoclassifythe rithmspairwise.
failure.Specifically,theysearchedforlogsassociatedwith Table 1 presents the accuracy and F1-scores of each al-
themicroserviceundertestwithinthepods/containeror gorithm.TheFriedmantestwasperformedtoevaluatethe
pods/describedirectories.Ifnorelevantlogswerefound, statisticalsignificanceofthedifferencesbetweenthealgo-
the logs of dependent microservices were consulted. Our rithms, resulting in a p-value of 0.00074 and a Q value of
analysisrevealedthattheerrororrelevantinformationcould 19.12,confirmingsignificantdifferencesinaccuracy.Wesub-
usuallybefoundinthesedirectories.Evenwhenitwasnot, sequently conducted a Nemenyi test, and the p-values of
therewerecluesindicatingpotentialfailuretype.Asaresult, thecombinationsofalgorithmsareshowninTable2withP-
we concluded that logs located in pods/containers and valueslessthan𝛼(0.05)inbold.RandomForestandGradient
pods/describedirectoriesarecrucialinmostinstances.To BoostingwerestatisticallybetterthanKNN.
further strengthen this conclusion, we also examined the Similarly,forF1-scores(Table3),theFriedmantestyielded
ticketssubmittedbythedevelopers.Wefoundthattheroot ap-valueof0.00056andaQvalueof19.76,indicatingsig-
directoriesfor43ofthe50reportedlogsnippetswerelocated nificantdifferences.TheNemenyitestshowedthatRandom
inpods/containerorpods/describe,orbothdirectories. Forest outperformed SVM and KNN with statistically sig-
The pods/containers and pods/describe directories nificantdifferences.Furthermore,KNN’sperformancewas
weredeterminedtobeimportantduringtheinterviewphase. significantlylowerthanGradientBoosting’s.Regardingboth
Thelogswerepre-processed,andthelogs’sizewassignif- F1-scoreandaccuracy,RandomForest,GradientBoosting,
icantlyreduced(upto96.08%)throughdataselectionand andMLPperformedsimilarly.
cleaning,reducingcomputationalresources. WeperformtheNemenyitesttodeterminewhichalgo-
rithmsarestatisticallydifferentbasedonF1-scores.Table2
representsthep-valueofF1-scoreforeachcombinationof
4 Developingpredictionmodels algorithms.Thep-valueinboldislessthan𝛼 (0.05).
Theclassificationalgorithmswereusedtoprocessthetrain- Finally,thealgorithmswereevaluatedbasedontheirtrain-
ingdataandgenerateaclassificationmodel,whichwasthen ingandpredictiontimes.Theaveragetrainingtimeinmin-
usedtopredictthetestdata’sclasslabels.Theperformance utesforalltenfoldsisshowninTable4.Itwasobserved
of the algorithms was evaluated based on their accuracy, thatGradientBoostingtookasignificantlylongertimefor
F1-score,trainingtime,andpredictiontime. trainingwhencomparedtootheralgorithms.Ontheother

| EASE’23,June14–16,2023,Oulu,Finland |     |     |     |     |     |              |     |     |     | SarikaandBadampudi,etal. |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ------------------------ | --- | --- |
| Table3.PairwiseP-valuesforF1-score  |     |     |     |     |     | 6 Conclusion |     |     |     |                          |     |     |
IdentifyingthereasonforafailedCICDtestisimportantto
|     |     |     | Random | Gradient |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
assignthefailuretotherelevantteamforresolution.Theau-
|     | SVM | KNN |        |          | MLP |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | Forest | Boosting |     |     |     |     |     |     |     |     |
tomaticidentificationoffailurereasonsminimizestheman-
| SVM | 1.0000 | 0.9000 | 0.0248 | 0.1143 | 0.4374 |     |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
ualeffortneededtoanalyzethefailure.Inthisstudy,were-
| KNN |     | 1.0000 | 0.0022 | 0.0160 | 0.1143 |     |     |     |     |     |     |     |
| --- | --- | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
portexperiencesofclassifyinglarge-scaleKubernetescluster
Random
1.0000 0.9000 0.6830 logsusingmachinelearningclassificationalgorithms:Sup-
Forest
portVectorMachines(SVM),K-NearestNeighbors(KNN),
Gradient
|     |     |     |     | 1.0000 | 0.9000 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Boosting RandomForestClassifier,GradientBoostingClassifier,and
MultilayerPerceptron(MLP).Eachloggenerates450MBof
| MLP |     |     |     |     | 1.0000 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
dataonaverage,whichwasreducedto91%byidentifying
relevantpartsofthelogsusingexpertopinion.Weusedthe
hand,MLPtookmorethan2xlongerfortrainingcompared
TF-IDFfeatureextractionmethod.Thenwetrainedandeval-
| to the Random | Forest. | Regarding |     | prediction | time, all five |     |     |     |     |     |     |     |
| ------------- | ------- | --------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
uatedtheclassificationalgorithmsintermsofaccuracy,F1
algorithmsfinishedpredictionsinlessthanasecond,indi-
scores,training,andpredictiontime.
catingnosignificantdifferencebetweentheminreal-world
|     |     |     |     |     |     | The results | indicated | that | Random | Forest | outperforms |     |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ---- | ------ | ------ | ----------- | --- |
performance.Basedontheanalysis,itcanbeconcludedthat
SVM,KNN,GradientBoosting,andMLPintermsofaccu-
theRandomForestalgorithmperformedbetterintermsof
|     |     |     |     |     |     | racy and | computational | cost. | When | evaluating |     | the proof- |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | ----- | ---- | ---------- | --- | ---------- |
bothaccuracyandtrainingtime.
of-concept,thedevelopersexpectadditionalinformationto
|     |     |     |     |     |     | strengthen | the confidence |     | in the prediction. |     | For | example, |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------------------ | --- | --- | -------- |
Table4.Trainingandpredictiontimeinminutes
|     |     |     |     |     |     | providing | similar logs | and | diagnosis | reports | can | help the |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --------- | ------- | --- | -------- |
developerstounderstandhowpreviouslyfailedtestswere
Algorithm Trainingtime Predictiontime classified manually and arrived at the same classification
predictedbythemodel.Aspartoffuturework,weaimto
| SVM |     |     | 0.845 |     | 0.082 |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
KNN 0.004 0.015 makethecomparisonofthealgorithmsmorerigorousby
1.702 0.006 applyinghyperparametertuningandfurtherimprovingthe
RandomForest
GradientBoosting 110.773 0.002 model’sinterpretabilityandexplainability.
4.111 0.005 Asaprospectforfutureresearch,weintendtoenhancethe
MLP
dimensionalityoftheinputdata.Currently,weconcatenate
logsfromdifferentservicesintoasinglefile,creatingatwo-
dimensionalinput.Ourplanistoaggregatelogsfromdiffer-
5 Pilotingthepredictionmodels
entpodswithineachservice,producingathree-dimensional
Totestthemodelinaproductionenvironment,wedeveloped
|     |     |     |     |     |     | input where | each service | has | its own | file. | This | approach |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------- | ----- | ---- | -------- |
anend-to-endprototype.Theresultsofthemodelwereadded wouldenableustoleveragedeeplearningalgorithms,such
toadashboardfordeveloperanalysis.
|     |     |     |     |     |     | as CNNs, | which are | proficient | in  | processing | 3D  | data. By |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --- | ---------- | --- | -------- |
Wereceivedfeedbackfromdevelopers,whoindicatedthat doingso,ourmodelwouldbeabletoidentifytheinterde-
whilethefailureclassificationhelpsthemunderstandthe
pendenciesamongtheservices,leadingtoimprovedresults.
| reason for | the failure | and | where | they should | look in the |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ----- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
logs,theywouldappreciateadditionalinformationbeyond Acknowledgments
| the failure | reason. | As part | of future | work, | we will devise |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | --------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
TheKnowledgeFoundationsupportsthisworkthroughthe
anadditionalsolutiontoincludethemostsimilarlogprevi-
OSIRproject(referencenumber20190081)atBlekingeInsti-
ouslyreportedalongwithitsdiagnosisreport.Reviewing
tuteofTechnology,Sweden.
diagnosisreportsofsimilarlogswillhelpdevelopersquickly
| understandthecauseoffailure.Thisway,developerscan |     |     |     |     |     | References |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
preciselylookatthespecificlogsincreasingtheirefficiency
[1] JanezDemšar.2006.Statisticalcomparisonsofclassifiersovermultiple
andhelpingthemclosethecasesfaster.
datasets.TheJournalofMachinelearningresearch7(2006),1–30.
Inaddition,developersexpressedconcernsaboutthetrust- [2] StuartJRussellandPeterNorvig.2010.ArtificialIntelligenceAModern
worthinessofthemodels’predictionsduetoalackofunder- ApproachThirdEdition.
[3] AuthorDanielLemire.2021.Big-Onotationandreal-worldperformance.
standingofhowthemodelarrivedatitsconclusions.Further
RetrievedFebruary20,2023fromhttps://lemire.me/blog/2013/07/11/big-
effortisrequiredtoimprovethemodels’interpretabilityand
o-notation-and-real-world-performance/
explainability.
[4] MuhammadUsman,DeepikaBadampudi,ChrisSmith,andHimansu
AlthoughRandomForestperformedbetter,weneedto Nayak.2022.AnEcosystemfortheLarge-ScaleReuseofMicroservices
tunethehyperparameterstotrulycapturetheeffectiveness inaCloud-NativeContext.IEEESoftware39,05(2022),68–75.
ofRandomForestcomparedtootheralgorithms.