PDF Download
3772052.3772234.pdf
18 March 2026
Total Citations: 0
. Total Downloads: 132
.
Latest updates: hps://dl.acm.org/doi/10.1145/3772052.3772234 .
.
Published: 13 January 2026
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
DRAM Failure Prediction with Correctable Error Spatial Paerns: A
.
.
Hybrid Learning Approach SoCC '25: ACM Symposium on Cloud
Computing
November 19 - 21, 2025
LEI LIU, Inspur Cloud Information Technology Co., Ltd., Jinan, Shandong, China Online, USA
.
. .
YINLING ZHANG Conference Sponsors:
SIGOPS
. . SIGMOD
.
Open Access Support provided by:
.
Inspur Cloud Information Technology Co., Ltd.
.
SoCC '25: Proceedings of the 2025 ACM Symposium on Cloud Computing (November 2025)
hps://doi.org/10.1145/3772052.3772234
ISBN: 9798400722769
.

DRAM Failure Prediction with Correctable Error Spatial Patterns:
|     |     |     |     | A   | Hybrid | Learning |     | Approach |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
YinlingZhang
|     |     |     | Lei | Liu |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AIOPSOperationCenter
AIOPSOperationCenter
JinanThermalPowerGroupCo.,Ltd
InspurCloudInformationTechnologyCo.,Ltd.
JinanChina
JinanChina
zhangyl01@jinanenergy.cn
liulei20@inspur.com
ABSTRACT multiplememorychips,theymaysurpassthecorrectioncapability
ofECC,potentiallyresultinginDRAMfailures[3].Moreover,the
| Dynamic | Random   | Access |          | Memory (DRAM) |          | failures are a |     |                |     |     |        |       |           |               |      |
| ------- | -------- | ------ | -------- | ------------- | -------- | -------------- | --- | -------------- | --- | --- | ------ | ----- | --------- | ------------- | ---- |
|         |          |        |          |               |          |                | ECC | implementation |     | on  | modern | Intel | platforms | is relatively | less |
| leading | cause of | server | downtime | in cloud      | centers. | Predicting     |     |                |     |     |        |       |           |               |      |
robust,makingitmoresusceptibletobiterrorsoriginatingfroma
DRAMfailurescouldreducedowntimeevents,avoidingdataloss
|     |     |     |     |     |     |     | single | memory |     | chip [4]. | Therefore, |     | relying solely | on  | ECC is |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | --------- | ---------- | --- | -------------- | --- | ------ |
and industry damage. In this study, a novel DRAM failure insufficienttoensurethereliabilityofDRAMsystems.
| predictionmethod |     | based | on spatialpatternsof |     | Correctable | Errors |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | -------------------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(CEs)wasproposed.AfterreconstructingtheCEinformationinto Currently,usingCEinformationtopredictDRAMfailureshas
a featuremap, effective artificial featureswere extracted. And an become a widely accepted approach [4]. In addition, various
|            |            |     |           |     |          |               | hardware |     | information | (such | as  | system | architecture, | vendor, | and |
| ---------- | ---------- | --- | --------- | --- | -------- | ------------- | -------- | --- | ----------- | ----- | --- | ------ | ------------- | ------- | --- |
| innovative | 3D CWT-PCA |     | transform | was | proposed | to render its |          |     |             |       |     |        |               |         |     |
spatial patterns. We explored feature importance using SHAP DIMM model), operational logs (such as temperature and
analysis and visualisation techniques. Then, ResNet and KAN workload), and out-of-band logs (such as SEL and iBMC black
boxlogs)arealsocommonlyutilized[5-8].InCE-basedresearch,
| networks | were employed |     | for hybrid | learning | to  | predict DRAM |     |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
failures. After achieving promising results on the publicly CE information was typically processed as tabular features and
available Large-scale Dataset, we further collected real-world analyzed using Machine Learning (ML) methods [9-16]. As
cloudcenterdataforgeneralizationvalidation. research progressed, the spatial patterns of CEs received
|     |     |     |     |     |     |     | increasing |     | attention | and | were | shown | to outperform | traditional |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | ---- | ----- | ------------- | ----------- | --- |
KEYWORDS
|     |     |     |     |     |     |     | tabular | features | [17, | 18]. | However, | previous | studies | did | not fully |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---- | ---- | -------- | -------- | ------- | --- | --------- |
DRAM Failure, Prediction, AIOps, Hybrid Learning, exploretheeffectivenessofCEspatialfeaturesforDRAMfailure
prediction.
CorrectableError
ThisstudyfocusesonCEspatialpatterns,thoroughlyexplores
|     |     |     |     |     |     |     | various | features, |     | and develops |     | a novel | DRAM | failure prediction |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------------ | --- | ------- | ---- | ------------------ | --- |
1INTRODUCTION
method.Tofacilitatefurtherresearchandimprovereproducibility,
Intheeraofcloudcomputing,cloudservershavebeenwidely
|     |     |     |     |     |     |     | the | algorithm | proposed |     | in this | study | is publicly | available | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------- | ----- | ----------- | --------- | --- |
deployedandadoptedacrossvariousdomains.Inlarge-scalecloud GitHub (https://github.com/syhnndas/dram_failure_prediction).
datacenters,DynamicRandomAccessMemory(DRAM)failures Thecontributionsofthisstudyareasfollows:
| constitute | a significant |     | portion | of hardware |     | malfunctions, |     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accounting for approximately 1/3 of all server hardware failures  We novelly reconstructed the CE information into a 3D
featuremapandextracteddistanceandareametrics.
| [1]. Prior | to the | occurrence | of  | DRAM failures, |     | memory errors |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ---------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 Aunique3DCWT-PCAtransformwasproposedtorenderthe
includingCorrectableErrors(CEs)andUncorrectableErrors(UEs)
| are frequently | observed. |     | Modern | computer | systems | incorporate |     | featuremaps. |          |     |           |     |             |     |           |
| -------------- | --------- | --- | ------ | -------- | ------- | ----------- | --- | ------------ | -------- | --- | --------- | --- | ----------- | --- | --------- |
|                |           |     |        |          |         |             |    | A hybrid     | learning |     | framework | was | constructed | to  | integrate |
ErrorCorrectionCode(ECC)mechanismstoautonomouslydetect
handcraftedanddeepfeatures.
andcorrectdatacorruptionerrors[2].However,whenthenumber
oferroneousbitsbecomesexcessiveortheerrorsspanacross
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor 2RELATEDWORK
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
for profit or commercial advantage and that copies bear this notice and the full DRAM failureprediction methods can be broadly categorized
citationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothers
intothreeclasses:thosebasedonhardwareruntimecharacteristics,
| than the author(s)mustbe |     | honored. | Abstracting | with | creditispermitted. | Tocopy |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | -------- | ----------- | ---- | ------------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
otherwise,orrepublish,to postonserversortoredistribute tolists,requiresprior CEtabularfeatures,andCEspatialfeatures.Inhardwareruntime-
specificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
|     |     |     |     |     |     |     | based | methods, | Sun | et  | al. [5] extracted |     | static parameters |     | such as |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | ----------------- | --- | ----------------- | --- | ------- |
SoCC'25,November19–21,2025,Online,USA
© 2025 Copyright held by the owner/author(s). Publication rights licensed to the memory speed and memory age to predict DRAM failure.
AssociationforComputingMachinery. Mukhanov et al. [6] analyzed hardware features such as memory
ACMISBN979-8-4007-2276-9/25/11
https://doi.org/10.1145/3772052.3772234 accessrateandcachemissrate,andcomparedvarioussupervised
299

| learning     | methods.    | Giurgiu | et          | al. [7] extracted |               | event logs | and      |     |     |     |     |     |     |     |
| ------------ | ----------- | ------- | ----------- | ----------------- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| sensor       | parameters, | and     | constructed |                   | an integrated |            | learning |     |     |     |     |     |     |     |
| approach.    | Literature  | [8]     | proposed    | a coding          | methodology   |            | called   |     |     |     |     |     |     |     |
| Hierarchical | DRAM        | Error   | Code        | (HiDEC),          | which         | analyzed   | the      |     |     |     |     |     |     |     |
valueofworkloadsforDRAMfailurepredictionfrombothmacro
| and micro       |       | perspectives. |       | However,        | hardware |                | runtime |     |     |     |     |     |     |     |
| --------------- | ----- | ------------- | ----- | --------------- | -------- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| characteristics | often | fall          | short | in sufficiently |          | characterizing |         |     |     |     |     |     |     |     |
DRAMfaults.
InstudiesbasedonCEtabularfeatures,Duetal.[9]proposed
anonlinelearningapproachtoprocessCEinformationandpredict
| DRAM faults.   | Alibaba    | Cloud           | hosted | a            | DRAM   | failure prediction |        |     |     |     |     |     |     |     |
| -------------- | ---------- | --------------- | ------ | ------------ | ------ | ------------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| challenge      | at PAKDD   | 2021.           | Using  | the released |        | dataset, Wu        | et al. |     |     |     |     |     |     |     |
| [10] conducted |            | a comparative   |        | study        | on the | performance        | of     |     |     |     |     |     |     |     |
| classical      | ML models. | Subsequently,   |        | Alibaba      |        | conducted          | an in- |     |     |     |     |     |     |     |
| depth study    | on         | CE information, |        | including    | bank,  | rank, row,         | and    |     |     |     |     |     |     |     |
column,andreleasedalargerdataset[11].Bogatinovskietal.[12]
| input the | feature | vectors | of CE | location | fields | into XGBoost | for |     |     |     |     |     |     |     |
| --------- | ------- | ------- | ----- | -------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.1.CESpatialReconfigurationMethods
| DRAM failure | prediction. |     | Research | [13, | 14] further | analyzed | the |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | -------- | ---- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
location, number, and frequency features of CE, and conducted Considering that the feature map may contain many “zeros”,
experiments using various classifiers. Studies [15, 16] analyzed which is unfavorable for feature aggregation, we performed a
|     |     |     |     |     |     |     |     | simple compression |     | operation. |     | Specifically, | the original | map in |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | --- | ------------- | ------------ | ------ |
statisticalinformationsuchasthedifferenceinthenumberofCEs
acrossdifferentbanks.Theyalsoexploredthecorrelationbetween Fig.1(a)wascompressedintoasmallerH×W×Cmap,asshownin
location fields and faults. Although these studies explored CE Fig. 1(b). The numbers of the corresponding regions were
features in depth, they were limited to tabular features and superimposed and the regions were not overlapped during
traditionalmachinelearningapproaches. compression. The resulting CE spactial map was used for
subsequentfeatureextraction.
Inrecentyears,thespatialpatternsofCEshaveattractedmuch
| attention | for their | excellent | prediction |     | effects. | Typical | research |     |     |     |     |     |     |     |
| --------- | --------- | --------- | ---------- | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
3.2ArtificialFeatureExtraction
| comes from   | Intel    | [17], where | scholars  | revealed |     | several high-risk  |     |                    |      |                  |     |      |                   |               |
| ------------ | -------- | ----------- | --------- | -------- | --- | ------------------ | --- | ------------------ | ---- | ---------------- | --- | ---- | ----------------- | ------------- |
|              |          |             |           |          |     |                    |     | Studies            | [17, | 18] demonstrated |     | that | the more          | dispersed the |
| CE alignment | patterns | and         | performed | DRAM     |     | failure prediction |     |                    |      |                  |     |      |                   |               |
|              |          |             |           |          |     |                    |     | distributionofCEs, |      | themorelikelyit  |     | may  | beto leadtoUEsand |               |
basedonthem.Study[18]alsoexploredthemethodofpredicting
|     |     |     |     |     |     |     |     | DRAM | failures. | Meanwhile, |     | study [15] | concluded | that the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---------- | --- | ---------- | --------- | -------- |
UE based on CE spatial structure. And They proved the differenceinthenumberofCEsacrossbanksisagoodpredictor.
| effectiveness | of  | the CE | spatial | structure. | However, |     | current |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ------- | ---------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Basedonthesefindings,weextracted10Artificialfeatures(AFs)
| researches | on prediction |     | based | on spatial | structure | are immature |     |          |             |      |     |          |              |           |
| ---------- | ------------- | --- | ----- | ---------- | --------- | ------------ | --- | -------- | ----------- | ---- | --- | -------- | ------------ | --------- |
|            |               |     |       |            |           |              |     | from the | CE spactial | map, | as  | shown in | Table 1. The | schematic |
andlackofsystematicalgorithms.Toaddresstheseshortcomings,
diagramoftheextractionmethodisshowninFig.2.
| this study | proposes | a   | hybrid | learning | approach | based | on CE |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ------ | -------- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
spatialpatterns. The features HD, WD, CD, 2DD, 3DD all measure the
|          |     |     |     |     |     |     |     | distancebetween                                    |     | two CE         | clusters, | andtheconciseformulas |             | have      |
| -------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | -------------- | --------- | --------------------- | ----------- | --------- |
|          |     |     |     |     |     |     |     | been attached                                      | to  | thefigure.     | And       | themetrics            | MHD,        | MWD, MCD, |
| 3METHODS |     |     |     |     |     |     |     | M2DD,M3DDarethecorrespondingmaximumvaluestomeasure |     |                |           |                       |             |           |
|          |     |     |     |     |     |     |     | the degree                                         | of  | CE dispersion. |           | NA16,                 | NA64, NA144 | are the   |
3.1CESpaceReconstruction maximum number of CEs covered by different areas on a
|        |                   |     |     |       |      |      |        | particular | bank, | which | measures | the degree | of CE | clustering on |
| ------ | ----------------- | --- | --- | ----- | ---- | ---- | ------ | ---------- | ----- | ----- | -------- | ---------- | ----- | ------------- |
| In the | microarchitecture |     | of  | DRAM, | each | DRAM | module |            |       |       |          |            |       |               |
thisbank.
consistsofmultipleDual-InlineMemoryModules(DIMMs).Each
DIMMhastworanks,andeachrankcontains16banks.Eachbank Table1.Listofartificialfeatures
has217rowsand210columns[11].Therefore,theCElogcontains
|            |          |       |      |                    |     |               |     | Features |     | Description |     |     |     |     |
| ---------- | -------- | ----- | ---- | ------------------ | --- | ------------- | --- | -------- | --- | ----------- | --- | --- | --- | --- |
| fieldssuch | as rank, | bank, | row, | and col toidentify |     | thelocationof |     |          |     |             |     |     |     |     |
|            |          |       |      |                    |     |               |     | NCE      |     | NumberofCE  |     |     |     |     |
errors,asshowninthetableatthetopofFig.1(a). MHD MaximumHeightDistance
|     |     |     |     |     |     |     |     | MWD |     | MaximumWidthDistance |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
In this study, we reconstructed the bank, row, and column MCD MaximumChannelDistance
fieldsintomulti-channelfeaturemaps.Specifically,wetreatedthe NCEE NumberofCEsontheedges
three fields as a 3D coordinate [bank,row,col], and assigned a M2DD Maximum2Ddistance
valueof1(graysquare)atthatpositiontoindicatetheoccurrence M3DD Maximum3Ddistance
|     |     |     |     |     |     |     |     | NA16 |     | NumberofCEscoveredbyanareaof16 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------------------------ | --- | --- | --- | --- |
ofoneCE.All otherpositionsweresetto0(whitesquares).This NA64 NumberofCEscoveredbyanareaof64
process resulted in the feature map shown in Fig. 1. Considering NA144 NumberofCEscoveredbyanareaof144
themaximumvaluesofbank,row,andcol,wesetthefeaturemap
dimensionstoRow=217,Col=210,andBank=16.
300

|     |     |     |     |     |     |     |     | (a)SampleServer_23495 |     |     |     | (b)SampleServer_27867 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --------------------- | --- | --- |
Fig.3.CWTmapgeneratedby3DCWT-PCAmethod
Fig.2.Schematicofthefeatureextractionprocess
3.4HybridLearning
3.33DCWT-PCATransform
WeconstructedaResNetnetwork[19]toextractfeaturesfrom
| We proposed |     | a unique | transform | method | to  | extract | wavelet |             |       |           |     |               |         |            |
| ----------- | --- | -------- | --------- | ------ | --- | ------- | ------- | ----------- | ----- | --------- | --- | ------------- | ------- | ---------- |
|             |     |          |           |        |     |         |         | the CWTmap, | which | consisted | of  | four residual | blocks. | Initially, |
coefficientsfromCEspactialmap,andthendownscaledittoRGB
|            |        |        |                  |     |          |     |         | the complete | ResNet  | architecture, |               | including | the final | Linear and |
| ---------- | ------ | ------ | ---------------- | --- | -------- | --- | ------- | ------------ | ------- | ------------- | ------------- | --------- | --------- | ---------- |
| image. For | the 3D | matrix | X(h,w,c)RHWC, |     | discrete |     | CWT was |              |         |               |               |           |           |            |
|            |        |        |                  |     |          |     |         | Softmax      | layers, | was used      | for training. | After     | training, | these two  |
performedforeachrowhofeachchannelc: layers were frozen, and the output from the Flatten layer was
|     |     |     |     |     |     |     |     | extracted | as Deep | Features | (DFs). | Following | the | fusion of |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------- | ------ | --------- | --- | --------- |
W
|     |     | W(h,w,a,c)X(h,t,c) |     |     | * (t) |     | (1) |     |     |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a ,b Artificial Features (AFs) and DFs, SHAP analysis [20] was
t1
|                       |     |        |                                  |           |     |        |            | applied for | feature   | selection.   | In  | addition,  | the KAN network | [21]       |
| --------------------- | --- | ------ | -------------------------------- | --------- | --- | ------ | ---------- | ----------- | --------- | ------------ | --- | ---------- | --------------- | ---------- |
| where a isthescaleand |     |        | bw isthetimeposition.Thewavelet |           |     |        |            |             |           |              |     |            |                 |            |
|                       |     |        |                                  |           |     |        |            | had the     | advantage | of learnable |     | activation | functions.      | And it can |
| basis function(t)    |     | is the | Morlet                           | wavelet, |     | (t) is | the result |             |           |              |     |            |                 |            |
a,b
replacetheweightparameterswithlearnableunivariatefunctions.
afterscaletransformation:
WeintroducedtheKANnetworkforfinalprediction.
|                         |     |     |      | 1 tb |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                         |     |    | (t) |       |    |     | (2) |     |     |     |     |     |     |     |
|                         |     | a,b |      | |a|    | a  |     |     |     |     |     |     |     |     |     |
| Then,takethemeanonscale |     |     | a:   |         |     |     |     |     |     |     |     |     |     |     |
4EXPERIMENTS
1 |W(h,w,a,c)| A
|     | CWT | (h,w,c) |     |     |     |     | (3) |            |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|     |     | mean     |     | A   |     |     |     | 4.1Dataset |     |     |     |     |     |     |
a1
Thecoefficientmatrix CWT (h,w,c) ofshape[H,W,C]wasthen We used the Large-scale Dataset released by Alibaba Group
mean
[11].Itcontainedhistoricaldatafrom30,502servers.Thedataset
| obtained. Since | the        | number       | of channels |         | C may   | be large, | it is not |             |         |         |             |             |           |           |
| --------------- | ---------- | ------------ | ----------- | ------- | ------- | --------- | --------- | ----------- | ------- | ------- | ----------- | ----------- | --------- | --------- |
|                 |            |              |             |         |         |           |           | included    | over 75 | million | CE records, | collected   | over      | 8 months. |
| conducive       | to feature | aggregation. |             | We      | further | perform   | PCA       |             |         |         |             |             |           |           |
|                 |            |              |             |         |         |           |           | During this | period, | 3,017   | servers     | experienced | failures. | Among     |
| dimensionality  | reduction  | on           | CWT         | (h,w,c) | to      | compress  | C into    |             |         |         |             |             |           |           |
mean
|     |     |     |     |     |     |     |     | them, 2,139 | servers | had | CEs recorded |     | before the | failure. The |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ------------ | --- | ---------- | ------------ |
C.ThisstepwasperformedusingthePCAfunctionofthescikit-
datasetincludedthreefiles,“mcelog”recordedCElogs,including
learn package. And the pixel values were linearly normalized to timestamp, rank, bank, row, and column; “inventory” provided
| [0,255]. The | final | coefficient | map | obtained | was | called | CWTmap |          |        |     |       |              |                   |     |
| ------------ | ----- | ----------- | --- | -------- | --- | ------ | ------ | -------- | ------ | --- | ----- | ------------ | ----------------- | --- |
|              |       |             |     |          |     |        |        | hardware | vendor | and | model | information; | “trouble_tickets” |     |
andtheshapewas[H,W,C].Theconcisestepsareasfollows:
|     |     |     |     |     |     |     |     | contained | server | IDs and | failure | times. To | ensure class | balance, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------- | ------- | --------- | ------------ | -------- |
weusedrandomundersampling[22]toselectthesamenumberof
| CWT | (h,w,c)PCACWT |     | (h,w,c)NormalizationCWTmap(h,w,c) |     |     |     | (4) |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mean mean normal and failure samples. The data was then split into training
Inthisarticle,severalcomparisonexperimentswereconducted
|             |       |       |      |          |      |           |     | and testing | sets | in an 8:2 | ratio.    | Following | [10], our      | prediction |
| ----------- | ----- | ----- | ---- | -------- | ---- | --------- | --- | ----------- | ---- | --------- | --------- | --------- | -------------- | ---------- |
| and finally | H=32, | W=16, | C=16 | and C3 | were | selected. | The |             |      |           |           |           |                |            |
|             |       |       |      |          |      |           |     | experiment  | was  | performed | 5 minutes | in        | advance, i.e., | only CE    |
CWTmapobtainedfromthetwoexamplesamplesisshowninFig.
|                                                   |     |     |     |     |     |     |     | records generated |     | more than | 5   | minutes | before the | failure were |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | --- | ------- | ---------- | ------------ |
| 3.Theseimageswillbeusedforthedeeplearningnetwork. |     |     |     |     |     |     |     | used.             |     |           |     |         |            |              |
Inaddition,real-worldproductiondatawerecollectedfromthe
InspurCloudDataCenter.Morethan3,600serversacross14test
|     |     |     |     |     |     |     |     | cloud centers | nationwide |     | were | monitored. | From July | 2023 to |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ---- | ---------- | --------- | ------- |
March2025,over1millionCErecordswerecollected.Atotalof
106serversexperiencedDRAMfailures,allofwhichemittedCEs
|     |     |     |     |     |     |     |     | before the | failure. | Fig. 4 | shows | the CE information | fields, | which |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | ----- | ------------------ | ------- | ----- |
includedkeyinformationsuchasbank(ba),row(ce_row),andcol
|     |     |     |     |     |     |     |     | (ce_col).       | Random | undersampling |             | was again | used to          | select 220 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ------------- | ----------- | --------- | ---------------- | ---------- |
|     |     |     |     |     |     |     |     | normal samples. |        | Due to        | the smaller | data      | size, the Inspur | Cloud      |
301

Data was only used to evaluate the generalization ability of the features are shown in Fig. 6. The x-axis represents the SHAP
proposed method. Table 2 summarizes all datasets used in this values, which describetheimpact of each feature onthe model’s
study,alongwiththenumberofsamplesandtheirpurposes. output. Larger positive or negative values indicate greater
importance.They-axisrepresentsthefeatureidentifiers.Onlythe
top20mostimportantfeaturesareshowninthefigure.Theorder
ofthefeaturesonthey-axisisbasedontheabsolutevalueofthe
SHAPvalues,withthemostimportantfeatureslistedatthetop.
Fig.4.CEsintheInspurCloudData
Table2.Datasets,samplesizes,andtheirusage
Numberofsamples
| Dataset |     |     |     |     | Usage |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Failure/Normal)
| Large-scale |     |     |     |     | Training | and |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4278(2139/2139)
| Dataset     |     |              |     |     | testing         |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InspurCloud |     |              |     |     | Generalizabilit |     |     |     |     |     |     |     |     |     |
| Data        |     | 326(106/220) |     |     | yvalidation     |     |     |     |     |     |     |     |     |     |
4.2Experiments
| The overall | experimental |     | workflow | isillustrated |     | inFig. | 5. On |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | -------- | ------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
onehand,theCEspatialmapwastransformedusingthe3DCWT-
| PCA method             | to generate |                 | the CWTmap, |             | which         | was then | fed into |     |     |     |     |     |     |     |
| ---------------------- | ----------- | --------------- | ----------- | ----------- | ------------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| the ResNet             | for         | feature         | extraction. | The         | difference    |          | between  |     |     |     |     |     |     |     |
| ResidualBlock-1        | and         | ResidualBlock-2 |             | lay         | in thepadding |          | settings |     |     |     |     |     |     |     |
| of their convolutional |             | layers.         | By          | configuring | the           | Flatten  | layer to |     |     |     |     |     |     |     |
output 16 dimensions, a total of 16 Deep Features (DFs) were Fig.6.SHAPanalysisresults
extracted,denotedasDF1toDF16.
Asshown,amongthetop10mostimportantfeatures,8areDF
|     |     |     |     |     |     |     |     | features,      | demonstrating | the      | feature        | extraction | capability | of the    |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | -------- | -------------- | ---------- | ---------- | --------- |
|     |     |     |     |     |     |     |     | ResNet.        | M2DD and      | NA16     | are relatively | important  | AF         | features, |
|     |     |     |     |     |     |     |     | both extracted | from          | the same | bank.          | Similarly, | MWD, NA64, | and       |
NA144arefeaturesfromthesamebank.ThissuggeststhattheCE
distributioncharacteristicsonthesamebankhavestrongpotential
|     |     |     |     |     |     |     |     | for DRAM        | fault characterization. |               | In          | contrast,     | NCE, as     | well as |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------------------- | ------------- | ----------- | ------------- | ----------- | ------- |
|     |     |     |     |     |     |     |     | MHD, NCEE,      | and                     | M3DD—features |             | not shown     | in the      | figure— |
|     |     |     |     |     |     |     |     | were relatively | less                    | important.    | Through     | multiple      | comparative |         |
|     |     |     |     |     |     |     |     | experiments,    | the optimal             |               | feature set | was selected. | The         | best    |
predictionperformancewasachievedusingthetop18features.
5.2DRAMFailurePredictionResults
Fig.5.ExperimentalWorkflow
|        |       |       |          |            |          |       |     | We conducted | prediction |     | experiments | using | only DF | features, |
| ------ | ----- | ----- | -------- | ---------- | -------- | ----- | --- | ------------ | ---------- | --- | ----------- | ----- | ------- | --------- |
| On the | other | hand, | a set of | Artificial | Features | (AFs) | was |              |            |     |             |       |         |           |
onlyAFfeatures,andthefusionofboth.TheimpactofSHAPwas
extracted from the CE spatial map, as listed in Table 1. These also discussed. When SHAP was applied, the top 18 most
handcrafted features were then combined with the DFs. SHAP important features were selected for the experiments. The results
analysis [20] was applied to identify themost important features. ontheLarge-scaleDatasetareshowninTable3.Inthecalculation
| Finally, the | KAN | network | was | used to predict | whether | a   | DRAM |            |         |        |                |         |         |      |
| ------------ | --- | ------- | --- | --------------- | ------- | --- | ---- | ---------- | ------- | ------ | -------------- | ------- | ------- | ---- |
|              |     |         |     |                 |         |     |      | of metrics | such as | Recall | and Precision, | failure | samples | were |
failurewouldoccurinthenearfuture. considered as positive samples, and normal samples were
consideredasnegativesamples.
| 5RESULTSAND |     |     | ANALYSIS |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.1SHAPAnalysis
| After | the fusion | of DF | features | and AF | features, | a total | of 26 |     |     |     |     |     |     |     |
| ----- | ---------- | ----- | -------- | ------ | --------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
featureswereobtained.TheresultsoftheSHAPanalysisonthese
302

Table3.DRAMfailurepredictionresults(onLarge-scaleDataset)
Result(%)
Features
|            |     | Accuracy | Recall | Precision |     | F1-score |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| DF         |     | 71.23    | 75.43  | 68.59     |     | 71.85    |     |     |     |     |     |     |     |
| DF+SHAP    |     | 79.65    | 76.43  | 70.32     |     | 73.25    |     |     |     |     |     |     |     |
| AF         |     | 69.87    | 66.78  | 72.12     |     | 69.35    |     |     |     |     |     |     |     |
| AF+SHAP    |     | 70.33    | 69.18  | 75.64     |     | 72.27    |     |     |     |     |     |     |     |
| DF+AF      |     | 82.30    | 77.23  | 76.22     |     | 76.72    |     |     |     |     |     |     |     |
| DF+AF+SHAP |     | 81.60    | 79.73  | 74.88     |     | 77.23    |     |     |     |     |     |     |     |
Fig.8.Effectsofdifferentclassifiers
5.4GeneralizabilityVerification
|     |     |     |     |     |     |     | After developing |                | the | method      | on the public |      | dataset, we |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------------- | --- | ----------- | ------------- | ---- | ----------- |
|     |     |     |     |     |     |     | conducted        | generalization |     | experiments | on data       | from | real-world  |
cloudcenter.TheparametersoftheResNetandKANmodelswere
|     |     |     |     |     |     |     | determined    | based  | on the  | public dataset. | The           | entire pipeline | was       |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------- | --------------- | ------------- | --------------- | --------- |
|     |     |     |     |     |     |     | then applied  | to the | Inspur  | Cloud Data.     | And forecasts |                 | were made |
|     |     |     |     |     |     |     | for different | time   | windows | in advance.     | Different     | time            | windows   |
meandifferentamountsofCEdataareavailable.AsshowninFig.
Fig.7.Resultsofdifferentfeaturecombinations
9,assumingthataDRAMfailureoccursatthemomentt1andthe
Adonut chartwas plottedtofurthercomparetheperformance prediction window is T, only the data before the moment t0 is
| ofvariousfeaturecombinations,asshowninFig.7.Insuchfailure |              |          |                   |               |     |            | available. |     |     |     |     |     |     |
| --------------------------------------------------------- | ------------ | -------- | ----------------- | ------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| prediction                                                | experiments, |          | the Recall metric | is relatively |     | important. |            |     |     |     |     |     |     |
| When only                                                 | AF           | features | were used,        | the Recall    | was | 66.78%,    |            |     |     |     |     |     |     |
indicatingthatthehandcraftedfeaturesextractedwereinsufficient
| to represent | DRAM | faults. | In contrast, | DF features |     | performed |     |     |     |     |     |     |     |
| ------------ | ---- | ------- | ------------ | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
betterthanAFfeatures.Thebestperformancewasachievedwhen
bothfeaturesetswereusedtogether,withaRecallof77.23%.The
importanceoftheSHAPalgorithmisalsoevident.Whetherusing
| AF or DF | alone, | or both | in combination, | incorporating |     | SHAP |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --------------- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Fig.9.Schematicofthepredictiontimewindow
| consistently | improved |     | performance. | The | DF+AF+SHAP |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
combinationachievedthehighestRecallandF1-score. Table4.PredictionresultsontheInspurCloudData.
Prediction
5.3EffectsofDifferentClassifiers Accuracy Recall Precision F1-score
window(T)
Experiments were conducted on Random Forest (RF), 10min 65.34% 51.89% 47.01% 49.33%
XGBoost,andtheKANnetwork,withresultsshowninFig.8.The
|              |         |                 |              |           |              |             | 5min |     | 73.62% | 65.09% | 58.47% |     | 61.61% |
| ------------ | ------- | --------------- | ------------ | --------- | ------------ | ----------- | ---- | --- | ------ | ------ | ------ | --- | ------ |
| dataset used | was     | the Large-scale | Dataset.     | The       | KAN network, | an          |      |     |        |        |        |     |        |
|              |         |                 |              |           |              |             | 2min |     | 73.93% | 66.04% | 58.82% |     | 62.22% |
| improvement  | on      | MLP [21],       | was proposed | in        | 2024.        | The results |      |     |        |        |        |     |        |
|              |         |                 |              |           |              |             | 1min |     | 76.38% | 67.92% | 62.61% |     | 65.16% |
| showed       | that RF | achieved        | the highest  | Accuracy, |              | XGBoost     |      |     |        |        |        |     |        |
achieved the highest Precision and F1-score. And the KAN In the Large-scale Dataset, predictions were made with a 5-
|     |     |     |     |     |     |     | minute time | window. | To  | examine | the impact | of the | prediction |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ------- | ---------- | ------ | ---------- |
networkachievedthehighestRecall,withanacceptableF1-score,
window,experimentswereconductedontherealclouddatacenter
makingitthebest-performingmodel.
datawithtimewindowsof10minutes,5minutes,2minutes,and
|     |     |     |     |     |     |     | 1 minute, | respectively. | The | results | are shown | in Table | 4. When |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------- | --------- | -------- | ------- |
predictingwitha10-minuteleadtime,theRecallwasonly51.89%.
|     |     |     |     |     |     |     | Asit gets closer | tothefailure, |     | theRecall | valueincreases. |     | Thisis |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------- | --- | --------- | --------------- | --- | ------ |
similartothefindingsin[11],wherealargenumberofCEsoften
occurjustbeforeaDRAMfailure.
|     |     |     |     |     |     |     | Currently,      | thetypical | timerequired |           | tomitigate   | DRAM | failure     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------ | --------- | ------------ | ---- | ----------- |
|     |     |     |     |     |     |     | in the industry | is         | around       | 5 minutes | [10], making | 5    | minutes the |
idealpredictionwindow.However,theresultsfor2-minuteand1-
|     |     |     |     |     |     |     | minute lead       | times | indicate     | that shorter | prediction    | windows | yield      |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | ------------ | ------------ | ------------- | ------- | ---------- |
|     |     |     |     |     |     |     | better prediction |       | performance. | This         | also suggests | that    | industries |
shouldstrivetoreducethefailuremitigationtime.Asshowninthe
303

| confusion | matrix    | in Fig. 10,       | the number | of predicted | Pre-Failure |     |     |     |     |     |     |     |
| --------- | --------- | ----------------- | ---------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| samples   | increases | as the prediction | window     | shortens     | (from 55 to |     |     |     |     |     |     |     |
72).
|     |     |            |     |           |     |     | (a)CWTmap |     | (b)Gran-CAMmap |     |     |     |
| --- | --- | ---------- | --- | --------- | --- | --- | --------- | --- | -------------- | --- | --- | --- |
|     |     | (a)T=10min |     | (b)T=5min |     |     |           |     |                |     |     |     |
|     |     |            |     |           |     |     | (c)CWTmap |     | (d)Gran-CAMmap |     |     |     |
|     |     | (c)T=2min  |     | (d)T=1min |     |     |           |     |                |     |     |     |
Fig.11.Grad-CAMVisualization
Fig.10.Confusionmatrixfordifferentpredictionwindows
Table5.ComparisonofRelatedStudies
Result(%)
|     | Literatures       |     |     | Focus | Specificfeatures      |     |     |           |        |          |     |     |
| --- | ----------------- | --- | --- | ----- | --------------------- | --- | --- | --------- | ------ | -------- | --- | --- |
|     |                   |     |     |       |                       |     |     | Precision | Recall | F1-score |     |     |
|     | X.Duetal.[9],2018 |     |     |       | Cells,Rows,andColumns |     |     | 64.9      | 57.1   | 60.3     |     |     |
Z.Wuetal.[10],2021 Rows,ColumnsandKerneladdressfeatures 58.9 40.5 48.0
Counterfeatures,Componentfeatures,
|     | Z.Chengetal.[11],2022 |     |     | CEtabular |     |     |     | 59.6 | 66.8 | 62.9 |     |     |
| --- | --------------------- | --- | --- | --------- | --- | --- | --- | ---- | ---- | ---- | --- | --- |
StatisticalfeaturesandConfigurationfeatures
features
Q.Yuetal.[14],2023 CEErrorRate,FaultCounts,DQ-BeatError 63.5 57.4 60.3
bits,ErrorBitPatternsandMemoryEvents
AddressmcefeaturesandKerneladdress
|     | F.Yuetal.[15],2021 |     |     |     |     |     |     | 50.9 | 63.6 | 56.6 |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | --- | --- |
features
C.Lietal.[17],2022 RiskyCEIndicatorandFaultindicators 78.0 81.5 79.7
|     |                    |     |     | CESpatial | DQ-BeatErrorBitsandCEpatternindicators |     |     |      |      |      |     |     |
| --- | ------------------ | --- | --- | --------- | -------------------------------------- | --- | --- | ---- | ---- | ---- | --- | --- |
|     | Q.Yuetal.[18],2023 |     |     |           |                                        |     |     | 53.2 | 82.0 | 64.4 |     |     |
patterns
Artificialfeatures,deepfeatures,hybrid
|     | Ourwork |     |     |     |     |     |     | 74.88 | 79.73 | 77.23 |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | --- | --- |
learninginCEspatialpatterns
5.5VisualizationExploration this conclusion needs further validation through subsequent
experiments.
| SHAP       | analysis   | clearly identifies |     | which artificial | features are   |     |     |     |     |     |     |     |
| ---------- | ---------- | ------------------ | --- | ---------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| relatively | important. | However,           | the | black-box        | nature of deep |     |     |     |     |     |     |     |
learningmakesitchallengingtodeterminetheimportanceofdeep
6DISCUSSION
| features. | In this | section, the | Grad-CAM | algorithm | was used to |     |     |     |     |     |     |     |
| --------- | ------- | ------------ | -------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
explore the importance of the CWTmap and ResNet. The The studies on DRAM failure prediction are mainly based on
visualization results for two randomly selected CWTmaps are CE table features, while there are also some studies based on
|     |     |     |     |     |     | spatial structure. | The | latest related | studies | are shown | in  | Table 5. |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | -------------- | ------- | --------- | --- | -------- |
showninFig.11.
Mostoftheprimitivetablefeatures,suchasCells,Rows,Columns
| It  | can be | observed that | the network | focuses | more on the |     |     |     |     |     |     |     |
| --- | ------ | ------------- | ----------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
andKerneladdress,donothaveverygoodfailurecharacterisation
| regions | with | low wavelet coefficient |     | energy (green | areas) in the |             |          |                   |     |            |     |        |
| ------- | ---- | ----------------------- | --- | ------------- | ------------- | ----------- | -------- | ----------------- | --- | ---------- | --- | ------ |
|         |      |                         |     |               |               | capability, | with the | resulting Recalls | of  | only 57.1% | and | 40.5%. |
CWTmap, whilegiving less attentionto high-energy regions(red Later,scholarsproposedavarietyofderivedfeaturesbasedonthe
areas).Thismaybebecausethelow-energyregionscorrespondto
|      |           |                   |      |            |               | original features, | such           | as CE Error | Rate,  | DQ-Beat | Error     | bits and |
| ---- | --------- | ----------------- | ---- | ---------- | ------------- | ------------------ | -------------- | ----------- | ------ | ------- | --------- | -------- |
| more | scattered | CE distributions. | This | indirectly | suggests that |                    |                |             |        |         |           |          |
|      |           |                   |      |            |               | so on.             | These features | enhanced    | Recall | and     | confirmed | the      |
scatteredCEsaremorelikelytoleadtoDRAMfailures.However,
|     |     |     |     |     |     | effectiveness | of feature | engineering. | However, |     | these researches |     |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | ------------ | -------- | --- | ---------------- | --- |
werestillnotfreefromthelimitationsofformfeatures.
304

In contrast, the discovery of spatial features, especially the [4] Q. Yu, J. Cardoso and O. Kao, "Unveiling DRAM Failures Across
Risky CE pattern [17], has pushed the research in this field DifferentCPUArchitecturesinLarge-ScaleDatacenters,"2024IEEE44th
forward.ItseemsthatthespatiallayoutoftheCEcanapproximate International Conference on Distributed Computing Systems (ICDCS),
|                    |     |        |       |         |            |        |       | Jersey | City, | NJ, | USA, | 2024, | pp. | 1462-1463, | doi: |
| ------------------ | --- | ------ | ----- | ------- | ---------- | ------ | ----- | ------ | ----- | --- | ---- | ----- | --- | ---------- | ---- |
| the representation |     | of the | error | bits in | the actual | memory | stick |        |       |     |      |       |     |            |      |
10.1109/ICDCS60910.2024.00152.
| where they | occur.    | They | obtained | the Recall   | of  | 78.0%. Similarly, |         |             |                 |     |           |     |          |          |         |
| ---------- | --------- | ---- | -------- | ------------ | --- | ----------------- | ------- | ----------- | --------------- | --- | --------- | --- | -------- | -------- | ------- |
|            |           |      |          |              |     |                   |         | [5] X. Sun, | K. Chakrabarty, |     | R. Huang, | Y.  | Chen, B. | Zhao and | H. Cao, |
| study [18] | inherited | this | finding  | and combined |     | it with           | DQ-Beat |             |                 |     |           |     |          |          |         |
"System-levelhardwarefailurepredictionusingdeeplearning,"201956th
ErrorBitsfrom[14]toobtainbetterresults.However,thestudies
ACM/IEEEDesignAutomationConference(DAC),LasVegas,NV,USA,
| [17,18] | do not | seem | to be suitable |     | for engineering |     | landing, | 2019,pp.1-6. |     |     |     |     |     |     |     |
| ------- | ------ | ---- | -------------- | --- | --------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
reflected intheidealisticand not easily quantifiablenatureof the [6]L.Mukhanov,K.Tovletoglou,H.Vandierendonck,D.S.Nikolopoulos
RiskyCE pattern.As wellasthefact thatDQ-Beat Errorbitsare and G. Karakonstantis, "Workload-Aware DRAM Error Prediction using
|                 |            |                          |           |          |             |            |          | Machine          | Learning," | 2019 | IEEE International |          | Symposium | on           | Workload |
| --------------- | ---------- | ------------------------ | --------- | -------- | ----------- | ---------- | -------- | ---------------- | ---------- | ---- | ------------------ | -------- | --------- | ------------ | -------- |
| difficult       | to compute | in                       | real-time | in large | cloud       | centres,   | they are |                  |            |      |                    |          |           |              |          |
|                 |            |                          |           |          |             |            |          | Characterization | (IISWC),   |      | Orlando,           | FL, USA, | 2019,     | pp. 106-118, | doi:     |
| onlysuitablefor |            | analysinghistoricaldata. |           |          | Inaddition, | theirstudy |          |                  |            |      |                    |          |           |              |          |
10.1109/IISWC47752.2019.9041963.
onlyusedpubliclyavailableLarge-scaleDatasetanddidnotverify
|     |     |     |     |     |     |     |     | [7] I. Giurgiu, | J.  | Szabo, D. | Wiesmann, | and | J. Bird, | "Predicting | DRAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --------- | --- | -------- | ----------- | ---- |
thefeasibilityonrealcloudcentredata.
reliabilityinthefieldwithmachinelearning,"InProceedingsofthe18th
|      |            |     |           |         |     |            |          | ACM/IFIP/USENIX |             | Middleware |               | Conference: |            | Industrial | Track      |
| ---- | ---------- | --- | --------- | ------- | --- | ---------- | -------- | --------------- | ----------- | ---------- | ------------- | ----------- | ---------- | ---------- | ---------- |
| This | study drew | on  | the ideas | of [17, | 18] | and, based | on this, |                 |             |            |               |             |            |            |            |
|      |            |     |           |         |     |            |          | (Middleware).   | Association |            | for Computing |             | Machinery, | New        | York, USA, |
innovativelyproposedtoreconstructtheCEintoafeaturemapfor
15–21,2017,doi:10.1145/3154448.3154451
quantification.Inadditionawiderangeoffeaturescontainingboth
[8]X.Wang,Y.Li,Y.Chen,S.Wang,Y.DuandC.He,"OnWorkload-
artificialanddeepfeaturesareextracted,makingthefeaturesmore Aware DRAM Failure Prediction in Large-Scale Data Centers," 2021
comprehensive compared to previous studies. Comparable results IEEE39thVLSITestSymposium(VTS),SanDiego,CA,USA,2021,pp.
to existing studies were obtained on the public dataset, i.e., the 1-6,doi:10.1109/VTS50974.2021.9441059.
[9]X.DuandC.Li,"MemoryFailurePredictionUsingOnlineLearning,"
| Recall of | 79.73% | and | the Precision |     | of 74.88%. | The | proposed |                |     |                   |     |           |     |        |         |
| --------- | ------ | --- | ------------- | --- | ---------- | --- | -------- | -------------- | --- | ----------------- | --- | --------- | --- | ------ | ------- |
|           |        |     |               |     |            |     |          | In Proceedings | of  | the International |     | Symposium | on  | Memory | Systems |
methodhasbeensuccessfullyengineeredanddeployedonalarge-
|               |     |            |       |         |          |          |     | (MEMSYS). | Association | for | Computing | Machinery, |     | New | York, 2018, |
| ------------- | --- | ---------- | ----- | ------- | -------- | -------- | --- | --------- | ----------- | --- | --------- | ---------- | --- | --- | ----------- |
| scale cluster | at  | the Inspur | Cloud | Center, | yielding | a Recall | of  |           |             |     |           |            |     |     |             |
USA,38–49,doi:10.1145/3240302.3240309.
65.09%asreportedinTable4.
|     |     |     |     |     |     |     |     | [10] Z. Wu, | H. Xu, | G. Pang, | F. Yu, | Y. Wang, | S.  | Jian, and | Y. Wang, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | -------- | ------ | -------- | --- | --------- | -------- |
"DramFailurePredictioninAiops:EmpiricalEvaluation,Challengesand
Opportunities,"arXivpreprintarXiv:2104.15052,2021.
7CONCLUSION [11]Z.Cheng,S.Han,P.P.C.Lee,X.Li,J.LiuandZ.Li,"AnIn-Depth
|      |               |     |           |         |          |            |      | Correlative | Study | Between | DRAM | Errors | and | Server | Failures in |
| ---- | ------------- | --- | --------- | ------- | -------- | ---------- | ---- | ----------- | ----- | ------- | ---- | ------ | --- | ------ | ----------- |
| This | study focused |     | on the CE | spatial | patterns | and delved | into |             |       |         |      |        |     |        |             |
various features to establish a novel DRAM failure prediction ProductionDataCenters,"202241stInternationalSymposiumonReliable
|           |                 |     |                             |     |     |     |     | Distributed | Systems | (SRDS), | Vienna, | Austria, | 2022, | pp. 262-272, | doi: |
| --------- | --------------- | --- | --------------------------- | --- | --- | --- | --- | ----------- | ------- | ------- | ------- | -------- | ----- | ------------ | ---- |
| method.We | reconstructedCE |     | informationintofeaturemaps, |     |     |     | and |             |         |         |         |          |       |              |      |
10.1109/SRDS55811.2022.00032.
proposeda3DCWT-PCAtransformationforrenderingthem.The
[12]J.Bogatinovski,O.Kao,Q.YuandJ.Cardoso,"FirstCEMatters:On
| extracted | artificial | and | deep features |     | were fused | and | selected. |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
theImportanceofLongTermPropertiesonMemoryFailurePrediction,"
| Finally, | a hybrid | learning | approach |     | using | ResNet and | KAN |     |     |     |     |     |     |     |     |
| -------- | -------- | -------- | -------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2022IEEEInternationalConferenceonBigData(BigData),Osaka,Japan,
networks was employed for DRAM failure prediction. Feature 2022,pp.4733-4736,doi:10.1109/BigData55660.2022.10020671.
selection and visualization techniques were used to uncover [13]I.Boixaderas,D.Zivanovic,S.Moré,J.Bartolome,D.VicenteandM.
important CE spatial features and patterns. The proposed method Casas, "Cost-Aware Prediction of Uncorrected DRAM Errors in the
Field,"SC20:InternationalConferenceforHighPerformanceComputing,
| achieved | good | results | on the | public | Large-scale | Dataset, | and |     |     |     |     |     |     |     |     |
| -------- | ---- | ------- | ------ | ------ | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Networking,StorageandAnalysis,Atlanta,GA,USA,2020,pp.1-15,doi:
demonstratedstronggeneralizationonreal-worldcloudcenterdata.
10.1109/SC41405.2020.00065.
| These contributions |     | would | provide | valuable |     | insights for | AIOps |             |     |           |         |           |            |     |         |
| ------------------- | --- | ----- | ------- | -------- | --- | ------------ | ----- | ----------- | --- | --------- | ------- | --------- | ---------- | --- | ------- |
|                     |     |       |         |          |     |              |       | [14] Q. Yu, | W.  | Zhang, P. | Notaro, | S. Haeri, | J. Cardoso | and | O. Kao, |
tasksincloudcenters.
|     |     |     |     |     |     |     |     | "HiMFP: | Hierarchical  | Intelligent | Memory |        | Failure Prediction |     | for Cloud     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ----------- | ------ | ------ | ------------------ | --- | ------------- |
|     |     |     |     |     |     |     |     | Service | Reliability," | 2023        | 53rd   | Annual | IEEE/IFIP          |     | International |
ConferenceonDependableSystemsandNetworks(DSN),Porto,Portugal,
| REFERENCES          |     |                                         |     |     |     |     |     | 2023,pp.216-228,doi:10.1109/DSN58367.2023.00031. |        |          |           |     |          |        |       |
| ------------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------------------ | ------ | -------- | --------- | --- | -------- | ------ | ----- |
|                     |     |                                         |     |     |     |     |     | [15] F. Yu,                                      | H. Xu, | S. Jian, | C. Huang, | Y.  | Wang and | Z. Wu, | "DRAM |
| [1]B.SchroederandG. |     | A.Gibson,"ALarge-ScaleStudyofFailuresin |     |     |     |     |     |                                                  |        |          |           |     |          |        |       |
FailurePredictioninLarge-ScaleDataCenters,"2021IEEEInternational
| High-Performance |     | Computing | Systems," |     | in IEEE | Transactions | on  |            |          |       |           |        |         |        |          |
| ---------------- | --- | --------- | --------- | --- | ------- | ------------ | --- | ---------- | -------- | ----- | --------- | ------ | ------- | ------ | -------- |
|                  |     |           |           |     |         |              |     | Conference | on Joint | Cloud | Computing | (JCC), | Oxford, | United | Kingdom, |
DependableandSecureComputing,vol.7,no.4,pp.337-350,Oct.-Dec.
2021,pp.1-8,doi:10.1109/JCC53141.2021.00012.
2010,doi:10.1109/TDSC.2009.4.
|     |     |     |     |     |     |     |     | [16] J. Jung | and | M. Erez, | "Predicting | Future-System |     | Reliability | with a |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ----------- | ------------- | --- | ----------- | ------ |
[2]J.HunKwon,H.KonBae,Y.SeoLee,Y.H.GongandS.WooChung,
|           |               |     |             |                   |          |                    |        | Component-Level |           | DRAM | Fault             | Model," | 2023     | 56th     | IEEE/ACM |
| --------- | ------------- | --- | ----------- | ----------------- | -------- | ------------------ | ------ | --------------- | --------- | ---- | ----------------- | ------- | -------- | -------- | -------- |
| "ZEC ECC: | A Zero-Byte   |     | Eliminating | Compression-Based |          | ECC                | Scheme |                 |           |      |                   |         |          |          |          |
|           |               |     |             |                   |          |                    |        | International   | Symposium | on   | Microarchitecture |         | (MICRO), | Toronto, | ON,      |
| for DRAM  | Reliability," | in  | IEEE        | Access,           | vol. 12, | pp. 100366-100376, |        |                 |           |      |                   |         |          |          |          |
Canada,2023,pp.944-956.
2024,doi:10.1109/ACCESS.2024.3431209.
|            |           |     |         |          |         |                   |     | [17] C. Li, | Y. Zhang, | J. Wang, | H.  | Chen, | X. Liu and | T. Huang, | "From |
| ---------- | --------- | --- | ------- | -------- | ------- | ----------------- | --- | ----------- | --------- | -------- | --- | ----- | ---------- | --------- | ----- |
| [3] W. Li, | M. Zhang, | T.  | Gui, Z. | Fang, C. | Xie and | F. Wu, "Improving |     |             |           |          |     |       |            |           |       |
CorrectableMemoryErrorstoUncorrectableMemoryErrors:WhatError
DRAMReliabilityUsingaHighOrderErrorCorrectionCode,"inIEEE
|              |     |                |     |        |               |          |     | Bits Tell," | SC22: | International |     | Conference | for | High | Performance |
| ------------ | --- | -------------- | --- | ------ | ------------- | -------- | --- | ----------- | ----- | ------------- | --- | ---------- | --- | ---- | ----------- |
| Transactions | on  | Computer-Aided |     | Design | of Integrated | Circuits | and |             |       |               |     |            |     |      |             |
Computing,Networking,StorageandAnalysis,Dallas,TX,USA,2022,pp.
| Systems, | vol. | 43, no. | 12, pp. | 4775-4785, |     | Dec. 2024, | doi: |     |     |     |     |     |     |     |     |
| -------- | ---- | ------- | ------- | ---------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
01-14,doi:10.1109/SC41404.2022.00081.
10.1109/TCAD.2024.3400677.
[18]Q.Yu,W.Zhang,J.CardosoandO.Kao,“ExploringErrorBitsfor
|     |     |     |     |     |     |     |     | Memory | Failure | Prediction: | An  | In-Depth | Correlative | Study,” | 2023 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----------- | --- | -------- | ----------- | ------- | ---- |
305

IEEE/ACM International Conference on Computer Aided Design [21]Z.Liu,Y.Wang,S.Vaidya,F.Ruehle,J.Halverson,M.Soljačić,T.
(ICCAD), San Francisco, CA, USA, 2023, pp. 01-09, doi: Y.Hou,M.Tegmark"Kan:Kolmogorov-arnoldnetworks,"arXivpreprint,
10.1109/ICCAD57390.2023.10323692. 2024arXiv:2404.19756.
[19] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for [22]E.Freeman,G.MoisenandT.Frescino,"Evaluatingeffectivenessof
image recognition," Proceedings of the IEEE conference on computer down-sampling for stratified designs and unbalanced prevalence in
visionandpatternrecognition(CVPR),2016,pp.770-778. RandomForestmodelsoftreespeciesdistributionsinNevada,"Ecological
[20]Z.Li,"Extractingspatialeffectsfrommachinelearningmodelusing modelling,2012,233:1-10.
local interpretation method: An example of SHAP and XGBoost,"
Computers,EnvironmentandUrbanSystems,2022,96:101845.
306