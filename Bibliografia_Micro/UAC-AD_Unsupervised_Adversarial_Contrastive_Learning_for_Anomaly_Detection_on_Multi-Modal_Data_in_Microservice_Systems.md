IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024 3887
| UAC-AD:  |     |     |      | Unsupervised |              |     | Adversarial |         |     | Contrastive |     |     |     |     |
| -------- | --- | --- | ---- | ------------ | ------------ | --- | ----------- | ------- | --- | ----------- | --- | --- | --- | --- |
| Learning |     |     | for  | Anomaly      |              |     | Detection   |         | on  | Multi-Modal |     |     |     |     |
|          |     |     | Data | in           | Microservice |     |             | Systems |     |             |     |     |     |     |
HongyiLiu ,XiaosongHuang,MengxiJia ,TongJia ,JingHan,ZhonghaiWu ,andYingLi ,Member,IEEE
Abstract—Toensurethestabilityandreliabilityofmicroservice many instances (e.g., virtual machines or containers). How-
| systems, timely | and       | accurate    | anomaly | detection   | is     | of utmost     | im-        |     |           |            |     |              |     |         |
| --------------- | --------- | ----------- | ------- | ----------- | ------ | ------------- | ---------- | --- | --------- | ---------- | --- | ------------ | --- | ------- |
|                 |           |             |         |             |        |               | ever, with | the | scale and | complexity | of  | microservice |     | systems |
| portance.       | Recently, | considering |         | the lack of | labels | in real-world |            |     |           |            |     |              |     |         |
expandingrapidly,failureisinevitable.Whenaninstancefails,
scenariosandthecollaborativeandcomplementaryrelationships
ofmulti-modaldatainreflectingsystemanomalies,unsupervised itmaydegradetheperformanceoftheentiresystem,impactuser
multi-modalanomalymethodshavebeenproposed.However,ex- experience,andresultinsubstantialfinanciallosses.Therefore,
istingmethodsfacechallengesineffectivelydistinguishingnormal itiscrucialtoproactivelydetectanomaliesandmitigatefailures
hardsamples(theyarenormalbuthardtoclassifycorrectly)from
toguaranteethereliabilityofthemicroservicesystems.Inreal-
| anomalies.      | This is | mainly   | caused  | by two aspects. | First,      | the   | hard               |     |          |     |            |     |            |       |
| --------------- | ------- | -------- | ------- | --------------- | ----------- | ----- | ------------------ | --- | -------- | --- | ---------- | --- | ---------- | ----- |
|                 |         |          |         |                 |             |       | world microservice |     | systems, |     | many types | of  | monitoring | data, |
| sample patterns | are     | complex. | Second, | the             | convergence | speed | is                 |     |          |     |            |     |            |       |
inconsistentbetweenhardandsimplesamples.Toovercomethese includingmetrics,logs,alerts,andtraces,playanessentialrole
issues,weproposeanunsupervisedadversarialcontrastivemulti- insoftwarereliabilityengineering.Especiallyforlogandmetric
modalanomalydetectionmethod(UAC-AD).Weutilizecontrastive data, operators continuously collect them for prompt anomaly
learningtohelplearnthecomplexpatternsofhardsamplesanden-
|     |     |     |     |     |     |     | detection. | Metric | data | includes | system-level |     | metrics | (such as |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | -------- | ------------ | --- | ------- | -------- |
largethedistancebetweenhardandanomalysamples.Meanwhile,
|     |     |     |     |     |     |     | CPU utilization, |     | memory | usage, | and | network | bandwidth) | and |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------ | --- | ------- | ---------- | --- |
theadversarialframeworkautomaticallyidentifieshardsamples
|     |     |     |     |     |     |     | user-perceived |     | metrics | (like average | response |     | time, | error rate, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ------------- | -------- | --- | ----- | ----------- |
andfine-grainedadjuststhetrainingweightstoeachmodalitypart
ofthesehardsamples.Inthiscase,Thehardsampleproblemsof etc.).Logsaresemi-structuremessagesprinted,whichtypically
twoaspectscanbealleviated.WeextensivelyevaluateUAC-ADon capture operational information about hardware and software,
| two open-source | simulated |     | datasets | and a real | industrial |     | dataset |     |     |     |     |     |     |     |
| --------------- | --------- | --- | -------- | ---------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
includingstatechanges,debugoutputs,andsystemalerts.
| from a large | communication |     | company. | Extensive |     | experimental |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | -------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Asmanuallyidentifyinganomaliesisimpracticalandprone
resultsdemonstratetheeffectivenessofourapproachinanomaly
toerrors,significanteffortsareinvestedinautomatedanomaly
detection.Wealsoreleasethecodeanddatasetforreplicationand
futureresearch. detection. Some methods rely on metrics to detect anomalies
|             |                   |              |     |           |             |            | by probability |            | density | estimation, | outlier    | detection, |            | or autore- |
| ----------- | ----------------- | ------------ | --- | --------- | ----------- | ---------- | -------------- | ---------- | ------- | ----------- | ---------- | ---------- | ---------- | ---------- |
| Index       | Terms—Adversarial |              |     | learning, | anomaly     | detection, |                |            |         |             |            |            |            |            |
|             |                   |              |     |           |             |            | gressive       | bias (more | details | are         | introduced | in         | subsection | II-A).     |
| contrastive | learning,         | microservice |     | systems,  | multi-modal |            | data,          |            |         |             |            |            |            |            |
|             |                   |              |     |           |             |            | Other methods  |            | rely on | logging     | to detect  | anomalies  |            | through    |
softwarereliability,unsupervisedlearning.
|           |     |      |              |             |              |     | keyword               | matching | or            | learning-based |                 | methods | (more      | details     |
| --------- | --- | ---- | ------------ | ----------- | ------------ | --- | --------------------- | -------- | ------------- | -------------- | --------------- | ------- | ---------- | ----------- |
|           |     |      |              |             |              |     | are introduced        |          | in subsection |                | II-B). However, |         | in         | the context |
|           |     | I.   | INTRODUCTION |             |              |     |                       |          |               |                |                 |         |            |             |
|           |     |      |              |             |              |     | of microservice       |          | systems,      | relying        | on              | only    | one single | modal       |
| RECENTLY, |     | with | more and     | more online | applications |     | mi-                   |          |               |                |                 |         |            |             |
|           |     |      |              |             |              |     | data is insufficient. |          | It is         | unable         | to depict       | the     | status     | of systems  |
gratingtocloudplatforms,microservicearchitecturehas preciouslytojudgewhetheranomaliesoccur[1],[2].Existing
received great attention. They are widely adopted due to their unsupervised multi-modal anomaly detection methods mainly
capabilitytoallowdevelopment,deployment,update,andscale
relyonreconstruction-basedapproaches[3],assumingthatnor-
foreachservice.Amicroservicesystemisalargesystemwith mal data is easier to reconstruct than anomalous data. These
|     |     |     |     |     |     |     | methods | learn | the distribution |     | of normal | data | by fitting | unla- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------------- | --- | --------- | ---- | ---------- | ----- |
Manuscriptreceived25October2023;revised10May2024;accepted28 beled data and identifying anomalies based on reconstruction
| May2024.Dateofpublication7June2024;dateofcurrentversion30December |     |     |     |     |     |     | errors. |     |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
2024.ThisworkwassupportedbythePKU-ZTECooperationResearchRroject.
(HongyiLiu,XiaosongHuang,andMengxiJiacontributedequallytothiswork.) However, these existing reconstruction-based multi-modal
(Correspondingauthor:YingLi.) anomalydetectionmethodsstruggletodistinguishbetweenhard
Hongyi Liu, Mengxi Jia, Zhonghai Wu, and Ying Li are with the andanomaloussamplesinthedecisionspace,leadingtolimited
| School of Software | &   | Microelectronics, |     | Peking University, |     | Beijing | 100871, |     |     |     |     |     |     |     |
| ------------------ | --- | ----------------- | --- | ------------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
anomalydetectionperformance.Inourwork,hardsamplesrefer
China(e-mail:hongyiliu@pku.edu.cn;mxjia@pku.edu.cn;wuzh@pku.edu.cn;
li.ying@pku.edu.cn). tonormalhardsamples,whichareapartofnormalsamples,but
XiaosongHuangiswiththeSchoolofComputerScience,PekingUniversity,
aredifficultforthemodeltoclassifycorrectlyandcanbeeasily
Beijing100871,China(e-mail:hxs@stu.pku.edu.cn).
classifiedasabnormalsamples[4],[5].Theunderlyingreasons
TongJiaiswithInstituteforArtificialIntelligence,PekingUniversity,Beijing
100871,China(e-mail:jia.tong@pku.edu.cn). for this limitation are twofold: (1) Complex Combination: In
JingHaniswiththeDepartmentofAlgorithm,ZTE,Shenzhen518083,China
|     |     |     |     |     |     |     | microservice | systems, |     | the combination |     | of normal |     | samples is |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | --------------- | --- | --------- | --- | ---------- |
(e-mail:han.jing28@zte.com.cn).
complex.(onelogpatterncanbecombinedwithmultiplemetric
DigitalObjectIdentifier10.1109/TSC.2024.3411481
1939-1374©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

3888 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
improvetheperformanceofanomalydetection.Somestudies[6]
haveconfirmedthattime-alignedmulti-modaldatareflectsthe
operational state of the system, while unaligned data reflects
inconsistent system states. Therefore, we consider the time-
alignedcombinationoflogsandmetricsaspositive(i.e.,normal)
samples and treat the unaligned combination as negative (i.e.,
abnormal) samples. Then we increase the distance between
positiveandnegativesamples,alleviatingthefirstchallengeof
hardsamples.
Moreover,inouradversarialtrainingphase,thediscriminator
canjudgethereconstructionperformanceofthegeneratorand
increase the weight of reconstruction learning for the parts
with poor reconstruction performance (i.e., hard samples for
thereconstruction-basedanomalydetectionmethods).Wefur-
thermoredesignseparatediscriminatorsagainsteachmodality
partofthemulti-modaldatatoachieveamodality-leveltraining
optimizationadjustmentforhardsamples.
Fig.1. TheMotivationofUAC-AD.Thefigureillustratesthefittingprocess
Ourcontributionsareasfollows:
ofAutoencoder(AE,i.e.,Method5inTableIII)andGAN(i.e.,Method6in (cid:2)
TableIII)forhardandsimplesamplesinthetrainingsetofDatasetA(introduced Weclarifytheproblemofinconsistentconvergencespeed
insectionIV-A1).Thehardsamplesaremarkedaccordingtothefalsepositives of hard samples for multi-modal anomaly detection in
identifiedbytheAE-basedanomalydetectionmodelthatcompletedthefirst
microservice systems, and we design a fine-grained ad-
epochofreconstructiontraining,whiletherestsamplesareconsideredassimple
samples.Thetopfiguredemonstratestheissueofinconsistentconvergencespeed versarial learning framework to adjust the convergence
betweenmulti-modalhardandsimplesamples:bothAEandGANconvergein speedofeachmodalitypartofmulti-modalhardsamples.
two epochs for simple samples, whereas hard samples require more epochs
Extensive ablation studies verify the effectiveness of the
toconverge.ThebottomfigurepresentstheperformanceofAEandGANfor
anomalydetection.Thesetwofiguresdemonstratethatadversariallearningcould proposedadversariallearningstrategy.
(cid:2)
adjusttheconvergencespeedbetweenhardandsimplesamplesandleadtoa Within the adversarial learning framework, we introduce
improvedanomalydetectionperformance.
contrastivelearningtoenhancethemodel’sunderstanding
of complex combinations of the multi-modal hard sam-
patterns to represent normal system states, and similarly, one ples. This widens the gap between hard and anomalous
metricpatterncanalsobecombinedwithmultiplelogpatterns samples in the decision space, thereby achieving better
to represent normal system states). In consideration that hard anomalydetectionperformance.Moreover,wereleaseour
samples are part of normal samples, the combination of hard codeandrelateddatasetsforbetterreplicationandfuture
samples is also complex. Existing reconstruction-based meth- research[7].
ods fail to capture diverse and complex combinations of hard
samples,whichmayidentifythesehardsamplesasanomalies. II. RELATEDWORK
(2) Inconsistent Convergence Speed: As shown in Fig. 1, the
Recently, tremendous efforts have been devoted to anomaly
convergencespeedofsimpleandhardsamplesinmulti-modal
detection to ensure the reliability of large-scale systems. The
dataareinconsistent,leadingtomodelsoverfittingsimplesam-
anomalydetectionmethodsareusuallybasedonlogs,metrics,or
ples and underfitting hard samples, thus limiting the model’s
both.Inthissection,wefirstreviewtheanomalydetectionworks,
ability to model normal samples and consequently restricting
includingmetric-based,logging-based,andmulti-modal-based
theeffectivenessofanomalydetection.Forreconstruction-based
methods, which are closely related to our work. We then in-
anomaly detection methods, multi-modal hard samples may
troduce the key techniques we used in this paper, including
exhibitlargereconstructionerrorsinbothmodalitiesorinone
adversariallearningandcontrastivelearning.
singlemodality.Forthelattercase,fine-grained(modality-level
ratherthansample-level)trainingoptimizationadjustmentsare
A. Metric-BasedMethods
requiredtobalancethefittingdegreesofbothmodalities,achiev-
ing unified modeling of normal samples and obtaining better Metric data is a typical time series data collected from the
anomalydetectionperformance. monitors to monitor the running state of the instances at the
To address the two challenges of hard samples mentioned application or system level. According to the criterion for
above,weproposeanovelunsupervisedadversarialcontrastive anomalydetermination,theparadigmsofmetric-basedanomaly
learning-basedmethodforgenerallog-metricmulti-modaldata detectioncanbecategorizedintothreetypes.Densityestimation-
anomaly detection (UAC-AD). Specifically, we propose an basedmethods[8],[9],[10],[11]assumedthatthenormaldata
adversarial learning framework with contrastive learning. We conforms to a specific probability distribution and identified
utilizecontrastivelearningistolearnthecomplexcombinations anomaliesaccordingtotheprobabilitydensityofthedatapoints
of normal samples by enlarging the distance between normal orthelikelihoodofthedatapointsappearing.Zongetal.[10]
and anomaly samples so that the model can better distinguish andYairietal.[11]introducedtheGaussianmixturemodelsinto
betweenhardandabnormalsamples,reducefalsepositives,and their framework, facilitating the estimation of representation
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore. Restrictions apply.

LIUetal.:UAC-AD:UNSUPERVISEDADVERSARIALCONTRASTIVELEARNINGFORANOMALYDETECTIONONMULTI-MODAL 3889
densities. Clustering-based methods [12], [13], [14] assumed unexpectedbehaviorsinvolvingeitherlogs,metrics,orbothof
thattheoutlierdataistheanomalyandidentifiedtheanomalies them.So,toachievebetterperformance,theresearchersattempt
accordingtothedistancefromthedatapointtotheclustercenter. toanalyzemorethanonedatasourcecomprehensivelytoreveal
Taxetal.[12]andRuffetal.[13]constructedaclusterfromthe the actual anomalies. Some research [1], [29], [30], [31], [32]
representationofthenormaldatawithnonlineartransformation. proposedintegratingtracingdatawithlogsormetricstogroup
Reconstruction-basedmethods[15],[16],[17],[18],[19],[20] logsormetricsfromthesameexecutioncontext,aimingtobetter
assumed that the abnormal data is difficult to reconstruct, and learn data patterns in microservices systems and assist in pin-
determinedtheanomaliesaccordingtothereconstructionerror. pointingfaultynodes.However,acquiringtracingdatarequires
Park et al. [15], and Ya et al. [16] used the LSTM or GRU to pre-instrumentation, making it challenging to apply to already
capture the temporal dependency and the Variational AutoEn- deployedmicroservices.Moreover,thecollectionoftracingdata
coder(VAE)toreconstruct.Hangetal.[17],andJunetal.[18], imposes additional overhead on running services, potentially
both of which incorporated Graph Attention Networks (GAT) constraining service response times. Lee et al. [28] proposed
tocapturespatialcorrelationsamongdimensionsinmultivariate a log-metric modal anomaly detector via a semi-supervised
timeseries.Estimation-basedmethodspresupposespecificdata learningmethodtoeffectivelydetectanomalies.Inconsideration
distributions,clustering-basedmethodsrelyonhyperparameter ofscarcelabeldatainpractice,Zhaoetal.[3]andChenetal.[33]
configurations, and reconstruction-based methods are vulner- designedunsupervisedanomalydetectionmethodsbasedonlog
able to hard samples within training data. Consequently, de- and metric data with a concatenation feature fusion strategy
ployingtheseapproachesinpracticalproductionenvironments andreconstruction-basedcriterion.Zhangetal.[34]conducted
presentsformidablechallenges. autoregressive anomaly detection separately based on log and
metric modalities and fused the results according to anomaly
B. Log-BasedMethods density. However, existing unsupervised methods struggle to
adapttotheintricatedatadisparitiesbetweenmultiplemodalities
Logdataissemi-structuredtextcollectedbyinstancesatthe
andaresusceptibletotheinfluenceofhardsamples,restricting
applicationorsystemlevel.Logsarewidelyadoptedinpractice
theaccuracyofanomalydetection.
foranomalydetection.Traditionallog-basedanomalydetection
methodsareusuallydesignedtoidentifykeywordsinlogslike
“error”or“fail”orcountthenumberoflogsthatappearduring D. AdversarialLearning
a period of time. However, negative keywords or the number Adversarial Learning, exemplified by the Vanilla Gener-
of logs within a period of time could not accurately imply in- ative Adversarial Network (GAN) proposed by Goodfellow
stancefailures.Thus,advancedapproachesareproposed,which et al. [35], is a fundamental technique in machine learning.
followasimilarworkflow:logparsing,featureextraction,and This approach involves a generator and a discriminator. The
anomaly detection. These works mine the log patterns (e.g., generator reconstructs input data and attempts to deceive the
sequentialfeature,semanticfeature)ofnormalexecutions and discriminator,whilethediscriminatordiscernswhethertheinput
judge whether an anomaly occurs when the current execution dataoriginatesfromrealorgeneratedsources.LetGdenotethe
deviatesfromthelearnednormalexecution.Forexample,Xuet generatornetwork,andDdenotethediscriminatornetwork.The
al. [21] constructed normal and abnormal space of log event optimizationobjectiveofGANis:
count matrix using Principal Component Analysis (PCA) to
detect anomalies. Lin et al. [22] and He et al. [23] designed minmaxV(G,D)=E
x∼p(x)
[log(D(x))]
clustering-basedmethodstoidentifyproblemsofonlineservice G D
systems.Duetal.[24]predictedthelogsthatmayappearaftera +E x∼p(x) [log(1−D(G(x)))]. (1)
slidingwindowutilizingtheLSTMmodel.Zhangetal.[25]took
theentiresequenceintoaccountandtrainedanattention-based NumerousstudieshaveexploredtheapplicationofGANsin
Bi-LSTM model on the log sequence for supervised learning. anomaly detection, primarily focusing on unimodal data types
Wei et al. [26] employed feature engineering to extract log suchasimages[36],[37]andtimeseries[19],[20].Incontrast
featurevectors.TheyutilizedaGRU-basedAutoencodertolearn tothesesingle-modalapproaches,ourproposedmethoddelves
reconstructionandidentifiedanomaliesbasedonreconstruction intotherealmofmulti-modaldata,investigatinghowGANscan
errors.Yuanyuanetal.[27]extractedsemanticfeaturesoflogs beharnessedtoenhancetheeffectivenessofanomalydetection
using Transformers. They employed LSTM and CNN to cap- acrossdiversedatamodalities.
ture both global and local correlations within log sequences,
enhancing the performance of supervised anomaly detection. E. ContrastiveLearning
However,existingmethodsforlog-basedanomalydetectionare
Contrastive learning is a self-supervised learning method in
constrainedbytheirrelianceonsingulardatasources,makingit
deeplearningthatdoesnotrequireextraannotationinformation
challengingtomeetthereal-worlddemandforaccuracy.
to augment the representation of data. Triplet loss [38] is a
typical method to achieve contrastive learning, which reduces
C. Multi-ModalBasedMethods the distance between x and x+, and increases the distance
Althoughsingle-modal-basedanomalydetectionmethodsare betweenxandx−,asshownin(2).Wherex+isapositivesample
confirmedeffective,[28]demonstratedthatitmayneglectsome thatissimilartox,x− isanegativesamplethatisdissimilarto
anomalieswhenonlyrelyingonsingledata.TheFaultscancause x,αisahyperparameterusedtoadjustthedifferencebetween
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore. Restrictions apply.

3890 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
Fig.2. TheUAC-ADpipelinecomprisesageneratorandadiscriminatormodule.Thegoalistoaccuratelyfitthenormalsampledistributionanddistinguish
anomaliesutilizingmulti-modaldatathroughanadversarialmechanism.Thegenerator,withfourcomponents,i.e.,logmodeling,metricmodeling,multi-modal
self-attention,anddecoder,aimstofitmulti-modalnormaldatathroughreconstruction.Thediscriminator,comprisinglogandmetricsdiscriminator,effectively
guidesthegeneratorbydistinguishingbetweenoriginalandreconstructeddata.
twodistances.
L=max(0,d(f(x),f(x +))−d(f(x),f(x −))+α). (2)
Toourknowledge,thereareveryfewworks[6],[39]thatat-
tempttousecontrastivelearninginmulti-modalanomalydetec-
tionformicroservices.Themostrelevantwork,CL-MMAD[6],
employsCNNandLSTMtoextractfeaturesfrommetricsand
tracesseparately.Itthenutilizescontrastivelearningtonarrow
downthedistancebetweenthesefeaturesinthefeaturespaceand
employs the distance of both features as anomaly scores. This
approachusescontrastivelossasthesoletrainingloss,enabling
ittodetectanomaliesrelatedtomodalinconsistenciesbutstrug-
glingtoadapttoanomalies thatexhibitmodalconsistency but Fig. 3. Illustration of the training and inferring phase of UAC-AD. The
temporalanomalies.Inourwork,wefusemulti-modalfeatures training phase incorporates multi-modal data modeling, reconstruction, and
discrimination.Thegeneratorusesamixoflossestofitthenormaldata,withthe
throughtimealignment.Wetreattimeblockswithmatchedlogs
discriminatordifferentiatingbetweenrealandgenerator-generatedsamplesto
andmetricsaspositivesamplesandthosewithunmatchedlogs refinethisfitness.Theinferringphasecentersonthegenerator’sreconstruction
andmetrics(generatedindifferenttimeblocks)asnegativesam- errors.Surpassingapredefinedthresholdindicatesananomaly.
ples.Thisfusioncontributestothereconstructionofmulti-modal
inputdatawithintimewindows,enablingfurtherlearningofthe
temporal correlations in multi-modal data. Consequently, our
reconstructionlossisemployedtolearnthedistributionofnor-
approach yields improved representations of multi-modal data
maldatabyminimizingtheerrorbetweeninputandoutputdata.
andbetteroverallperformance.
Simultaneously,theadversariallossisemployedtodeceivethe
discriminator,enablingthegeneratortoautomaticallyadjustthe
III. METHODOLOGY convergencespeedsforhardsamplesandsimplesamples.This
further facilitates the fitting of the distribution of normal data.
A. Overview
Moreover,thecontrastivelossisutilizedtoaidthegeneratorin
Our approach consists of two key modules, the Generator learningmulti-modaldatacombinationsoflogandmetricdata
and the Discriminator, as illustrated in Fig. 2. The Generator thatcorrespondtonormaloperationstatesinmicroservices.This
serves as an autoencoder and is employed to reconstruct the is achieved by preventing the learning of abnormal combina-
originaldata.TheDiscriminatoractsasaclassifier,distinguish- tions,therebyenhancingthedifferentiationbetweennormaland
ingbetweenoriginalandreconstructeddata,therebyeffectively abnormaldata.Thiscontrastivelossiscomputedbasedonmodel
guidingtheGeneratortofitthenormalsampledistribution.The outputsformatchedpairsandunmatchedpairs.Amatchedpair,
overview of the training and inference phases is illustrated in comprising logs and metric data collected at the same time
Fig.3. block,representsaunifiedsystemstateandisconsiderednormal.
•Inthetrainingphase,theGeneratorleveragesacombination In contrast, an unmatched pair consists of logs and metrics
ofreconstructionloss,adversarialloss,andcontrastiveloss.The collected at different time blocks, considered abnormal. The
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore. Restrictions apply.

LIUetal.:UAC-AD:UNSUPERVISEDADVERSARIALCONTRASTIVELEARNINGFORANOMALYDETECTIONONMULTI-MODAL 3891
Discriminator employs adversarial loss to distinguish whether templatesandleveragingthemtodifferentiatedifferentsystem
inputdataoriginatesfromrealorGenerator-generateddata.For statuses(normalorabnormal).
hard samples that are difficult to reconstruct and have larger Through the above data process, we convert raw logs and
reconstruction errors, the discriminator can distinguish them metricstoalignedmatchedtimeseriesdata,X =(X ,X )=
|     |     |     |     |     |     |     |     |                 |     |     |                  |     |     | l   | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | {x1,x2,...,xt}, |     |     | ∈Rt×(n+n(cid:4)) |     |     |     |     |
betweenrealorreconstructedwell.Todeceivethediscriminator, where X indicates the multi-
∈Rt×n
thegeneratorispushedtofitthenormaldatadistributionclosely. modal data, X indicates the processed log template
l
•Intheinferencephase,weprimarilyfocusonthegenerator’s features,X ∈Rt×n(cid:4) indicatesthesampledmetrics,tindicates
m
reconstructionerrors,whichindicatesthegapbetweenrealdata thetotalnumberoftimeblocks,nindicatesthetotalnumberof
andreconstructeddata.Whentheseerrorsexceedapredefined logtemplatetypes,n(cid:4)indicatesthetotalnumberofmetrics.The
threshold, we classify it as an anomaly, triggering an alert to goalofanomalydetectioninmulti-modaldataistoconstructa
modelF(Xi)topredictwhetherXicontainsanomaliesornot,
notifyoperationspersonnel.
The proposed method follows an instance-based approach where Xi ={xi,xi−1,...,xi−w−1} indicates the multi-modal
rather than a system-based approach. Therefore, we apply our data of the i th slide window, the w denotes the slide window
| model separately |        | to the | real-time  | data generated |            | by each | ser-   | size. |     |     |     |     |     |     |     |
| ---------------- | ------ | ------ | ---------- | -------------- | ---------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| vice instance    | within | the    | system for | anomaly        | detection. |         | If any |       |     |     |     |     |     |     |     |
instance reports an anomaly, we consider the entire system to C. GeneratorModule
beanomalous.Theadvantageofthisinstance-basedapproachis
|     |     |     |     |     |     |     |     | The structure |     | of the | generator | module | is shown | in  | Fig. 2. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | --------- | ------ | -------- | --- | ------- |
thatitallowsustopinpointthespecificinstance(s)experiencing
|           |       |               |        |         |     |                 |     | It is divided | into | four | parts: log | modeling, | metric | modeling, |     |
| --------- | ----- | ------------- | ------ | ------- | --- | --------------- | --- | ------------- | ---- | ---- | ---------- | --------- | ------ | --------- | --- |
| anomalies | while | also avoiding | issues | related |     | to inconsistent |     |               |      |      |            |           |        |           |     |
multi-modalself-attention,anddecoder.
| timestamps | across | different | services. | Many | existing |     | methods |               |     |             |     |               |     |        |        |
| ---------- | ------ | --------- | --------- | ---- | -------- | --- | ------- | ------------- | --- | ----------- | --- | ------------- | --- | ------ | ------ |
|            |        |           |           |      |          |     |         | Log Modeling: |     | We designed |     | a log encoder |     | module | to en- |
foranomalydetectioninlogsandmetrics,suchasHades[28],
|                                                     |     |     |     |     |     |     |     | code the        | relationships |          | between         | time blocks | further. |         | For i |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | -------- | --------------- | ----------- | -------- | ------- | ----- |
| OmniAnomaly[16],andDeepLog[24],alsoadoptaninstance- |     |     |     |     |     |     |     |                 |               |          |                 |             |          |         | th    |
|                                                     |     |     |     |     |     |     |     | sliding window, |               | we adopt | a Convolutional |             | Neural   | Network |       |
basedapproach.
|     |     |     |     |     |     |     |     | (CNN) to  | map low-dimensional |       |               | features | to high-dimensional |          |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | ----- | ------------- | -------- | ------------------- | -------- | --- |
|     |     |     |     |     |     |     |     | features. | Then we             | apply | a Transformer |          | encoder             | to learn | the |
B. DataPreprocessing time-association features between blocks, and then we obtain
|       |            |     |          |         |      |                |     | the log hidden                | layer | representation |     | for | the i sliding   |     | window |
| ----- | ---------- | --- | -------- | ------- | ---- | -------------- | --- | ----------------------------- | ----- | -------------- | --- | --- | --------------- | --- | ------ |
| Given | a sequence | of  | logs and | metrics | from | a microservice |     |                               |       |                |     |     | t h             |     |        |
|       |            |     |          |         |      |                |     | Zi ∈Rw×h,asshownin(3).WhereXi |       |                |     |     | indi c atesthei |     | slide  |
|       |            |     |          |         |      |                |     | l                             |       |                |     | l   |                 |     | th     |
system,thefirstchallengeoffusionmulti-modaldataistoalign
|          |             |     |          |      |       |             |     | window | of the log | template | feature, | h denotes | the | hidden | size |
| -------- | ----------- | --- | -------- | ---- | ----- | ----------- | --- | ------ | ---------- | -------- | -------- | --------- | --- | ------ | ---- |
| the logs | and metrics | at  | the same | time | block | to indicate | the |        |            |          |          |           |     |        |      |
oftheneuralnetwork.
| same system | state. | The | metrics are | in the | typical | time | series |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ----------- | ------ | ------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Zi =TransEncoder(CNN(Xi)).
format with a certain sampling interval, which can be easily (3)
|     |     |     |     |     |     |     |     |     |     | l   |     |     | l   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
handled.However,thelogsaresemi-structuredorunstructured
|     |     |     |     |     |     |     |     | Metric | Modeling: | Similar | to  | Log Modeling, |     | we use | CNN |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | --- | ------------- | --- | ------ | --- |
messages(texts)withthecorrespondingtimestamp,whichcon-
|                 |     |         |               |     |            |     |       | and Transformer |              | encoder | to capture | the    | correlation           | between |     |
| --------------- | --- | ------- | ------------- | --- | ---------- | --- | ----- | --------------- | ------------ | ------- | ---------- | ------ | --------------------- | ------- | --- |
| tains variables | and | impedes | log analysis. |     | Therefore, | we  | adopt |                 |              |         |            |        |                       |         |     |
|                 |     |         |               |     |            |     |       | indicators      | and generate |         | metric     | hidden | layer representations |         |     |
awidelyadoptedparsercalledDrain[40]toextractlogevents,
|     |     |     |     |     |     |     |     | Zi ∈Rw×h,asshownin(4).WhereXi |     |     |     |     |               |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ------------- | --- | ----- |
|     |     |     |     |     |     |     |     |                               |     |     |     |     | indicatesthei |     | slide |
as Drain has been proven to be effective and efficient in past m m th
windowofsampledmetric.
evaluations.WefirstutilizetheDraintoextractnlogtemplates,
and then when a log message arrives, we could match it to =TransEncoder(CNN(Xi )).
|                   |     |           |               |     |     |              |     |     | Zi  |     |     |     |     |     | (4) |
| ----------------- | --- | --------- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |           |               |     |     |              |     |     | m   |     |     |     | m   |     |     |
| the corresponding |     | template. | Subsequently, |     | all | log messages |     |     |     |     |     |     |     |     |     |
are converted into log events arranged in chronological order. Multi-modal Self-attention: In order to learn the correlation
|          |       |          |             |     |         |              |     | between | hidden | variables | in different | modalities, |     | we consider |     |
| -------- | ----- | -------- | ----------- | --- | ------- | ------------ | --- | ------- | ------ | --------- | ------------ | ----------- | --- | ----------- | --- |
| Then, we | align | the logs | and metrics | by  | setting | the sampling |     |         |        |           |              |             |     |             |     |
concatenatingthehiddenlayerrepresentationsofbothmodali-
| interval of | metrics | as the | size of | the aligned |     | time block | and |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------ | ------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assigning all log events and metrics to their respective time tiesandapplyingself-attentionfusion,resultinginamulti-modal
self-attention(MSA)mechanism.Theformulasareasfollows:
blocks.
Then, we uniform the data structure of log data and metric =Cat(Zi,Zi ),
Zi
|     |     |     |     |     |     |     |     |     |     | f   |     | l m |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
databytransforminglogdataintotimeseriesdata.Foreachtime
|     |     |     |     |     |     |     |     |     |     | =Z  | iW  | iW  | iW  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
block,weassesstheoccurrenceofeachlogtemplate,markingit Q,K,V ,Z ,Z ,
|     |     |     |     |     |     |     |     |     |     |     | f Q | f K | f V |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as1ifitappearsand0otherwise.Bydoingso,weobtaina1×n (cid:2) (cid:3)
QKT
(cid:4)i
dimensionaltemplatefeatureforthespecifictimeblock,where Z =Softmax √ V,
f
| thenisthenumberoftemplatetypes.Themotivationbehindthis |     |     |     |     |     |     |     |     |     |                 |     | d   |            |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---------- | --- | --- |
|                                                        |     |     |     |     |     |     |     |     |     | (cid:4)(cid:4)i |     |     | (cid:4)i), |     |     |
stemsfromthefactthatthereisasignificantdifferencebetween Z =LayerNorm(Zi +Z (5)
|     |     |     |     |     |     |     |     |     |     | f   |     | f   | f   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thelogtemplatesinthenormalandabnormalsystemstatus.For
example,whenitcomestoabnormalsystemstatus,therearelog where Z i and Z i are the hidden layer representations of the
|     |     |     |     |     |     |     |     |     | l   | m   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
twomodalities.Cat()representstheconcatenatefunctioninthe
templatescontainingerrorhandlingandfaulttolerance-related
∈Rw×2h
information, while these log templates rarely appear in the lastaxis.Zi istheconcatenatedrepresentationofZi
|                                                      |     |     |     |     |     |     |     |          | f    |     |       |           |               |     | l      |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | ----- | --------- | ------------- | --- | ------ |
|                                                      |     |     |     |     |     |     |     | and Zi . | W ,W | ,W  | ∈Rd×d | represent | the trainable |     | hyper- |
| normalsystemstate.Therefore,wefocusontheoccurrenceof |     |     |     |     |     |     |     | m        | Q    | K V |       |           |               |     |        |
eachtemplate,capturingtheco-occurrencerelationshipsamong parameters,andQ,K,andVarethelinearprojectionsofZi.d
f
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

3892 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
indicatesthehiddensizeoftheattentionlayer(inthere,dequals to(6).Werefertothedifferencebetweenreconstructedvalues
2h).Z(cid:4)i ∈Rw×2histheoutputafterattentionoperation.Finally, and real values as reconstructed errors. Then, we proceed to
f
we use residual connections [41] and layer normalization [42] jointly train it using the reconstruction errors for both the log
togeneratetheultimatefusedfeaturesZ(cid:4)(cid:4)i ∈Rw×2h. andmetricsmodalities,asshownin(9).WhereG ()denotesthe
|          |            |      |                 | f   |     |           |                                              |     |     |     |     |     |     | l            |     |
| -------- | ---------- | ---- | --------------- | --- | --- | --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- |
|          |            |      |                 |     |     |           | generatorthatoutputsthelogsportion,i.e.,Ri,G |     |     |     |     |     |     | ()denotesthe |     |
| Decoder: | To achieve | data | reconstruction, | we  | map | the fused |                                              |     |     |     |     |     |     | m            |     |
l
featuresbacktotheinputspace.Specifically,weemployalinear thegeneratorthatoutputsthemetricsportion,i.e.,Ri ,MSE()
m
transformationtomapZ(cid:4)(cid:4)itoRi ∈Rk×(n+n(cid:4)),andsplitRiinto isusedtocomputetheMeanSquaredError(MSE)betweentwo
f
Ri ∈Rk×nandRi ∈Rk×n(cid:4) .RiandRi arethereconstructed inputs,andL representsthereconstructionloss,N represents
| l               | m   |     | l   | m   |     |     |                                 |     | r   |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| valuesofXiandXi |     |     |     |     |     |     | thetotalnumberofslidingwindows. |     |     |     |     |     |     |     |     |
,respectively.Theformulaisshownin(6):
l m
(cid:4)N
|     |       | Ri =σ(W     | Z (cid:4)(cid:4)i+b | ),  |     |     |     |     |        |                |     |     |     |         |     |
| --- | ----- | ----------- | ------------------- | --- | --- | --- | --- | --- | ------ | -------------- | --- | --- | --- | ------- | --- |
|     |       |             | d f                 | d   |     |     |     | =   | [MSE(G | (Xi),Xi)+MSE(G |     |     |     | (Xi),Xi | )]. |
|     |       |             |                     |     |     |     | L   | r   |        | l              |     |     | m   |         | (9) |
|     |       |             |                     |     |     |     |     |     |        |                | l   |     |     |         | m   |
|     | Ri,Ri | =Split(Ri), |                     |     |     | (6) |     |     |        |                |     |     |     |         |     |
|     | l     | m           |                     |     |     |     |     |     | i      |                |     |     |     |         |     |
whereRdenotesthereconstructionofX,σ()denotestheReLU AdversarialLearning:Toenhancethefittingofhardsamples
activationfunction,theW ∈R2h×(n+n(cid:4))andb ∈R(n+n(cid:4))are withoutoverfittingsimpleones,weintroducethemechanismof
|     |     | d   |     | d   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Split() adversariallearning.Thediscriminatorisviewedasadynamic
| the learnable | parameters, | and | the | indicates |     | the split |     |     |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
detectorfordiscerninghardandsimplesamples.Whenthegen-
operationofRinthelastaxis.
eratorperformspoorlyonhardsamples,makingitchallenging
|     |     |     |     |     |     |     | to deceive |     | the discriminator, |     | the | generator | experiences |     | higher |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------ | --- | --- | --------- | ----------- | --- | ------ |
D. DiscriminatorModule
trainingloss.Conversely,whenthegeneratorreconstructssuffi-
Intheframeworkofourdiscriminator,whichservestodiffer-
cientlywellonsimplesamples,easilydeceivingthediscrimina-
entiate real data from generated (fake) data, we introduce two tor,thegeneratorexperienceslowertrainingloss.Throughthe
individualdistinctcomponents:theLogDiscriminatorandthe
|     |     |     |     |     |     |     | adversarial |     | game | between | the generator |     | and | the discriminator, |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ------- | ------------- | --- | --- | ------------------ | --- |
MetricsDiscriminator. themodelautomaticallyadjuststhetraininglossconcerninghard
Log Discriminator: The log discriminator, denoted as D , and simple samples. This automatic adjustment balances the
l
consistsofafeatureembeddinglayerandalinearclassification
progressoffittinghardandsimplesamples,leadingtoabetter
iintoa
layer.ItemploysaCNNtoembedlogtemplatefeaturesI fitforthedistributionofnormaldata.
l
| hiddenrepresentationdenotedasZ |     |     | (cid:4)i ∈Rw×h,whereI |     | icouldbe |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l l The discriminator, which operates on both log and metrics
iorX i.Subsequently,alinearnetworkfollowedbyaSoftmax
R modalities, is trained to differentiate between real data and
l l
function is used for the purpose of classification. The specific generated data. We utilize cross-entropy loss for this purpose.
| computationalprocessisshownin(7).WhereY(cid:4)i |     |     |     |     | ∈[0,1]2 | in- |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theproposedadversariallearningarchitecturenotonlyallows
| dicatestheconfidenceofrealandfake,respectively,P(cid:4)i |     |     |          |      |     | ∈[0,1]  |                                                          |                |     |            |         |         |     |      |            |
| -------------------------------------------------------- | --- | --- | -------- | ---- | --- | ------- | -------------------------------------------------------- | -------------- | --- | ---------- | ------- | ------- | --- | ---- | ---------- |
|                                                          |     |     |          |      |     |         | for                                                      | the adjustment |     | of fitting | degrees | between |     | hard | and simple |
| indicatestheconfidenceofreal,                            |     |     | W ∈Rwh×2 | andb |     | ∈R2 are |                                                          |                |     |            |         |         |     |      |            |
|                                                          |     |     | l        |      | l   |         | multi-modalsamplesbutalso,withtwoseparatediscriminators, |                |     |            |         |         |     |      |            |
thelearnableparameters.
|     |     |     |     |     |     |     | enables | the | adjustment | of  | fitting | degrees | between | the | log and |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---------- | --- | ------- | ------- | ------- | --- | ------- |
metricmodalitypartofhardsamples.Thisenhancestheunified
Z (cid:4)i =CNN(Ii),
|     | l   |     | l   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
multi-modalrepresentationlearning.Theadversariallossforthe
|                                                       | (cid:4)i     |           | (cid:4)i+b |     |     |     |                |     |          |                  |     |     |        |     |     |
| ----------------------------------------------------- | ------------ | --------- | ---------- | --- | --- | --- | -------------- | --- | -------- | ---------------- | --- | --- | ------ | --- | --- |
|                                                       | Y =Softmax(W |           | Z          | ),  |     |     | discriminatorL |     |          | isdefinedas(10): |     |     |        |     |     |
|                                                       | l            |           | l l        | l   |     |     |                |     | ad       |                  |     |     |        |     |     |
|                                                       | (cid:4)i     | (cid:4)i. |            |     |     |     |                |     | (cid:4)N |                  |     |     |        |     |     |
|                                                       | P =Y         |           |            |     |     | (7) |                |     |          |                  |     |     |        |     |     |
|                                                       | l            | l,0       |            |     |     |     |                | = − | [log(D   | (Xi))+log(D      |     |     | (Xi )) |     |     |
|                                                       |              |           |            |     |     |     | L ad           |     |          | l                |     | m   |        |     |     |
|                                                       |              |           |            |     |     |     |                |     |          |                  | l   |     | m      |     |     |
| MetricDiscriminator:Themetricsdiscriminator,denotedas |              |           |            |     |     |     |                |     | i        |                  |     |     |        |     |     |
D ,followsastructuresimilartotheLogDiscriminator,with
| m   |     |     |     |     |     |     |     | +log(1−D |     | (G  | (Xi)))+log(1−D |     |     | (G  | (Xi)))]. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------------- | --- | --- | --- | -------- |
the distinction that its input is metric features Ii that could l l m m
m
(10)
| be Ri or | Xi . The specific |     | computational | process |     | is shown |     |     |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | ------------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| m        | m                 |     |               |         |     |          |     |     |     |     |     |     |     |     |     |
in (8). Where W ∈Rwh×2 and b ∈R2 are the learnable Thegeneratoristrainedtoproducedatathatcaneffectively
|     | m   |     | m   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameters. fool both D l and D m . This is achieved by minimizing the
|     |                       |          |            |       |     |     | following |     | adversarial | loss     | for the | discriminator |        | L   | , as shown |
| --- | --------------------- | -------- | ---------- | ----- | --- | --- | --------- | --- | ----------- | -------- | ------- | ------------- | ------ | --- | ---------- |
|     | Z (cid:4)i =CNN(Ii    |          | ),         |       |     |     |           |     |             |          |         |               |        | ag  |            |
|     | m                     |          | m          |       |     |     | in(11):   |     |             |          |         |               |        |     |            |
|     | Y (cid:4)i =Softmax(W |          | Z (cid:4)i | +b ), |     |     |           |     |             |          |         |               |        |     |            |
|     | m                     |          | m m        | m     |     |     |           |     |             | (cid:4)N |         |               |        |     |            |
|     | (cid:4)i              | (cid:4)i |            |       |     |     |           |     | L           | =        | log(1−D | (G            | (Xi))) |     |            |
|     | P =Y                  | .        |            |       |     | (8) |           |     | ag          |          |         | l             | l      |     |            |
m m,0
i
|                  |     |     |     |     |     |     |     |     |     | +log(1−D |     | (G  | (Xi))). |     |      |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------- | --- | ---- |
| E. ModelTraining |     |     |     |     |     |     |     |     |     |          |     | m   | m       |     | (11) |
Reconstruction Learning: To effectively capture the distri- ContrastiveLearning:Duetothecomplexityofmulti-modal
bution of normal data, we employ a reconstruction task as a hard sample combinations, to further learn the distribution of
fundamental component of our generator’s training regimen. normallog-metricmulti-modalsamplesandenhancethedistin-
Xi,
Specifically, for input data our generator is tasked with guishingabilitybetweennormalandabnormaldata,weemploy
producingcorrespondingreconstructeddata,asillustratedin(3) unmatcheddatatosimulateoneoftheabnormalscenariosinthe
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

LIUetal.:UAC-AD:UNSUPERVISEDADVERSARIALCONTRASTIVELEARNINGFORANOMALYDETECTIONONMULTI-MODAL 3893
multi-modal setting. Matched data is used to simulate normal TABLEI
scenarios. Through contrastive learning, we aim to increase THEOVERVIEWOFTHEEVALUATIONDATASETS
| the reconstruction |       | error | of unmatched |       | data and              | reduce | the re- |     |     |     |     |     |     |     |     |
| ------------------ | ----- | ----- | ------------ | ----- | --------------------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| construction       | error | of    | matched      | data, | thereby strengthening |        | the     |     |     |     |     |     |     |     |     |
distinctionbetweennormalandabnormaldata.
| Construction |     | of Unmatched |     | Pairs: | To construct | unmatched |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ------ | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
timeblocks,wekeepthelogmodalitydatafixed,searchformet-
ricsmodalitydatathatdoesnotmatch,andgenerateunmatched
| timeblocks.Specifically,forthei |     |     |     |     | timeblockxi | =(xi | ,xi ), |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ----------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
th l m the continuous changes in the number of log templates and
|     |     |     |     |     | =(xj,xj | )   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
we randomly select a time block xj from all time monitoringmetrics.
|                                         |     |     |                     |     | l m     |                    |     |                  |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | ------------------- | --- | ------- | ------------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| blocks.Werequirethatxj                  |     |     | (cid:6)=xjandabs(xi |     | ,xj     | )≥θ(cid:4),andthen |     |                  |     |     |     |     |     |     |     |
|                                         |     |     |                     |     | m m     |                    |     |                  |     |     |     |     |     |     |     |
| generateanewunmatchedtimeblockx(cid:4)i |     |     | l                   | l   | =(xi,xj | ),asshown          |     |                  |     |     |     |     |     |     |     |
|                                         |     |     |                     |     |         | l m                |     | F. ModelInfering |     |     |     |     |     |     |     |
in(12).Whereθ(cid:4)isathresholdtodefinethedifferencebetween
xi xj When performing inference with our model, we utilize the
| and | . And | then, | for the | i th | matched slide | window, | we  |     |     |     |     |     |     |     |     |
| --- | ----- | ----- | ------- | ---- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| m   | m     |       |         |      |               |         |     |     |     |     |     |     |     |     |     |
generateunmatchedtimeblocksforeachmatchedtimeblockto generatortoreconstructinputdataandthendetermineanomalies
achieveunmatchedslidewindowX(cid:4)i ∈Rw×(n+n(cid:4)). based on the reconstruction error (anomaly score Score), as
shownin(16),comparedtoapredefinedthreshold.Thethresh-
|     |     |     | x (cid:4)i | =(xi ,xj | ),  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l m oldistypically determined bybinary searching forthebest-f1
throughwholedataset,likethepriorresearches[16],[17],[18],
|     |     |     | ∃xj    | =(xj,xj | ),          |     |      |       |                     |     |         |     |        |         |      |
| --- | --- | --- | ------ | ------- | ----------- | --- | ---- | ----- | ------------------- | --- | ------- | --- | ------ | ------- | ---- |
|     |     |     |        | l       | m           |     |      | [20]. |                     |     |         |     |        |         |      |
|     |     |     | s.t.   | xi      | (cid:6)=xj, |     |      |       |                     |     |         |     |        |         |      |
|     |     |     |        | l       | l           |     |      |       | Score(Xi)=MSE(Xi,(G |     |         |     | (Xi))) |         |      |
|     |     |     |        |         | (cid:4)     |     |      |       |                     |     |         | l   | l      |         |      |
|     |     |     | abs(xi | ,xj )≥θ | .           |     | (12) |       |                     |     |         |     |        |         |      |
|     |     |     | m      | m       |             |     |      |       |                     |     | +MSE(Xi |     | ,(G    | (Xi))). |      |
|     |     |     |        |         |             |     |      |       |                     |     |         |     |        | m       | (16) |
m
ConstructionofContrastiveLoss:Weutilizeatriplelossto
| construct | the     | contrastive | loss  | L , reducing | the                | reconstruction |      |     |     |     |                |     |     |     |     |
| --------- | ------- | ----------- | ----- | ------------ | ------------------ | -------------- | ---- | --- | --- | --- | -------------- | --- | --- | --- | --- |
|           |         |             |       | c            |                    |                |      |     |     |     | IV. EVALUATION |     |     |     |     |
| loss for  | matched | data        | while | increasing   | the reconstruction |                | loss |     |     |     |                |     |     |     |     |
forunmatcheddata,withtheconstraintthatitdoesnotexceed We evaluate UAC-AD by answering the following research
α. The α represents the expected inter-class distance. This is questions(RQs):
(cid:2)
expressedasshownin(13): (cid:2) RQ1:HoweffectiveisUAC-ADinanomalydetection?
RQ2:WhatisthecontributionofeachcomponentofUAC-
(cid:4)N
AD?
|     | L   | =   | max(0,MSE(G |     | (Xi),Xi | )   |     | (cid:2) |     |      |        |         |     |          |             |
| --- | --- | --- | ----------- | --- | ------- | --- | --- | ------- | --- | ---- | ------ | ------- | --- | -------- | ----------- |
|     | c   |     |             |     | m       | m   |     |         |     |      |        |         |     |          |             |
|     |     |     |             |     |         |     |     | RQ3:    | How | does | UAC-AD | perform |     | in terms | of time and |
i
storeefficiency?
|     |     |     |     | (cid:4)i),X | (cid:4)i)+α). |     |     | (cid:2) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | ------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
−MSE(G (X (13) RQ4: How much is the method affected by parameter
|     |     |     |     | m   | m   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sensitivity?
| Lossfunction:Insummary,duringthetrainingofthegenera- |     |     |     |     |     |     |     | (cid:2) |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
RQ5:Canwevisuallyexplaintheimpactofeachcompo-
| tor,wesimultaneouslyemployreconstructionlossL |     |     |     |     |     | ,adversar- |     |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
nentinourproposedmodel?
| iallossL                                   | ag ,andcontrastivelossL |     |     | c   | asindicatedin(14).Here, |     |        |     |     |     |     |     |     |     |     |
| ------------------------------------------ | ----------------------- | --- | --- | --- | ----------------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| weaimtominimizethewholelossofthegeneratorL |                         |     |     |     |                         |     | .Where |     |     |     |     |     |     |     |     |
G
λ and λ are weighting parameters that control the balance A. ExperimentsSetup
1 2
betweenthethreelosses.
|     |     |     |     |     |     |     |     | 1)  | Datasets: | To evaluate |     | the performance |     | of UAC-AD, | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --------------- | --- | ---------- | --- |
=L +λ +λ conductextensiveexperimentsusingtwoopen-sourcedatasets
|     |     | L G | r   | 1L ag | 2L c . |     | (14) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
andarealindustrialdatasetfromalargecommunicationcom-
| During | the training | of  | the discriminator, |     | we minimize |     | the ad- |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ------------------ | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
pany,asshowninTableI.Wepartition70%ofeachdatasetfor
versarial loss of discriminator L to distinguish whether data trai ningandreservetheremaining30%fortesting.
|     |     |     |     | ad  |     |     |     | (cid:2) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
comesfromrealsourcesorthegenerator,asexpressedin(15),
|     |     |     |     |     |     |     |     | Dataset |     | A is an | in-lab | dataset | publicly | released | by [28] |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ------ | ------- | -------- | -------- | ------- |
wheretheL D indicatesthetraininglossofthediscriminator. designed specifically for evaluating the effectiveness of
|     |     |     |     |     |     |     |      | multi-modal |     | anomaly |     | detection. | It encompasses |     | 11 met- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------- | --- | ---------- | -------------- | --- | ------- |
|     |     |     | L   | =L  | .   |     | (15) |             |     |         |     |            |                |     |         |
|     |     |     | D   | ad  |     |     |      |             |     |         |     |            |                |     |         |
rics,sampledat10-secondintervals,formingtimeblocks
Itisworthnotingthatduringdatapreprocessing,itiscrucial of10seconds.Itslogdataincludes117logtemplates.
(cid:2)
todeterminethetotalnumberoflogtemplatesandmonitoring DatasetBisacomplexmulti-modaldatasetsimulatedby
metrics. When these quantities change, the proposed method anintelligentoperationscompany.Itservesasanevalua-
requires retraining. Alternatively, if new log templates emerge tionbenchmarkformulti-modalanomalydetectionunder
butthereisnodesiretoretrainthemodel,similaritymatchingcan intricate scenarios. The dataset comprises metric and log
beemployedtomapthenewlogtemplatestoknowntemplates, datafromfourdistinctservices,with85metricssampled
ensuring the model’s availability. In the future, there is a need every30seconds.Thelogdataconsistsof20logtemplates.
to design anomaly detection methods capable of adapting to This dataset incorporates a variety of artificially injected
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

3894 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
faults,suchasCPUstress,memorystress,loggingfailure, andmetricmodeldetectedananomalyforatimeblock,this
andnetworkfailures. anomalyisconsideredtohavebeendetected.
(cid:2)
Dataset C is derived from a large-scale communication 3) Evaluation Measurements: We apply the widely used
enterprise’sreal-timecomputingserviceplatformwith21 measurements to assess our method. We adopt true positive
online services. It is utilized to allocate computational (TP), false positive(FP), and false negative(FN) to label the
resources for the company’s online services. The dataset anomaly detection results according to the ground truth. TP
spansthreedaysandincludes115metrics,sampledevery denotes a failure both confirmed by ground truth and de-
30seconds.Italsofeatureslogdatawith639uniquetem- tected by a method. FP is a normal time block that is falsely
plates.Notably,thisdatasetincludes6genuineanomalies identified by a method. FN is a missed anomaly that should
inducedbyfactorssuchasdiskpartitionstress,CPUstress, have been detected. We calculate precision=TP/(TP +
andmemorystress. FP), recall=TP/(TP +FN), and F1−score=(2·
2) Baseline: To assess the effectiveness of our proposed precision·recall)/(precision+recall).
method,weconductedcomprehensivecomparisonswithvarious 4) Implementation: UAC-AD is implemented in Pytorch,
types of baseline methods. These comparisons encompassed andalloftheexperimentsareconductedonaLinuxServerwith
differentdatasources,includingsingle-modallogdata,single- anNVIDIAGeForceGTX3090GPUviaPython3.8.Asforthe
modalmetricdata,andmulti-modaldata.Additionally,weex- hyper-parameters, UAC-AD adopts the unmatched α=0.16,
ploreddiversetrainingstrategies,spanningsupervisedlearning, thewindowsizew =40,andthehiddensizeh=32,andthese
semi-supervisedlearning,andunsupervisedlearningparadigms. hyper-parametersaredescribedindetailinsectionIV-E.Weuse
Next,wewillintroducethemindetail. theAdamoptimizer[44]withaninitiallearningrateof0.001.We
(cid:2)
Deeplog[24]isawidelyappliedunsupervisedloganomaly settheλ 1 =λ 2 =1totreatdifferentlearningstrategiesequally.
detection method. It uses the LSTM neural network to We set the θ(cid:4) =0.15 to balance the distinguishment between
encodethelogsequentialinformation,predictthenextlog matched and unmatched pair samples and the time-coast for
template,anddeterminetheanomalybyjudgingwhether finding the unmatched pair samples following (12). The batch
thenextlogtemplateisintop-klargestlikelypredictedlog sizeis256,andtheepochofeachtrainingphaseisdynamically
templates. adjustedbyanearlystopstrategy.
(cid:2)
LogRobust [25] is a supervised log anomaly detection For hyper-parameters of baselines, we adopt the public im-
method,whichencodesthelogsequencefeatures,classifies plementationsof[3],[16],[17],[24],[25],[28],anddetermine
them,andachievesrobustandsatisfactoryperformanceon thehyper-parametercombinationachievingthehighesttestF1-
anomalydetection. scoreforeachbaseline.
(cid:2)
OmniAnomaly [16] is an unsupervised anomaly detec-
tion based on metric. It seamlessly integrates Variational
B. RQ1:TheOverallPerformanceoftheProposedMethod
AutoEncoders (VAE) into time series anomaly detection.
Thisintegrationservestocompressfeatureseffectivelyand To assess the effectiveness of our proposed method, we
learntheintricatedistributionpatternsofnormalsamples. compareditwithvarioustypesofbaselinemethods,including
(cid:2)
MTAD-GAT [17] is an unsupervised anomaly detection single-modalmethodsforlogsandmetrics,multi-modalmeth-
that relies on metric data, which incorporates the graph ods,andensemblelearningmethods,asshowninTableII.The
attentionneuralnetwork(GAT)tocapturethespatialcor- resultsdemonstratethatourproposedapproachoutperformsthe
relationsamongdimensionsinmultivariatetimeseries. baseline methods on Dataset B and Dataset C, achieving im-
(cid:2)
SCWarn[3]andDAM[33]areunsupervisedmulti-modal provementsof4.5and19.3percentagepoints,respectively.On
anomalydetectionmethodsthatadopttheLSTMtoencode DatasetA,ourmethodsurpassesexistingunsupervisedstate-of-
thelogandmetricsequentialfeaturesandfusethefeatures the-artmethodsby6.7pointsandapproachestheperformanceof
byconcatenationorcrossattentionoperation. existingmulti-modalsemi-supervisedstate-of-the-artmethods.
(cid:2)
Hades [28] is a semi-supervised multi-modal anomaly Thishighlightstheeffectivenessofourproposedapproach.
detectionapproach.ThismethodemploysFastText[43]for Comparedtosingle-modalmethodsthatconsideronlylogor
logtextembedding,utilizesTransformerforlogfeatureex- metric data, our method simultaneously incorporates informa-
traction,employsCNNsformetricfeatureextraction,and tionfrommultiplemodalities,leadingtosignificantperformance
integratesthesefeaturesthroughconcatenationoperations. gains.Incontrasttoexistingmulti-modalunsupervisedmethods,
(cid:2)
Union:Tofurtherinvestigatetheeffectofourmulti-modal ourapproachenhancesfitnesstohardsamplesandfurtherlearns
method,wealsodesigntheensemblemethodsasbaselines. thedistributionofnormalmulti-modaldatathroughadversarial
Wesplitourmodelintotwosinglemodels:thelogmodel contrastivelearning.Consequently,itimprovesthediscrimina-
and the metric model. Then, we use them for anomaly tive power between normal and anomalous data, resulting in
detection,respectively,anduniontheirresultsasthefinal additional performance gains. It is interesting to note that the
results:Ifoneofthelogmodelorthemetricmodeldetected proposedunsupervisedmethodgenerallyoutperformsthesemi-
ananomalyforatimeblock,thisanomalyisconsideredto supervisedmethodHades.Thismaybebecausesemi-supervised
havebeendetected. methods like Hades are prone to be influenced by sparsely
(cid:2)
Intersection:SimilartotheUnionbaseline,thedifference labeled data, making it difficult to adapt to unseen anomalies.
iswetaketheintersectionoftheresultsfromthelogmodel In contrast, our proposed unsupervised method learns implicit
andthemetricmodelasthefinalresults:Boththelogmodel patterns of multi-modal data more comprehensively through a
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore. Restrictions apply.

LIUetal.:UAC-AD:UNSUPERVISEDADVERSARIALCONTRASTIVELEARNINGFORANOMALYDETECTIONONMULTI-MODAL 3895
TABLEII
THEOVERALLPERFORMANCECOMPARISONOFOURMETHODUAC-ADANDSEVERALSTATE-OF-THE-ARTMETHODS
TABLEIII
THEABLATIONSTUDYONEACHCOMPONENTOFUAC-ADOVERTHREEDATASETS
TABLEIV
| reconstruction | task, without | being affected | by the scarcity | of  |     |     |     |     |
| -------------- | ------------- | -------------- | --------------- | --- | --- | --- | --- | --- |
THECOMPARATIVEANALYSISOFDIFFERENTFEATUREFUSIONSTRATEGIES
| labeled data. | This leads | to superior performance | compared | to  |     |     |     |     |
| ------------- | ---------- | ----------------------- | -------- | --- | --- | --- | --- | --- |
SHOWCASINGTHEF1SCOREEVALUATIONMETRIC
Hades.Moreover,comparedtomethodsdirectlyperformingre-
sultfusion,ourproposedapproachutilizesdeeperfeaturefusion,
| leading to | more substantial | improvements | in performance. | In  |     |     |     |     |
| ---------- | ---------------- | ------------ | --------------- | --- | --- | --- | --- | --- |
termsoftherecallmetric,onlytheunionmethodsurpassesour
| method. | This is because | the union method | splits our | method |     |     |     |     |
| ------- | --------------- | ---------------- | ---------- | ------ | --- | --- | --- | --- |
intotwomodels,oneforlogsandoneformetrics,andcombines
theresultsusingalogicalORoperation.Consequently,itisless
likelytomissanomalies,resultinginaparticularlyhighrecall
| rate. However, | it may | also lead to more | false positives | since |     |     |     |     |
| -------------- | ------ | ----------------- | --------------- | ----- | --- | --- | --- | --- |
anomaliesineitherlogsormetricscantriggeranalert,evenifthe
systemisnotactuallyexperiencingananomaly.Similarly,only
EffectivenessofAdversarialLearning:TableIIIdemonstrates
the intersection method outperforms our method in precision. thatintroducingadversariallearningsignificantlyenhancesthe
| This is because | the intersection | method | only considers | cases |     |     |     |     |
| --------------- | ---------------- | ------ | -------------- | ----- | --- | --- | --- | --- |
F1scoreofanomalydetection,bothinsingle-modal(comparing
wherebothmodelsdetectanomaliesasactualanomalies.Asa
|     |     |     |     | Method | 1 with Method 3, | or Method | 2 with | Method 4) and |
| --- | --- | --- | --- | ------ | ---------------- | --------- | ------ | ------------- |
result,itsprecisionishigh,butittendstomissmanyanomalies,
|     |     |     |     | multi-modal | scenarios (comparing |     | Method 5 with | Method 6). |
| --- | --- | --- | --- | ----------- | -------------------- | --- | ------------- | ---------- |
resultinginalowerrecallrate.
Thisimprovementisattributedtoadversariallearning’sabilityto
helpthegeneratorbalancethetrainingofhardsamplesandsim-
plesamples,improvingthefittingofthedistributionofnormal
C. RQ2:TheAblationStudyoftheProposedMethod
|     |     |     |     | data, and | thereby enhancing | anomaly | detection | effectiveness. |
| --- | --- | --- | --- | --------- | ----------------- | ------- | --------- | -------------- |
Toassesstheeffectivenessofeachcomponentinourproposed After the introduction of GAN, the significant increase in F1
method,weconductedcomparisonsusingdifferentvariantsof scoreinthemulti-modalscenarioisnotablyhigherthantheim-
ourapproach,asshowninTablesIIIandIV. provementsseenineachindividualmodality.Thisisattributed
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

3896 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
TABLEV
THECOMPARISONOFTHETIMEANDSTORAGEEFFICIENCYBETWEEN
UAC-ADANDBASELINEMETHODS
Fig.4. ThecomparisonbetweenFusedGANandSeparateGAN(i.e.,Method6
inTableIII)with10timesrunning.ThediscriminatorofFusedGANutilizestwo
TableV.TimeEfficiency:Theresultsdemonstratethatalthough
1DCNNstoembeddatafromthelogandmetricmodalitiesseparately.These
|     |     |     |     |     |     |     | the proposed | method |     | may not | excel in | training | time | due to its |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --- | ------- | -------- | -------- | ---- | ---------- |
embeddingsarethenfusedusingMSAtoobtainaunifiedrepresentation,which
isfinallyusedbytheclassificationlayertodiscriminatewhethertheinputdata
|     |     |     |     |     |     |     | focus on | acquiring | better | representations |     | of  | multimodal | data, |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --------------- | --- | --- | ---------- | ----- |
isrealorreconstructed.
|     |     |     |     |     |     |     | it still demonstrates |     | efficient |               | model | inference | time,       | making |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --------- | ------------- | ----- | --------- | ----------- | ------ |
|     |     |     |     |     |     |     | it well-suited        | for | real-time | applications. |       | Store     | Efficiency: | The    |
to the fact that separate discriminators also regulate the fitting resultsshowthatourproposedmethodrequiresfewerparameters
degreesofdifferentmodalitypartsofhardsamples,facilitating thanmostbaselinemodels(LogRobust,OmniAnomaly,MTAD-
themodeltobetterlearnthenormalpatternsoflogandmetric GAT,SCWarn,andHades),indicatingitsrelativelysmallstorage
modaldata.Fig.4providesamorestraightforwardcomparison, overheadandfacilitatingthedeploymentofthemodel.Although
showingthatcomparedtoFusedGAN,SeparateGANexhibits DeepLog has a smaller number of parameters, the substantial
betteranomalydetectionperformanceacrossallthreedatasets, performancegainsofourproposedmethodmakeitquitesuitable
validatingtheeffectivenessoffine-grainedadversariallearning. forpracticalapplicationsinreal-worldscenarios.
EffectivenessofContrastiveLearning:ComparingMethod5
| with Method     | 7   | in Table | III, the      | results indicate | that | introduc-   |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------------- | ---------------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing contrastive |     | learning | significantly | improves         | the  | F1 score of |     |     |     |     |     |     |     |     |
E. RQ4:TheParameterSensitivityoftheProposedMethod
| anomaly | detection. | Contrastive |     | learning achieves |     | this through |     |     |     |     |     |     |     |     |
| ------- | ---------- | ----------- | --- | ----------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Toevaluatethesensitivityofourmethod’shyperparameters,
| the matched | pairs | and | the unmatched | pairs, | enhancing | the |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ------------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
learningofthedistributionofmulti-modalnormaldata.Thisin- wecalculatedtheaverageF1-scoreunderdifferenthyperparam-
etersettings,asshowninFig.5.
creasesthediscriminativepowerbetweennormalandanomalous
|     |     |     |     |     |     |     | The inter-class |     | distances | in  | contrastive | learning: |     | The pa- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | ----------- | --------- | --- | ------- |
data,improvinganomalydetectioneffectiveness.Additionally,
|           |         |     |           |                |      |          | rameter | α introduced |     | in (13) | holds significant |     | importance | as  |
| --------- | ------- | --- | --------- | -------------- | ---- | -------- | ------- | ------------ | --- | ------- | ----------------- | --- | ---------- | --- |
| comparing | Methods | 5,  | 6, 7, and | 8, the results | show | that the |         |              |     |         |                   |     |            |     |
ahyperparameterinourcontrastivelearningmodule,exertinga
| combination | of  | contrastive | learning | and adversarial |     | learning |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | -------- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
substantialimpactontheperformanceofUAC-AD.Wesystem-
leadstofurtherperformanceimprovements.Thisdemonstrates
aticallyvariedαacrossarangefrom0.02to0.2.Interestingly,as
thecomplementarycontributionsofthesetwocomponents,con-
αincreased,therewasanoticeableimprovementinF1-scorefor
firmingtheireffectiveness.
DatasetC.However,thisimprovementwaslimitedinDatasetA.
| Effectiveness |     | of MSA | Design: | To evaluate | the effectiveness |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ------- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisdivergenceinperformancemaybeattributedtothediverse
oftheMulti-ModalSelf-Attention(MSA)design,wecompared
natureofmatchedpairswithindifferentdatasets.Inthecaseof
itwithcommonmulti-modalfeaturefusionmethods,asshown
DatasetA,theunmatchedpairsmaybesimilartothematched
| in Table | IV. The | results | highlight | the significant | effectiveness |     |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | --------- | --------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pairs.Consequently,enforcingacleardistinctionbetweenpos-
| of MSA | compared | to other | feature | fusion | mechanisms. | This |     |     |     |     |     |     |     |     |
| ------ | -------- | -------- | ------- | ------ | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
superiority is due to MSA’s ability to capture not only the itive and negative samples could potentially compromise the
|     |     |     |     |     |     |     | performance | of  | UAC-AD. | To strike | a   | balance | in performance |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --------- | --- | ------- | -------------- | --- |
correlationsbetweenlatentvariablesacrossdifferentmodalities
acrossalldatasets,weoptedforα=0.16,achoicethatresulted
butalsothecorrelationsbetweenlatentvariableswithinsingle
inaharmoniousandoptimalperformance.
modalities.Consequently,MSAachievessuperiorfeaturefusion
Thetimewindowsizesofadversariallearninggenerator:We
results.
|     |     |     |     |     |     |     | systematically |     | varied | w within | the range | of 10 | to 100. | As ob- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | -------- | --------- | ----- | ------- | ------ |
served,increasingthevalueofwinitiallyledtoanimprovement
D. RQ3:TheTimeandStorageEfficiencyofthe
intheF1-score,followedbyasubsequentdecline.Thisbehavior
ProposedMethod
|     |     |     |     |     |     |     | can be attributed |     | to the | fact | that a | larger time | window | can |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | ---- | ------ | ----------- | ------ | --- |
To evaluate the time and storage efficiency of our proposed provide a richer contextual understanding, thereby enhancing
method, we compared the inference time and the number of themodel’sperformance.However,ifthetimewindowbecomes
parametersrequiredwithvariousbaselinemethods,asshownin excessivelylarge,themodelencounterschallengesincapturing
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

LIUetal.:UAC-AD:UNSUPERVISEDADVERSARIALCONTRASTIVELEARNINGFORANOMALYDETECTIONONMULTI-MODAL 3897
Fig.5. Theevaluationoftheimpactofdifferentinter-classdistancesαincontrastivelearning,varioustimewindowsizesw,differenthiddenlayersizeshof
adversariallearninggenerators,differentsamplefrequency,differentλ 1andλ 2onanomalydetectionperformanceacrossthreedatasets.
intricateandextensivetemporalcorrelations,resultinginade- Dataset B and dataset C initially exhibit an increase followed
creaseinoverallperformance.Toattainoptimalmodelperfor- byadecreaseinF1score,demonstratingtheeffectivenessofin-
mance, we carefully evaluated the impact of different window troducingcontrastivelearning.However,datasetAconsistently
|                         |     | =50yieldedthebestresults. |     | showsadeclinewithincreasingλ |                          |     |     |
| ----------------------- | --- | ------------------------- | --- | ---------------------------- | ------------------------ | --- | --- |
| sizesanddeterminedthatw |     |                           |     |                              | 2.Theunderlyingreasonfor |     |     |
The hidden layer sizes of adversarial learning gener- thistrendmaystillbethattheunmatchedpairsaresimilartothe
ator: We systematically varied h within the range of matchedpairs.Therefore,wechooseλ =1.0toachievebetter
2
[16,32,64,128,256,512].
|     |     | Our observations | revealed | that in- results. |     |     |     |
| --- | --- | ---------------- | -------- | ----------------- | --- | --- | --- |
creasing the value of h initially resulted in an improvement Samplingfrequency:Althoughtheoriginalsamplingfrequen-
in the F1-score, followed by a rapid decline. This pattern can ciesofdifferentdatasetshavebeenfixed,forexample,dataset
be attributed to the fact that larger hidden layer representation A is sampled every 10 seconds, while datasets B and C are
vectorscancapturemoreintricatefeatures,leadingtoenhanced sampledevery30seconds,weattemptedtoexploretheimpact
modelperformance.However,anexcessivelylargehiddenlayer ofdifferentsamplingfrequenciesontheproposedmethod.Let
representation might encode excessive detail in the features, τ represent the original sampling interval of the dataset. We
resultinginalackofhigh-levelfeaturerepresentationandasub- systematically varied the sampling intervals as [τ, 3τ, 6τ, 9τ,
sequent decline in overall model performance. Our evaluation 12τ].Theresultsshowthatasthesamplingintervalincreases,
indicatedthath=32yieldedthemostfavorableresults,striking theoverallF1scoreoftheproposedmethodtendstostabilize,
abalancebetweencapturingdetailedfeaturesandmaintaining indicating that the proposed method is insensitive to sampling
| high-levelfeaturerepresentationinthemodel. |                                                  |                   |                | frequency. |     |     |     |
| ------------------------------------------ | ------------------------------------------------ | ----------------- | -------------- | ---------- | --- | --- | --- |
| The weights                                | of the                                           | training loss: We | systematically | varied     |     |     |     |
| λ 1 andλ                                   | 2 withintherangeof[0.1,0.5,1.0,1.5,2].Theresults |                   |                |            |     |     |     |
F. RQ5:TheInterpretabilityoftheProposedMethod
| indicatethatasλ | increases,theoverallF1scoreofthemodel |     |     |     |     |     |     |
| --------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
1
λ =1.0.
initially increases, stabilizing around 1 This suggests Inordertobetterassesstheeffectivenessofthecomponents
the effectiveness of adversarial learning in anomaly detec- wedesigned,wevisuallydemonstratedtheimpactofdifferent
λ =1.0
tion. Therefore, we select 1 to achieve better results. componentsonthereconstructionerrorsofinputdata,asshown
λ
Meanwhile, as 2 increases, the overall F1 score of the model in Fig. 6. In this context, normal samples interspersed with
transitions from stability to decline. This could be due to the anomalysamplescanberegardedashardsamples.Introducing
unmatched pairs still retaining certain temporal characteristics theAdversarialLearningmechanismsignificantlyreducedthe
ofmetrics,andexcessivelymagnifyingthereconstructionper- reconstruction errors of normal data. This indicates that our
| formance | of unmatched | pairs may disrupt | the learning | of un-               |                   |             |         |
| -------- | ------------ | ----------------- | ------------ | -------------------- | ----------------- | ----------- | ------- |
|          |              |                   |              | designed Adversarial | Learning enhances | the model’s | balance |
derlyingmulti-modalpatterns.Moreover,asλ
2increases,there betweenhardsamplesandsimplesamples,andstrengthensthe
are variations in model performance across different datasets. learning of normal data distribution. With the introduction of
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

3898 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
|     |     |     |     |     |     |     |     | take into | account | logs from | middleware |     | services | to aid | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | ---------- | --- | -------- | ------ | ------ |
detectionprocess.
B. TheGeneralityoftheProposedMethod
Theproposedmethodexhibitsacertaindegreeofgeneraliza-
tion.First,intermsoffeaturequantity,ourmethodcollectsall
datafromdifferentdatasetsandinputsthemintothegenerator,
whichautomaticallyextractsafixednumberoffeatures(deter-
|     |     |     |     |     |     |     |     | mined by   | the hyperparameter |            | hidden | size). | Second,  | in        | terms |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | ---------- | ------ | ------ | -------- | --------- | ----- |
|     |     |     |     |     |     |     |     | of anomaly | types,             | our method | does   | not    | restrict | the types | of    |
anomaliesitcandetectandcanidentifyanomaliesindifferent
Fig.6. Thevisualizationofreconstructionerrorsfortestsetsamplesobtained
| using various | learning | strategies | on Dataset | B.  | The magenta | dots | indicate |               |          |            |     |            |     |              |     |
| ------------- | -------- | ---------- | ---------- | --- | ----------- | ---- | -------- | ------------- | -------- | ---------- | --- | ---------- | --- | ------------ | --- |
|               |          |            |            |     |             |      |          | microservices | systems. | Therefore, |     | our method |     | demonstrates | a   |
anomalysamples,whilethebluedotsrepresentnormalsamples.Thehorizontal
certainlevelofgeneralization.
axissignifiesthereconstructionerror,whiletheverticalaxisisassociatedwith
randomvaluestoenableatwo-dimensionalvisualizationofthereconstruction
| error. |     |     |     |     |     |     |     | C. ThreatstoValidity |             |          |      |      |     |            |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- | -------- | ---- | ---- | --- | ---------- | --- |
|        |     |     |     |     |     |     |     | Threats              | to internal | validity | come | from | the | annotation | of  |
anomalies.Labelingprinciplesvarydependingonthepurpose,
theContrastiveLearningmechanism,thereconstructionerrors
|             |      |               |     |            |           |     |          | system, | person, and | so  | on. Thus, | the | labeling | may exist | as  |
| ----------- | ---- | ------------- | --- | ---------- | --------- | --- | -------- | ------- | ----------- | --- | --------- | --- | -------- | --------- | --- |
| of abnormal | data | significantly |     | increased, | enhancing |     | the dis- |         |             |     |           |     |          |           |     |
inconsistencywhenitcomestonon-extremeanomaliesorrare
tancebetweennormalandabnormalsamples.Thisdemonstrates
|          |          |             |          |     |          |     |         | patterns, | such as the | slightly | steep | ups | and downs | in metrics, |     |
| -------- | -------- | ----------- | -------- | --- | -------- | --- | ------- | --------- | ----------- | -------- | ----- | --- | --------- | ----------- | --- |
| that our | designed | Contrastive | Learning |     | improves | the | model’s |           |             |          |       |     |           |             |     |
metricvariationsbetweennormalandabnormalfluctuation,log
| understanding |     | of multi-modal | normal | data. | By  | expanding | the |     |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | ------ | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statementsrarelyoccurring,etc.Toalleviatetheseconcerns,the
distancebetweenpositiveandnegativesamples,itenhancesthe
adopteddatasetsareverifiedbyexperiencedannotators,andwe
distinguishabilitybetweennormalandabnormalsamples.
furtherevaluatethecorrectnessofthelabelingofeachdataset.
Theexternalthreatmainlycomesfromourdatasets.Though
V. DISCUSSION
|     |     |     |     |     |     |     |     | our experiments | are | evaluated     | on  | three  | datasets, | it is yet | un- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | ------ | --------- | --------- | --- |
|     |     |     |     |     |     |     |     | known whether   | the | effectiveness |     | of our | method    | UAC-AD    | can |
A. LessonsLearned
begeneralizedacrossallotherdatasets.Tomitigatethethreat,we
| Complementarity |     | of Multi-Source |     | Data | for Anomaly |     | Detec- |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | ---- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
usedifferentdatasetswithrepresentativeworkloadsandtypical
tion in Microservices Systems: While impressive results can faultstoevaluateUAC-AD,andtheexperimentalresultsshow
| be achieved | with | single-modal |     | data, as | demonstrated |     | by the |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | -------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
theUAC-ADcanworknotonlyonsimulateddatabutalsoon
metric-basedanomalydetection(e.g.,Method1)inDatasetA,or realindustrialdata.Wewillalsoevaluateourmethodonmore
thelog-basedanomalydetection(e.g.,Method2)inDatasetB, datasetsinthefuture.
asshowninTableIII,theeffectivefusionandlearningofmulti-
modaldatastillleadtoanotableimprovementinperformance.
|     |     |     |     |     |     |     |     |     |     | VI. | CONCLUSION |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
Thisemphasizesthecomplementarynatureofmulti-modaldata
in microservices systems for anomaly detection. This insight Inthispaper,weprimarilyaddressthehardsampleproblem
inanomalydetectionoflog-metricmodalitiesinmicroservices
suggeststhatfutureresearchinmicroservicessystemanomaly
detectionshouldfocusmoreonthedetectionofanomaliesusing systems. To tackle the complexity of their combinations, we
designcontrastivelearningtocapturethepatternsoflog-metric
multi-modaldataratherthanrelyingsolelyonsingle-modaldata.
UtilityofMiddlewareServiceLogsforAnomalyDetectionin combinationsduringnormalsystemoperation,whiledistancing
OtherServices:InDatasetC,wecollectedmetricsandlogsfrom from abnormal combinations. To address the issue of incon-
sistentconvergencespeeds,weemployanadversariallearning
atotalof21services,withmostworkingservicesnotgenerating
logs. The majority of collected logs were from a middleware framework to adjust the learning speeds of hard and simple
|     |     |     |     |     |     |     |     | samples | automatically. | Moreover, |     | we use | separate | discrimina- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --------- | --- | ------ | -------- | ----------- | --- |
serviceofamessageprocessor.Despitefaultspotentiallyoccur-
ringinworkingservicesthatdonotgeneratelogs(forinstance, tors to regulate the fitting degree of each modality part of the
if a container of a working service crashes and restarts, and multi-modalhardsamples.Extensiveexperimentsareconducted
tovalidatetheefficacyofourproposedmethod.
| coincidentally |     | not reflected | in the | metric | data | due to inherent |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | ------ | ------ | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
samplingintervalsandimperfectconfiguration[45]),anomalies
canstillbedetectedusinglogsfromthemessageprocessor,as REFERENCES
| evident | from the | log-based | anomaly | detection |     | (Method1 | and |                                                                  |     |     |     |     |     |     |     |
| ------- | -------- | --------- | ------- | --------- | --- | -------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|         |          |           |         |           |     |          |     | [1] G.Yu,P.Chen,Y.Li,H.Chen,X.Li,andZ.Zheng,“Nezha:Interpretable |     |     |     |     |     |     |     |
Method3)recallrateofnearly100%inTableIII.Thisindicates
fine-grainedrootcausesanalysisformicroservicesonmulti-modalob-
thatlogsfrommiddlewareservicescanbehelpfulfordetecting servabilitydata,”inProc.31stACMJointEur.Softw.Eng.Conf.Symp.
Found.Softw.Eng.,2023,pp.553–565.
| anomalies | in other | services. | This | insight | suggests | that | future |                                                             |     |     |     |     |     |     |     |
| --------- | -------- | --------- | ---- | ------- | -------- | ---- | ------ | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |          |           |      |         |          |      |        | [2] C.Lee,T.Yang,Z.Chen,Y.Su,andM.R.Lyu,“Eadro:Anend-to-end |     |     |     |     |     |     |     |
microservices’multi-modalanomalydetectionshouldnotonly troubleshooting framework for microservices on multi-source data,” in
considermetricsandlogsfromthetargetservicebutshouldalso Proc.IEEE/ACM45thInt.Conf.Softw.Eng.,2023,pp.1750–1762.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore.  Restrictions apply.

LIUetal.:UAC-AD:UNSUPERVISEDADVERSARIALCONTRASTIVELEARNINGFORANOMALYDETECTIONONMULTI-MODAL 3899
[3] N.Zhaoetal.,“Identifyingbadsoftwarechangesviamultimodalanomaly [28] C.Lee,T.Yang,Z.Chen,Y.Su,Y.Yang,andM.R.Lyu,“Heterogeneous
detectionforonlineservicesystems,”inProc.29thACMJointMeeting anomalydetectionforsoftwaresystemsviasemi-supervisedcross-modal
Eur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,2021,pp.527–539. attention,”2023,arXiv:2302.06914.
[4] S.Jinetal.,“Unsupervisedhardexampleminingfromvideosforimproved [29] C.Zhangetal.,“DeepTraLog:Trace-logcombinedmicroserviceanomaly
objectdetection,”inProc.Eur.Conf.Comput.Vis.,2018,pp.307–324. detection through graph-based deep learning,” in Proc. 44th Int. Conf.
[5] C. Zhang, Y. Wang, and W. Tan, “MTHM: Self-supervised multi-task Softw.Eng.,2022,pp.623–634.
anomaly detection with hard example mining,” IEEE Trans. Instrum. [30] J. Bogatinovski and S. Nedelkoski, “Multi-source anomaly detection
Meas.,vol.72,pp.1–13,2023. in distributed it systems,” in Proc. Int. Conf. Serv.-Oriented Comput.,
[6] S.Kong,J.Ai,andM.Lu,“CL-MMAD:Acontrastivelearningbased Springer,2020,pp.201–213.
multimodal software runtime anomaly detection method,” Appl. Sci., [31] J.Huang,Y.Yang,H.Yu,J.Li,andX.Zheng,“Twingraph-basedanomaly
vol.13,no.6,2023,Art.no.3596. detectionviaattentivemulti-modallearningformicroservicesystem,”in
[7] “UAC-AD,”[Online].Available:https://github.com/lhysgithub/UAC-AD Proc.38thIEEE/ACMInt.Conf.Autom.Softw.Eng.,2023,pp.66–78.
[8] M.M.Breunig,H.-P.Kriegel,R.T.Ng,andJ.Sander,“LOF:Identifying [32] X.Li,P.Chen,L.Jing,Z.He,andG.Yu,“Swisslog:Robustanomaly
density-basedlocaloutliers,”inProc.ACMSIGMODInt.Conf.Manage. detectionandlocalizationforinterleavedunstructuredlogs,”IEEETrans.
Data,2000,pp.93–104. DependableSecureComput.,vol.20,no.4,pp.2762–2780,Aug.2023.
[9] J.Tang,Z.Chen,A.-C.Fu,andD.W.Cheung,“Enhancingeffectiveness [33] Y. Chen, M. Yan, D. Yang, X. Zhang, and Z. Wang, “Deep attentive
of outlier detections for low density patterns,” in Proc. Adv. Knowl. anomalydetectionformicroservicesystemswithmultimodaltime-series
Discov.DataMining:6thPacific-AsiaConf.,PAKDD2002Taipei,Taiwan, data,”inProc.IEEEInt.Conf.WebServ.,2022,pp.373–378.
Springer,2002,pp.535–548. [34] Q.Zhang,J.Han,L.Cheng,B.Zhang,andZ.Gong,“Approachtoanomaly
[10] B. Zong et al., “Deep autoencoding gaussian mixture model for unsu- detectioninmicroservicesystemwithmulti-sourcedatastreams,”ZTE
pervisedanomalydetection,”inProc.Int.Conf.Learn.Representations, Commun.,vol.20,no.3,pp.85–92,2022.
2018. [35] I.Goodfellowetal.,“Generativeadversarialnets,”inProc.Adv.Neural
[11] T.Yairi,N.Takeishi,T.Oda,Y.Nakajima,N.Nishimura,andN.Takata, Inf.Process.Syst.,2014,pp.2672–2680.
“Adata-drivenhealthmonitoringmethodforsatellitehousekeepingdata [36] S.Akcay,A.Atapour-Abarghouei,andT.P.Breckon,“GANomaly:Semi-
based on probabilistic clustering and dimensionality reduction,” IEEE supervisedanomalydetectionviaadversarialtraining,”inProc.14thAsian
Trans.Aerosp.Electron.Syst.,vol.53,no.3,pp.1384–1401,Jun.2017. Conf.Comput.Vis.,Perth,Australia,Springer,2019,pp.622–637.
[12] D.M.TaxandR.P.Duin,“Supportvectordatadescription,”Mach.Learn., [37] T.Schlegl,P.Seeböck,S.M.Waldstein,U.Schmidt-Erfurth,andG.Langs,
vol.54,pp.45–66,2004. “Unsupervisedanomalydetectionwithgenerativeadversarialnetworksto
[13] L.Ruffetal.,“Deepone-classclassification,”inProc.Int.Conf.Mach. guide marker discovery,” in Proc. Int. Conf. Inf. Process. Med. Imag.,
Learn.,2018,pp.4393–4402. Springer,2017,pp.146–157.
[14] L.Shen,Z.Li,andJ.Kwok,“Timeseriesanomalydetectionusingtemporal [38] F.Schroff,D.Kalenichenko,andJ.Philbin,“FaceNet:Aunifiedembed-
hierarchicalone-classnetwork,”inProc.Adv.NeuralInf.Process.Syst., dingforfacerecognitionandclustering,”inProc.IEEEConf.Comput.
2020,pp.13016–13026. Vis.PatternRecognit.,2015,pp.815–823.
[15] D.Park,Y.Hoshi,andC.C.Kemp,“Amultimodalanomalydetectorfor [39] S.-J.Peng,Y.Fan,Y.-M.Cheung,X.Liu,Z.Cui,andT.Li,“Towards
robot-assistedfeedingusinganlstm-basedvariationalautoencoder,”IEEE efficientcross-modalanomalydetectionusingtriple-adaptivenetworkand
Robot.Automat.Lett.,vol.3,no.3,pp.1544–1551,Jul.2018. bi-quintuplecontrastivelearning,”IEEETrans.Emerg.TopicsComput.
[16] Y.Su,Y.Zhao,C.Niu,R.Liu,W.Sun,andD.Pei,“Robustanomaly Intell.,vol.8,no.1,pp.697–709,Feb.2024.
detectionformultivariatetimeseriesthroughstochasticrecurrentneural [40] P.He,J.Zhu,Z.Zheng,andM.R.Lyu,“Drain:Anonlinelogparsing
network,”inProc.25thACMSIGKDDInt.Conf.Knowl.Discov.Data approachwithfixeddepthtree,”inProc.IEEEInt.Conf.webServ.,2017,
Mining,2019,pp.2828–2837. pp.33–40.
[17] H.Zhaoetal.,“Multivariatetime-seriesanomalydetectionviagraphatten- [41] K.He,X.Zhang,S.Ren,andJ.Sun,“Deepresiduallearningforimage
tionnetwork,”inProc.IEEEInt.Conf.DataMining,2020,pp.841–850. recognition,”inProc.IEEEConf.Comput.Vis.PatternRecognit.,2016,
[18] J.Zhanetal.,“Stgat-mad:Spatial-temporalgraphattentionnetworkfor pp.770–778.
multivariate time series anomaly detection,” in Proc. IEEE Int. Conf. [42] J. L. Ba, J. R. Kiros, and G. E. Hinton, “Layer normalization,”
Acoust.,SpeechSignalProcess.,2022,pp.3568–3572. 2016,arXiv:1607.06450.
[19] D. Li, D. Chen, B. Jin, L. Shi, J. Goh, and S.-K. Ng, “MAD-GAN: [43] A. Joulin et al., “Fasttext.zip: Compressing text classification models,”
Multivariateanomalydetectionfortimeseriesdatawithgenerativeadver- 2016,arXiv:1612.03651.
sarialnetworks,”inProc.Int.Conf.Artif.NeuralNetw.,Springer,2019, [44] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
pp.703–716. 2014,arXiv:1412.6980.
[20] J. Audibert, P. Michiardi, F. Guyard, S. Marti, and M. A. Zuluaga, [45] M.Maetal.,“Anempiricalinvestigationofmissingdatahandlingincloud
“USAD:Unsupervisedanomalydetectiononmultivariatetimeseries,”in nodefailureprediction,”inProc.30thACMJointEur.Softw.Eng.Conf.
Proc.26thACMSIGKDDInt.Conf.Knowl.Discov.DataMining,2020, Symp.Found.Softw.Eng.,2022,pp.1453–1464.
pp.3395–3404.
[21] W.Xu,“Systemproblemdetectionbyminingconsolelogs,”Universityof Hongyi Liu received the MS degree from Peking
California,Berkeley,Tech.Rep.UCB/EECS-2010–112,2010. University,in2021.Currently,heisworkingtoward
[22] Q.Lin,H.Zhang,J.-G.Lou,Y.Zhang,andX.Chen,“Logclusteringbased thePhDdegreewiththeSchoolofSoftware&Mi-
problemidentificationforonlineservicesystems,”inProc.38thInt.Conf.
croelectronics, Peking University. His research in-
Softw.Eng.Companion,2016,pp.102–111.
terestsincludecouldcomputing,softwarereliability,
[23] S.He,Q.Lin,J.-G.Lou,H.Zhang,M.R.Lyu,andD.Zhang,“Identifying anomalydetection,andAIforsoftwareengineering.
impactfulservicesystemproblemsvialoganalysis,”inProc.26thACM
Joint Meeting Eur. Softw. Eng. Conf. Symp. Found. Softw. Eng., 2018,
pp.60–70.
[24] M.Du,F.Li,G.Zheng,andV.Srikumar,“DeepLog:Anomalydetection
anddiagnosisfromsystemlogsthroughdeeplearning,”inProc.ACM
SIGSACConf.Comput.Commun.Secur.,2017,pp.1285–1298. XiaosongHuangreceivedtheBSdegreefromthe
[25] X. Zhang et al., “Robust log-based anomaly detection on unstable log BeijingInstituteofTechnology,in2021.Heiscur-
data,” in Proc. 27th ACM Joint Meeting Eur. Softw. Eng. Conf. Symp. rentlyworkingtowardthePhDdegreewiththeSchool
Found.Softw.Eng.,2019,pp.807–817. of Computer Science at Peking University. His re-
[26] W.Guan,J.Cao,Y.Gu,andS.Qian,“GRASPED:AGRU-AEnetwork searchinterestsincludeAIOps,softwarereliability,
basedmulti-perspectivebusinessprocessanomalydetectionmodel,”IEEE AIforsoftwareengineering.
Trans.ServicesComput.,vol.16,no.5,pp.3412–3424,Sep./Oct.2023.
[27] Y.Fu,K.Liang,andJ.Xu,“MLog:MogrifierLSTM-basedloganomaly
detectionapproachusingsemanticrepresentation,”IEEETrans.Services
Comput.,vol.16,no.5,pp.3537–3549,Sep./Oct.2023.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore. Restrictions apply.

3900 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
Mengxi Jia received the BS degree from Central ZhonghaiWureceivedthePhDdegreefromZhe-
SouthUniversity,China.Sheiscurrentlyworkingto- jiang University, Hangzhou, China, in 1997. Pre-
wardthePhDdegreewiththeSchoolofSoftwareand viously he worked as a postdoctoral and associate
Microelectronic,PekingUniversity,Beijing,China. professorwiththeInstituteofComputerScienceand
Herresearchinterestsincludemachinelearning,deep Technology, Peking University, Beijing, China. He
representationlearning,AIforsoftwareengineering. is currently a professor and dean with the School
ofSoftwareandMicroelectronics,PekingUniversity.
Hisresearchinterestsincludecloudcomputing,Big
Data,AIandinformationsecurity.
TongJiareceivedthePhDdegreeinsoftwareengi-
neeringfromPekingUniversity,China,in2019.He
iscurrentlyanassistantresearchprofessorwiththe
instituteforartificialintelligence,PekingUniversity,
China.HisresearchinterestsincludeAIOps,anomaly
detection,etc.Hepublishedmorethan30papersin
internationaljournalsandconferences.
YingLi(Member,IEEE)receivedthePhDdegreein
computerscienceandengineeringfromNorthwestern
PolytechnicalUniversity(NWPU),China,in2001.
She is currently a professor with the National En-
JingHanreceivedtheMSdegreefromtheNanjing gineeringResearchCenterofSoftwareEngineering
UniversityofAeronauticsandAstronautics,in2000. and the School of Software and Microelectronics,
Currently,sheisworkingwithZTE.Sheisrespon- Peking University, China. Before joining PKU in
sible for AIOPS in the communications and cloud 2012, she worked as a STSM and senior manager
domains. leadingthedepartmentofdistributedcomputingin
IBMChinaResearchCenter.Herresearchinterests
includedistributedcomputinganddependabilityen-
gineering. She filed 40+ US/CN granted patents and was awarded as “IBM
MasterInventor”.Shepublishedmorethan90academicpapersininternational
journals and conferences and served as PC member of several international
conferencesandreviewerofinternationaljournals.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:36:17 UTC from IEEE Xplore. Restrictions apply.