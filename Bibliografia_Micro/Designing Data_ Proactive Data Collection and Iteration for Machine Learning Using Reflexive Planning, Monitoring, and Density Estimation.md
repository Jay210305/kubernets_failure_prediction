Designing Data: Proactive Data Collection and Iteration for Machine Learning
|     | Using | Reflexive |     | Planning, | Monitoring, |     | and | Density | Estimation |     |     |     |
| --- | ----- | --------- | --- | --------- | ----------- | --- | --- | ------- | ---------- | --- | --- | --- |
AspenHopkins12 FredHohman2 LucaZappella2 XavierSuauCuadros2 DominikMoritz2
|     |     | Abstract |     |     |     | Failuretoeffectivelyrecognizedataqualityandcoverage |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
needscanleadtobiasedMLmodels(Mitchelletal.,2020).
| Lack | of diversity | in data | collection | has | caused |     |     |     |     |     |     |     |
| ---- | ------------ | ------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
3202 luJ 92  ]CH.sc[  2v91301.1032:viXra Such failures are responsible for the perpetuation of sys-
significantfailuresinmachinelearning(ML)ap-
temicpowerandaccessdifferentialsandthedeploymentof
| plications. |     | While ML developers |     | perform | post- |                                            |     |     |     |     |             |     |
| ----------- | --- | ------------------- | --- | ------- | ----- | ------------------------------------------ | --- | --- | --- | --- | ----------- | --- |
|             |     |                     |     |         |       | inaccessibleordefectiveproductexperiences. |     |     |     |     | Yetbuilding |     |
collectioninterventions,thesearetimeintensive
representativedatasetsisanarduous,historicallydifficult
| and | rarely | comprehensive. | Thus, | new | meth- |     |     |     |     |     |     |     |
| --- | ------ | -------------- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
undertaking(Tayi&Ballou,1998;Sambasivanetal.,2021)
odstotrack&managedatacollection,iteration,
thatreliesontheefficacyofhuman-specifieddatarequire-
andmodeltrainingarenecessaryforevaluating
ments.
| whetherdatasetsreflectrealworldvariability. |     |     |     |     | We  |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
presentdesigningdata,aniterativeapproachto Toensureadatasetcoversall,orasmany,characteristics
data collection connecting HCI concepts with aspossible,specificationsmustbetheresultofacompre-
| ML  | techniques. | Our process | includes |     | (1) Pre- |     |     |     |     |     |     |     |
| --- | ----------- | ----------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
hensiveenumerationofpossibledimensions—anopenand
Collection Planning, to reflexively prompt and hardproblemthatfewhavepracticallygrappledwithinthe
document expected data distributions; (2) Col- contextofML.Furthercontributingtothisdifficultyisthe
lectionMonitoring,tosystematicallyencourage realizationthatitisnotenoughforthetrainingdatasetstobe
samplingdiversity; and(3)DataFamiliarity, to alignedwithexpecteddistributions: theymustalsoinclude
| identify | samples | that are unfamiliar |     | to  | a model |        |          |      |              |     |           |           |
| -------- | ------- | ------------------- | --- | --- | ------- | ------ | -------- | ---- | ------------ | --- | --------- | --------- |
|          |         |                     |     |     |         | enough | examples | from | conceptually |     | harder or | less com- |
using density estimation. We apply designing moncategoriesifsaidcategoriesaretobelearned(Asudeh
datatoadatacollectionandmodelingtask. We etal.,2019). Failuretosufficientlyconsiderboththecrit-
findmodelstrainedon“designed”datasetsgen-
|     |     |     |     |     |     | ical dimensions |     | of data | and their | relative | complexity | can |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --------- | -------- | ---------- | --- |
eralize better across intersectional groups than havetroublingconsequences. Instancesofsuchmissteps
thosetrainedonsimilarlysizedbutlesstargeted span issues of justice, healthcare, hiring practices, voice
datasets,andthatdatafamiliarityiseffectivefor andfacerecognition,andloanqualifications,whereinbiases
debuggingdatasets. of data and algorithms limit technological use and cause
|     |     |     |     |     |     | harm | (Buolamwini | &   | Gebru, | 2018; | Asudeh et | al., 2019; |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------ | ----- | --------- | ---------- |
Palanicaetal.,2019;Angwinetal.,2016;Noble,2018).Yet
1.Introduction understandingthesedatarequirementsevenaftertrainingis
difficult;knowingthemaprioriisexceptionallyso.
Curatingrepresentativetrainingandtestingdatasetsisfunda-
Ratherthanemphasizetoolsthatenablebettercollectionand
mentaltodevelopingrobust,generalizablemachinelearning
(ML)models. However,understandingwhatisrepresenta- dataiterationpractices—thatdesignbetterdata—research
tive for a specific task is an iterative process. ML practi- in fairness and machine learning has largely focused on
tionersneedtochangedata, models, andtheirassociated prescriptive“how-to”frameworks,definitionsoffairness,
processesastheybecomemorefamiliarwiththeirmodeling and post-collection analysis techniques (Amershi et al.,
|     |     |     |     |     |     | 2019; | Yang | et al., 2020). | While | there | are exceptions | to  |
| --- | --- | --- | --- | --- | --- | ----- | ---- | -------------- | ----- | ----- | -------------- | --- |
task,asthestateoftheworldevolves,andasproductsare
updatedormaintained. Iterationdirectedbythisevolving this(Hohmanetal.,2020b),thehiddentechnicaldebt(Scul-
understandingseekstoimprovemodelperformance,often leyetal.,2015)accumulatedfrompoordatadesignremains
editingdatasetstoensuredesiredoutcomes. anunderexploredspace. Toreducethistechnicaldebtand
encouragediversedatasets,methodsofexternalizingdata
1 MassachusettsInstituteofTechnology2Apple.
|     |     |     |     |     | Correspon- | collection,iteration,andtrainingarenecessarychecksfor |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
denceto:AspenHopkins<dataspen@mit.edu>.
ensuringdatasetsreflectdiverseexperiencesandarerobust
|                  |          | 40th              |               |     |               | whendeployedinreal-worldmodels. |     |     |     |     |     |     |
| ---------------- | -------- | ----------------- | ------------- | --- | ------------- | ------------------------------- | --- | --- | --- | --- | --- | --- |
| AI & HCI         | Workshop | at the            | International |     | Conference on |                                 |     |     |     |     |     |     |
| MachineLearning, |          | Honolulu, Hawaii, | USA.PMLR202,  |     | 2023.         |                                 |     |     |     |     |     |     |
ContributionsWepresentdesigningdata,aniterative,bias
Copyright2023bytheauthor(s).
1

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
iterate / collect data
iterate / collect data
|     |     |     |     | Collection
 |     |     | Data
 |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | ------ | --- | --- |
Pre-Collection

Familiarity (DE)
|     |     | Planning | Collect | Monitoring |     | Train |     | Deploy |     |
| --- | --- | -------- | ------- | ---------- | --- | ----- | --- | ------ | --- |
Figure1. Designingdataincludes(I)Pre-CollectionPlanning,(II)CollectionMonitoring,&(III)DataFamiliarity.Eachsupplements
theother,andshouldbeusediteratively.
mitigatingapproachtodataplanning,collection,andML documentationfortransparencyindownstreammodeland
development;weimplementthisapproachinaninteractive datasetuse(Koestenetal.,2019;Bender&Friedman,2018;
dashboardthatscaffoldseachstepforpractitioneruse. Mo- Arnoldetal.,2019). Thistypeofdocumentationhasbeen
tivated by 24 formative interviews 3, designing data is a widelyadopted(Hopkins&Booth,2021). However,docu-
structured,holisticparalleltothecurrentstandardsforde- mentationonitsownislimited,asittypicallyaccompanies
velopingproduction-qualitydatasets(Hohmanetal.,2020b). amodelordatasetuponreleaseratherthanshapingitsde-
Eachstepproactivelyintroducesinterventionstoimprove velopment. For instance, Model Cards do not explicitly
modelspriortodeployment: guidehowtoreconcilemodelweaknessoractivelydirect
datacollectiontoimprovefairness–rather,theyareintended
1. Pre-CollectionPlanningprioritizesreflexiveconsid- fortransparency. Ourcontributionisembeddingthetrans-
erationfordomainanddataneedspriortomodeling,
parencyrevealedbysuchdocumentationintoourdesigning
| documents | expected | distributions |     | of attributes, | and |                          |     |                            |     |
| --------- | -------- | ------------- | --- | -------------- | --- | ------------------------ | --- | -------------------------- | --- |
|           |          |               |     |                |     | dataprocessanddashboard. |     | Throughsimpleprompts,users |     |
highlightspotentialbiasesthroughquestionsrelatedto actively surface and engage with their priors–which later
classorcharacteristicrepresentationwithindata.
informstheirevaluation.
2. Collection Monitoring communicates insight into ReflexivityandSelf-ReflectionInsocialscience,theprac-
datasetevolution,allowinguserstomaketargetedad- tice of reflexivity is a way to externalize implicit subjec-
justmentstocollectionprocessesbasedonnewinsight tivitypresentindatacollectionandinterpretation(Fish&
ordisparitiesbetweenexpecteddistributionsandexist- Stark, 2021; Dodgson, 2019). Reflexivity entails deliber-
ingdata. atelyexaminingpractitioners’ownassumptions,practices,
andbeliefsystems,thencontrastingthemwithalternative
| 3. Data   | Familiarity   | borrows              | from Out-of-Distribution |            |         |                                                 |                                          |     |           |
| --------- | ------------- | -------------------- | ------------------------ | ---------- | ------- | ----------------------------------------------- | ---------------------------------------- | --- | --------- |
|           |               |                      |                          |            |         | perspectives.                                   | Thisacknowledgespositionality—howdiffer- |     |           |
| (OOD)     | methodologies | to                   | identify data            | that       | a model |                                                 |                                          |     |           |
|           |               |                      |                          |            |         | encesinsocialpositionandpowershapeidentities.   |                                          |     | While     |
| perceives | as            | unfamiliar, creating | new                      | directives | for     |                                                 |                                          |     |           |
|           |               |                      |                          |            |         | reflexivityistypicallypracticedretrospectively, |                                          |     | (Soedirgo |
dataandmodeliteration.
&Glas,2020)outlinedhowitcouldbeanactiveprocess
through“ongoingreflectionaboutourownsociallocation
We demonstrate designing data’s effectiveness through a and[...] ourassumptionsregardingothers’perceptions.”
case study using inertial measurement units (IMU) data– Thisapproachincludesrecordingassumptionsofposition-
timeseriesdatarepresentingX,Y,&Zpositioning–toclas-
|     |     |     |     |     |     | ality; routinizingreflexivity; |     | includingotheractorsinthe |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ------------------------- | --- |
sify hand position while texting. First, we collected data process;andcommunicatingreflexiveoutcomeswithdata.
iteratively,usingPre-CollectionPlanningandMonitoring
Separatefromyetrelatedtoreflexivityisrecentdatavisual-
| stepstobuildadiversedataset. |     | Then,weuseleave-one-out |     |     |     |     |     |     |     |
| ---------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
izationworkpromptingviewerstoreflectontheirindividual
cross-validationtoevaluatehowtheseinitialstepsinfluence
|              |          |             |             |     |           | beliefs of | data (Kim et | al., 2018; Hohman | et al., 2020a). |
| ------------ | -------- | ----------- | ----------- | --- | --------- | ---------- | ------------ | ----------------- | --------------- |
| performance. | Finally, | we evaluate | familiarity | to  | first de- |            |              |                   |                 |
ExamplesofthisincludeTheNewYorkTimes“YouDraw
| bugadataset,thentodirectcollectionefforts. |     |     |     | Eachstepis |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
It”visualizations,wherereadersdrawaprojectedtrendline
| centralizedwithinadashboard. |     |     | Wefindmodelstrainedon |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
ofwhattheythinkthedatalookslikeandthencomparethat
highlydiversedataoutperformthosetrainedonlessdiverse
projectionwiththerealdata(Aischetal.,2015;Katz,2017;
dataacrossintersectionalgroups.
|     |     |     |     |     |     | Buchanan | et al., 2017), | and an MIT Tech | Review article |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --------------- | -------------- |
2.RelatedWork illustratingthecomplexityofbuildingfairrecidivismmod-
elswhereinreaderschangedifferenthyperparametersthen
MLDocumentation Aclosealternativetodesigningdata contrasttheiroutcomestoexistingmodels(Hao&Stray,
ismodelanddatasetdocumentation,suchasModelCards 2019;Stray&Hao,2020). Suchvisualizationsactaspow-
(Mitchell et al., 2019) or Datasheets for Datasets (Gebru erfultoolsensuringself-reflection—animportantfactorin
| etal.,2021). | Suchworkdetailswhattoincludewithinsaid |     |     |     |     |     |     |     |     |
| ------------ | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
buildingrepresentativedatasets. understandingofcriticaldimensionsofthedatabeforestart-
ingdatacollection,therearesomecommoncharacteristics
| Learnability | and | Familiarity | Having | diverse | character- |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
forhuman-centricdatacollectionbasedonexistingknowl-
| istics with | sample | size parity | in data | is one | step towards |                                               |     |     |     |     |     |     |
| ----------- | ------ | ----------- | ------- | ------ | ------------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
|             |        |             |         |        |              | edgeofpopulationstatisticsandpowerimbalances. |     |     |     |     |     | How |
mitigatingbiasbutdoesnotensureequitablelearningacross
|     |     |     |     |     |     | useful that | information | is depends |     | on the | context | of how |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---------- | --- | ------ | ------- | ------ |
classes. Instead,theseapproachesignoredatalearnability:
thedataisused—forexample,aperson’saccentandspeech
havinganequalnumberofsamplesperclassneglectsthe
pathologyareimportantfactorsinspeechrecognition,but
factthatsomeclassesareinherentlyeasiertolearnthanoth-
|     |     |     |     |     |     | notforcreatingapersonalizedwinerecommendation. |     |     |     |     |     | Un- |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
ers(Ben-Davidetal.,2019;Schapire,1990;Klawonnetal.,
|                       |     |      |            |       |            | like summary | statistics, | surfacing |     | noisy data | or  | missing |
| --------------------- | --- | ---- | ---------- | ----- | ---------- | ------------ | ----------- | --------- | --- | ---------- | --- | ------- |
| 2019). Unfortunately, |     | this | complexity | might | not become |              |             |           |     |            |     |         |
subsets–essentially“debugging”data–requiressignificant
| apparent | until after | deployment. | In  | order | to build better |            |         |             |       |           |          |     |
| -------- | ----------- | ----------- | --- | ----- | --------------- | ---------- | ------- | ----------- | ----- | --------- | -------- | --- |
|          |             |             |     |       |                 | effort. As | another | interviewee | said, | “fairness | analysis | is  |
systems,discoveringwhathasnotbeenlearnedbyamodel
usefultoapoint”.Generictoolsforsurfacingthesenuanced
| iscritical. | Inthepast,testingdataactedasaproxyforthis |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
limitationsofdatadonotexist,butthereisbothneedand
| evaluation. | Butwhiletestdatasetsofferexcellentthresholds |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
desireforthem(Holsteinetal.,2019).
forperformanceexpectations,thesearenotthesamemea-
Difficultyofcollectionleadstocompromises(T2).
| surements: | testingaccuracymeasureswhetheramodelwas |     |     |     |     |     |     |     |     |     |     | Data |
| ---------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
correctinitsclassificationwithoutconsiderationforhow collectionisadifficultprocesstolaunch,requiringsignifi-
itreacheditsconclusion. Forthisreason,modelsareoften canttooling. Thisdifficultycontributestoissuesofrepre-
poorlycalibrated(VanCalsteretal.,2019). Toaddressthis, sentationindata,astheemphasisinearlydatacollectionis
weusedensityestimation(DE)–acommontechniquefor onhowtocollectandstructuredataratherthanbuildinga
measuringOOD–toevaluatehowfamiliaramodelistoa completepictureofwhattocollectfor. Further,earlycollec-
givensample. OurimplementationofDEismostsimilarto tioneffortstendtoprototype,makingconveniencesampling
(Leeetal.,2018),whouseittodetectanomaloussamples canon. Inhuman-centricdata(e.g. speechormovement),
post-training(e.g.,adversarialattacks). Unlikepriorwork, suchrequirementscanencumberdiversityacrossmanyaxes.
weextendDEtechniquesintotrainingtodirectdataefforts. ThishasthepotentialtoinhibitrobustML—whilethereis
anaturaliterationindatasetsstemmingfromdistribution
OuruseofDEtoguidedatacollectionisaresponsetotwo
shift(Quionero-Candelaetal.,2009)andcollectors’evolv-
| drawbacks | we note | from other | work | seeking | to improve |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ingunderstanding,itisacyclefullofforkingpaths(Kale
| datarepresentationandmodelperformance: |     |     |     |     | (1)alternative |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
etal.,2019;Hohmanetal.,2020b)anddead-ends.
approachesrequirepriorawarenessofwhatfacetsofdata
arevariable—fordatathatpeopleareunaccustomedto,this Modelfailuresareinvisiblewithoutparticipationand
mightbeimpossible—and(2)measuringdiversitywithina iteration(T3). Realworldfailuresareonlyvisiblewhen
givendatasetdoesnotaccountforwhatthemodelactually communicated. Butthatcommunicationcomesfromthose
learns(Hooker,2021;Schmidtetal.,2018). Becauseitis investedenoughinthetool,system,orresearchagendato
modeloutputsthatweareconcernedfor,theseareimportant maketheefforttobridgethecommunicationgap. Toquote
weaknessestocounter. aninterviewee: “Thepeoplewhohadissueswereinvisible
tothesystembecausetheydidn’tlikeusingit”.
Unlikeother
3.FormativeInterviews domains which employ tools to surface and track issues
|     |     |     |     |     |     | via user engagement, |     | there | are currently | no  | tools | that ad- |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ------------- | --- | ----- | -------- |
TounderstandMLpractitioners’datacollectionneeds,we
|     |     |     |     |     |     | dress the | gap between | a deployed |     | ML product | (let | alone |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | ---------- | --- | ---------- | ---- | ----- |
conducted24semi-structuredexploratoryinterviewswith itsearlyprototype)andauser. Suchgapsarewidenedby
individualspossessingextensivemachinelearninganddata languageandknowledgebarriers, andtheproductsthem-
collectionexperiencewithinalargetechnologycompany.
selvesareinaccessibletomanywhodonotalignwiththe
TheintervieweesrangedfromMLresearchscientistsand priors on which the system is built. As these limitations
designersfocusedonMLexperiencestoengineeringprod-
havesubstantialdownstreamimpacts,wesoughttointro-
Interviewslasted∼onehour.
uctmanagers. Asinterviews duceearly,comprehensivedata&modelcheckstofacilitate
progressed,commonthemessurfacedthatdirectedourat- easypivotingduringdatacollection.
| tentiontoissuesofdatacoverageandrepresentation. |     |         |          |     | We            |                 |     |     |     |     |     |     |
| ----------------------------------------------- | --- | ------- | -------- | --- | ------------- | --------------- | --- | --- | --- | --- | --- | --- |
| describethosethemes(T1-T3)below.                |     |         |          |     |               | 4.DesigningData |     |     |     |     |     |     |
| Critical dimensions                             |     | of data | are hard | to  | know a priori |                 |     |     |     |     |     |     |
Existingbiasmitigationandmodelevaluationapproaches
(T1).Aproactiveapproachtodatacollectionrequiresknow- attempttoaddressthethemesuncoveredinourformative
| ingwhataxesareimportantforobservation. |     |     |     |     | Asoneinter- |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
interviewsbutarenotcomprehensivetodatacollectionand
vieweeputit,“howdoweknowwhoandwhatismissing?”
|     |     |     |     |     |     | machine | learning | pipelines. | In response | to  | this | disparity, |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | ----------- | --- | ---- | ---------- |
This was a shared difficulty described in nearly all inter- weproposeaniterativeapproachtodatacollectionandma-
views. Whileitistypicallyimpossibletohaveacomplete
3

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
|     |     |     |     |     | C scene                                                                                |                                               | hand                                             | gender | sex                              |
| --- | --- | --- | --- | --- | -------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------ | ------ | -------------------------------- |
|     | A   |     |     |     | b ab c a k c _ k b_ e b d e _ d r _ i g l e h f t t                                    |                                               |                                                  |        | F e m a l e                      |
|     |     |     |     |     | lr ei l f e t f _ t s _ i s d i e d _ e r _ i g l e h f ttt                            | le ft                                         | Fe m a l e                                       |        |                                  |
|     |     |     |     |     | r i g h g t h _ t s _ i s d i e d _ e r _ i g l e h f t                                |                                               |                                                  |        | M a l e                          |
|     |     |     |     |     | st i s t ti t i n t i g n _ g r _ i g l e h f t t                                      |                                               | M a l e                                          | N o    | n - b i n a r y                  |
|     |     |     |     |     | ts t lmo m s t s a a c n a h d n _ id n b i g n e _ g d r _ _ i g l l e e h f f t tt t | rig h t                                       |                                                  |        | O t h e r                        |
|     |     |     |     |     | swa lao ik i a n c _g h _ _ s b l o e w d yl _ y r _ i g l e h f tt                    |                                               | O th e r                                         | Tr a n | s g e n d e r                    |
|     |     |     |     |     | w k n g s l o w l _ r i g h 0.000.02prob0.a0b4ility0.060.08                            | 0.00.1                                        | p0r.o2babi0li.t3y0.40.5 0.0 0.1prob0a.2bility0.3 | 0.4    | 0.0 0.1pro0.b2abilit0y.3 0.4     |
|     |     |     |     |     | race                                                                                   |                                               | agegroup handedness                              |        | handsize                         |
|     |     |     |     |     | AmericanIndianorAlaskaN a t i v e                                                      | 2 1 - 2 5                                     |                                                  |        |                                  |
|     |     |     |     |     | A s i a n                                                                              | 2 3 6 1 - - 3 3 0 5                           | Both                                             |        | large                            |
|     |     |     |     |     | BlackorAfr ic an A m e ri c a n                                                        | 3 6 - 4 0                                     |                                                  |        |                                  |
|     |     |     |     |     | M u lti pl e/ O t h e r                                                                | 4 1 - 4 5                                     | Left                                             |        | medium                           |
|     |     |     |     |     | NativeHawaiianorOtherPac if ic …                                                       | 4 51 6 - - 5 5 0 5                            |                                                  |        |                                  |
|     |     |     |     |     | W h it e                                                                               | < 2 0                                         | Right                                            |        | small                            |
|     |     |     |     |     | 0.000.05prob0a.1b0ility0.150.20                                                        | > 5 6 0.000.050.1p0rob0a.1b5ilit0y.200.250.30 | 0.0 0.2prob0a.4bility0.6                         | 0.8    | 0.00.10.p2rob0a.3bilit0y.40.50.6 |
|     |     |     |     |     | naillength                                                                             |                                               | phonesize                                        |        |                                  |
|     |     |     |     |     | long                                                                                   | max                                           |                                                  |        |                                  |
mid
short
mini
|     |     |     |     |     | 0.00.1 p0r.o2babi0li.t3y0.40.5                                                         | 0.00.10.p2rob0a.3bilit0y.40.50.6                  |                                                           |        |                                  |
| --- | --- | --- | --- | --- | -------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------- | ------ | -------------------------------- |
|     |     |     |     |     | D scene                                                                                |                                                   | hand                                                      | gender | sex                              |
|     |     |     |     |     | b ab c a k c _ k b _ e b d e _ d r _ i g l e h f t t                                   |                                                   |                                                           |        | F e m a l e                      |
|     |     |     |     |     | lr ei l f e t f _ t s_ is d i e d _ e r _ i g l e h f t tt                             | le ft                                             | Fe m a l e                                                |        |                                  |
|     |     |     |     |     | r i g h g t h _ t s _ i s d i e d _ e r _ i g l e h f t                                |                                                   |                                                           |        | M a l e                          |
|     |     |     |     |     | st i s t ti t id nt i g n _g r _ i g l e h f t t                                       |                                                   | M a l e                                                   | N o    | n - b i n a r y                  |
|     | B   |     |     |     | ts t lmo m s t s a a c n a _h d n b_ i n b i g n e _ g d r _ _ i g l l e e h f f t t t | rig h t                                           |                                                           |        | O t h e r                        |
|     |     |     |     |     | swa lao ik i a n c _g h _ s l o e w d yl_ _ yr r _ i g l e h f tt t                    |                                                   | O th e r                                                  | Tr a n | s g e n d e r                    |
|     |     |     |     |     | w k n g s l o w l i g h 0.000.02pr0o.0b4abilit0y.06                                    | 0.08 0.00.1                                       | 0p.2roba0b.i3lity0.4 0.5 0.00.10.2pro0b.3abil0it.4y0.50.6 |        | 0.00.10.2pro0b.3abil0it.4y0.50.6 |
|     |     |     |     |     | race                                                                                   |                                                   | agegroup handedness                                       |        | handsize                         |
|     |     |     |     |     | AmericanIndianorAlaskaN a t i v e                                                      | 2 1 - 2 5                                         |                                                           |        |                                  |
|     |     |     |     |     | A s i a n                                                                              | 2 3 6 1 - - 3 3 0 5                               | Both                                                      |        | large                            |
|     |     |     |     |     | BlackorAfr ic an A m e ri c a n                                                        | 3 6 - 4 0                                         |                                                           |        |                                  |
|     |     |     |     |     | M u lti pl e/ O t h e r                                                                | 4 1 - 4 5                                         | Left                                                      |        | medium                           |
|     |     |     |     |     | NativeHawaiianorOtherPac if ic …                                                       | 4 51 6 - - 5 5 0 5                                |                                                           |        |                                  |
|     |     |     |     |     | W h it e                                                                               | < 2 0                                             | Right                                                     |        | small                            |
|     |     |     |     |     | 0.00.1 0p.2roba0b.i3lity0.4                                                            | 0.5 > 5 6 0.000.050.1p0rob0a.1b5ilit0y.200.250.30 | 0.0 0.2prob0a.4bility0.6                                  | 0.8    | 0.0 0.2prob0a.4bility0.6 0.8     |
|     |     |     |     |     | naillength                                                                             |                                                   | phonesize                                                 |        |                                  |
typea excptueaclted
|     |     |     |     |     | long | max |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
mid
short
mini
|     |     |     |     |     | 0.0 0.2prob0a.4bility0.6 | 0.8 0.00.10.p2rob0a.3bilit0y.40.50.6 |     |     |     |
| --- | --- | --- | --- | --- | ------------------------ | ------------------------------------ | --- | --- | --- |
Figure2. (A)Dashboardpromptspractitionersthroughdesigningtheirdatasets.(B)Beforecollection,thedashboardpromptsdocumenta-
tionofexpecteddistribution.(C)Thesearevisualizedashistograms.(D)Asdataiscollected,truedistributions(pink)overlayexpected
distributions(blue),highlightingdivergentpatterns.
chinelearningthatwecalldesigningdata. Designingdata prompts, drop-down selections, and simple declarations.
respondstoourthemesbyintroducinginterventionsbefore, Whenthedatarelatestoahumansubject(i.e., imagesof
during,andaftercollection&training. ShowninFigure1, faces,movementdata,orvoicerecordings),ourdashboard
eachstepisintendedtocomplementtheothers,compensat- promptsself-reporteddemographicinformationaboutteams
ingfortheirlimitationstoholisticallyimprovethedevelop- orindividualusersinvolvedindevelopingthedataset. After,
mentanddeploymentprocess. Wedescribeeachbelow. usersareaskedwhatdatadistributionstheyexpect. Thisis
|                   |          |               |         |         | animportantstep: |     | priorworksuggeststhatsimplyrecogniz- |     |     |
| ----------------- | -------- | ------------- | ------- | ------- | ---------------- | --- | ------------------------------------ | --- | --- |
| I: Pre-Collection | Planning | To facilitate | broader | consid- |                  |     |                                      |     |     |
ingsuchinformation(Fish&Stark,2021;Kimetal.,2017),
| eration of | critical facets | of data, data | design | requires | ex- |     |     |     |     |
| ---------- | --------------- | ------------- | ------ | -------- | --- | --- | --- | --- | --- |
andintroducingdesignfrictions(Gullstro¨m,2012;Penny-
plicitdocumentationofwhatwillbecollected—including
|     |     |     |     |     | cooketal.,2020), |     | mayimprovethequalityofdatawork. |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | ------------------------------- | --- | --- |
expecteddimensionsanddistributionsofdata—beforecol-
Anexampleofthedimensionsandrelateddistributionsis
| lectionbegins. | Ourdocumentationprocessensuresdevelop- |     |     |     |                 |     |                                    |     |     |
| -------------- | -------------------------------------- | --- | --- | --- | --------------- | --- | ---------------------------------- | --- | --- |
|                |                                        |     |     |     | showninFigure2. |     | Fromtheseinputteddimensions,audits |     |     |
erspaycloseattentiontodatadiversityandcoverageearly
|                                       |              |                   |             |     | of population               |     | statistics, | missing | data, and undersampled   |
| ------------------------------------- | ------------ | ----------------- | ----------- | --- | --------------------------- | --- | ----------- | ------- | ------------------------ |
| in an ML                              | pipeline and | creates reference | points      | for | com-                        |     |             |         |                          |
|                                       |              |                   |             |     | subsetsarepresentedtousers. |     |             |         | Differentcategoriesofthe |
| parisonwhennewinformationisuncovered. |              |                   | Thisprocess |     |                             |     |             |         |                          |
data,includingdemographics,metadata,taskspecifics,class
alignswithpriorworkinheuristics,implicitbias,cognition,
representation,andintersectionalcategoriesarevisualized.
| andfakenewssusceptibility: |     | deliberation—reflection—can |     |     |     |     |     |     |     |
| -------------------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
correctintuitivemistakes,suchasthosemadeindatacollec- II: Collection Monitoring By stating expected distribu-
tion(Pennycook&Rand,2019;Bagoetal.,2020;Toplak tions prior to collection, auditing the data against those
et al., 2011; Saul, 2013). While it is difficult to enumer- distributionsisstraightforward,allowingreadjustmentsto
ateallcriticalfactors,thisfirststepinourdesigningdata be made quickly when necessary. Each view reflects the
processprovidesscaffolding,respondingtoourfirsttheme data’sevolution,allowingreal-timeinsightonwhereaddi-
(T1): criticaldimensionsofdataarehardtoknowapriori. tionalcollectionisneeded. Ourdashboardincludesgraphs
highlightingdistributiondisparitiesthatwereperpetuated
| As shown | in Figure 2 (A), | Pre-Collection | Planning |     | asks |     |     |     |     |
| -------- | ---------------- | -------------- | -------- | --- | ---- | --- | --- | --- | --- |
orintroducedasthedatawascollected,asshownin Fig-
aseriesofquestionstopromptreflexiveconsiderationfor
ure2(D).Thesechartsbenefitusersbynotingwhenthedata
individuals’personalbiasesthroughaseriesofopen-text
collectionprocessiseitherskewed(forexample,through
4

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
conveniencesampling)orwhenpreviouslystatedexpecta- currenttrainingset,weobtaintheactivationsfromlayerl,
tionsdidnotalignwithreality. Thisstep’siterativenature thenusePCAtoreduceitsdimensionality. Thisprojection
shortenstheresponsetimetocorrectfundamentalerrorsin stepservestwopurposes: itreducesthedispersionofpoints
data,highlightinglimitationsthatmayhaveremainedunno- thatistypicalinhighdimensionalspaces,andmakesthe
ticed,asdescribedinoursecondandthirdthemes: difficulty remainingcomputationmoretractable.
ofcollectionleadstocompromises(T2),andmodelfailures
We then perform a Variational Bayesian estimation of a
areinvisiblewithoutparticipationanditeration(T3).
Gaussianmixture(Zobay,2014)intheprojectedspace. The
III:DataFamiliarityAfteramodelistrained,understand- fittedGMMallowsustogiveafamiliarityscoretoeachnew
ingwhatithasandhasnotlearnedappropriatelyiscritical sample. Giventhissample,weextracttheactivationfrom
1. The value in this form of auditing is significant: some thesamelayerl,againapplydimensionalityreduction,then
datamayprovemoredifficulttolearnduetotheirinherent evaluatethelog-likelihoodprovidedbythefittedGMM—
complexity, orfromnothavingenoughsimilarexamples. thisisourfamiliarityscore.Ifthesamplefallsintoadensely
Despitetheincreasedrigorofdatacollectionasresultofour populated area, its log-likelihood will be high: from the
earlierdesigningdatasteps,expectedandactualdatadistri- perspective of the features extracted by the current state
butionsmightnotmatchthelearningneedsforthemodel, of layer l, this sample appears as familiar. Conversely,
thus requiring a stop gap such as under or oversampling, if the sample falls into a scarcely populated area, its log-
generatingsyntheticdata,orcontinueddatacollection. We likelihood will be low and the sample less familiar. This
adoptdensityestimation(DE)tomeasurehowfamiliarour measurementcanbeappliedtonewsamples—thosenotseen
modeliswithindividualdatapoints. WhileDEforOOD byamodelpreviously—orontrainingsamples. Familiarity
detectioniswellstudied(Gawlikowskietal.,2021),ouruse scoresarepresentedinourdashboardthroughaseriesof
ofDEtodirectdatawork(e.g. collectionandannotation)is graphsdepictingtheirrangeandfrequency,providingusers
unique. Bygaininginsightonhowapartiallytrainedmodel directionforfuturedataefforts;samplesthatareunfamiliar
perceivesdata,wecanfocuseffortsonthemostusefulsub- arereconciledwithhumanexpectations.
sets,reweightingorreplacingthedataaccordingly. Inthis
way, eventhoughdifficultyofcollectionleadstocompro- 5.TaskSelection,DataCollection,Modeling
mises(T2),weareabletointeractivelyuncoverremaining
Weinstantiatedourdesigningdataapproachthroughahu-
issues,assuggestedby(T3).
man activity recognition (HAR) task using inertial mea-
Unfamiliarsamplesare“edgecases”—thosethateitherare surementunit(IMU)data—Whiledesigningdatagenerally
notrepresentedappropriatelywithinthedataset,areparticu- appliestoalldatacollectionandmachinelearningprocesses,
larlychallengingforthemodeltolearn,orwereerroneously ourselectionofdatatypeandtaskweremotivatedbythe
collected(e.g.,noisy). Inearlydatasetdevelopment,famil- unique challenges IMU data presents to building data di-
iarityscoresactasusefulchecksfordatawithlittlesignal— versity. First, IMUdatainherentlylackstheclosenessof
sampleswhereweexpectthemodeltoperformwellyetmay mapping(Blackwelletal.,2001)thatimageandaudiodata
benoisyandthusrequirehumaninspection. Tomeasure havetohumanmodelsoftheworld,makingitmoredifficult
thefamiliarityofthedata,weincorporatedensityestimates toaudit. RecognizingwhenIMUdatacoverageisincom-
oflayeractivationsacrossaneuralnetwork(NN).Wefocus pletecanbedifficultwhencomparedtoimagedataaslevels
onthepenultimatelayerbeforethepredictionsoftmaxasit ofabstractionoftenobfuscatefundamentalproblemsina
isthefinalfeaturerepresentationusedtomakeaprediction. dataset (Ramasamy Ramamurthy & Roy, 2018; Bartram
PassingN inputsthroughthenetworkproducesanactiva- et al., 2021)). Second, IMU data requires contextualiza-
tionmatrixA(N)∈RN×M forallM neuronsinsubsetof tion to create meaning—real-time labeling, or additional
selectedlayersL′ ⊆L. WelearnaGaussianMixturemodel informationfromaudioandvideo—andishardertocollect,
ontheselayeractivationsasgivenbythefollowing: unlikeimagesandaudioclipswhicharenowubiquitous(Ra-
M masamyRamamurthy&Roy,2018). YetIMUdatastillhas
(cid:88)
p(x|λ)= w g(x|µ ,Σ ) (1) thepotentialtobiasMLmodels. Thus,weevaluatedesign-
i i i
i=1 ingdata’smeritwithinatypicallychallengingcontext.
where x is a matrix of layer activations, w i ,i = 1,...,M OurexperimentaltaskresemblesworkbyGoeletal.(2013),
arethemixtureweights,andg(x|µ i ,Σ i ),i = 1,...,M are whoimprovedmobiletextentrybycategorizingdifferent
thecomponentGaussiandensities2. Foreachsampleinthe hand positions when users typed. Before collection, par-
ticipantsprovideddemographicinformationandmetadata.
1Thepurposeofdesigningdataisnottoreplaceexistingtools
Thisincludedrace,ethnicity,gender,sex,age,handlength
butrathertoencourageaholisticapproachthatincorporatesnew
ML techniques. For interventions during training, we refer to (mm),naillength(mm),handdominance,phoneversionand
existingliterature(Murphy,2012;Japkowicz&Stephen,2002).
2ThismodeofDEisinterchangeablewithotherDEorOOD methodssuchas(Wkeglarczyk,2018;Leeetal.,2018).
5

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
phonesize. Wecollecteddatafrom33participantsrecruited moremeaningfultoperformancethanothers. Performance
overthreeseparateperiodsinresponsetodatadisparities disparity—suchasloweraccuracy—acrosscategoriesde-
highlightedbyourdashboard. Intotal,wecollected>3.88 spiteequalsamplesizewouldsupportthishypothesis.
millionmeasurementsfrom1455sessions.Thisdataisused
EvaluationWhencomparedtomodelstrainedonlessdi-
topopulatedashboard,trainandevaluateclassifiers,then
versedata,wefoundthatmodelswithdiversedatahadan
| refined according |     | to familiarity | evaluations. | We  | use 1D |     |     |     |     |     |     |     |
| ----------------- | --- | -------------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
overallhigheraccuracyandperformedbetteracrossintersec-
convolutionalneuralnets(CNNs)forclassification3.
|     |     |     |     |     |     | tionalgroups,asshownin |     |     | Figure3. | Forexample, |     | Figure3 |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | -------- | ----------- | --- | ------- |
6.ModelingExperiments B shows a significant dip in performance for the model
trainedwithoutdatafromtheright-side-leftconditioncom-
Theabilitytoproducediversesubsetsdoesnotguarantee paredtodiversemodel(Figure3C).Thisisasweantici-
appropriaterepresentationofsensitiveattributes. Ourap- pated,andweseethatfordatawhereparticipantsweretyp-
proach to encouraging fair outcomes considers the amal- ingintheright-side-leftcondition,theless-diversemodel
gamation of both data and model. The following experi- actuallyperformsworsethanrandomchance. Thispattern
mentsadaptthefollowingdefinitionoffairness—ratherthan isrepeatable—acrosskmodelswhereweintentionallyleft
seekahighaverageaccuracyacrossclasses,welookatnu- outonegroup(Figure3A),weseeacorrelateddiagonalof
ancedperformance—accuracy,loss,andmisclassification— lightercolorindicatinglowertestingaccuracy,supporting
between intersectional groups. To this end, we consider ourhypothesisthattheextensivecharacteristicswecollected
severalquestionsaspartofourdesigningdataevaluation: data for do effect IMU performance. In contrast, diverse
(Q1)Doesauditingtoincreasedatadiversityimprovemodel modelsshowlessperformancevariance,insteadperforming
betteracrossdifferentdemographics—matchingwhatwe
| generalizability? | and(Q2)Isdatafamiliarityusefulinau- |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ditingmodel&data?Weevaluateourinterventionsthrough wouldhopetoachievetominimizeworstgroupgeneraliza-
aseriesofmodelingexperiments. First, weshowthatdi- tion(Sagawaetal.,2019). Wefoundsomeintersectional
versedatadoesleadtobetterperformance. Then,weuse subgroupsperformeddrasticallydifferentcomparedtotheir
familiaritytouncovernoisydatawithinthedatasetandde- overallgroupperformance. Intypicalevaluations,thisnu-
anceisoftenobfuscatedbyaggregation,yetwewereable
scribehowremovingthesesamplesimpactsintersectional
accuracy. Finally,weshowthatsupplementingthedataset tocaptureitusingsimpleinterventionsandvisualizations.
withunfamiliarsamplesimprovesmodelperformance.
|                  |     |                            |     |     |     | 6.2.Familiarity: | Isdatafamiliarityusefulinauditing |     |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | ---------------- | --------------------------------- | --- | --- | --- | --- | --- |
| 6.1.DiverseData: |     | Doesauditingtoincreasedata |     |     |     |                  |                                   |     |     |     |     |     |
model&data?
diversityimprovemodelgeneralizability?
|     |     |     |     |     |     | There are | two scenarios |     | where | familiarity | is useful | in di- |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ----- | ----------- | --------- | ------ |
WesoughttoanswerQ1throughourfirstsetofexperiments.
|     |     |     |     |     |     | rectingdatasetiteration: |     |     | tofacilitatedatacleaning,andto |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------------ | --- | --- | --- |
Wecompare“diverse”modelsto“lessdiverse”models. We encourageappropriaterepresentationofdiversedatafora
| do so for | two reasons: | first, | it may not | be clear | to practi- |     |     |     |     |     |     |     |
| --------- | ------------ | ------ | ---------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
givenmodel.Whenadatasetcontainsnoisydata,familiarity
tionersthatcollectingdiversedataearlyindevelopmentis
|     |     |     |     |     |     | canhelpsurfacethesesamplesforhumanevaluation. |     |     |     |     |     | Ifa |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
critical to building functional tools. Second, despite best datasethasalreadybeencleaned,thenfamiliarityisusedto
effortstocuratealistofmeaningfulcharacteristics,wedid
|     |     |     |     |     |     | highlightsamplesthatlessfamiliar. |     |     |     | Weevaluatefamiliar- |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ------------------- | --- | --- |
notknowiftheseadditionaldatadimensionshadanytrue ity’sefficacyindirectingdatasetiteration(Q2)througha
effectontheclassificationtask.
seriesofexperimentstoimproveperformanceonthesame
|     |     |     |     |     |     | testingdatausedin |     | subsection6.2,modifyingtrainingdata |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------------------------------- | --- | --- | --- | --- |
Bothdiverseandlessdiversemodelsaretrainedusingthe
|     |     |     |     |     |     | but maintaining | sample |     | size parity. | Modifications |     | to the |
| --- | --- | --- | --- | --- | --- | --------------- | ------ | --- | ------------ | ------------- | --- | ------ |
samenumberoftrainingsamplesandareevaluatedonthe
same test data. Less diverse models are trained on data trainingdataarecompletedusing“self-familiarity”scores
(i.e.,familiarityoftrainingdata)toavoidoverfitting.
| whereonegroup(e.g. |               | smallhanded)wasleftout. |                  |     | Inthis   |                   |     |               |     |     |         |          |
| ------------------ | ------------- | ----------------------- | ---------------- | --- | -------- | ----------------- | --- | ------------- | --- | --- | ------- | -------- |
| way, we perform    | leave-one-out |                         | cross-validation |     | and con- |                   |     |               |     |     |         |          |
|                    |               |                         |                  |     |          | 6.2.1 Familiarity |     | for Debugging |     | Our | dataset | was col- |
sider the specific effects of a given demographic group. lected“inthewild”withoutadditionalannotationfrompar-
All models were trained with the same sample size. We ticipants. Whileparticipantsweregivenclearinstructions,
| thengeneratepredictionsfromtheoriginaltestset. |     |     |     |     | Paying |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
weanticipatedthatasmallnumberofsampleswouldshow
close attention to intersectional groups, we expect to see significantnoiseordistortion—participantsmightdroptheir
moreperformancestratificationinlessdiversemodels. We phones as they type, or switch hands part way through a
comparemodelsacrossoverall,group-specific,andintersec- session. Such samples may introduce unwanted effects
tionalaccuracies. Wehypothesizethatsomecategoriesare downstreamifleftuncaught. Giventhesizeofthedataset,
inspectingtimeseriesplotsforeachsessionwasuntenable.
3Seeappendixfordetailsondataprocessing,modeling,and
|     |     |     |     |     |     | Instead, incorporating |     | familiarity |     | may greatly |     | reduce the |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | ----------- | --- | ----------- | --- | ---------- |
iteratingwithPre-CollectionPlanning&Monitoring
|     |     |     |     |     |     | numberofsamplestoevaluate. |     |     | Byusinganleastpartially |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ----------------------- | --- | --- | --- |
6

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
B C
A
stomach_bed_left Category
right_side_right
| back_bed_left   |     |     |     |     |     | age_group  |
| --------------- | --- | --- | --- | --- | --- | ---------- |
| right_side_left |     |     |     |     |     | hand_size  |
| left_side_left  |     |     |     |     |     | handedness |
walking_slowly_right nail_length
walking_slowly_left phone_size
| Scene sitting_right |     |     |     |     |     | race |
| ------------------- | --- | --- | --- | --- | --- | ---- |
scene
stomach_bed_right
| sitting_left |     |     |     |     |     | sex |
| ------------ | --- | --- | --- | --- | --- | --- |
left_side_right
| tesataDgnitseTfospuorgbuS standing_right |     |     |     |     |     | Subgroup |
| ---------------------------------------- | --- | --- | --- | --- | --- | -------- |
| standing_left                            |     |     |     |     |     | Accuracy |
back_bed_right
| White |     |     |     |     |     | 1.0 |
| ----- | --- | --- | --- | --- | --- | --- |
Race Asian
Black
| Multiple |     |     |     |     |     | 0.8 |
| -------- | --- | --- | --- | --- | --- | --- |
Hand Left
Right
| medium |     |     |     |     |     | 0.6 |
| ------ | --- | --- | --- | --- | --- | --- |
Hand Size large
small
Female
| Sex Male |     |     |     |     |     | 0.4 |
| -------- | --- | --- | --- | --- | --- | --- |
26-30
31-35
| 41-45 |     |     |     |     |     | 0.2 |
| ----- | --- | --- | --- | --- | --- | --- |
Age 36-40
46-50
| >56 |     |     |     |     |     | 0.0 |
| --- | --- | --- | --- | --- | --- | --- |
21-25
Nail long
Length short
mini
Phone mid
Size max
| tfel_deb_hcamots thgir_edis_thgir tfel_deb_kcab tfel_edis_thgir tfel_edis_tfel thgir_ylwols_gniklaw tfel_ylwols_gniklaw | thgir_gnittis thgir_deb_hcamots tfel_gnittis thgir_edis_tfel thgir_gnidnats tfel_gnidnats thgir_deb_kcab etihW naisA kcalB | elpitluM tfeL thgiR muidem egral llams elameF elaM 03-62 53-13 | 54-14 04-63 05-64 65> 52-12 gnol trohs inim dim | xam enecs_atad_esrevid ecar_atad_esrevid ssendednah_atad_esrevid ezis_dnah_atad_esrevid xes_atad_esrevid puorg_ega_atad_esrevid htgnel_lian_atad_esrevid ezis_enohp_atad_esrevid | 0.0 0.5 1.0 0.0 | 0.5 1.0 |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------- |
Subgroup Subgroup
Accuracy Accuracy
htgneL
|     | enecS ecaR | dnaH dnaH | enohP         |     |     |     |
| --- | ---------- | --------- | ------------- | --- | --- | --- |
|     |            | eziS xeS  | egA liaN eziS |     |     |     |
DiverseData
|     |     | Models |     | Models |     |     |
| --- | --- | ------ | --- | ------ | --- | --- |
Figure3. Performancepersubgroupontestingdata(y-axis)permodel(x-axis),splitacrosscategories.Thelargesquarematrix(left)
showsaccuracywhereasubgroupwasleftoutofthetrainingset.Therectangularmatrix(right)showsperformanceofmodelstrainedon
diversedata.(A)Thearrowhighlightsthediagonalofthematrix:subgroupsofdatathatperformworsethanothers,correspondingto
themodeltrainedwithoutthisparticularsubgroup.(B)E.g.,takingtheleft side rightmodelfromthematrix,weseeitperforms
poorlyontheleft side rightsubgroup.(C)Modelstrainedonsamesizedyetmorediversedatasetshownodipinaccuracy.
A Diverse Data Intersectional
 B Post-Familiarity Intervention Intersectional

 Group Accuracy
Change in Accuracy
Figure4. (A)Accuracyforintersectionalsubgroupsinadiversedatamodel.(B)Differenceinaccuracyforsubgroupsbefore&after
familiarityinterventions(greenispositive,purplenegative).
7

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
trainedmodelonthedatasettouncoverunfamiliarsamples, groups,asdescribedin Section6.1. Thesescoresareused
familiarityoffersapossiblesolutiontocapturenoisydata, determinenextstepsforadditionaldatacollection,augmen-
presentinganalternativetoworksuchas (Pleissetal.,2020; tation,ormodified(over/under)sampling. Here,wesample
Shen&Sanghavi,2019),whichincorporatelossasametric out a percentage of the most familiar data, and add data
forcapturingnoisysamples. Wehypothesizethatleastfa- matchingtheintersectionalcharacteristicsforthesameper-
miliarsampleswithinanoisydatasetwillincludeinstances centageofleastfamiliardata. Substituteddatawasheldout
ofnoisydataposingthegreatestharmtothemodel. fromtrainingin Section6.1,thusisnewtothemodels. We
|             |                    |             |               | replace | samples | based on | metadata characteristics, |     | using |
| ----------- | ------------------ | ----------- | ------------- | ------- | ------- | -------- | ------------------------- | --- | ----- |
| We explored | how to incorporate | familiarity | as a tool for |         |         |          |                           |     |       |
combinatorialoptimizationtobestmatchunfamiliardata.
debuggingfirstthroughanautomatedapproachtoremoving
|                                      |                                           |     |               | Using PCA,             | we                                       | project     | down to 50                  | dimensions, | then fit   |
| ------------------------------------ | ----------------------------------------- | --- | ------------- | ---------------------- | ---------------------------------------- | ----------- | --------------------------- | ----------- | ---------- |
| data,thenbyincorporatinghumanreview. |                                           |     | Ourprotocolis |                        |                                          |             |                             |             |            |
|                                      |                                           |     |               | 5 GMMs                 | to last                                  | dense layer | for each                    | 1D CNN      | trained in |
| asfollows:                           | first,wetrainaninitialmodelonallavailable |     |               |                        |                                          |             |                             |             |            |
|                                      |                                           |     |               | Section6.1.            | Scoringourtrainingdata,wesavefamiliarity |             |                             |             |            |
| trainingdata.                        | Weapplyself-familiaritytothetrainingand   |     |               |                        |                                          |             |                             |             |            |
|                                      |                                           |     |               | scoresandmodelweights. |                                          |             | Wevarytherangeoffamiliarity |             |            |
testingset,selectingonly0.1%ofthedatacorrespondingto
|                       |     |                                |     | scores to | sample | from, percentage | of  | data, and | two sam- |
| --------------------- | --- | ------------------------------ | --- | --------- | ------ | ---------------- | --- | --------- | -------- |
| leastfamiliarsamples. |     | Thisdataiseitherremovedfromthe |     |           |        |                  |     |           |          |
plinginmethods—topkandrandomselectionfromaleast
dataset,orvisualizedandmanuallyreviewedpersampleto
|                                              |     |     |     | familiardatarange—comparedtoarandombaseline. |     |     |     |     | We  |
| -------------------------------------------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
| evaluateiftheyaretrulynoisyorsimplyuncommon. |     |     | We  |                                              |     |     |     |     |     |
structuretheseexperiments—varyingwindowsizeandsam-
removedthesamenumberofsampleswithmanualreview
|     |     |     |     | plingpercentage—touncoverasweetspot: |     |     |     | removingtoo |     |
| --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ----------- | --- |
4.
| of truly noisy | data as with | the automated | removal We |     |     |     |     |     |     |
| -------------- | ------------ | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
muchdatamayharmperformanceonfamiliargroups,and
comparedoutcomesofbothautomatedremovalandremoval
toolargeawindowmightimpingeonlessfamiliardata.
throughhumanreview,butfoundthatdeletingapercentage
ofleastfamiliardataremovedbothnoisydataandimportant EvaluationSelf-familiarityscorescreateadistinctcurve,
outliers. Weevaluatethisoutcomebycomparingtheresults withunfamiliardatafallingintothelong-tail. Wefindac-
ofthefollowingexperimenttoimprovedatadiversityacross curacy scores are far more striated prior to familiarity in-
eachapproachtodatacleaningwhencomparedtoabaseline terventions,showingsomeconceptsarelearnedbetterthan
wherenodataisremoved. others. Followingfamiliarityinterventions,modelsdoshow
|     |     |     |     | targetedimprovement. |     | Modelsperformedmorepoorlyin |     |     |     |
| --- | --- | --- | --- | -------------------- | --- | --------------------------- | --- | --- | --- |
EvaluationInpractice,wefoundthatfamiliarityworked
regionswithhighnumbersoflowfamiliaritydata(anex-
| wellasatoolfordebugging. |     | Beforeremovingnoisydata |     |          |       |          |           |              |        |
| ------------------------ | --- | ----------------------- | --- | -------- | ----- | -------- | --------- | ------------ | ------ |
|                          |     |                         |     | ample of | which | is shown | in Figure | 4). Of note, | models |
fromthecompletedataset,alargepercentageoftheleast
didnotnecessarilyimproveoverall—althoughthiswasfre-
familiarsamplesshowedsignificantdistortion,despiteour
quentlythecase—insteadshowingimprovementinareas
| effortstonormalizethedata. |     | Becauseofthepresenceof |     |     |     |     |     |     |     |
| -------------------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
oflowperformanceandregressioninthosewithhighper-
thesenoisydata,runningourfamiliarityexperimentswith
|                       |                 |                             |                  | formance.                                       | In Figure4,weshowmodelperformanceson |                                 |     |     |       |
| --------------------- | --------------- | --------------------------- | ---------------- | ----------------------------------------------- | ------------------------------------ | ------------------------------- | --- | --- | ----- |
| data that             | was not cleaned | did not show                | the same levels  |                                                 |                                      |                                 |     |     |       |
|                       |                 |                             |                  | intersectionalgroups:                           |                                      | (A)isamodeltrainedonthediverse- |     |     |       |
| ofgeneralimprovement. |                 | Inthiscase,matchingmetadata |                  |                                                 |                                      |                                 |     |     |       |
|                       |                 |                             |                  | data-scenedatasetwithnofamiliarityintervention. |                                      |                                 |     |     | Wecan |
| to noisy              | samples was     | not the correct             | comparison—these |                                                 |                                      |                                 |     |     |       |
seeloweraccuraciesinback-bed-leftandright-side-left
sampleswerenotexemplarsofthesubpopulation.
|     |     |     |     | comparedtoothersubgroups. |     |     | Incontrast,sitting-leftand |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --- | -------------------------- | --- | --- |
Inmanuallyevaluatingourunfamiliardatabeforeremoval, back-bed-right had much higher accuracy compared to
we uncovered cases where unfamiliar samples were not othersubgroups. Figure4(B)showsthedifferencebetween
noisybutratherunderrepresentedintersectionalgroups. For thismodelandonetrainedonthesamedatawithfamiliar-
instance, a person identifying as an Asian Female with ityinterventions. Regionswithrelativepoorperformance
Small hands and Large phone was as unfamiliar to the improveddramatically,whilethosewithhigheraccuracies
modelasincrediblynoisyexamples. Noisydatahasdiffer- showedsomeregression. Incorporating0.1%leastfamiliar
entimplicationsforthemodelthanunusualsamples. For datawasoptimalforourexperiments. Overall,familiarity
thisreason,removing0.1%oftheleastfamiliardatapriorto consistentlycapturedunder-representedsamples.
experimentsdidnotimproveperformancetotheextentseen
7.Conclusion
| whenmanualreviewwasimplemented. |     |     | Thatis,familiarity |     |     |     |     |     |     |
| ------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
cannotdistinguishbetweendistortednoiseandunderrepre-
|                  |                                    |     |     | We need  | processes   | that  | integrate data | and models | in sys-   |
| ---------------- | ---------------------------------- | --- | --- | -------- | ----------- | ----- | -------------- | ---------- | --------- |
| sentedorOODdata. | Fordatasetswheresignificantnoiseis |     |     |          |             |       |                |            |           |
|                  |                                    |     |     | tematic, | transparent | ways. | While each     | step of    | designing |
present,humanreviewisnecessarytoevaluatedataquality.
datacanbeincorporatedinisolation,theinterventionsare
complimentary,compensatingforthecascadingeffectsof
| 6.2.2FamiliarityforDiverseDataCoverage |     |     | Next, we |                                |     |     |                   |     |     |
| -------------------------------------- | --- | --- | -------- | ------------------------------ | --- | --- | ----------------- | --- | --- |
|                                        |     |     |          | upstreamanddownstreammissteps. |     |     | Dataisshapedbythe |     |     |
comparefamiliarityscoresacrossthedifferentdescriptive
perspectiveoftheobserver;ourworkhighlightshowsys-
4ExperimentalprotocolcanbefoundintheAppendix. tematicprocessesmaycurtailbiasearlyindevelopment.
8

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Acknowledgements Bartram, L., Correll, M., andTory, M. Untidydata: The
|     |     |     |     |     |     |     | unreasonable |     | effectiveness |     | of tables. |     | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | ---------- | --- | ----- | -------- |
WethankourcolleaguesatApplefortheirtimeandeffort
arXiv:2106.15005,2021.
| participatinginourresearch. |     |     | WeespeciallythankDonghao |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RenandHaldenLinfortheirhelpbuildingtheiOSapplica-
|     |     |     |     |     |     |     | Ben-David, | S., | Hrubesˇ, | P., Moran, |     | S., Shpilka, |     | A., and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ---------- | --- | ------------ | --- | ------- |
tionandKayurPatelforhisguidance. AspenHopkinswas Yehudayoff,A. Learnabilitycanbeundecidable. Nature
partiallysupportedbytheSiebelFellowship.
MachineIntelligence,1(1):44,2019.
|     |     |     |     |     |     |     | Bender,E.M.andFriedman,B. |     |     |     | Datastatementsfornatural |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- |
References
|     |     |     |     |     |     |     | languageprocessing: |     |     | Towardmitigatingsystembiasand |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
https://
Facets. Google PAIR, 2017. URL enablingbetterscience. TransactionsoftheAssociation
pair-code.github.io/facets/. forComputationalLinguistics,6:587–604,2018.
Aisch,G.,Cox,A.,andQuealy,K.Youdrawit:Howfamily
Blackwell,A.F.,Britton,C.,Cox,A.,Green,T.R.,Gurr,C.,
incomepredictschildren’scollegechances.TheNewYork Kadoda,G.,Kutar,M.,Loomes,M.,Nehaniv,C.L.,Petre,
Times,28,2015.
M.,etal.Cognitivedimensionsofnotations:Designtools
|          |                 |     |              |     |        |          | forcognitivetechnology. |     |     | InInternationalConferenceon |     |     |     |     |
| -------- | --------------- | --- | ------------ | --- | ------ | -------- | ----------------------- | --- | --- | --------------------------- | --- | --- | --- | --- |
| Amershi, | S., Chickering, |     | M., Drucker, |     | S. M., | Lee, B., |                         |     |     |                             |     |     |     |     |
CognitiveTechnology,pp.325–341.Springer,2001.
| Simard,P.,andSuh,J. |          |       | Modeltracker: | Redesigningper- |     |         |                                  |     |     |     |     |            |     |      |
| ------------------- | -------- | ----- | ------------- | --------------- | --- | ------- | -------------------------------- | --- | --- | --- | --- | ---------- | --- | ---- |
| formance            | analysis | tools | for machine   | learning.       |     | In Pro- |                                  |     |     |     |     |            |     |      |
|                     |          |       |               |                 |     |         | Buchanan,L.,Park,H.,andPearce,A. |     |     |     |     | Youdrawit: |     | What |
ceedingsofthe33rdAnnualACMConferenceonHuman
|     |     |     |     |     |     |     | gotbetterorworseduringobama’spresidency. |     |     |     |     |     | TheNew |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | ------ | --- |
FactorsinComputingSystems,pp.337–346,2015.
YorkTimes,15,2017.
Amershi,S.,Weld,D.,Vorvoreanu,M.,Fourney,A.,Nushi,
|     |     |     |     |     |     |     | Buolamwini, | J.  | and Gebru, | T.  | Gender | shades: |     | Intersec- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | ------ | ------- | --- | --------- |
B.,Collisson,P.,Suh,J.,Iqbal,S.,Bennett,P.N.,Inkpen,
tionalaccuracydisparitiesincommercialgenderclassifi-
| K., et al. | Guidelines |     | for human-ai | interaction. |     | In Pro- |         |                                          |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------------ | ------------ | --- | ------- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |            |     |              |              |     |         | cation. | InACMConferenceonFairness,Accountability |     |     |     |     |     |     |
ceedingsofthe2019CHIConferenceonHumanFactors
andTransparency,pp.77–91,2018.
inComputingSystems,pp.1–13,2019.
|            |         |     |                 |     |       |       | Celis, L. | E., Deshpande, |       | A.,      | Kathuria, | T., | and   | Vishnoi, |
| ---------- | ------- | --- | --------------- | --- | ----- | ----- | --------- | -------------- | ----- | -------- | --------- | --- | ----- | -------- |
| Anari, N., | Gharan, | S.  | O., and Rezaei, | A.  | Monte | carlo |           |                |       |          |           |     |       |          |
|            |         |     |                 |     |       |       | N. K.     | How            | to be | fair and | diverse?  |     | arXiv | preprint |
markovchainalgorithmsforsamplingstronglyrayleigh
arXiv:1610.07183,2016.
InCon-
distributionsanddeterminantalpointprocesses.
ferenceonLearningTheory,pp.103–115,2016.
|                                             |     |     |     |     |     |         | Celis, L.     | E., Keswani, |         | V.,      | Straszak, | D.,   | Deshpande, |         |
| ------------------------------------------- | --- | --- | --- | --- | --- | ------- | ------------- | ------------ | ------- | -------- | --------- | ----- | ---------- | ------- |
|                                             |     |     |     |     |     |         | A., Kathuria, |              | T., and | Vishnoi, |           | N. K. | Fair       | and di- |
| Angwin,J.,Larson,J.,Mattu,S.,andKirchner,L. |     |     |     |     |     | Machine |               |              |         |          |           |       |            |         |
ProPublica,23,2016. verse dpp-based data summarization. arXiv preprint
bias.
arXiv:1802.04023,2018.
| Arjovsky, | M.,       | Bottou, | L., Gulrajani, |     | I., and | Lopez-   |           |       |        |           |     |          |         |     |
| --------- | --------- | ------- | -------------- | --- | ------- | -------- | --------- | ----- | ------ | --------- | --- | -------- | ------- | --- |
|           |           |         |                |     |         |          | Chao, A., | Chiu, | C.-H., | and Jost, | L.  | Unifying | species | di- |
| Paz, D.   | Invariant | risk    | minimization.  |     | arXiv   | preprint |           |       |        |           |     |          |         |     |
arXiv:1907.02893,2019. versity,phylogeneticdiversity,functionaldiversity,and
|     |     |     |     |     |     |     | related | similarity | and | differentiation |     | measures |     | through |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --------------- | --- | -------- | --- | ------- |
Arnold,M.,Bellamy,R.K.,Hind,M.,Houde,S.,Mehta, hillnumbers. AnnualReviewofEcology,Evolution,and
S.,Mojsilovic´,A.,Nair,R.,Ramamurthy,K.N.,Olteanu, Systematics,45:297–324,2014.
| A.,Piorkowski,D.,etal. |     |     | Factsheets: | Increasingtrustin |     |     |                             |     |     |     |                      |     |     |     |
| ---------------------- | --- | --- | ----------- | ----------------- | --- | --- | --------------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
|                        |     |     |             |                   |     |     | Corbett-Davies,S.andGoel,S. |     |     |     | Themeasureandmismea- |     |     |     |
aiservicesthroughsupplier’sdeclarationsofconformity.
IBMJournalofResearchandDevelopment,63(4/5):6–1, sureoffairness:Acriticalreviewoffairmachinelearning.
arXivpreprintarXiv:1808.00023,2018.
2019.
Asudeh,A.,Jin,Z.,andJagadish,H. Assessingandreme- Cruciani,F.,Vafeiadis,A.,Nugent,C.,Cleland,I.,McCul-
dyingcoverageforagivendataset. In2019IEEE35th lagh,P.,Votis,K.,Giakoumis,D.,Tzovaras,D.,Chen,L.,
|     |     |     |     |     |     |     | andHamzaoui, |     | R.  | Featurelearningforhumanactivity |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ------------------------------- | --- | --- | --- | --- |
InternationalConferenceonDataEngineering,pp.554–
565.IEEE,2019. recognitionusingconvolutionalneuralnetworks. CCF
TransactionsonPervasiveComputingandInteraction,2
| Bago,B.,Rand,D.G.,andPennycook,G. |     |     |     |     | Fakenews,fast |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1):18–32,2020.
| and slow: | Deliberation |     | reduces | belief | in false | (but not |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
true)newsheadlines. JournalofExperimentalPsychol- Dodgson,J.E. Reflexivityinqualitativeresearch. Journal
| ogy: General,2020. |     |     |     |     |     |     | ofHumanLactation,35(2):220–222,2019. |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
9

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Donini,M.,Oneto,L.,Ben-David,S.,Shawe-Taylor,J.S., Hao,K.andStray,J. Canyoumakeaifairerthanajudge?
andPontil,M.Empiricalriskminimizationunderfairness play our courtroom algorithm game. MIT Technology
| constraints. | InAdvancesinNeuralInformationProcess- |     |     |     |     | Review,2019. |     |     |     |     |
| ------------ | ------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
ingSystems,pp.2791–2801,2018.
|     |     |     |     |     |     | Hinton,G.E. | Trainingproductsofexpertsbyminimizing |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------------------------------- | --- | --- | --- |
Drosou,M.,Jagadish,H.,Pitoura,E.,andStoyanovich,J. contrastivedivergence. NeuralComputation,14(8):1771–
| Diversityinbigdata: |     | Areview. | BigData,5(2):73–84, |     |     |     |     |     |     |     |
| ------------------- | --- | -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
1800,2002.
2017.
Hohman,F.,Kahng,M.,Pienta,R.,andChau,D.H. Visual
| D’souza,D.,Nussbaum,Z.,Agarwal,C.,andHooker,S. |     |     |     |     | A   |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
analyticsindeeplearning:Aninterrogativesurveyforthe
| taleoftwolongtails. |     | arXivpreprintarXiv:2107.13098, |     |     |     |                |                                    |     |     |     |
| ------------------- | --- | ------------------------------ | --- | --- | --- | -------------- | ---------------------------------- | --- | --- | --- |
|                     |     |                                |     |     |     | nextfrontiers. | IEEETransactionsonVisualizationand |     |     |     |
2021.
|     |     |     |     |     |     | ComputerGraphics(TVCG),2018. |                            |     |     | doi: 10.1109/TVCG. |
| --- | --- | --- | --- | --- | --- | ---------------------------- | -------------------------- | --- | --- | ------------------ |
|     |     |     |     |     |     | 2018.2843369.                | URLhttps://fredhohman.com/ |     |     |                    |
Dwork,C.,Hardt,M.,Pitassi,T.,Reingold,O.,andZemel,
R. Fairnessthroughawareness. InProceedingsofthe3rd visual-analytics-in-deep-learning/.
InnovationsinTheoreticalComputerScienceConference,
Hohman,F.,Conlen,M.,Heer,J.,andChau,D.H.P. Com-
pp.214–226,2012.
|                                                      |     |     |                    |     |     | municating | with interactive |     | articles. | Distill, 5(9):e28, |
| ---------------------------------------------------- | --- | --- | ------------------ | --- | --- | ---------- | ---------------- | --- | --------- | ------------------ |
| Fish,B.andStark,L.Reflexivedesignforfairnessandother |     |     |                    |     |     | 2020a.     |                  |     |           |                    |
| humanvaluesinformalmodels.                           |     |     | InProceedingsofthe |     |     |            |                  |     |           |                    |
Hohman,F.,Wongsuphasawat,K.,Kery,M.B.,andPatel,K.
2021AAAI/ACMConferenceonAI,Ethics,andSociety,
Understandingandvisualizingdataiterationinmachine
pp.89–99,2021.
|     |     |     |     |     |     | learning. | InProceedingsofthe2020CHIConferenceon |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------------------- | --- | --- | --- |
Friedler, S.A., Scheidegger, C., Venkatasubramanian, S., HumanFactorsinComputingSystems,pp.1–13,2020b.
| Choudhary,S.,Hamilton,E.P.,andRoth,D. |     |     |     | Acompara- |     |                                      |     |     |     |               |
| ------------------------------------- | --- | --- | --- | --------- | --- | ------------------------------------ | --- | --- | --- | ------------- |
|                                       |     |     |     |           |     | Holstein,K.,WortmanVaughan,J.,Daume´ |     |     |     | III,H.,Dudik, |
tivestudyoffairness-enhancinginterventionsinmachine
learning. InProceedingsoftheConferenceonFairness, M.,andWallach,H. Improvingfairnessinmachinelearn-
Accountability,andTransparency,pp.329–338,2019. ing systems: What do industry practitioners need? In
Proceedingsofthe2019CHIConferenceonHumanFac-
Gawlikowski,J.,Tassi,C.R.N.,Ali,M.,Lee,J.,Humt,M.,
torsinComputingSystems,pp.1–16,2019.
| Feng,J., | Kruspe,A., | Triebel, | R.,Jung, | P.,Roscher,R., |     |     |     |     |     |     |
| -------- | ---------- | -------- | -------- | -------------- | --- | --- | --- | --- | --- | --- |
etal. Asurveyofuncertaintyindeepneuralnetworks. Hooker, S. Moving beyond “algorithmic bias is a data
arXivpreprintarXiv:2107.03342,2021. Patterns,2(4):100241,2021.
problem”.
Gebru,T.,Morgenstern,J.,Vecchione,B.,Vaughan,J.W.,
|                                    |     |     |     |               |     | Hopkins, | A. and Booth, | S.           | Machine | learning practices    |
| ---------------------------------- | --- | --- | --- | ------------- | --- | -------- | ------------- | ------------ | ------- | --------------------- |
| Wallach,H.,Iii,H.D.,andCrawford,K. |     |     |     | Datasheetsfor |     |          |               |              |         |                       |
|                                    |     |     |     |               |     | outside  | big tech:     | How resource |         | constraints challenge |
datasets. Communications of the ACM, 64(12):86–92, Proceedings of the 2021
|     |     |     |     |     |     | responsible | development. |     | In  |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --- | --- |
2021.
AAAI/ACMConferenceonAI,Ethics,andSociety,AIES
’21,pp.134–145,NewYork,NY,USA,2021.Associa-
| Goel, M., | Jansen, | A., Mandel, | T., Patel, | S. N., and | Wob- |     |     |     |     |     |
| --------- | ------- | ----------- | ---------- | ---------- | ---- | --- | --- | --- | --- | --- |
brock,J.O.Contexttype:Usinghandpostureinformation tionforComputingMachinery. ISBN9781450384735.
|                                      |     |     |     |            |     | doi: 10.1145/3461702.3462527. |     |     | URLhttps://doi. |     |
| ------------------------------------ | --- | --- | --- | ---------- | --- | ----------------------------- | --- | --- | --------------- | --- |
| toimprovemobiletouchscreentextentry. |     |     |     | InProceed- |     |                               |     |     |                 |     |
org/10.1145/3461702.3462527.
| ings of | the SIGCHI | Conference | on  | Human Factors | in  |     |     |     |     |     |
| ------- | ---------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
ComputingSystems,pp.2795–2798,2013.
|     |     |     |     |     |     | Inc., G. | Know your | data, | 2021. | URL https:// |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | ----- | ------------ |
Grout, J., Frederic, J., Corlay, S., and Ragan-Kelley, knowyourdata.withgoogle.com/.
| M.  | Ipywidgets | jupyter | widgets, | 2019. | URL |     |     |     |     |     |
| --- | ---------- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
Japkowicz,N.andStephen,S.Theclassimbalanceproblem:
https://github.com/jupyter-widgets/
ipywidgets. Asystematicstudy. IntelligentDataAnalysis,6(5):429–
449,2002.
| Gullstro¨m,C. | Designfrictions. |     | AI&Society,27(1):91–110, |     |     |           |                      |     |     |                    |
| ------------- | ---------------- | --- | ------------------------ | --- | --- | --------- | -------------------- | --- | --- | ------------------ |
|               |                  |     |                          |     |     | Kale, A., | Kay, M., andHullman, |     | J.  | Decision-makingun- |
2012.
|     |     |     |     |     |     | deruncertaintyinresearchsynthesis: |     |     |     | Designingforthe |
| --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --------------- |
Go¨rtler,J.,Hohman,F.,Moritz,D.,Wongsuphasawat,K.,
|     |     |     |     |     |     | gardenofforkingpaths. |     | InProceedingsofthe2019CHI |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------------------- | --- | --- |
Ren,D.,Nair,R.,Kirchner,M.,andPatel,K. Neo: Gen- ConferenceonHumanFactorsinComputingSystems,pp.
eralizingconfusionmatrixvisualizationtohierarchical
1–14,2019.
| andmulti-outputlabels. |     |     | InProceedingsoftheSIGCHI |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
Conference on Human Factors in Computing Systems. Katz, J. You draw it: Just how bad is the drug overdose
ACM,2022. doi: 10.1145/3491102.3501823. epidemic. TheNewYorkTimes,2017.
10

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Kendall,A.andGal,Y. Whatuncertaintiesdoweneedin Mitchell,M.,Baker,D.,Moorosi,N.,Denton,E.,Hutchin-
bayesiandeeplearningforcomputervision? Advances son,B.,Hanna,A.,Gebru,T.,andMorgenstern,J. Di-
inneuralinformationprocessingsystems,30,2017. versityandinclusionmetricsinsubsetselection. InPro-
ceedingsoftheAAAI/ACMConferenceonAI,Ethics,and
Kim, H. K., Kim, N., and Park, J. Relationship analysis Society,pp.117–123,2020.
betweenbodyflexionanglesandsmartphonetiltduring
|                |     |                                     |     |     |     |     | Mouchet, | M. A., | Ville´ger, | S., | Mason, | N. W., and Mouil- |
| -------------- | --- | ----------------------------------- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | ------ | ----------------- |
| smartphoneuse. |     | InternationalJournalofIndustrialEr- |     |     |     |     |          |        |            |     |        |                   |
gonomics,80:103034,2020. lot, D. Functionaldiversitymeasures: Anoverviewof
theirredundancyandtheirabilitytodiscriminatecommu-
Kim,Y.-S.,Reinecke,K.,andHullman,J. Explainingthe nityassemblyrules. FunctionalEcology,24(4):867–876,
| gap: Visualizingone’spredictionsimprovesrecalland |     |     |                           |     |     |     | 2010.       |                  |     |     |                        |     |
| ------------------------------------------------- | --- | --- | ------------------------- | --- | --- | --- | ----------- | ---------------- | --- | --- | ---------------------- | --- |
| comprehensionofdata.                              |     |     | InProceedingsofthe2017CHI |     |     |     |             |                  |     |     |                        |     |
|                                                   |     |     |                           |     |     |     | Murphy,K.P. | Machinelearning: |     |     | Aprobabilisticperspec- |     |
ConferenceonHumanFactorsinComputingSystems,pp.
tive. MITpress,2012.
1375–1386,2017.
|              |                                       |     |              |     |         |         | Noble,S.U.       | Algorithmsofoppression:Howsearchengines |                |     |     |     |
| ------------ | ------------------------------------- | --- | ------------ | --- | ------- | ------- | ---------------- | --------------------------------------- | -------------- | --- | --- | --- |
| Kim, Y.-S.,  | Reinecke,                             | K., | and Hullman, |     | J. Data | through |                  |                                         |                |     |     |     |
|              |                                       |     |              |     |         |         | reinforceracism. |                                         | NYUPress,2018. |     |     |     |
| others’eyes: | Theimpactofvisualizingothers’expecta- |     |              |     |         |         |                  |                                         |                |     |     |     |
tionsonvisualizationinterpretation. IEEETransactions Noroozi,F.,Kaminska,D.,Corneanu,C.,Sapinski,T.,Es-
onVisualizationandComputerGraphics,24(1):760–769, calera,S.,andAnbarjafari,G. Surveyonemotionalbody
gesturerecognition.IEEETransactionsonAffectiveCom-
| 2018. | doi: 10.1109/TVCG.2017.2745240. |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
puting,2018.
| Klawonn,M.,Heim,E.,andHendler,J. |     |     |     |     | Exploitingclass |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Olah,C.,Satyanarayan,A.,Johnson,I.,Carter,S.,Schubert,
| learnability | in noisy | data.      | In            | Proceedings | of     | the AAAI |                            |     |                        |     |                     |     |
| ------------ | -------- | ---------- | ------------- | ----------- | ------ | -------- | -------------------------- | --- | ---------------------- | --- | ------------------- | --- |
|              |          |            |               |             |        |          | L.,Ye,K.,andMordvintsev,A. |     |                        |     | Thebuildingblocksof |     |
| Conference   | on       | Artificial | Intelligence, |             | volume | 33, pp.  |                            |     |                        |     |                     |     |
|              |          |            |               |             |        |          | interpretability.          |     | Distill,3(3):e10,2018. |     |                     |     |
4082–4089,2019.
Palanica,A.,Thommandram,A.,Lee,A.,Li,M.,andFossat,
| Koesten, | L., Kacprzak, | E., | Tennison, | J., | and Simperl, | E.  |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Y. Doyouunderstandthewordsthatarecominouttamy
Collaborative practices with structured data: Do tools mouth? voice assistant comprehension of medication
| supportwhatusersneed? |     |     | InProceedingsofthe2019CHI |     |     |     |        |                                   |     |     |     |     |
| --------------------- | --- | --- | ------------------------- | --- | --- | --- | ------ | --------------------------------- | --- | --- | --- | --- |
|                       |     |     |                           |     |     |     | names. | NPJDigitalMedicine,2(1):1–6,2019. |     |     |     |     |
ConferenceonHumanFactorsinComputingSystems,pp.
1–14,2019. Papadopoulos,A.,Kyritsis,K.,Klingelhoefer,L.,Bostan-
jopoulou,S.,Chaudhuri,K.R.,andDelopoulos,A. De-
| Lee, K., | Lee, K., | Lee, H., | and Shin, | J. A | simple | unified |     |     |     |     |     |     |
| -------- | -------- | -------- | --------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- |
tectingparkinsoniantremorfromimudatacollectedin-
frameworkfordetectingout-of-distributionsamplesand the-wild using deep multiple-instance learning. IEEE
adversarialattacks. Advancesinneuralinformationpro- Journal of Biomedical and Health Informatics, 24(9):
cessingsystems,31,2018. 2559–2569,2020. doi: 10.1109/JBHI.2019.2961748.
Lee, S., Lee, H., Lee, J., Ryu, H., Kim, I.Y., andKim, J. Pennycook,G.andRand,D.G. Lazy,notbiased: Suscepti-
bilitytopartisanfakenewsisbetterexplainedbylackof
Clip-onimusystemforassessingage-relatedchangesin
handfunctions. Sensors,20(21):6313,2020. reasoningthanbymotivatedreasoning. Cognition,188:
39–50,2019.
| MacKenzie, | I. S. | and Soukoreff,    |     | R. W.     | Phrase | sets for |            |     |                                        |     |        |                    |
| ---------- | ----- | ----------------- | --- | --------- | ------ | -------- | ---------- | --- | -------------------------------------- | --- | ------ | ------------------ |
|            |       |                   |     |           |        |          | Pennycook, | G., | McPhetres,                             | J., | Zhang, | Y., Lu, J. G., and |
| evaluating | text  | entry techniques. |     | In CHI’03 |        | Extended |            |     |                                        |     |        |                    |
|            |       |                   |     |           |        |          | Rand,D.G.  |     | Fightingcovid-19misinformationonsocial |     |        |                    |
AbstractsonHumanFactorsinComputingSystems,pp.
|     |     |     |     |     |     |     | media: | Experimentalevidenceforascalableaccuracy- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------------------------- | --- | --- | --- | --- |
754–755,2003.
|            |            |      |             |              |              |       | nudgeintervention. |        |     | PsychologicalScience,31(7):770– |        |                 |
| ---------- | ---------- | ---- | ----------- | ------------ | ------------ | ----- | ------------------ | ------ | --- | ------------------------------- | ------ | --------------- |
| Milani,    | M., Huang, | Y.,  | and Chiang, | F.           | Diversifying |       | 780,2020.          |        |     |                                 |        |                 |
| anonymized | data       | with | diversity   | constraints. |              | arXiv |                    |        |     |                                 |        |                 |
|            |            |      |             |              |              |       | Pleiss, G.,        | Zhang, | T., | Elenberg,                       | E. R., | and Weinberger, |
preprintarXiv:2007.09141,2020.
K.Q. Identifyingmislabeleddatausingtheareaunder
|     |     |     |     |     |     |     | the margin | ranking. |     | arXiv | preprint | arXiv:2001.10528, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ----- | -------- | ----------------- |
Mitchell,M.,Wu,S.,Zaldivar,A.,Barnes,P.,Vasserman,
2020.
| L., Hutchinson, |     | B., Spitzer, | E., | Raji, I. | D., and | Gebru, |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
T. Modelcardsformodelreporting. InProceedingsof Quionero-Candela,J.,Sugiyama,M.,Schwaighofer,A.,and
theConferenceonFairness,Accountability,andTrans- Lawrence,N.D. Datasetshiftinmachinelearning. The
| parency,pp.220–229,2019. |     |     |     |     |     |     | MITPress,2009. |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
11

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Ramasamy Ramamurthy, S. and Roy, N. Recent trends VanCalster,B.,McLernon,D.J.,VanSmeden,M.,Wynants,
inmachinelearningforhumanactivityrecognition—a L.,andSteyerberg,E.W. Calibration: theachillesheel
survey. Wiley Interdisciplinary Reviews: Data Mining ofpredictiveanalytics. BMCmedicine,17(1):1–7,2019.
andKnowledgeDiscovery,8(4):e1254,2018.
|     |     |     |     |     |     |     | VanderPlas, | J., | Granger, | B., Heer, | J., Moritz, | D., | Wong- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --------- | ----------- | --- | ----- |
Rosenfeld, E., Ravikumar, P., and Risteski, A. The suphasawat,K.,Satyanarayan,A.,Lees,E.,Timofeev,I.,
risks of invariant risk minimization. arXiv preprint Welsh,B.,andSievert,S. Altair: Interactivestatistical
arXiv:2010.05761,2020.
|         |          |        |            |     |            |           | visualizationsforpython. |     |     | JournalofOpenSourceSoft-  |     |     |     |
| ------- | -------- | ------ | ---------- | --- | ---------- | --------- | ------------------------ | --- | --- | ------------------------- | --- | --- | --- |
|         |          |        |            |     |            |           | ware,3(32):1057,2018.    |     |     | doi: 10.21105/joss.01057. |     |     | URL |
| Sagawa, | S., Koh, | P. W., | Hashimoto, |     | T. B., and | Liang, P. |                          |     |     |                           |     |     |     |
https://doi.org/10.21105/joss.01057.
Distributionallyrobustneuralnetworksforgroupshifts:
Ontheimportanceofregularizationforworst-casegener-
Wexler,J.,Pushkarna,M.,Bolukbasi,T.,Wattenberg,M.,
| alization. | arXivpreprintarXiv:1911.08731,2019. |     |     |     |     |     |                                 |     |     |                 |              |             |     |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --------------- | ------------ | ----------- | --- |
|            |                                     |     |     |     |     |     | Viegas,F.,andWilson,J.          |     |     | TheWhat-IfTool: |              | Interactive |     |
|            |                                     |     |     |     |     |     | ProbingofMachineLearningModels. |     |     |                 | IEEETVCG,26, |             |     |
Samadi,S.,Tantipongpipat,U.,Morgenstern,J.H.,Singh,
|                  |                                         |     |                    |     |             |     | 2019.      | doi: 10.1109/tvcg.2019.2934619. |           |                 |     |     |         |
| ---------------- | --------------------------------------- | --- | ------------------ | --- | ----------- | --- | ---------- | ------------------------------- | --------- | --------------- | --- | --- | ------- |
| M.,andVempala,S. |                                         |     | Thepriceoffairpca: |     | Oneextradi- |     |            |                                 |           |                 |     |     |         |
| mension.         | InAdvancesinNeuralInformationProcessing |     |                    |     |             |     |            |                                 |           |                 |     |     |         |
|                  |                                         |     |                    |     |             |     | Whittaker, | R. H.                           | Evolution | and measurement |     | of  | species |
Systems,pp.10976–10987,2018.
|     |     |     |     |     |     |     | diversity. | Taxon,21(2-3):213–251,1972. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------------- | --- | --- | --- | --- | --- |
Sambasivan,N.,Kapania,S.,Highfill,H.,Akrong,D.,Par-
|                |        |            |          |              |               |       | Wieringa,       | M. What                                  | to                               | account for | when | accounting | for |
| -------------- | ------ | ---------- | -------- | ------------ | ------------- | ----- | --------------- | ---------------------------------------- | -------------------------------- | ----------- | ---- | ---------- | --- |
| itosh,         | P. K., | and Aroyo, | L.       | M. ”everyone | wants         | to do |                 |                                          |                                  |             |      |            |     |
|                |        |            |          |              |               |       | algorithms:     | Asystematicliteraturereviewonalgorithmic |                                  |             |      |            |     |
| the model      | work,  | not        | the data | work”:       | Data cascades | in    |                 |                                          |                                  |             |      |            |     |
|                |        |            |          |              |               |       | accountability. |                                          | InProceedingsofthe2020Conference |             |      |            |     |
| high-stakesai. |        | 2021.      |          |              |               |       |                 |                                          |                                  |             |      |            |     |
onFairness,Accountability,andTransparency,pp.1–18,
| Saul, J. | Scepticism | and | implicit | bias. | Disputatio, | 5(37): | 2020. |     |     |     |     |     |     |
| -------- | ---------- | --- | -------- | ----- | ----------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
243–263,2013.
|     |     |     |     |     |     |     | Wkeglarczyk,S. |     | Kerneldensityestimationanditsapplica- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------------------------- | --- | --- | --- | --- |
Schapire,R.E. Thestrengthofweaklearnability. Machine tion. InITMWebofConferences,volume23,pp.00037.
| Learning,5(2):197–227,1990. |                |     |     |          |             |         | EDPSciences,2018. |         |     |              |       |         |      |
| --------------------------- | -------------- | --- | --- | -------- | ----------- | ------- | ----------------- | ------- | --- | ------------ | ----- | ------- | ---- |
| Schmidt,                    | L., Santurkar, |     | S., | Tsipras, | D., Talwar, | K., and |                   |         |     |              |       |         |      |
|                             |                |     |     |          |             |         | Yang, K.,         | Qinami, | K., | Fei-Fei, L., | Deng, | J., and | Rus- |
Madry,A. Adversariallyrobustgeneralizationrequires sakovsky, O. Towards fairer datasets: Filtering and
moredata.InAdvancesinNeuralInformationProcessing
|     |     |     |     |     |     |     | balancing | the | distribution | of the | people | subtree | in the |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | ------ | ------ | ------- | ------ |
Systems,pp.5014–5026,2018.
|     |     |     |     |     |     |     | imagenethierarchy. |     | InProceedingsofthe2020Confer- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------------------- | --- | --- | --- | --- |
enceonFairness,Accountability,andTransparency,pp.
Sculley,D.,Holt,G.,Golovin,D.,Davydov,E.,Phillips,T.,
547–558,2020.
Ebner,D.,Chaudhary,V.,Young,M.,Crespo,J.-F.,and
| Dennison,D. |                                         | Hiddentechnicaldebtinmachinelearning |     |     |     |     |                                      |     |     |     |                       |           |     |
| ----------- | --------------------------------------- | ------------------------------------ | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --------------------- | --------- | --- |
|             |                                         |                                      |     |     |     |     | Zheng,W.,Wang,X.,Fang,H.,andCheng,H. |     |     |     |                       | Coverage- |     |
| systems.    | InAdvancesinNeuralInformationProcessing |                                      |     |     |     |     |                                      |     |     |     |                       |           |     |
|             |                                         |                                      |     |     |     |     | basedsearchresultdiversification.    |     |     |     | InformationRetrieval, |           |     |
Systems,pp.2503–2511,2015.
15(5):433–457,2012.
| Shen, Y.                                 | and Sanghavi, |     | S.  | Learning | with bad | training   |                        |                                           |     |                                |     |     |     |
| ---------------------------------------- | ------------- | --- | --- | -------- | -------- | ---------- | ---------------------- | ----------------------------------------- | --- | ------------------------------ | --- | --- | --- |
|                                          |               |     |     |          |          |            | Zobay, O.              | VariationalBayesianinferencewithGaussian- |     |                                |     |     |     |
| dataviaiterativetrimmedlossminimization. |               |     |     |          |          | InInterna- |                        |                                           |     |                                |     |     |     |
|                                          |               |     |     |          |          |            | mixtureapproximations. |                                           |     | ElectronicJournalofStatistics, |     |     |     |
tionalConferenceonMachineLearning,pp.5739–5748.
8(1):355–389,2014.
PMLR,2019.
| Soedirgo,J.andGlas,A.                           |     |     | Towardactivereflexivity: |     |     | Posi- |                  |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | ------------------------ | --- | --- | ----- | ---------------- | --- | --- | --- | --- | --- | --- |
| tionalityandpracticeintheproductionofknowledge. |     |     |                          |     |     | PS:   | A.DataCollection |     |     |     |     |     |     |
PoliticalScience&Politics,53(3):527–531,2020.
WebuiltacustomiOSdatacollectionappusingtheSwift
Stray,J.andHao,K. Interactivevisualizationoffairness programminglanguagewithpublicframeworksincluding
| tradeoffs. | Computation+JournalismSymposium,2020. |     |     |     |     |     |                                     |     |     |     |     |            |     |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ---------- | --- |
|            |                                       |     |     |     |     |     | SwiftUI,CommonCrypto,andCoreMotion. |     |     |     |     | Theappcol- |     |
lectsrightandleft-handedtextingdataacrossdifferentcon-
| Tayi,G.K.andBallou,D.P. |     |     |     | Examiningdataquality. |     | Com- |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
textspeoplemaytypein,suchastextingwhilewalkingor
municationsoftheACM,41(2):54–57,1998.
|     |     |     |     |     |     |     | layingdown. | ExampleviewsoftheappareshowninFig- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | --- |
Toplak,M.E.,West,R.F.,andStanovich,K.E. Thecog- ure5. Alldatawerecollectedwithinformedconsent. Dur-
nitive reflection test as a predictor of performance on ing collection, participants were given instructed how to
heuristics-and-biasestasks. Memory&Cognition,39(7): handposturewhenholdingthephone. Whilethisapproach
1275,2011. producesconsistentdatafortrainingpurposes,thislimited
12

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
theinherentvariabilitywithinthedata. Wesimplifiedthe thenaskedtoenterexpecteddimensionsanddistributions
tasktobinaryhandedness(typingwiththeleftorrighthand), ofdatabeforecollectingdata(MainBodyFigure2B,C).
butintroducedasourceofnaturalvariabilitybyprompting Whendistributionshaveincorrectvalues(i.e.,donotadd
userstoperformaseriesofactionsinparallelwhiletyping. upto100%),thedashboardnormalizes. Thisactiveexpres-
Thiscontrasts (Goeletal.,2013),whocollecteddatawhile sionofexpecteddataencouragesuserstoacknowledgeand
userssatinalabenvironment. Weintroduced6typingsce- document the specific limitations of their data, setting a
narios(walking,sitting,standing,lyingonyourback,lying precedentofconsciousdecisionmakingfromthebeginning.
onyourside,andlyingonyourfront)torepresentaselection Itcreatesasimpleprovenanceforearlyassumptionsanda
ofpossiblecontextsusersmightnormallyexperiencetyp- baselinetoevaluateagainstduringdatacollection.
ing. ParticipantswerethenaskedtotypeanEnglishphrase
Fromtheseinputteddimensions,auditsofpopulationstatis-
fromMacKenzieandSoukoreff’sphraseset(MacKenzie
tics,missingdata,andundersampledsubsetsarepresented
&Soukoreff,2003)usingtheirleftorrighthandforato-
|     |     |     |     | tousers,reflectingDuringCollection. |     |     | Newdimensionscan |     |
| --- | --- | --- | --- | ----------------------------------- | --- | --- | ---------------- | --- |
talof6(positions)×4(typingsessions)×2(hands)=72
|                 |         |               |                      | beaddedasneeded. | Differentcategoriesofthedata,includ- |     |     |     |
| --------------- | ------- | ------------- | -------------------- | ---------------- | ------------------------------------ | --- | --- | --- |
| trials. Entered | phrases | were recorded | as a trial. Partici- |                  |                                      |     |     |     |
ingdemographicinformationandmetadata(describedinthe
| pants were | automatically | redirected | to the iOS Measure |     |     |     |     |     |
| ---------- | ------------- | ---------- | ------------------ | --- | --- | --- | --- | --- |
participantsubsection),taskspecifics,andclassrepresen-
| app to determine                    | hand | and nail length. | The app disabled |                                            |            |              |          |            |
| ----------------------------------- | ---- | ---------------- | ---------------- | ------------------------------------------ | ---------- | ------------ | -------- | ---------- |
|                                     |      |                  |                  | tationarethenshowninvisualizationsFigure2. |            |              |          | Similarly, |
| keyboardautocompleteandautocorrect. |      |                  | Beginningwhen    |                                            |            |              |          |            |
|                                     |      |                  |                  | intersectional                             | categories | (such as age | and hand | size) are  |
peoplepressed“start”,wecollecteddatawascollectedat
shown. Thisviewreflectsthedataevolutionasmoredata
| a sampling | rate of 200 | Hz. When | the task was finished, |     |     |     |     |     |
| ---------- | ----------- | -------- | ---------------------- | --- | --- | --- | --- | --- |
iscollected,allowingreal-timeinsightintowhatadditional
metadata,IMUdata,andtrialmetadata(includingscenario,
|     |     |     |     | collectionmightberequired. |     | Followingcollection,thedash- |     |     |
| --- | --- | --- | --- | -------------------------- | --- | ---------------------------- | --- | --- |
phrase,keyboardrecording,andsessiontime)werepushed
boardallowsuserstouseapre-trainedmodelortraintheir
toanencrypteddatabase.
own. Followingtraining,savedstatesofaneuralnetwork
andmodelarchitectureareloadedintoourfamiliarityfunc-
B.Dashboard&Questions
|     |     |     |     | tions. Dataisinputtedtobuildoutfamiliarityscores, |     |     |     | the |
| --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- |
finalstepinourdesigningdataprocess.
| We built | our dashboard | in JupyterLab | using Altair (Van- |     |     |     |     |     |
| -------- | ------------- | ------------- | ------------------ | --- | --- | --- | --- | --- |
derPlasetal.,2018),adeclarativevisualizationlibraryfor
B.1.VisualExaminationofFamiliarity
| Python,andIpywidgets(Groutetal.,2019). |     |     | Asshownin |     |     |     |     |     |
| -------------------------------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
MainBodyFigure2(A),thedashboardasksaseriesofques- Log-likelihoodisarelativemeasure. Givenourinterestin
tionstopromptreflexiveconsiderationfortheteamorindi-
thespreadoffamiliarityscoresacrossdifferentcategories
vidualspersonalbiases. Usingdrop-downselections,they withinthedataset,weintroducedthevisualizationsshown
are asked to describe their team’s representational make- in Figure 8 and Figure 9 into the dashboard for quick
up—includingrace,accessibilityneeds,age,sexandgender
insightintoifthereareparticularsubsetsthatareseemless
identities. Afterfillingoutthisinformation,usersaretold: familiarthanothers. Anoverviewofthefamiliarityscores
“Thefollowinggroupsandtheirsubsequentintersectionsare
|     |     |     |     | can be seen | in Figure | 6 For example, | with | a close look |
| --- | --- | --- | --- | ----------- | --------- | -------------- | ---- | ------------ |
not participating in your project development. To ensure we see that the least familiar samples across genders are
anoptimalresult,takestepstoconsiderhowtheirexperi- consistentlyfemale. Similarly,weseeouroldestage-range
encesandviewsmightdifferfromthecurrentlyrepresented
|     |     |     |     | (¿56)isleastfamiliarforage. |     | Thisviewcanbecompared |     |     |
| --- | --- | --- | --- | --------------------------- | --- | --------------------- | --- | --- |
ones.” This notice is followed by a list of demographic acrossiterationsofdataormodeldevelopmentforagestalt
informationnotidentifiedbytheusers. Thisisanimportant ofthechangesinfamiliarity.
step: priorworkhasshownthatsimplyrecognizingsuch
| information | (Fish & Stark, | 2021; Kim | et al., 2017), and |              |                     |     |     |     |
| ----------- | -------------- | --------- | ------------------ | ------------ | ------------------- | --- | --- | --- |
|             |                |           |                    | C.CaseStudy: | ReflectingonOurData |     |     |     |
introducingdesignfrictions(Gullstro¨m,2012;Pennycook
CollectionProcess
etal.,2020),canincreasethequalityandconsiderationthat
goesintodatawork.
|     |     |     |     | It was unclear          | how | diverse IMU                | data would | influence |
| --- | --- | --- | --- | ----------------------- | --- | -------------------------- | ---------- | --------- |
|     |     |     |     | ourmodelingexperiments, |     | orifthecategoriesdeveloped |            |           |
Onelimitationtothisproceduralapproachishowscoped
ourquestionsare—theyarenotall-encompassing, butin- through our reflexive prompts would meaningfully align
tended to start the process of reflection and inquiry early withvariationwithinthedata. Priorworkonhumanges-
|     |     |     |     | tureshasshownage |     | (Leeetal.,2020),emotion |     | (Noroozi |
| --- | --- | --- | --- | ---------------- | --- | ----------------------- | --- | -------- |
on. Asafinalstepinthisreflexiveprocess,andtominimize
thislimitation,aseriesofopen-endedquestionsthattake etal.,2018),andhealth(Papadopoulosetal.,2020)influ-
|     |     |     |     | encegesturepresentation. |     | Thetiltofasmartphoneduring |     |     |
| --- | --- | --- | --- | ------------------------ | --- | -------------------------- | --- | --- |
infree-formtextasks,“What’smissing,inthecontextof
yourproject?” followedbysomeexamplesthatexpandon textingiscapturedbyIMUdata,andcanbeassociatedto
axesofdiversityteamsmightneedtoconsider. Usersare backposture(Kimetal.,2020). Handpositionduringtyp-
ingissimilarlydistinguishable(Goeletal.,2013),yetIMU
13

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Figure5. OurIMUDataCollectionAppshowingtheprimaryscreensofthestudy.Participantsenteredtheirdemographicinformation
suchashanddominance,handandnaillength,sexandgender,andage(left).Theappinstructsaparticipanttotypeontheirphoneusing
eithertheirrightorlefthandinaphysicalconfiguration(middle).Participantsthentypethepresentedphrase(right).
aroleinhowpeopletext,despitenotbeingvariablestyp-
|     |     |     |     |     |     | ically considered |     | in such | tasks. | It was also | through | this |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ------ | ----------- | ------- | ---- |
processofreflectingonimpactfulfeaturesthatwerealized
theadvantagesofaskingparticipantstoactoutvariousbe-
|     |     |     |     |     |     | haviorsduringtheirtypingtasks.                    |            |                                |             | Thismeaningfullyshaped |       |          |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | ---------- | ------------------------------ | ----------- | ---------------------- | ----- | -------- |
|     |     |     |     |     |     | ourtask. Othermeasurementsthatwerenotedduringthis |            |                                |             |                        |       |          |
|     |     |     |     |     |     | process would                                     | have       | added                          | substantial | complexity             |       | to our   |
|     |     |     |     |     |     | collection                                        | procedure. | Most                           | prominent   | of                     | these | was hand |
|     |     |     |     |     |     | strengthanddexterity.                             |            | Thesefeaturesareimpactfultohow |             |                        |       |          |
Figure6. Overviewoffamiliarityoverthetwotailendsofthe
|     |     |     |     |     |     | individuals | type—a | person | with | carpel tunnel | or  | arthritis |
| --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | ---- | ------------- | --- | --------- |
distribution(mostfamiliarontheright,leastfamiliarontheleft).
|     |     |     |     |     |     | will type                                             | differently | compared |            | to someone | without       | these |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | ----------- | -------- | ---------- | ---------- | ------------- | ----- |
|     |     |     |     |     |     | conditions—but                                        |             | required | additional | tooling    | to accurately |       |
|     |     |     |     |     |     | capture. Instead,wenotedstrengthanddexterityforfuture |             |          |            |            |               |       |
datacollectionrarelyincludesmetainformationaboutpar- evaluation,tobecompletedpriortopublicdeployment.
| ticipants. Similarly, | context | is often | not documented |     | for |     |     |     |     |     |     |     |
| --------------------- | ------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TheresultsofCollectionMonitoringledtothreeinstances
| imagedata(e.g. | theproverbialquestionofwhat’soutside |     |     |     |     |                |            |     |      |            |         |          |
| -------------- | ------------------------------------ | --- | --- | --- | --- | -------------- | ---------- | --- | ---- | ---------- | ------- | -------- |
|                |                                      |     |     |     |     | of additional, | retargeted |     | data | collection | efforts | based on |
theframe?).
|     |     |     |     |     |     | unexpectedskew. |     | Duringourinitialdatacollection,there |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------------------------------------ | --- | --- | --- | --- |
We explored how these and other common demographic weremultiplecategorieswhichdidnotmatchourpreviously
| categories influenced | model | performance |     | and show | how |                         |     |     |                    |     |            |     |
| --------------------- | ----- | ----------- | --- | -------- | --- | ----------------------- | --- | --- | ------------------ | --- | ---------- | --- |
|                       |       |             |     |          |     | describeddistributions. |     |     | Wecalloutseveralin |     | Figure10to |     |
considerationfordiversedatashouldbeemphasizedprior
demonstratetheoutcomesofourdatacollectionre-targeting.
todeployment,notjustafterdeployment. Weincorporated While all participants were employees from a large tech
ourdashboard’sPre-Collectionsuiteofpromptsinourown
|     |     |     |     |     |     | company, | we did | not anticipate |     | our initial | wave | of data |
| --- | --- | --- | --- | --- | --- | -------- | ------ | -------------- | --- | ----------- | ---- | ------- |
IMUdatacollectiontodeterminewhatcharacteristicstocol-
collectiontobesoskewedtowardsindividualsbetweenthe
lectfor.Itwasthroughthesepromptsthatwerealizedaneed agesof21and40. Intruth,weinitiallyhadnoparticipants
tomeasureadditionalinformationastypicaldemographics
|     |     |     |     |     |     | over38. Asaresult,weemphasizeddiversityinparticipant |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
didnotcapturehowpeopleheldtheirphones. Wenotedthat agemovingforwardwithsomesuccess—eachconsecutive
| Phone Size, | Hand Size, | Handedness, |     | and | Nail |                              |     |     |     |                         |     |     |
| ----------- | ---------- | ----------- | --- | --- | ---- | ---------------------------- | --- | --- | --- | ----------------------- | --- | --- |
|             |            |             |     |     |      | waveimprovedthedatacoverage. |     |     |     | Familiarityalsodirected |     |     |
Length(particularlyinthecaseofacrylicnails)mayplay
14

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Collect more data
Adjust

parameters
Typical

|     |     | 1   | 2   | 3   | 4   | 5   | 6   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Development
|     |     | Data collection &  | Build
 | Train &
 Compare treatment
 |     | Set prediction  | Deploy  |     |
| --- | --- | ------------------ | ------- | ---------------------------- | --- | --------------- | ------- | --- |
|     |     | pre-processing     | models  | evaluate across groups
      |     | thresholds      | model   |     |
Designing

Collect more data
Data
Adjust

parameters
| Reflexivity |     | 1 Tracking | 2   | 3   | 4   | Familiarity | 5   | 6   |
| ----------- | --- | ---------- | --- | --- | --- | ----------- | --- | --- |
Data collection &
|     |                |     | Build
 | Train &
 Compare treatment
 |     |     | Set prediction  | Deploy  |
| --- | -------------- | --- | ------- | ---------------------------- | --- | --- | --------------- | ------- |
|     | pre-processing |     |         |                              |     |     |                 | model   |
|     |                |     | models  | evaluate across groups
      |     |     | thresholds      |         |
Figure7.Designingdataprocesscomparedtoconventionalmachinelearningdevelopment.Reflexivityensuresappropriateconsideration
ofpositionalityandexpectationsisgivenbeforepriortocollection.Monitoringprovidesinsightintounexpectedtrendsduringcollection.
Familiarityfacilitatesdebuggingandhighlightspotentiallynoisyorunderrepresentedsubpopulationstodirectiteration. Thisfigure
representsasimplificationofthedatacollectionprocess.TheresultsofFamiliaritycanalsobeincorporatedintotraining(aftercleaning
thedataset)andtracking(aftertraininganinitialmodel).
our collection efforts, leading us to seek additional data nitionChain,whichincludespre-processing,segmentation,
for an intersectional subset of Female participants with featureextraction,andclassificationsteps(Crucianietal.,
LargephonesandSmallhands. 2020)forourapproachtomodeling. Weused1Dconvolu-
|     |     |     |     | tionalneuralnets(CNNs)forsequenceclassification. |     |     |     | The |
| --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
C.1.CollectionRetargeting CNN’sarchitectureperformsfeatureextractionthroughthe
|            |          |                   |                     | convolutionoftheinputsignalwithakernel(orfilter). |     |     |     | To  |
| ---------- | -------- | ----------------- | ------------------- | ------------------------------------------------- | --- | --- | --- | --- |
| Similarly, | we noted | that the majority | of our participants |                                                   |     |     |     |     |
pre-processdata,eachsessionwassegmentedinto200ms
self-describedasWhite,butthattherewerenoBlackorIn-
|                                 |     |                         |     | windows,with40msoverlapbetweensegments. |     |     |     | Session |
| ------------------------------- | --- | ----------------------- | --- | --------------------------------------- | --- | --- | --- | ------- |
| digenousparticipantswhatsoever. |     | Despiteourbestattempts, |     |                                         |     |     |     |         |
timingvariedbyhowlongittookparticipantstofinishtyp-
thiswasonlypartiallyamended;inoptimizingacrossinter-
ingagivenphrase.WecorrectedourIMUdatasettoaccount
sectionalgroups,wewerenotabletoperfectlymatchour forgravitationalaccelerationeffects,thennormalized(using
expectedorupdateddistributions(atleastwithinthecontext
adirectcurrentblocker)andsegmentedIMUdatainseries
| ofthissetofiterations). |     | Incontrast,ourinitiallycollected |     |                                      |     |     |             |     |
| ----------------------- | --- | -------------------------------- | --- | ------------------------------------ | --- | --- | ----------- | --- |
|                         |     |                                  |     | toensureallwindowswereofequallength. |     |     | Wediscarded |     |
Handednessdistributionperfectlymatchedourexpectations.
|     |     |     |     | windowscontainingdatafrommultiplesessions. |     |     |     | Fortrain- |
| --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --------- |
Thispromptedadiscussionofwhetherthisdistributionwas
ing,onesampleequatedtoawindowofthetimeseriesdata.
reasonable—despitematchingtheratioofleftversusright
Trainingbatchsizeswere256(batch)×200(ms)×3(IMU),
handednessinUSpopulations,webelievedthatrightand
wheremsisthewindowoftime,batchisthebatchsize,and
lefthandedindividualswouldtypeindramaticallydifferent
|     |     |     |     | IMUrepresentsthethreeaccelerometerdatasources. |     |     |     | All |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
ways,thusmayrequiresamplesizeparitytobeappropri- computationswererunonNVIDIAV100GPUs. Training
| ately learned | by the | model. Examples | of our retargeting |     |     |     |     |     |
| ------------- | ------ | --------------- | ------------------ | --- | --- | --- | --- | --- |
allmodelstookapproximately30hours.
| effortscanbeseenin |     | Figure10. |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
E.Experiments
D.Modeling
E.1.DiverseDataExperimentalProtocol
| Using Keras, | our architecture | included | two 1D convolu- |     |     |     |     |     |
| ------------ | ---------------- | -------- | --------------- | --- | --- | --- | --- | --- |
tionallayers(standardfortimeseriesdata), max-pooling Wesaveeverymodel,theirweights,trainingaccuracyand
layers,adropoutlayer,afullyconnecteddenselayerwith loss curves, and training dataset, keeping track of model
ReLu activations, and a fully connected dense layer with version. Notethateachmodelwastrained10x10times,
keepingtherandomseedstableforrtimes,thenrepeating
softmaxactivations.WefollowedthegenericActivityRecog-
15

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Figure8. Visualpresentingfamiliaritydistributionsacrossdiffer-
entcategories(part1). Figure9. Visualpresentingfamiliaritydistributionsacrossdiffer-
entcategories(part2).
16

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Iterative Data Collection
First Wave Second Wave Third Wave
AGE
HANDEDNESS
RACE
SCENE
Figure10. Selectedviewsofdatadistributionsacrossthreedifferentwavesofdatacollection. Eachnewiterationofdatacollection
wastheresultofevolvingunderstandingaboutthedata.ForAge,initiallytherewerenoparticipantsovertheageof38.Handedness
initiallymetexpecteddistributions,howeverthesedidnotmatchdownstreamneeds. InRace,therewassubstantialskewforWhite
participants.Anerrorindatacollectionledtoaskewinwhichsceneswerepresentedtoparticipants.
17

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
|     | Intersectional Group Accuracies
 |     |     | Intersectional Group Accuracies
 |     |     |     |
| --- | -------------------------------- | --- | --- | -------------------------------- | --- | --- | --- |
|     | A                                |     |     | B                                |     |     |     |
|     | of X_test on max                 |     |     | of X_test on diverse_data_scene  |     |     |     |
Figure11.Comparisonofintersectionalgroupsofalessdiversemodel(A)toadiversemodel(B).Striatedaccuracyacrosspopulations—
asdescribedbythemetadatadescriptions—performedworsewhengroupswereleftout,indicatingthatthesecharacteristicswerealigned
withmeaningfuldiversityinthedata.
withadifferentseed. Weightsfromthemodelswithhighest E.2.FamiliarityExperiments: CapturingNoisyData
accuracyacrossthetrialswerekeptforlaterexperiments.
|     |     |     |     | Different layers | of an NN capture | distinct features | of the |
| --- | --- | --- | --- | ---------------- | ---------------- | ----------------- | ------ |
First, shuffle then randomly select train and test datasets inputdata(Olahetal.,2018). Familiarityscorescanthere-
| suchthatnotypingtrialsaresplitacrossdatasets. |     |     | Wesave |                   |                 |                |         |
| --------------------------------------------- | --- | --- | ------ | ----------------- | --------------- | -------------- | ------- |
|                                               |     |     |        | fore be extracted | from any layer. | Earlier layers | capture |
the test dataset to evaluate every model trained with the fundamentalstructurefoundintheinputdata,whiledeeper
currenttrain/testsplit. Then,wecomparethefulldataset layerscapturesemanticcontent. Forthisreason,wefocus
andtrain/testdistributionsusingavisualcheckandearth onthefinaldenselayer,whichholdstheclosestsemantic
mover’sdistance(EMD).Ifthedifferenceindistributions alignmenttohumanperception. Avisualoverviewofthe
| aresignificant,repeatthefirststep. |           | Wegroupthedataby        |       |                                      |     |           |     |
| ---------------------------------- | --------- | ----------------------- | ----- | ------------------------------------ | --- | --------- | --- |
|                                    |           |                         |       | familiarityimplementationcanbeseenin |     | Figure13. |     |
| category (e.g.,                    | Sex) then | by type (e.g., Female). | Next, |                                      |     |           |     |
Ingeneral,anyDEtechniquecanreplaceourimplementa-
randomlydownsampleeachgroupsuchthateachsubsetis
tion. Notethatthesamedatashowntoadifferentmodelis
| ofequalsize. | Wecomparethedistributionofdatasampled |     |     |     |     |     |     |
| ------------ | ------------------------------------- | --- | --- | --- | --- | --- | --- |
likelytoobtainadifferentfamiliarityscore;eachsampleis
outtothedownsampledgroupdata,repeatingsamplingin
|                                          |     |     |           | tightlycoupledtohowaspecificmodelperceivesit. |     |     | This |
| ---------------------------------------- | --- | --- | --------- | --------------------------------------------- | --- | --- | ---- |
| thecaseofskew,thensavethesampledoutdata. |     |     | Lastly,we |                                               |     |     |      |
analysiscannotbedoneonthedatasetwithouttheguidance
repeatthepriorstepbutdosofromthecompletetraining
ofanatleastpartiallytrainedmodel.
| set: thisisthe“diverse”datasetforthecategory. |     |     | Foreach |     |     |     |     |
| --------------------------------------------- | --- | --- | ------- | --- | --- | --- | --- |
groupwithinacategory,weappendallothergroupstogether
AcomparisonofnoisydatatoOODandmoretypicalsam-
andthenleavethecurrentgroupoutsuchthatnewtraining plesisshownin Figure14.
| groupswereFemale | (cid:83) Intersex(forexample). |     | Foreach |     |     |     |     |
| ---------------- | ------------------------------ | --- | ------- | --- | --- | --- | --- |
setwithinacategory,trainanewmodelusingourpreviously E.3.DiverseDataWithFamiliarity
described1DCNN.Wemonitorforoverfittingbysetting
earlystoppingbasedonlosswithapatienceof4. Given our intention was to encourage diversity in our
dataset,anineffectivesamplingstrategymightexacerbate
Finally,theinfluenceofdemographicsonperformancevar-
|                  |          |                        |         | edge case failures.                          | We then select | a range from | the data |
| ---------------- | -------- | ---------------------- | ------- | -------------------------------------------- | -------------- | ------------ | -------- |
| ied. In general, | removing | activity and age group | subsets |                                              |                |              |          |
|                  |          |                        |         | distributiontosamplethemostfamiliardatafrom. |                |              | Thuswe   |
wasmoreharmfultomodelsthanhandsize,gender,orrace exploredthreegeneralapproaches:
subsets,buttherewereexceptions.
18

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
|     |     |     |     | race33,962Instances |     |     | scene65,461Instances |     |
| --- | --- | --- | --- | ------------------- | --- | --- | -------------------- | --- |
age_group54,693Instances
| diverse_data_age_group |             |             |                   | Multiple    |             | diverse_data_scene   |     |     |
| ---------------------- | ----------- | ----------- | ----------------- | ----------- | ----------- | -------------------- | --- | --- |
|                        | 21-25       |             | diverse_data_race |             |             | stomach_bed_right    |     |     |
|                        | >56         |             |                   | Black       |             | sitting_left         |     |     |
|                        | 46-50       |             |                   | White       |             | stomach_bed_left     |     |     |
|                        | 36-40       |             |                   | Asian       |             | sitting_right        |     |     |
|                        | 41-45       |             |                   | 0.0 0.2 0.4 | 0.6 0.8 1.0 | walking_slowly_right |     |     |
|                        | 26-30       |             |                   | Accuracy    |             | standing_right       |     |     |
|                        | 31-35       |             |                   |             |             | standing_left        |     |     |
|                        | 0.0 0.2 0.4 | 0.6 0.8 1.0 |                   |             |             |                      |     |     |
walking_slowly_left
|     | Accuracy |     |     |     |     | left_side_left |     |     |
| --- | -------- | --- | --- | --- | --- | -------------- | --- | --- |
back_bed_right
|     | phone_size33,870Instances |     |     | hand_size20,325Instances |     |     |     |     |
| --- | ------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- |
right_side_left
back_bed_left
| diverse_data_phone_size |     |     | diverse_data_hand_size |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
left_side_right
|     | mini |     |     | small |     |     |     |     |
| --- | ---- | --- | --- | ----- | --- | --- | --- | --- |
right_side_right
|     | max |     |     | large  |     |     |             |             |
| --- | --- | --- | --- | ------ | --- | --- | ----------- | ----------- |
|     | mid |     |     | medium |     |     | 0.0 0.2 0.4 | 0.6 0.8 1.0 |
Accuracy
|     | 0.0 0.2 0.4 | 0.6 0.8 1.0 |     | 0.0 0.2 0.4 | 0.6 0.8 1.0 |     |     |     |
| --- | ----------- | ----------- | --- | ----------- | ----------- | --- | --- | --- |
|     | Accuracy    |             |     | Accuracy    |             |     |     |     |
nail_length21,460Instances sex30,414Instances handedness20,348Instances
| diverse_data_nail_length |     |     | diverse_data_sex |        |     |                         | Left |     |
| ------------------------ | --- | --- | ---------------- | ------ | --- | ----------------------- | ---- | --- |
|                          |     |     |                  | Female |     | diverse_data_handedness |      |     |
short
|     | long |     |     | Male |     |     | Right |     |
| --- | ---- | --- | --- | ---- | --- | --- | ----- | --- |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
|     |     |     |     | Accuracy |     |     | Accuracy |     |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- |
Accuracy
Figure12. Theperformanceofeverymodelonthesametestset,splitacrosscategories. Foreachcategory,amodel’slabelindicates
whichsubgroupwasheldoutfromitstrainingset.Toensurefaircomparison,withineachcategoryeachmodelwastrainedonthesame
numberofinstances.Noticeforeachcategorythatthe“diverse”model(highlightedwithadarkercolor),i.e.,themodelwithnosubgroup
heldout,almostexclusivelyperformsthebest,despitehavingthesamenumberofdatainstancesastheothermodels.
Figure13.Overviewoffamiliarityimplementation.(1)WefitaGaussianMixtureModeltoourmodelofinterest.(2)Wepresentsamples
(e.g.ourtrainingdatafor“self-familiarity”)totheGMM,returninglog-likelihoodscores.
19

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
A IMU Time Series for standing_right Session 665
C IMU Time Series for back_bed_right Session 1459
B IMU Time Series for standing_right Session 633
Figure14.Distinctexamplesofdatacharacterizedasmost“unfamiliar”toamodel.(A)isanexampleofdatawewouldconsideroutof
distribution,(B)presentsacaseofsensorfailure—thesensorstoppedrecordingpartwaythroughthetask—and(C)showsaparticularly
noisysample,likelywheresomeonedroppedtheirphonemid-typing.
1. Replacekmostfamiliarsampleswithkleastfamiliar might seek to incorporate algorithmic methods of distin-
samples; guishingsourcesofuncertainty,howeverthereiscurrently
littleworkonthetopic. Existingresearcheitherrelieson
2. Distributedsamplingacrossawindowofk+imost
thelearningrateasaproxyfordiscriminatingtypesofun-
familiarsampleswithkleastfamiliarsamples,where
certaintyasaleatoricorepistemic(D’souzaetal.,2021),for
irepresentsapercentageoftheoveralltrainingset
example,orbuildsonBayesiannetworks(Kendall&Gal,
2017). Both face various weaknesses, and there remains
3. Distributedsamplingacrossawindowofk+imost
greatneedforadditionaltechniquesandevaluations.
familiar samples with k + i least familiar samples,
whereiisapercentageofthetrainingset
Familiarityfornewdata Whileweexploredfamiliarity
Eachsamplingmechanismwascomparedacrossmultiplek largelyfromtheperspectiveof“self-familiarity”—thatis,
andk+ivaluestodeterminetherelative“sweetspot”for whatthemodelhasalreadybeenexposedto,italsointro-
oursamplingstrategygivenaparticulartrainingdataset. We duces a mechanism by which we can understand how a
randomlyselectX percentofbestandworstscores,vary- modelrespondstodatait’spreviouslynotseen. Thismay
ingpercentagebetween0.5%—0.01%. Wetrainmodel(s) offer a mechanism of transparency through which future
oneachvariationofwindowsizeandsamplingpercentage, users could evaluate how a model responds to new data.
repeatingthepreviousstepsktimestoensureamultifoldval- Inthiswork,wecomputedfamiliarityfromasinglelayer.
idation,thencomparingtheintersectionalperformancesof Infuturework,wewillexplorehowfamiliaritycomputed
M tothenewmodelM trainedonthefamiliarity-informed atdifferentlayerscanbeleveraged. Giventhateachlayer
1 i
dataset. Thisisrepeatedperthescenariodescribedinthe capturesdistinctfeatureswithinthedata,aggregatinginfor-
fullpaper. mationacrossdepthsofthemodelmayleadtomoreholistic
identificationofunfamiliardataandwhatfeaturesaremore
specificallysotothemodel. Onewaytodothisisthrougha
F.LimitationsandFutureExtensionsof
ProductofExperts(PoE)paradigm(Hinton,2002)where
Familiarity
eachlayerisconsideredan“expert”.
Distinguishing between rare and noisy data A weak-
ness of familiarity is that we have no current method of Comparisons against active learning On the surface,
distinguishingnoisysamplesfromoutofdistributiondata. familiarityappearssimilartoactive-learning(AL).ALre-
Whileanunfamiliarsamplemightstandouttothemodel,in quires practitioners to choose which data to use given a
manycases,humanreviewisnecessarytoevaluateitsimpli- largecollection. Inourscenario,wemustunderstandwhich
cations. Forthisreason,inverynoisydatasets,familiarity data to collect or gather when there is no additional data
may be a tool best used for debugging. Future research readilyavailabletoruntheALalgorithmon. Onewayto
20

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
Figure15.Comparisonofaccuracyontestingdatabeforeandafterfamiliarityintervention.Minorregressionsareshown,whileaccuracy
improvementsincontrast
21

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
circumvent this difference is to apply AL to the training tributes have similar predictive performance), or calibra-
set,andthenextractstatisticsonthemetadatathattheAL tion(resultsareindependentofprotectedattributes)meth-
algorithmindicatesasmostuseful. Forexample,onecould ods (Corbett-Davies & Goel, 2018). In contrast to group
usetheentropyofthelogits: highentropyonadatapoint fairness,individualfairness(Dworketal.,2012)asksthat
mightbeanindicationthatthemodelisstilluncertainabout individualssimilarforataskbetreatedsimilarlythroughout
such type of data. An issue with such approach is that it thattask. Whilewell-intentioned,eachofthesefairnessen-
implicitlyassumesmodelsarewellcalibrated,whichisnot hancingapproacheshaveincitedcriticism(Corbett-Davies
| alwaysthecase. |     |     |     |     | &Goel,2018). |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
Mitchelletal.describeddiversity,heterogeneity,andfair-
| Interactivesystemsfordesigningdata |     |     | Designingdata |     |     |     |     |     |
| ---------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- |
nessasrelatedbutdistinctconcepts(Mitchelletal.,2020).
| advances | how we account | for the interplay | between | data |             |          |                 |                     |
| -------- | -------------- | ----------------- | ------- | ---- | ----------- | -------- | --------------- | ------------------- |
|          |                |                   |         |      | In contrast | to prior | work by (Asudeh | et al., 2019; Zheng |
andmodel(Hooker,2021),consideringbothwithinthede- et al., 2012), which considers a more encompassing def-
| ploymentcycletocompensateformisstepsineither. |     |     |     | Inour |            |             |            |                        |
| --------------------------------------------- | --- | --- | --- | ----- | ---------- | ----------- | ---------- | ---------------------- |
|                                               |     |     |     |       | inition of | diversity—a | measure to | capture nuance of col- |
case study, we use data visualizations (e.g., Figure 2) to lectionbasedonvarietyofconstituentelements—Mitchell
comparepractitioners’expectationsagainstcollecteddata
|                |                |             |            |         | et al.’s diversity | emphasizes | attributes | of social concern. |
| -------------- | -------------- | ----------- | ---------- | ------- | ------------------ | ---------- | ---------- | ------------------ |
| distributions, | then visualize | familiarity | to explore | rare or |                    |            |            |                    |
Theyarguediversitymeasuresthatarenotspecifictosocial
noisy samples. The visualizations and interfaces used in groups should instead be considered heterogeneity mea-
| this work | are largely static; | however, | we see | a great op- |     |     |     |     |
| --------- | ------------------- | -------- | ------ | ----------- | --- | --- | --- | --- |
sures,thoughdiversityhaslongbeeninterchangeablewith
portunity to build the designing data process into future heterogeneity. Mitchelletal.’sargumentisunderstandably
interactivesystemsandtoolsforbetterdataworkandmodel motivatedbyconcernsofspecificityandimpact,butrecon-
| evaluation. | FromtheHCIandvisualizationcommunities, |     |     |     |     |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
cilingwhatdatamayconferbiasingeffectsforsocialgroups
thereareanumberofinteractivesystemsthathavehelped with what does not is difficult: can human-agnostic data
MLpractitionersexploretheirdata(Inc.,2021;201,2017;
existindatacollectedbyandinreferencetopeople?
Hohmanetal.,2020b)andevaluatetheirmodels(Amershi
|                                                  |     |     |     |     | Fields with | historic | interest in diversity | or heterogeneity |
| ------------------------------------------------ | --- | --- | --- | --- | ----------- | -------- | --------------------- | ---------------- |
| etal.,2015;Wexleretal.,2019;Go¨rtleretal.,2022); |     |     |     | for |             |          |                       |                  |
anin-depthsurveyonvisualanalyticsforMLsee(Hohman includeinformationretrieval,ecology,biology,organization
science,sociology,andchemistry,allofwhichhavedevel-
| etal.,2018). | Directionsforfutureinteractivesystemsmight |     |     |     |     |     |     |     |
| ------------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
opedoremployedapproachestomeasurediversity. These
includetoolstohelppractitionersreflectontheirdatacol-
approacheslargelyfallintooneofthesevenfollowingbuck-
| lection practices | (e.g., digging | into their | expectations, | as  |     |     |     |     |
| ----------------- | -------------- | ---------- | ------------- | --- | --- | --- | --- | --- |
ets: geometricordistance-based,combinatorial,aggregate,
discussedinAppendixC),ortoolstodirectfamiliarityanal-
| yses. |     |     |     |     | utilityandranking,coverage,andhybriddistanceandcov- |     |     |     |
| ----- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
eragebaseddiversitymeasures(Drosouetal.,2017;Zheng
|     |     |     |     |     | etal.,2012). | Examplesofgeometricordistance-basedmea- |     |     |
| --- | --- | --- | --- | --- | ------------ | --------------------------------------- | --- | --- |
G.ExtendedLiteratureReview
|     |     |     |     |     | sures of diversity |     | include by dataset’s | volume (Mouchet |
| --- | --- | --- | --- | --- | ------------------ | --- | -------------------- | --------------- |
etal.,2010;Chaoetal.,2014;Anarietal.,2016;Celisetal.,
G.1.Fairness,Diversity,andHeterogeneity
2016;Whittaker,1972)orbyvariancesuchasinprinciple
Fairnesshasbecomeanincreasinglycommonconsideration componentanalysis(PCA)(Samadietal.,2018). Ingen-
for algorithmic contexts (Drosou et al., 2017). However, eral,thesemetricsmorecloselymatchwithMitchelletal.’s
thetermhasbeenconflatedwithjustice,bias,ethicalma-
definitionofheterogeneityastheydonotexplicitlyreferto
chinelearning, equity, diversity, heterogeneity, andinclu- features with societal import and context (Mitchell et al.,
sionduetocross-disciplinaryuseandoverloadedterminol- 2020). Ultimately,Mitchelletal.’sinterpretationofdiver-
ogy(Mitchelletal.,2020;Celisetal.,2018). sity is intended to bring to light social inequalities found
|     |     |     |     |     | in ML products | specifically, | while | others emphasize the |
| --- | --- | --- | --- | --- | -------------- | ------------- | ----- | -------------------- |
Algorithmicnotionsoffairnessareoftenpresentedthrough
measureofheterogeneity—comprehensivevarietywithin
| mathematical | formalizations | intended | to  | ensure anti- |     |     |     |     |
| ------------ | -------------- | -------- | --- | ------------ | --- | --- | --- | --- |
thedataset.
| discriminationinthecontextofclassificationsystems. |          |          |           | They    |     |     |     |     |
| -------------------------------------------------- | -------- | -------- | --------- | ------- | --- | --- | --- | --- |
| most commonly                                      | focus on | ML model | outcomes, | but may |     |     |     |     |
DiversitymetricsinMLcontextshavebeenusedtodirect
also describe input data or how systems use model re- bias mitigation efforts (Celis et al., 2016). Instances of
sults (Mitchell et al., 2020). ML models incorporate thiscanbefoundinsubsetselection,wheredeclarationsof
outcome-specificfairnessbyaddingconstraintstoensure
“diversityconstraints”defineexpectedfrequenciesforsensi-
eithergrouporindividualparityacrossclassificationerror tivevaluesthatthedatamustsatisfy(Milanietal.,2020),
| metrics (Mitchell | et al., | 2020). Group | fairness | enhanced |     |     |     |     |
| ----------------- | ------- | ------------ | -------- | -------- | --- | --- | --- | --- |
ortomeasurerelativecoveragewithinadataset(Mitchell
models(Friedleretal.,2019)useeitheranti-classification etal.,2020). Analternativesubsetselectiontechniqueas-
(whereinprotectedattributesarenotincludedindecision sociates diversity scores to subsets then chooses subsets
making),classificationparity(groupsacrossprotectedat-
22

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
whenprobabilitiesareproportionaltothisscore(Celisetal., them(Palanicaetal.,2019).
| 2016;2018). | Uniformly,thesemethodsactasstopgapsto |     |     |     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Outsideofcensoringoutputs,biasmitigationstrategiescan
biasedand/orhomogeneousdata—particularlycommonin
bedividedintothreestagesofaMLmodeldevelopment:
| the context | of data summarizations | of big | datasets (Celis |     |     |     |     |
| ----------- | ---------------------- | ------ | --------------- | --- | --- | --- | --- |
pre-training(e.g.,sampleweightingordatasetbalancing),
etal.,2018).
in-training(e.g.,addingspecificconstraintsinthefunction
Theabilitytoproducediversesubsetsusingdiversitymet- thatisbeingoptimized)andpost-training(e.g.,bytweak-
ricsdoesnotguaranteefairnessacrosssamplesintheform ing the prediction in order to ensure some fairness met-
ofappropriaterepresentationofsensitiveattributes(Celis ric)(Doninietal.,2018).Pre-trainingcanbefurtherdivided
etal.,2018). Partially,thisisbecausefairnesshasmultiple intocollectionandpost-collection. Despitethefundamental
measures(Mitchelletal.,2020). Fairtreatmentacrossso- nature of data collection, typical technical approaches to
cial groups may also require different things for different biasmitigationfocusonpost-collectionefforts—e.g.,modi-
contexts. Forinstance,consideradatasetinwhicheachdata ficationofthedataset,reweightingandfine-tuningofhyper-
point has a gender. One notion of group fairness, useful parameters,filteringoutput,orsomecombinationtherein—
for ensuring that the ground truth is not distorted, is pro- whichlargelyactasstopgaps, aresensitivetounderlying
portional representation, i.e., the distribution of sensitive data(Wieringa,2020)andultimatelymaynotresolveun-
characteristicsintheoutputsetshouldbeidenticaltothatof derlyingissuesathand.
| theinputdataset. | Anothernotionoffairness,arguedtobe |     |     |     |     |     |     |
| ---------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
Additionalcomplicationsarisewhenworkingwithdataac-
necessarytoreversetheeffectofhistoricalbiases,couldbe
quiredindependently,possiblythroughaprocessinwhich
equalrepresentationwheretherepresentationofsensitive
|     |     |     |     | the data scientist | has little | or no control. | This “found |
| --- | --- | --- | --- | ------------------ | ---------- | -------------- | ----------- |
characteristicsshouldbeequalindependentoftheratioin
data”(RamasamyRamamurthy&Roy,2018)introduces
| the input dataset. | The plethora | of metrics | and evaluative |     |     |     |     |
| ------------------ | ------------ | ---------- | -------------- | --- | --- | --- | --- |
uniquechallengestoensuringdatacoverageforscientists
| toolsvaryandeachhaveongoingdiscussionsofmerit. |     |     | Ulti- |               |                                     |     |     |
| ---------------------------------------------- | --- | --- | ----- | ------------- | ----------------------------------- | --- | --- |
|                                                |     |     |       | andengineers. | Forbothfounddataandbigdatacontexts, |     |     |
mately,datasetsmustbeconsideredinrelationtotheuseat
post-collectionapproachessuchassubsetselectionandclass
hand,andthepotentialharmanyfailuresmaycause.
imbalancecorrectionslikeunder-orover-samplingarein-
Qualitativeresearchmethods,statistics,andsurveyliterature troducedtocounterbiasandskew(Japkowicz&Stephen,
have historically managed representative data collection 2002). Yet sampling methods can obfuscate information
in a variety of ways, from expert panels to standards in aboutappearancefrequencyinadataset—iftherearelimited
populationsurveytechniques,yetthesemethodsfacetheir examplesofXandsoweoversample,thenthoseinstancesof
owncomplicationsanddonotnecessarilytranslatetothe Xarenotuniqueandmaycausethemodeltoinferincorrect
needsofmachinelearningteams. characteristicsofaclass,affectingaccuracymetricsaswell
|     |     |     |     | asproductionperformance. |     | Theseapproachesarelimited; |     |
| --- | --- | --- | --- | ------------------------ | --- | -------------------------- | --- |
forexample,whenimprovingamodelwithoutaccesstothe
G.2.BiasMitigation
originaltrainingdataset,balancinginthetraditionalsenseis
Whileexamplesofalgorithmicbiasareoftenhighlightedby
|     |     |     |     | impossible. | Regardlessofthecontext,thesedatabalancing |     |     |
| --- | --- | --- | --- | ----------- | ----------------------------------------- | --- | --- |
mediaoutlets,thisfrequencybeliesthedifficultyofinitial
|     |     |     |     | approachesignoredatalearnability: |     | havinganequalnum- |     |
| --- | --- | --- | --- | --------------------------------- | --- | ----------------- | --- |
discovery—failuresarehardtouncoverduringdevelopment,
berofsamplesperclassneglectsthefactthatsomeclasses
thusresponsibilityoftenfallstothepublicviaproducten- areinherentlyeasiertolearnthanothers(Ben-Davidetal.,
| gagement. | InthecaseofGooglePhotos,themodelcould |     |     |     |     |     |     |
| --------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
2019;Schapire,1990;Klawonnetal.,2019).
notdistinguishbetweenagorillaandaBlackpersonandit
WorkonMLgeneralizationhaslookedtoavoidtheissue
wasamemberofthepublicthatflaggedtheconcerningla-
beling. Situationslikeracistphotoidentificationalgorithms ofbiasesindata distributionandcollectionaltogether by
arenotuncommon,andonceuncoveredarerespondedto focusingonthecausalrelationshipswithindata. Suppos-
edlyrobusttolackofcoverageorvariationwithinadataset,
| inavarietyofways. | Google’sresponsewastocensorout- |     |     |     |     |     |     |
| ----------------- | ------------------------------- | --- | --- | --- | --- | --- | --- |
puttedlabelssuchas“chimpanzee”and“gorilla”withinthe Invariant Risk Minimization (IRM) relies on latent vari-
ableswithinthedata—informationnotexplicitlyobserved,
publicPhotosappsearchresults(?).Intheircase,themodel
couldnotdistinguishbetweenagorillaandaBlackperson butratherwhichareinferredfromexistingdata—tolearn
becauseitwasnottrainedtodoso—therewerenotenough conceptsmorecloselyalignedwithgroundtruth(Arjovsky
|     |     |     |     | etal.,2019). | IRMhasmetbeenmetwithscepticism,how- |     |     |
| --- | --- | --- | --- | ------------ | ----------------------------------- | --- | --- |
instancesofBlackfacesinthedataset(Asudehetal.,2019).
Biased data and lack of diverse representation has broad ever,andworkbyRosenfeldetal.foundthatIRMcan“fail
catastrophically”unlessthetestandtrainingdistributions
| impactsindomainsbeyondcomputervision. |     |     | Popularper- |     |     |     |     |
| ------------------------------------- | --- | --- | ----------- | --- | --- | --- | --- |
sonalizedvoiceagents,forexample,struggletorecognize aresufficientlysimilar(Rosenfeldetal.,2020),ultimately
foreignaccentsundercertaincontextssuchasunderstand- comingbacktotheintitialquestionofhowtodevelopdi-
|                |            |                 |            | verse datasets | that more accurately | reflect | real world use |
| -------------- | ---------- | --------------- | ---------- | -------------- | -------------------- | ------- | -------------- |
| ing medication | names when | users correctly | pronounced |                |                      |         |                |
23

DesigningData:ProactiveDataCollectionandIterationforMachineLearning
cases.
G.3.ContrastingFamiliaritytoOtherMethods
Leeetal(Leeetal.,2018)ismostsimilartoourproposed
methodoffamiliarity.However,thereareseveraldifferences
betweenourworkandtheirs:theyuseclass-conditionalden-
| sity estimation,              | while        | we do   | not use                   | labels,   | thus fit one |
| ----------------------------- | ------------ | ------- | ------------------------- | --------- | ------------ |
| model across                  | all classes. | We      | use PCA                   | to reduce | activa-      |
| tion dimensionality           | before       | fitting | the                       | model (DE | in high      |
| dimensionalspaceisdifficult). |              |         | Finally,weuseavariational |           |              |
BayesianestimationoftheGMM;theyestimateGaussian
meanandcovariancedifferently.
24