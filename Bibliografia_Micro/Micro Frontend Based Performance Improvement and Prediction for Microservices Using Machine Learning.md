Journal of Grid Computing (2024) 22:44
https://doi.org/10.1007/s10723-024-09760-8
RESEARCH
| Micro Frontend |             | Based Performance | Improvement   |     |          |     |
| -------------- | ----------- | ----------------- | ------------- | --- | -------- | --- |
| and Prediction |             | for Microservices | Using Machine |     | Learning |     |
|                | ·           | ·                 |               |     |          |     |
| NehaKaushik    | HarishKumar | VinayRaj          |               |     |          |     |
Received:15December2023/Accepted:18March2024/ Published online: 16 April 2024
©TheAuthor(s),underexclusivelicencetoSpringerNatureB.V.2024
Abstract Microservices has become a buzzword in alongwiththebackendmicroservices.Toimprovethe
industryasmanylargeITgiantssuchasAmazon,Twit- performance ofthemicroservicesbased webapplica-
ter,Uber,etchavestartedmigratingtheirexistingappli- tions,inthispaper,anewframeworkforthedesignof
cationstothisnewstyleandfewofthemhavestarted webapplicationswithmicrofrontendsforfrontendand
buildingtheirnewapplicationswiththisstyle.Dueto microservicesinthebackendoftheapplicationispre-
increasinguserrequirementsandtheneedtoaddmore sented.Toassesstheproposedframework,anempirical
business functionalities to the existing applications, investigationisperformedtoanalyzetheperformance
thewebapplicationsdesignedusingthemicroservices anditisfoundthattheapplicationsdesignedwithmicro
stylealsofaceafewperformancechallenges.Though frontends with microservices have performed better
thisstylehasbeensuccessfullyadoptedinthedesignof thantheapplicationswithmonolithicfrontends.Addi-
largeenterpriseapplications,stilltheapplicationsface tionally, to predict the performance of microservices
performance related issues. It is clear from the litera- based applications, a machine learning model is pro-
turethatmostofthearticlesfocusonlyonthebackend posed as machine learning has wide applications in
microservices.Tothebestofourknowledge,therehas software engineering related activities. The accuracy
beennosolutionproposedconsideringmicrofrontends of the proposed model using different metrics is also
presented.
HarishKumarandVinayRajarebotharecontributedequallyto
|          |     |     |                        |     | ·           | ·      |
| -------- | --- | --- | ---------------------- | --- | ----------- | ------ |
| thiswork |     |     | Keywords Microservices |     | Performance | Micro- |
frontends·Regression
B
| N.Kaushik ( | )·H.Kumar |     |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- | --- |
DepartmentofComputerEngineering,J.C.Bose
UniversityofScience&Technology,YMCA,Faridabad
| 121006,Haryana,India |     |     | 1 Introduction |     |     |     |
| -------------------- | --- | --- | -------------- | --- | --- | --- |
N.Kaushik
e-mail:20001902008@jcboseust.ac.in In recent years, increasing demand for independently
developedanddeployedwebapplicationshasledtoa
H.Kumar
e-mail:htanwar@jcboseust.ac.in considerableincreaseintheuseofdistributedsystems.
|     |     |     | In today’s environment, |     | everything must | be available |
| --- | --- | --- | ----------------------- | --- | --------------- | ------------ |
DepartmentofComputerApplications,NationalInstitute
ofTechnologyTiruchirappalli,Tiruchirappalli620015, online and delivered promptly for business purposes.
TamilNadu,India Distributedsystemsareessentialinordertospeedup
|     |     |     | service delivery | through | continuous | integration and |
| --- | --- | --- | ---------------- | ------- | ---------- | --------------- |
V.Raj
continuousdevelopment[31].ServiceOrientedArchi-
e-mail:vinayraj@nitt.edu
123

44 Page 2 of 26 Journal of Grid Computing (2024) 22:44
tecture(SOA)andMicroservicesArchitecture(MSA) ofthisarchitecturalstyle.Theoptimalgranularityofa
are two architectural styles based on distributed sys- microservice[33],serviceavailability[36],Qualityof
tems. Initially, applications were designed based on Service(QoS)ofmicroservices[34,35],microservices
themonolithicarchitecturalstyle.Monolithicarchitec- management[37],deploymentandscalability[38,39]
turebasedapplicationswereeasiertodevelop,testand are the issues on which researchers are focusing cur-
deploy because of their single code base. But as the rently.Apartfromseveraldifferentkindsofchallenges,
applicationsizeincreasesitbecomesdifficulttomain- performance monitoring, performance improvement,
tainandaccommodatenewchangestotheapplication self-adaptability, and performance prediction are the
becauseofitssingle,largeandcomplexcodebase[2– most common concerns among the researchers and
5]. To overcome these challenges SOA architectural practitioners[11–14].TheperformanceofMSAbased
stylecameintoexistence. application can be measured in terms of the time it
SOA provides guidelines for the development of takestorespondtouserrequestssi.e.ResponseTime,
large enterprise systems by the composition of seg- the number of requests completed per unit time i.e.
mentsofdifferentfunctionalities.SOAbasedapplica- Throughputorthenumberofresourcesanapplication
tionsarebasedupontheprincipleofdistributedsystems usestoservetheuserrequesti.e.Resourceusage.The
andtheseapplicationsareeasiertomanageandmain- lifecycleofamicroservicesapplicationcanbedivided
tain in comparison to monolithic architecture. Apart into two phases, developmental phase and the opera-
fromseveralbenefitstherearetheissuessuchasscal- tional phase [19]. The performance of an application
ability,centralgovernanceofservicesanddeployment can be improved by working on both phases of the
ofservicesthatdeveloperswerefacing[32].Allthese application.Buttothebestofourknowledge,several
issuesledtothetransitiontomicroservicesarchitecture researchershavesuggestedimprovingtheperformance
basedapplications. byfocusingonthegranularityofthemicroservicebut
MSAisanarchitecturalstylewhereanapplication in actuality there is a lack of work done in order to
isacollectionoflooselycoupledandindependentser- optimise the performance of a microservice architec-
vices and each service is responsible for performing turebasedapplicationbyfocusingonitsdevelopmental
a single task [8]. Microservices architectural style is phase.
an extension of SOA i.e. it inhabits all the proper- There is still a scope where by making changes
ties of SOA along with some additional properties. tothearchitectureofmicroservicesarchitecturebased
In microservices architecture based applications, dif- webapplications,theirperformancecanbeimproved.
ferent technologies can be used for developing each Moreover,makingchangesduringtheearlystageofthe
service, separate teams are assigned for the devel- applicationdevelopmentnotonlyimprovestheperfor-
opment of individual services hence teams can work mance of the web application but it will also be less
in parallel on several microservices which reduces complexandcosteffective.
development time,sincetheservicesarelooselycou- The paper resolved the existing gap by present-
pled they can be maintained and deployed indepen- ing a model implementing micro frontend following
dent of other services. The loosely coupled nature microservicesinthebackend.Theexistingapproaches
of microservices makes them easier to maintain and either focus on the operational level improvements
accommodate changes without affecting the whole or they use only micro fronted or microservices but
application. Delegation of team responsibility, main- not using both approaches together. To the best of
tainability,scalability,DevOpssupport,faulttolerance our knowledge, none of the existing work has imple-
and separation of software responsibilities are some mentedandprovedtheuseofmicrofrontendfollowing
oftheadditionalbenefitsofmicroservicesarchitecture microservicesasasolutionforperformanceimprove-
[10]. Because of several advantages associated with mentofmicroservicesarchitecturebasedwebapplica-
microservicesarchitecturestyle,ithasgainedtheatten- tions. In the proposed model, micro frontend is used
tionofresearchersandindustryexperts[1]. fordevelopingthefrontendofthewebapplicationand
Today,internetgiantssuchasNetflix,eBay,LinkedIn, themicroservicesapproachisusedfordevelopingthe
SoundcloudandAmazonhaveadoptedmicroservices backend of the application. The whole application is
architecture style for application development and now divided into small services where a service will
researchers are working to get a better understanding beresponsibleforexecutingasingletask.Alltheser-
123

| Journal of Grid Computing (2024) 22:44 |     |     |     |     |     |     |     |     | Page 3 of 26    44 |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- |
viceswillbedeveloped,deployed,debugged,evolved berofservicesandthenumberofrequestssubmittedto
andmaintainedindependentlyofotherservices.Inthe theapplication.Hencetheresultsthatwillbeobtained
proposed model a single team will be responsible for from this phase of the proposed work can be used by
developingthebackendandfrontendoftheapplication. researchersandpractitionersatanearlystageofappli-
Thecommunicationbetweenthefrontendservicesand cationdevelopmenttoimprovetheperformanceofthe
backendserviceswilltakeplaceviatheAPIGateway microservicesapplication.
oraggregationlayer.APIgatewaywilldecidetowhich Tosummarise,thispapermakesthefollowingcon-
| service the             | user request | should | be  | forwarded | for pro- | tributions: |     |     |     |     |
| ----------------------- | ------------ | ------ | --- | --------- | -------- | ----------- | --- | --- | --- | --- |
| cessingontheserverside. |              |        |     |           |          | (cid:129)   |     |     |     |     |
Developedamodelwheremicrofrontendhasbeen
Machinelearningmodelshavebeenwidelyapplied
usedfordesigningtheuserinterfaceoftheapplica-
| in software | engineering | especially |     | in predicting | and |     |     |     |     |     |
| ----------- | ----------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
tionandmicroserviceshavebeenusedfordesign-
| improving | the performance |     | of services | which | in turn |         |         |              |             |          |
| --------- | --------------- | --- | ----------- | ----- | ------- | ------- | ------- | ------------ | ----------- | -------- |
|           |                 |     |             |       |         | ing the | backend | architecture | of the same | applica- |
hasproducedpromisingbenefits.Inordertopredictthe
tion.
performanceofmicroservicesbasedapplicationscon-
(cid:129) Conductedanempiricalanalysistoinvestigatethe
sideringthenumberofservicesandcomplexityofthe
|     |     |     |     |     |     | performance | of  | the proposed | model | and com- |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ----- | -------- |
application,aregressionmodelisconstructedwiththe
pareditwithexistingmonolithicfrontendfollow-
datausedfortraining.Theproposedregressionmodel
ingmicroservicesarchitecturebasedapplication.
isalsotestedforestimatingtheaccuracyofthemodel.
|              |               |     |        |          |       | (cid:129) Proposed | a machine | learning | based model | to pre- |
| ------------ | ------------- | --- | ------ | -------- | ----- | ------------------ | --------- | -------- | ----------- | ------- |
| For a better | understanding |     | of the | proposed | model |                    |           |          |             |         |
dicttheresponsetimeofmicroservicesarchitecture
andtoclearlystatethemotivationbehindtheresearch
|           |           |          |           |     |            | based applications |     | which | can be used | for making |
| --------- | --------- | -------- | --------- | --- | ---------- | ------------------ | --- | ----- | ----------- | ---------- |
| work, the | following | Research | Questions |     | (RQs) have |                    |     |       |             |            |
performanceimprovementdecisions.
beenframed:
RQ 1: How the performance of MSA based appli- Theremainingpartofthepaperisstructuredasfol-
cationscanbeimproved. lows: The background of the proposed work includ-
| RQ 2: | Will the | implementation |     | of the | proposed |     |     |     |     |     |
| ----- | -------- | -------------- | --- | ------ | -------- | --- | --- | --- | --- | --- |
ingmonolithicandmicroservicesstylesispresentedin
model help in improving the performance of the Section2.Relatedworkfromtheliteratureisdiscussed
microservicesapplicationornot?
inSection3.Theproposedmodelanditsempiricaleval-
RQ3:Howmachinelearningcanbeusedtopredict uation are presented in Sections 4 and 5 respectively.
theresponsetimeofMSAbasedapplications.
Anapproachtopredicttheresponsetimeofmicroser-
ForRQ1,aframeworkincludingmicrofrontendfol- vicesusingMLisproposedinSection6.Thethreatsto
lowedbymicroservicesinthebackendofthewebappli- validityoftheproposedworkarepresentedinSections
cationhasbeenproposed.Tothebestofourknowledge, 7and8concludesthepaper.
whichisbasedontheliteraturesurveyandstudieson
recentworksthathavebeendonebythepractitioners
| in the field | of microservices, |     | none    | has tried   | to inte- | 2 Background |     |     |     |     |
| ------------ | ----------------- | --- | ------- | ----------- | -------- | ------------ | --- | --- | --- | --- |
| grate these  | two technologies  |     | for the | improvement | of       |              |     |     |     |     |
the performance of microservices applications. In the The preliminaries that are required to understand the
proposedframework,microfrontendhasbeenusedfor proposed model have been discussed in this section.
better handling of user requests and the frontend of The primary aim of this paper is to improve the per-
thewebapplicationandmicroservicesinbackendare formance of MSA based applications by using micro
usedforefficientdeploymentoftheapplicationwhich frontend instead of monolithic frontend. In this sec-
leads to efficient processing of the user requests on tion,toeasethereadersunderstanding,detailsofthese
theserverside.ToanswerRQ2,anempiricalanalysis differentarchitecturalstylesarediscussed.
| has been made | in order  | to           | compare | the results | of the      |     |     |     |     |     |
| ------------- | --------- | ------------ | ------- | ----------- | ----------- | --- | --- | --- | --- | --- |
| proposed      | model and | the existing |         | model.      | The results |     |     |     |     |     |
showhowtheproposedmodelimprovedthethrough- 2.1 MonolithicArchitecture
putofmicroservicesbasedwebapplications.ForRQ3,
machinelearninghasbeenusedtopredicttheresponse Monolithic architecture is a single-tiered architecture
time of the microservices application using the num- wheredifferentcomponentsarecombinedintoasingle
123

44 Page 4 of 26 Journal of Grid Computing (2024) 22:44
program running as a single deployment process [2]. Micro frontend is an approach where the frontend of
Monolithic architecture based applications are easier theapplicationisdividedintosmallservices.Eachser-
to develop, test and deploy because of a single code vicecanbedesignedbyaseparateteamusingdifferent
base[4].However,theencapsulationofallcomponents technologies.Inmicrofrontendarchitecture,therout-
as a unified process results in a tightly coupled soft- inglayerplaysakeyroleinmanagingtheroutingand
wareapplicationwherethemodulescannotbeexecuted navigationofeachmicrofrontendmoduleaswellasthe
independently and this problem becomes more com- overallapplication.Itachievesthisbyinterceptinguser
plexasthesizeofapplicationincreases[3,5].Because requestsanddeterminingwhichmicrofrontendmod-
of the tightly coupled nature of monolithic applica- ule should handle the request based on the requested
tions,changesinonecomponentcanaffecttheworking UniformResourceLocator(URL).Whenausermakes
ofothercomponentsandbecauseofthecomplexand arequest,theroutinglayerchecksiftherequestedURL
largecodebase,itisdifficulttodebug,evolveandmain- matchesanyoftheregisteredroutes.Ifamatchisfound,
tainthewholeapplication[6].Thecoordinationofthe theroutinglayeridentifiesthemicrofrontendmodule
developmentteamalsobecomesdifficultasthenumber responsible for handling that route and forwards the
of developers are high in monolithic applications [7]. requesttoit.Themicrofrontendmodulethenretrieves
Longtermcommitmenttoatechnologystack,continu- thenecessarydataandrenderstheappropriateviewor
ousdeploymentandscalingtheapplicationaresomeof component, which is then displayed to the user. If no
theotherdrawbacksassociatedwithmonolithicarchi- matchisfoundfortherequestedURL,theroutinglayer
tecture[4].Becauseofthesedrawbacks,organisations can either display a default page or redirect the user
havemigratedtomicroservicesarchitecturestyle. toanerrorpage.Technologyagnostic,codeisolation,
namingconventionsandresilientwebsitesaresomeof
theadditionalbenefitsofthemicrofrontendapproach
2.2 MicroservicesArchitecture to software development [18]. Micro frontend archi-
tecture based applications have independent services
Theconceptofmicroservicesarchitecturewasfirstdis- in the frontend of the application but the monolithic
cussedbyJamesLewisandMartinFowler.Microser- backendoftheapplicationstillfacesdependency.
vices Architecture (MSA) is based upon the dis- Figure1depictsthearchitecturaldifferencebetween
tributed system approach where the web applications monolithic architecture, MSA and micro frontend
are divided into loosely coupled, independent, highly based applications. In the below figure, it is clearly
cohesive and finely grained services. Each microser- visiblethatthefrontendandbackendorthemonolithic
vice is responsible for performing only a single task architecture based application has asinglecode base.
representingabusinesscapabilityanduseslightweight Thisindicatesthatthewholeapplicationincludingthe
mechanismssuchasHTTPandRESTAPIsforcommu- backend and frontend will be developed by several
nicatingwithothermicroservices[8,9].MSAenables teamsusingthesametechnologystack,thenintegrated
each microservice to be developed, tested, deployed, intoasinglecodebaseandthendeployedonthecloud.
andupgradedindependently[30].Microservicesarchi- Now in case of heavy workload several instances of
tectureprovidesindependentservicesonlyintheback- the whole application will be created, which will be
end of the application. Frontend of the application costly in terms of resource consumption. The second
still faces a significant degree of dependency and disadvantage of monolithic architecture is that if you
thisdependencyleadstocouplingandcommunication want to make changes in one module of the applica-
overhead[15]. tionthenthewholeapplication willbeunavailable to
theuserbecauseofasinglecodebase.Nowifyousee
microservicesarchitectureinFigure1,youwillnotice
2.3 MicroFrontend that the application is divided into several small ser-
vices(microservices)inthebackend.Itmeansincase
Inrecentyears,theconceptofmicrofrontendhasbeen ofheavyworkloadonamicroservicemultipleinstances
usedfordevelopingthefrontendofwebapplications. of that particular microservice will be created while
123

| Journal of Grid Computing (2024) 22:44 |     |     |     |     |     |     |     | Page 5 of 26    44 |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------ |
Fig.1 ComparisonofSeveralApplicationDevelopmentArchitectures
keeping the instances of other services as it is. So it comparedwiththeexistingmodelandresultsarepre-
willberesourceandcostefficient.Butnowifwesee sentedinthepaper.
thefrontendofanMSAbasedapplicationinFigure1
wecanobservethatithasamonolithicfrontend,which
meansifwetrytomakechangesinthefrontendthen
3 RelatedWork
| again the   | whole application        | will be impacted. | Micro  |     |     |     |     |     |
| ----------- | ------------------------ | ----------------- | ------ | --- | --- | --- | --- | --- |
| frontend in | Figure 1 has independent | services          | in the |     |     |     |     |     |
3.1 StudiesonPerformanceofMicroservices
| frontendoftheapplication,whichindicatesthatmak- |     |     |     | Architecture |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
ingchangesinfrontendwouldbeeasierandwhenthe
user sends a request, its request will be forwarded to The deployment complexities of microservices increase
theappropriateservicebyAPIgatewaybutintheback-
|     |     |     |     | as they scale. | It becomes | important | to  | measure and |
| --- | --- | --- | --- | -------------- | ---------- | --------- | --- | ----------- |
enditstillhasmonolithicarchitecturewhichmakesit monitor their performance before they degrade the
difficulttoscaleanddeploy.
|     |     |     |     | performance | of the whole | system. | Brondlin | and San- |
| --- | --- | --- | --- | ----------- | ------------ | ------- | -------- | -------- |
Hence to fill the gaps observed in the above dis- tambrogio [40] proposed a Black-Box monitoring
cussion,anovelframeworkhasbeenproposed,where
approachformicroservicesdeployedwithDockercon-
the web application has a micro frontend following tainers and managed by a Kubernetes orchestrator.
| microservices | in the backend. | Micro frontend | effi- |            |          |             |           |         |
| ------------- | --------------- | -------------- | ----- | ---------- | -------- | ----------- | --------- | ------- |
|               |                 |                |       | The author | has used | performance | counters, | network |
ciently improves the handling and forwarding of user performance, power consumption and resource usage
requestsandmicroservicesinthebackendhelpinthe
|     |     |     |     | metrics to | monitor the | microservices |     | at scale. How- |
| --- | --- | --- | --- | ---------- | ----------- | ------------- | --- | -------------- |
proper processing of requests and proper handling of ever, the focus of this work is on data monitoring,
heavyworkloadswithefficientutilisationofresources.
|     |     |     |     | which has | its limitations | in terms | of how | and where |
| --- | --- | --- | --- | --------- | --------------- | -------- | ------ | --------- |
The performance of the proposed framework is also this monitored data may be used to predict or opti-
123

44 Page 6 of 26 Journal of Grid Computing (2024) 22:44
mise microservice performance. Abdullah et al. [11] 3.2 StudiesontheRoleofMachineLearningin
proposed a burst aware autoscaling method to solve PerformanceofMicroservices
theproblemofdetectingandhandlingburstworkload
in containerized microservices based applications in Abdullah et al. [11] has performed resource predic-
order to preserve performance. The proposed model tionusingtheDecisionTreeRegressiontechniqueand
resulted in performance improvement but the limita- after resource prediction the author has predicted the
tion of the proposed model is that it was tested on a workload using Elastic Net (EN) regression model.
singlemicroservicebutnotontheapplicationcontain- Basedontheoutputreceivedfromthesetwostepsthe
ing multiple microservices. The distributed nature of autoscaling decisions are made. The proposed algo-
microservicesmakesresourcemanagementaconcern rithm succeeds to handle bursty workload situations
asitnotonlyincreasesthecostbutalsoaffectstheper- whilekeepinglessresponsetime.Thedrawbackofthe
formance of application. Joseph and Chandrasekaran proposed model is that the author has used a single
[19] reduced the response time of microservices and microserviceinitsexperimentation.Hencewhetherthe
performedefficientutilisationofresourcesbydeploy- proposed approach is suitable for the whole applica-
ing the microservices based on their interaction with tionincludingseveralmicroservicesisstillaconcern.
other microservices. However the author focused on Qassem et al. [26] has used a proactive approach for
theefficientutilisationofresourcesbutnotconsiderthe making autoscaling decisions. Random forest model
impactofnetworkcharacteristicssuchaslinkconges- hasbeenusedtopredictthefuturememoryandCPU
tion before making deployment decisions. Addition- requirementsofeachmicroservices.Laterbasedonthe
ally, energy efficiency of nodes is also a key point to predicted values horizontal and vertical scaling deci-
considerindeploymentdecisions,whichwasignored sions are made. In future progressive learning can be
in the proposed model of the author. Sampaio Jr. et usedtogetbetterandmoreaccurateresults.Yanetal.
al. [20] has used a three step approach for optimis- [27] used Bi-LSTM for predicting the workload and
ingtheperformanceofmicroservicesapplication.The performed elastic scaling using reinforcement learn-
first step includes the monitoring of microservices to ingalgorithms.Theloadpredictionmodelusedbythe
obtainresource,communicationaffinitiesrelatedinfor- author is inaccurate and requires update and regular
mation. Second step is to identify the performance trainingasthebusinessenvironmentchanges.Xuetal.
orientedoptimalplaceforlocatingthemicroservices. [28]haveproposedCoScalusinggradientdescentunits
Thethirdstepisthemigrationofmicroservicesbased forpredictingtheworkloadintimeseriesmannerand
ontheinformationobtainedfromprevioussteps.The reinforcementlearningalgorithmsforefficientscaling
approach used by the author sometimes improves the decisions. The proposed model succeeds in reducing
performance but at the same time in some cases it is theresponsetimeby6-10%.Deeplearningcanbeused
alsoresponsibleforperformancedegradation.Camilli infutureforimprovingtheaccuracyofworkloadpre-
and Russo [21] focused on identifying the microser- diction.
vicesthatcanleadtoperformancedegradationofcom-
plete applications. The results of the proposed model
can be used by the engineers during system main- 3.3 StudiesonMicroFrontend
tenance. Cortellessa et al. [22] monitors the runtime
interactionsofallmicroservicesofanapplicationand TheauthorPeltonenetal.[17]hasdiscussedtheben-
then uses the monitored data to improve the perfor- efitsandissuesrelatedtoMicroFrontendarchitectural
mancebyre-engineeringthedesignoftheapplication. style. The author in the survey found that the Micro
Intheproposedapproach,therefactoringdecisionsare frontendisanewarchitecturalstylewithseveralbene-
fullyautomated,anditisnotagoodpracticetoneglect fitsandlackofnecessaryfunctionalitiesthatcansup-
humanexpertiseinsoftwarere-engineering.Luoetal. port Micro Frontend. Yang et al. [24] has designed
[23]havedoneanindepthstudyofmicroservicescall a content management system using micro frontend
graphstofindthepossiblesolutionsforoptimisingthe architecturalstyleandcompareditwiththemonolithic
performance. frontendstyle.Theauthorfoundthatitislesscomplex
123

Journal of Grid Computing (2024) 22:44 Page 7 of 26    44
tomanagethesystembyusingmicrofrontendincom- designingthefrontend,backendandmaintenanceofthe
parison to monolithic frontend as the application size service.Alltheservicescanbedevelopedusingdiffer-
grows. Prajwal et al. [25] have studied the pros and ent programming languages. When using micro fron-
cons associated with the micro frontend architectural tends and microservices together, the front-end mod-
style.Technologyagnostic,faultisolation,teaminde- ules are developed and deployed independently, but
pendence and release independence are some of the theystillneedtocommunicatewiththeback-endser-
benefitsassociatedwithMicroFrontendwhileredun- vices.Thiscanbedoneusingwell-definedAPIsanda
dancy,communicationandriskofcodedivergenceare gatewaythathandlesthecommunicationbetweenthe
some of the issues that need to be addressed. Wang front-endmodulesandtheback-endservices.Figure2
et al. [16] have designed a graduate informed sys- depictstheproposedarchitecture,whereanapplication
tem using micro frontend architecture. The author isdividedintofourservicesnamedasServiceA,Ser-
used micro frontend architecture to verify how well viceB,ServiceCandServiceD.Arealtimeapplication
this architecture minimizes coupling and costs while can have any number of services depending upon the
improvingthecomposabilityandscalabilityofthesys- requirementbutheresobetterunderstandingofthepro-
tem. posedmodelwehaveonlyfourservices.Thebackend,
Josephetal.[19]dividedthelifecycleofmicroser- frontend of each service will be developed by sepa-
vices application into developmental phase and oper- rate teams. Each service can be developed using dif-
ationalphase.Basedontheanalysisofthefirststudy, ferent technologies in the backend and frontend and
it is found that most of the researchers have been different teams can work on their services simultane-
focusingontheperformanceimprovementofmicroser-
vicesapplicationbyworkingontheoperationalstage.
Noneoftheexistingworkhasfocusedonperformance
| improvement | by  | working | in the development |     | phase |
| ----------- | --- | ------- | ------------------ | --- | ----- |
oftheapplication.Makingimprovementsintheearly
stageiscosteffectiveandeasiertodo.Thesecondstudy
| shows how | proactive | actions | are better | than | reactive |
| --------- | --------- | ------- | ---------- | ---- | -------- |
actions.TheuseofMachineLearningleadstoaproac-
tiveactionwhicheliminatesthechanceofperformance
degradation.Thethirdstudyoftheliteratureshowsthat
MicroFrontendisanewarchitecturalstylewithseveral
| benefits | and challenges |     | that need to | be addressed. | To  |
| -------- | -------------- | --- | ------------ | ------------- | --- |
overcomealltheseexistinggaps,amodelisproposed
topredictandimprovetheperformanceofMSAbased
applications.
4 ProposedModel
| In this section, | an         | answer     | to RQ1 | has been | provided |
| ---------------- | ---------- | ---------- | ------ | -------- | -------- |
| by having        | a detailed | discussion | about  | the      | proposed |
model.Intheproposedmodel,microfrontendfollow-
| ing microservices |                 | in the   | backend            | has been    | used. We |
| ----------------- | --------------- | -------- | ------------------ | ----------- | -------- |
| will design       | an application, |          | where              | the whole   | applica- |
| tion will         | be divided      | into     | small and          | independent | ser-     |
| vices. Each       | service         | will     | be responsible     | for         | perform- |
| ing a single      | task            | and will | have access        | to its      | separate |
| database.         | Every webpage   |          | of the application |             | can con- |
sistofasingleormultipleservicesdependinguponits
requirement.Asingleteamwillberesponsibleforthe Fig.2 Architectureofmicrofrontendandmicroservices
123

| 44   Page 8 of 26 |     |     |     |     |     |     |     |     | Journal of Grid Computing (2024) 22:44 |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- |
ously hence reducing development time of the appli- The division of whole application into individual
cation. Each service has its own database and can be servicesmakeiteasiertodesignanddevelopit,allow
deployedinthecloudindependentofotherservices.In fasterdeliveryoftheapplicationtotheclient,loosely
caseofheavyworkloadonaparticularservice,thereis coupled services require less communication hence
noneedtoincreasetheinstancesofalltheservices,only reducingthecommunicationoverheadandimproving
theinstanceofthatparticularservicewillbeincreased responsetime,makingchangestooneapplicationdoes
whichinturnreducescostandimprovesefficientutil- not affect the other services and allows the other ser-
isationofresources. vicestowork.Henceitiseasiertomaintaintheappli-
Figure3showstheworkingoftheproposedmodel. cation developed using proposed model, independent
When a user clicks on a link, the routing layer is servicesmakesthedeploymentandscalingoperations
responsible for identifying the micro frontend ser- easytoimplementandcosteffective.
| vice responsible |     | for handling |     | the user | request. | Rout- |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- |
inglayerwillusetheURLoftheuserrequestinorder
|             |               |             |       |                  |           |         | 5 EmpiricalAnalysis |     |               |                 |     |
| ----------- | ------------- | ----------- | ----- | ---------------- | --------- | ------- | ------------------- | --- | ------------- | --------------- | --- |
| to identify | the           | appropriate |       | frontend service | for       | han-    |                     |     |               |                 |     |
| dling the   | user request. |             | After | frontend         | service   | identi- |                     |     |               |                 |     |
|             |               |             |       |                  |           |         | In this section     | we  | have analysed | the performance | of  |
| fication    | the service   | displays    |       | the appropriate  | interface |         |                     |     |               |                 |     |
theproposedmodelandtheexistingapproachinorder
andoptionstotheuser.Nowtheuserwillinteractwith
|     |     |     |     |     |     |     | to answer | RQ2. | RQ2 focused | on the implementation |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ----------- | --------------------- | --- |
themicrofrontendandmicrofrontendresponsetothe
oftheproposedmodelandtriedtofindwhetherornot
userbaseduponitsclicks.Nowiftheusersendssome
|     |     |     |     |     |     |     | the proposed | model | succeeded | in improving | the per- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --------- | ------------ | -------- |
requesttotheserverthenthefrontendserviceforwards
formanceofthemicroservicesapplicationornot.
| that request | to  | API gateway |     | and now | API gateway | is  |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
responsibleforforwardingtheuserrequesttotheright
backed microservice. The microservice processes the 5.1 CaseStudyApplication
| user request | using | its | database(if | needed) | and | if the |     |     |     |     |     |
| ------------ | ----- | --- | ----------- | ------- | --- | ------ | --- | --- | --- | --- | --- |
microservicewantstocommunicatetoothermicroser-
Toperformtheempiricalanalysis,anEshopapplication
| vices then | it communicates |     |     | with other | microservices |     |     |     |     |     |     |
| ---------- | --------------- | --- | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
usingmonolithicfrontendfollowedbymicroservicesin
| through | the API | gateway | only. | Now after | processing |     |     |     |     |     |     |
| ------- | ------- | ------- | ----- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
thebackendandmicrofrontendfollowedbymicroser-
| the user | request, | the microservice |     | sends | the response |     |     |     |     |     |     |
| -------- | -------- | ---------------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
vicesinthebackendisdevelopedusingtheserver-side
totheAPIgatewaywhichinturnforwardstheresponse
templatecomposition.Italsousescontainerapplication
| to appropriate |     | frontend | service. | After | receiving | the |     |     |     |     |     |
| -------------- | --- | -------- | -------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
servertomanagealltheservicesonasinglewebpage.
responsethefrontendservicedisplaystheappropriate
|     |     |     |     |     |     |     | Figure 4 | represents | the case | study application | devel- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | ----------------- | ------ |
outputtotheuser.
opedusingamonolithicfrontend.Thefrontendofthis
Fig.3 Workingofmicrofrontendfollowedbymicroservices
123

Journal of Grid Computing (2024) 22:44 Page 9 of 26 44
whichisresponsiblefordisplayinginformationofall
theproductsavailableonthewebsite.Afterdeveloping
all these components they are integrated into a single
and integrated codebase to form an application. The
backend services are responsible for maintaining the
informationrelatedtoeachcomponent.
Figure5representsthecasestudyapplicationhaving
micro frontend and microservices in the backend. To
buildthisapplication,thewholeapplicationisdivided
intofourservicesthatwillberesponsibletoperforma
singletaskandindependentofeachother.Thesefour
servicesarenamedHomeservice,Sellerservice,Buyer
Service and About service. The task of home service
is to display and maintain the information related to
the Home page of the application. The Seller service
willberesponsibleformaintaininganddisplayingthe
informationrelatedtoeachsellerandtheirratinggiven
tothembythecustomers.TheBuyerservicewillmain-
tainanddisplaytheinformationrelatedtoeachbuyer
andtheirpreviouspurchasehistory.TheAboutservice
willberesponsibletomaintainanddisplaytheinforma-
Fig.4 CaseStudyApplicationusingMonolithicFrontend
tionrelatedtoeachproductavailableonline.Nowthe
differenceinthisapplicationincomparisontothepre-
application has four main components as Home ser- viousapplicationisthattherewillbeaseparateteamfor
vice,SellerService,BuyerserviceandAboutService. eachservicewhichwilldevelopthefrontendandback-
Same technology stack has been used for developing end of their assigned service using different or same
thesecomponentsofthefrontend.Thesecomponents technology.Theseserviceswillbedeployedindepen-
arethenintegratedtoformasinglecodebase.Theback- dent of other services and in case of updates to one
endofthisapplicationhasfourdifferentmicroservices service other services will keep working and remain
named as Home service, Seller Service, Buyer Ser- unaffected.Whentheuseraccessestheapplicationthen
viceandAboutService.Theseservicesaredeveloped the browser will call the container application server,
usingdifferenttechnologystacksandareindependent which will call and assemble the respective services
ofeachother.Whentheuseraccessesthisapplication, that are needed to be displayed on the page based on
thewebbrowserfirstlydownloadsthefrontendcodeof useraction.Asinglepagewillcontainasingleormore
the application and then handles and renders the user numberofservices.
interfaceonthecomputerscreenbasedonuseractions.
Whileontheserverside,whenthebrowsersendsHTTP
request to the server, the server receives that HTTP 5.2 EmpiricalAnalysis
request and then calls the API gateway. API gateway
furthercallstheappropriateservicetohandletheuser Inordertovalidatetheproposedapproachofintegrat-
requests. In Figure 4, Home service represents Home ingmicrofrontendwithmicroservices,itisrequiredto
component which is responsible to display the home perform empirical analysis of the proposed approach
page of the application, Seller service represents the with existing standard of designing web applications.
sellercomponentoftheapplicationwhichisresponsi- In this section, empirical analysis performed with
blefordisplayingtheinformationrelatedtoallsellers respect to performance parameters i.e, response time
andtheirratings,Buyerservicerepresentingthebuyer andthroughputisanalyzedandresultsarepresented.
component which is responsible for displaying infor- Toperformtheempiricalanalysis,themainaimwas
mation related to each buyer and their past shopping tocapturetheresponsetime(s),throughput,anderror
details.AboutServicerepresentstheAboutcomponent percentagebyprovidingvaryingloadsfrom1to10000
123

44 Page 10 of 26 Journal of Grid Computing (2024) 22:44
Fig.5 CaseStudy
ApplicationusingMicro
Frontend
userrequests.Toachieveit,ApacheJMetertoolisused the minimum time an application takes to respond to
inourworkwhichhelpsinaccessingtheperformance the user request. All response times are measured in
by conducting load testing. The case study applica- milliseconds. Error percentage represents the number
tionreceivesuserrequestsfromthetoolwithdifferent offailedrequestsoutoftotalrequeststhatweresentto
loadsbyhittingrequeststhroughHTTPandtheresults the application. Throughput represents the number of
arecapturedforvaryingloads,whicharepresentedin userrequestscompletedpersecond.
Tables1to4. Table1representsthedatafortheHomeMicroser-
Thetablesinthissectionmainlyhavesevenfields. viceoftheapplication.Inthistable,thenumberofuser
Architectural style field represents the existing style requestsvaryfrom1to10000.Thetablealsorepresents
usedtodevelopmicroservicesapplicationsandarchi- response time, throughput and error rate using micro
tecturalstylethathasbeenusedintheproposedmodel. frontendandwithoutusingmicrofrontend.Wecansee
Inthiswork,monolithicfrontendfollowedbymicroser- fromthetablethattheproposedmodelleadstodecrease
vices architectureinthebackend hasbeen usedasan the response time of the microservice as the number
existingapproachofdevelopingMSAapplicationsand of users is increasing. The proposed model leads to
for the proposed model micro frontend followed by increasingthethroughputofthehomemicroservicein
MSA in backend has been used. So the Architectural comparisontoexistingapproaches.However,itisalso
style field of the tables will represent these two cat- observedthattheerrorpercentageisincreasingwhen
egories only. Second field of the tables is Number of thenumberofusersexceed5000.Fromthetable,itis
users, it represents the number of users that can send observedthattheerrorpercentageforboththestylesis
HTTPrequeststotheapplicationsimultaneously.Aver- 30.74%and51.47%respectively.AsJmeterhasbeen
ageresponsetimeistheaveragetimetakentorespond usedfortestingtheperformance,amaximumof10000
totheuserrequest.Maximumresponsetimerepresents user requests can be sent to the application and it is
themaximumtimetheapplicationtakestorespondto the main reason for the failure of requests when hit-
the user request. Minimum response time represents tingwith10000requests.Therefore,itdoesnotreflects
123

Journal of Grid Computing (2024) 22:44 Page 11 of 26    44
tuphguorhT
|           |           |     |                   |                     |           | ces/2.1001 ces/4.5901 |
| --------- | --------- | --- | ----------------- | ------------------- | --------- | --------------------- |
| ces/0.005 | ces/0.005 |     |                   | ces/0.433 ces/4.433 | ces/1.487 | ces/8.939             |
|           |           |     | ces/8.33 ces/8.33 |                     |           |                       |
ces/7.3 ces/7.3
egatnecreProrrE
| %00.0 | %00.0 %00.0 | %00.0 | %00.0 %00.0 | %00.0 %00.0 | %61.0 | %00.0 %47.03 %74.15 |
| ----- | ----------- | ----- | ----------- | ----------- | ----- | ------------------- |
esnopseRmumixaM
)smni(emiT
|     |     |     |     |     | 2904 | 7995 2946 |
| --- | --- | --- | --- | --- | ---- | --------- |
|     |     |     |     | 11  |      | 47        |
| 2   | 2 6 | 3   | 9 8 | 6   |      |           |
esnopseRmuminiM
)smni(emiT
| 2   | 2 2 | 1   | 1 1 | 0 0 | 3   | 0 7 2 |
| --- | --- | --- | --- | --- | --- | ----- |
esnopseRegarevA
)smni(emiT
|     |     |     |     |     | 774 | 1472 1761 |
| --- | --- | --- | --- | --- | --- | --------- |
| 2   | 2 4 | 1   | 3 3 | 1 1 |     | 8         |
sresUforebmuN
ecivreSemoHfoelbaTecnamrofreP
00001 00001
|     |     |     |         | 0001 0001 | 0005 | 0005 |
| --- | --- | --- | ------- | --------- | ---- | ---- |
|     |     |     | 001 001 |           |      |      |
01 01
1 1
| -lof                | ybdewollofdnetnorforciM -lof | ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof                | ybdewollofdnetnorforciM -lof ybdewollofdnetnorforciM |
| ------------------- | ---------------------------- | ----------------------- | ---------------------------- | ---------------------------- | ------------------- | ---------------------------------------------------- |
| dnekcabniASMybdewol |                              | dnekcabniASMybdewol     | dnekcabniASMybdewol          | dnekcabniASMybdewol          | dnekcabniASMybdewol | dnekcabniASMybdewol                                  |
| dnetnorF            | dnetnorF                     |                         | dnetnorF                     | dnetnorF                     | dnetnorF            | dnetnorF                                             |
elytSlarutcetihcrA
|            | dnekcabniASM | dnekcabniASM |            | dnekcabniASM | dnekcabniASM | dnekcabniASM dnekcabniASM |
| ---------- | ------------ | ------------ | ---------- | ------------ | ------------ | ------------------------- |
| cihtilonoM | cihtilonoM   |              | cihtilonoM | cihtilonoM   | cihtilonoM   | cihtilonoM                |
1elbaT
123

44   Page 12 of 26 Journal of Grid Computing (2024) 22:44
tuphguorhT
|           | ces/0.0001 |     |                     | ces/2.1001 |           | ces/2.7321 |
| --------- | ---------- | --- | ------------------- | ---------- | --------- | ---------- |
| ces/0.005 |            |     | ces/7.333 ces/9.333 | ces/6.599  | ces/8.719 |            |
ces/7.33 ces/6.33
egatnecreProrrE
| %00.0 | %00.0 %00.0 | %00.0 | %00.0 %00.0 | %00.0 %00.0 | %20.37 | %41.15 |
| ----- | ----------- | ----- | ----------- | ----------- | ------ | ------ |
esnopseRmumixaM
)smni(emiT
|     | 001 |     |       | 477 942 | 7998 | 4926 |
| --- | --- | --- | ----- | ------- | ---- | ---- |
|     |     |     | 31 11 |         |      |      |
| 2   | 1   | 6   |       |         |      |      |
esnopseRmuminiM
)smni(emiT
| 2   | 1 1 | 1   | 1 1 | 1 1 | 2   | 2   |
| --- | --- | --- | --- | --- | --- | --- |
esnopseRegarevA
)smni(emiT
0833 4052
521
55
| 2   | 1 6 | 3   | 1 1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
sresUforebmuN
ecivreSrelleSfoelbaTecnamrofreP
00001 00001
|     |     |     | 0001 0001 | 0005 0005 |     |     |
| --- | --- | --- | --------- | --------- | --- | --- |
001 001
1 1
| -lof                | ybdewollofdnetnorforciM -lof | ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof                | ybdewollofdnetnorforciM |
| ------------------- | ---------------------------- | ----------------------- | ---------------------------- | ---------------------------- | ------------------- | ----------------------- |
| dnekcabniASMybdewol |                              | dnekcabniASMybdewol     | dnekcabniASMybdewol          | dnekcabniASMybdewol          | dnekcabniASMybdewol |                         |
| dnetnorF            | dnetnorF                     |                         | dnetnorF                     | dnetnorF                     | dnetnorF            |                         |
elytSlarutcetihcrA
|            | dnekcabniASM | dnekcabniASM |            | dnekcabniASM | dnekcabniASM | dnekcabniASM |
| ---------- | ------------ | ------------ | ---------- | ------------ | ------------ | ------------ |
| cihtilonoM | cihtilonoM   |              | cihtilonoM | cihtilonoM   | cihtilonoM   |              |
2elbaT
123

Journal of Grid Computing (2024) 22:44 Page 13 of 26    44
tuphguorhT
|           | ces/0.0001 |     |                     | ces/0.2001 ces/0.3001 | ces/3.6041 | ces/5.7541 |
| --------- | ---------- | --- | ------------------- | --------------------- | ---------- | ---------- |
| ces/0.005 |            |     | ces/1.233 ces/2.433 |                       |            |            |
ces/5.33 ces/8.33
egatnecreProrrE
%85.27 %73.05
| %00.0 | %00.0 %00.0 | %00.0 | %00.0 %00.0 | %00.0 %00.0 |     |     |
| ----- | ----------- | ----- | ----------- | ----------- | --- | --- |
esnopseRmumixaM
)smni(emiT
6455 8735
|     | 01  |     |     | 142 931 |     |     |
| --- | --- | --- | --- | ------- | --- | --- |
| 2   | 1   | 8   | 8 7 |         |     |     |
esnopseRmuminiM
)smni(emiT
| 2   | 1 1 | 1   | 1 1 | 1 1 | 2   | 2   |
| --- | --- | --- | --- | --- | --- | --- |
esnopseRegarevA
)smni(emiT
1562 4903
|     |     |     |     | 36 91 |     |     |
| --- | --- | --- | --- | ----- | --- | --- |
| 2   | 1 5 | 4   | 1 1 |       |     |     |
sresUforebmuN
ecivreSreyuBfoelbaTecnamrofreP
00001 00001
|     |     |     | 0001 0001 | 0005 0005 |     |     |
| --- | --- | --- | --------- | --------- | --- | --- |
001 001
1 1
| -lof                | ybdewollofdnetnorforciM -lof | ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof                | ybdewollofdnetnorforciM |
| ------------------- | ---------------------------- | ----------------------- | ---------------------------- | ---------------------------- | ------------------- | ----------------------- |
| dnekcabniASMybdewol |                              | dnekcabniASMybdewol     | dnekcabniASMybdewol          | dnekcabniASMybdewol          | dnekcabniASMybdewol |                         |
| dnetnorF            | dnetnorF                     |                         | dnetnorF                     | dnetnorF                     | dnetnorF            |                         |
elytSlarutcetihcrA
|            | dnekcabniASM | dnekcabniASM |            | dnekcabniASM | dnekcabniASM | dnekcabniASM |
| ---------- | ------------ | ------------ | ---------- | ------------ | ------------ | ------------ |
| cihtilonoM | cihtilonoM   |              | cihtilonoM | cihtilonoM   | cihtilonoM   |              |
3elbaT
123

44   Page 14 of 26 Journal of Grid Computing (2024) 22:44
tuphguorhT
| ces/33.333 |           |     |                     | ces/2.1001 |           | ces/6.7321 |
| ---------- | --------- | --- | ------------------- | ---------- | --------- | ---------- |
|            | ces/0.005 |     | ces/0.333 ces/4.433 | ces/6.799  | ces/0.748 |            |
ces/6.33 ces/7.33
egatnecreProrrE
| %00.0 | %00.0 %00.0 | %00.0 | %00.0 %00.0 | %00.0 %00.0 | %04.96 | %39.33 |
| ----- | ----------- | ----- | ----------- | ----------- | ------ | ------ |
esnopseRmumixaM
)smni(emiT
|     |     |     |     | 5211 932 | 5898 | 9026 |
| --- | --- | --- | --- | -------- | ---- | ---- |
21
| 3   | 2 9 | 9   | 5   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
esnopseRmuminiM
)smni(emiT
| 3   | 2 1 | 1   | 1 1 | 1 1 | 6   | 2   |
| --- | --- | --- | --- | --- | --- | --- |
esnopseRegarevA
)smni(emiT
9224 5782
|     |     |     |     | 39 15 |     |     |
| --- | --- | --- | --- | ----- | --- | --- |
| 3   | 2 5 | 4   | 1 1 |       |     |     |
sresUforebmuN
ecivreStuobAfoelbaTecnamrofreP
00001 00001
|     |     |     | 0001 0001 | 0005 0005 |     |     |
| --- | --- | --- | --------- | --------- | --- | --- |
001 001
1 1
| -lof                | ybdewollofdnetnorforciM -lof | ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof ybdewollofdnetnorforciM | -lof                | ybdewollofdnetnorforciM |
| ------------------- | ---------------------------- | ----------------------- | ---------------------------- | ---------------------------- | ------------------- | ----------------------- |
| dnekcabniASMybdewol |                              | dnekcabniASMybdewol     | dnekcabniASMybdewol          | dnekcabniASMybdewol          | dnekcabniASMybdewol |                         |
| dnetnorF            | dnetnorF                     |                         | dnetnorF                     | dnetnorF                     | dnetnorF            |                         |
elytSlarutcetihcrA
|            | dnekcabniASM | dnekcabniASM |            | dnekcabniASM | dnekcabniASM | dnekcabniASM |
| ---------- | ------------ | ------------ | ---------- | ------------ | ------------ | ------------ |
| cihtilonoM | cihtilonoM   |              | cihtilonoM | cihtilonoM   | cihtilonoM   |              |
4elbaT
123

Journal of Grid Computing (2024) 22:44 Page 15 of 26 44
Fig.6 MaximumResponse
TimeofHomeService
any issue with the proposed approach or the chosen thantheapplicationwhichisnotusingmicrofrontend.
casestudyapplication.However,someadvancedtest- The maximum response time and average response
ingtoolssuchasK6,Locust,ApacheBenchcanbeused time represent the worst case and average case sce-
fortestingbutthesetoolsdorequirehigherconfigura- narios of time complexity. So in order to analyse the
tionsystemsforprocessingtherequests. performanceoftheproposedmodelandexistingmodel
The maximum response time of the application themaximumandaverageresponsetimematricesare
usingamicrofrontend,followedbytheMSAandthe considered. The results show that in the case of the
application without using a micro frontend, is shown Homeserviceproposedmodelperformsbetterthanthe
graphicallyinFigure6.FromFigure6,itisclearthat existingmodel.
the use of a micro frontend with a microservice per- Table2representstheperformancematrixofSeller
formsbetterthantheexistingapproachsinceitreduces service. We can see how the response time using the
theresponsetimeoftheapplication. micro frontend and microservices decreases in com-
Figure7isthegraphicalrepresentationoftheaver- parison to monolithic frontend followed by microser-
agetimetakentorespondtouserrequestsbythepro- vices.Thegapbetweentheresponsetimesusingboth
posed model and the existing model. Figure 7 shows the approaches is increasing as the number of users
theuseofmicrofrontendresultsinlesserresponsetime is increasing. The error rate is also less when we are
Fig.7 AverageResponse
TimeofHomeService
123

44 Page 16 of 26 Journal of Grid Computing (2024) 22:44
Fig.8 MaximumResponse
TimeofSellerService
usingthemicrofrontend.Thenumberofrequestssuc- Hencewecansaythattheproposedmodelworksbetter
cessfully executed per second is also larger when we thantheexistingmodelinthecaseofSellerservice.
usethemicrofrontend. Table3representstheperformanceofBuyerservice
Figure8isthegraphicalrepresentationofthemax- usingbothmicrofrontendandmonolithicfrontend.We
imumresponsetimeoftheSellerservice.Itrepresents canseefromthetablethatwhetherthenumberofusers
the maximum response time of the proposed model is1,10,100,1000,5000or10000,foreverynumber
whichusesmicrofrontendtoimprovetheperformance ofuserstheerrorrateandresponsetimeofmicrofron-
of the application and existing model which do not tend based application is either the same as existing
usemicrofrontend.Thegraphicalrepresentationshows approachoritisdecreasedandthethroughputisalso
thattheproposedmodelismoreefficientthantheexist- increasedusingthemicrofrontend.
ingmodelintermsofperformance. Figure10showsthegraphicalrepresentationofthe
Figure 9 represents the average response time of maximumresponsetimeofBuyerservice.Aswecan
Sellerservicewithandwithoutmicrofrontend.From see, the use of a micro frontend either reduces the
thisfigure,itisclearthattheproposedmodelhelpsin response time or keeps it the same as that of the pro-
reducingtheaverageresponsetimeinmostofthecases. posedmodel.SowecansaythatinthecaseofBuyer
Fig.9 AverageResponse
TimeofSellerService
123

Journal of Grid Computing (2024) 22:44 Page 17 of 26 44
Fig.10 Maximum
ResponseTimeofBuyer
Service
service, the use of a micro frontend performs better Figure12depictsthegraphicalrepresentationofthe
thanexistingmodelasitreducestheresponsetimein responsetimecollectedduringimplementationofpro-
somecases. posedmodelandexistingmodel.Thisfigureshowsthat
Figure 11 represents the average response time of for About service, the use of micro frontend leads in
proposed model and existing model. The use of the reducing the response time for any number of users.
proposedmodelreducedtheresponsetimeinallcases It means we can say that for About service the pro-
exceptwhenthenumberofusersis10000. posed model of micro fronted and microservices per-
Table4representstheresponsetime,errorrateand formsbetterthantheexistingmodel.
throughputofAboutserviceusingmicrofrontendand Figure13isthegraphicalrepresentationoftheAver-
withoutmicrofrontend.Theresultsshowthatthemicro age response time of the About service of the case
frontend is giving better results than the monolithic study applications. The graph shows that the average
frontend. No matter what the number of users, in all responsetimeofaboutserviceiseitherreducedinmost
thecasesmicrofrontendandmicroservicesaregiving ofthecasesorremainsthesame.Hencewecansaythat
better results. And as the number of users is increas- forAboutservice,theproposedmodelleadstobetter
ingthegapbetweentheresultsisalsoincreasingand performanceincomparisontotheexistingmodelwhich
makingtheproposedapproachworkbetter. usesmonolithicfrontendandmicroservices.
Fig.11 AverageResponse
TimeofBuyerService
123

44 Page 18 of 26 Journal of Grid Computing (2024) 22:44
Fig.12 Maximum
ResponseTimeofAbout
Service
Afterobservingthemaximumandaverageresponse approachisdefinitelyarecommendationfordesigning
time of all the services using the proposed model i.e. largeenterprisewebapplications.Thesummaryofour
micro frontend followed by MSA and existing model findingsisdiscussedhere.
i.e.monolithicfrontendfollowedbyMSA,wecansay Thefindingsindicatethattheaverageresponsetime
that proposed model leads to reduced response time. usingaMicroFrontendistypicallybetterthantheaver-
Also,thethroughputofalltheserviceswiththenum- age response time obtained using a Monolithic Fron-
berofusersas1,100,1000,5000and10000isgraphi- tend for all services and also for varying numbers of
callyrepresentedinFigures14to18respectively.The users. In some cases, the average response time of
graphshowsthattheproposedmodelleadtoimprove micro frontend architectural style is the same as that
throughputinmostcases. ofmonolithicfrontend.Forexample,whenthenumber
ofusersis1000,alltheserviceshavethesameaverage
responsetimeforboththearchitecturalstylesi.e.using
5.3 Discussion microfrontendandwithoutmicrofrontend.InFigure7,
whenthenumberofusersis100,Homeservicehasthe
After analyzing the response time and throughput of sameaverageresponsetimeforboththestyles.Onlyin
theproposedapproachwithrespecttotheearlierstyles onecasetheaverageresponsetimeofthemicrofron-
ofdesigningapplications,itisclearthattheproposed tendbasedarchitecturalstyleishigherthantheaverage
Fig.13 AverageResponse
TimeofAboutService
123

Journal of Grid Computing (2024) 22:44 Page 19 of 26 44
Fig.14 Throughputwhen
thenumberofusersis1
Fig.15 Throughputwhen
thenumberofusersis100
Fig.16 Throughputwhen
thenumberofusersis1000
123

| 44   Page 20 of 26 |     |     |     |     | Journal of Grid Computing (2024) 22:44 |     |     |
| ------------------ | --- | --- | --- | --- | -------------------------------------- | --- | --- |
Fig.17 Throughputwhen
thenumberofusersis5000
response time of the monolithic frontend. For exam- The comparison between both the approaches is
ple, the Buyer service using micro frontend has high based on the response time, error percentage and
average response time when the number of users is throughput matrix. And in all three matrices, fron-
10000.Themaximumresponsetimeusingmicrofron- tendbasedapplicationsleadtoreducedresponsetime
tend is always less than the maximum response time i.e. faster response to the end user for their HTTP
without micro frontend. Only in two cases, the maxi- requests,increasedthethroughputandreducednumber
mum response timeisthe samefor both architectural offailedrequests.Observingtheperformancematrixof
styles. For example in Table 1, when the number of allthemicroservices andthegraphicalrepresentation
usersis1,andinTable4whenthenumberofusersis of response time and throughput, it can be concluded
100,themaximumresponsetimeformonolithicfron- thattheproposedmodelisgivingbetterresultsthanthe
| tend and      | micro frontend   | is the same. | Figure 14 to 18   | existingmodel. |     |     |     |
| ------------- | ---------------- | ------------ | ----------------- | -------------- | --- | --- | --- |
| represent     | the service wise | comparison   | of throughput     |                |     |     |     |
| for different | number of        | users. The   | figures show that |                |     |     |     |
6 PerformancePrediction
| in most   | of the cases,   | the proposed | framework leads |     |     |     |     |
| --------- | --------------- | ------------ | --------------- | --- | --- | --- | --- |
| to better | throughput than | the existing | approach. The   |     |     |     |     |
Inthissection,theregressionmodelforpredictingthe
throughputofHomeserviceissameforbotharchitec-
|              |          |                 |               | performance         | of microservices | based applications, | the      |
| ------------ | -------- | --------------- | ------------- | ------------------- | ---------------- | ------------------- | -------- |
| tural styles | when the | number of users | is 1, 100 and |                     |                  |                     |          |
|              |          |                 |               | dataset information | about            | the microservices   | applica- |
1000.
Fig.18 Throughputwhen
thenumberofusersis
10000
123

| Journal of Grid Computing (2024) 22:44        |     |     |     |             |     |     | Page 21 of 26    44 |
| --------------------------------------------- | --- | --- | --- | ----------- | --- | --- | ------------------- |
| tionsandthemeasurestoevaluatetheaccuracyofthe |     |     |     | 6.2 Dataset |     |     |                     |
proposedregressionmodelsarepresented.
Thecollectionofdatasetformicroservicesbasedappli-
cationisreallyachallengeduetotheinabilitytoaccess
projectsdevelopedinindustryandtheunavailabilityof
|     |     |     |     | performance | metrics of | the applications | available in |
| --- | --- | --- | --- | ----------- | ---------- | ---------------- | ------------ |
6.1 RegressionAnalysis
publicdatasets.Duetothis,applicationsconsideredas
casestudiesindifferentresearcharticlesfromliterature
| Regression | is one of the | important methods | of ana- |     |     |     |     |
| ---------- | ------------- | ----------------- | ------- | --- | --- | --- | --- |
lyzing the relationship between dependent and inde- areconsideredasdataset.Therequiredinformationfor
thisregressionanalysisisgatheredfromthepapersand
pendentvariablesbygeneratingamodeltopresentthe
relationship.Ifthenumberofindependentvariablesis thedetailsofwhicharepresentedinTable5.Totalof
10microservicesbasedapplicationdataarecollected,
| more than | two, then the | generated model | is called as |     |     |     |     |
| --------- | ------------- | --------------- | ------------ | --- | --- | --- | --- |
multipleregressionanditismostpreferredandapplied outofwhich8recordsareusedfortrainingthemodel
andtheremainingtwoapplicationsfortestingthecon-
methodinsoftwareengineeringanalytics.Astheaimof
thisproposedmodelistoestimatetheperformanceof structedregressionmodel.
| a microservices | based application, | it is dependent             | on  |     |     |     |     |
| --------------- | ------------------ | --------------------------- | --- | --- | --- | --- | --- |
| many factors    | including          | the number of microservices |     |     |     |     |     |
6.3 EvaluationCriteria
| and number | of requests           | submitted to the | application. |     |     |     |     |
| ---------- | --------------------- | ---------------- | ------------ | --- | --- | --- | --- |
| We define  | a multiple regression | model based      | perfor-      |     |     |     |     |
Toevaluatetheaccuracyofthepredictionmodel,sev-
mancepredictionmodelwhichisrepresentedbasedon
|     |     |     |     | eral frequently | used measures | [51,52] | are considered |
| --- | --- | --- | --- | --------------- | ------------- | ------- | -------------- |
thebelowequation.
suchasmagnituderelativeerror(MRE),meanofMRE
(MMRE),rootmeansquareerror(RMSE),andpredic-
| =β +β | +β  | +(cid:3) |     |     |     |     |     |
| ----- | --- | -------- | --- | --- | --- | --- | --- |
y 0 1 x 1 2 x 2 (1) tionwithin25%oftheactualvalue.Thedefinitionsof
themeasuresarediscussedbelow.
whereyrepresentstheperformance, x representsthe (cid:129) Themagnitudeofrelativeerror(MRE)iscalculated
1
number of microservices in the application and x 2 asgivenbelow.
| represents                            | the number | of user requests given | to the  |     |                                          |     |     |
| ------------------------------------- | ---------- | ---------------------- | ------- | --- | ---------------------------------------- | --- | --- |
| microservicesapplication.Thevaluesofx |            |                        | andx    |     |                                          |     |     |
|                                       |            |                        | 1 2 are |     | ActualResponseTime−EstimatedResponseTime |     |     |
MRE=
consideredastheindependentvariablesandthecoef- ActualResponseTime
| ficients  | β , β and β | represent the constant | values.     |     |     |     | (2) |
| --------- | ----------- | ---------------------- | ----------- | --- | --- | --- | --- |
|           | 1 2 0       |                        |             |     |     |     |     |
| Sometimes | during the  | calculation, error     | is induced, |     |     |     |     |
whichisrepresentedusing(cid:3).
Table5 Datasetofmicroservicesbasedapplicationsfromliterature
S.No Nameofapplication #Modules #Userrequests Responsetime(ms)
| 1   | SockShopapplication[42]          |     |     | 9   | 500  | 425.51  |     |
| --- | -------------------------------- | --- | --- | --- | ---- | ------- | --- |
| 2   | eShopper[43]                     |     |     | 9   | 1000 | 666.5   |     |
| 3   | TrainTicket[43]                  |     |     | 40  | 100  | 249.32  |     |
| 4   | Stan’sRobotShop[44]              |     |     | 12  | 50   | 47.2    |     |
| 5   | WebApplication[45]               |     |     | 6   | 1051 | 934     |     |
| 6   | e-ShopApplication[46]            |     |     | 5   | 100  | 1219    |     |
| 7   | fabricstoreinformationsystem[47] |     |     | 5   | 300  | 3703.2  |     |
| 8   | xyzapplication[48]               |     |     | 4   | 1100 | 300     |     |
| 9   | WebApplication[49]               |     |     | 7   | 1676 | 232.67  |     |
| 10  | WebShopApplication[50]           |     |     | 5   | 1500 | 321.645 |     |
123

44 Page 22 of 26 Journal of Grid Computing (2024) 22:44
(cid:129) MMREisthemeanoftheMREsofalltheapplica- wherenisthenumberofapplicationschosenfor
tions and it is used to evaluate the prediction per- evaluationofperformance.
formanceofthemodel.TheMeanofMREiscal- (cid:129) Standardisedaccuracy(SA)isoneofthepreferred
culatedas measurements for comparing the performance of
MAE-basedpredictionmodels.Itisdefinedasfol-
1 (cid:2)n lows:
MMRE = ( MRE ) (3)
i
n
i=1 SA=1− MAE Pj ×100 (7)
MAE
guess
(cid:129) The Root Mean Square Error (RMSE) measures
the difference between the actual and estimated where MAE istheMAEoftheproposedapproach
Pj
responsetimes.Itisusedtocalculatethestandard and MAE is the value of MAE of a random
guess
deviationoftheerrorsthatarisewhentheproposed guess. The standard accuracy represents the impact
approach is applied to the datasets. RMSE is cal- of MAE whencomparedtoanyrandomguess.For
Pj
culatedasgivenbelow. performancepredictiontechniques,thevalueofMAE
shouldbelessandSAshouldbemaximum.
(cid:3)
(cid:4)
RMSE=
(cid:4) (cid:5)1 (cid:2)n
(ActualResponseTime−EstimatedResponseTime)2
n
i=1 6.4 Results
(4)
Theproposedregressionmethodisusedandthefunc-
tionforresponsetimepredictionisobtained.First,the
(cid:129) To check whether the predicted values are within variablesx andx fromthedatasettableareanalysed,
1 2
m%oftheactualvalues,weemployameasure,with andtheirvaluesareusedtocalculatetheresponsetime
mgenerallysetto25%insoftwareengineering.The using the regression model. To increase accuracy, we
measurePRED(25)iscalculatedas useaLeave-N-Outpolicy,inwhichwetrainthemodel
onlyonthefirsteightapplicationstocalculatethecoef-
k ficientsandthentestitontheremainingtwoapplica-
PRED(25)= (5)
n tions.Theestimatedcoefficientvaluesareshowninthe
responsetimepredictionfunction,whichisgiveninthe
where k is the number of observations for those equationbelow.
whose MRE is less than or equal to 0.25 and n is
thetotalnumberofapplications. y =1944.5075−47.8322x −0.8573x (8)
1 2
(cid:129) Becausethepreviouslydiscussedmeasuresarecri-
tiquedandreactdifferentlywhenevaluatingpredic- Usingthecalculatedcoefficientvaluesβ =1944.50
0
tionmodels,twoadditionalmeasuresareproposed 75,β =-47.8322,andβ =-0.8573,wetesttheremain-
1 2
[23].The mean absoluteerror(MAE) isunbiased ing two applications. The response times calculated
andiscalculatedasfollows. using the generated coefficients are presented in the
Table 6. Due to lack of application data for different
1 (cid:2)n microservices, the proposed model does not generate
MAE=
n i=1
|ActualResponseTimei −EstimatedResponseTimei |
better accuracy values. In machine learning, datasets
(6) playakeyroleinimprovingtheaccuracyofprediction
Table6 Applicationofregressionmodelontestdata
S.No ActualRT(ms) PredictedRT(ms) MRE
9 232.67 183.8473 0.209
10 321.645 411.3965 -0.279
123

| Journal of Grid Computing (2024) 22:44 |     |     |     |     |     |     | Page 23 of 26    44 |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
Table7 Accuracyofthepredictionmodel
| Model         |     | MMRE  | RMSE    | PRED(25) |     | MAE    |     | SA    |
| ------------- | --- | ----- | ------- | -------- | --- | ------ | --- | ----- |
| Proposedmodel |     | 0.348 | 719.125 | 0.5      |     | 332.25 |     | 66.75 |
and classification problems. The proposed regression theproposedregressionmodelandtheactualresponse
model works as recommendation system for estimat- times are compared and presented as line graph as
ingtheresponsetimerequiredforprocessingtheuser showninFigure19.Thex-axisrepresentstheapplica-
requestsgiventomicroservices. tions and y-axis represents the responsetimes inmil-
liseconds.Fromthegraph,itisclearthatthepredicted
|     |     |     |     | response times | are little | closer to | the actual | response |
| --- | --- | --- | --- | -------------- | ---------- | --------- | ---------- | -------- |
6.5 PerformanceofProposedRegressionModel
timesoftheapplications.
Theaccuracyoftheproposedregressionmodeliseval-
uated using the metrics presented in Section 6.3 and 7 ThreatstoValidity
| the values | are presented | in Table 7. From | the results, |     |     |     |     |     |
| ---------- | ------------- | ---------------- | ------------ | --- | --- | --- | --- | --- |
SA value is 66.75% and as stated before, due to lack The following threats to validity have been identified
ofdatasetofmicroservicesapplications,theaccuracy
intheproposedwork:
| of the models | is less. | However, the accuracy | can be |                         |            |         |        |          |
| ------------- | -------- | --------------------- | ------ | ----------------------- | ---------- | ------- | ------ | -------- |
|               |          |                       |        | (cid:129) The empirical | evaluation | carried | out on | the pro- |
improvedbyapplyingoptimizationtechniquessuchas
posedframeworkisdoneonacasestudyapplica-
gradientdescenttoformthebestfitregressionmodel
tionwhichisverysmallandhasonlyfourmicroser-
forthechosendatasetapplications.
|     |     |     |     | vices. So, | a detailed                | empirical | analysis should | be   |
| --- | --- | --- | --- | ---------- | ------------------------- | --------- | --------------- | ---- |
|     |     |     |     | carried    | out on large applications |           | or consider     | mul- |
6.6 Comparison tiple applications for analysis to arrive at such a
conclusionthatmicroserviceswithmicrofrontends
The proposed prediction function is computed using performbetter.
firsteightapplicationsbyapplyingregressionanalysis (cid:129) Intheempiricalinvestigation,themaximumwork-
leavingoneapplicationineachiteration.Thevaluesof loadgiventotheapplicationis10000requestsonly
coefficients are computed and the response times are duetolackofhardwareandtoolsupport.Asinreal-
generatedforeachapplication.Theresponsetimesby time,microservicesbasedwebapplicationsreceive
Fig.19 Differentmeasures
fortheproposedprediction
model
123

| 44   Page 24 of 26 |     |     |     |     |     | Journal of Grid Computing (2024) 22:44 |     |     |
| ------------------ | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- |
thousandsandlakhsofrequest,athoroughtesting InformationandCommunicationTechnologies(AICT),pp.
| isrequired. |     |     |     | 1-4.IEEE,(2020) |     |     |     |     |
| ----------- | --- | --- | --- | --------------- | --- | --- | --- | --- |
(cid:129) 3. Bucchiarone, A., Dragoni, N., Dustdar, S., Larsen, S.T.,
Sincethedatasetrelatedtoperformancfeofmicroser-
Mazzara,M.:Frommonolithictomicroservices:Anexpe-
vicesishardtofind,theproposedpredictionmodel
riencereportfromthebankingdomain.IEEESoftw.35(3),
| is constructed | using only | ten applications. | As  | 50–55(2018) |     |     |     |     |
| -------------- | ---------- | ----------------- | --- | ----------- | --- | --- | --- | --- |
observedfromtheresults,themodelframedisnot 4. Ponce,F.,Marquez,G.,Astudillo,H.:Migratingfrommono-
lithicarchitecturetomicroservices:ARapidReview.In2019
accurateenoughtoclaim.Hence,predictionmodel
38thInternationalConferenceoftheChileanComputerSci-
canbegeneratedbyusinghugedataonly.
enceSociety(SCCC),pp.1-7.IEEE,(2019)
|     |     |     |     | 5. Raj, | V., Ravichandra, | S.: Microservices: | A   | perfect SOA |
| --- | --- | --- | --- | ------- | ---------------- | ------------------ | --- | ----------- |
basedsolutionforEnterpriseApplicationscomparedtoWeb
|     |     |     |     | Services. | In 2018 | 3rd IEEE International | Conference | on  |
| --- | --- | --- | --- | --------- | ------- | ---------------------- | ---------- | --- |
8 Conclusion
recenttrendsinelectronics,information&communication
technology(RTEICT)pp.1531-1536.IEEE(2018)
PerformanceisoneoftheveryimportantQoSparame- 6. Raj,V.,Sadam,R.:Performanceandcomplexitycomparison
tersforanysoftwareapplicationasithasmajorimpact ofserviceorientedarchitectureandmicroservicesarchitec-
ture.Int.J.Commun.Netw.Distrib.Syst.27(1),100–117
| on the business | and the customer | satisfaction. | On the |     |     |     |     |     |
| --------------- | ---------------- | ------------- | ------ | --- | --- | --- | --- | --- |
(2021)
otherhand,microservicesarchitectureistrendingand
|     |     |     |     | 7. Al-Debagy, | O., Martinek, | P.: A | comparative | review of |
| --- | --- | --- | --- | ------------- | ------------- | ----- | ----------- | --------- |
it has become a very popular style of designing large microservicesandmonolithicarchitectures.In2018IEEE
enterprise applications. Though microservices based 18th International Symposium on Computational Intelli-
genceandInformatics(CINTI),pp.000149-000154.IEEE,
applicationexhibitnumerousbenefitsoverotherstyles
(2018)
ofdesigningapplications,duetolargenumberofser-
8. Raj,V.,Sadam,R.:EvaluationofSOA-basedwebservices
vices and complexity of the application, the perfor- and microservices architecture using complexity metrics.
mance of the applications can still be improved. In SNComput.Sci.2,1–10(2021)
9. Raj,V.,Ravichandra,S.:Aservicegraphbasedextraction
| this paper, | an attempt to | improve the performance |     |     |     |     |     |     |
| ----------- | ------------- | ----------------------- | --- | --- | --- | --- | --- | --- |
ofmicroservicesfrommonolithservicesofservice?oriented
ofmicroservices,micro-frontendbasedmicroservices
architecture.Softw.Pract.Exper.52(7),1661–1678(2022)
application framework is proposed and comparative 10. Taibi,D.,Lenarduzzi,V.,Pahl,C.:Processes,motivations,
resultsarefoundtobesatisfactory.Also,aregression andissuesformigratingtomicroservicesarchitectures:An
empiricalinvestigation.IEEECloudComput.4(5),22–32
| model to predict | the performance | of the applications |     |     |     |     |     |     |
| ---------------- | --------------- | ------------------- | --- | --- | --- | --- | --- | --- |
(2017)
| based on number | of microservices | in the | application |               |            |             |             |              |
| --------------- | ---------------- | ------ | ----------- | ------------- | ---------- | ----------- | ----------- | ------------ |
|                 |                  |        |             | 11. Abdullah, | M., Iqbal, | W., Berral, | J.L., Polo, | J., Carrera, |
andthenumberofuserrequestsgiven.Acomparison D.: Burst-aware predictive autoscaling for containerized
oftheproposedregressionmodelwithamultiplesetof microservices. IEEE Trans. Serv. Comput. 15(3), 1448–
1460(2020)
metricsisalsopresented.However,gatheringdatasets
|     |     |     |     | 12. Zhou, | X., Peng, | X., Xie, T., Sun, | J., Ji, C., | Li, Wenhai, |
| --- | --- | --- | --- | --------- | --------- | ----------------- | ----------- | ----------- |
formicroservicesbasedapplicationwasamajorchal-
Ding,Dan:Deltadebuggingmicroservicesystemswithpar-
lengeandhence,consideringlargedatasetsforapply- alleloptimization.IEEETrans.Serv.Comput.15(1),16–29
| ing the machine | learning models | can be proposed | in  | (2019) |     |     |     |     |
| --------------- | --------------- | --------------- | --- | ------ | --- | --- | --- | --- |
13. Wei,H.,Rodriguez,J.S.,Garcia,O.N.T.:Deploymentman-
future.
|     |     |     |     | agement | and topology      | discovery of | microservice | applica-    |
| --- | --- | --- | --- | ------- | ----------------- | ------------ | ------------ | ----------- |
|     |     |     |     | tions   | in the multicloud | environment. | J. Grid      | Comput. 19, |
Declarations
1–22(2021)
14. Magableh,Basel,Almiani,Muder:AdeeprecurrentQnet-
worktowardsself?adaptingdistributedmicroservicearchi-
| Conflicts of | interest The authors | do not have any | conflict of |     |     |     |     |     |
| ------------ | -------------------- | --------------- | ----------- | --- | --- | --- | --- | --- |
tecture.Softw.Pract.Exper50(2),116–135(2020).Tomas
interest.
|     |     |     |     | Fernandez.: | MicroFrontends: | Microservices |     | for the Fron- |
| --- | --- | --- | --- | ----------- | --------------- | ------------- | --- | ------------- |
tend
|     |     |     |     | 15. https://semaphoreci.com/blog/microfrontends. |     |     |     | Accessed |
| --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | -------- |
19-Feb-2023
References
16. Peltonen,S.,Mezzalira,L.,Taibi,D.:Motivations,benefits,
andissuesforadoptingmicro-frontends:amultivocalliter-
1. Lenarduzzi,V.,Lomio,F.,Saarimaki,N.,Taibi,D.:Does aturereview.Inf.Softw.Technol.136,106571(2021)
migrating a monolithic system to microservices decrease 17. Prajwal,Y.,Parekh,J.V.,Shettar,R.:Abriefreviewofmicro-
thetechnicaldebt?J.Syst.Softw.169,110710(2020) frontends.UnitedInt.J.Res.Technol2,123–126(2021)
2. Kuryazov, D., Jabborov, D., Khujamuratov, B.: Towards 18. Joseph, C.T., Chandrasekaran, K.: IntMA: Dynamic
decomposingmonolithicapplicationsintomicroservices.In Interaction-aware resource allocation for containerized
2020IEEE14thInternationalConferenceonApplicationof
123

Journal of Grid Computing (2024) 22:44 Page 25 of 26 44
microservices in cloud environments. Journal of Systems 36. Yan,M.,Liang,X.,Lu,Z.,Wu,J.,Zhang,W.:HANSEL:
Architecture111,101785(2020) adaptive horizontal scaling of microservices using Bi-
19. Sampaio, A.R., Rubin, J., Beschastnikh, I., Rosa, N.S.: LSTM.Appl.SoftComput.105,107216(2021)
Improving microservice-based applications with runtime 37. Srirama,S.N.,Adhikari,M.,Paul,S.:Applicationdeploy-
placementadaptation.J.Int.Serv.Appl.10(1),1–30(2019) mentusingcontainerswithauto-scalingformicroservices
20. ZargarAzad,M.,Ashtiani,M.:Anauto-scalingapproachfor incloudenvironment.J.Netw.Comput.Appl.160,102629
microservicesincloudcomputingenvironments(2023) (2020)
21. Cortellessa, V., Di Pompeo, D., Eramo, R., Tucci, M.: A 38. Wei,H.,Rodriguez,J.S.,Garcia,O.N.T.:Deploymentman-
model-driven approach for continuous performance engi- agement and topology discovery of microservice applica-
neeringinmicroservice-basedsystems.J.Syst.Softw.183, tionsinthemulticloudenvironment.J.GridComput.19(1),
111084(2022) 1–22(2021)
22. Raj,V.,Ravichandra,S.:EnhancedServicePointApproach 39. Brondolin, R., Santambrogio, M.D.: A black-box moni-
for Microservices Based Applications Using Machine toringapproachtomeasuremicroservicesruntimeperfor-
Learning Techniques. In International Conference on mance. ACM Trans. Archit. Code Optim. (TACO) 17(4),
AdvancedInformaticsforComputingResearchpp.78-90. 1–26(2020)
Cham:SpringerInternationalPublishing(2021) 40. Wang,D.,Yang,D.,Zhou,H.,Wang,Y.,Hong,D.,Dong,
23. Yang,C.,Liu,C.,Su,Z.:Researchandapplicationofmicro Q.,Song,S.:Anovelapplicationofeducationalmanage-
frontends.InIOPconferenceseries:materialsscienceand mentinformationsystembasedonmicrofrontends.Proce-
engineeringvol.490,p.062082.IOPPublishing(2019) diaComput.Sci.176,1567–1576(2020)
24. Prajwal, Y., Parekh, J. V., Shettar, R.: A brief review of 41. Cully,K.:PerformanceofMicroservicesResultData.(2021)
micro-frontends.UnitedInt.J.Res.Technol.,2(8)(2021) https://dx.doi.org/10.21227/hhf7-8b30
25. Al Qassem, L.M., Stouraitis, T., Damiani, E., Elfadel, 42. Joseph, C.T., Chandrasekaran, K.: IntMA: Dynamic
I.A.:ProactiveRandom-ForestAutoscalerforMicroservice interaction-aware resource allocation for containerized
ResourceAllocation.IEEEAccess11,2570–2585(2023) microservicesincloudenvironments.J.Syst.Archit.111,
26. Yan,M.,Liang,X.,Lu,Z.,Wu,J.,Zhang,W.:HANSEL: 101785(2020)
Adaptive horizontal scaling of microservices using Bi- 43. Cortellessa, V., Di Pompeo, D., Eramo, R., Tucci, M.: A
LSTM.Appl.SoftComput.105,107216(2021) model-driven approach for continuous performance engi-
27. Aydemir,F.,Basciftci,F.:BuildingaPerformanceEfficient neeringinmicroservice-basedsystems.J.Syst.Softw.183,
CoreBankingSystemBasedontheMicroservicesArchitec- 111084(2022)
ture.J.GridComput.20(4),37(2022) 44. Xu,M.,Song,C.,Ilager,S.,Gill,S.S.,Zhao,J.,Ye,K.,Xu,
28. Noorabad, R., Charkari, N.M., Nogoorani, S.D.: PoMic: C.:CoScal:Multifacetedscalingofmicroserviceswithrein-
Dynamic Power Management of VM-Microservices in forcementlearning.IEEETrans.Netw.Serv.Manag.19(4),
OvercommittedCloud.J.GridComput.21(1),12(2023) 3995–4009(2022)
29. Taibi,D.,Spillner,J.,Wawruch,K.:Serverlesscomputing- 45. Saransig,A.,Tapia,F.:Performanceanalysisofmonolithic
wherearewenow,andwhereareweheading?IEEESoftw. and micro service architectures?containers technology. In
38(1),25–31(2020) TrendsandApplicationsinSoftwareEngineering:Proceed-
30. Raj,V.,Sadam,R.:PatternsforMigrationofSOABased ingsofthe7thInternationalConferenceonSoftwareProcess
Applications to Microservices Architecture. J. Web Eng. Improvement(CIMPS2018)7pp.270-279.(2019)Springer
20(5),1229–1246(2021) InternationalPublishing
31. Wei,H.,Rodriguez,J.S.,Garcia,O.N.T.:Deploymentman- 46. Shabani,I.,Meziu,E.,Berisha,B.,Biba,T.:Designofmod-
agement and topology discovery of microservice applica- erndistributedsystemsbasedonmicroservicesarchitecture.
tions in the multicloud environment. J. Grid Comput. 19, Int.J.Adv.Comput.Sci.Appl.,12(2)(2021)
1–22(2021) 47. Rahmatulloh,A.,Nugraha,F.,Gunawan,R.,Darmawan,I.:
32. Li,S.,Zhang,H.,Jia,Z.,Li,Z.,Zhang,C.,Li,J.,Gao,Q., November. Event-Driven Architecture to Improve Perfor-
Ge,J.,Shan,Z.:Adataflow-drivenapproachtoidentifying manceandScalabilityinMicroservices-BasedSystems.In
microservicesfrommonolithicapplications.J.Syst.Softw. 2022 International Conference Advancement in Data Sci-
157,110380(2019) ence,E-learningandInformationSystems(ICADEIS)pp.
33. Brondolin, R., Santambrogio, M.D.: A black-box moni- 01-06.IEEE(2022)
toringapproachtomeasuremicroservicesruntimeperfor- 48. Villamizar, M., Garces, O., Castro, H., Verano, M., Sala-
mance. ACM Trans. Archit. Code Optim. (TACO) 17(4), manca, L., Casallas, R., Gil, S.: September. Evaluating
1–26(2020) themonolithicandthemicroservicearchitecturepatternto
34. Cinque, M., Della Corte, R., Pecchia, A.: Microservices deploywebapplicationsinthecloud.In201510thCom-
monitoring with event logs and black box execution trac- putingColombianConference(10CCC)pp.583-590.IEEE
ing.IEEETrans.Serv.Comput.(2019) (2015)
35. Vayghan, L.A., Saied, M.A., Toeroe, M., Khendek, F.: A 49. Salunkhe,P.S.:MicroservicesvsMonolithicArchitecture:
Kubernetescontrollerformanagingtheavailabilityofelastic LoadTestinginAWSonReactJSWebApplicationforPer-
microservicebasedstatefulapplications.J.Syst.Softw.175, formance(Doctoraldissertation,Dublin,NationalCollege
110924(2021) ofIreland)(2022)
123

44 Page 26 of 26 Journal of Grid Computing (2024) 22:44
50. Barczak,A.,Barczak,P.M.,Toledo,M.:Performancecom- 52. Menzies, T., Yang, Y., Mathew, G., Boehm, B., Hihn, J.:
parisonofmonolithandmicroservicesbasedapplications Negativeresultsforsoftwareeffortestimation.Empir.Softw.
51. Sarro,F.,Petrozziello,A.andHarman,M.:Multi-objective Eng.22,2658–2683(2017)
softwareeffortestimation.InProceedingsofthe38thInter-
nationalConferenceonSoftwareEngineeringpp.619-630
(2016) Publisher’sNote SpringerNatureremainsneutralwithregard
tojurisdictionalclaimsinpublishedmapsandinstitutionalaffil-
iations.
SpringerNatureoritslicensor(e.g.asocietyorotherpartner)
holdsexclusiverightstothisarticleunderapublishingagreement
withtheauthor(s)orotherrightsholder(s);authorself-archiving
oftheacceptedmanuscriptversionofthisarticleissolelygov-
ernedbythetermsofsuchpublishingagreementandapplicable
law.
123