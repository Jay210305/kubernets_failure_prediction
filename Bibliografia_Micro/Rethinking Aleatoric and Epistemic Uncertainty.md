|     |     | Rethinking |                       | Aleatoric | and           | Epistemic                                        |               | Uncertainty      |     |           |      |              |     |
| --- | --- | ---------- | --------------------- | --------- | ------------- | ------------------------------------------------ | ------------- | ---------------- | --- | --------- | ---- | ------------ | --- |
|     |     |            | FreddieBickfordSmith1 |           | JannikKossen1 |                                                  |               | EleanorTrollope1 |     |           |      |              |     |
|     |     |            | MarkvanderWilk1       |           | AdamFoster1   |                                                  | TomRainforth1 |                  |     |           |      |              |     |
|     |     | Abstract   |                       |           |               | sumptionsaremadeabouthowuncertaintywilldecompose |               |                  |     |           |      |              |     |
|     |     |            |                       |           |               | on unseen                                        | data          | (Seebo¨ck        | et  | al, 2019; | Wang | & Aitchison, |     |
Theideasofaleatoricandepistemicuncertainty
2021),andmisleadingconnectionsaredrawnbetweenun-
arewidelyusedtoreasonabouttheprobabilistic
5202 guA 81  ]GL.sc[  3v29802.2142:viXra
certaintyandpredictiveaccuracy(Orlandoetal,2019;Wang
| predictionsofmachine-learningmodels. |     |     |     | Weiden- |     |        |        |           |          |     |              |            |     |
| ------------------------------------ | --- | --- | --- | ------- | --- | ------ | ------ | --------- | -------- | --- | ------------ | ---------- | --- |
|                                      |     |     |     |         |     | et al, | 2019). | Meanwhile | distinct |     | mathematical | quantities |     |
tifyincoherenceinexistingdiscussionsofthese
|       |             |      |            |                |     | areusedtorefertonotionallythesameconcepts: |     |              |     |          |           |         | epistemic |
| ----- | ----------- | ---- | ---------- | -------------- | --- | ------------------------------------------ | --- | ------------ | --- | -------- | --------- | ------- | --------- |
| ideas | and suggest | this | stems from | the aleatoric- |     |                                            |     |              |     |          |           |         |           |
|       |             |      |            |                |     | uncertainty,                               |     | for example, |     | has been | variously | defined | us-       |
epistemicviewbeinginsufficientlyexpressiveto
ingdensity-based(Mukhotietal,2023;Postelsetal,2020),
captureallthedistinctquantitiesthatresearchers
information-based(Galetal,2017)andvariance-based(Gal,
| are interested |     | in. To | address | this we present | a   |     |     |     |     |     |     |     |     |
| -------------- | --- | ------ | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2016;Kendall&Gal,2017;McAllister,2016)quantities.
| decision-theoretic |     | perspective |     | that relates | rigor- |     |     |     |     |     |     |     |     |
| ------------------ | --- | ----------- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ousnotionsofuncertainty,predictiveperformance We suggest this incoherence arises from the aleatoric-
andstatisticaldispersionindata. Thisservesto epistemic view being too simplistic in the context of ma-
support clearer thinking as the field moves for- chinelearning.Researchersarelookingforconcretenotions
ward. Additionallyweprovideinsightsintopopu- ofamodel’spredictiveuncertaintyandhowthatuncertainty
larinformation-theoreticquantities,showingthey mightormightnotchangewithmoredata(associatedwitha
canbepoorestimatorsofwhattheyareoftenpur- decompositionintoirreducibleandreduciblecomponents),
portedtomeasure,whilealsoexplaininghowthey butalsorelatednotionsofpredictiveperformanceanddata
canstillbeusefulinguidingdataacquisition. dispersion. Thealeatoric-epistemicviewcannotsatisfyall
|     |     |     |     |     |     | theseneeds:                                     |     | manyconceptsstandtobedefined,whilethe |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | viewfundamentallyonlyhascapacityfortwoconcepts. |     |                                       |     |     |     |     | Yet |
1 Introduction
|     |     |     |     |     |     | the current |     | state of | play is | to nevertheless |     | appeal | to the |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------- | --------------- | --- | ------ | ------ |
aleatoric-epistemicview,withdifferentresearchersusingit
Whenmakingdecisionsunderuncertainty,itcanbeuseful indifferentways. Aresultofthisconceptualoverloading
toreasonaboutwherethatuncertaintycomesfrom(Osband
istoconflatequantitiesthatoughttoberecognisedasdis-
| etal,2023;Wenetal,2022). |     |     | Researchersoftenaimtodo |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tinct. Farfromjustamatterofsemantics,thisishavinga
thisbyreferringtoaleatoric(literalmeaning: “relatingto meaningfuleffectonthefield’sprogress: methodsarebeing
| chance”) | and epistemic | (“relating |     | to knowledge”) | uncer- |     |     |     |     |     |     |     |     |
| -------- | ------------- | ---------- | --- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
designedandevaluatedbasedonshakyfoundations.
tainty,ideaswithalonghistoryinthestudyofprobability
|                 |                                        |     |     |     |     | To establish |     | a clearer | perspective, |     | we  | draw on | powerful |
| --------------- | -------------------------------------- | --- | --- | --- | --- | ------------ | --- | --------- | ------------ | --- | --- | ------- | -------- |
| (Hacking,1975). | Aleatoricuncertaintyistypicallyassoci- |     |     |     |     |              |     |           |              |     |     |         |          |
atedwithstatisticaldispersionindata(sometimesthought yet underappreciated ideas from decision theory (Dawid,
|     |     |     |     |     |     | 1998;DeGroot,1962;Neiswangeretal,2022). |     |     |     |     |     | Ourstarting |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
ofasnoise),whileepistemicisassociatedwithamodel’sin-
ternalinformationstate(Hu¨llermeier&Waegeman,2021). pointisafinaldecisionofinterestwithanassociatedloss
function. Giventhis,uncertaintyinpredictivebeliefscanbe
Concerninglygiventheirscaleofuse,theseideasarenotbe- formalisedasthesubjectiveexpectedlossofactingBayes-
| ingdiscussedcoherentlyintheliterature. |     |     |     | Thelinebetween |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimallyunderthosebeliefs;thisgeneralisesquantitieslike
model-basedpredictionsanddata-generatingprocessesisre- varianceandShannonentropy. Fromthereweshowhow
peatedlyblurred(Aminietal,2020;Ayhan&Berens,2018;
reasoningaboutnewdatagivesrisetoanotionofexpected
Immeretal,2021;Kapooretal,2022;Smith&Gal,2018;
|     |     |     |     |     |     | uncertainty |     | reduction, | which | we  | can use | to identify | a de- |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ----- | --- | ------- | ----------- | ----- |
van Amersfoort et al, 2020). On top of this, tenuous as- compositionofuncertaintyintoirreducibleandreducible
1UniversityofOxford. components. Thenweclarifytheconnectionbetweenuncer-
CorrespondencetoFreddieBickford
tainty,predictiveperformanceanddatadispersion,linking
Smith<fbickfordsmith@cs.ox.ac.uk>.
toclassicdecompositionsfromstatisticsandinformation
42nd
Proceedings of the International Conference on Machine theory. Overall this provides a coherent synthesis of key
Learning,Vancouver,Canada.PMLR267,2025.Copyright2025 quantitiesthatresearchersareinterestedin(Figure1).
bytheauthor(s).
1

RethinkingAleatoricandEpistemicUncertainty
|                 | Learning | Reasoning       |                     |                 |     |     |     |
| --------------- | -------- | --------------- | ------------------- | --------------- | --- | --- | --- |
| Decisionproblem |          | Predictivemodel | Bayes-optimalaction |                 |     |     |     |
| ℓ:A×Z→R         |          | pn(z)=p(z;y1:n) | a∗ =argmina∈A       | E pn(z)[ℓ(a,z)] |     |     |     |
n
| Trainingdata |     |     | Uncertaintyquantification |     |     |     |     |
| ------------ | --- | --- | ------------------------- | --- | --- | --- | --- |
y1:n∼ptrain(y1:n|π)
|     |     |     | Predictiveuncertainty |            | Expecteduncertaintyreduction |                |     |
| --- | --- | --- | --------------------- | ---------- | ---------------------------- | -------------- | --- |
|     |     |     | h[pn(z)]=E            | pn(z)[ℓ(a∗ |                              |                |     |
|     |     |     |                       | n ,z)]     | EURt z rue(π,m)=h[pn(z)]−E   | + [h[pn+m(z)]] |     |
ptrain(y1 :m|π)
|     |     |     |     |     | ≈h[pn(z)]−E | [h[qn+m(z)]] |     |
| --- | --- | --- | --- | --- | ----------- | ------------ | --- |
pn(y1 + :m|π′)
Modelevaluation
|     |     |     | Properscoringrule | Discrepancyfunction |     |     |     |
| --- | --- | --- | ----------------- | ------------------- | --- | --- | --- |
d(pn,peval)=E
|     |     |     | s(pn,z)=ℓ(a∗ | n ,z) | peval(z)[s(pn,z)]−h[peval(z)] |     |     |
| --- | --- | --- | ------------ | ----- | ----------------------------- | --- | --- |
Figure1 Ourdecision-theoreticviewcoherentlyrelatesmachine-learningconceptsthathavebeenconflatedunderthealeatoric-epistemic
view.Weconsidertakinganaction,a∈A,inlightofimperfectknowledgeofz∈Z,withanaction’sconsequencesmeasuredbyaloss
function,ℓ(a,z).Sincezisunknown,weuseanyavailabletrainingdata,y ,tobuildapredictivemodel,p (z),withwhichwecan
|     |     |     |     | 1:n |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
reasonoverpossiblevaluesofzandthuschooseanaction.Additionallywecanusethemodeltoquantifyuncertaintyanditsreducibility
withrespecttonewdata,andwecanevaluatethemodelusingaground-truthrealisationofzorareferencedistribution,p (z).
eval
Bridgingthisgeneralisedperspectivebacktohowaleatoric whetherthatpredictionisfundamentallyuncertainforthe
andepistemicuncertaintyhavebeendiscussedinpastwork, given model class or instead due to a lack of data. This
weprovidenewinsightsonBALD,apopularinformation- breakdownhasclearutilityinthecontextofseekingnew
theoretic objective for data acquisition (Gal et al, 2017; datathatwillreducepredictiveuncertainty(BickfordSmith
Houlsbyetal,2011;Lindley,1956). Inparticularwehigh- etal,2023;2024;MacKay,1992a;b). Butitisalsorelevant
lightthatitshouldbeseennotasadirectmeasureoflong- elsewhere: inmodelselection,forexample,wemightwant
runreduciblepredictiveuncertainty,ashasbeensuggested toquantifyamodel’sscopeforimprovementbyforecasting
inthepast, butinsteadasanestimatorthatcanbehighly howitspredictionswillchangegivenmoredata(Barbieri
inaccurate. ReconcilingthiswithBALD’spracticalutility, &Berger,2004;Fong&Holmes,2020;Geisser&Eddy,
wesuggestitisoftenbetterunderstoodasapproximately 1979;Kadane&Lazar,2004;Laud&Ibrahim,1995).
| measuringshort-runreductionsinparameteruncertainty. |     |     | It  |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Uncertaintythatresolvesinlightofnewdatacanbethought
canthereforebeuseful,albeitstillsuboptimalinprediction-
ofas“epistemic”inthesensethatdataconveysknowledge.
orientedsettings(BickfordSmithetal,2023;2024).
Intuitivelythecorrespondingirreducibleuncertaintyseems
Ourworkthusservestoinformfutureworkintwokeyways. tobedeterminedbynotonlythemodelclassbutalso,among
Ontheonehanditshedslightonthecontradictionsofthe otherthings,an“inherent”levelofuncertaintyassociated
aleatoric-epistemicviewandpresentsacoherentalternative withthedatasourceathand,whichisoftenthoughtofin
perspectivethatallowsclearerthinkingaboutuncertaintyin termsofrandomnessorchance,hencetheword“aleatoric”.
| machinelearning. | Ontheotherhanditprovidesmoredirect |     |     |     |     |     |     |
| ---------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
Whiletheconceptsofaleatoricandepistemicuncertainty
| practicalinsights. | Itclarifiesthatwhatmighthaveseemed |     |     |     |     |     |     |
| ------------------ | ---------------------------------- | --- | --- | --- | --- | --- | --- |
hadpreviouslybeenusedinmachinelearning,forexample
likearbitrarychoicesforadecision-makercaninsteadbe
byLawrence(2012)andSengeetal(2014),theirpopular-
| made by following | well-defined | logic: given | some basic |          |                |                |                  |
| ----------------- | ------------ | ------------ | ---------- | -------- | -------------- | -------------- | ---------------- |
|                   |              |              |            | ity grew | following work | by Gal (2016), | Gal et al (2017) |
componentsandprinciples,itbecomesclearhowweshould
|     |     |     |     | and Kendall | & Gal (2017). | The most widely | used math- |
| --- | --- | --- | --- | ----------- | ------------- | --------------- | ---------- |
measurepredictiveuncertainty,predictiveperformanceand
ematicaldefinitionsoftheseideas,whichwewilldiscuss
datadispersion,andhowwecanidentifygoodfuturetrain-
inSection4,aretheinformation-theoreticquantitiesused
ingdata. Italsohighlightsapproximationsthatoftenhave
byGaletal(2017),buildingonearlierworkonBayesian
tobemadeinpractice,revealingscopeforsuboptimalper-
experimentaldesign(Lindley,1956)andBayesianactive
formanceandthereforeinformingfuturemethodsresearch.
learning(Houlsbyetal,2011;MacKay,1992a;b).
2 Background Arangeofperspectivesonaleatoricandepistemicuncer-
taintyinmachinelearninghavebeenputforwardinrecent
Thebroadmotivationofthealeatoric-epistemicviewisto years. Theseincludeadiscussionofsourcesofuncertainty
distinguish between different sources of uncertainty. If a in machine learning (Gruber et al, 2023); a case against
model’s prediction is uncertain, we might want to know Shannon entropy as a measure of predictive uncertainty
2

RethinkingAleatoricandEpistemicUncertainty
(Wimmeretal,2023);proposalsforalternativeinformation thatminimisesthissubjectiveexpectedloss(Ramsey,1926;
quantities(Schweighoferetal,2023a;b;2025);andvarious Savage,1951). Alternativedecision-makingapproachesin-
other suggestions for how to define uncertainty, such as cludeminimax,whichinvolvesminimisingtheworst-case
intermsofclass-wisevariance(Saleetal,2023b;2024b), frequentistrisk(vonNeumann,1928;Wald,1939;1945).
| credal sets | (Hofman | et al, | 2024a; Sale | et al, | 2023a), dis- |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------ | ----------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
3.4 Machinelearningallowsdata-drivenprediction
tancesbetweenprobabilitydistributions(Saleetal,2024a),
frequentistrisk(Kotelevskiietal,2022;2025;Lahlouetal,
Minimisingsubjectiveexpectedlossrequiresbeliefsoverz,
2023)andproperscoringrules(Hofmanetal,2024b). As andthosebeliefscanoftenbeinformedbysometraining
wewillshow,ourreplacementforthealeatoric-epistemic
|                                         |     |     |     |     |     | data,    | y   | ∼ p     | (y      | |π), whereπ | ∈ Πisapolicythat |         |     |
| --------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | ------- | ------- | ----------- | ---------------- | ------- | --- |
| viewunifiesandexplainsmanyoftheseideas. |     |     |     |     |     |          | 1:n | train   | 1:n     |             |                  |         |     |
|                                         |     |     |     |     |     | controls |     | aspects | of data | generation. | We want          | notions | of  |
uncertaintythatreflecthowwewillactuallylearnfromdata,
3 Keyconcepts ratherthanassumingidealisedupdatingthatwecannotper-
|     |     |     |     |     |     | forminpractice. |     |     | Wethereforedefineourpredictivemodel, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
Ouraiminthisworkistoformaliseandlinktogetherquanti-
|                                                      |     |     |     |     |     | p   | (z)=p(z;y |     | ),tobetheoutputofagenericmachine- |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------------------------- | --- | --- | --- | --- |
| tiesthathavebeenassociatedwiththeideasofaleatoricand |     |     |     |     |     | n   |           | 1:n |                                   |     |     |     |     |
learningmethodappliedtothetrainingdata(andtheinput
| epistemicuncertaintyinpastwork. |     |     |     | Inparticularwelook |     |     |          |          |         |     |              |       |         |
| ------------------------------- | --- | --- | --- | ------------------ | --- | --- | -------- | -------- | ------- | --- | ------------ | ----- | ------- |
|                                 |     |     |     |                    |     | of  | interest | if there | is one) | for | any given n, | which | lets us |
toidentifyarigorousnotionofpredictiveuncertaintyand
reasonaboutactualchangesinuncertaintyasnvaries.
theextenttowhichitreducesasmoredataisobserved,and
alsomeasuresofpredictiveperformanceandstatisticaldis- Conventional Bayesian inference—taking a generative
persionindata. Westartbyhighlightingsomefoundational modeloverpossibledataandconditioningontheobserved
|                                                |     |     |     |     |     | data,givingp |     | (z) | = p(z|y | )—isonepossibleupdating |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | ------- | ----------------------- | --- | --- | --- |
| conceptsthatwillbeusedthroughoutourdiscussion. |     |     |     |     |     |              |     | n   |         | 1:n                     |     |     |     |
method. Othersincludedeeplearning(LeCunetal,2015),
3.1 Reasoningshouldstartwiththedecisionofinterest in-contextlearning(Brownetal,2020)andnon-Bayesian
|                                                    |     |     |     |          |          | ensemblemethods(Breiman,2001).  |     |           |     |                             | Insomecasesthepre- |       |        |
| -------------------------------------------------- | --- | --- | --- | -------- | -------- | ------------------------------- | --- | --------- | --- | --------------------------- | ------------------ | ----- | ------ |
| Weconsidertakinganaction,a∈A,underimperfectknowl-  |     |     |     |          |          |                                 |     |           |     |                             | E                  |       |        |
|                                                    |     |     |     |          |          | dictivedistributionisdefinedasp |     |           |     |                             | (z) =              | [p    | (z|θ)] |
| edgeofaground-truthvariable,z                      |     |     | ∈   | Z. Herez | couldfor |                                 |     |           |     |                             | n                  | pn(θ) | n      |
|                                                    |     |     |     |          |          | whereθ                          | ∼p  | (θ)=p(θ;y |     | )representsasetofstochastic |                    |       |        |
| examplebeanoutputrelatingtoagiveninput(ifso,thein- |     |     |     |          |          |                                 |     | n         |     | 1:n                         |                    |       |        |
modelparametersthatweaverageoveratpredictiontime.
putisleftimplicitinournotation)oraparameterinamodel,
andacouldbeadirectpredictionofz,withA=Zforpoint Regardlessofwhethertherearestochasticparameters,the
prediction,orA = P(Z)forprobabilisticprediction. We updating scheme could be stochastic. To handle this we
emphasiseourchoicetofocusonthisdecision,indeliberate taketheconventionthatupdatingstochasticityisimplicitly
contrastwiththemorecommonstartingpointoflearninga absorbedintoy : wecanconsiderourmachine-learning
1:n
modelfromfixeddata. Wewantanotionofpredictiveun- methodtobeadeterministicmappingthattakesarandom-
certaintythatisgroundedinactionsandtheirconsequences, numberseedasanauxiliaryinputalongwithdata. Thus,
andweneedtoreasonaboutdifferentpossibledatasetsto whilestochasticupdatingcanbesourceofvariabilityinhow
rigorouslythinkaboutreductionsinuncertainty. uncertainty reduces, this can be dealt with as part of the
variabilityalreadypresentinwhatdataweobserve.
3.2 Actionsinducelossesthatreflectpreferences
3.5 Bayesoptimalityisasubjectivenotion
| We assume | we can | measure | the consequences |     | of taking |     |     |     |     |     |     |     |     |
| --------- | ------ | ------- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
actionainlightofarealisationofz usingaloss(orneg- An action taken by minimising subjective expected loss
R.
ative utility) function, ℓ : A×Z → In principle the underp (z)isreferredtoasBayesoptimal(Murphy,2022);
n
specificationofℓfollowsdirectlyfromhavingpreferences if the action is an estimator of some quantity of interest
that satisfy basic axioms of rationality (von Neumann & thenitisknownasaBayesestimator. ThenotionofBayes
Morgenstern,1947). Inpracticeitcanbehardtoknowwhat optimality assumes our beliefs, p (z), represent our best
n
ℓshouldbe;optionsfordealingwiththisincludeusingan knowledge of z, and ℓ reflects our preferences. It says
intrinsiclossorarandomloss(Robert,1996;2007). nothingatallabouthowwellourbeliefsmatchreality,or
abouttheactionswewouldtakeifwehaddifferentbeliefs.
3.3 Subjectiveexpectedlossenablesdecision-making
Bayes-optimalactionscanthereforebesuboptimalasjudged
|                                 |     |     |     |                |     | usingrealisationsofz |     |     | fromsomewhereotherthanp |     |     |     | (z), |
| ------------------------------- | --- | --- | --- | -------------- | --- | -------------------- | --- | --- | ----------------------- | --- | --- | --- | ---- |
| Sinceℓisafunctionoftheunknownz, |     |     |     | itcannotbeused |     |                      |     |     |                         |     |     |     | n    |
suchasasystemservingasasourceofgroundtruth.
| directlyasanobjectiveforselectinganaction,a. |     |     |     |     | Aprin- |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
cipledsolutionthatwefocusonhereistoformsubjective
3.6 Predictionsoftendonotmatchdatageneration
| beliefs | over possible | values | of z (conventionally |     | this be- |     |     |     |     |     |     |     |     |
| ------- | ------------- | ------ | -------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
liefstatewouldbeaBayesianpriororposterior),average The correspondence between our predictions, p (z), and
n
overthesetoformanexpectedloss,thenchooseanaction thedata-generatingprocess,p train (y i |π(y <i ),y <i ),canbe
3

RethinkingAleatoricandEpistemicUncertainty
Aleatoricuncertainty
“capturesnoiseinherentinthe “cannotbereducedevenifmore Expectedparameter-conditional
observations” ̸= dataweretobecollected” ̸= predictiveentropy
H[ptrain(y1:n|π)]orH[peval(z)] H[p∞(z)] E pn(θ)[H[pn(z|θ)]]
Epistemicuncertainty
“uncertaintyinthemodel “canbeexplainedawaygiven Expectedinformationgainin
parameters” ̸= enoughdata” ̸= themodelparameters
H[pn(θ)] H[pn(z)]−H[p∞(z)] H[pn(z)]−E pn(θ)[H[pn(z|θ)]]
Figure2 Apopularinterpretationofaleatoricandepistemicuncertaintyinmachinelearningattachesmultiplemathematicalquantities
toeachofthetwoconcepts,renderingitincoherentandthusalikelysourceofconflationsintheliterature.Hereweshowquotationsfrom
Kendall&Gal(2017)expressedmathematicallyasinformation-theoreticquantities,alongwithaninterpretationofEquation1duetoGal
(2016)andGaletal(2017).Someofthequantitiesshowncancoincideinparticularcasesbutinthegeneralcasetheyaredistinct.
weak. Onebasicreasonforthisisthattheymightbedefined etal(2017)madetheexplicitlinktoEquation1,informed
over different event spaces. We could for example have byHoulsbyetal(2011).Kendall&Gal(2017)discussedthe
y ̸∈Z: perhapswewanttopredictacoin’sbiasbasedon aleatoric-epistemicviewinthecontextofcomputervision.
i
outcomesofcointosses,orwewanttopredictavariablein
While that work successfully captured some of the intu-
onedomain(eg,vision)basedondatafromanotherdomain
itionsfromSection2,wehighlightthatitalsooverloaded
(eg,text). Evenifthatisnotthecase,p (z)isareflection
n theideasofaleatoricandepistemicuncertaintywithmulti-
ofassumptionsanddesigndecisionsbasedonincomplete
plemeanings,introducinganumberofspuriousassociations
knowledge(Box,1976;Kleijn&vanderVaart,2006),and
(Figure 2). The competing definitions of aleatoric uncer-
thereisnogeneralguaranteethatitwillmatchreality.
taintyconflateH[p (z)],theentropyofp (z)asn → ∞
∞ n
(this depends on the data-generating process, as we will
3.7 Modelevaluationreliesonexternalgrounding
discussinSection5.2),withthreeseparatequantities:
Becauseweexpectp (z)tobeimperfect,weoftenwantto
n
(a) H[p (y |π)], the entropy in training-data gener-
assessitagainstaground-truthrealisationofzorareference train 1:n
ation. Issue: p (z) represents subjective predictive
distribution,p (z). Commonlythisdistribution—which ∞
eval
beliefsthatneednotmatchp (y |π)(Section3.6).
couldforexamplerepresentacomputerprogram,ahuman train 1:n
expertoraphysicalsensor—isusedassourceofevaluation (b) H[p (z)],theentropyinevaluation-datageneration.
eval
dataforcomputinganestimatoroffrequentistrisk(Berger, Issue: p (z)representssubjectivepredictivebeliefs
∞
1985), such as the mean squared error. Notably p eval (z) thatneednotmatchp eval (z)(Sections3.6and3.7).
could itself be imperfect (Fluri et al, 2023), so designing
(c) E [H[p (z|θ)]], the expected conditional predic-
andinterpretingevaluationsofthisformrequirescare. pn(θ) n
tiveentropy.Issue:forfinitentheexpectedconditional
predictive entropy is only an estimator of H[p (z)],
∞
4 Assessingapopularview
anditcanbehighlyinaccurate(Section5.5).
Havingoutlinedintuitivedescriptionsofaleatoricandepis- Meanwhilethemultipledefinitionsofepistemicuncertainty
temic uncertainty and their motivation in Section 2, we mixupH[p (z)]−H[p (z)],thepredictive-entropyreduc-
n ∞
turntohowtheyhavebeenformalisedinmachinelearning. tionfromupdatingoninfinitenewdata,withtwoquantities:
Aleatoricandepistemicuncertaintyareoftenthoughtofas
(a) H[p (θ)],theentropyofthemodel’sstochasticparame-
additivecomponentsofpredictiveuncertainty. Apopular n
ters.Issue:themappingfromparameterstopredictions
waytoformalisethisformodelswithstochasticparameters,
istypicallynotinvertible,soH[p (θ)]willnotneces-
θ,istorelatethreeinformation-theoreticquantities: n
sarilyrelatetothereductioninpredictiveentropy.
E
|
I
{
G
z
θ
}
= H
|
[p
{
n
z
(z)
}
]−E
|
pn(θ) [H
{
[
z
p n (z|θ)]
}
] (1) (b) H[p
n
(z)]−E
pn(θ)
[H[p
n
(z|θ)]],theexpectedinforma-
“epistemic” “total” “aleatoric” tiongaininthemodelparameters. Issue: forfiniten
thisEIGisonlyanestimatorofH[p (z)]−H[p (z)],
whereHdenotesShannonentropyandEIG ,alsoknown n ∞
θ andtheestimationerrorcanbelarge(Section5.5).
astheBALDscore(Houlsbyetal,2011),istheexpected
informationgaininθfromobservingz. Gal(2016)stated Othersourcesofconfusioninthisaleatoric-epistemicview
the“total=aleatoric+epistemic”relationshipandthecor- includeanincorrectassociationbetweenamodel’ssubjec-
respondencebetweenp (z)andtotaluncertainty,whileGal tiveuncertaintyandfrequentistmeasuresofperformance,
n
4

RethinkingAleatoricandEpistemicUncertainty
suchasclassificationaccuracy(Figure2inKendall&Gal dependingontheirdecisionsofinterestandlossfunctions.
(2017)), along with misleading implications about how a Onemightusevariance(Hastieetal,2009)whiletheother
model’suncertaintywillbehavewithvaryingn(Figure6.11- usesentropy(Shannon,1948),asExamples1and2show.
6.12inGal(2016)andTable3inKendall&Gal(2017))and
varyingdistancefromthetrainingdata(“Aleatoricuncer- Example1(Dawid,1998) PointpredictionwithA = Z
|     |     |     |     |     |     | and | ℓ(a,z) | = (a−z)2 | corresponds |     | to measuring | uncer- |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----------- | --- | ------------ | ------ |
taintydoesnotincreaseforout-of-dataexamples...whereas
epistemicuncertaintydoes”inKendall&Gal(2017)). taintyinourbeliefs,p (z),usingvariance.
n
|     |     |     |     |     |     | Proof | Theoptimalactionisthemeanofp |     |     |     | n (z): |     |
| --- | --- | --- | --- | --- | --- | ----- | ---------------------------- | --- | --- | --- | ------ | --- |
5 Analternativeperspective
(cid:2) (a−z)2(cid:3)
|     |     |     |     |     |     |     | a∗ =argmin |     | E         |     | =E    | [z]. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | ----- | ---- |
|     |     |     |     |     |     |     | n          |     | a∈A pn(z) |     | pn(z) |      |
Wenowpresentacoherent,generalsynthesisofkeyideas
usedinexistingdiscussionsofaleatoricandepistemicuncer- The subjective expected loss of taking this action is the
| tainty(Figure1). | Webeginbyreasoningaboutthesubjec- |     |     |     |     | varianceofp |     | n (z): |     |     |     |     |
| ---------------- | --------------------------------- | --- | --- | --- | --- | ----------- | --- | ------ | --- | --- | --- | --- |
tiveexpectedlossofactingBayes-optimallyunderagiven
|     |     |     |     |     |     |     |     |     | (cid:2) [z]−z)2(cid:3) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
beliefstate,whichleadstoadecision-groundedmeasureof h[p (z)]=E (E =V [z].
|                        |     |                              |     |     |     |         | n   | pn(z) | pn(z)         |     | pn(z)      |      |
| ---------------------- | --- | ---------------------------- | --- | --- | --- | ------- | --- | ----- | ------------- | --- | ---------- | ---- |
| predictiveuncertainty. |     | Bythinkingabouthowthatuncer- |     |     |     |         |     |       |               |     |            |      |
|                        |     |                              |     |     |     | Example |     | 2     | Probabilistic |     | prediction | with |
taintywillchangeinlightofnewdata,wethenidentifya (Dawid, 1998)
|     |     |     |     |     |     | A   | = P(Z)andℓ(a,z) |     | = −loga(z)correspondstomea- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------------------- | --- | --- | --- |
notionofexpecteduncertaintyreduction,whichweuseto
|                                                     |     |     |     |     |     | suringuncertaintyinourbeliefs,p |     |     |     | (z),usingentropy. |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ----------------- | --- | --- |
| defineadecompositionofuncertaintyintoirreducibleand |     |     |     |     |     |                                 |     |     |     | n                 |     |     |
reduciblecomponents,andwhichalsohasdirectpractical
|     |     |     |     |     |     | Proof | Theoptimalactionisp |     |     | (z): |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------------------- | --- | --- | ---- | --- | --- |
n
| relevance. | Then,shiftingourfocustoexternallygrounded |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
evaluation,wehighlightthedistinctionbetweenuncertainty, a∗ =argmin −E [loga(z)]=p (z).
|                                         |     |     |     |              |     |     | n   |     | a∈A pn(z) |     | n   |     |
| --------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --------- | --- | --- | --- |
| predictiveperformanceanddatadispersion. |     |     |     | Finallywere- |     |     |     |     |           |     |     |     |
turntotheBALDscorediscussedinSection4,providing The subjective expected loss of taking this action is the
insightsonitsutilityasadata-acquisitionobjective. Shannonentropyofp (z):
n
(z)]=−E
5.1 Predictiveuncertaintycanbederivedfromthe h[p n pn(z) [logp n (z)]=H[p n (z)].
finaldecisionofinterestandtheassociatedloss
5.2 Decomposingpredictiveuncertaintyrequires
Wefirstdealwiththequestionofhowtomeasurepredictive
uncertainty,towhichmanydifferentanswershavebeenput accountingforthedata-generatingprocess
| forward(Sections1and2). |     |     | Revisitingpastwork,weshow |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Next,toformalisethepopularideaofdecomposingpredic-
| that minimising | subjective |     | expected | loss (Ramsey, | 1926; |     |     |     |     |     |     |     |
| --------------- | ---------- | --- | -------- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
tiveuncertaintyintoirreducibleandreduciblecomponents
| Savage, | 1951) directly | leads | to  | a loss-grounded | measure |     |     |     |     |     |     |     |
| ------- | -------------- | ----- | --- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
(Sections2and4),wereasonabouthowpredictiveuncer-
of uncertainty that reflects our preferences about model taintychangesinlightofnewdata. Weshowthat,aslong
| behaviourinthefinaldecisionofinterest. |     |     |     | Wethusclarify |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
asweexplicitlyaccountforthedata-gatheringprocess,we
thatadecision-makerdoesnotfaceanarbitrarychoiceover
canwritedownanotionofexpecteduncertaintyreduction
| uncertaintymeasures: |     | iftheyspecifyalossfunctionbased |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thatiswelldefinedforanymethodthatmapsfromdatatoa
ontheirpreferences,arigorousuncertaintymeasurefollows.
|     |     |     |     |     |     | predictivedistribution(Section3.4). |     |     |     | Fromthisweidentify |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ------------------ | --- | --- |
arigorousirreducible-reducibledecomposition.
Ifp (z)representsourbeliefsoverzthenwecanidentify
n
theBayes-optimalaction,a∗,inourfinaldecisionofinterest
|     |     |     | n   |     |     | Characterisingthereducibilityofuncertaintyinitiallyseems |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
byminimisingtheexpectedlossunderthosebeliefs: assimpleasconsideringnewdata, y+ = y ,
|     |     |     |     |     |     |     |     |     |     | 1:m | (n+1):(n+m) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
andmeasuringthecorrespondinguncertaintyreduction,
|                                                | a∗ =argmin |     | E         | [ℓ(a,z)]. | (2) |     |     |       |                |     |       |     |
| ---------------------------------------------- | ---------- | --- | --------- | --------- | --- | --- | --- | ----- | -------------- | --- | ----- | --- |
|                                                | n          |     | a∈A pn(z) |           |     |     |     |       |                |     |       |     |
|                                                |            |     |           |           |     |     | UR  | (y+   | )=h[p (z)]−h[p |     | (z)], |     |
| Nowwecanreasonaboutthelossweexpect(underourbe- |            |     |           |           |     |     |     | z 1:m | n              |     | n+m   |     |
liefstate)toincurbytakingthisBayes-optimalaction. An whichwenotecouldbenegative. Butthisuncertaintyreduc-
important,underappreciatedresultisthatthisminimalex-
tiondependsonexactlywhatthenewdatais,andthatinturn
| pectedlossprovidesawaytomeasureuncertaintyinp |     |     |     |     | (z) |                                               |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                               |     |     |     |     | n   | dependsontheprocessbywhichthedataisgenerated. |     |     |     |     |     | We  |
(Dawid,1998;DeGroot,1962;Neiswangeretal,2022):
thereforeneedtoexplicitlyaccountforthedata-generating
processtoproduceawell-definednotionofreducibility.Any
|     | h[p | (z)]=E |     | [ℓ(a∗,z)]. |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
n pn(z) n stochasticityinmodelupdatingalsohastobetakenintoac-
count,butthiscanbeachievedbyabsorbingtheupdating
Acrucialimplicationofthisisthatanytwodecision-makers
|        |                 |        |      |             |          | stochasticityintothedefinitionofy+ |     |     |     |     | (Section3.4). |     |
| ------ | --------------- | ------ | ---- | ----------- | -------- | ---------------------------------- | --- | --- | --- | --- | ------------- | --- |
| should | not necessarily | usethe | same | uncertainty | measure, |                                    |     |     |     | 1:m |               |     |
5

RethinkingAleatoricandEpistemicUncertainty
Revisitingthedata-generatingprocessfromSection3.4,we thiswemightalsoneedtoapproximatehowourbeliefsover
definethedistributionovery+todependondecisionsmade zupdatewhenweobtainnewdata. InprincipletheEURis
i
bythedata-acquisitionpolicy,π,andonthepreviousdata: definedwithrespecttowhicheverupdatingschemeweare
using,butinpracticethetrueupdatecanbetooexpensive
m
Y
p (y+ |π)= p (y+|π(y ),y ). toperformwithinanexpectationovernewdata. Thiscan
train 1:m train i <i <i
beaddressedbyusingsomeq (z)inplaceofp (z).
i=1 n+m n+m
AcommonapproachistoassumeaBayesianbeliefupdate
Withthiswecandefinethetrueexpecteduncertaintyreduc-
giveny+ ,evenifthetrueupdateisnotBayesian(Bickford
tion(EUR)inzunderagivenpolicy,π,as 1:m
Smithetal,2023;2024;Galetal,2017;Kirschetal,2019;
EURtrue(π,m)=E [UR (y+ )]. (3) 2023). It might be, for example, that we want to use a
z ptrain(y 1 + :m |π) z 1:m Bayesianmodelbutcannotperformexactinference. Ifthe
This allows us to shift from thinking about a specific re- trueupdateisBayesianandcanbeperformedexactlythen
alisation of data to the range of possible data that might thisassumptionisofcoursenotanapproximation.
be generated. Working from this EUR to an uncertainty
Combiningmodel-baseddatasimulationwithanapproxi-
decomposition,weconsiderthelimitofm→∞:
mateupdatingscheme,wecanestimatethetrueEURusing
E | URt z r { u z e(π,∞ } )=h | [p { n z (z) } ]−E | ptrain(y 1 + :∞ { |π z ) [h[p ∞ (z)] } ]. EURe z st(π′,m)=h[p n (z)]−E pn(y 1 + :m |π′) [h[q n+m (z)]].
reducible total irreducible
The accuracy of this estimator depends on the mismatch
Thus we see that three components—a loss function, a betweenp (y+ |π′)andp (y+ |π)aswellasthemis-
n 1:m train 1:m
machine-learningmethodmappingfromdatatoapredictive matchbetweenq (z)andp (z),bothofwhichare
n+m n+m
distribution,andadata-acquisitionpolicy—fullyspecifya likelytobegreaterforlargerm. Estimationthereforere-
rigorousmeasureofexpecteduncertaintyreductionandan quirescarefultradeoffstomitigatethesemismatches.
associatedirreducible-reducibledecomposition. Thiscon-
Thepracticalrelevanceofthisbecomescleareruponappre-
trastswiththedecompositioninEquation1,whichrequires
ciatingthattheEURestimatorgeneralisesanumberofexist-
stochasticmodelparametersandexactBayesianupdating.
ingdata-acquisitionobjectives. Undertheexact-Bayesian-
Itisworthnotingthatinsomerestrictedcasesthedepen- updatingassumptionitisequivalenttowhathasvariously
dencyonthedata-acquisitionpolicy,π,oftheinfinite-data beencalledthe“expectedvalueof[additional/sample]in-
termsinthisuncertaintydecompositioncandisappear. For formation”(Bernardo&Smith,1994;Raiffa&Schlaifer,
example,ifweareinasupervised-learningsettingwhere 1961),the“expectedH -informationgain”(Neiswanger
ℓ,A
thepolicy’sdecisionsconcernwhichinputstoacquirelabels etal,2022)andthe“expecteddecisionutilitygain”(Huang
for,andifweareusingawell-specifiedBayesianmodeland etal,2024). Fromthatobjectivewecanthenrecoverthe
exactBayesianupdating,p (z)shouldbeindependentofπ expectedinformationgaininz,whichcorrespondstothe
∞
aslongasπproducesdensesamplesacrosstheinputspace BALDscore(Galetal,2017;Houlsbyetal,2011)ifz =θ
(Kleijn&vanderVaart,2012). However,therequirements representsasetofstochasticmodelparameters,ortheex-
forthisareverystrict,withanymodelmisspecificationor pected predictive information gain (Bickford Smith et al,
errorinbeliefupdatingreintroducingthedependency. 2023)ifz =(x ,y )representsatargetinputanditsoutput.
∗ ∗
NotablyEURest(π′,m)isalsocloselyrelatedtotheideaof
z
5.3 Practicalestimationofexpecteduncertainty themartingaleposterior(Fongetal,2023)asp (y+ |π′)
n 1:m
reductionreliesonapproximations andourupdatingschemetogetherimplyajointdistribution
fromwhichamartingaleposteriorcanbederived.
Nowweturntoestimatingexpecteduncertaintyreduction
(EUR) in practice. The decomposition in Section 5.2 is
5.4 Model-baseduncertaintyshouldbeusedwithcare,
well defined but the infinite-data quantities within it are
andexternallygroundedevaluationiscrucial
typicallynotpracticallyobtainable. Whilethismightseem
problematic,wesuggestthetakeawayshouldinfactbeto Nextweclarifytherelationshipbetweenthepredictiveun-
deemphasisethedecompositioninthecontextofreal-world certaintywehavediscussedsofarandquantitiescommonly
machinelearning,wherewedonothaveinfinitedata. There associatedwithit(Sections2and4): measuresofpredictive
is more concrete value (eg, for data acquisition or model performanceanddatadispersion. Weidentifyhowamodel
selection)inestimatingtheEURinEquation3forfinitem, couldbeusedtoestimatethosequantitiesbutemphasisethe
whichreliesonsomeimportantpracticalapproximations. limitationsofthatapproach,underliningthekeyroletobe
playedbyexternallygroundedevaluation(Section3.7).
Since we typically do not know the true data-generating
process, p (y+ |π), a core approximation is to use a Weconsiderassessingapredictivedistribution,p (z),either
train 1:m n
modelovernewdata, p (y+ |π′), asaproxy. Ontopof usingasingleground-truthvalueofzorusingareference
n 1:m
6

RethinkingAleatoricandEpistemicUncertainty
1
0
1
−
5 0 5
− x
z
Data,referencedistribution
andpredictivedistribution
1.0
0.5
0.0
5 0 5
− x
eulaV
Uncertaintyandevaluation
withloss‘(a,z)=(a z)2
−
0.2
0.0
5 0 5
− x
eulaV
Uncertaintyandevaluationwith
loss‘(a,z)=max(0,z) (a z)2
· −
trainingdata
referencemean
predictivemean
predictiveuncertainty
datadispersion
expectedscore
Figure3 Model-baseduncertainty,predictiveperformanceanddatadispersionarerelatedbutdistinctquantities. Hereweshowa
model’spredictivedistributionoveranoutput,z∈R,correspondingtoaninput,x∈R;wealsoshowareferencedistributionservingas
asourceofevaluationdata.Usingthemodelalone,wecomputeameasureofpredictiveuncertaintyusingalossfunction,ℓ(a,z),where
aisanaction. Thisdiffersfromthedatadispersion,whichdescribesthereferencedistribution. Connectingthetwodistributions,the
expectedscore(lowerisbetter)measuresthepredictiveperformanceofthemodelasjudgedusingdatafromthereferencedistribution.
distributionoverz. Ifwehaveasinglez,wecanevaluate Proposition1(Berger,1985) LetF beaquantityofinterest,
p (z)usingaproperscoringrule(Savage,1971)oftheform and let f(θ) represent subjective beliefs over F, derived
n
fromapushforwardofadistributiononmodelparameters
s(p ,z)=ℓ(a∗,z)
n n θ ∼p (θ). Underaquadraticestimationloss,ℓ (η,θ)=
n η
wherea∗
n
isdefinedasinEquation2(Dawid,1998). This (η−f(θ))2,theBayesestimatorofF isη∗ =E pn(θ) [f(θ)].
scoringrulemeasuresthelossincurredbytheBayes-optimal
Proposition2 Assumep (z)=E [p (z|θ)]isamodel
actionunderp
n
(z)whenthegroundtruthisz.
intendedtodirectlyappro
n
ximatep
pn(θ
(
)
z).
n
Thenthemodel’s
eval
Ifweinsteadhaveareferencedistribution,p (z),wecan predictive uncertainty, h[p (z)], is a Bayes estimator of
eval n
evaluatep (z)usingadiscrepancyfunction(Dawid,1998): E [s(p ,z)], the expected loss from acting Bayes-
n peval(z) n
optimallyunderp (z)whenzisinfactdrawnfromp (z).
d(p ,p )=E [ℓ(a∗,z)−ℓ(a∗ ,z)] (4) n eval
n eval = | E p p e e v v a a l l ( ( z z ) ) { [ z s(p n n ,z) } ] − h | e [ v p a e l { va z l (z) } ] (5) P an r d oo f f (θ A ) p = p E ly p in n g (z P |θ r ) o [ p s( o p si n ti , o z n )] 1 g w iv i e th s F η∗ = = E h p [ e p v n al ( (z z ) ) [ ] s . (p n ,z)]
expectedscore datadispersion
Proposition 3 Assume the same model as in Proposi-
wherea∗ isdefinedanalogouslytoa∗ butwithp (z)
eval n eval tion2. Thentheexpectedconditionalpredictiveuncertainty,
as the predictive distribution. Equation 4 highlights that
E [h[p (z|θ)]],isaBayesestimatorofh[p (z)],the
the discrepancy is the expected excess loss from acting pn(θ) n eval
dispersionindatadrawnfromareferencedistribution.
based on p (z) rather than p (z) when p (z) repre-
n eval eval
sentsthegroundtruth,whichislinkedtotheideaofregret Proof Applying Proposition 1 with F = h[p (z)] and
eval
(Szepesva´ri,2010). Equation5showsthatthediscrepancy f(θ)=h[p (z|θ)]givesη∗ =E [h[p (z|θ)]].
n pn(θ) n
alsocorrespondstotheexpectedscoreofp (z),whichmea-
n
sures predictive performance (lower is better), minus the ThreethingsareimportanttonoteinregardtoPropositions2
uncertaintymeasurefromSection5.1appliedtop (z), and3. First,whiletheybothsupposethatp (z)isdesigned
eval n
whichmeasuresthestatisticaldispersioninevaluationdata to directly approximate p (z), this need not always be
eval
drawnfromthereferencedistribution.Thisrelationshipgen- the case. Because p (z) might itself be imperfect, our
eval
eralisesclassicdecompositionsfromstatistics(Rice,2007) evaluationmightjustbeservingtoprovidearoughsignalof
andinformationtheory(Cover&Thomas,2005),asshown themodel’spredictiveperformance(Section3.7). Second,
in Examples 3 and 4. Notably the expected score can be theybothassumeaquadraticestimationloss,whichmight
seen as a form of frequentist risk for an “outer” decision notreflectourpreferences. Analternativelosswouldresult
problem;anotherformalsoaveragesoverthetrainingdata. in different Bayes estimators. For example, an absolute
losswouldleadustousemediansratherthanexpectations
Becausepastworkhassometimesdrawnconnectionsbe-
(Berger,1985). Third,theypresentestimatorsthatarede-
tweenmodel-baseduncertainty,predictiveperformanceand
rivedfromsubjectivemodelsandthat,asaresult,haveno
datadispersion,wenowexplainhowsuchconnectionscan
accuracyguaranteeinthegeneralcase(Section3.5).
comeaboutandwhyinthegeneralcasetheyshouldnotbe
takentohold. Inparticular,ifweassumeaspecificmodel We therefore stress that model-based uncertainty should
setupandestimationlossthenwecanderiveBayesestima- be considered separate from predictive performance and
torsthatgeneralisethemarginalpredictiveentropyandthe data dispersion, as shown in Figure 3 (see Appendix C
expectedconditionalpredictiveentropyinEquation1,but for details). Uncertainty alone is not a reliable indicator
theseassumptionswilltypicallynotapplyand,evenifthey of whether we can trust a model. Some kind of external
doapply,theestimatorscanbehighlyinaccurate. groundingiscrucialforwell-informedpracticaldeployment.
7

RethinkingAleatoricandEpistemicUncertainty
|     |     | EIGerrorsfordiscretedata |     |     |     |     |     | Predictivedistributionsfordiscretedata |     |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
)2stan(rorrederauqS
|     |     | 0.002 |     | εz  | 0.6     |     |     |     |     |     |     |     | n=100 |     |
| --- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
|     |     |       |     | εθ  | )1=z(np |     |     |     |     |     |     |     |       |     |
n=101
|     |     |     |     |     | 0.5 |     |     |     |     |     |     |     | n=102 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
0.001
n=103
0.4
n=
|     |     | 0.000                      |         |     | 0.3 |     |     |                                          |                   |     |     |     | ∞   |     |
| --- | --- | -------------------------- | ------- | --- | --- | --- | --- | ---------------------------------------- | ----------------- | --- | --- | --- | --- | --- |
|     |     | 100                        | 101 102 | 103 |     |     | 10  | 20                                       |                   | 30  | 40  | 50  |     |     |
|     |     | Numberofexamples,n         |         |     |     |     |     |                                          | Random-numberseed |     |     |     |     |     |
|     |     | EIGerrorsforcontinuousdata |         |     |     |     |     | Predictivedistributionsforcontinuousdata |                   |     |     |     |     |     |
)2stan(rorrederauqS
|     |     | 0.6 |     | εz  |     | 5   |     |     |     |     |     |     | p100(z) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
|     |     |     |     | εθ  |     |     |     |     |     |     |     |     | p101(z) |     |
0.4
|     |     |     |     |     | z   |     |     |     |     |     |     |     | p102(z) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
0
|     |     | 0.2                |         |     |     |     |     |     |                   |     |     |     | p103(z) |     |
| --- | --- | ------------------ | ------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ------- | --- |
|     |     |                    |         |     |     |     |     |     |                   |     |     |     | p (z)   |     |
|     |     | 0.0                |         |     |     |     |     |     |                   |     |     |     | ∞       |     |
|     |     | 100                | 101 102 | 103 |     | 1   | 2 3 | 4 5 | 6                 | 7 8 | 9   | 10  |         |     |
|     |     | Numberofexamples,n |         |     |     |     |     |     | Random-numberseed |     |     |     |         |     |
Figure4 BALD’scorrespondencewithinfinite-steppredictiveinformationgain(amodel’slong-runreductioninpredictiveentropy)can
beweak,suchthatitisoftenbetterthoughtofasanestimatorofa“true”one-stepexpectedinformationgaininthemodelparameters.
Hereweshowthebehaviourofconjugatemodelstrainedondiscrete(top)andcontinuousdata(bottom).Forn∈(1,10,100,1000)we
|     |     |     |     |     |     |     | ))2andε |     | −EIGtrue)2. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- |
computedtwoestimationerrors: ε z =(EIG θ −IG z (y+ θ =(EIG θ Weshowtheseerrors(left;meanover
|     |     |     |     |     |     |     | 1:∞ |     |     | θ   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50random-numberseeds)alongwiththeevolutionofthepredictivedistribution(right).Bothestimationerrorsareduetoinaccurately
simulatingfuturedata,anissuethatresolvesasnincreasesandthepredictivedistributionconvergestothedata-generatingprocess.
5.5 Popularinformation-theoreticquantitiesarebest parameters,EIG ,fromobservingz isaBayesestimator
θ
understoodasimperfectestimators oftheinfinite-steppredictiveinformationgain,IG z (y+ ).
1:∞
Finallywereturntotheinformation-theoreticquantitiesin
|     |     |     |     |     |     |     |     | InFigure4wedemonstratethattheapproximationEIG |     |     |     |     |     | ≈   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
θ
Equation1,whichhavebeencentraltomanyexistingdis- IG (y+ )fromProposition5canbecoarse. Theseresults
z 1:∞
| cussionsofaleatoricandepistemicuncertainty. |     |     |     |     |     | Principally |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
wereproducedwithextremelysimplesetupswithinwhich
| we  | highlight | that BALD | (that | is, EIG | ,   | the expected | in- |                                                 |     |     |     |     |     |     |
| --- | --------- | --------- | ----- | ------- | --- | ------------ | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |           |           |       |         | θ   |              |     | wecanperformexactinferenceandwearesuretorecover |     |     |     |     |     |     |
formationgaininasetofstochasticmodelparameters,θ)
thetruedata-generatingprocessinthelimitofinfinitedata
canbeunderstoodasanestimatoroftwoseparateunknown
|     |     |     |     |     |     |     |     | (seeAppendixCfordetails). |     |     |     | Wethereforeknowthatthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ---------------------- | --- | --- |
quantities: theinfinite-stepinformationgaininthemodel estimationerrorisduetoafailureofthemodeltoaccurately
predictionsanda“true”one-stepexpectedinformationgain
simulatefuturedata,whichinturnisduetonbeingfinite.
| inthemodelparameters. |     |     | Wealsosuggesttherelativemag- |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisbehaviourappearstoalignwithexistingresults(with
nitudesofthetwocorrespondingestimationerrorsmight
helpexplainBALD’sutilityasadata-acquisitionobjective. thecaveatthatpaststudiesdidnotmatchtheassumptions
|     |     |     |     |     |     |     |     | ofPropositions4and5). |     |     | Figure2inBickfordSmithetal |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------------------------- | --- | --- | --- |
Firstweshowthat,underassumptionsonthedataandmodel
(2024)andFigure5inWimmeretal(2023)showsmall-nes-
| that | result | in convergence | to  | a single | setting | of  | θ (Doob, |              |     |                                         |     |     |     |     |
| ---- | ------ | -------------- | --- | -------- | ------- | --- | -------- | ------------ | --- | --------------------------------------- | --- | --- | --- | --- |
|      |        |                |     |          |         |     |          | timatesofEIG |     | thatdiffersubstantiallyfromthechangesin |     |     |     |     |
θ
1949;Freedman,1963;1965),BALDcanbeunderstoodas predictiveentropythatactuallyoccurredinpractice. Those
anestimatoroftheinfinite-steppredictiveinformationgain,
resultsevensuggestitwouldhavebeenmoreaccurateto
|     |     |           |          |     |       |     |     | assumeIG                 | (y+ | ) = | H[p (z)], | withH[p | (z|y+ | )] = 0, |
| --- | --- | --------- | -------- | --- | ----- | --- | --- | ------------------------ | --- | --- | --------- | ------- | ----- | ------- |
|     | IG  | (y+ )=H[p | (z)]−H[p |     | (z|y+ | )], |     |                          | z   | 1:∞ | n         |         | n     | 1:∞     |
|     |     | z 1:∞     | n        |     | n     | 1:∞ |     | thantoestimateitusingEIG |     |     |           |         |       |         |
θ . MeanwhileMucsa´nyietal
|     |     |     |     |     |     |     |     | (2024) | and Valdenegro-Toro |     |     | & Saromo-Mori |     | (2022) em- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------- | --- | --- | ------------- | --- | ---------- |
measuringthereductioninthemodel’spredictiveentropy
|                                         |     |     |     |     |     |     |     | phasised | the | “entanglement” |     | of aleatoric- | and | epistemic- |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | ------------- | --- | ---------- |
| fromaBayesianupdateoninfinitenewdata,y+ |     |     |     |     |     |     | .   |          |     |                |     |               |     |            |
1:∞
uncertaintyestimators,whichcanbeunderstoodastheesti-
Proposition4 Lety+ andp (y|θ)p (z|θ)p (θ)beacom- matorsthemselveshavingan“epistemic”component—or,
|     |     | 1:m |     | n   | n   | n   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inourterminology,beinginaccuratefinite-dataestimators.
binationofdatasequenceandgenerativemodelthatyield
| p (θ|y+ | )→δ | (θ)asm→∞. |     |     | Thentheexpectedcon- |     |     |                                                |     |     |     |     |     |     |
| ------- | --- | --------- | --- | --- | ------------------- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
| n       | 1:m | θ∞        |     |     |                     |     |     | ThisraisesthequestionofwhyBALDhasprovenpracti- |     |     |     |     |     |     |
ditionalpredictiveentropy,E
pn(θ) [H[p n (z|θ)]],isaBayes callyusefulasadata-acquisitionobjectiveinactivelearning
| estimatorofH[p                           |     | (z|y+ | )],themarginalpredictiveentropy |     |     |     |     |                                                       |     |     |     |     |     |     |
| ---------------------------------------- | --- | ----- | ------------------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                          |     | n     | 1:∞                             |     |     |     |     | (Galetal,2017;Houlsbyetal,2011;Osbandetal,2023).      |     |     |     |     |     | If  |
| afteraBayesianupdateoninfinitenewdata,y+ |     |       |                                 |     |     |     | .   |                                                       |     |     |     |     |     |     |
|                                          |     |       |                                 |     |     | 1:∞ |     | ourintuitionisthatBALD’sutilitystemsfromitscorrespon- |     |     |     |     |     |     |
dencewithinfinite-steppredictiveinformationgain(thatis,
| Proposition5 |     | AssumethedataandmodelfromProposi- |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
along-runreductioninamodel’spredictiveentropy)and
| tion | 4. Then | the expected | information |     | gain | in the | model |     |     |     |     |     |     |     |
| ---- | ------- | ------------ | ----------- | --- | ---- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
8

RethinkingAleatoricandEpistemicUncertainty
CuratedMNIST CoarseImageNet interestisawell-motivatedobjectivefordataacquisition,
doohilekilgol.gentseT
assumingtheactionofinterestisaprobabilisticprediction
random
|     |     |     |     | entropy 1.5 |     |     |     |          |        |                           |     |     |               |
| --- | --- | --- | --- | ----------- | --- | --- | --- | -------- | ------ | ------------------------- | --- | --- | ------------- |
|     | 1.0 |     |     |             |     |     |     | of z and | we use | a negative-log-likelihood |     |     | loss function |
BALD
(Example2),butitalsocruciallydependsonthemodel’s
1.0
|     | 0.5 |                |     |     |     |                |      | abilitytosimulatefuturedata,anditassumesaBayesian |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | -------------- | ---- | ------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |                |     | 0.5 |     |                |      | updatethatmightnotmatchthetrueupdate(Section5.3). |     |     |     |     |     |
|     |     | 0 100          | 200 | 300 | 0   | 500            | 1000 |                                                   |     |     |     |     |     |
|     |     | Numberoflabels |     |     |     | Numberoflabels |      |                                                   |     |     |     |     |     |
6 Conclusion
| Figure | 5   | BALD | outperforms |     | predictive | entropy | as a data- |     |     |     |     |     |     |
| ------ | --- | ---- | ----------- | --- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
acquisitionobjectiveinactivelearning,eventhoughBALDtends Wehavearguedthatthealeatoric-epistemicviewonuncer-
tobeaworseestimatoroflong-runpredictiveinformationgainin
taintydoesnotservemachine-learningresearchers’needs:
thesetupsstudied.Theseresultswereproducedusingexperimen-
itslackofexpressivecapacityhasledtoconceptualover-
talsetupsdescribedinBickfordSmithetal(2023;2024).
|     |     |     |     |     |     |     |     | loadingandconfusion. |     | Toaddressthiswehavepresenteda |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------------------------- | --- | --- | --- |
decision-theoreticviewthatunifiesmanyconceptsofinter-
|     |     |     |     |     |     |     |     | esttoresearchers. |     | Thisprovidesclarityonfivekeypoints: |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------------------------------- | --- | --- | --- |
weconsidersetupsinwhichthecurrentpredictiveentropy
| is  | a better | estimator | than | BALD, | then | we would | expect |     |     |     |     |     |     |
| --- | -------- | --------- | ---- | ----- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- |
(a) Measuresofpredictiveuncertaintyneednotbeanarbi-
thatusingthepredictiveentropyasadata-acquisitionobjec-
trarychoicebutcaninsteadbederivedfromadecision
tivewouldleadtobetterpredictiveperformanceinactive
ofinterestwithanassociatedlossfunction.
learning. Yetthisisnotwhatweseeinpractice(Figure5).
(b) Ifweexplicitlyaccountforhowtrainingdataisgener-
| We  | suggest | another | perspective |     | on BALD | might | address |     |     |     |     |     |     |
| --- | ------- | ------- | ----------- | --- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
ated,wecanidentifyadecompositionofuncertainty
| thisquestion. |     | Inparticularitcanbeunderstood(givenas- |     |     |     |     |     |      |           |     |             |            |         |
| ------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | ---- | --------- | --- | ----------- | ---------- | ------- |
|               |     |                                        |     |     |     |     |     | into | reducible | and | irreducible | components | for any |
sumptionsonthedataandmodel)asanestimatorofthetrue
methodthatmapsfromdatatoapredictivedistribution.
one-stepexpectedinformationgaininthemodelparameters,
(c) Inpracticewecantypicallyonlyproduceanapprox-
|     | EIGt | rue =H[p |     | (θ)]−E |     | [H[p (θ|z)]], |     |     |     |     |     |     |     |
| --- | ---- | -------- | --- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
θ n ptrain(z) n imate notion of expected uncertainty reduction that
reliesonaproxyforthetruedata-generatingprocess
| where | the | expectation |     | is over | observations | from | the true |     |     |     |     |     |     |
| ----- | --- | ----------- | --- | ------- | ------------ | ---- | -------- | --- | --- | --- | --- | --- | --- |
andpossiblyalsoanapproximationofmodelupdating.
data-generatingprocess,notmodel-simulatedobservations.
(d) Predictiveuncertaintyshouldbeassumedtobesepa-
Proposition6 Letz =y . Assumey areindependent ratefrommeasuresofpredictiveperformanceanddata
|     |     |     |     | n+1 |     | 1:n |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andidenticallydistributed,withy i ∼p train (y),andassume dispersion,andexternallygroundedevaluationisthere-
p (z) = E [p (z|θ)] is a model intended to directly forekeyforbuildingtrustinamodel’spredictions.
| n            |     | pn(θ) | n    |                                |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ---- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| approximatep |     |       | (z). | Thentheexpectedinformationgain |     |     |     |     |     |     |     |     |     |
train
(e) BALDdoesnotdirectlymeasurelong-runreducible
| inthemodelparameters,EIG |     |        |               | ,fromobservingzisaBayes |          |             |       |                                                  |     |     |     |     |     |
| ------------------------ | --- | ------ | ------------- | ----------------------- | -------- | ----------- | ----- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|                          |     |        |               | θ                       |          |             |       | predictiveuncertaintybutratherestimatesit,andthe |     |     |     |     |     |
| estimator                |     | of the | true one-step |                         | expected | information | gain, |                                                  |     |     |     |     |     |
EIGtrue,wheretheexpectationiswithrespecttop associatedestimationerrorcanbelarge.
|     |     |     |     |     |     |     | train (z). |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
θ
Webelieveourdecision-theoreticviewshouldbeusedin
Returningtothesameexperimentalsetupasbefore,wefind
|                                  |     |     |     |       |                      |                |     | place of                                         | the predominant |                                | aleatoric-epistemic |     | view as the |
| -------------------------------- | --- | --- | --- | ----- | -------------------- | -------------- | --- | ------------------------------------------------ | --------------- | ------------------------------ | ------------------- | --- | ----------- |
| (Figure4)thattheapproximationEIG |     |     |     |       |                      | ≈EIGtrueismore |     |                                                  |                 |                                |                     |     |             |
|                                  |     |     |     |       |                      | θ              | θ   | fieldmovesforward.                               |                 | Ourhopeisthatitwillsupportmore |                     |     |             |
| accuratethanEIG                  |     |     | ≈IG | (y+   | ). Inotherwords,BALD |                |     |                                                  |                 |                                |                     |     |             |
|                                  |     |     | θ   | z 1:∞ |                      |                |     | productivediscourseandmethodologicaldevelopment. |                 |                                |                     |     |             |
morecloselytracksshort-runchangesinparameteruncer-
Wealsourgecareinusinguncertaintyandrelatedquantities
taintythanitdoeslong-runchangesinpredictiveuncertainty.
|     |     |     |     |     |     |     |     | inpractice. | Acrucialrecurringpointinthisworkisthattrue |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------------------------ | --- | --- | --- | --- |
Wedonotclaimthisisageneralresultthatwillholdinall
settings,butitisconsistentwithBALDbeingusefulasa quantitiesofinterestalmostalwayshavetobeapproximated
|                            |     |     |     |                               |     |     |     | intherealworld. |     | Ignoringapproximationerrorscanleadto |     |     |     |
| -------------------------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --------------- | --- | ------------------------------------ | --- | --- | --- |
| data-acquisitionobjective. |     |     |     | Thedata-acquisitionhorizonsin |     |     |     |                 |     |                                      |     |     |     |
activelearningaretypicallyveryshort,soitistheshort-run dangerousassumptionsandineffectivemethods.
notionofinformationgainthatmatters,nottheasymptotic Finallywesuggestthatfuturemethodsresearchshouldbe
notion. Andwhiletargetingpredictionsratherthanparame-
|     |     |     |     |     |     |     |     | guided by | practical | utility | in concrete | decision | problems, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | ----------- | -------- | --------- |
terscanbeevenmoreeffective(BickfordSmithetal,2023;
|     |     |     |     |     |     |     |     | such as | data acquisition |     | and model | selection, | rather than |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | --------- | ---------- | ----------- |
2024),maximisingshort-runparameterinformationgainis moreabstractnotionsofapproximationaccuracy.Combined
stilloftenpreferableoverrandomacquisition.
withstrongerconceptualfoundations,arenewedemphasis
onreal-worldperformancecouldaccelerateprogressinthe
Onetakeawayhereisthatinformation-theoreticquantities
should not be confused with the quantities they estimate. useofprobabilisticreasoninginmachinelearning.
Anotheristhatexpectedinformationgaininavariableof
9

RethinkingAleatoricandEpistemicUncertainty
Impactstatement Cover&Thomas(2005). ElementsofInformationTheory.
JohnWileyandSons.
Thispaperpresentsworkwhosegoalistoadvancethefield
of machine learning. There are many potential societal Dawid(1998). Coherentmeasuresofdiscrepancy, uncer-
| consequences | of  | our work, | none | which we | feel must | be  |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
taintyanddependence,withapplicationstoBayesianpre-
specificallyhighlightedhere. dictiveexperimentaldesign. Technicalreport,University
CollegeLondon.
Acknowledgements
|     |     |     |     |     |     |     | DeGroot(1962). | Uncertainty,information,andsequential |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------------------------- | --- | --- | --- | --- |
WethankPhilipDawidforsharingatechnicalreportwith experiments. AnnalsofMathematicalStatistics.
us. WearealsogratefultoAndreasKirsch,MikeOsborne
|     |     |     |     |     |     |     | Doob(1949). | Applicationofthetheoryofmartingales. |     |     |     | Le  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------------------ | --- | --- | --- | --- |
andtheanonymousreviewersofthispaperforusefuldiscus-
CalculdesProbabilite´setsesApplications.
| sionsandfeedback. |     | FreddieBickfordSmithissupported |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bytheEPSRCCentreforDoctoralTraininginAutonomous Fluri, Paleka, & Trame`r (2023). Evaluating superhuman
| Intelligent | Machines | and | Systems | (EP/L015897/1). |     | Tom |     |     |     | arXiv. |     |     |
| ----------- | -------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | ------ | --- | --- |
modelswithconsistencychecks.
RainforthissupportedbyEPSRCgrantEP/Y037200/1.
|     |     |     |     |     |     |     | Fong & Holmes     | (2020).     | On  | the marginal | likelihood | and |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | --- | ------------ | ---------- | --- |
|     |     |     |     |     |     |     | cross-validation. | Biometrika. |     |              |            |     |
References
|                     |             |                               |     |               |      |     | Fong,Holmes,&Walker(2023). |                                            |     | Martingaleposteriordis- |     |     |
| ------------------- | ----------- | ----------------------------- | --- | ------------- | ---- | --- | -------------------------- | ------------------------------------------ | --- | ----------------------- | --- | --- |
| Amini,              | Schwarting, | Soleimany,                    |     | & Rus (2020). | Deep | ev- |                            |                                            |     |                         |     |     |
|                     |             |                               |     |               |      |     | tributions.                | JournaloftheRoyalStatisticalSociety:Series |     |                         |     |     |
| identialregression. |             | ConferenceonNeuralInformation |     |               |      |     |                            |                                            |     |                         |     |     |
B(StatisticalMethodology).
ProcessingSystems.
|                     |     |     |                              |     |     |     | Freedman                    | (1963). On | the asymptotic |                      | behavior | of Bayes |
| ------------------- | --- | --- | ---------------------------- | --- | --- | --- | --------------------------- | ---------- | -------------- | -------------------- | -------- | -------- |
| Ayhan&Berens(2018). |     |     | Test-timedataaugmentationfor |     |     |     |                             |            |                |                      |          |          |
|                     |     |     |                              |     |     |     | estimatesinthediscretecase. |            |                | AnnalsofMathematical |          |          |
estimationofheteroscedasticaleatoricuncertaintyindeep
Statistics.
| neuralnetworks. |     | ConferenceonMedicalImagingwith |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DeepLearning. Freedman (1965). On the asymptotic behavior of Bayes
|                        |     |     |                              |     |     |     | estimatesinthediscretecaseII. |     |     | AnnalsofMathematical |     |     |
| ---------------------- | --- | --- | ---------------------------- | --- | --- | --- | ----------------------------- | --- | --- | -------------------- | --- | --- |
| Barbieri&Berger(2004). |     |     | Optimalpredictivemodelselec- |     |     |     |                               |     |     |                      |     |     |
Statistics.
tion. AnnalsofStatistics.
|               |           |                                      |     |     |     |     | Gal (2016).            | Uncertainty | in  | deep learning. | PhD | thesis, |
| ------------- | --------- | ------------------------------------ | --- | --- | --- | --- | ---------------------- | ----------- | --- | -------------- | --- | ------- |
| Berger(1985). |           | StatisticalDecisionTheoryandBayesian |     |     |     |     |                        |             |     |                |     |         |
| Analysis.     | Springer. |                                      |     |     |     |     | UniversityofCambridge. |             |     |                |     |         |
Bernardo&Smith(1994). BayesianTheory. JohnWiley Gal,Islam,&Ghahramani(2017). DeepBayesianactive
| andSons. |     |     |     |     |     |     | learningwithimagedata. |     |     | InternationalConferenceon |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ------------------------- | --- | --- |
MachineLearning.
| BickfordSmith,Foster,&Rainforth(2024). |     |     |     |     | Makingbet- |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ter use of unlabelled data in Bayesian active learning. Geisser & Eddy (1979). A predictive approach to model
InternationalConferenceonArtificialIntelligenceand selection.JournaloftheAmericanStatisticalAssociation.
Statistics.
Gruber,Schenk,Schierholz,Kreuter,&Kauermann(2023).
Bickford Smith, Kirsch, Farquhar, Gal, Foster, & Rain- Sources of uncertainty in machine learning—a statisti-
| forth(2023). |     | Prediction-orientedBayesianactivelearn- |     |     |     |     | cians’view. | arXiv. |     |     |     |     |
| ------------ | --- | --------------------------------------- | --- | --- | --- | --- | ----------- | ------ | --- | --- | --- | --- |
ing. InternationalConferenceonArtificialIntelligence
|     |     |     |     |     |     |     | Hacking(1975). | TheEmergenceofProbability. |     |     |     | Cambridge |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------------------------- | --- | --- | --- | --------- |
andStatistics.
UniversityPress.
| Box(1976). | Scienceandstatistics. |     |     | JournaloftheAmerican |     |     |     |     |     |     |     |     |
| ---------- | --------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
StatisticalAssociation. Hastie, Tibshirani, Friedman, & Friedman (2009). The
|                |       |                |          |                   |     |      | ElementsofStatisticalLearning. |                      |     | Springer. |             |     |
| -------------- | ----- | -------------- | -------- | ----------------- | --- | ---- | ------------------------------ | -------------------- | --- | --------- | ----------- | --- |
| Breiman(2001). |       | Randomforests. |          | MachineLearning.  |     |      |                                |                      |     |           |             |     |
|                |       |                |          |                   |     |      | Hofman,                        | Sale, & Hu¨llermeier |     | (2024a).  | Quantifying |     |
| Brown,         | Mann, | Ryder,         | Subbiah, | Kaplan, Dhariwal, |     | Nee- |                                |                      |     |           |             |     |
lakantan,Shyam,Sastry,Askell,Agarwal,Herbert-Voss, aleatoric and epistemic uncertainty: a credal approach.
|     |     |     |     |     |     |     | Workshop | on “Structured |     | Probabilistic | Inference | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------------- | --------- | --- |
Krueger,Henighan,Child,Ramesh,Ziegler,Wu,Winter,
GenerativeModeling”,InternationalConferenceonMa-
Hesse,Chen,Sigler,Litwin,Gray,Chess,Clark,Berner,
chineLearning.
| McCandlish,Radford,Sutskever,&Amodei(2020). |     |     |     |                  |     | Lan- |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| guagemodelsarefew-shotlearners.             |     |     |     | ConferenceonNeu- |     |      |     |     |     |     |     |     |
ralInformationProcessingSystems.
10

RethinkingAleatoricandEpistemicUncertainty
Hofman, Sale, & Hu¨llermeier (2024b). Quantifying Lahlou, Jain, Nekoei, Butoi, Bertin, Rector-Brooks, Ko-
aleatoricandepistemicuncertaintywithproperscoring rablyov,&Bengio(2023). DEUP:directepistemicun-
rules. arXiv. certaintyprediction. TransactionsonMachineLearning
Research.
| Houlsby,Husza´r,Ghahramani,&Lengyel(2011). |     |     |     |     |     | Bayesian |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
activelearningforclassificationandpreferencelearning. Laud&Ibrahim(1995).Predictivemodelselection.Journal
| arXiv. |     |     |     |     |     |     | oftheRoyalStatisticalSociety: |     |     | SeriesB(Methodologi- |     |
| ------ | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | -------------------- | --- |
cal).
| Huang,Guo,Acerbi,&Kaski(2024).        |     |     |     | AmortizedBayesian |              |     |                  |     |      |            |           |
| ------------------------------------- | --- | --- | --- | ----------------- | ------------ | --- | ---------------- | --- | ---- | ---------- | --------- |
| experimentaldesignfordecision-making. |     |     |     |                   | Conferenceon |     |                  |     |      |            |           |
|                                       |     |     |     |                   |              |     | Lawrence (2012). |     | What | is machine | learning? |
NeuralInformationProcessingSystems. videolectures.net/mlss2012_lawrence_
machine_learning.
| Hu¨llermeier&Waegeman(2021).             |            |                  |     | Aleatoricandepistemic |           |          |                             |                                    |     |               |         |
| ---------------------------------------- | ---------- | ---------------- | --- | --------------------- | --------- | -------- | --------------------------- | ---------------------------------- | --- | ------------- | ------- |
| uncertaintyinmachinelearning:            |            |                  |     | anintroductiontocon-  |           |          |                             |                                    |     |               | Nature. |
|                                          |            |                  |     |                       |           |          | LeCun,Bengio,&Hinton(2015). |                                    |     | Deeplearning. |         |
| ceptsandmethods.                         |            | MachineLearning. |     |                       |           |          |                             |                                    |     |               |         |
|                                          |            |                  |     |                       |           |          | Lindley(1956).              | Onameasureoftheinformationprovided |     |               |         |
| Immer,Bauer,Fortuin,Ra¨tsch,&Khan(2021). |            |                  |     |                       |           | Scalable |                             |                                    |     |               |         |
|                                          |            |                  |     |                       |           |          | byanexperiment.             | AnnalsofMathematicalStatistics.    |     |               |         |
| marginal                                 | likelihood | estimation       |     | for model             | selection | in       |                             |                                    |     |               |         |
deep learning. International Conference on Machine MacKay(1992a). Theevidenceframeworkappliedtoclas-
| Learning. |     |     |     |     |     |     | sificationnetworks. | NeuralComputation. |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------- | ------------------ | --- | --- | --- |
Kadane&Lazar(2004). Methodsandcriteriaformodel MacKay (1992b). Information-based objective functions
selection.JournaloftheAmericanStatisticalAssociation.
|         |            |           |      |                |             |        | foractivedataselection. |          | NeuralComputation. |              |                |
| ------- | ---------- | --------- | ---- | -------------- | ----------- | ------ | ----------------------- | -------- | ------------------ | ------------ | -------------- |
| Kapoor, | Maddox,    | Izmailov, | &    | Wilson (2022). | On          | uncer- |                         |          |                    |              |                |
|         |            |           |      |                |             |        | McAllister (2016).      | Bayesian |                    | learning for | data-efficient |
| tainty, | tempering, | and       | data | augmentation   | in Bayesian |        |                         |          |                    |              |                |
control. PhDthesis,UniversityofCambridge.
| classification. |     | Conference | on  | Neural | Information | Pro- |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ------ | ----------- | ---- | --- | --- | --- | --- | --- |
cessingSystems. Mucsa´nyi,Kirchhof,&Oh(2024). Benchmarkinguncer-
|                                        |     |     |                             |     |            |     | taintydisentanglement: |                                   | specializeduncertaintiesforspe- |     |     |
| -------------------------------------- | --- | --- | --------------------------- | --- | ---------- | --- | ---------------------- | --------------------------------- | ------------------------------- | --- | --- |
| Kendall&Gal(2017).                     |     |     | Whatuncertaintiesdoweneedin |     |            |     |                        |                                   |                                 |     |     |
|                                        |     |     |                             |     |            |     | cializedtasks.         | ConferenceonNeuralInformationPro- |                                 |     |     |
| Bayesiandeeplearningforcomputervision? |     |     |                             |     | Conference |     |                        |                                   |                                 |     |     |
cessingSystems.
onNeuralInformationProcessingSystems.
|          |           |               |            |         |              |     | Mukhoti,Kirsch,vanAmersfoort,Torr,&Gal(2023). |     |                     |     | Deep    |
| -------- | --------- | ------------- | ---------- | ------- | ------------ | --- | --------------------------------------------- | --- | ------------------- | --- | ------- |
| Kirsch,  | Farquhar, | Atighehchian, |            | Jesson, | Branchaud-   |     |                                               |     |                     |     |         |
|          |           |               |            |         |              |     | deterministicuncertainty:                     |     | anewsimplebaseline. |     | Confer- |
| Charron, | & Gal     | (2023).       | Stochastic | batch   | acquisition: |     |                                               |     |                     |     |         |
enceonComputerVisionandPatternRecognition.
| asimplebaselinefordeepactivelearning. |     |     |     |     | Transactions |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
onMachineLearningResearch. Murphy(2022). ProbabilisticMachineLearning: AnIntro-
|         |                 |     |       |         |            |     | duction. MITPress. |     |     |     |     |
| ------- | --------------- | --- | ----- | ------- | ---------- | --- | ------------------ | --- | --- | --- | --- |
| Kirsch, | van Amersfoort, |     | & Gal | (2019). | BatchBALD: | ef- |                    |     |     |     |     |
ficientanddiversebatchacquisitionfordeepBayesian Neiswanger,Yu,Zhao,Meng,&Ermon(2022). General-
| activelearning. |     | ConferenceonNeuralInformationPro- |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
izingBayesianoptimizationwithdecision-theoreticen-
cessingSystems. tropies. ConferenceonNeuralInformationProcessing
Systems.
| Kleijn&vanderVaart(2006). |     |     |     | Misspecificationininfinite- |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
dimensionalBayesianstatistics. AnnalsofStatistics. Orlando,Seebo¨ck,Bogunovic´,Klimscha,Grechenig,Wald-
Kleijn&vanderVaart(2012). TheBernstein-von-Mises stein, Gerendas, & Schmidt-Erfurth (2019). U2-net: a
BayesianU-netmodelwithepistemicuncertaintyfeed-
| theorem | under | misspecification. |     | Electronic | Journal | of  |     |     |     |     |     |
| ------- | ----- | ----------------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
Statistics. backforphotoreceptorlayersegmentationinpathologi-
|                                                      |     |     |     |     |     |     | calOCTscans. | InternationalSymposiumonBiomedical |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------------------- | --- | --- | --- |
| Kotelevskii,Artemenkov,Fedyanin,Noskov,Fishkov,Shel- |     |     |     |     |     |     | Imaging.     |                                    |     |     |     |
manov,Vazhentsev,Petiushko,&Panov(2022).Nonpara-
Osband,Wen,Asghari,Dwaracherla,Ibrahimi,Lu,&Van
metricuncertaintyquantificationforsingledeterministic
neuralnetwork. ConferenceonNeuralInformationPro- Roy(2023). Epistemicneuralnetworks. Conferenceon
| cessingSystems. |     |     |     |     |     |     | NeuralInformationProcessingSystems. |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
Kotelevskii,Kondratyev,Taka´cˇ,Moulines,&Panov(2025). Postels, Blum, Cadena, Siegwart, Van Gool, & Tombari
From risk to uncertainty: generating predictive uncer- (2020). Quantifyingaleatoricandepistemicuncertainty
taintymeasuresviaBayesianestimation. International usingdensityestimationinlatentspace. arXiv.
ConferenceonLearningRepresentations.
11

RethinkingAleatoricandEpistemicUncertainty
Raiffa & Schlaifer (1961). Applied Statistical Decision Senge,Bo¨sner,Dembczyn´ski,Haasenritter,Hirsch,Donner-
Theory. DivisionofResearch,HarvardBusinessSchool. Banzhoff,&Hu¨llermeier(2014). Reliableclassification:
|               |                      |     |                     |     |     | learning          | classifiers | that distinguish     | aleatoric | and epis- |
| ------------- | -------------------- | --- | ------------------- | --- | --- | ----------------- | ----------- | -------------------- | --------- | --------- |
| Ramsey(1926). | Truthandprobability. |     | StudiesinSubjective |     |     |                   |             |                      |           |           |
|               |                      |     |                     |     |     | temicuncertainty. |             | InformationSciences. |           |           |
Probability.
|     |     |     |     |     |     | Shannon(1948). |     | Amathematicaltheoryofcommunication. |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----------------------------------- | --- | --- |
Rice (2007). Mathematical Statistics and Data Analysis. TheBellSystemTechnicalJournal.
ThomsonBrooks/Cole.
|               |                  |                    |     |     |     | Smith &                               | Gal (2018). | Understanding | measures     | of uncer- |
| ------------- | ---------------- | ------------------ | --- | --- | --- | ------------------------------------- | ----------- | ------------- | ------------ | --------- |
| Robert(1996). | Intrinsiclosses. | TheoryandDecision. |     |     |     |                                       |             |               |              |           |
|               |                  |                    |     |     |     | taintyforadversarialexampledetection. |             |               | Conferenceon |           |
UncertaintyinArtificialIntelligence.
| Robert(2007).                           | TheBayesianChoice. |     | Springer. |              |     |                    |     |                                     |     |     |
| --------------------------------------- | ------------------ | --- | --------- | ------------ | --- | ------------------ | --- | ----------------------------------- | --- | --- |
|                                         |                    |     |           |              |     | Szepesva´ri(2010). |     | AlgorithmsforReinforcementLearning. |     |     |
| Sale,Bengs,Caprio,&Hu¨llermeier(2024a). |                    |     |           | Second-order |     |                    |     |                                     |     |     |
uncertainty quantification: a distance-based approach. MorganandClaypool.
InternationalConferenceonMachineLearning.
|     |     |     |     |     |     | Valdenegro-Toro |     | & Saromo-Mori | (2022). A deeper | look |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | ---------------- | ---- |
intoaleatoricandepistemicuncertaintydisentanglement.
| Sale, Caprio, | & Hu¨llermeier | (2023a). |     | Is the | volume of |     |     |     |     |     |
| ------------- | -------------- | -------- | --- | ------ | --------- | --- | --- | --- | --- | --- |
Workshopon“LatinXinCVResearch”,Conferenceon
| a credal | set a good measure | for | epistemic | uncertainty? |     |     |     |     |     |     |
| -------- | ------------------ | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- |
ConferenceonUncertaintyinArtificialIntelligence. ComputerVisionandPatternRecognition.
Sale, Hofman, Lo¨hr, Wimmer, Nagler, & Hu¨llermeier vanAmersfoort,Smith,Teh,&Gal(2020). Uncertaintyes-
timationusingasingledeepdeterministicneuralnetwork.
| (2024b). | Label-wisealeatoricandepistemicuncertainty |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
InternationalConferenceonMachineLearning.
| quantification. | ConferenceonUncertaintyinArtificial |     |     |     |     |     |     |     |     |     |
| --------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Intelligence. vonNeumann(1928). ZurTheoriederGesellschaftsspiele.
MathematischeAnnalen.
| Sale, Hofman,                          | Wimmer,                         | Hu¨llermeier, | &   | Nagler         | (2023b). |                               |                                            |                           |                  |     |
| -------------------------------------- | ------------------------------- | ------------- | --- | -------------- | -------- | ----------------------------- | ------------------------------------------ | ------------------------- | ---------------- | --- |
| Second-orderuncertaintyquantification: |                                 |               |     | variance-based |          |                               |                                            |                           |                  |     |
|                                        |                                 |               |     |                |          | vonNeumann&Morgenstern(1947). |                                            |                           | TheoryofGamesand |     |
| measures.                              | arXiv.                          |               |     |                |          |                               |                                            |                           |                  |     |
|                                        |                                 |               |     |                |          | EconomicBehavior.             |                                            | PrincetonUniversityPress. |                  |     |
| Savage(1951).                          | Thetheoryofstatisticaldecision. |               |     |                | Journal  |                               |                                            |                           |                  |     |
|                                        |                                 |               |     |                |          | Wald(1939).                   | Contributionstothetheoryofstatisticalesti- |                           |                  |     |
oftheAmericanStatisticalAssociation.
|     |     |     |     |     |     | mationandtestinghypotheses. |     |     | AnnalsofMathematical |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | -------------------- | --- |
Statistics.
| Savage (1971). | Elicitation                            | of personal |     | probabilities | and |                 |                                           |                      |     |     |
| -------------- | -------------------------------------- | ----------- | --- | ------------- | --- | --------------- | ----------------------------------------- | -------------------- | --- | --- |
| expectations.  | JournaloftheAmericanStatisticalAssoci- |             |     |               |     |                 |                                           |                      |     |     |
|                |                                        |             |     |               |     | Wald(1945).     | Statisticaldecisionfunctionswhichminimize |                      |     |     |
| ation.         |                                        |             |     |               |     | themaximumrisk. |                                           | AnnalsofMathematics. |     |     |
Schweighofer,Aichberger,Ielanskyi,&Hochreiter(2023a). Wang&Aitchison(2021). BayesianOODdetectionwith
Introducinganimprovedinformation-theoreticmeasure
|               |              |          |     |              |     | aleatoricuncertaintyandoutlierexposure. |     |     | arXiv. |     |
| ------------- | ------------ | -------- | --- | ------------ | --- | --------------------------------------- | --- | --- | ------ | --- |
| of predictive | uncertainty. | Workshop | on  | “Mathematics |     |                                         |     |     |        |     |
of Modern Machine Learning”, Conference on Neural Wang,Li,Aertsen,Deprest,Ourselin,&Vercauteren(2019).
InformationProcessingSystems. Aleatoricuncertaintyestimationwithtest-timeaugmenta-
tionformedicalimagesegmentationwithconvolutional
Schweighofer,Aichberger,Ielanskyi,&Hochreiter(2025).
|     |     |     |     |     |     | neuralnetworks. |     | Neurocomputing. |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | --- |
Oninformation-theoreticmeasuresofpredictiveuncer-
tainty. Conference on Uncertainty in Artificial Intelli- Wen, Osband, Qin, Lu, Ibrahimi, Dwaracherla, Asghari,
| gence. |     |     |     |     |     | &VanRoy(2022).                            |     | Frompredictionstodecisions: |        | the |
| ------ | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --------------------------- | ------ | --- |
|        |     |     |     |     |     | importanceofjointpredictivedistributions. |     |                             | arXiv. |     |
Schweighofer,Aichberger,Ielanskyi,Klambauer,&Hochre-
iter(2023b). Quantificationofuncertaintywithadversar- Wimmer, Sale, Hofman, Bischl, & Hu¨llermeier (2023).
ialmodels.ConferenceonNeuralInformationProcessing Quantifying aleatoric and epistemic uncertainty in ma-
Systems. chine learning: are conditional entropy and mutual in-
|           |                   |            |             |     |       | formationappropriatemeasures? |     |     | ConferenceonUncer- |     |
| --------- | ----------------- | ---------- | ----------- | --- | ----- | ----------------------------- | --- | --- | ------------------ | --- |
| Seebo¨ck, | Orlando, Schlegl, | Waldstein, | Bogunovic´, |     | Klim- |                               |     |     |                    |     |
taintyinArtificialIntelligence.
| scha,Langs,&Schmidt-Erfurth(2019). |     |     |     | Exploitingepis- |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
temicuncertaintyofanatomysegmentationforanomaly
| detectioninretinalOCT. |     | TransactionsonMedicalImag- |     |     |     |     |     |     |     |     |
| ---------------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ing.
12

RethinkingAleatoricandEpistemicUncertainty
A Examples
Example3 Evaluatingp (z)againstareferencedistribution,p (z),withA=Z andℓ(a,z)=(a−z)2correspondsto
|     |     | n   |     |     |     |     | eval |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
measuringthepredictiveperformanceofp (z)usingmeansquarederror,measuringthediscrepancybetweenp (z)and
n n
| p (z)usingsquaredbiasandmeasuringdispersioninp |     |     |     |     |     |      | (z)usingvariance. |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ---- | ----------------- | --- | --- | --- | --- |
| eval                                           |     |     |     |     |     | eval |                   |     |     |     |     |
|                                                |     |     |     |     |     | a∗   | E                 |     | a∗  |     | E   |
Proof Starting from Equation 4 with optimal actions n = pn(z) [z] = µ n and = peval(z) [z] = µ eval from
eval
| Example1,thediscrepancybetweenp |     |     |        | (z)andp  | (z)is   |         |      |             |        |      |     |
| ------------------------------- | --- | --- | ------ | -------- | ------- | ------- | ---- | ----------- | ------ | ---- | --- |
|                                 |     |     |        | n        | eval    |         |      |             |        |      |     |
|                                 |     |     |        |          | (cid:2) |         |      | −z)2(cid:3) |        |      |     |
|                                 |     | d(p | ,p )=E |          | (µ      | −z)2−(µ |      |             | =(µ −µ | )2.  |     |
|                                 |     | n   | eval   | peval(z) | n       |         | eval |             | n      | eval |     |
NowstartingfromEquation5,itcanalsobewrittenas
(cid:2) −z)2(cid:3)
|     |     |     | d(p | ,p     | )=E      | (µ  |     | −V       | [z]. |     |     |
| --- | --- | --- | --- | ------ | -------- | --- | --- | -------- | ---- | --- | --- |
|     |     |     |     | n eval | peval(z) |     | n   | peval(z) |      |     |     |
Equatingthesetwoexpressionsforthediscrepancyleadstoastandardbias-variancedecomposition:
|     |     |     | E                | (cid:2) | −z)2(cid:3) |             |      | )2+V |          |     |     |
| --- | --- | --- | ---------------- | ------- | ----------- | ----------- | ---- | ---- | -------- | --- | --- |
|     |     |     |                  |         | (µ          | =(µ         | −µ   |      | [z]      |     |     |
|     |     |     | peval(z)         |         | n           | n           | eval |      | peval(z) |     |     |
|     |     |     | |                |         | {z          | } |         | {z   | } |  | {z }     |     |     |
|     |     |     | meansquarederror |         |             | squaredbias |      |      | variance |     |     |
wherethemeansquarederrormeasurespredictiveperformanceandthevariancemeasuresdatadispersion.
Example 4 Evaluating p n (z) against a reference distribution, p eval (z), with A = P(Z) and ℓ(a,z) = −loga(z)
correspondstomeasuringthepredictiveperformanceofp (z)usingcrossentropy,measuringdiscrepancybetweenp (z)
n n
andp (z)usingKullback-Leiblerdivergenceandmeasuringdispersioninp (z)usingShannonentropy.
| eval |     |     |     |     |     |     |     |     | eval |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
Proof Starting from Equation 4 with optimal actions a∗ = p (z) and a∗ = p (z) (Example 2), the discrepancy
|                    |      |        |      |          |        | n        | n    | eval      | eval  |       |     |
| ------------------ | ---- | ------ | ---- | -------- | ------ | -------- | ---- | --------- | ----- | ----- | --- |
| betweenp n (z)andp | eval | (z)is  |      |          |        |          |      |           |       |       |     |
|                    |      | d(p ,p | )=E  |          | [−logp | (z)+logp |      | (z)]=KL[p | (z)∥p | (z)]. |     |
|                    |      | n      | eval | peval(z) |        | n        | eval |           | eval  | n     |     |
NowstartingfromEquation5,itcanalsobewrittenas
)=−E
|     | d(p | ,p   |          | [logp | (z)]−H[p |      | (z)]=H[p |      | (z)∥p (z)]−H[p |     | (z)]. |
| --- | --- | ---- | -------- | ----- | -------- | ---- | -------- | ---- | -------------- | --- | ----- |
|     | n   | eval | peval(z) |       | n        | eval |          | eval | n              |     | eval  |
Equatingthesetwoexpressionsforthediscrepancyleadstoastandardinformation-theoreticdecomposition:
|     |     |     | H[p eval     | (z)∥p | n (z)]=KL[p | eval         | (z)∥p | n (z)]+H[p | eval (z)] |     |     |
| --- | --- | --- | ------------ | ----- | ----------- | ------------ | ----- | ---------- | --------- | --- | --- |
|     |     |     | |            | {z    | }           | |            | {z    | }          | | {z      | }   |     |
|     |     |     | crossentropy |       |             | KLdivergence |       |            | entropy   |     |     |
wherethecrossentropymeasurespredictiveperformanceandtheentropymeasuresdatadispersion.
13

RethinkingAleatoricandEpistemicUncertainty
B ProofsofPropositions4to6
Proposition 4 Let y+ and p n (y|θ)p n (z|θ)p n (θ) be a combination of data sequence and generative model that yield
1:m
p (θ|y+ ) → δ (θ) as m → ∞. Then the expected conditional predictive entropy, E [H[p (z|θ)]], is a Bayes
| n 1:m | θ∞  |     |     |     |     |     |     | pn(θ) n |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------- |
estimatorofH[p (z|y+ )],themarginalpredictiveentropyafteraBayesianupdateoninfinitenewdata,y+ .
n 1:∞ 1:∞
Proof Since y+ recovers a single setting of θ, reasoning about θ is equivalent to reasoning about y+ , following
1:∞ 1:∞
the argument presented in Fong et al (2023). This allows us to apply Proposition 1 with F = H[p n (z|y+ )] and
1:∞
| f(θ)=H[p | (z|θ)],whichgivesη∗ |     | =E [H[p | (z|θ)]]. |     |     |     |     |
| -------- | ------------------- | --- | ------- | -------- | --- | --- | --- | --- |
|          | n                   |     | pn(θ)   | n        |     |     |     |     |
Proposition5 AssumethedataandmodelfromProposition4. Thentheexpectedinformationgaininthemodelparameters,
EIG ,fromobservingzisaBayesestimatoroftheinfinite-steppredictiveinformationgain,IG (y+ ).
| θ   |     |     |     |     |     |     |     | z 1:∞ |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Proof Theinformationgaintobeestimated,IG z (y+ ),isdefinedasthereductioninthemodel’spredictiveentropyfrom
1:∞
| aBayesianupdateoninfinitenewdata,y+ |     |     | :   |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1:∞
|     |     |     | IG (y+ | )=H[p | (z)]−H[p | (z|y+ | )]. |     |
| --- | --- | --- | ------ | ----- | -------- | ----- | --- | --- |
|     |     |     | z 1:∞  |       | n        | n     | 1:∞ |     |
CombiningtheknownH[p (z)]withtheBayesestimatorofH[p (z|y+ )]fromProposition4gives
|     |     | n   |     |      |        | n 1:∞   |         |     |
| --- | --- | --- | --- | ---- | ------ | ------- | ------- | --- |
|     |     |     | EIG | =H[p | (z)]−E | [H[p    | (z|θ)]] |     |
|     |     |     | θ   | n    |        | pn(θ) n |         |     |
(y+
| asaBayesestimatorofIG |     | z   | ).  |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1:∞
Proposition6 Letz =y . Assumey areindependentandidenticallydistributed,withy ∼p (y),andassume
|     |     | n+1 | 1:n |     |     |     |     | i train |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- |
p (z)=E [p (z|θ)]isamodelintendedtodirectlyapproximatep (z). Thentheexpectedinformationgaininthe
| n   | pn(θ) n |     |     |     |     | train |     |     |
| --- | ------- | --- | --- | --- | --- | ----- | --- | --- |
modelparameters,EIG ,fromobservingzisaBayesestimatorofthetrueone-stepexpectedinformationgain,EIGtrue,
θ θ
| wheretheexpectationiswithrespecttop |     |     | (z). |     |     |     |     |     |
| ----------------------------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
train
Proof Theexpectedinformationgaintobeestimated,EIGtrue,isdefinedasthereductioninthemodel’sparameterentropy
θ
| fromaBayesianupdateonnewdata,z,wherezisdrawnfromp |     |     |         |      |           | train (z): |          |     |
| ------------------------------------------------- | --- | --- | ------- | ---- | --------- | ---------- | -------- | --- |
|                                                   |     |     | EIGtrue |      | (θ)]−E    |            |          |     |
|                                                   |     |     |         | =H[p |           | [H[p       | (θ|z)]]. |     |
|                                                   |     |     | θ       | n    | ptrain(z) |            | n        |     |
The second term here can be estimated by applying Proposition 1 with F = E [H[p (θ|z )]] and f(θ) =
|     |     |     |     |     |     |     | ptrain(z) | n 1:m |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- |
| E   |     |     |     |     |     | η∗  | E         |       |
[H[p n (θ|z)]]. The Bayes estimator that results from this, = [H[p n (θ|z)]], can be combined with the
| pn(z|θ)                 |     |                |     |     |     |     | pn(z) |     |
| ----------------------- | --- | -------------- | --- | --- | --- | --- | ----- | --- |
| knowncurrententropy,H[p |     | (θ)],toproduce |     |     |     |     |       |     |
n
|     |     |     | EIG | =H[p | (θ)]−E | [H[p    | (θ|z)]] |     |
| --- | --- | --- | --- | ---- | ------ | ------- | ------- | --- |
|     |     |     | θ   | n    |        | pn(z) n |         |     |
asaBayesestimatorofEIGtrue.
θ
14

RethinkingAleatoricandEpistemicUncertainty
C Implementationdetails
CodetogenerateFigures3and4isavailableatgithub.com/fbickfordsmith/rethinking-aleatoric-epistemic.
C.1 Figure3
|     | R,  |     | R.  |     |     |
| --- | --- | --- | --- | --- | --- |
Weconsiderpredictinganoutput, z ∈ correspondingtoaninput, x ∈ Thetrainingdata, y 1:n , comprisesn = 2
input-labelpairs: y = (−2,tanh(−2))andy = (2,tanh(2)). WeusethistocomputeaGaussian-processpredictive
| 1   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- |
posterior,p (z|x) = p(z|x,y ),basedonagenerativemodelcomprisingaGaussianlikelihoodfunction,p(z|x,θ) =
n 1:n
Normal(z|θ(x),σ2),whereσ =0.1,andaGaussian-processprior,θ ∼GP(0,k),wherek(x,x′)=exp(−(x−x′)2/2).
Wecomparethiswithareferencedistribution,p (z|x) = Normal(y|tanh(x),σ2). Usingp (z|x)andp (z|x),we
|     |     | eval |     | n   | eval |
| --- | --- | ---- | --- | --- | ---- |
computethreequantitiesforx∈[−8,8]: thepredictiveuncertainty,h[p n (z|x)];thedatadispersion,h[p eval (z|x)];andthe
expectedscore,E [s(p ,z)].Wedothisfortwolossfunctions:ℓ(a,z)=(a−z)2andℓ(a,z)=max(0,z)·(a−z)2.
peval(z|x) n
C.2 Figure4
Weconsidertwocasesofpredictingz =y :adiscretecaseandacontinuouscase.Inthediscretecasewehavey ∈{0,1},
n+1
datageneratedfromp (y)=Bernoulli(y|η =0.5),andtheBayesiangenerativemodelis
train
p(y,η|α,β)=p(y|η)p(η|α,β)
p(y|η)=Bernoulli(y|η)
p(η|α,β)=Beta(η|α,β).
In the continuous case we have y ∈ R, data generated from p (y) = Normal(y|µ = 1,σ2 = 1), and the Bayesian
train
generativemodelis
p(y,µ,λ|α,β,κ,m)=p(y|µ,λ)p(µ|m,κ,λ)p(λ|α,β)
p(y|µ,λ)=Normal(y|µ,λ−1)
p(µ|m,κ,λ)=Normal(µ|m,(κλ)−1)
p(λ|α,β)=Gamma(λ|α,β).
In both cases we can compute exact Bayesian posteriors (Murphy, 2022), and there is some n for which p (z) =
n
p (z) (Doob, 1949; Freedman, 1963; 1965). For each case we sample four datasets, y , with y ∼ p (y) and
| train |     |     |     | 1:n | i train |
| ----- | --- | --- | --- | --- | ------- |
n∈(1,10,100,1000).OneachdatasetwecomputetheBayesianparameterposterior,p n (θ)=p(θ|y 1:n ),whereθ =(α,β)
orθ =(α,β,κ,m),andthencomputetwoquadraticestimationerrors. Thefirstistheerrorfromapproximatingthe“true”
expectedinformationgaininθwiththestandard,model-basedexpectedinformationgaininθ:
√
−EIGtrue
ε =EIG
|     | θ θ θ  |                    |             |               |     |
| --- | ------ | ------------------ | ----------- | ------------- | --- |
|     | (θ)]−E |                    | (θ)]−E      |               |     |
|     | =(H[p  | [H[p (θ|z)]])−(H[p |             | [H[p (θ|z)]]) |     |
|     | n      | pn(z) n            | n ptrain(z) | n             |     |
|     | =E     | (θ|z)]]−E          |             |               |     |
[H[p [H[p (θ|z)]].
|     | ptrain(z) n | pn(z) n |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
Thesecondistheerrorfromapproximatingtheinfinite-stepinformationgaininzwiththeexpectedinformationgaininθ:
√
(y+
|     | ε z =EIG θ −IG | z ) |     |     |     |
| --- | -------------- | --- | --- | --- | --- |
1:∞
(z)]−E
|     | =(H[p n | pn(θ) [H[p n (z|θ)]])−(H[p | n (z)]−H[p | train (z)]) |     |
| --- | ------- | -------------------------- | ---------- | ----------- | --- |
(z)]−E
|     | =H[p train | pn(θ) [H[p n (z|θ)]]. |     |     |     |
| --- | ---------- | --------------------- | --- | --- | --- |
Weaverageover50repeatswithdifferentrandom-numberseeds.
15