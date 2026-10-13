ISSN 0361-7688, Programming and Computer Software, 2023, Vol. 49, No. 8, pp. 796–821. © Pleiades Publishing, Ltd., 2023.
A Tertiary Study on Microservices:
Research Trends and Recommendations
Z. Stojanova,* (ORCID: 0000-0001-6930-5337), I. Hristoskib,** (ORCID: 0000-0002-9291-7873),
J. Stojanova,*** (ORCID: 0000-0002-2237-8026), and A. Stojkova,**** (ORCID: 0000-0002-1078-7068)
aUniversity of Novi Sad, Technical Faculty “Mihajlo Pupin” Zrenjanin,
Zrenjanin, Serbia
bUniversity “St. Kliment Ohridski”–Bitola, Faculty of Economics–Prilep,
Prilep, North Macedonia
*e-mail: zeljko.stojanov@uns.ac.rs
**e-mail: ilija.hristoski@uklo.edu.mk
***e-mail: jelena.stojanov@uns.ac.rs
****e-mail: aleksandra.stojkov@tfzr.rs
Received June 14, 2023; revised July 12, 2023; accepted August 2, 2023
Abstract—The development and adoption of microservices, as one of the most promising directions for devel-
oping heterogeneous distributed software systems, have been driven by dynamic changes in business and
technology. In addition to the development of new applications, a significant aspect of microservices is the
migration from legacy monolithic systems to microservice architectures. Such development trends are
accompanied by an increase in the number of primary and secondary publications addressing microservices,
highlighting the need to systematize research at a higher level. The objective of this study is to comprehen-
sively analyze secondary studies in the field of microservices from the following five aspects: (1) publishing
trends, (2) quality trends of secondary studies, (3) research trends, (4) domains of implementation, and
(5)future research directions. The study follows the guidelines for conducting a systematic literature review.
Thefindings were derived from 44 secondary studies published in the period from January 2016 to January 2023.
These studies were organized and analyzed to address the five proposed research questions pertaining to the
study objectives. The findings suggest that the most promising research directions are related to the develop-
ment, implementation, and validation of new approaches, methods, and tools that encompass all the phases
of the life cycle. Additionally, these research directions have applications in a variety of business and human
life domains. Recommendations for further literature reviews relate to improvement of quality assessment of
selected studies, more detailed review of architecture quality attributes, inquiry of human factor issues, and
certain maintenance and operation issues. From the methodological aspect, recommendations relate to using
social science qualitative methods for more detailed analysis of selected studies, and inclusion of gray litera-
ture that will bring the real experience of experts from industry.
Keywords: microservices, tertiary study, systematic literature review
DOI: 10.1134/S0361768823080200
1. INTRODUCTION dIn, and Netflix, and later by other companies [5, 6].
This led to an increasing trend in the use of microser-
Microservices have become immensely popular
vices for developing cloud-based applications.
and widely used architectural model for cloud-based
According to Larrucea et al., the adoption of micros-
applications. They can be considered successors to
service-oriented architectures (SOA) and represent ervices in developing or reengineering software sys-
the new trend in developing distributed software sys- tems requires embracing a new organizational and
tems [1, 2]. These small, independent services offer business culture, with special attention to system
improved performance and support for continuous details and architecture [7]. Additionally, the adoption
delivery [3]. While there is no clearly defined principle of DevOps is crucial for better integration throughout
for breaking up monolithic applications, certain fac- the system life cycle [8]. Furthermore, the develop-
tors should be considered such as the number of ment of new complex and heterogeneous software sys-
objects owned by a service, the level of responsibility, tems based on microservices necessitates the adoption
and the team distribution [4]. Initially, microservices of agile approaches not only in development but also
were adopted by large companies like Amazon, Linke- in deployment, operation, and monitoring [6]. In this
796

A TERTIARY STUDY ON MICROSERVICES 797
context, the utilization of contemporary life cycle nal knowledge, while the processed results can be
approaches based on DevOps and continuous soft- shared and accessed by other microservices [2]. This
ware engineering (Continuous Integration, Continu- structure ensures stability, even when system upgrades
ous Delivery, Continuous Deployment, and Continu- or expansions are necessary. With microservices, cli-
ous Monitoring) becomes necessary for the success ents can be confident that any changes or growth in
and competitiveness of software organizations [9]. their business will be seamlessly integrated into the
Literature reviews, such as systematic literature software, as these applications are designed to support
reviews (SLRs) [10] or systematic mapping studies and facilitate work processes. Microservices have
(SMSs) [11, 12], have recently been embraced by the proven to be superior to monolithic architectures, par-
software engineering research community to system- ticularly in terms of meeting business requirements,
atically analyze evidence on practice. This recognition ensuring systems reliability, enhancing maintainabil-
has led to the emergence of Evidence-Based Software ity, and bolstering infrastructure resilience. Even
Engineering (EBSE) as a concept applicable to both though they require more teams and greater effort, the
researchers and practitioners [13]. In addition to long-term benefits make the investment worthwhile
reviewing academic literature, commonly referred to [15]. Presently, it has become a common practice to
as “white literature,” these reviews also encompass migrate monolithic or legacy systems to service-ori-
“gray literature” sources such as blog posts, white ented architectures [16], particularly microservice
papers, industrial magazines, and videos. Conse- architectures, which significantly improve overall sys-
quently, multivocal literature reviews, which rely on tem performance [17, 18]. As the field of microservices
both white and gray literature, have gained promi- engineering matures, the utilization of specific design
nence [14]. patterns will become commonplace, resulting in more
efficient development practices and better fulfillment
Given the aforementioned context, the objective of
of various architectural quality attributes [19].
this study is twofold: (a) to present the current state-
of-the-art in microservice research and (b) to propose Microservices-based systems consist of numerous
recommendations for further research. Special individual microservices, each performing a specific
emphasis is placed on the quality of the published functionality, with no dependencies among them.
studies and the prevailing trends and research land- Consequently, if one component fails, the entire sys-
scape in microservice implementation. To achieve tem remains unaffected. The principle of Autonomy is
these objectives, a systematic literature review was responsible for this behavior, alongside other key prin-
conducted following the guidelines proposed in [10, ciples, which include [15]: Resilience–ensuring that
13]. The search and selection process yielded 44 sec- the application can continue providing services even if
ondary studies, forming the foundation for drawing a specific microservice encounters failure; Transpar-
research findings. Based on these findings, we discuss ency–exposing the necessary details and providing
implications, validity, and recommendations for fur- documentation for each microservice, enabling other
ther research. services to effectively utilize it and understand its cur-
rent state; Automation–employing tools that enhance
This paper is structured as follows. Section 2 pro-
the efficiency, reliability, and scalability of the micro-
vides background information on microservices and
services’ building and maintenance processes; and
tertiary studies related to microservices. Section 3 out-
Alignment–emphasizing the significance of harmoniz-
lines the research methods employed in the study,
ing different microservices within the system, as well
while Section 4 presents the research findings. In Sec-
as aligning them with the organization’s goals and
tion 5, we delve into the research implications, valid-
needs. By adhering to these key principles, microser-
ity, and recommendations for future reviews. The con-
vices architectures can achieve robustness, flexibility,
cluding section summarizes the key insights and high-
and effective collaboration within the system.
lights avenues for further research.
Microservices offer another advantage through uti-
lization of APIs for communication. This approach
2. BACKGROUND
enhances the flexibility and operability of microser-
In this section, we provide an overview of the fun- vices by employing a universal languages that are inde-
damental concepts of microservices in the first sub- pendent of the programming languages used for cod-
section. The second subsection offers a concise review ing the application. Given the multitude of compo-
of published tertiary studies about microservices. nents in microservice-based systems, the selection of a
communication method becomes crucial. Newman
discusses various communication styles, such as syn-
2.1. Microservices
chronous blocking, asynchronous non-blocking,
Microservices have recently emerged as an request-response, event-driven, and common data,
immensely popular software architecture paradigm. along with their respective advantages and disadvan-
They consist of multiple components that collectively tages [2]. The choice of communication style depends
form the entire system. Each component performs a on the specific requirements of the tasks at hand.
single task, with its boundaries shielding it from exter- However, the most commonly employed communica-
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

798 STOJANOV et al.
User interface
Request Response
Microservice system
API
Microservice DB
Microservice
Microservice Microservice
Microservice
DB DB DB
Fig. 1. Microservices-based system.
tion mechanism is the HTTP protocol, which aligns 2.2. Related Work
with the REST architectural style [20]. This choice
Tertiary studies in software engineering serve the
ensures compatibility and ease of integration within
purpose of reviewing secondary studies and conduct-
microservices architectures.
ing meta-analyses on specific research topics. Recent
tertiary studies have covered a range of subjects
Figure 1 illustrates a typical example of microser-
including DevOps [22], architecting systems of sys-
vice architecture. An integrated microservice system
tems [23], cloud computing [24], agile software devel-
comprises a user interface and a collection of micros-
opment [25], variability in software product lines [26],
ervices (although some microservices may not have a
and testing artifact quality [27].
user interface). The number of microservices can vary
depending on the specific purpose of the system. During the search conducted in December 2022,
Unlike monolithic systems, microservices operate two tertiary studies on microservices were identified.
with individual databases; each service has its dedi- The first study, titled “Research on Microservice
cated database. To interact with the system, users send Architecture: A Tertiary Study” by Liu et al. [28], and
requests through the user interface in a format defined the second study titled “Microservice Architecture:
by the API. The API receives each request and for- ATertiary Study” by Costa et al. [29], both primarily
focus on microservices architecture. However, other
wards it to the corresponding microservice responsible
aspects such as migration to microservices, security
for resolving it. Once the API receives a response from
issues, or implementation in specific sociotechnical
a selected microservice, it relays it back to the user.
contexts are not directly addressed. Table 1 provides
Similarly, APIs serve as the communication channels
comprehensive information on these tertiary studies,
for microservices to interact with one another and
including the period covered and the number of sec-
share data. This enables seamless coordination and
ondary studies included in each review. The review
collaboration among the microservices within the
types encompass systematic literature reviews (SLRs),
architecture.
systematic mapping studies (SMSs), systematic grey
Microservice organizations encompass various literature reviews (SGLRs), and multivocal literature
types, with one of the most prevalent being container- reviews (MVRs).
based architecture [21]. Containers play a vital role in Liu et al. (2022) conducted a systematic literature
physically isolating individual microservices from one review, identifying 37 secondary studies on microser-
another, as microservices operate within distributed vices published between 2016 and 2021 [28]. Liu et al.
systems. By leveraging containers, the requirement for formulated two research questions for their review:
deploying microservices on dedicated machines to (RQ1) What are the common topics addressed in sec-
achieve separation is eliminated. Containers provide the ondary studies related to microservices architecture
necessary isolation between microservices, reducing the (MSA), and what are their findings? (RQ2) What are
reliance on physical machines for deployment [2]. the potential areas for new research in the field of
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 799
Table 1. Tertiary studies on microservices
Study reference Time span SLRs SMSs MVRs SGLRs
Liu et al. (2022) [28] 2016–2021 17 20 0 0
Costa et al. (2020) [29] 2016–2019 5 14 2 1
MSA? To assess the quality of the secondary studies, even multivocal literature reviews that encompass gray
the authors have employed the DARE quality criteria literature [14].
as described in [13]. During the search conducted in digital libraries,
two articles were identified as tertiary studies on
Costa et al. (2020) conducted a systematic litera-
microservices: a study titled “Research on Microser-
ture review, identifying 22 secondary studies on
vice Architecture: A Tertiary Study” by Liu et al. [28],
microservices published from 2016 to 2019 [29]. The
and a study titled “Microservice Architecture: A Ter-
original study was written in Portuguese, necessitating
tiary Study” by Costa et al. [29]. It is worth noting that
the translation of methodological issues and results
[29] is written in Portuguese, while [28] is in English.
into English during the analysis. Costa et al. addressed
the following research questions: (RQ1) Which sec- Insights derived from these two studies revealed a
ondary studies have been published in the field of consistent increase in the number of secondary studies
microservices? (RQ2) What research topics on micro- over the years. This trend is expected to continue in
services have been investigated? (RQ3) What emerging 2023 and beyond, highlighting the need for a new
patterns have been identified? (RQ4) What solutions reviews of recent secondary research. Furthermore,
and support tools have been utilized to facilitate the these two studies did not specifically investigate qual-
development and operation of microservices architec- ity trends in secondary studies, migration-related
ture? (RQ5) In which areas, particularly in the indus- issues, or implementation challenges in various
try, are microservices being applied? (RQ6) Which domains. Therefore, further research opportunities
topics exhibit gaps and require further exploration in exist in these areas. Considering these factors, con-
future microservices research? Costa et al. assessed the ducting a new systematic literature review that incor-
quality of secondary studies using the DARE quality porates the most recent studies and focuses on assess-
criteria as described in [13]. ing the quality of secondary research would greatly
contribute to enhancing the knowledge base within
the field of software engineering.
3. RESEARCH METHOD 3.1.2. Research questions. To enhance comprehen-
sion of the current research landscape in the field of
This study adheres to the guidelines outlined for
microservices, several research questions have been
conducting systematic literature reviews, as proposed
formulated to explore the findings of secondary stud-
in [10, 13]. The research process is structured into
ies, trends in the quality of secondary studies, and
three primary phases: (1) planning the review, (2) con-
challenges that warrant future research. The proposed
ducting the review, and (3) reporting the findings.
research questions (RQs) are as follows.
RQ1. What are the publishing trends observed in
3.1. Planning the Review secondary studies?
RQ2. What is the trajectory of quality trends in sec-
The planning phase includes justifying the need for
ondary studies?
a tertiary study, determining research questions,
RQ3. What are the predominant topics investigated
selecting digital databases, and defining the studies
in secondary studies?
search and selection process with clearly stated key-
words for searching, inclusion/exclusion criteria, and RQ4. In which domains are microservices com-
quality assessment criteria. These issues are discussed monly implemented?
in the following subsections. RQ5. What future research directions have been
identified?
3.1.1. Need to conduct a tertiary study on microser-
vices. Microservices have emerged as a significantly By addressing these research questions, a compre-
popular research field, witnessing a substantial growth hensive understanding can be obtained regarding the
in the number of studies presenting theoretical and publication patterns, quality aspects, research topics,
empirical findings over the past decade. Due to this implementation domains, and future research direc-
development, the consolidation of individual study tions within the realm of microservices.
outcomes has become essential, leading to the execu- 3.1.3. Selection process of secondary studies. We
tion of systematic reviews. These reviews encompass have carefully selected specific keywords to encompass
various approaches, such as systematic literature the concepts of microservices and secondary studies
reviews [10], systematic mapping studies [11], and that can be conducted as systematic literature reviews
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

800 STOJANOV et al.
or systematic mapping studies. To this end, we have All secondary studies identified through the sys-
divided the keywords into two groups: the first group tematic search using search strings or the snowball
includes the keywords “microservices” and “micros- method are evaluated against these inclusion and
ervices architecture,” while the second group com- exclusion criteria. If a secondary study fails to meet
prises the keywords “SLR,” “Systematic literature even one criterion, it is excluded from further analysis.
review,” “SMS,” and “Systematic mapping study.” 3.1.4. Quality assessment of secondary studies. The
Toperform searches in digital databases, we utilized secondary studies were evaluated for quality based on
the following search strings: guidelines proposed in [13]. The primary objectives of
[1]: (“microservices architecture” OR “microser- the quality assessment were as follows: (1) to identify
vices”) AND (“SLR” OR “Systematic literature and exclude low-quality studies from the detailed
review”) analysis and synthesis of review findings and (2) to
[2]: (“microservices architecture” OR “microser- provide insights for addressing RQ2 regarding quality
vices”) AND (“SMS” OR “Systematic mapping trends in secondary studies. A three-point scale was
study”) used for the quality assessment, with values of 1 (Yes),
0.5 (Partly), and 0 (No). This scale was based on the
The process of searching and selecting studies
five questions (Q2–Q6) proposed in [13], along with
involved the following phases (Ph#no.):
an additional question concerning the use of the
(cid:129) Ph#1: Searching digital libraries using search
review methodology (Q1). The questions were as fol-
strings composed of relevant keywords;
lows.
(cid:129) Ph#2: Selecting specific studies based on their
Q1. Is the review methodology clearly stated and
title, abstract, and keywords. This phase also involves
appropriate?
removing duplicates (in case a study appears in multi-
ple databases), and selecting the most recent version
Q2. Are the review’s inclusion and exclusion crite-
ria described and appropriate?
of the study (if there are multiple versions by the same
authors); Q3. Is the literature search likely to have covered all
(cid:129) Ph#3: Employing the snowball method [30] to relevant studies?
search for additional studies and minimize the possi- Q4. Did the reviewers assess the quality/validity of
bility of overlooking or omitting any relevant second- the included studies?
ary studies; Q5. Were basic studies adequately described?
(cid:129) Ph#4: Applying inclusion/exclusion criteria to Q6. Were the extracted data from included studies
the studies selected in the phases Ph#2 and Ph#3; synthesized in the findings?
(cid:129) Ph#5: Conducting a detailed reading and analy- The authors of this paper have agreed that studies
sis of the studies that passed Ph#4, while comparing with an average quality score of less than 0.5 will be
them against defined quality assessment criteria. excluded of the detailed analysis.
The digital libraries used for searching secondary
studies include ACM Digital Library, IEEE Xplore,
ScienceDirect, Springer, Wiley Online Library, and 3.2. Conducting Review
MDPI. These libraries were selected because they The search for secondary studies commenced in
publish a majority of the leading journals and confer- January 2023. The first phase (Ph#1), which involved
ence proceedings in the field. searching selected digital libraries using the provided
The following inclusion and exclusion criteria were search strings, has concluded, resulting in the identifi-
applied to filter the studies obtained from the search of cation of 821 papers that will proceed to subsequent
these digital libraries. review phases. The details of the search conducted in
(cid:129) Inclusion criteria. digital libraries are presented in Table 2.
(cid:2) I1. A study reviews relevant studies on microser- Figure 2 illustrates the phased process of selecting
secondary studies, while Table 3 provides specific
vices.
details regarding the selection of SLRs and SMSs
(cid:2) I2. A study follows guidelines for conducting SLR
throughout the phases.
or SMS.
The fourth filtering phase (Ph#4) involves assess-
(cid:2) I3. A study answers research questions in the
ing studies against the proposed inclusion/exclusion
domain of microservices.
criteria. After evaluating each of the 57 studies, 44
(cid:129) Exclusion criteria. were selected for further analysis and quality assess-
(cid:2) E1. Full text of a study is not available. ment. Three studies were excluded based on the E3
(cid:2) E2. A study is not peer-reviewed. exclusion criterion, one study based on the E1 exclu-
sion criterion, and nine studies based on the E5 exclu-
(cid:2) E3. The study is less than 6 pages.
sion criterion.
(cid:2) E4. A study is not written in English.
3.2.1. Quality assessment. The quality assessment
(cid:2) E5. A review study that includes gray literature. of studies that met the inclusion/exclusion criteria was
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 801
Table 2. Total number of papers obtained through search in digital libraries
Library Number of search results for [1]Number of search results for [2] Totally for [1, 2]
| ACM Digital Library  |     |     | 68  | 90  | 158 |
| -------------------- | --- | --- | --- | --- | --- |
| IEEE Xplore          |     |     | 13  | 14  | 27  |
| ScienceDirect        |     |     | 127 | 85  | 212 |
| Springer             |     |     | 144 | 183 | 327 |
| Wiley Online Library |     |     | 31  | 58  | 89  |
| MDPI                 |     |     | 5   | 3   | 8   |
| Total                |     |     | 388 | 433 | 821 |
conducted  by  the  first,  third,  and  fourth  authors, Based on the quality assessment results, the mini-
mum score achieved was 0.53 (for study SS42), while
while the second author reviewed the grades and cal-
the average quality score across all studies was 0.81.
culated the average quality scores for all studies. Table 4
presents the average scores for the quality assessment After completing all phases of filtering the second-
ary studies, a total of 44 studies were selected for in-
| of  the  selected  | studies,  | indicating  | that  all  studies |     |     |
| ------------------ | --------- | ----------- | ------------------ | --- | --- |
exceeded the minimum required quality threshold for depth analysis. The selected secondary studies (SSs)
are listed in Appendix A.
| further  analysis  | (overall  | quality  score  | greater  than |     |     |
| ------------------ | --------- | --------------- | ------------- | --- | --- |
3.2.2. Data extraction and analysis. The data from
0.50). Each evaluator assigned a mark from the three-
the selected secondary studies were extracted using the
point scale (0.0, 0.5, or 1.0) to each study based on the
template provided in Table 5. The selection of data to
quality assessment criteria. The average quality score
extract was guided by the research questions, encom-
for each study was then calculated as the mean of all passing general information about each study’s publi-
average values assigned by each evaluator. cation  and  specific  data  relevant  to  each  research
44 secondary
studies
821 papers
57 secondary
Phase #2
studies
|     |     | Selection based  |     | Phase #4 |     |
| --- | --- | ---------------- | --- | -------- | --- |
Phase #1
on screening
|     |     | title, abstract, |     |     | Phase #5 |
| --- | --- | ---------------- | --- | --- | -------- |
keywords, and  Merging
Implementing
| Search by using  |     | introduction  |     |                      |                    |
| ---------------- | --- | ------------- | --- | -------------------- | ------------------ |
| search strings   |     |               |     | inclusion/exclusion  |                    |
|                  |     | section       |     |                      | Quality assessment |
criteria
Removing
duplicates
Digital databases
Handling
Phase #3
multiple
ACM
versions of a
|     |     | study |     | 44 secondary   | 21 SLRs  |
| --- | --- | ----- | --- | -------------- | -------- |
|     |     |       |     | studies        | 23 SMSs  |
IEEE Snowball
44 secondary
ScienceDirect
studies (SSs)
Springer
13 secondary
Wiley studies
MDPI
Fig. 2. The phased process of selecting secondary studies.
| PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 49   No. 8  |  2023 |     |
| ---------------------------------- | --- | --- | ----------------- | ----- | --- |

802 STOJANOV et al.
Table 3. Details of the phased process for selecting secondary studies
SLRs SMSs MVRs Totally SSs
[Ph#1] Selected studies after checking titles, abstracts, and keywords 19 23 14 56
[Ph#2] Selected studies after removing duplicates 16 19 9 44
[Ph#3] Snowball search for additional studies 6 7 0 13
Merging digital libraries and snowball search results 22 26 9 57
[Ph#4] Selected studies after implementing inclusion/exclusion criteria 21 23 0 44
[Ph#5] A final set of secondary studies after quality assessment 21 23 0 44
question. The extracted data was organized in an Excel venue. It is obvious that the total number of studies has
spreadsheet, with each column dedicated to a specific consistently grown over the years, and there has been
category of extracted information. a notable shift from primarily conference proceedings
The research findings were then synthesized using to journals. Out of the 44 studies, 22 were published in
the extracted data, with the primary objective of pro- conference proceedings, and another 22 were pub-
viding comprehensive answers to the stated research lished in journals. Although one study published in
questions. January 2023 does not align with this trend, it will still
be utilized to address other research questions.
4. RESEARCH FINDINGS
4.2. Quality Trends of Secondary Studies (RQ2)
As mentioned earlier in the preceding section, the
findings presented here are derived from the data Table 4 presents a detailed analysis of the quality
extracted from 44 secondary studies that successfully assessment conducted on the secondary studies,
passed all phases of the selection process. Among revealing the following findings.
these studies, 23 of them are SMSs, while the remain-
(1) The average quality score for all the selected
ing 21 are SLRs (refer to Table 3). The findings will be
secondary studies is 0.81. This indicates that the
organized and presented in alignment with the
authors of these studies have dedicated significant
research questions outlined in this study.
attention to assessing the quality of the studies they
analyzed.
4.1. Publishing Trends for Secondary Studies (RQ1)
(2) When comparing SLRs to SMSs, the average
The selected secondary studies span the publica- quality score for SLRs is 0.84, while the average qual-
tion period from 2016 to 2023. Figure 3 showcases the ity score for SMSs is 0.77. This difference in scores is
publication trends of secondary studies based on the primarily attributed to the low score for Q4 in SMSs.
Number of studies
9
8
7
6
5
4
3
2
1
0
2016 2017 2018 2019 2020 2021 2022 2023
Years
Conference paper Journal paper
Fig. 3. Secondary studies publication trends by venue.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

|     |     |     | A TERTIARY STUDY ON MICROSERVICES |     |     |     |     | 803 |
| --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
Table 4. Average scores for quality assessment of the selected secondary studies
| ID   | Year | Type | Q1   | Q2 Q3     | Q4   | Q5   | Q6   | AVG  |
| ---- | ---- | ---- | ---- | --------- | ---- | ---- | ---- | ---- |
| SS01 | 2020 | SLR  | 0.67 | 0.67 0.83 | 0.33 | 0.83 | 0.83 | 0.69 |
| SS02 | 2019 | SLR  | 1.00 | 1.00 1.00 | 0.83 | 1.00 | 1.00 | 0.97 |
| SS03 | 2019 | SLR  | 0.83 | 1.00 1.00 | 0.83 | 0.83 | 0.83 | 0.89 |
| SS04 | 2020 | SLR  | 0.67 | 1.00 1.00 | 0.33 | 0.83 | 0.67 | 0.75 |
| SS05 | 2018 | SLR  | 0.50 | 0.50 0.67 | 0.33 | 0.83 | 0.83 | 0.61 |
| SS06 | 2021 | SLR  | 1.00 | 1.00 1.00 | 1.00 | 0.83 | 1.00 | 0.97 |
| SS07 | 2021 | SLR  | 1.00 | 1.00 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| SS08 | 2018 | SLR  | 0.50 | 0.67 0.67 | 0.50 | 1.00 | 1.00 | 0.72 |
| SS09 | 2019 | SLR  | 0.50 | 0.50 0.83 | 0.67 | 0.83 | 0.83 | 0.69 |
| SS10 | 2020 | SLR  | 1.00 | 1.00 1.00 | 0.33 | 1.00 | 1.00 | 0.89 |
| SS11 | 2022 | SLR  | 1.00 | 1.00 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| SS12 | 2022 | SLR  | 0.50 | 0.33 1.00 | 0.17 | 0.83 | 0.83 | 0.61 |
| SS13 | 2022 | SLR  | 1.00 | 1.00 0.83 | 0.00 | 0.83 | 0.83 | 0.75 |
| SS14 | 2022 | SLR  | 1.00 | 1.00 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| SS15 | 2022 | SLR  | 1.00 | 1.00 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| SS16 | 2022 | SLR  | 0.83 | 1.00 1.00 | 0.83 | 1.00 | 1.00 | 0.94 |
| SS17 | 2021 | SLR  | 1.00 | 1.00 0.83 | 0.83 | 1.00 | 1.00 | 0.94 |
| SS18 | 2021 | SLR  | 0.67 | 1.00 1.00 | 0.50 | 1.00 | 1.00 | 0.86 |
| SS19 | 2018 | SLR  | 1.00 | 1.00 0.67 | 0.83 | 1.00 | 0.83 | 0.89 |
| SS20 | 2021 | SLR  | 0.67 | 1.00 0.83 | 0.33 | 1.00 | 0.83 | 0.78 |
| SS21 | 2021 | SLR  | 0.67 | 1.00 1.00 | 0.00 | 0.83 | 0.83 | 0.72 |
| SS22 | 2022 | SMS  | 1.00 | 1.00 0.83 | 0.00 | 1.00 | 0.83 | 0.78 |
| SS23 | 2017 | SMS  | 1.00 | 0.83 1.00 | 0.00 | 0.67 | 0.83 | 0.72 |
| SS24 | 2021 | SMS  | 0.83 | 1.00 1.00 | 0.00 | 1.00 | 1.00 | 0.81 |
| SS25 | 2020 | SMS  | 1.00 | 1.00 1.00 | 0.00 | 0.67 | 1.00 | 0.78 |
| SS26 | 2021 | SMS  | 1.00 | 1.00 0.83 | 0.00 | 0.67 | 0.83 | 0.72 |
| SS27 | 2017 | SMS  | 1.00 | 1.00 1.00 | 0.00 | 0.67 | 1.00 | 0.78 |
| SS28 | 2019 | SMS  | 1.00 | 1.00 1.00 | 0.67 | 1.00 | 0.83 | 0.92 |
| SS29 | 2016 | SMS  | 1.00 | 1.00 0.83 | 0.17 | 1.00 | 1.00 | 0.83 |
| SS30 | 2022 | SMS  | 1.00 | 1.00 1.00 | 0.00 | 1.00 | 0.83 | 0.81 |
| SS31 | 2022 | SMS  | 0.83 | 0.83 1.00 | 0.75 | 0.50 | 0.83 | 0.79 |
| SS32 | 2021 | SMS  | 0.83 | 1.00 1.00 | 0.00 | 1.00 | 0.67 | 0.75 |
| SS33 | 2020 | SMS  | 1.00 | 0.83 1.00 | 0.33 | 1.00 | 1.00 | 0.86 |
| SS34 | 2019 | SMS  | 1.00 | 1.00 1.00 | 0.00 | 1.00 | 1.00 | 0.83 |
| SS35 | 2021 | SMS  | 1.00 | 1.00 1.00 | 1.00 | 1.00 | 0.83 | 0.97 |
| SS36 | 2017 | SMS  | 0.50 | 0.50 0.83 | 0.00 | 0.67 | 0.83 | 0.56 |
| SS37 | 2019 | SMS  | 1.00 | 1.00 1.00 | 0.00 | 0.83 | 0.83 | 0.78 |
| SS38 | 2022 | SMS  | 1.00 | 0.83 1.00 | 0.00 | 1.00 | 0.67 | 0.75 |
| SS39 | 2021 | SMS  | 0.83 | 1.00 1.00 | 0.00 | 1.00 | 1.00 | 0.81 |
| SS40 | 2019 | SMS  | 0.83 | 1.00 1.00 | 0.00 | 1.00 | 1.00 | 0.81 |
| SS41 | 2019 | SMS  | 0.83 | 1.00 1.00 | 0.00 | 0.17 | 1.00 | 0.67 |
| SS42 | 2019 | SMS  | 0.50 | 0.33 0.83 | 0.33 | 0.50 | 0.67 | 0.53 |
| SS43 | 2016 | SMS  | 1.00 | 1.00 1.00 | 0.17 | 1.00 | 1.00 | 0.86 |
| SS44 | 2023 | SMS  | 1.00 | 1.00 1.00 | 0.00 | 0.33 | 1.00 | 0.72 |
Average scores for all SSs 0.86 0.91 0.94 0.37 0.87 0.90 0.81
| Average scores SLRs                |     |     | 0.81 | 0.89 0.91         | 0.60  | 0.93 | 0.91 | 0.84 |
| ---------------------------------- | --- | --- | ---- | ----------------- | ----- | ---- | ---- | ---- |
| Average scores SMSs                |     |     | 0.91 | 0.92 0.96         | 0.15  | 0.81 | 0.89 | 0.77 |
| PROGRAMMING AND COMPUTER SOFTWARE  |     |     |      |  Vol. 49   No. 8  |  2023 |      |      |      |

| 804 |     |     | STOJANOV et al. |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
Table 5. Data extraction template
| ID                                                |     | Explanation |     |                 |     | Use |     |     |
| ------------------------------------------------- | --- | ----------- | --- | --------------- | --- | --- | --- | --- |
| D1 Study ID                                       |     |             |     | Demography, RQ1 |     |     |     |     |
| D2 Title                                          |     |             |     | Demography, RQ1 |     |     |     |     |
| D3 Year                                           |     |             |     | Demography, RQ1 |     |     |     |     |
| D4 Study type (SLR, SMS)                          |     |             |     | Demography, RQ1 |     |     |     |     |
| D5 Venue type (conference, journal, book chapter) |     |             |     | Demography, RQ1 |     |     |     |     |
| D6 Sample size (number of primary studies)        |     |             |     | Demography, RQ1 |     |     |     |     |
D7 Used research methodology description Quality assessment Q1, RQ2
| D8 Inclusion/Exclusion criteria  |     |     |     | Quality assessment Q2, RQ2 |     |     |     |     |
| -------------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |
| D9 Coverage of relevant studies  |     |     |     | Quality assessment Q3, RQ2 |     |     |     |     |
| D10 Quality assessment questions |     |     |     | Quality assessment Q4, RQ2 |     |     |     |     |
D11 Method for describing selected studies Quality assessment Q5, RQ2
D12 Data extraction methods and tools Quality assessment Q6, RQ2
| D13 Research questions             |     |     |     | Research topics, RQ3  |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
| D14 Research topics                |     |     |     | Research topics, RQ3  |     |     |     |     |
| D15 Technical implementation areas |     |     |     | Application area, RQ4 |     |     |     |     |
D16 Future research directions Future research direction, RQ5
This distinction is influenced by the general guidelines each  study,  with  particular  attention  given  to  the
for conducting systematic literature reviews, where research  questions  and  presented  findings.  The
quality assessment is mandatory for SLRs, while it extracted data correspond to values in columns D13
remains optional for SMSs. (research  questions)  and  D14  (research  topics)  in
Table 5. A general overview of the topics investigated
(3) The quality assessment scores for each question
are presented in Table 4, revealing that there is one in the secondary studies is depicted in Fig. 4.
concerning score of 0.37 specifically related to ques-
During the detailed analysis of the selected studies,
tion Q4, which pertains to the assessment of the qual- 21  challenges  were  identified,  with  many  of  them
ity of included studies. Notably, SMSs received an appearing across multiple studies that focused on dif-
even lower score of 0.15 for this question. This suggests ferent topics. Subsection 4.3.5 will provide a more in-
that the authors of the secondary studies did not pay
depth discussion of these challenges.
enough attention to evaluating the quality of the pri-
It is worth noting that while most studies have a
mary studies they included, which could potentially
primary focus on a specific topic, they also touch upon
impact the reliability of their findings.
other related topics. For instance, it is common for a
(4) The average scores for questions Q1 (use of
study to discuss architecture design patterns while also
review methodology), Q2 (use of inclusion/exclusion
addressing quality attributes and specific challenges
| criteria),  Q3  | (relevance  | of  included  | studies),  Q5 |     |     |     |     |     |
| --------------- | ----------- | ------------- | ------------- | --- | --- | --- | --- | --- |
(e.g., SS27 [Research on architecting microservices:
(description of included studies), and Q6 (synthesis of Trends, focus, and potential for industrial adoption]).
findings) range from 0.86 to 0.94. These results indi-
A comprehensive analysis of all the identified gen-
cate that these aspects of quality assessment in the sec-
ondary studies have been addressed effectively. eral topics will be presented in the subsequent subsec-
tions.
Table 6 illustrates the average quality assessment
scores for all the quality questions (Q1–Q6) concern- 4.3.1. Architecture. Architectural design plays a
ing different publishing venues. Notably, studies pub- vital role in the development of microservice-based
software systems as it encompasses both the technical
lished in journals exhibit higher score values across all
the  questions,  suggesting  that  the  authors  have design of system functionalities and the consideration
demonstrated greater diligence in assessing the quality
of the primary studies due to the more rigorous peer
Table 6. Average quality assessment scores regarding publi-
review process associated with journal publications.
cation venue
|     |     |     |     |     | Q1 Q2 | Q3 Q4 | Q5 Q6 | AVG |
| --- | --- | --- | --- | --- | ----- | ----- | ----- | --- |
4.3. Topics Inquired in Secondary Studies (RQ3)
|     |     |     |     | Conferences | 0.83 0.89 | 0.91 0.29 | 0.83 0.88 | 0.77 |
| --- | --- | --- | --- | ----------- | --------- | --------- | --------- | ---- |
The identification of topic areas in the selected sec-
ondary studies is based on a thorough examination of Journals 0.90 0.92 0.97 0.44 0.91 0.92 0.84
|     |     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 49  |  No. 8  |  2023 |
| --- | --- | --- | ---------------------------------- | --- | --- | --------- | ------- | ----- |

A TERTIARY STUDY ON MICROSERVICES 805
Monitoring and tracing Testing and quality assurance
Deployment
Communication
Performance
Challenges Service discovery
Security
Data management
Organizational issues
Other . . .
Human factor
Microservices
Design
Analysis
Implementation
Granularity
Life cycle scope
Testing
Architecture
Patterns
Migration
Deployment
Presentation
Maintenance and
operation Quality attributes
Runtime Process/roadmap Approach Challenges
Fig. 4. General overview of microservices research topics.
of non-functional requirements, often referred to as Granularity. Granularity refers to the size of indi-
quality attributes. Additionally, the architecture vidual microservices within a software system based
should be analyzed and presented in a manner that on the microservices architecture. It plays a crucial
facilitates efficient development, operation, and main- role in determining the functioning of the system and
tenance of software systems. The main topics related to its quality attributes, including performance, main-
microservices architecture in the selected secondary tainability, data storage, and scalability. The granular-
studies include analysis, granularity, patterns, presen- ity of microservices has a direct impact on how well
tation, and quality attributes (refer to Fig. 4). the system performs and how effectively it can be
maintained and scaled to meet changing demands.
A more comprehensive examination of architec- Consideration of granularity is essential when devel-
ture topics, including identified subtopics and the dis- oping a new system or migrating legacy systems to a
tribution of secondary studies that mention them, is microservices architecture [SS09][SS24]. Determin-
provided in Table 7. ing the optimal granularity involves finding the right
balance between the level of functionality encapsu-
Analysis. The analysis of software architecture is
lated within each microservice and the need for mod-
crucial for understanding both new software systems
ularity, maintainability, and scalability. By carefully
and those that require migration to microservice
assessing the purpose and requirements of the system,
architectures. It focuses on the following aspects: (1)
developers can determine the appropriate size and
Methods [SS09][SS27][SS35][SS39][SS44]: Various
scope of each microservice to achieve the desired
methods can be distinguished, including static analy-
architectural goals. Insights from the selected studies
sis, dynamic analysis, combined dynamic and static on granularity reveal the following main subtopics: (1)
analysis, model-based analysis, graph-based analysis, Methods or approaches for defining granularity
and pattern-based analysis; (2) Tools [SS30][SS39]: [SS04][SS09][SS17][SS24]; (2) Metrics used for evalu-
Specific tools tailored to each analysis method, which ating granularity [SS17]; and (3) Quality attributes
facilitate more efficient and automated work; and (3) affected by granularity [SS17]. In a detailed inquiry
Challenges [SS30][SS39]: These encompass architec- presented in [SS17], various approaches are used to
tural analysis, migration to microservices, software define the granularity of microservices. These include
architecture reconstruction, technical debt analysis, the trial and error approach, the approach based on
microservice evolution, quality attribute analysis, and the number of lines of code, the approach related to
fault analysis. By considering these aspects, a compre- implementation units, the approach related to busi-
hensive understanding of software architectures, espe- ness capabilities, and the approach using domain-
cially in the context of microservices, can be achieved. driven design. Additionally, findings from [SS09] clas-
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

806 STOJANOV et al.
Table 7. Topics and subtopics related to a microservices architecture
| Topic       |                    | Subtopic |                              | Secondary studies |     |     |
| ----------- | ------------------ | -------- | ---------------------------- | ----------------- | --- | --- |
| Analysis    | Methods            |          | SS09, SS27, SS35, SS39, SS44 |                   |     |     |
|             | Tools              |          | SS30, SS39                   |                   |     |     |
|             | Challenges         |          | SS30, SS39                   |                   |     |     |
| Granularity | Approach           |          | SS04, SS09, SS17, SS24       |                   |     |     |
|             | Quality attributes |          | SS17                         |                   |     |     |
|             | Metrics            |          | SS17                         |                   |     |     |
Patterns Design SS03, SS05, SS19, SS27,SS33, SS34, SS37, SS43
|              | Composition   |     | SS02, SS09, SS19, SS33, SS43       |     |     |     |
| ------------ | ------------- | --- | ---------------------------------- | --- | --- | --- |
|              | Communication |     | SS03, SS05, SS06, SS19, SS33, SS37 |     |     |     |
|              | Deployment    |     | SS03, SS06, SS37, SS19, SS33, SS37 |     |     |     |
|              | Data storage  |     | SS03, SS19, SS33, SS37             |     |     |     |
|              | Antipattern   |     | SS01, SS44                         |     |     |     |
| Presentation | Languages     |     | SS22, SS27, SS29, SS33             |     |     |     |
|              | Diagrams      |     | SS27, SS29                         |     |     |     |
|              | Visualization |     | SS30                               |     |     |     |
Quality attributes Reliability SS03, SS08, SS17, SS27, SS33, SS34
|     | Security        |     | SS03, SS07, SS08, SS17, SS27, SS29, SS33, SS40   |     |     |     |
| --- | --------------- | --- | ------------------------------------------------ | --- | --- | --- |
|     | Compatibility   |     | SS03, SS27, SS33, SS34, SS40                     |     |     |     |
|     | Maintainability |     | SS03, SS08, SS17, SS27, SS29, SS33, SS34         |     |     |     |
|     | Performance     |     | SS03, SS07, SS17, SS19, SS27, SS29, SS33, SS34,  |     |     |     |
SS40
|     | Portability    |     | SS03, SS27, SS33, SS34                           |     |     |     |
| --- | -------------- | --- | ------------------------------------------------ | --- | --- | --- |
|     | Testability    |     | SS07, SS33                                       |     |     |     |
|     | Availability   |     | SS07, SS08, SS17, SS33                           |     |     |     |
|     | Monitorability |     | SS07, SS33                                       |     |     |     |
|     | Scalability    |     | SS07, SS08, SS17, SS19, SS27, SS29, SS33, SS34,  |     |     |     |
SS40
|     | Modularity |     | SS17, SS29       |     |     |     |
| --- | ---------- | --- | ---------------- | --- | --- | --- |
|     | Other…     |     | SS29, SS33, SS40 |     |     |     |
sify approaches for determining granularity as static commonly referred to as patterns. Incorporating pat-
code analysis aided, meta-data aided, workload-data terns into the software life cycle enables developers to
aided,  and  dynamic  microservice  composition,  all find reliable solutions to common problems, enhances
considering different levels of granularity within soft- communication among team members and with cli-
ware systems. Common metrics used for measuring
ents, and aids in meeting quality requirements. The
granularity encompass coupling, cohesion, complex- analysis of the secondary studies reveals that a signifi-
ity, performance, quality attributes, use of computa- cant portion of them directly or indirectly explore pat-
tional resources, development team, and source code.
terns associated with different facets of microservices
Regarding quality attributes, granularity has an impact
|     |     |     | architecture.  | Additionally,  | some  studies  | delve  into |
| --- | --- | --- | -------------- | -------------- | -------------- | ----------- |
on runtime attributes such as scalability, performance,
adapting patterns in other domains, such as DevOps or
reliability, availability, and functionality, as well as
their application in IoT-based smart systems. The sec-
attributes related to software as an artifact, such as
ondary studies identify the following categories of pat-
maintainability, modularity, and reusability.
|     |     |     | terns:  (1)  | Design  [SS03][SS05][SS19][SS27][SS33] |     |     |
| --- | --- | --- | ------------ | -------------------------------------- | --- | --- |
Patterns. The identification and categorization of [SS34][SS37][SS43]–patterns  used  for  structuring
specific challenges and their corresponding solutions and organizing microservices efficiently. Commonly
used patterns include API gateway, publish/subscribe,
during software development, operation, and mainte-
nance contribute to the recognition of recurring sce- circuit breaker, proxy, and load balancer [SS27]); (2)
narios that can be addressed with specific solutions, Composition  [SS02][SS09][SS19][SS33][SS43]–pat-
|     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 49   No. 8  |  2023 |
| --- | --- | ---------------------------------- | --- | --- | ----------------- | ----- |

A TERTIARY STUDY ON MICROSERVICES 807
terns related to composing different microservices in a Quality attributes. Quality characteristics of soft-
software system. Commonly used patterns include ware systems are typically reflected in the form of
semantic annotation [SS02], best-fitting, and work- quality attributes, which are associated with non-
load-based approaches [SS09]); (3) Communication functional requirements. While there are numerous
[SS03][SS05][SS06][SS19][SS33][SS37]–patterns related quality attributes, it is often challenging to satisfy all of
to communication between multiple microservices. them simultaneously for a specific system. In such
Commonly used patterns include synchronous com- cases, trade-offs must be made when considering
munication, publish/subscribe communication, com- quality attributes. Table 7 presents the most common
bination of HTTP and message queue, communica- quality attributes mentioned in many studies, includ-
tion using message-oriented middleware, asynchro- ing Reliability, Security, Compatibility, Maintainability,
nous communication, point-to-point Performance, Portability, Testability, Availability, Mon-
communication, and communication using binary itorability, Scalability, and Modularity. These attri-
protocols [SS06]); (4) Deployment butes have been extensively discussed in various
[SS03][SS06][SS37][SS19] [SS33][SS37]–patterns sources and are relevant throughout the software life
related to the deployment or distribution of microser- cycle, from design to operational use and mainte-
vices to multiple resources for operational use. Com- nance. The selected secondary studies also mention
monly used patterns include serverless deployment, additional quality attributes, such as Modifiability
service instances per VM, and service instances per [SS33], Usability [SS33], Deployability [SS33], Flexi-
container [SS06]); and (5) Data storage bility [SS33], Reusability [SS29], Manageability
[SS03][SS19][SS33][SS37]–patterns oriented [SS29], Independence [SS29], Traceability [SS40],
towards improving performances of data management Complexity [SS40], Load balancing [SS29], and Orga-
systems. Commonly used patterns include the data- nizational alignment [SS29].
base-per-service pattern, the database cluster pattern,
To effectively address quality attributes, appropri-
and the shared database server pattern [SS37]).
ate metrics need to be proposed, such as time, com-
plexity, number of requests, or number of affected files
In addition, the authors discussed antipatterns in
[SS03][SS17]. These metrics facilitate continuous
[SS01] and [SS44], which refer to design and imple-
improvements in quality attributes over time [SS07].
mentation choices that result in inadequate/poor soft-
ware system design, leading to issues during operation 4.3.2. Life cycle scope. Microservice-based sys-
and maintenance. In [SS01], antipatterns are catego- tems, like other software systems, undergo various
rized in a catalog that covers the design, implementa- lifecycle phases that bring forth unique challenges,
tion, deployment, and monitoring of microservices. necessitating the utilization of specific methods,
On the other hand, [SS44] focuses on antipatterns and approaches, and tools. It is crucial to consider not only
specific software tools for visualizing microservices technical and technological aspects but also human
during runtime. and organizational factors that impact activities
throughout the entire lifecycle. The primary topics
Presentation. Efficient design and utilization of
identified in the selected secondary studies pertaining
microservice-based systems require the presentation
to the life cycle scope of microservices encompass
of software architecture through various approaches
Design, Implementation, Testing, Deployment, Mainte-
that depict the system’s structure and behavior. It is
nance and Operation, Runtime, Organizational issues,
crucial to consider the dynamic characteristics of the
and the Human factor (refer to Fig. 4).
system during both the development phase and opera-
A more comprehensive review of life cycle scope
tional use, which necessitates effective visualization.
topics, along with their respective subtopics and the
The secondary studies identified the following subtop-
distribution of secondary studies mentioning them is
ics: (1) Languages [SS22][SS27][SS29][SS33]–This
given in Table 8.
pertains to the use of specific languages for describing
the architecture, such as RAML, YAML, Jolie, or var- Design. The design phase of the lifecycle is crucial
ious pseudocodes [SS27][SS29]; (2) Diagrams for achieving the desired system structure and fulfill-
[SS27][SS29]–this involves the utilization of visual ing the proposed quality characteristics. Topics in this
diagrams, ranging from informal drawings to special- phase are closely related to design patterns, architec-
ized and sophisticated diagrams such as Compo- ture representation, and quality attributes, all of which
nent/Container, Process/Behavior, Sequence, Execu- fall under the general topic of Architecture. The fol-
tion Timeline, Deployment, Class, Use Case, Type lowing subtopics have been identified in the secondary
Graph, Instance Graph, and Dependency Graph studies: (1) Identification strategies [SS02][SS04]– this
[SS29]; and (3) Visualization [S30]–this subtopic subtopic focuses on the identification of services
focuses on the application of dynamic analysis tech- during the design of complex systems; (2) Domain-
niques, supported with specialized tools, for analyzing Driven Design [SS04][SS39]–this subtopic relates to
or recovering software architecture. Techniques such the use of principles, patterns, and domain-specific
as process mining, distributed tracing, and monitoring knowledge during system design; (3) Representations
are employed for this purpose. [SS04][SS34][SS36][SS39]–this subtopic is about the
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

| 808 |     | STOJANOV et al. |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- |
Table 8. Topics and subtopics related to the life cycle scope of microservices
| Topic                   |                             | Subtopic |     |                                          | Secondary studies |     |
| ----------------------- | --------------------------- | -------- | --- | ---------------------------------------- | ----------------- | --- |
| Design                  | Identification strategies   |          |     | SS02, SS04                               |                   |     |
|                         | Domain driven design        |          |     | SS04, SS39                               |                   |     |
|                         | Representations             |          |     | SS04, SS34, SS36, SS39                   |                   |     |
|                         | Design for failure          |          |     | SS08, SS36                               |                   |     |
| Implementation          | Technology stack            |          |     | SS08, SS36, SS37                         |                   |     |
|                         | Supporting systems          |          |     | SS08, SS34, SS36, SS37                   |                   |     |
|                         | Services interfaces         |          |     | SS08, SS34                               |                   |     |
| Testing                 | Approaches                  |          |     | SS14, SS23, SS25, SS36, SS37, SS40       |                   |     |
|                         | Tools                       |          |     | SS25, SS37, SS40                         |                   |     |
| Deployment              | Platform                    |          |     | SS08, SS32, SS34, SS37                   |                   |     |
|                         | Monitoring                  |          |     | SS08, SS14, SS23, SS32, SS34, SS36, SS39 |                   |     |
|                         | Approaches                  |          |     | SS06, SS23, SS32, SS37                   |                   |     |
| Maintenance & Operation | Load balancing              |          |     | SS11, SS34                               |                   |     |
|                         | Fault diagnosis             |          |     | SS11, SS23, SS36, SS37, SS39             |                   |     |
|                         | Autoscaling                 |          |     | SS11, SS12, SS21, SS34, SS37             |                   |     |
|                         | Anomaly detection           |          |     | SS13, SS37                               |                   |     |
|                         | Resource scheduling         |          |     | SS13, SS33                               |                   |     |
|                         | Analysis                    |          |     | SS36, SS39                               |                   |     |
| Runtime                 | Virtualization              |          |     | SS08, SS43                               |                   |     |
|                         | Discovery                   |          |     | SS14, SS43                               |                   |     |
|                         | Control                     |          |     | SS08, SS34, SS39                         |                   |     |
|                         | Verification and validation |          |     | SS08, SS21                               |                   |     |
|                         | Visualization               |          |     | SS30, SS39, SS44                         |                   |     |
Organizational issue DevOps SS08, SS19, SS25, SS32, SS33, SS34, SS37,
SS43
|              | Continuous delivery–integration–deployment |     |     | SS08, SS25, SS43 |     |     |
| ------------ | ------------------------------------------ | --- | --- | ---------------- | --- | --- |
| Human factor | Roles                                      |     |     | SS04, SS17       |     |     |
|              | Skills                                     |     |     | SS04, SS38       |     |     |
use  of  various  methods  and  tools  for  representing Supporting  systems  [SS08][SS34][SS36][SS37]–this
microservice system being developed; and (4) Design subtopic focuses on data storage systems for distrib-
for failure [SS08][SS36]–this subtopic is related to uted microservices (e.g., SQL, graph-oriented, docu-
design principles and methods that enable the design ment-oriented) and systems for service discovery in a
of systems with increased fault tolerance, self-healing dynamic environment with heterogeneous microser-
capabilities, and variability characteristics. These sub- vices (e.g., client-drive, server-driven); and (3) Service
topics provide valuable insights into the design phase interfaces [SS08][SS34]–this subtopic concerns the
and its importance in creating robust microservice-
specification of contracts for microservices communi-
based systems. cation, encompassing formal, tech-tied, and ad-hoc
definitions in a novel language. These subtopics shed
Implementation.  The  implementation  phase  uti- light on the implementation phase and the important
lizes the products and decisions from the design phase
considerations related to technology selection, sup-
| to  create  microservices  | and  integrate  | them  into  | a   |     |     |     |
| -------------------------- | --------------- | ----------- | --- | --- | --- | --- |
porting systems, and service interfaces in the develop-
cohesive system. Through an analysis of the secondary
ment of microservice-based systems.
studies, the following subtopics have been identified:
(1) Technology stack [SS08][SS36][SS37]–this sub- Testing. The complex nature and dynamic behavior
topic pertains to the use of various languages (formal, of microservice-based systems present several chal-
scripting,  object-oriented),  interaction  models  for lenges in their testing, as it requires a deep understand-
communication flow, and protocols for data exchange ing of the intricate and concurrent behaviors of micro-
(e.g., REST/HTTP, RPC-alike, message queues); (2) services and their mutual interactions. Through an
|     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 49   No. 8  |  2023 |
| --- | --- | ---------------------------------- | --- | --- | ----------------- | ----- |

A TERTIARY STUDY ON MICROSERVICES 809
analysis of the secondary studies, the following sub- [SS23][SS36][SS37][SS39]–this subtopic involves
topics have been identified: (1) Approaches [SS14] improving the quality and efficiency of software oper-
[SS23][SS25][SS36][SS37][SS40]–this subtopic encom- ation by detecting faults. It includes activities such as
passes various testing approaches employed during monitoring and localization of faults, identifying fault
development, ranging from unit testing to integration types, and fault modeling; (3) Autoscaling [SS11]
testing., It also includes continuous testing as part of [SS12][SS21][SS34][SS37]–autoscaling relates to the
DevOps and continuous engineering practices, testing adjustment of system resources to meet changing
of microservices and system performance, testing needs and growing requirements. This subtopic covers
during migration, and model-based testing; and (2) resource prediction and scheduling methods, as well
Tools [SS25][SS37][SS40]–this subtopic pertains to as resource allocation and recovery techniques; (4)
the tools utilized in the testing process, with a prefer- Anomaly detection [SS13][SS37] – Anomaly detection
ence for automated testing. It includes libraries and focuses on identifying critical behaviors or abnormal
frameworks that enable specific types of tests. These states in application performance. It involves tech-
subtopics shed light on the challenges associated with niques for detecting and handling anomalies to ensure
testing microservice-based systems and highlight the system stability; (5) Resource scheduling [SS13][SS33]–
importance of employing appropriate approaches and this subtopic involves the dynamic adjustments of sys-
tools for comprehensive and effective testing through- tem resources in response to the overall system state
out the software development lifecycle. and workload. It includes techniques for efficiently
Deployment. A deployment practice encompasses managing and allocating resources based on demand;
activities, methods, and tools necessary for the estab- and (6) Analysis [SS36][SS39]–this subtopic covers
lishment of heterogeneous microservices to meet the methods and tools for analyzing the states and behav-
requirements of contemporary businesses. Automated iors of microservice-based systems during operational
and continuous development and deployment pro- use. It includes static analysis, dynamic analysis, com-
cesses are essential in ensuring the reliable and scalable bined dynamic and static analysis, model-based anal-
delivery and operation of microservice-based systems. ysis, graph-based analysis, and pattern-based analysis.
The analysis of the secondary studies has identified All these subtopics highlight the importance of load
the following subtopics: (1) Platform [SS08][SS32] balancing, fault diagnosis, autoscaling, anomaly
[SS34][SS37]–this subtopic pertains to the selection detection, resource scheduling, and analysis in the
of a hosting system for running microservices, such as maintenance and operation of microservice-based
public cloud, private cloud, or in-house infrastruc- systems.
ture; (2) Monitoring [SS08][SS14][SS23][SS32] Runtime. Analyzing the architecture, functioning,
[SS34][SS36][SS39]–this subtopic relates to the and performance of microservices-based systems
activities performed to prevent or respond to failures or requires extracting information from both static and
changes in the environment. It encompasses the use of dynamic sources during runtime. Monitoring the
built-in cloud services, third-party services, and ad- dynamics of the system is crucial because changes in
hoc solutions for monitoring microservices; and (3) structure and communication often occur during sys-
Approaches [SS06][SS23][SS32][SS37]–this subtopic tem execution. The following subtopics have been
addresses the various ways and strategies employed to identified: (1) Virtualization [SS08][SS43]–this sub-
facilitate the utilization of microservices-based sys- topic pertains to different levels of platform abstrac-
tems. It includes considerations such as hosting multi- tion, isolation, and sharing. It includes technologies
ple services per host or adopting a single service-per- such as virtual machines, containers, serverless com-
host approach. These subtopics highlight the impor- puting, and non-virtualized environments; (2) Discov-
tance of selecting the appropriate platform, imple- ery [SS14][SS43]–discovery relates to identifying and
menting robust monitoring practices, and employing finding appropriate services based on workload, scal-
effective approaches for deploying and utilizing ability, and service quality considerations. This sub-
microservice-based systems. topic covers mechanisms and optimization techniques
Maintenance and operation. The primary focus of for efficient service discovery; (3) Control
maintenance and operation activities in the software [SS08][SS34][SS39]–control involves managing exe-
life cycle is to ensure the usability and operability of cution at both the local level of individual microser-
the software. Effective maintenance activities are cru- vices and the system level as a whole. It includes activ-
cial for ensuring the stable and reliable functioning of ities such as monitoring, planning, execution, and
complex microservice-based software systems. The evaluation to ensure effective control over the system;
following subtopics have been identified: (1) Load bal- (4) Verification and Validation [SS08][SS21]–this sub-
ancing [SS11][SS34]–this subtopic pertains to the topic focuses on assessing the quality of microservices
coordination and management of a large number of during runtime. It includes the use of models and
service requests in systems with heterogeneous and properties for verification and validation purposes;
distributed microservices. It involves the use of algo- and (5) Visualization [SS30][SS39][SS44]–visualiza-
rithms and performance measurement techniques to tion relates to visually representing the microservices
optimize load distribution; (2) Fault diagnosis [SS11] architecture during runtime. This subtopic covers
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

810 STOJANOV et al.
techniques, tools, and types of information that can be to keep them operational and useful for end users.
extracted and displayed for better understanding and However, frequent modifications can increase soft-
analysis. Overall, these subtopics highlight the impor- ware complexity, reduce performance, and make
tance of virtualization, discovery, control, verification maintenance challenging. One common solution to
and validation, and visualization in the analysis of address these issues is migrating software systems to
microservices-based systems. microservices architectures. In the selected secondary
studies, the main topics related to migration to micro-
Organizational issue. Software development, oper-
services are Approach, Process/roadmap, and Chal-
ation, and maintenance take place within specific
lenges (refer to Fig. 4). A more detailed review of
organizational contexts, including software develop-
migration topics, including identified subtopics and
ment organizations and client organizations. These
the distribution of secondary studies that mention
contexts have their own processes, procedures, chal-
them, is presented in Table 9.
lenges, and cultures that impact the technical and
technological aspects of software processes. The follow- Approach. In practice, different types of legacy sys-
ing subtopics have been identified: (1) DevOps [SS08] tems require varying approaches for modernization
[SS19][SS25][SS32][SS33][SS34][SS37][SS43]–DevOps and migration to microservice architectures. These
encompasses the cultural and practical aspects of approaches necessitate the use of specific strategies,
organizing stakeholders involved in the development methods, and tools while also presenting specific chal-
and operation of microservices-based systems. lenges. The identified subtopics in the secondary stud-
Itinvolves addressing people-related issues, establish- ies are as follows: (1) Strategy [SS24][SS13][SS26]
ing effective processes, and utilizing appropriate tools [SS38]–this subtopic pertains to the overall strategy
and technologies; and (2) Continuous Delivery, Inte- chosen in a migration project, such as clustering, can-
gration, and Deployment [SS08][SS25] [SS43]–this didate identification based on quality attributes, data-
subtopic focuses on continuous activities that facilitate driven approaches, or bottom-up approaches; (2)
a seamless transition between phases in microservices- Decomposition method [SS09][SS24][SS13][SS26]–
based systems. It includes practices related to continu- this subtopic focuses on the selection of the analysis
ous delivery, integration, and deployment to ensure method used to decompose the legacy system and
smooth and efficient software development and identify microservices. Examples include Static Code
deployment processes. These subtopics highlight the Analysis, Meta-Data aided, Workload-Data aided, or
importance of considering organizational contexts, Dynamic Microservice Composition; (3) Unit level
including DevOps practices and continuous delivery, [SS09][SS24][SS38]–this subtopic involves selecting
integration, and deployment, to effectively address the the most suitable level of software artifacts during the
challenges and complexities associated with software decomposition of the old system and migration to
development, operation, and maintenance within dif- microservices. Options may include business func-
ferent organizations. tions, database tables, classes, use cases, or EJBs; and
(4) Evolution [SS09][SS24][SS38]–this subtopic
Human factor. Even though the literature primarily relates to supporting the scalability and maintainabil-
emphasizes technical and technological aspects, it is ity features of the new microservice-based system
important to recognize that all activities in the soft- throughout the migration process. All these subtopics
ware systems’ life cycle are ultimately carried out and highlight the diverse considerations and decisions
supervised by people. The following subtopics have involved in modernizing and migrating legacy systems
been identified: (1) Roles [SS04][SS17]–this subtopic to microservices. They provide insights into the strat-
pertains to the various roles that individuals assume in egies, decomposition methods, unit levels, and evolu-
the microservice life cycle within software organiza- tionary aspects that are crucial for successful migra-
tions and client organizations; and (2) Skills tion projects.
[SS04][SS38]–this subtopic focuses on the technical and
Process/roadmap. Every migration project follows
soft skills that are necessary for individuals in different
a process or roadmap that guides the organization of
roles within the microservices’ life cycle. It encompasses
activities and determines the input and output infor-
the specific knowledge, expertise, and abilities
mation. Additionally, specific factors can significantly
required to effectively perform their respective tasks.
influence the migration process, depending on the
These subtopics underscore the significance of con-
unique characteristics of each project. The identified
sidering the human factor in addition to the technical
subtopics in the secondary studies are as follows: (1)
and technological aspects of software development.
Definition [SS24][SS26][SS38]–this subtopic pertains
By understanding the roles and skills of individuals
to the selection or proposal of different processes,
involved in the microservice life cycle, organizations
guidelines, and roadmaps, supported by specific tools,
can better support their teams and ensure the success-
to facilitate the migration process; (2) Input informa-
ful execution of software projects.
tion [SS24][SS26][SS38]–this subtopic focuses on
4.3.3. Migration. One of the primary challenges identifying the required input information for the
with legacy software systems, built on monolithic migration process, such as documents, APIs, non-
architecture, is the need for subsequent modifications functional requirements, tools, and the team’s exper-
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 811
Table 9. Topics and subtopics related to migration to microservices
|                 | Topic |                      | Subtopic |                        | Secondary studies |
| --------------- | ----- | -------------------- | -------- | ---------------------- | ----------------- |
| Approach        |       | Strategy             |          | SS24, SS13, SS26, SS38 |                   |
|                 |       | Decomposition method |          | SS09, SS24, SS13, SS26 |                   |
|                 |       | Unit level           |          | SS09, SS24, SS38       |                   |
|                 |       | Evolution            |          | SS09, SS24, SS38       |                   |
| Process/roadmap |       | Definition           |          | SS24, SS26, SS38       |                   |
|                 |       | Input information    |          | SS24, SS26, SS38       |                   |
|                 |       | Output information   |          | SS24, SS26             |                   |
|                 |       | Success factors      |          | SS38                   |                   |
|                 |       | Motivation           |          | SS24                   |                   |
| Challenges      |       | Technical            |          | SS24, SS26, SS38       |                   |
|                 |       | Organizational       |          | SS26, SS38             |                   |
|                 |       | Knowledge and skills |          | SS04, SS26, SS38       |                   |
tise; (3) Output information [SS24][SS26]–this sub- cal skills necessary for the successful implementation
topic relates to the information produced upon com- of the migration project. It highlights the significance
pleting the migration process, including microservices of expertise and competency within the team. These
candidates, communication approaches, and system subtopics highlight the significant aspects that need to
architecture; (4) Success factors [SS38]–this subtopic be addressed during the migration of existing systems
encompasses the factors that influence the successful to a microservice-based architecture. The technical
execution and completion of the migration process, considerations, organizational adjustments, and the
such as system architecture, time and cost consider- importance of assembling a knowledgeable and skilled
ations, replacement strategies, achievable attributes, team contribute to the overall success of the migration
application size, and complexity; and (5) Motivation project.
[SS24]–this subtopic explores the motivations or driv-
4.3.4. Challenges. The adoption of microservices in
| ing  factors  | behind  organizing  | a  migration  | project, |     |     |
| ------------- | ------------------- | ------------- | -------- | --- | --- |
industrial practice presents numerous challenges for
which can be technical, operational, or organizational
both practitioners and researchers, given the inherent
in nature. All these subtopics shed light on the various complexity and heterogeneity of microservice-based
elements involved in migration projects, ranging from
systems. Exploring and addressing the problems and
defining processes and gathering input information to
challenges identified in the literature can lead to solu-
| generating  | output  information,  | considering  | success |     |     |
| ----------- | --------------------- | ------------ | ------- | --- | --- |
tions that enhance the performance of software sys-
factors, and understanding the motivations behind the tems in practical settings. Figure 4 illustrates eight
project. They provide insights into the comprehensive
challenges that have been mentioned in at least three
framework necessary for a successful and well-orga-
secondary studies, with additional challenges catego-
nized migration process.
rized under the “Other …” section. A comprehensive
list of 21 identified challenges, along with the corre-
Challenges. The migration of existing systems to a
sponding secondary studies that reference them, is
new microservice-based architecture is a challenging
project that poses various obstacles for organizations, presented in Table 10. By understanding and tackling
these challenges, practitioners, and researchers can
teams, and individuals involved. The identified sub-
make significant strides in overcoming the obstacles
topics in the secondary studies are as follows: (1) Tech-
inherent in microservice adoption and improve the
nical [SS24][SS26][SS38]–this subtopic focuses on
the introduction of new technologies and the selection effectiveness of software systems.
of the most suitable tools for the migration process; (2) Upon reviewing the secondary studies, it becomes
Organizational [SS26][SS38]–this subtopic pertains to evident that regardless of the topics covered, all studies
organizational changes within an IT company that identified  specific  challenges  and  proposed  corre-
undertakes a migration process. It involves reorganiz- sponding solutions. Among the challenges identified,
ing the hierarchical structure of the company and Security emerges as the most crucial, with 13 occur-
establishing independent teams to work on individual rences across the studies. These discussions encom-
services,  promoting  a  more  efficient  and  effective pass  a  wide  range  of  topics,  needs,  and  scenarios
workflow.; and (3) Knowledge and skills [SS04, SS26, [SS16], with proposed taxonomies or frameworks to
SS38]–this subtopic emphasizes the importance of address  security  issues  [SS14].  Following  closely,
selecting team members with the appropriate knowl- Communication is mentioned in seven studies as the
edge and a combination of technical and non-techni- second most frequently cited challenge. Communica-
| PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 49   No. 8  |  2023 |     |
| ---------------------------------- | --- | --- | ----------------- | ----- | --- |

812 STOJANOV et al.
Table 10. Challenges related to microservices
|     | Challenge |     |     | Secondary studies |     |     | Frequency |
| --- | --------- | --- | --- | ----------------- | --- | --- | --------- |
Security SS14, SS15, SS16, S18, SS23, SS27, SS28, SS29, SS33, SS34, SS35, SS36, SS42 13
| Communication |     | SS06, SS14, SS18, SS23, SS27, SS29, SS34 |     |     |     |     | 7   |
| ------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
Testing and quality assurance SS14, SS23, SS25, SS27, SS34, SS36 6
| Performance            |     | SS14, SS23, SS29, SS33, SS36 |     |     |     |     | 5   |
| ---------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- |
| Deployment             |     | SS06, SS23, SS29, SS32, SS36 |     |     |     |     | 5   |
| Monitoring and tracing |     | SS14, SS23, SS29, SS32, SS36 |     |     |     |     | 5   |
| Service discovery      |     | SS14, SS23, SS29             |     |     |     |     | 3   |
| Data management        |     | SS14, SS27, SS34             |     |     |     |     | 3   |
| Scalability            |     | SS21, SS36                   |     |     |     |     | 2   |
| Migration              |     | SS26, SS38                   |     |     |     |     | 2   |
| Complexity             |     | SS27, SS34                   |     |     |     |     | 2   |
| Composition            |     | SS27, SS34                   |     |     |     |     | 2   |
| Decomposition          |     | SS14                         |     |     |     |     | 1   |
| Orchestration          |     | SS14                         |     |     |     |     | 1   |
| Modeling               |     | SS23                         |     |     |     |     | 1   |
| Context awareness      |     | SS23                         |     |     |     |     | 1   |
| Integration            |     | SS29                         |     |     |     |     | 1   |
| Fault tolerance        |     | SS29                         |     |     |     |     | 1   |
| Publishing             |     | SS32                         |     |     |     |     | 1   |
| Upgrading              |     | SS32                         |     |     |     |     | 1   |
| Availability           |     | SS36                         |     |     |     |     | 1   |
tion challenges may arise from remote calls, during of appropriate discovery mechanisms is crucial. Addi-
replication of services or data, or service discovery tionally, during runtime, it becomes essential to dis-
[SS06]. The third most frequently mentioned chal- cover services that meet the required quality parame-
| lenge  pertains  | to  Testing  | and  | quality  assurance  | of ters [SS14]. |     |     |     |
| ---------------- | ------------ | ---- | ------------------- | --------------- | --- | --- | --- |
microservice-based systems. This encompasses vari-
Overall, all the identified challenges, as presented
ous specific challenges, including faster test feedback, in Table 10, require careful consideration in specific
automated testing, intercommunication testing, gran-
|                    |          |           |                       | design  or  usage  | scenarios.  | This  involves  | exploring |
| ------------------ | -------- | --------- | --------------------- | ------------------ | ----------- | --------------- | --------- |
| ularity  testing,  | runtime  | testing,  | integration  testing, |                    |             |                 |           |
potential solutions for identified problems and making
and performance testing [SS25].
informed decisions to ensure the desired fulfillment of
system quality attributes.
Deployment poses a significant challenge due to the
| complexity  | involved  | in  deploying  | heterogeneous |     |     |     |     |
| ----------- | --------- | -------------- | ------------- | --- | --- | --- | --- |
microservices. This challenge encompasses deploy-
4.4. Technical Implementation and Integration (RQ4)
ment coordination, cost considerations, required con-
figurations, continuous integration, continuous deliv- The dynamics and the increasing need for integrat-
ery, and managing independent microservice failures ing heterogeneous and complex systems in various
[SS06]. Another important challenge pertains to the sectors such as healthcare, industry, and transporta-
Performance quality attribute, which receives the most tion  necessitate  the  adoption  of  service-oriented
attention, especially when trade-offs between multiple architectures to facilitate distributed processing capa-
attributes are necessary [SS07]. Monitoring and tracing bilities  and  data  integration.  Microservices  have
microservice-based systems involve monitoring run- emerged as a popular solution due to their widely rec-
time performance, overseeing the infrastructure sup- ognized advantages, leading to their widespread use
porting microservices execution, and logging data for across  different  business  domains  and  in  various
further  analysis  to  enhance  system  performance aspects of human life. The selected secondary studies
[SS30]. Data management presents challenges related highlight three main topics related to the technical
to maintaining service independence, ensuring data implementation  and  integration,  including  Service
consistency,  and  governing  distributed  transactions type, Service domain, and Industry adoption (refer to
[SS14]. Service discovery poses a challenge during sys- Fig. 4). For a more comprehensive examination of
tem design and implementation, where the selection technical implementation and integration, Table 11
|     |     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 49   No. 8  |  2023 |
| --- | --- | --- | ---------------------------------- | --- | --- | ----------------- | ----- |

A TERTIARY STUDY ON MICROSERVICES 813
Table 11. Topics and subtopics related to technical implementation and integration of microservices
Topic Subtopic Secondary studies
Service type Functional SS05, SS34
Infrastructure SS05, SS34
Domain Smart systems SS05, SS09, SS31, SS43 (smart city, IoT)
Fog applications SS42
Big data SS20
Blockchain SS31
Enterprise SS31, SS33, SS43
Industry adoption Readiness level SS27, SS34
Industry involvement SS27, SS34
Tools and system support SS27, SS34
Evaluation and benchmarking SS27, SS31, SS34
provides a detailed overview of the identified related on the use of microservices in various business
subtopics and the distribution of secondary studies domains, such as healthcare, online commerce, sup-
that mention them. ply chain management, financial systems, and tele-
communications. All these subtopics provide insights
4.4.1. Service type. Microservices are deployed
into the specific application areas where microservices
within complex and heterogeneous systems, requiring
are utilized, enabling researchers and practitioners to
sophisticated infrastructures for hosting and execu-
explore and contribute to these domains.
tion. Apart from the functional services that cater to
user needs, it is crucial to deploy services that support 4.4.3. Industry adoption. The majority of studies
the infrastructure essential for the proper functioning
report the widespread acceptance and adoption of
of microservices. The secondary studies have identi-
microservices in various business scenarios, establish-
fied two main subtopics in this context: (1) Functional ing them as a prominent software development
services [SS05][SS34]–these services are responsible
approach in the software and IT industry. However,
for providing functionalities to users, enabling them to
adopting microservices introduces several issues that
perform tasks or access features; and (2) Infrastructure
warrant investigation to enhance practices in the soft-
services [SS05][SS34]–these services encompass non-
ware industry. The identified subtopics in the second-
functional requirements, infrastructure, and service
ary studies are as follows: (1) Readiness level [SS27]
monitoring, as well as maintenance tasks that are not
[SS34]–this topic pertains to the maturity level of spe-
directly related to user functionalities but are crucial
cific methods, tools, and technologies intended for
for the overall functioning of the system. By under-
implementation in industrial projects. It focuses on
standing and addressing these subtopics, organiza-
assessing the readiness of these resources for practical
tions can ensure the efficient deployment and man-
adoption; (2) Industry involvement [SS27][SS34]–this
agement of microservices within their infrastructures.
subtopic explores the degree of engagement and par-
4.4.2. Domain. The secondary studies have identi- ticipation of industry experts in research projects. Col-
fied the following subtopics: (1) Smart systems [SS05] laboration with industry professionals enhances
[SS09][SS31][SS43]–this subtopic focuses on the knowledge sharing and promotes practical applicabil-
implementation of microservices for technical inte- ity; (3) Tools and system support [SS27][SS34]–this
gration in smart systems, such as smart cities, smart subtopic examines the utilization of specialized tools
transportation, and IoT applications; (2) Fog applica- and systems that support the development and opera-
tions [SS42]–this subtopic explores the use of micros- tion of microservice-based systems. Examples include
ervices in fog computing applications, including moti- knowledge-based tools and open-source test systems
vations, challenges, and methods; (3) Big data that facilitate the implementation and management of
[SS20]–this subtopic examines the utilization of such architectures; and (4) Evaluation and benchmark-
microservices in Big Data applications, exploring the ing [SS27][SS31, SS34]–this subtopic emphasizes the
interplay between microservices and Big data, as well use of evaluation and benchmarking tools to assess the
as relevant methods and application domains; (4) quality and effectiveness of designed microservice-
Blockchain [SS31]–this subtopic investigates the com- based architectures. Evaluation and benchmarking
bination of microservices with blockchain technolo- provide valuable insights into the performance and
gies, addressing methods, challenges, and domains viability of these architectures. The aforementioned
where these technologies are applied together; and (5) subtopics shed light on critical aspects related to
Enterprise [SS31][SS33][SS43]–this subtopic focuses microservices adoption, including readiness, industry
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

814 STOJANOV et al.
collaboration, tooling support, and evaluation prac- approaches [SS06][SS09][SS25][SS29], technologies
tices. Exploring and addressing these areas can contrib- [SS31][SS34], design patterns [SS03][SS15][SS44]
ute to further improvements in the software industry. and antipatterns [SS01][SS44], languages [SS22], and
tools [SS04][SS16][SS22][SS24][SS25][SS26][SS30]
[SS39][SS44] can be utilized. These resources offer
4.5. Directions for Future Research (RQ5) opportunities for advancements in microservice archi-
When considering the enumeration and listing of tectures, enabling more efficient and effective devel-
potential future research directions, it should be noted opment and operation [SS08][SS14][SS32]. By lever-
that these directions have been identified by analyzing aging these innovative elements, researchers and prac-
the discussion sections and concluding remarks of titioners can explore new possibilities and overcome
each examined secondary study. These sections also existing challenges in this domain.
highlight the emerging open challenges that need to be
(cid:129) To ensure the quality of microservice architec-
addressed. Therefore, we searched within the second-
tures, it is crucial to assess the associated quality attri-
ary studies using keywords such as “future” in combi-
butes [SS19]. These attributes encompass scalability
nation with the words “research,” “work,” and “direc-
[SS12][SS21][SS22], performance [SS24][SS33]
tion,” as well as the keywords “further,” “challenge,”
[SS43], availability [SS11], monitorability [SS33], reli-
and “gap.”
ability [SS11][SS25][SS40], security [SS16][SS27]
Notably, the majority of authors indicate future [SS28][SS33][SS34], testability [SS25][SS27][SS34],
research directions in two main ways: (a) by highlight- maintainability [SS11][SS43], resilience [SS25],
ing and elaborating on potential research gaps, open interoperability [SS40], and portability [SS21][SS27]
challenges, and issues encountered during their analy- [SS34]. It is also important to consider their complex
sis, and using them as a basis to propose broader interactions and trade-offs [SS03][SS07][SS25][SS34]
research directions through calls for action to the [SS39][SS42][SS43]. By evaluating and addressing
community of researchers and practitioners in the these attributes, researchers and practitioners can
field of microservice architectures; and (b) by propos- optimize the performance, robustness, and overall
ing specific research directions that are closely related effectiveness of microservice architectures. This com-
to the research methodology employed in their study. prehensive assessment can help identify areas for
These specific directions aim to promote the effective improvement and guides the development of resilient
development and application of microservice archi- and adaptable systems.
tectures.
(cid:129) Focusing on the industrial adoption of microser-
In the coming years, the research focus on archi-
vice architectural designs, which involves several cru-
tecting with microservices, which is expected to shape
cial phases, including implementation, validation
their future, will center on addressing the following
[SS02][SS16][SS27], operation, deployment [SS06],
issues.
maintenance, and testing of microservice architectural
(cid:129) Exploring various types of microservice architec-
designs in practice [SS05][SS10][SS11][SS25][SS26]
tures, their structure, and design aspects. This involves
[SS32][SS34][SS35][SS36][SS37][SS41]. These phases
expanding the existing knowledge base in a systematic,
play a significant role in ensuring the successful imple-
structured, and consistent manner, (a) by including
mentation and long-term viability of microservice sys-
both theoretical and practical learning and exploration
tems in practice. Throughout the implementation
[SS07][SS10][SS19][SS23][SS26][SS29][SS32][SS37
phase, careful attention is given to translating architec-
][SS39][SS41][SS43], (b) by investigating the applica-
tural designs into tangible systems. Validation activi-
tion of microservices in specific domains [SS20] or real-
ties are conducted to verify that the microservice
world scenarios [SS21][SS24][SS25][SS27][SS30]
architecture aligns with the intended objectives and
[SS31][SS33], and (c) by considering organizational
requirements [SS02][SS16][SS27]. Once deployed,
factors [SS26][SS38] and addressing human-related
the system enters the operational phase, where it is
issues [SS27][SS31][SS32][SS37][SS38] in microser-
actively used and monitored to ensure its smooth
vice architectures. These research directions aim to
functioning [SS06]. Maintenance tasks, such as bug
enhance our understanding of microservices and con-
fixing, performance optimization, and feature
tribute to the development of a comprehensive and
updates, are performed to keep the microservice sys-
practical framework for their successful implementa-
tem in optimal condition [SS05][SS10][SS11][SS25]
tion.
[SS26]. Additionally, rigorous testing is carried out to
(cid:129) To enhance the current state and facilitate the verify the reliability, performance, and resilience of the
development and operation of future microservice architecture [SS32][SS34][SS35][SS36][SS37][SS41].
architectures, various novel and innovative methods By emphasizing these essential implementation
[SS16][SS17][SS26][SS39], models [SS13][SS14] phases, organizations can effectively adopt microser-
[SS39][SS41], frameworks [SS18][SS26][SS44], infra- vice architectures and reap the benefits of scalability,
structures [SS06], techniques [SS11][SS17][SS28], flexibility, and maintainability offered by this archi-
algorithms [SS39], migration strategies [SS16][SS24], tectural style.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 815
(cid:129) Standardizing microservice architecture, inter- determine which tools and approaches are suitable for
faces, and related aspects such as load balancing, fault practical implementation. Nonetheless, numerous
detection, and autoscaling [SS08][SS34][SS43]. challenges persist in this field, calling for continued
(cid:129) Designing fault-tolerant and event-driven/asyn- breakthroughs in the years to come.
chronous microservices, particularly for smart systems,
fog applications, and IoT applications [SS05][SS10]
5. DISCUSSION
[SS38][SS42].
(cid:129) Transitioning from specific solutions and their The following subsections present the implications
related validation to more general solutions through of the study for researchers and industry practitioners,
fundamental research, reusable practices, and lessons as well as validity considerations and recommenda-
learned [SS20][SS25][SS31]. tions for further research.
(cid:129) Addressing the complexities of the migration pro-
cess from monolithic applications to microservice-based
5.1. Implications
architectures systematically [SS07][SS09][SS16]
[SS23], as well as tackling challenges related to micro- The research encompasses studies published
service identification, granulation, and proper design within the last seven years. The analysis reveals a grad-
[SS38]. ual increase in the number of papers focused on the
(cid:129) Conducting additional systematic literature reviews topic of microservices, indicating its growing popular-
that consider gray literature to compare findings and chal- ity and the increasing interest in this subject. More-
lenges identified in both white and gray literature over, the realm of microservices covers a wide range of
[SS14][SS15][SS16][SS25][SS31][SS33], extending areas. The analyzed papers address various aspects,
existing secondary studies to include the latest knowledge including the architecture, life cycle, migration,
supplements [SS07][SS15][SS29][SS40] or exploring implementation, and challenges. This work’s signifi-
additional databases for comprehensive coverage cance lies in its contribution to a comprehensive body
[SS20][SS40], and enhancing literature review of knowledge constructed through the examination of
approaches by improving data extraction and synthesis 44 secondary studies. Researchers and industry prac-
methods, validity, and quality assessment of primary titioners who aim to explore this field can utilize this
studies [SS14][SS18][SS21]. knowledge as a foundation to delve into microservices
further.
All these research directions aim to advance our
understanding of microservices architecture and facil- 5.1.1. Implications for researchers. Researchers
itate the development of best practices, standardized from academic institutions and PhD students can
approaches, and improved methodologies in this rap- acquire valuable insights into cutting-edge research on
idly evolving field. microservices by carefully examining the paper’s find-
The analysis of the directions for future research ings. The presented results, along with the compre-
reveals that they are numerous and diverse. This can hensive list of references, serve as an excellent starting
be attributed to the relative novelty of microservices point for researching specific microservices-related
and microservice architectures, and their unique, yet topics, such as microservice architecture, life cycle
relatively unexplored nature, characterized by hetero- issues, migration, or technical implementation within
geneity, decentralization, and independence. Despite specific domains. Furthermore, researchers can lever-
their established status and known design practices, age the proposed methodology for conducting system-
challenges persist in effectively decomposing mono- atic literature reviews in their studies. It is worth noting
lithic systems and adopting microservice architec- that the research findings indicate a lax implementa-
tures. Research studies suggest a myriad of migration tion of quality assessment measures in the evaluated
strategies, technologies, tools, approaches, and lan- papers. This observation highlights areas that require
guages for this purpose. Nevertheless, there is still further investigation and emphasizes the need for
room for improvement, clarification, and standard- more stringent quality assessment practices in future
ization in these areas. The breadth of future research studies.
directions signifies that the field of microservice anal- 5.1.2. Implications for practitioners. The findings
ysis remains open to innovations and methodologies. reveal the current research focus and the growing
These advancements hold the potential to support the interest in various topics and areas. This information is
development of more robust systems and architectural significant for industry practitioners as it helps them
designs, particularly on an industry level. Since their stay informed about the most actively researched sub-
introduction, the influence and impact of microser- jects. Practitioners can easily access information on
vice architectures have significantly grown. specific topics related to microservice architecture,
This study provides a valuable roadmap for including models, patterns, granularity, quality attri-
researchers, highlighting areas that require further butes, life cycle issues, migration challenges, and tech-
exploration. It also serves as a guide for practitioners, nical implementation in specific domains. Further-
enabling them to assess the progress made thus far and more, they can gain valuable insights into recent
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

816 STOJANOV et al.
methods, topics, tools, and technologies, which can tertiary studies. These recommendations stem directly
be applied to enhance their professional work. from the research findings presented in this study. The
primary objective is to address areas that have received
limited attention in the analyzed secondary studies
5.2. Validity
and offer guidance on enhancing existing research and
In empirical software engineering, it is crucial to enriching the knowledge base. The recommendations
mitigate threats to validity, which enhances the study’s are organized and presented based on the overarching
quality and ensures the reliability of the findings [31]. topics discussed in the research findings section,
Validity assessment encompasses internal and external which include quality assessment trends, microser-
validity. vices architecture, life cycle issues, migration, techni-
5.2.1. Internal validity. Our study acknowledges cal implementation in different domains, and further
several threats to methodological validity, which research directions.
should be treated as constraints since it is impossible 5.3.1. Quality assessment trends. According to
to guarantee complete coverage. However, by adhering guidelines for conducting literature reviews, quality
to our methods, we have minimized the potential for assessment of included studies is typically considered
bias. The threats addressed in this study include the a mandatory component of systematic literature
selection of search strings, digital library selection, reviews, whereas it may not be required for systematic
selection criteria for secondary studies, and the con- mapping studies. Consequently, the quality assess-
struction of study findings. To address the first threat, ment question Q4 received a low score of 0.37. How-
we employed two search strings with relevant key- ever, it is important to note that the overall quality of
words aligned with our research objective, covering the review study, particularly the quality of findings
both SLRs and SMSs. For the second threat, we uti- and study validity, is greatly influenced by the assessed
lized six reputable digital libraries, encompassing pub- quality of the studies included in the review. There-
lications from esteemed journals and international fore, the primary recommendation for addressing this
conference proceedings. We employed the snowball- issue is to assess the quality of all the studies selected
ing technique to ensure a comprehensive collection of for inclusion in the review. Additionally, it is advisable
references. Regarding the third threat, we employed a to establish a minimum value threshold for study
five-phase approach to select primary studies, incor- inclusion to maintain rigorous standards throughout
porating carefully defined inclusion and exclusion cri- the review process.
teria, as well as quality assessment of secondary stud-
ies. The fourth threat was mitigated by conducting the 5.3.2. Architecture. Research about microservices
research in a manner that allows for easy traceability of architecture exhibits a significant level of research
all findings back to the original secondary studies. maturity, particularly in the areas of architecture anal-
Additionally, all authors actively participated in data ysis, pattern utilization, and the adoption of various
extraction and analysis processes, minimizing the methods for architectural representation. Moreover,
potential for misinterpretation of the initial data and considerable attention has been given to exploring
the constructed findings. The detailed description of quality attributes and their associated trade-offs.
the research process in the third section of the paper However, the research findings indicate the necessity
provides transparency by allowing insights into all for additional primary and secondary studies to
stages of the research, bolstering the validity and reli- address certain aspects. Specifically, there is a need to
ability of the constructed findings. evaluate quality attributes and metrics pertaining to
granularity, runtime architecture visualization, as well
5.2.2. External validity. The generalizability of the
as specific quality attributes such as context awareness,
findings is a key concern when assessing study external
integrability, fault tolerance, upgrading, and availabil-
validity. As this study specifically focuses on the field
ity. Conducting further studies in these areas will con-
of microservices as a tertiary study, the findings can-
tribute to a more comprehensive understanding of
not be directly extrapolated to other domains of soft-
microservices architecture and its associated quality
ware engineering. Nonetheless, the detailed descrip-
considerations.
tion of the research process and the construction of
research findings enable the replication and adapta- 5.3.3. Life cycle issues. Researchers have dedicated
tion of the procedure in similar studies within different substantial attention to life cycle issues, particularly
areas of software engineering. Through such imple- the utilization of contemporary approaches like
mentation and adaptation, the presented research pro- DevOps and continuous software engineering prac-
cess can be generalized and applied effectively. tices (continuous integration, continuous delivery,
continuous deployment, and monitoring). However,
certain topics have not received sufficient inquiry,
5.3. Recommendations
including human factor issues, domain-driven design,
This section provides comprehensive recommen- and specific maintenance and operation concerns,
dations for further literature reviews in the field of such as load balancing and anomaly detection, which
microservices, encompassing primary, secondary, and are closely associated with the system’s availability and
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 817
reliability attributes. It is recommended that further of findings in a more structured manner, it is suggested
research be conducted to address these areas and to employ data extraction and synthesis methods com-
deepen our understanding of their impact on micros- monly used in social sciences. These methods can
ervices. include grounded theory [32] for developing theories,
general inductive analysis [33] for creating catalogs
5.3.4. Migration. The migration of legacy systems,
with categories, or inductive thematic analysis [34] for
typically characterized by monolithic architectures, to
constructing thematic frameworks, leading to the
microservice architectures is a significant research
identification of patterns in practice [35], and the
topic. Numerous methods and tools have been pro-
development of theories necessary for building and
posed and evaluated in real-world settings, forming a
extending a knowledge base in this area of software
substantial knowledge base for practitioners and
engineering [36]. By implementing these recommen-
researchers alike. However, upon analyzing the study
dations, future review studies can further refine their
findings, it is evident that two key areas, namely moti-
methodologies and generate more robust and struc-
vation and success factors, have not been sufficiently
tured findings, contributing to the advancement of
addressed in the existing research. Investigating these
knowledge in the field.
aspects requires a comprehensive examination of both
technical and non-technical elements, encompassing
organizational and human factors, in both empirical
6. CONCLUSIONS
studies and literature reviews that systematically
address these issues. By addressing these gaps, future This tertiary study offers a comprehensive analysis
research can provide valuable insights into the motiva- of recent research on microservices, focusing on pub-
tion and success factors associated with migrating leg- lication trends, quality trends of published secondary
acy systems to microservice architectures. studies, research topics, domains of implementation,
and future research challenges. The findings stem
5.3.5. Technical implementation in different
from a systematic literature review process, which
domains. Limited research has been documented in
involved the selection of 44 secondary studies. The
research papers and literature reviews concerning the
study addresses research implications for both aca-
technical implementation of microservices across var-
demic researchers and software industry experts, dis-
ious domains. Most of the research focuses on the ini-
cusses the validity of the study, and provides detailed
tial development of microservice-based systems, with
recommendations for further research. The primary
limited evaluations conducted in real-world settings,
contribution of this study lies in its in-depth explora-
primarily within IoT-based smart systems. Conse-
tion of microservices implementation across various
quently, there is a lack of empirical evidence regarding
domains, as well as providing detailed and structured
the implementation of proposed solutions and the uti-
recommendations for further research endeavors.
lization of technologies in real systems. Furthermore,
projects carried out by academic institutions often lack Building upon the research findings, recommen-
involvement from industry experts. There is a pressing dations for further literature reviews include improv-
need to conduct implementation studies within ing the quality assessment of analyzed studies, con-
authentic settings across different domains to obtain ducting more detailed reviews of architecture quality
valuable feedback on architecture models, methodol- attributes, exploring human factor issues, and address-
ogies, and employed technologies. It is also strongly ing maintenance and operation concerns. Addition-
recommended to engage industry experts to gain a ally, conducting reviews that focus on the technical
more comprehensive understanding of microservice- implementations of microservices within different
based system implementations. By addressing these business and human life domains is advised to gain a
gaps, researchers can enhance the practical applicabil- deeper understanding of their advantages, disadvan-
ity and effectiveness of microservices in real-world tages, and comparative analysis with other architec-
scenarios. tural approaches. The inclusion of domain experts in
the preparation and implementation of these literature
5.3.6. Methodological issues for further research. reviews will lead to more precise and valid findings.
Upon examining the methodological aspects of sec-
From the methodological standpoint, further
ondary studies, it is evident that there are several areas
reviews should consider incorporating qualitative
for further enhancement in review studies. The pre-
social science methods, such as inductive thematic
sented literature review offers recommendations in the
analysis or grounded theory, to obtain more structured
following areas. (1) Integration of gray literature: it is
and reliable findings. This approach may aid in identi-
recommended to incorporate gray literature into
fying patterns in practice, and contribute to the devel-
review studies to complement the insights obtained
opment of theories necessary for building a knowledge
from white literature. This inclusion will provide a
base in this area of software engineering.
more comprehensive understanding of the industry
experts’ perspectives and the current state of practice. Future work will be directed toward three main
(2) Utilization of data extraction and synthesis meth- areas. Firstly, there will be an emphasis on incorporat-
ods from social sciences: to enhance the development ing gray literature in the review process to gain insights
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

818 STOJANOV et al.
predominantly from industry experts and to compare review. Information and software technology, 131,
the state of practice from both academic researchers’ 106449.
and industry experts’ perspectives. Secondly, there https://doi.org/10.1016/j.infsof.2020.106449.
will be a focus on conducting literature reviews specif- [SS08] Garriga, M. (2017). Towards a taxonomy of
ically centered on microservices implementation in microservices architectures. In International confer-
different business and human life domains. Lastly, a ence on software engineering and formal methods (pp.
more comprehensive review of organizational issues 203–218). https://doi.org/10.1007/978-3-319-74781-
and the human factor in the microservices life cycle 1_15.
will be undertaken, addressing areas that have received
[SS09] Fritzsch, J., Bogner, J., Zimmermann, A.,
less attention in recent literature.
and Wagner, S. (2019). From monolith to microser-
vices: A classification of refactoring approaches.
APPENDIX A InInternational Workshop on Software Engineering
Aspects of Continuous Development and New Para-
LIST OF SECONDARY STUDIES
digms of Software Production and Deployment
[SS01] Tighilt, R., Abdellatif, M., Moha, N., Mili, H., (pp.128–141). https://doi.org/10.1007/978-3-030-
Boussaidi, G.E., Privat, J., and Guéhéneuc, Y.G. 06019-0_10.
(2020). On the study of microservices antipatterns:
[SS10] Razzaq, A. (2020). A systematic review on
Acatalog proposal. In Proceedings of the European
software architectures for IoT systems and future
Conference on Pattern Languages of Programs 2020
direction to the adoption of microservices architec-
(pp. 1–13).
ture. SN Computer Science, 1(6), 1–30.
https://doi.org/10.1145/3424771.3424812
https://doi.org/10.1007/s42979020-00359-w.
[SS02] Chávez, K., Cedillo, P., Espinoza, M., and
[SS11] Wang, L., Jiang, Y.X., Wang, Z., Huo, Q.E.,
Saquicela, V. (2019). A systematic literature review on
Dai, J., Xie, S.L., … and Jiang, Z.P. (2022). The oper-
composition of microservices through the use of seman-
ation and maintenance governance of microservices
tic annotations: solutions and techniques. In 2019 Inter-
architecture systems: A systematic literature review.
national Conference on Information Systems and Com-
Journal of Software: Evolution and Process, e2433.
puter Science (INCISCOS) (pp. 311–318).
https://doi.org/0.1002/smr.2433.
https://doi.org/10.1109/INCISCOS49368.2019.00056
[SS12] Jawaddi, S.N.A., Johari, M.H., and Ismail, A.
[SS03] Valdivia, J.A., Limón, X., and Cortes-Ver-
(2022). A review of microservices autoscaling with for-
din, K. (2019). Quality attributes in patterns related to
mal verification perspective. Software: Practice and
microservice architecture: a Systematic Literature Review.
Experience, 52(11), 2476–2495.
In 2019 7th International Conference in Software Engi-
https://doi.org/10.1002/spe.3135.
neering Research and Innovation (CONISOFT)
[SS13] Nguyen, H.X., Zhu, S., and Liu, M. (2022).
(pp.181–190). https://doi.org/10.1109/10.1109/CONI-
A Survey on Graph Neural Networks for Microser-
SOFT.2019.00034
vice-Based Cloud Applications. Sensors, 22(23),
[SS04] Schmidt, R.A. and Thiry, M. (2020, June).
9492. https://doi.org/10.3390/s22239492.
Microservices identification strategies: A review
[SS14] Söylemez, M., Tekinerdogan, B., and
focused on Model Driven Engineering and Domain
Kolukısa Tarhan, A. (2022). Challenges and Solution
Driven Design approaches. In 2020 15th Iberian Con-
Directions of Microservice Architectures: A System-
ference on Information Systems and Technologies
atic Literature Review. Applied Sciences, 12(11), 5507.
(CISTI) (pp. 1–6).
https://doi.org/10.3390/app12115507.
https://doi.org/10.23919/CISTI49556.2020.9141150
[SS15] de Almeida, M.G. and Canedo, E.D.
[SS05] Prasetyo, Y.A. and Suhardi (2018). Micros-
(2022). Authentication and Authorization in Micros-
ervice Platform for Smart City: Concepts, Services
ervices Architecture: A Systematic Literature Review.
and Technology. In 2018 International Conference on
Applied Sciences, 12(6), 3023.
Information Technology Systems and Innovation
https://doi.org/10.3390/app12063023.
(ICITSI) (pp. 358–363).
https://doi.org/10.1109/ICITSI.2018.8695927 [SS16] Berardi, D., Giallorenzo, S., Mauro, J.,
[SS06] Karabey Aksakalli, I., Çelik, T., Can, A.B., Melis, A., Montesi, F., and Prandini, M. (2022).
and Tekinerdogan, B. (2021). Deployment and com- Microservice security: A systematic literature review.
munication patterns in microservice architectures: A PeerJ Computer Science, 8, e779.
systematic literature review. Journal of Systems and https://doi.org/10.7717/peerj-cs.779.
Software, 180, 111014. [SS17] Vera-Rivera, F.H., Gaona, C., and Astudi-
https://doi.org/10.1016/j.jss.2021.111014. llo, H. (2021). Defining and measuring microservice
[SS07] Li, S., Zhang, H., Jia, Z., Zhong, C., granularity–a literature overview. PeerJ Computer
Zhang, C., Shan, Z., … and Babar, M.A. (2021). Science, 7, e695. https://doi.org/10.7717/peerj-cs.695.
Understanding and addressing quality attributes of [SS18] Leines-Vite, L., Pérez-Arriaga, J.C., and
microservices architecture: A Systematic literature Limón, X. (2021). Confidentiality and Integrity
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 819
Mechanisms for Microservices Communication. [SS28] Pereira-Vale, A., Márquez, G., Astudillo, H.,
International Journal of Network Security and Its and Fernandez, E.B. (2019). Security mechanisms
Applications, 13(6), 85–103. used in microservices-based systems: A systematic
https://doi.org/10.5121/ijnsa.2021.13607. mapping. In 2019 XLV Latin American Computing
Conference (CLEI) (pp. 01–10).
[SS19] Osses, F., Márquez, G., and Astudillo, H.
https://doi.org/10.1109/CLEI47609.2019.235060.
(2018). An exploratory study of academic architectural
tactics and patterns in microservices: A systematic lit- [SS29] Alshuqayran, N., Ali, N., and Evans, R.
erature review. Avances en Ingenieria de Software a (2016). A systematic mapping study in microservice
Nivel Iberoamericano, CIbSE, 2018, pp. 71–84. architecture. Proceedings-2016 IEEE 9th Interna-
tional Conference on Service-Oriented Computing
[SS20] Staegemann, D., Volk, M., Shakir, A.,
and Applications, SOCA 2016 pp. 44–51.
Lautenschläger, E., and Turowski, K. (2021). Exam-
https://doi.org/10.1109/SOCA.2016.15.
ining the Interplay Between Big Data and Microser-
vices–A Bibliometric Review. Complex Systems [SS30] Gortney, M.E., Harris, P.E., Cerny, T., Al
Informatics and Modeling Quarterly, (27), pp. 87– Maruf, A., Bures, M., Taibi, D., and Tisnovsky, P.
118. https://doi.org/10.7250/csimq.2021-27.04. (2022). Visualizing Microservice Architecture in the
Dynamic Perspective: A Systematic Mapping Study.
[SS21] Nunes, J.P.K., Bianchi, T., Iwasaki, A.Y.,
IEEE Access, 10, 119999–120012.
and Nakagawa, E.Y. (2021). State of the art on micro-
https://doi.org/10.1109/ACCESS.2022.3221130.
services autoscaling: An overview. Anais do XLVIII
[SS31] Santos, R., Soares, P., Rodrigues, E.,
Seminário Integrado de Software e Hardware, 30-38.
Maia,P.H.M., and Silveira, A. (2022). How Block-
https://doi.org/10.5753/semish.2021.15804.
chain and Microservices are Being Used Together: a
[SS22] Lelovic, L., Mathews, M., Elsayed, A.,
Systematic Mapping Study. In 2022 IEEE/ACM 5th
Cerny, T., Frajtak, K., Tisnovsky, P., and Taibi, D.
International Workshop on Emerging Trends in Soft-
(2022). Architectural languages in the microservice
ware Engineering for Blockchain (WETSEB) (pp. 39–
era: a systematic mapping study. In Proceedings of the
46). https://doi.org/10.1145/3528226.3528371.
Conference on Research in Adaptive and Convergent
[SS32] Niño-Martínez, V.M., Ocharán-Hernán-
Systems (pp. 39–46).
dez, J.O., Limón, X., and Pérez-Arriaga, J.C. (2021,
https://doi.org/10.1145/3538641.3561486.
October). Microservices Deployment: A Systematic
[SS23] Cerny, T., Donahoo, M.J., and Trnka, M. Mapping Study. In 2021 9th International Conference
(2018). Contextual understanding of microservice in Software Engineering Research and Innovation
architecture: Current and future directions. ACM (CONISOFT) (pp. 24–33).
SIGAPP Applied Computing Review, 17(4), 29–45. https://doi.org/10.1109/CONISOFT52520.2021.00016.
https://doi.org/10.1145/3183628.3183631.
[SS33] Waseem, M., Liang, P., and Shahin, M.
[SS24] Wolfart, D., Assunção, W.K., da Silva, I.F., (2020). A systematic mapping study on microservices
Domingos, D.C., Schmeing, E., Villaca, G.L.D., and architecture in DevOps. Journal of Systems and Soft-
Paza, D.D.N. (2021). Modernizing legacy systems ware, 170, 110798.
with microservices: A roadmap. In Evaluation and https://doi.org/10.1016/j.jss.2020.110798.
Assessment in Software Engineering (pp. 149–159).
[SS34] Di Francesco, P., Lago, P., and Malavolta, I.
https://doi.org/10.1145/3463274.3463334.
(2019). Architecting with microservices: A systematic
[SS25] Waseem, M., Liang, P., Márquez, G., and mapping study. Journal of Systems and Software, 150,
Di Salle, A. (2020). Testing microservices architec- 77–97. https://doi.org/10.1016/j.jss.2019.01.001.
ture-based applications: A systematic mapping study. [SS35] Hannousse, A. and Yahiouche, S. (2021).
In 2020 27th Asia-Pacific Software Engineering Con- Securing microservices and microservice architec-
ference (APSEC) (pp. 119–128). tures: A systematic mapping study. Computer Science
https://doi.org/10.1109/APSEC51365.2020.00020. Review, 41, 100415. https://doi.org/10.1016/j.cos-
[SS26] Velepucha, V., and Flores, P. (2021). rev.2021.100415.
Monoliths to microservices-Migration Problems and [SS36] Vural, H., Koyuncu, M., and Guney, S.
Challenges: A SMS. In 2021 Second International (2017). A systematic literature review on microser-
Conference on Information Systems and Software vices. In International Conference on Computational
Technologies (ICI2ST) (pp. 135–142). Science and Its Applications (pp. 203–217).
https://doi.org/10.1109/ICI2ST51859.2021.00027. https://doi.org/10.1007/978-3-319-62407-5_14.
[SS27] Di Francesco, P., Malavolta, I., and Lago, P. [SS37] Taibi, D., Lenarduzzi, V., and Pahl, C.
(2017). Research on architecting microservices: (2019). Continuous architecting with microservices
Trends, focus, and potential for industrial adoption. and DevOps: A systematic mapping study. In Interna-
In2017 IEEE International Conference on Software tional Conference on Cloud Computing and Services
Architecture (ICSA) (pp. 21–30). Science (pp. 126–151). https://doi.org/10.1007/978-
https://doi.org/10.1109/ICSA.2017.24. 3-030-29193-8_7.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

820 STOJANOV et al.
[SS38] Razzaq, A. and Ghayyur, S.A. (2022). A pp.228–235.
systematic mapping study: The new age of software https://doi.org/10.1145/3129676.3129682.
architecture from monolithic to microservice archi- 2. Newman, S., Building Microservices: Designing Fine-
tecture–awareness and challenges. Computer Appli- Grained Systems, Sebastopol, CA: O’Reilly Media,
cations in Engineering Education. 2021.
https://doi.org/10.1002/cae.22586. 3. Dragoni, N., Giallorenzo, S., Lafuente, A.L., Maz-
[SS39] Bushong, V., Abdelfattah, A.S., Maruf, A.A., zara, M., Montesi, F., and Mustafin, R., Safina, L.,
Microservices: Yesterday, today, and tomorrow, in
Das, D., Lehman, A., Jaroszewski, E., … and Bures, M.
Present and Ulterior Software Engineering, Mazzara, M.
(2021). On microservice analysis and architecture
and Meyer, B., Eds., Cham: Springer Int. Publ., 2017,
evolution: A systematic mapping study. Applied Sci-
pp.195–216.
ences, 11(17), 7856.
https://doi.org/10.1007/978-3-319-67425-4_12.
https://doi.org/10.3390/app11177856.
4. Alaasam, A.B., Radchenko, G., and Tchernykh, A.,
[SS40] Ghani, I., Wan-Kadir, W.M., Mustafa, A., Refactoring the monolith workflow into independent
and Babir, M.I. (2019). Microservice testing micro-workflows to support stream processing, Pro-
approaches: A systematic literature review. Interna- gram. Comput. Software, 2021, vol. 47, pp. 591–600.
tional Journal of Integrated Engineering, 11(8), 65– https://doi.org/10.1134/S0361768821080077
80. https://doi.org/10.30880/ijie.2019.11.08.008. 5. Baškarada, S., Nguyen, V., and Koronios, A., Archi-
tecting microservices: Practical opportunities and chal-
[SS41] Velepucha, V., Flores, P., and Torres, J.
lenges, J. Comput. Inf. Syst., 2018, vol. 60, pp. 428–436.
(2019). Migration of monolithic applications towards
https://doi.org/10.1080/08874417.2018.1520056
microservices under the vision of the information hid-
6. Niño-Martínez, V.M., Ocharán-Hernández, J.O.,
ing principle: a systematic mapping study. In the
Limón, X., and Pérez-Arrilaga, J.C., A microservice
International Conference on Advances in Emerging
deployment guide, Program. Comput. Software, 2022,
Trends and Technologies (pp. 90–100).
vol. 48, pp. 632–645.
https://doi.org/10.1007/978-3030-32022-5_9.
https://doi.org/10.1134/S0361768822080151
[SS42] Yu, D., Jin, Y., Zhang, Y., and Zheng, X. 7. Larrucea, X., Santamaria, I., Colomo-Palacios, R.,
(2019). A survey on security issues in services commu- and Ebert, C., Microservices, IEEE Software, 2018,
nication of Microservices-enabled fog applications. vol.35, pp. 96–100.
Concurrency and Computation: Practice and Experi- https://doi.org/10.1109/MS.2018.2141030
ence, 31(22), e4436. 8. Ebert, C., Gallardo, G., Hernantes, J., and Serrano, N.,
https://doi.org/10.1002/cpe.4436. DevOps, IEEE Software, 2016, vol. 33, pp. 4–100.
[SS43] Pahl, C. and Jamshidi, P. (2016). Microser- 9. Bosch, J., Continuous Software Engineering, Cham:
vices: A Systematic Mapping Study. In the 6th Inter- Springer Int. Publ., 2014.
national Conference on Cloud Computing and Ser- 10. Kitchenham, B., Procedures for performing systematic
vices Science (CLOSER 2016) CLOSER (1), 137– review, Technical Report, Keele: Keele Univ., Depart-
146. ment of Computer Science, Software Engineering
Group, 2004, no. TR/SE-0401.
[SS44] Parker, G., Kim, S., Al Maruf, A., Cerny, T.,
Frajtak, K., Tisnovsky, P., and Taibi, D. (2023). Visu- 11. Petersen, K., Feldt, R., Mujtaba, S., and Mattsson, M.,
Systematic mapping studies in software engineering,
alizing Anti-Patterns in Microservices at Runtime: A
Proc. 12th Int. Conf. on Evaluation and Assessment in
Systematic Mapping Study. IEEE Access, 11, 4434–
Software Engineering, Bari, 2008, pp. 68–77.
4442.
12. Petersen, K., Vakkalanka, S., and Kuzniarz, L., Guide-
https://doi.org/10.1109/ACCESS.2023.3236165.
lines for conducting systematic mapping studies in soft-
ware engineering: an update, Inf. Software Technol.,
2015, vol. 64, pp. 1–8.
FUNDING
https://doi.org/10.1016/j.infsof.2015.03.007
This work was supported by ongoing institutional fund-
13. Kitchenham, B., Budgen, D., and Brereton, P., Evi-
ing. No additional grants to carry out or direct this particu- dence-Based Software Engineering and Systematic Re-
lar research were obtained. views, Boca Raton, FL: CRC Press, 2016.
14. Garousi, V., Felderer, M., and Mäntylä, M.V., Guide-
lines for including grey literature and conducting mul-
CONFLICT OF INTEREST
tivocal literature reviews in software engineering, Inf.
The authors declare that they have no conflicts of interest. Software Technol., 2019, vol. 106, pp. 101–121.
https://doi.org/10.1016/j.infsof.2018.09.006
15. Bruce, M. and Pereira, P.A., Microservices in Action,
REFERENCES
Shelter Island, NY: Manning Publ., 2019.
1. Cerny, T., Donahoo, M.J., and Pechanec, J., Disam- 16. Abdellatif, M., Shatnawi, A., Mili, H., Moha, N., El
biguation and comparison of SOA, microservices and Boussaidi, G., Hecht, G., Privat, J., and Guéhé-
self-contained systems, Proc. Int. Conf. on Research in neuc,Y.-G., A taxonomy of service identification ap-
Adaptive and Convergent Systems, Krakow, 2017, proaches for legacy software systems modernization, J.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023

A TERTIARY STUDY ON MICROSERVICES 821
Syst. Software, 2021, vol. 173, p. 110868. 27. Tran, H.K.V., Unterkalmsteiner, M., Börstler, J., and
https://doi.org/10.1016/j.jss.2020.110868 bin Ali, N., Assessing test artifact quality–a tertiary
study, Inf. Software Technol., 2021, vol. 139, p. 106620.
17. Henry, A. and Ridene, Y., Migrating to microservices,
https://doi.org/10.1016/j.infsof.2021.106620
in Microservices: Science and Engineering, Bucchiarone, A.,
Dragoni, N., Dustdar, S., Lago, P., Mazzara, M., Ri- 28. Liu, X., Li, S., Zhang, H., Zhong, C., Wang, Y.,
vera, V., and Sadovykh, A., Eds., Cham: Springer Int. Waseem, M., and Babar, M.A., Research on microser-
Publ., 2020, pp. 45–72. vice architecture: A tertiary study, SSRN Electron. J.,
https://doi.org/10.1007/978-3-030-31646-4_3 2022
https://doi.org/10.2139/ssrn.4204345
18. Stojanov, A. and Stojanov, Z., Review of methods for
migrating software systems to microservices architec- 29. Costa, D.I.C., Filho, E.P. e S., da Silva, R.F., Quares-
ture, J. Eng. Manag. Competitiveness, 2021, vol. 11, ma Gama, T.D. de C., and Cortés, M.I., Microservice
pp.152–162. architecture: a tertiary study, Proc. 14th Brazilian Symp.
on Software Components, Architectures, and Reuse, Na-
19. Valdivia, J.A., Lora-González, J., Limón, X., Cortes- tal, 2020, pp. 61–70.
Verdin, K., and Ocharán-Hernández, J.O., Patterns re- https://doi.org/10.1145/3425269.3425277
lated to microservice architecture: a multivocal litera-
30. Wohlin, C., Guidelines for snowballing in systematic
ture review, Program. Comput. Software, 2020, vol. 46,
literature studies and a replication in software engineer-
pp. 594–608.
ing, Proc. 18th Int. Conf. on Evaluation and Assessment in
https://doi.org/10.1134/S0361768820080253
Software Engineering, London, 2014, pp. 38:1–38:10.
20. Abdelfattah, A.S. and Cerny, T., Roadmap to reasoning https://doi.org/10.1145/2601248.2601268
in microservice systems: a rapid review, Appl. Sci.,
31. Zhou, X., Jin, Y., Zhang, H., Li, S., and Huang, X., A
2023, vol. 13, p. 1838.
Mmap of threats to validity of systematic literature re-
https://doi.org/10.3390/app13031838
views in software engineering, Proc. 23rd Asia–Pacific
21. Alaasam, A.B., Radchenko, G., Tchernykh, A., and Software Engineering Conf. (APSEC), Hamilton, 2016,
González Compeán, J.L., Analytic study of container- pp. 153–160.
izing stateful stream processing as microservice to sup- https://doi.org/10.1109/APSEC.2016.031
port digital twins in fog computing, Program. Comput.
32. Bryant, A. and Charmaz, K., The SAGE Handbook of
Software, 2020, vol. 46, pp. 511–525.
Current Developments in Grounded Theory, Thousand
22. Arvanitou, E.M., Ampatzoglou, A., Bibi, S., Chatzi- Oaks, CA: SAGE Publ., 2019.
georgiou, A., and Deligiannis, I., Applying and re-
33. Thomas, D.R., A general inductive approach for ana-
searching DevOps: A tertiary study, IEEE Access, 2022,
lyzing qualitative evaluation data, Am. J. Eval., 2006,
vol. 10, pp. 61585–61600.
vol. 27, pp. 237–246.
https://doi.org/10.1109/ACCESS.2022.3171803
https://doi.org/10.1177/1098214005283748
23. Cadavid, H., Andrikopoulos, V., and Avgeriou, P., Ar-
34. Braun, V. and Clarke, V., Using thematic analysis in
chitecting systems of systems: A tertiary study, Inf. Soft-
psychology, Qual. Res. Psychol., 2006, vol. 3, pp. 77–
ware Technol., 2020, vol. 118, p. 106202. 101.
https://doi.org/10.1016/j.infsof.2019.106202 https://doi.org/10.1191/1478088706qp063oa
24. Delavari, V., Shaban, E., Janssen, M., and Hassanza- 35. Goh, K.T. and Pentland, B.T., From actions to paths to
deh, A., Thematic mapping of cloud computing based patterning: Toward a dynamic theory of patterning in
on a systematic review: a tertiary study, J. Enterpr. Inf. routines, Acad. Manag. J., 2019, vol. 62, pp. 1901–
Manag., 2019, vol. 33, pp. 161–190. 1929.
https://doi.org/10.1108/JEIM-02-2019-0034
36. Sjøberg, D.I.K., Dyba, T., Anda, B.C.D., and Hannay, J.E.,
25. Hoda, R., Salleh, N., Grundy, J., and Tee, H.M., Sys- Building theories in software engineering, in Guide to
tematic literature reviews in agile software develop- Advanced Empirical Software Engineering, Shull, F.,
ment: A tertiary study, Inf. Software Technol., 2017, Singer, J., and Sjøberg, D.I.K., Eds., London: Spring-
vol.85, pp. 60–70. er, 2008, pp. 312–336.
https://doi.org/10.1016/j.infsof.2017.01.007 https://doi.org/10.1007/978-1-84800-044-5_12.
26. Raatikainen, M., Tiihonen, J., and Männistö, T., Soft-
ware product lines and variability modeling: A tertiary Publisher’s Note. Pleiades Publishing remains
study, J. Syst. Software, 2019, vol. 149, pp. 485–510. neutral with regard to jurisdictional claims in
https://doi.org/10.1016/j.jss.2018.12.027 published maps and institutional affiliations.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 49 No. 8 2023