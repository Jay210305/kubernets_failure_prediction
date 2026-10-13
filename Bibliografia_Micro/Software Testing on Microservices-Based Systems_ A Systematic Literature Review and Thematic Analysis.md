ISSN 0361-7688, Programming and Computer Software, 2025, Vol. 51, No. 8, pp. 548–578. © Pleiades Publishing, Ltd., 2025.
Software Testing on Microservices-Based Systems:
A Systematic Literature Review and Thematic Analysis
Sebastián Bello-Trejoa,* (ORCID: 0009-0000-0249-5527), Xavier Limóna,** (ORCID: 0000-0003-4654-636X),
Jorge Octavio Ocharán-Hernándeza,*** (ORCID: 0000-0002-2598-1445),
and Lizbeth A. Hernández-González a,**** (ORCID: 0000-0002-8524-3209)
a Facultad de Estadística e Informática, Universidad Veracruzana, Xalapa, Veracruz, México
*e-mail: sebastianbello.trejo@gmail.com
**e-mail: hlimon@uv.mx
***e-mail: jocharan@uv.mx
****e-mail: lizhernandez@uv.mx
Received August 17, 2025; revised August 27, 2025; accepted August 27, 2025
Abstract—Microservice architecture (MSA) has emerged as a significant software architecture in both indus-
try and academia, garnering attention as a key research area. MSA offers numerous benefits, such as facilitat-
ing independent development, testing, and system deployment. However, its distributed characteristics intro-
duce various challenges. Testing microservices presents diverse challenges derived from complex dependen-
cies, diverse execution environments, and different development teams, which lessen the effectiveness of
conventional testing methods. Through a systematic literature review, we aim to present an overview of vari-
ous testing strategies, testing tools, innovative testing solutions, and associated challenges. Our research
includes academic resources from IEEE Xplore, ACM Digital Library, ScienceDirect, SpringerLink, and
Wiley Online Library. From this research, we identified 76 primary studies, which we analyzed through the-
matic synthesis. Our analysis yielded 16 distinct testing strategies for microservices-based systems, accompa-
nied by 19 distinct categories of proposed solutions for microservices testing. Furthermore, we compiled a
total of 95 relevant tools for testing microservices. We also documented 22 distinct categories of challenges
specific to testing microservices-based systems, including but not limited to automated testing, performance
evaluation, and the creation of MSA-based testing environments. This study aims to serve as a resource for
software engineering professionals and researchers interested in microservices testing.
Keywords: microservices, software testing, testing strategies, testing tools, challenges, systematic review
DOI: 10.1134/S0361768825700422
1. INTRODUCTION and communicate with each other through lightweight
mechanisms [2]. This architecture encompasses tech-
This paper is an extension of a study initially pre-
nological heterogeneity, fault handling, functional
sented at the 12th International Conference on Soft-
degradation, gradual scaling, and autonomous
ware Engineering Research and Innovation (CONI-
deployment, further extending the benefits of distrib-
SOFT 2024) [1]. The original study conducted a Sys-
uted computing [3]. As a result of these benefits, com-
tematic Literature Review on software testing for
panies such as Amazon, LinkedIn, Netflix, Uber, and
microservices-based systems. In this extended work,
Verizon have embraced microservices in developing
we enhanced our initial analysis by applying thematic
their products and services [4].
synthesis to explore further and analyze information
related to software testing for microservices-based sys- The microservices architecture is a global trend, as
tems, considering the development aspects of this kind shown in a 2021 study by the business intelligence
of system. This extended study encompasses a broader platform Statista [5], which targets developers and
selection of primary studies and provides a signifi- security professionals worldwide. The study revealed
cantly expanded discussion regarding the methodolo- that 37% of the participants already use microservices
gies followed and the obtained results. in their systems. The emergence of microservices
The microservices architecture (MSA) is an archi- architecture in the industry is driven by organizations’
tectural style for developing applications through a technical debt accumulation, overcoming limitations
collection of small, independent services known as related to practices such as continuous integration
microservices. These services operate independently (CI), dissatisfaction in the industry with the capabili-
548

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 549
ties of service-oriented architecture (SOA), the rise of the systematic literature review. The outcomes
key trends like domain-driven design (DDD), and its obtained from the research method are detailed in
compatibility with agile development principles and Section 4, followed by a discussion in Section 5. Sec-
DevOps practices [6–8]. Similar to the industry, aca- tion 6 discusses potential threats to the validity of this
demia is gaining a growing interest in microservices study. Lastly, Section 7 presents the conclusions
[8,9]. This academic interest is attributed, among derived from this research.
other factors, to the challenges encountered in design-
ing, monitoring, and testing microservices [10].
2. RELATED WORK
Software testing, along with its related activities,
aims to demonstrate that a program performs as spec- The emergence of the microservices architecture
ified and identifies its defects before deployment [11]. (MSA) has impacted the development of contempo-
Moreover, software testing is a necessary activity that rary distributed software systems. All components in
covers all the steps of any software development lifecy- this architectural style, or microservices, are cohesive,
cle [12]. In this context, the verification and validation independent processes that communicate through
of microservices-based systems are as important as in message exchanges. Each microservice is designed for
any other kind of system, particularly considering that a specific functionality, allowing teams to deploy and
traditional manual testing methods are insufficient to operate it independently [18]. Communication among
fully meet the requirements of microservices due to microservices through message exchanges is one of the
the heterogeneity of execution environments and characteristics of MSA. This architectural style
complex dependencies between services [13–15]. enables development teams to deploy and operate
Inaddition, Li et al. [16] also note that the cost of ver- microservices independently, helping to achieve scal-
ifying microservices-based systems using traditional ability and maintainability, among other key quality
methods is high. The authors further add that since attributes for distributed software systems.
communication between microservices often occurs
On the other hand, MSA has also introduced new
over the network, it is easy to encounter unstable
challenges in distributed software testing due to its dis-
results. Lastly, Duan et al. [17] emphasize that
tinctive characteristics. Coordinating multiple micro-
research on microservices-oriented testing processes is
services, handling asynchronous communication, and
still relatively new, stressing the importance of collect-
managing distributed states within the system compli-
ing and analyzing existing proposals to address these
cate effective testing approaches and strategies. Recent
challenges effectively.
systematic reviews have analyzed the testing
Given the growing interest and challenges associ-
approaches employed in this architectural style to
ated with testing microservices-based systems, the
understand current challenges and techniques while
objective of this paper is to present documented cases
evaluating their impact on system quality.
from academic literature regarding testing oriented
toward microservices-based systems through the con- Few systematic reviews have explored software
duct of a systematic literature review (SLR) with the testing in microservices-based systems. Ghani et al.
following specific objectives: [19] conducted a systematic literature review (SLR)
covering studies published between 2010 and 2018,
• Analyze types of software testing applicable to
focusing on classifying testing approaches for micros-
microservices-based systems and their application
ervices and analyzing their alignment with quality
contexts.
attributes. Their review highlighted that most micros-
• Analyze proposals aimed at the testing process
ervice testing solutions still build heavily on existing
applied in microservices-based systems.
frameworks, tools, and unit testing practices. The
• Identify tools used to test microservices-based major influences on testing solutions identified were
systems. security, performance, traceability, compatibility,
• Analyze the current challenges associated with complexity, effectiveness, and scalability. Their
testing microservices-based systems. descriptive analysis offered limited empirical valida-
Our research holds significant value as it contrib- tion of the proposed solutions. Ghani et al. [19] also
utes to practitioners and researchers interested in test- pointed to an important gap: the need for broader,
ing microservices-based systems. By identifying suit- more automated testing strategies that can operate
able tests for the requirements and constraints inher- across multiple testing levels.
ent to the microservices architecture, along with Building on this groundwork, Waseem et al. [20]
proposed solutions, available tools, and emerging conducted a systematic mapping study (SMS) to ana-
challenges, this research not only has the potential to lyze trends, research themes, approaches, tools, and
drive new lines of research but also to enhance testing challenges in testing microservices-based systems,
activities in the microservices development process. selecting papers from 2015 to 2019. Their study used
This paper is structured as follows: Section 2 pro- thematic analysis and open coding to organize testing
vides an overview of related work. Section 3 delineates practices. Integration and unit testing were the most
the research methodology employed for conducting commonly used approaches. They also observed a
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

550 BELLO-TREJO et al.
growing interest in challenges related to automated 76 primary studies, identifying 16 types of testing, ana-
testing and inter-service communication. Despite the lyzing 95 tools, and documenting 22 categories of
variety of novel testing approaches proposed, most challenges. In addition, we examine application con-
had not yet been validated on real-world microser- texts, automation trends, and gaps in empirical valida-
vices-based applications, and the lack of dedicated tion, providing a broader and integrated view of how
testing tools remained a notable gap, one that is now testing practices support microservices-based systems.
thoroughly addressed in our review. Moreover, the
study included only a limited empirical evaluation of
the effectiveness of these practices in real-world sce- 3. RESEARCH METHOD AND EXECUTION
narios.
The research method used for conducting the sys-
More recently, Miao et al. [21] conducted another tematic literature review (SLR) is based on the guide-
SMS covering 2015 to 2024, specifically focusing on lines proposed by [24]. According to the authors, a
test-generation techniques for microservices. Their systematic review in the context of software engineer-
study used thematic categorization and gap analysis to ing is a secondary study whose objective is to search for
study the challenges and practices in this area. Their and identify all relevant material related to a given
study explored contract testing, behavior-driven topic. We have chosen this method because it is well-
development, and automated regression testing in suited for software engineering topics. Furthermore, it
microservices, but also stressed the lack of dedicated is a widely respected methodology for secondary stud-
tools for automated test generation. While their study ies in this field.
provides valuable insights into emerging practices and
To enhance the stages of our research, we also inte-
the need for more adaptive testing approaches, it
grated methodologies referenced in [25] to strengthen
focuses on specific aspects of test generation, whereas
the automatic search procedure. We also leveraged the
our study has a broader scope. Furthermore, empirical
snowballing technique advocated by [26] to broaden
validation of the techniques remains limited, and the
our selection of primary studies. Finally, we followed
study did not include a formal quality assessment of
the approach outlined in [27] to categorize the infor-
the selected works.
mation discovered through thematic analysis and syn-
Other studies have examined aspects related to thesis.
testing in microservices-based systems. Silva et al. [22]
To outline the methodology systematically and
conducted a multivocal literature review (MLR) based
comprehensively, we detail the corresponding ele-
on Garousi’s guidelines, integrating white and grey lit-
ments and their execution. This section is further seg-
erature from ACM Digital Library, Scopus, Google,
mented into the following subsections: search process,
and StackOverflow. Their work synthesized 117 faults
selection process, snowballing process, evaluation of
associated with microservices applications, catego-
study quality, data extraction process, and data syn-
rized across six non-functional requirements and
thesis.
eleven architectural characteristics. The authors com-
piled a detailed catalog of faults in microservices, but
their study focuses primarily on documenting these
3.1. Search Process
faults without analyzing the testing techniques that
could address them or evaluating their effectiveness. The initial step in the search process involves defin-
On the other hand, our study tries explicitly to address ing the research questions (RQs). These RQs serve as
those limitations. the foundation of the research, as the primary goal is
to address these questions. Table 1 displays the
Complementarily, Li et al. [23] performed an SLR
research questions (RQs) alongside our research moti-
covering publications from 2015 to 2018, investigating
vations for addressing them.
quality attributes of microservices-based systems:
scalability, performance, availability, monitorability, 3.1.1. Search Strategy. For this research, we
security, and testability. While exploring several tactics employed the systematic approach suggested by Zhang
to achieve quality attributes, they do not examine how et al. [25] to develop search strategies, thereby enhanc-
specific testing strategies contribute to improving ing the rigor of systematic review search processes.
them. These studies provide helpful background for The proposed method consists of five steps, as illus-
understanding faults and quality concerns in micros- trated in Fig. 1. We present the execution of each of
ervices-based systems, but neither directly evaluates these steps below.
the role of testing practices, unlike our present study.
(1) Identifying related conferences, journals, and
Previous systematic reviews have categorized test- search engines: We manually searched for conferences
ing approaches and explored challenges in microser- and journals related to microservices testing for the
vices-based systems. However, they have not system- initial step. As we did not find specialized conferences
atically analyzed the types of tests, tools, proposals, or journals on the topic, we focused on resources that
and challenges to system quality attributes. Our study cover a wide range of conference proceedings and
addresses these gaps through a thematic synthesis of journals [24] that are recognized as reliable sources in
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 551
Table 1. Research questions specific instance, considering that the sample has
already yielded satisfactory results.
RQ Motivations
(3) Eliciting search strings: We employed an objec-
RQ-1. What software We believe that identifying test- tive approach to elicit search terms, aiming to obtain
tests are dedicated to sys- ing strategies and proposing relevant search terms through text mining [25].
tems based on MSA, and solutions for MSA can enhance Weanalyzed the titles and abstracts of the QGS stud-
in what contexts are they software quality and benefit ies to extract relevant search terms. Figure 2 shows the
applied? researchers and professionals. frequency of search terms we found. Based on the rel-
evant terms identified, we designed the search strings.
RQ-2. How does exist- Identifying proposals in the lit-
ing literature suggest erature focused on testing for (4) Conducting automated searches: In this step,
we applied the search strings to the selected digital
approaching the testing MSA would provide valuable
libraries. Table 4 presents the evaluated search strings
process for MSA-based information to researchers and
used.
systems? software engineering practi-
(5) Evaluating search performance: We tested each
tioners interested in microser-
search string based on the Recall and Precision met-
vices development.
rics to assess its performance. Recall is the percentage
RQ-3. What are the tools Since it is crucial to have the
of relevant studies (RS) obtained using the search
used to test MSA-based highest possible level of confi-
string divided by the total number of all studies (AS) in
systems? dence during the testing phase the QGS. Precision, on the other hand, is the percent-
[2], implementing software tools age of relevant studies obtained through the execution
becomes necessary. Therefore, it of the search string divided by all studies (relevant or
is essential to identify tools that not) retrieved prior to executing the search string.
are useful for MSA. Equations (1) and (2) formally define these metrics,
respectively.
RQ-4. What are the chal- Analyzing the current state of
lenges associated with the research, especially the most Recall = RS/AS of QGS , (1)
testing of MSA-based immediate challenges related to
Precision = RS/AS. (2)
systems? MSA, will help identify future
research directions. Additionally, Zhang et al. [25] note that any string
with sensitivity greater than or equal to 80% is suitable
for proceeding to the selection process. The evaluation
Table 2. Selected search engines results are presented in Table 5, showing that the
selected search string SS-3 exhibited the best results in
Search engine URL
both metrics.
SE-1 ACM Digital Library https://dl.acm.org
SE-2 IEEE Xplore https://ieeexplore.ieee.org 3.2. Selection Process
SE-3 Springer Link https://link.springer.com Once we have identified the candidate studies
SE-4 Science Direct https://link.springer.com through the search process, it is necessary to verify
their relevance to the RQs addressed in the review.
SE-5 Wiley Online Library https://onlinelibrary.wiley.com
Toachieve this, we applied a set of selection criteria to
aid in the identification of studies that provide relevant
evidence for the RQs [24].
software engineering [25]. Based on this criterion, we
selected the search engines listed in Table 2. We deliberately excluded studies that primarily
focused on root cause analysis (RCA) testing for
(2) Establishing the quasi-gold standard: The microservices or similar performance-related testing
approach by Zhang et al. [25] follows the concept of studies. This is due to the extensive representation of
the quasi-gold standard (QGS), which is a set of well- these investigations in our initial collection of primary
known studies from conferences and journals. studies. The wealth of information on RCA testing was
Toestablish the QGS, we manually reviewed the found to be proportionate to the rest of the informa-
works gathered from the research venues, which we tion on microservices testing. Thus, we aimed to pre-
identified in the previous step. We examined the title, vent RCA findings from overshadowing the broader
abstract, and keywords and fully analyzed the texts of study focus at this stage. While we intend to conduct
each work. This initial effort led us to identify eight dedicated research on this topic in the future, this
studies related to the research subject, as displayed in exclusion does not entail omitting any other forms of
Table 3. It is important to note that although the sam- research related to microservices performance in this
ple size may be perceived as small, we believe it is rep- review. The selection criteria are shown in Table 6.
resentative as it addresses all the research questions. Once we have established the inclusion and exclu-
Therefore, we deliberately limited our efforts to this sion criteria, the next step is to define the primary
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

552 BELLO-TREJO et al.
Approach
Automatic
Challenge
Complexity
Difficulty
Dynatic
Formal
Framework
Manual
Method
Methodology
Performance
Approach
Quality
Regression
Reliability
Scalability
Static
Strategy
Technology
Tool
Traditional
Verification
0
Fig. 2. Results from the objective elicitation of search
terms.
observed that 12 studies were added to our selection,
bringing the total number of primary studies consid-
ered for thematic synthesis to 76.
N
3.4. Evaluation of Study Quality
In addition to defining and applying inclusion and
Y
exclusion criteria to select relevant studies from a pool
of candidates, it is also important to establish and
implement criteria to assess the quality of the selected
primary studies [24]. Therefore, we designed a quanti-
tative tool to evaluate the quality of the primary studies
Fig. 1. Systematic literature search process. Adapted from
[25]. selected in the initial selection process. We based the
eight evaluation criteria on the work of Meckenstock
[29], whose proposal is built upon the works of Kitch-
study selection process, a systematic process divided enham et al. [30], Rohunen et al. [31], Usman et al.
into stages, each with a specific scope encompassing [32], as well as Dybå and Dingsøyr [33]. We present
various selection criteria. This breakdown is illustrated the criteria used for evaluating the quality of each pri-
in Fig. 3, followed by the results of this selection pro- mary study in Table 7; furthermore, Table 8 shows the
cess displayed in Fig. 4. We present the results from the traceability between the references and the evaluation
selection process following the notation from RepOrt- criteria.
ing standards for Systematic evidence syntheses, better
The evaluation results reveal that 34% of the stud-
known as ROSES [28].
ies achieved the highest rating of 8, while 46% attained
a rating of 7. The remaining studies (20%) only met
five of the eight established criteria.
3.3. Snowballing Process
To broaden our research selection, we imple-
mented the search approach proposed by [26], known 3.5. Data Extraction
as snowballing. This method involves using an article’s
Considering the examples suggested by Kitchen-
references or citations to identify other articles. The
ham et al. [24], we designed our template for extract-
utilization of references and citations is referred to as
backward snowballing. Since our research does not
consider studies published after 2024 and involves
analyzing the citations of the selected primary studies,
we chose to solely use the backward snowballing
approach.
Figure 5 illustrates the result of the selection pro-
cess adapted to backward snowballing. It can be
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025
smetI
Distribution of keywords (% of cases)
7 14 21 28 35 42 49 56 63
% of cases
Fig. 3. Selection process stages considering each criterion.

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 553
Table 3. Selected studies to establish the quasi-gold stan- ing data from the primary studies. The template
dard includes fields to capture general information and
more specific fields to gather data by RQ. Table 9 dis-
Reference
plays the fields of the data extraction form.
Camilli, M., Guerriero, A., Janes, A., Russo, B., y Russo, S.
To collect bibliographic information from the pri-
(2022). Microservices integrated performance and reliabil-
mary studies, we used Zotero version 7.0.11, while we
ity testing. Proceedings of the 3rd ACM/IEEE Interna-
employed MAXQDA Analytics Pro 2020 version
tional Conference on Automation.
20.2.1 to capture related information. We also used
Ding, H., Cheng, L., and Li, Q. (2020). An Automatic MAXQDA to conduct the synthesis method.
Test Data Generation Method for Microservice Applica-
tion. 2020 International Conference on Computer Engi-
3.6. Data Synthesis
neering and Application (ICCEA), 188–191.
Initially, we applied the narrative synthesis method
Duan, T., Li, D., Xuan, J., Du, F., Li, J., Du, J., y Wu, S.
with the support of the guide published by Rodgers
(2021). Design and Implementation of Intelligent Auto-
etal. [34], based on the research of Popay et al. [35].
mated Testing of Microservice Application. 2021 IEEE 5th
However, to improve the findings analysis and
Information Technology,Networking,Electronic and
strengthen our synthesis process, we decided to switch
Automation Control Conference
to the thematic synthesis method, which provides a
Elsner, D., Bertagnolli, D., Pretschner, A., y Klaus, R. more detailed presentation of research findings.
(2022). Challenges in regression test selection for end-to-
We adopted the flexible approach proposed by
end testing of microservice-based software systems. Pro-
Cruzes and Dybå [27] for thematic synthesis in Soft-
ceedings of the 3rd ACM/IEEE International Conference ware Engineering. A research synthesis is a collection
on Automation of Software Test, 1–5. of methods that summarize, integrate, combine, and
Gong, J., y Cai, L. (2023). Analysis for Microservice compare studies on a research topic or question. On
Architecture Application Quality Model and Testing the other hand, thematic analysis is a method
Method. 2023 26th ACIS International Winter Conference designed to identify, analyze, and represent patterns
(themes) within the data. This approach organizes and
on Software Engineering, Artificial Intelligence, Network-
provides a detailed description of the dataset, aiding in
ing and Parallel/Distributed Computing (SNPD- Winter),
interpreting the different aspects related to the
141–145.
research topic [27]. Figure 6 depicts the steps outlined
Li, H., Wang, J., Dai, H., y Lv, B. (2020). Research on
by the authors for conducting thematic synthesis.
Microservice Application Testing System. 2020 IEEE 3rd
The first step outlined by the authors is data
International Conference on Information Systems and
extraction, for which they suggest conducting a pre-
Computer Aided Education (ICISCAE), 363–368.
liminary reading of the selected primary studies. This
Meng, X., Duan, X., Tao, W., Luan, Y., Zhang, J., y Wu, D. process aids in becoming familiar with the subject of
(2021). Modeling and verification of Industrial Microser- study and developing a deeper understanding of the
vice Architecture Based on Formal Methods. 2021 China topic. The authors’ recommendations for data
Automation Congress (CAC), 3776–3780. extraction closely align with our extraction instru-
ment, recording publication details or bibliographic
Wu, C.-F., Ma, S.-P., Shau, A.-C., y Yeh, H.-W. (2022).
information, contextual descriptions, and findings.
Testing for Event-Driven Microservices Based on Con-
Inour case, this includes explicit information related
sumer-Driven Contracts and State Models. 2022 29th
to the research questions.
Asia-Pacific Software Engineering Conference (APSEC),
The next step involves identifying text segments
467–471.
and marking codes. Codes are descriptive labels
applied to segments of text in each study. Coding is the
process of examining and organizing the data within
Table 4. Evaluated search strings
each study of the systematic review. It goes beyond
ID Search string mere labeling; coding necessitates a clear understand-
ing of the context in which the findings are made. It is
SS-1 ((microservice* OR micro service* OR micro-ser-
basically identifying one or more text passages that
vice* OR microservices architect* OR microser-
exemplify the same theoretical or descriptive idea.
vices design) AND test*)
In our case, we adopted the inductive method to
SS-2 ((microservice* OR micro service* OR micro-ser-
identify codes within text segments. Data is meticu-
vice* OR “microservice? architect*”) AND (test*
lously reviewed line by line, and as a concept becomes
OR verification)) evident, it is assigned a code. Upon further data exam-
SS-3 ((microservice* OR “microservice? architect*”) ination, the analyst continues to allocate codes that
AND (test* OR verification OR validation)) mirror emerging concepts, highlighting and coding
lines, paragraphs, or segments that illustrate the cho-
SS-4 (microservice AND architect* AND test*)
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

| 554 |     |     | BELLO-TREJO et al. |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- |
sen concept. To determine if a code has been correctly Table 5. Evaluation of search strings. A bigger recall and
| assigned, the analyst compares text segments with oth- |     |     |     | precision are better |     |     |
| ------------------------------------------------------ | --- | --- | --- | -------------------- | --- | --- |
ers already assigned the same code and decides if they
|     |     |     |     | Search string ID | Recall | Precision |
| --- | --- | --- | --- | ---------------- | ------ | --------- |
reflect the same concept. This process fine-tunes the
dimensions of existing codes and identifies new codes. SS-1 0.875 0.006
To streamline this process, we employed MAXQDA
|     |     |     |     | SS-2 | 1   | 0.006 |
| --- | --- | --- | --- | ---- | --- | ----- |
Analytics Pro 2020, which provides a range of features
|     |     |     |     | SS-3 | 1   | 0.013 |
| --- | --- | --- | --- | ---- | --- | ----- |
for qualitative data analysis.
|            |                 |              |             | SS-4 | 0.875 | 0.017 |
| ---------- | --------------- | ------------ | ----------- | ---- | ----- | ----- |
| The  next  | step  involves  | translating  | codes  into |      |       |       |
themes. A theme is the result of coding, categorizing,
and analytical reflection, not something that is coded.
Translating codes into themes involves considering Table 6. Selection criteria
how different codes can be combined to form a general Inclusion Criteria Exclusion Criteria
theme. Typically, around 15 to 20 themes are created
|     |     |     |     | IC-1: Only studies written  | EC-1: Studies to which we  |     |
| --- | --- | --- | --- | --------------------------- | -------------------------- | --- |
to group all the codes [27]. This is not a direct process
because, as the codes are analyzed, some of the initial in English are collected and  do not have access are
|     |     |     |     | analyzed. | excluded. |     |
| --- | --- | --- | --- | --------- | --------- | --- |
iteration may be incorporated by other codes, edited,
or eliminated. As the translation into themes pro- IC-2: Only studies pub- EC-2: Only research studies
gresses, the coded data may be reorganized and reclas- lished between 2018 and  accepted in conference pro-
sified into different codes or even new ones. The end
|     |     |     |     | 2024 are considered. | ceedings and journals are  |     |
| --- | --- | --- | --- | -------------------- | -------------------------- | --- |
of the process occurs when theme saturation occurs.
considered, excluding any
| The  final  | step  entails  | specifying  | higher-order |     |     |     |
| ----------- | -------------- | ----------- | ------------ | --- | --- | --- |
other type of study.
themes. Essentially, the themes that emerged in the IC-3: The title or keywords  EC-3: Duplicate or repeated
previous steps can now be further explored and inter-
|     |     |     |     | specified by the study  | studies are discarded. |     |
| --- | --- | --- | --- | ----------------------- | ---------------------- | --- |
preted to create a coherent model of higher-order
authors include at least one
themes and the relationships between them. The aim
term related to testing for
is to revisit the original research questions and the the-
MSA-based systems.
oretical interests that relate to them and address them
with arguments based on the themes that emerged IC-4: The study abstract  EC-4: Studies focused on
during the exploration of the texts. shows signs of addressing at  RCA or similar experiments
The  final  outcome  of  this  step  may  include  a least one research question are discarded.
IC-5: After a thorough read-
description of higher-order themes, a taxonomy, a
model, or a theory. To achieve this, we designed a the- ing of the study, it is con-
matic map that facilitates traceability between the RQs firmed that it answers at
and the themes derived from the codes. As part of the
least one research question.
results, we will present the thematic map along with
the findings of the thematic synthesis.
Table 7. Criteria for assessing study quality
4. RESULTS
|     |     |     |     | ID  | Criteria | Reference |
| --- | --- | --- | --- | --- | -------- | --------- |
After conducting the methodology, we obtained a
total of 76 primary studies. This section presents the
|     |     |     |     | QC-1 Theoretical foundation |     | CR-1 |
| --- | --- | --- | --- | --------------------------- | --- | ---- |
results derived from the identified primary studies.
These outcomes encompass responses to RQs and a QC-2 Data collection, analysis, and  CR-2 CR-3
thematic map that synthesizes all data gathered in this
reporting
study. Additionally, the primary studies identified are
detailed in Table 10 for reference, each referenced by QC-3 Limitations and threats to validity CR-4
their identifier in the format PS-XX, where “PS”
denotes “Primary Study”. Figure 7 illustrates the dis- QC-4 References CR-4
tribution of studies published per year, showing an
increase in academia’s interest in exploring testing in QC-5 Research objectives CR-1
microservices and related issues. The latest year marks
the most prolific period of research on this subject. QC-6 Credibility and reporting of findings CR-1
On the other hand, Fig. 8 illustrates the distribu-
|     |     |     |     | QC-7 Study consistency |     | CR-1 |
| --- | --- | --- | --- | ---------------------- | --- | ---- |
tion of primary studies based on the search engine
| used.  IEEE  | Xplore  is  the  | most  productive  | search |                                    |     |      |
| ------------ | ---------------- | ----------------- | ------ | ---------------------------------- | --- | ---- |
|              |                  |                   |        | QC-8 Contribution to knowledge or  |     | CR-1 |
engine, contributing 49 primary studies, followed by
understanding
ACM Digital Library with 20 studies. The disparity
|     |     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |  Vol. 51  |  No. 8   2025 |
| --- | --- | --- | ---------------------------------- | --- | --------- | ------------- |

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 555
Fig. 4. Process selection results by process stage, n rep- Fig. 5. Outcome of applying backward snowballing.
resents the number of filtered studies.
according to the goal or purpose of the testing activity.
between IEEE Xplore and other search engines may In this context, we have identified eight types of tests
stem from the fact that search strings were primarily
according to their target: unit tests, integration tests,
evaluated on this engine. This potential bias will be
system tests, acceptance tests, service-based tests,
discussed in the chapter dedicated to the limitations
contract tests, component tests, and unique microser-
and threats to the validity of our research. Our analysis
vice tests. The relation between the studies and the
revealed that conference proceedings dominate the
testing targets is outlined in Table 11. The frequency of
distribution of primary studies by publication type,
accounting for 80.3% of the total, while the rest are occurrences of unit tests and integration tests is con-
journal articles. sistent with the findings reported by Waseem et al.
4.1. Answers to Research Questions
(1) RQ-1. What software tests are dedicated to sys-
tems based on MSA, and in what contexts are they
applied?
According to [36], testing types or levels can be
classified by target or by objective. By target refers to
classifying tests based on the level or component being
tested, while by objective refers to classifying tests Fig. 6. Thematic synthesis process, adapted from [27].
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

556 BELLO-TREJO et al.
[10], who indicate that these two testing strategies, Table 8. References to the criteria for quality assessment
alongside end-to-end tests, are the most utilized for
ID Reference
testing microservices.
Concerning tests classified by objective, we have CR-1 Kitchenham, B., & Charters, S. (2007). Guide-
identified six categories: nonfunctional tests, regres- lines for performing Systematic Literature Reviews
sion tests, A/B tests, cloud-based tests, API tests, in Software Engineering. 2.
functional tests, and end-to-end tests. Table 12 illus- CR-2 Rohunen, A., Rodriguez, P., Kuvaja, P., Krzanik, L.,
trates the correspondence between the studies and the y Markkula, J. (2010). Approaches to Agile Adop-
testing objectives covered in the study.
tion in Large Settings: A Comparison of the
In exploring the usage contexts of tests for micros- Results from a Literature Analysis and an Indus-
ervices-based systems, we observed that authors often trial Inventory. En M. Ali Babar, M. Vierimaa, & M.
refer to strategies within software development. Spe- Oivo (Eds.), Product-Focused Software Process
cifically, we noted the integration of tests for micros-
Improvement (pp. 77–91). Springer.
ervices within the frameworks of Continuous Integra-
CR-3 Usman, M., Mendes, E., Weidt, F., y Britto, R.
tion and continuous delivery (CI/CD), continuous
(2014). Effort estimation in agile software develop-
experimentation (CE), DevOps, and general software
ment: A systematic literature review. Proceedings
development life cycle (SDLC). The association
between studies referencing these contexts is docu- of the 10th International Conference on Predictive
mented in Table 13. Models in Software Engineering, 82–91.
(2) RQ-2. How does existing literature suggest CR-4 Dybå, T., y Dingsøyr, T. (2008). Empirical studies
approaching the testing process for MSA-based sys- of agile software development: A systematic
tems? review. Information and Software Technology,
We identified various proposals aimed at improv- 50(9), 833–859
ing the testing process for microservices. It was partic-
ularly insightful to delve into the academic perspective
on microservices, allowing us to recognize the most
Table 9. Data extraction template
common and significant research areas in this
domain. We present a classification of these proposals Field
in Table 14.
Identifier
As shown in Table 14, the most common research
areas are benchmarking, performance analysis, and Title
test automation. This is primarily because these Author(s)
aspects represent the most apparent challenges when
Year of publication
conducting tests in microservices environments.
Type of publication
(3) RQ-3. What are the tools used to test MSA-
based systems? Conference or journal
Automated testing simplifies the execution control Search engine
and allows for an efficient and continuous comparison
DOI
of results. Given the inherent complexity of microser-
vices, the use of software tools becomes essential. Keywords
Inthis context, we identified 95 tools used or men- Abstract
tioned in primary studies designed to address various
RQ-1: Test level
activities within the testing process. Furthermore,
considering the need for real microservices systems to RQ-1: Application context
evaluate their findings and produce reliable results, we
RQ-2: Literature proposal
have compiled a list of 26 microservices systems or
RQ-3: Testing tools
benchmarks mentioned in the literature. Table 15
shows the tools and systems found. RQ-4: Challenges
(4) RQ-4. What are the challenges associated with
the testing of MSA-based systems?
most challenges in microservices are performance,
The distributed nature of microservices presents
reliability, resilience, and security. Additionally, the
numerous challenges in the testing process. Therefore,
lack of real MSA-based systems and the need for
identifying and analyzing the most common chal-
lenges is crucial for guiding future research efforts that benchmarking hinder experimentation with the tools
address these issues. The main challenges identified in proposed in the literature. Regression testing and end-
the primary studies are presented in Table 16. As to-end testing also present the most critical issues in
depicted in Table 16, the quality attributes facing the the microservices testing process.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 557
Table 10. Selected primary studies
ID Title Author Year
S-1 Automation of regression test in microservice architecture Kargar and Hanifizade 2018
S-2 Towards Executable Specifications for Microservices Quenum and Aknine 2018
S-3 μ Suite: A Benchmark Suite for Microservices Sriraman and Wenisch 2018
S-4 ORCAS: Efficient Resilience Benchmarking of Microservice Architectures van Hoorn et al. 2018
S-5 TeaStore: A Micro-Service Reference Application for Benchmarking, von Kistowski et al. 2018
Modeling and Resource Management Research
S-6 An extensible fault tolerance testing framework for microservice-based Wu et al. 2018
cloud applications
S-7 Benchmarking microservice systems for software engineering research Zhou et al. 2018
S-8 Microservices in Industry: Insights into Technologies, Characteristics, Bogner et al. 2019
and Software Quality
S-9 Microservices in Industry: Insights into Technologies, Characteristics, Gan et al. 2019
and Software Quality
S-10 Automatic Performance Monitoring and Regression Testing During the Janes and Russo 2019
Transition from Monolith to Microservices
S-11 Performance Modeling for Cloud Microservice Applications Jindal et al. 2019
S-12 Performance and Scalability Testing Strategy Based on Kubemark Lei et al. 2019
S-13 Predicting the End-to-End Tail Latency of Containerized Microservices Rahman and Lama 2019
in the Cloud
S-14 Microservice-Tailored Generation of Session-Based Workload Models Schulz et al. 2019
for Representative Load Testing
S-15 Comparison of Runtime Testing Tools for Microservices Sotomayor et al. 2019
S-16 Design and Research of Microservice Application Automation Testing Wang et al. 2019
Framework
S-17 Latent error prediction and fault localization for microservice applica- Zhou et al. 2019
tions by learning from system trace logs
S-18 Scalability Assessment of Microservice Architecture Deployment Con- Avritzer et al. 2020
figurations: A Domain-based Approach Leveraging Operational Profiles
and Load Tests
S-19 An Automatic Test Data Generation Method for Microservice Application Ding et al. 2020
S-20 Microservices: A Performance Tester’s Dream or Nightmare? Eismann et al. 2020
S-21 Research on Microservice Application Testing System Li et al. 2020
S-22 Research on Microservice Application Testing Based on Mock Technology Lin et al. 2020
S-23 Fitness-guided Resilience Testing of Microservice-based Applications Long et al. 2020
S-24 Testing microservice architectures for operational reliability Pietrantuono et al. 2020
S-25 Workflow-Aware Automatic Fault Diagnosis for Microservice-Based Wang et al. 2020
Applications with Statistics
S-26 CIPC: A Change Impact Propagation Computing Based Technique for Chen et al. 2021
Microservice Regression Testing Prioritization
S-27 HawkEDA: a tool for quantifying data integrity violations in event-driven Das et al. 2021
microservices
S-28 Inferring Relations Among Test Programs in Microservices Applications De Angelis et al. 2021
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

558 BELLO-TREJO et al.
Table 10. (Contd.)
ID Title Author Year
S-29 Design and Implementation of Intelligent Automated Testing of Micros- Duan et al. 2021
ervice Application
S-30 Modeling and verification of Industrial Microservice Architecture Based Meng et al. 2021
on Formal Methods
S-31 Quality Assurance of Micro-Services - When to trust your micro-service Vassiliou-Gioles 2021
test results?
S-32 Design, monitoring, and testing of microservices systems: The practi- Waseem et al. 2021
tioners’ perspective
S-33 Fault Analysis and Debugging of Microservice Systems: Industrial Sur- Zhou et al. 2021
vey, Benchmark System, and Empirical Study
S-34 VECROsim: A Versatile Metric-oriented Microservice Fault Simulation Bi et al. 2022
System (Tools and Artifact Track)
S-35 Microservices integrated performance and reliability testing Camilli et al. 2022
S-36 Automated test-based learning and verification of performance models Camilli et al. 2022
for microservices systems
S-37 Modeling Performance of Microservices Systems with Growth Theory Camilli and Russo 2022
S-38 Challenges in regression test selection for end-to-end testing of microser- Elsner et al. 2022
vice-based software systems
S-39 Automated Testing and Resilience of Microservice’s Network-link using Karn et al. 2022
Istio Service Mesh
S-40 Version-based and risk-enabled testing, monitoring, and visualization of Ma et al. 2022
microservice systems
S-41 SEAByTE: A Self-adaptive Micro-service System Artifact for Automating Quin and Weyns 2022
A/B Testing
S-42 Bunk8s: Enabling Easy Integration Testing of Microservices in Kubernetes Reile et al. 2022
S-43 Testing for Event-Driven Microservices Based on Consumer-Driven Wu et al. 2022
Contracts and State Models
S-44 Defektor: An Extensible Tool for Fault Injection Campaign Management Baptista et al. 2023
in Microservice Systems
S-45 A microservice regression testing selection approach based on belief prop- Chen et al. 2023
agation
S-46 μ Bench: An Open-Source Factory of Benchmark Microservice Applications Detti et al. 2023
S-47 ExVivoMicroTest: ExVivo Testing of Microservices Gazzola et al. 2023
S-48 Analysis for Microservice Architecture Application Quality Model and Gong and Cai 2023
Testing Method
S-49 Twin Graph-Based Anomaly Detection via Attentive Multi-Modal Huang et al. 2023
Learning for Microservice System
S-50 UTEMS: A Unit Testing Scheme for Event-driven Microservices Ma et al. 2023
S-51 Detection of Faults in Microservices using Petri Nets Naik and D’Souza 2023
S-52 Microusity: A testing tool for Backends for Frontends (BFF) Microser- Rattanukul et al. 2023
vice Systems
S-53 HydraGen: A Microservice Benchmark Generator Sedghpour et al. 2023
S-54 Benchmarks for End-to-End Microservices Testing Smith et al. 2023
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 559
Table 10. (Contd.)
ID Title Author Year
S-55 Automatic Detection of Security Deficiencies and Refactoring Advises Ьnver and Britto 2023
for Microservices
S-56 Zero-Config Fuzzing for Microservices Wang et al. 2023
S-57 Fostering Microservice Maintainability Assurance Through a Compre- Abdelfattah 2024
hensive Framework
S-58 Interaction Prediction and Anomaly Detection in a Microservices-based Aktaş and Kilinc 2024
Telecommunication Platform
S-59 Towards LLM-Assisted System Testing for Microservices Almutawa et al. 2024
S-60 Can My Microservice Tolerate an Unreliable Database? Resilience Test- Assad et al. 2024
ing with Fault Injection and Visualization
S-61 MicroFI: Non-Intrusive and Prioritized Request-Level Fault Injection Chen et al. 2024
for Microservice Applications
S-62 Budget Aware Performance Test Selection for Microservices Cooper et al. 2024
S-63 Grammar-Based Anomaly Detection of Microservice Systems Execution D’Angelo and D’Aloisio 2024
Traces
S-64 MicroFuzz: An Efficient Fuzzing Framework for Microservices Di et al. 2024
S-65 Evaluating intrusion detection for microservice applications: Benchmark, Flora and Antunes 2024
dataset, and case studies
S-66 Identifying Performance Issues in Microservice Architectures through Giamattei et al. 2024
Causal Reasoning
S-67 Automated functional and robustness testing of microservice architectures Giamattei et al. 2024
S-68 Multi-task federated learning-based system anomaly detection and multi- Hao et al. 2024
classification for microservices architecture
S-69 Application of API automation testing based on microservice mode in Li et al. 2024
industry software
S-70 Multi-source Anomaly Detection For Microservice Systems Li et al. 2024
S-71 RVElastic: a Runtime Verification Framework for Microservice Systems Murino et al. 2024
S-72 Synthetic to Real-World: Insights on Microservices-Based Application Rashmi et al. 2024
Benchmarks
S-73 Boosting Microservice Resilience: An Evaluation of Istio’s Impact on Singh et al. 2024
Kubernetes Clusters Under Chaos
S-74 A Bayesian LSTM Based Active Anomaly Detection Service for Large Wang et al. 2024
Online Systems
S-75 A fuzzy logic-based quality model for identifying microservices with low Yılmaz and Buzluca 2024
maintainability
S-76 Fault Diagnosis for Test Alarms in Microservices through Multi-source Data Zhang et al. 2024
4.2. Thematic Synthesis Results structure depicted in Fig. 9, but to streamline the pre-
sentation, only the codes with the highest level of
From the analysis of 1384 text segments, we identi-
abstraction are included as sections.
fied 62 codes organized into 11 themes. We identified
(1) Tests and their application context
the higher-order themes based on their relation to the
research questions, following the approach by Cruzes Yılmaz and Buzluca [52] present an insightful per-
and Dybå [27]. The resulting thematic map is pre- spective on testability in microservices. They highlight
sented in Fig. 9. The following sections adhere to the that in the context of microservices, testability encom-
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

| 560 |     |     |     |     | BELLO-TREJO et al. |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Distribution of primary studies by year of publication Distribution of primary studies by search engine
25
|     |     |     |     |     |     | Science Direct | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
21
20
|     |     |     |     |     |     |     | SpringerLink 2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
enigne hcraeS
15
ydutS
|     |     |     |     |     | 12  |     | Wiley Online |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
3
|     |     | 10  |     | 10  |     |     | Library |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
10
|     |     |     | 8   | 8   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7
|     |     |     |     |     |     |     | ACM Digital | 20  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
Library
5
|     |     |     |     |     |     |     | IEEE Xplore |     |     | 49  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
0
|     | 2018 | 2019 | 2020 | 2021 2022 | 2023 2024 |     | 0 10 | 20 30 | 40  | 50 60 |
| --- | ---- | ---- | ---- | --------- | --------- | --- | ---- | ----- | --- | ----- |
|     |      |      |      | Year      |           |     |      | Study |     |       |
Fig. 7. Primary study distribution by year of publication.
Fig. 8. Number of findings for each search engine.
passes the capability to test each microservice in isola-
(b) Integration tests
tion from the system as a whole and in the context of
its interactions with other services. It is paramount to The purpose of integration tests is to validate the
communication paths and interactions between the
| guarantee  |     | that  | microservices  | are  easily  | testable  to |     |     |     |     |     |
| ---------- | --- | ----- | -------------- | ------------ | ------------ | --- | --- | --- | --- | --- |
microservices that make up a system, ensuring that
enhance the overall quality and reliability of the sys-
tem. As mentioned earlier, testing methods are broadly each  microservice  can  communicate  appropriately
| categorized based on the target and objective of the |     |     |     |     |     | with others. |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
test. The first group consists of unit, integration, and According to De Angelis et al. [53], these tests are
system testing – just to name a few. This section pres- a form of fast feedback towards integration. Similarly,
ents these testing strategies for microservices-based
Gong and Cai [42] emphasize that this testing strategy
systems.
verifies the interaction between the external commu-
Before introducing the subsections, it is important nication module of a microservice and external ser-
vices, as well as between the data access module and
to note that concerning system tests and acceptance
tests, we did not find relevant information regarding the external database.
their implementation; they were merely mentioned in
Li et al. [16] mention that this type of test verifies if
the studies listed in Tables 11 and 12.
|     |     |     |     |     |     | submodules  | can  cooperate  | with  | each  | other  as |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | ----- | ----- | --------- |
1. Test target expected. This is to ensure communication and inter-
(a) Unit tests action between submodules, checking if the interface
has any errors, and to guarantee the stable operation of
Unit tests verify the behavior of microservices [53].
| Specifically,  |     | unit  | tests  are  | a  technique  | to  verify |     |     |     |     |     |
| -------------- | --- | ----- | ----------- | ------------- | ---------- | --- | --- | --- | --- | --- |
whether the smallest unit of code in the software func- Table 11. Testing strategies grouped by test target
tions correctly. For applications, unit tests do not dif-
fer significantly from those in monolithic applica- Testing strategy Studies
tions, where the test objective is a class, function, or
|     |     |     |     |     |     | Unit | S-2, S-7, S-12, S-21, S-22, S-28,  |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ---------------------------------- | --- | --- | --- |
method of a class [42]. This strategy holds relevance in
methodologies  like  Test-Driven  Development S-32, S-43, S-45, S-48, S-50, S-62
(TDD), as it is considered the best approach to cover
|     |     |     |     |     |     | Integration | S-7, S-12, S-15, S-21, S-22, S-28,  |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------- | --- | --- | --- |
code logic [54]. A study by Waseem et al. [10] supports
S-31, S-32, S-42, S-43, S-48, S-62
this claim, noting that unit tests, integration, and end-
to-end tests are the three most used testing strategies System S-15, S-54
by survey respondents and interviewees, as per the
|     |     |     |     |     |     | Acceptance |     | S-2, S-62 |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- |
authors. The primary reasons for employing this test-
ing strategy include the following [10]: Service S-15, S-21, S-40, S-45
• Allow for isolated component testing. Contract S-15, S-21, S-28, S-40, S-43,
S-48, S-69
• Check that each microservice functions correctly
and has the required functionalities.
|     |     |     |     |     |     | Component |     | S-15, S-48 |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --- |
• Identify potential issues in microservices in the
|     |     |     |     |     |     | Single microservice |     |     | S-21 |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---- | --- |
early stages of system development.
|     |     |     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |     |     |  Vol. 51  |  No. 8  |  2025 |
| --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --------- | ------- | ----- |

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 561
Table 12. Testing strategies grouped by test objective (d) Contract tests. Contract testing, as described by
Vocke [57], is responsible for verifying interactions at
Testing strategy Studies
the application limits, ensuring that each microservice
Nonfunctional S-1, S-3, S-4, S-5, S-6, S-8, S-9, S-10, follows the contract expected by an external consum-
S-11, S-12, S-13, S-14, S-16, S-17, S-18, ing service. Li et al. [58] also elaborate on Consumer-
S-20, S-21, S-23, S-24, S-25, S-27, Contract-Based Testing, mentioning that this type of
S-31, S-32, S-33, S-34, S-35, S-36, test validates that the service can handle expected
requests and responses. This method prioritizes API
S-37, S-39, S-44, S-46, S-48, S-51,
quality, minimizing redundant test cases.
S-52, S-53, S-54, S-55, S-56, S-62, S-66
Gong and Cai [42] also mention contract testing
Regression S-1, S-10, S-20, S-26, S-28, S-38, S-45,
for microservices-based systems. According to the
S-47, S-54
authors, in a monolithic application, all functional
A/B S-8, S-32, S-41 modules belong to the same project and run in the
Cloud S-21 same runtime. In this scenario, when communication
API S-52, S-69 between modules fails to meet the interface specifica-
tion (contract), it is detected by the compiler. How-
Functional S-16, S-54, S-67
ever, microservices applications comprise several
End-to-end S-12, S-15, S-21, S-28, S-32, S-38, communicative services, and each service has its own
S-42, S-45, S-48, S-50 runtime environment. Considering this, if a service
modifies the contract, it goes unnoticed by the com-
piler, potentially breaking service compatibility.
Table 13. Testing application contexts Hence, contract tests serve as the primary method to
assess the compatibility of MSA applications.
Testing context Studies
Depending on who maintains the contract, there
CI/CD S1, S-2, S-32, S-41, S-42, S-62, are two types of contract testing: Consumer-side tests,
which is the most commonly used type, where the
S-65, S-69
contract is generated on the consumer side and the
CE S-41 provider is simulated during testing; and provider-side
tests, which generate the contract to configure the
DevOps S-1, S-5, S-11, S-14, S-20, S-22, S-35,
adapter and utilize mocks to fulfill the adapter’s
S-40, S-41, S-55, S-58, S-62
dependencies [42].
SDLC S-24, S-36, S-40, S-46, S-59, S-60 (e) Component tests. In microservices-based sys-
tems, component testing verifies the functionality and
other quality attributes of individual microservices.
the entire subsystem (p. 364). On the other hand, While these tests are conducted solely on specific
Waseem et al. [10] note that integration tests, along microservices, it is necessary to consider their depen-
with unit tests, are considered robust strategies. How- dencies on other microservices during test design [42].
ever, systematic testing is also required to cope with Ideally, the external services on which the service
the complexity of microservices-based systems. under test relies should be deployed and available to be
used directly for completing component tests. How-
Sotomayor et al. [55], citing Fowler and Lewis [2],
ever, in most cases, these external services are not
point out that when running integration tests on a
ready or accessible. In such scenarios, it is necessary to
microservices-based system, each microservice rep- employ simulated services to substitute these depen-
resents a component and can be grouped using the tra- dencies, ensuring the continuity of the tests [42].
ditional integration testing approach. Specifically, a
(f) Unique microservice tests. The goal of this type
test environment is used to integrate the individually
of test is to isolate all other services and resources a
tested microservices. Lastly, Vassiliou-Gioles [45]
microservice depends on, as well as the user perspec-
stresses that for integration test results to be reliable,
tive, to determine whether the microservice can
the developer must make sure that the specified
deliver the expected outcome. Unlike integration test-
microservice influenced the test result.
ing, single microservice testing concentrates on the
functionality of the entire service, not just external
(c) Service tests. Service tests can prevent user dis-
communication and storage [16].
ruptions and deliver prompt evaluations [56]. Never-
theless, these tests require consideration. For instance, 2. Test objective
Chen et al. [56], based on discussions from other (a) Nonfunctional tests. Nonfunctional tests, such
authors, point out that due to the complexities of ser- as performance and stress testing [55], are not the only
vice autonomy, dynamic linking, and access con- ones addressing quality aspects in microservices.
straints, service and end-to-end testing differ consid- Anillustrative example is the study by Bogner et al.
erably from conventional software [3]. [59], which examines how the industry perceives the
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

| 562 |     |     |     | BELLO-TREJO et al. |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- |
impact of MSA on software quality. According to this Table 14. Testing proposals in the literature
study, implementing MSA influences key characteris-
|     |     |     |     |     | Proposal |     | Studies |
| --- | --- | --- | --- | --- | -------- | --- | ------- |
tics like security, reliability, usability, and scalability.
Similarly, Avritzer et al. [60] emphasize that attri- Benchmarking S-3, S-4, S-5, S-7, S-9, S-46,
butes such as scalability, performance, and maintain- S-53, S-54, S-72
| ability  constitute  | a  significant  |     | portion  | of  research |             |                                |     |
| -------------------- | --------------- | --- | -------- | ------------ | ----------- | ------------------------------ | --- |
|                      |                 |     |          |              | Performance | S-10, S-11, S-12, S-13, S-14,  |     |
focused on the quality of MSA. This section discusses
S-18, S-20, S-35, S-36, S-37,
the various nonfunctional tests identified in the litera-
S-62, S-65
ture.
| i. Performance tests |     |     |     |     | Reliability | S-24, S-35, S-71 |     |
| -------------------- | --- | --- | --- | --- | ----------- | ---------------- | --- |
According to Leitner and Bezemer [61], perfor- Scalability S-12, S18
mance testing is already considered a challenge in tra-
|     |     |     |     |     | Resilience | S-23, S-39, S-67, S-73 |     |
| --- | --- | --- | --- | --- | ---------- | ---------------------- | --- |
ditional systems. Moreover, the architectural, techno-
|     |     |     |     |     | Security | S-27, S-43, S-52, S-55, S-64,  |     |
| --- | --- | --- | --- | --- | -------- | ------------------------------ | --- |
logical, and organizational changes induced by micro-
| services  | also  impact  | performance  |     | engineering |     |     | S-65 |
| --------- | ------------- | ------------ | --- | ----------- | --- | --- | ---- |
practices, as stated by Heinrich et al. [62]. This aligns
|     |     |     |     |     | Testability |     | S-31 |
| --- | --- | --- | --- | --- | ----------- | --- | ---- |
with the findings of Eismann et al. [40], who note that
|     |     |     |     |     | Test automation | S-2, S-15, S-16, S-19, S-21,  |     |
| --- | --- | --- | --- | --- | --------------- | ----------------------------- | --- |
performance testing in microservices poses challenges
S-22, S-28, S-29, S-40, S-42,
compared to traditional software.
S-55, S-57, S-69
The typical approaches to performance testing usu-
ally align with either testing to meet user experience Fault injection S-6, S-44, S-61
requirements  or  to  fulfill  a  scalability  requirement Fault simulation S-34
| [43].  Moreover,  | performance  | testing  | is  | conducted |                 |                                |     |
| ----------------- | ------------ | -------- | --- | --------- | --------------- | ------------------------------ | --- |
|                   |              |          |     |           | Fault detection | S-17, S-49, S-51, S-58, S-60,  |     |
using various testing strategies, such as unit testing or
S-63, S-68, S-70, S-74
integration testing [40].
|     |     |     |     |     | Fault diagnosis |     | S-25, S-76 |
| --- | --- | --- | --- | --- | --------------- | --- | ---------- |
Lastly, as individual services in a microservices-
| based  system  | are  typically  | deployed  | in  | containers, |                 |     |            |
| -------------- | --------------- | --------- | --- | ----------- | --------------- | --- | ---------- |
|                |                 |           |     |             | Ex-vivo testing |     | S-35, S-47 |
monitoring container resource utilization is crucial for
|     |     |     |     |     | Regression testing | S-1, S-10, S-26, S-38, S-45 |     |
| --- | --- | --- | --- | --- | ------------------ | --------------------------- | --- |
performance testing in microservices-based systems
[42]. For this reason, we find it useful to identify mon- Industry perspective S-8, S-32
itoring tools. Monitoring can be conducted in a black-
|     |     |     |     |     | Quality model |     | S-48, S-75 |
| --- | --- | --- | --- | --- | ------------- | --- | ---------- |
box or gray-box fashion, as discussed by Giamattei
|               |                     |     |            |           | Microservices event-driven  |     | S-27. S-50 |
| ------------- | ------------------- | --- | ---------- | --------- | --------------------------- | --- | ---------- |
| etal.  [63].  | In  the  black-box  |     | approach,  | only  the |                             |     |            |
architecture testing
| request-response  | pairs  | exchanged  | with  | the  edge |     |     |     |
| ----------------- | ------ | ---------- | ----- | --------- | --- | --- | --- |
microservices are collected. On the other hand, the
|     |     |     |     |     | Verification |     | S-30 |
| --- | --- | --- | --- | --- | ------------ | --- | ---- |
gray-box approach extends this monitoring to include
|     |     |     |     |     | A/B testing |     | S-41 |
| --- | --- | --- | --- | --- | ----------- | --- | ---- |
request-response pairs exchanged not only with the
edge microservices but also among internal microser-
vices. Related to monitoring, Murino et al. [64] men-
tion runtime verification (RV) as a promising approach platforms. Evaluating a system’s behavior under vary-
ing load levels can reveal areas for improvement, such
for real-time monitoring of distributed systems, includ-
as bottlenecks or failure points within the system.
ing microservices-based systems, enabling early detec-
tion of anomalies and safety hazards by instrumenting Often, these issues can only be uncovered through
the system with monitors that enforce specified prop- load testing because they only manifest or become vis-
ible under a specific load threshold in the system [66].
erties.
ii. Maintainability
i.a. Single-user load tests
This type of test assesses the performance of an
While we did not find evidence regarding main-
application under a single user load. The aim of these tainability testing, thanks to the research by Gong and
tests  is  to  comprehend  the  control  flow  of  user Cai [42], we understand how to measure it through
requests and pinpoint segments that consume most of five  subcharacteristics:  reusability,  analyzability,
the response time [43].
modifiability, and testability. However, the authors
i.b. Load tests only specify how to measure the modularity and trace-
ability of a system or application.
| Load  | tests  are  a  type  | of  performance  |     | test  that |     |     |     |
| ----- | -------------------- | ---------------- | --- | ---------- | --- | --- | --- |
assesses the performance of an application under real The  modularity  of  microservices-based  systems
load [65]. There are three main ways to conduct load can be divided into coupling and cohesion to indicate
testing [65]: using real users to generate load, employ- the complexity of the overall system [42]. Meanwhile,
ing load injectors, or deploying load tests on special traceability can be measured based on whether the
|     |     |     | PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 51  |  No. 8   2025 |
| --- | --- | --- | ---------------------------------- | --- | --- | --------- | ------------- |

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 563
Table 15. Testing tools and systems
|                           | Usage |                     | Tools |     |     |     | Studies |     |
| ------------------------- | ----- | ------------------- | ----- | --- | --- | --- | ------- | --- |
| Test execution            |       | HTML Unit WebDriver |       |     |     |     | S-54    |     |
| Testing coverage          |       | Jenkins             |       |     |     |     | S-21    |     |
| Test result visualization |       | SonarQube           |       |     |     |     | S-21    |     |
Fault injection Simian Army, Litmus, Hoverfly, Istio, Z3, DOCTOR,  S-6, S-15, S-23, S-39, S-44, S-60
ChaosMesh, RainMaker, AWS Aurora
Monitoring Istio, Heapster, Prometheus, Jaeger, Zipkin, Open- S-12, S-14, S-24, S-25, S-32, S-39,
Tracing, cAdvisor, Stack, CloudHealth, Monasca,  S-40, S-45, S-46, S-47, S-52, S-72
Varys, Amazon CloudWatch, Nagios, Zeek, Jira, Data-
dog Kafka Dashboard, Spring Boot Actuator, Grafana
Load testing JMeter, Tsung, Gatling, Grinder, BenchFlow, Locust,  S-13, S-14, S-18, S-25, S-35, S-39,
|     |     | K6  |     |     |     | S-54, S-61, S-65, S-73 |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
Contract testing Pact, Spring Cloud Contract S-21, S-40, S-43, S-48
| Mocking |     | Mockito, WireMock, JMockit, Minikube |     |     |     |     | S-15, S-22 |     |
| ------- | --- | ------------------------------------ | --- | --- | --- | --- | ---------- | --- |
Resilience testing Gremlin, Chaos Monkey, RestTestGen, RESTler,  S-6, S-15, S-44, S-67
bBOXRT
End-to-end testing Selenium, SideeX, Kubermark, Protractor, Robot  S-12, S-21, S-32, S-48, S-50
Framework
System testing Appium, Docker Compose Rule, Gatling, Gremlin,  S-15, S-54
Watir, Selenium
Integration testing Docker Compose Rule, Gremlin, Hoverfly, JMeter,  S-15, S-21, S-32, S-42
Minikube, Octopus, Istio, Jenkins, Teamcity
Component testing Gatling, Gremlin, Hoverfly, JMeter, Minikube, Telep- S-15, S-32
resence, Tsung
Unit testing JUnit, NUnit, Spring Boot Starter Test, Rspec, xUnit, Jest S-2, S-15, S-32
| Acceptance testing   |     | Cucumber                                  |     |     |     |     | S-2         |     |
| -------------------- | --- | ----------------------------------------- | --- | --- | --- | --- | ----------- | --- |
| API testing          |     | RESTler, Curl, Postman, SoapUI            |     |     |     |     | EP-52, S-69 |     |
| Regression testing   |     | Diffy                                     |     |     |     |     | S-1         |     |
| Test parallelization |     | TestNG                                    |     |     |     |     | S-17, S-54  |     |
| Fuzzing              |     | FUDGE, FuzzGen, libFuzzer, AFL, honggfuzz |     |     |     |     | S-56, S-64  |     |
Security testing OWASP ZAP, Nmap, Kubeaudit, Docker Bench for  S-55
Security, Trivy, Kube-hunter, Kube-bench, Terrascan
MSA systems, application  Sock Shop, m-Ticket, z-Shop, Need, WeChat, Online  S-5, S-13, S-14, S-17, S-18, S-23,
or benchmarks Boutique, Bookinfo, JPetStore, PetClinic, Fullteach- S-25, S-26, S-27, S-28, S-34, S-35,
ing, Stan’s Robot Shop, TrainTicket, μ Suite, Tail- S-37, S-39, S-44, S-45, S-46, S-47,
Bench, Theodolite, AcmeAir, ppbench, μ qsim, JOA,  S-51, S-53, S-54, S-65, S-66, S-67,
eShopContainers, PyggyMetrics, Hipster shop, Cloud- S-68, S-72, S-75
Suite, SpringCloudDemo, BiFrost
microservices-based system implements a service link measured by the benefit of its capacity growth in rela-
tion to the cost required to scale the system [42].
traceability function or by the proportion of traceable
services [42]. Scalability poses a significant challenge in micros-
ervices systems, as highlighted by Waseem et al. [10].
iii. Scalability
According to the authors, achieving scalability is com-
plex because business functionalities are developed in
Scalability is a key feature of microservices applica-
|     |     |     |     | various  | programming  | languages,  | distributed  | across |
| --- | --- | --- | --- | -------- | ------------ | ----------- | ------------ | ------ |
tions, which must be able to enhance the performance
|     |     |     |     | different  | machines,  | run  | on  diverse  | servers,  and |
| --- | --- | --- | --- | ---------- | ---------- | ---- | ------------ | ------------- |
of individual services by adding resources and service
deployed in multiple cloud environments. This level of
instances to avoid performance bottlenecks. There-
heterogeneity necessitates that architects design effec-
fore, for microservices applications, scalability can be tive strategies to coordinate the microservices at a
| PROGRAMMING AND COMPUTER SOFTWARE  |     |     |  Vol. 51  |  No. 8  |  2025 |     |     |     |
| ---------------------------------- | --- | --- | --------- | ------- | ----- | --- | --- | --- |

564 BELLO-TREJO et al.
large scale or, alternatively, identify which of them Table 16. Testing challenges in microservices-based systems
need to be scaled to meet the increasing demand.
Challenges Studies
iv. Security
Testing process S-15, S-16, S-19, S-21, S-22, S-24,
Software security testing is a subset of software test-
S-26, S-28, S-29, S-32, S-40, S-47,
ing that focuses on the security properties of computer
S-48, S-75
applications. It is divided into functional security test-
ing and vulnerability security testing [44]. Regression testing S-1, S-26, S-28, S-38, S-45
Functional security tests ensure that security fea- Performance S-9, S-11, S-12, S-13, S-20, S-21,
tures are correctly implemented in an application [44]. S-25, S-27, S-35, S-36, S-37, S-40,
Vulnerability security testing focuses on uncovering S-53, S-62, S-63
security risks and vulnerabilities that could render a
Verification and S-21, S-44, S-47
software system susceptible to attacks. These tests can
validation
be either static or dynamic. Static tests aim to identify
configuration errors and vulnerabilities in the source Fault diagnosis S-17, S-25, S-34, S-39, S-44,
code, whereas dynamic tests are geared towards Manual testing S-16, S-19, S-32
detecting vulnerabilities and security weaknesses in
Reliability S-8, S-24, S-25, S-35, S-49
applications by evaluating them during execution [44].
Contract testing S-40
Among the findings related to security, we found
Scalability S-32, S-36
fuzzing testing, which is a valuable addition to existing
testing techniques. It works by generating a large num- Resilience S-23, S-61
ber of randomly generated test inputs. This approach Security S-8, S-21, S-27, S-32, S-52, S-53,
can detect programming errors such as buffer over-
S-55, S-56
flows and memory leaks. It is worth mentioning that
Monitoring S-32, S-40
since microservices are designed to facilitate modular-
ity and ease of testing, fuzzing is a suitable approach Benchmarking S-3, S-5, S-33, S-46, S-53,
for microservices [67]. S-67, S-72
v. Reliability End-to-end testing S-15, S-21, S-32, S-38, S-42, S-48
In the context of microservices, performance test- Service testing S-21
ing, as outlined by Avritzer et al. [60], and reliability
Unit testing S-22
testing, according to Pietrantuono et al. [41], have
Integration testing S-21, S-32
been studied as separate issues. Unfortunately, there is
a striking lack of integrated testing approaches capable Fault detection S-7, S-33, S-51, S-63, S-68, S-76
of evaluating both quality attributes and deriving A/B testing S-41
mutual relationships. This integration is crucial, espe-
API testing S-52, S-67
cially when considering that automated reliability test-
Load testing S-14, S-62
ing of microservices is vital in DevOps [43]. Therefore,
achieving a high level of reliability in software requires Testability S-31
excessive testing efforts to reach an acceptable level of
Fault tolerance S-6, S-71
confidence [41].
Maintainability S-57
In this category, fault tolerance testing is essential
Fault injection S-60
to verify the effectiveness of the fault tolerance mech-
anism, ensuring that the application can function cor- Fuzzing S-6
rectly as specified in the fault tolerance design. Activ-
ities stemming from this aspect of software quality
include fault detection, simulation, diagnosis, and whenever a service modification occurs, regression
fault injection [46]. Fault detection in microservices testing is necessary to detect any faults introduced by
plays a crucial role. If faults are only detected after the modifications, as noted by Chen et al. [56].
deployment, resources are wasted on unnecessary
We found the subcategory of functional regression
postmortem analysis [48]. On the other hand, as a core
testing, which evaluates the system after a modifica-
technology in fault tolerance testing, fault injection is
tion to ensure that all features, flows, and functional-
a relatively mature topic in the reliability domain [46],
ities of the system work as they did in the previous ver-
especially using chaos engineering [68].
sion or according to a specified or expected function-
(b) Regression tests.
ality. It contributes to ensuring the system’s quality
Regression testing, across different stages of testing and helps prevent unintended system changes induced
activities, aims to ensure that changes made to a soft-
by the pressure of modifications [66].
ware module do not adversely affect its behavior or
that of the entire software system [53]. In other words, (c) A/B tests.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 565
Fig. 9. Higher-order themes model, consisting of four main themes.
A/B testing is a systematic approach to compare (e) Functional tests.
the usage of two versions of a system and determine
Functional testing ensures that various system fea-
which variant is preferred based on specific criteria.
tures operate in line with the system specifications or
Specifically, an A/B test involves a randomized con-
expected functionality. Test cases typically derive from
trolled experiment where experimental units are
software component specifications, with each test cor-
assigned to one of two variants labeled A and B, which
responding to a specific software requirement or fea-
are expected to impact a specific metric of interest
ture. This approach helps ensure that different parts of
[51].
the overall software system function independently.
Accompanying this definition, we highlight a find- By focusing on software requirements, the outcome is
ing from the study by Waseem et al. [10] regarding the aligned with end-user expectations [66].
perspective on testing in microservices. They noted
Functional tests consider the system as a black box
that when asked about the use of A/B testing, 33.0% of
and do not take into account the internal decomposi-
the participants frequently or very frequently utilize
tion into microservices, which often reflects the user’s
this strategy. However, 53.8% of the participants rarely
perspective [66]. Giamattei et al. [63] note that func-
or never use A/B testing, indicating a contradictory
tional testing in MSA predominantly utilizes estab-
preference among practitioners.
lished tools for black-box testing of RESTful web ser-
Another type of test stemming from this concept is vices. These tools typically aim to maximize API cov-
multivariate testing. According to the definition by erage (number of executed methods), cover a wide
Quin and Weyns [51], these tests are similar to A/B range of HTTP response codes, and automate fault
tests, but they involve using more than two versions detection.
simultaneously.
Lastly, Wang et al. [69] provide an alternative defi-
(d) Ex vivo tests. nition of functional testing. According to the authors,
its primary goal is to verify if a service can achieve the
Another type of testing objective is found in ex vivo
expected functional outcomes and if the system can
testing, which, as defined by Gazzola et al. [49], uses
operate normally. The tester compares the returned
field-extracted information to expand existing test
data with the expected result by means of automatic
cases or generate new test cases that can be used to
logging, detection, and reproduction to confirm if the
consistently validate software updates in line with real-
service can attain the expected function.
world field uses. The opposite approach to ex vivo test-
ing is in vivo testing. (f) API tests.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

566 BELLO-TREJO et al.
In their study, Li et al. [58] use a company’s cloud strategy. Regarding DevOps, Janes et al. [72], Ünver
billing product to illustrate the API testing process. and Britto [44], Lin et al. [54], and Aktaş and Kilinc
They specifically consider API automation testing [73] have incorporated these practices into their pro-
within microservices architecture in industrial soft- posals.
ware, emphasizing the enhancements brought to Furthermore, in the study by Waseem et al. [10],
industry testing efficiency. The study suggests that API participants were asked about potential solutions to
automation testing in a microservices environment microservices problems, and they concluded that one
improves efficiency and accuracy in industrial soft- solution is the implementation of DevOps or CI/CD
ware development, especially in regression testing for for continuous testing of microservices systems. This
CI/CD environments. As the testing scale expands, same perspective can be found in the study by Cooper
the benefits of automation become even more evident. et al. [74], providing guidance to DevOps teams on
(g) End-to-end tests. optimal strategies for creating performance tests that
align with CI/CD practices.
Chen et al. [56] affirm that end-to-end testing
focuses on the behavior of the entire system. On the On the other hand, Camilli et al. [43] demonstrate
other hand, Lei et al. [70] state that end-to-end testing how they can facilitate traceability between perfor-
is the best way to verify if the entire system can operate mance verification activities and software require-
smoothly once deployed. ments. In contrast, Detti et al. [37], through their tool
μBench, enable designers to make informed decisions
However, as noted by Reile et al. [71], these types
regarding the performance impact on MSA. A similar
of tests are fragile, costly to write, slow to execute, and
approach is presented by Ma et al. [75] with the
require deploying the entire application. Similarly,
VMAMV system.
Waseem et al. [10] analyzed end-to-end testing and
Finally, Pietrantuono et al. [41] provide an inter-
stressed that while it offers a practical solution for test-
esting perspective on the reliability of microservices,
ing individual microservices or the entire microser-
emphasizing that stakeholders need to be informed
vices system, it can pose several challenges during the
about the operational reliability of the MSA. This
testing process, including delivery delays, the genera-
enables strategic decision-making, for example,
tion of hard-to-isolate errors, and conflicts in respon-
regarding efforts allocation to maintenance or reengi-
sibilities. Therefore, they suggest that future work
neering activities.
needs to address the issues associated with these tests
to make them more beneficial. (2) Literature proposals
(h) Cloud-based tests. Literature proposals focus on performance analysis
and the implementation of systems or applications
Cloud-based testing not only provides a compre-
based on MSA, commonly referred to as benchmark-
hensive testing environment but also offers a variety of
ing. In this section, we will classify and describe the
additional services. These services include the ability
literature proposals oriented toward testing in micros-
to create restore points, enabling evaluators to reset
ervices.
virtual machines to a previously specified state. They
support the monitoring of the actions of the program 1. Reference systems or applications
under test, helping to identify issues and pinpoint Given the need to develop more accurate systems
errors more accurately [16]. based on microservices that more faithfully reflect the
complexity of large-scale systems composed of hun-
Furthermore, cloud-based testing is ideal for con-
dreds of microservices, various solutions have been
ducting large-scale tests as it allows the creation of
proposed to address this challenge. For example, Detti
multiple test clients. This approach, coupled with the
et al. [37] introduce μBench, an open-source frame-
utilization of a significant number of virtual machines,
work designed for creating and executing reference
enables putting pressure on the system under test,
applications based on microservices. A more recent
which is crucial for effectively performing stress tests
study by Rashmi et al. [38] improved μBench by incor-
[16].
porating message passing among different microser-
3. Application contexts
vices. Similarly, some years ago, Gan et al. [76] intro-
Given the usefulness of practices such as DevOps duced DeathStarBench, an open-source suite focused
and CI/CD in enhancing software quality through the on microservices for cloud computing and Internet of
automation of phases in the development process, Things (IoT) environments.
such as software testing, we found it pertinent to iden-
In addition to these reference systems, there are
tify instances where these practices are applied or fol-
other notable proposals such as VECROsim [77],
lowed and how they impact other development
HydraGen [78], μSuite [79], TrainTicket [80],
phases.
ORCAS [81], TeaStore [82], and the testing suite for
For instance, Quin and Weyns [51] introduce a tool benchmarking by Smith et al. [66]. These tools pro-
that implements continuous experimentation (CE) to vide valuable alternatives for future research to evalu-
automate A/B testing. Similarly, Kargar and Hani- ate their approaches and advance in the development
fizade [50] devised a CD-oriented regression testing of microservices-based systems. Efforts are underway
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 567
to develop an automated assessment framework for In addressing monitoring challenges, Murino et al.
microservice systems [83]. The goal is to improve ana- [64] introduce RVElastic, a monitoring framework for
lytical capabilities, foster better reasoning in architec- microservices-based systems. This framework utilizes
tural design, and enhance overall testability. Apache Kafka for system instrumentation and relies
on OpenSearch for the analysis and visualization of
2. Test objectives
verification results.
(a) Functional tests.
Also, related to monitoring, Aktaş and Kilinc [73]
Giamattei et al. [63] propose MacroHive, a frame-
introduce an approach that leverages supervised and
work designed for the generation, execution, and gray-
unsupervised machine learning algorithms to detect
box analysis of functional and robustness tests within
anomalies within microservice logs. This method aims
microservice architectures. This framework includes
to streamline debugging processes and improve anom-
features such as combinatorial test case generation, an
aly detection. Similarly, D’Angelo and D’Aloisio [90]
infrastructure for executing and monitoring interac-
have introduced a compelling approach that focuses
tions, and a causal inferential engine. These compo-
on energy-efficient anomaly detection within micros-
nents provide testers with valuable insights into inter-
ervice systems' execution traces. Their work proposes
nal coverage, failing services, and the causal relation-
an innovative method that utilizes a formal Context-
ships between failures.
Free grammar for this purpose. There are also new
A noteworthy new advancement, as outlined by efforts on anomaly detection based on Federated
[84], involves employing LLM models to identify the Learning [91], multimodal learning [92], filtering on
system’s functional requirements and generate perti- multisource data [93], and time series data through an
nent test cases. Their work essentially extends monkey active Bayesian approach [94].
testing by leveraging LLMs to enhance branch cover-
Regarding reliability experimentation, proposals
age.
have been published for fault injection [77, 46]. How-
(b) Nonfunctional tests.
ever, there are also proposals for fault detection [47,
i. Performance 48] and fault diagnosis [95, 96]. In addition to fault
Performance is one of the main areas of concern for tolerance, we gathered the works of Karn et al. [65]
MSA due to its distributed nature. This is why various and Long et al. [97] to evaluate the resilience of micro-
solutions have been proposed to address this and other services systems.
issues associated with the quality attributes of micros-
Fault injection can be utilized to test the resilience
ervices.
of a microservices-based system using chaos engineer-
Approaches in the literature include performance ing. This method deliberately introduces faults into
analysis in microservices [40], automation of perfor- operational systems to assess and enhance their resil-
mance testing [43, 60, 85], performance modeling [86, ience against failures [68]. More precisely, the authors
87], and testing for finding conditions for performance inject faults into the database clients to replicate sce-
issues based on causal inference [88]. Similarly, solu- narios in which databases return corrupted data in
tions have been proposed for specific performance response to queries. Another study that utilizes chaos
aspects, such as load testing [43] or performance engineering [98] focuses on testing the stability of
regression testing [72]. microservices-based systems under various load sce-
narios and simulated failures within Kubernetes envi-
Regarding load testing, Schulz et al. [89] propose
ronments. An alternative to chaos engineering is ser-
two algorithms that enable load testing with efficient
vice-level fault injection testing (SFIT). SFIT inte-
resource usage and generate a workload that is more
grates fault injection testing into the early stages of the
representative than a simple request-based workload
development process. Unlike chaos engineering, SFIT
model. Additionally, they could reduce the test execu-
allows for the injection of faults before application
tion time compared to system-level testing, especially
deployment. With this technique, developers can
for combinations of microservices under test with a
introduce faults into the services within their micros-
low number of endpoints. Cooper et al. [74] present an
ervice application and directly test their resilience in
alternative method for a CI/CD environment, for
their integrated development environment (IDE) [68].
short load test selection that mirrors the response time
distribution of lengthier tests. This method offers the Another proposal for fault injection was made by
advantages of a traditional load test but in a much Chen et al. [99], who developed a fault injection frame-
shorter timeframe by leveraging historical workloads. work named MicroFI. This framework is designed to
ii. Reliability evaluate the resilience of diverse business functions
within applications through request-level fault injec-
Specifically for reliability testing, we identified
tion. Moreover, MicroFI specifically focuses on identi-
tools such as EMART, proposed by Pietrantuono et al.
fying and rectifying high-impact faults during the test-
[41], a method for evaluating the reliability of opera-
ing process.
tional MSA systems. Nevertheless, we also found pro-
posals related to fault tolerance and resilience. iii. Maintainability
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

568 BELLO-TREJO et al.
Yılmaz and Buzluca [52] introduce a hierarchical gaining popularity in the sector. Additionally, the
quality model that relies on fuzzy logic and incorpo- authors conclude that the inherent complexity of
rates low-level software code metrics to gauge and microservices-based systems poses significant chal-
assess the maintainability of microservice architec- lenges to their design, monitoring, and testing.
tures. This model identifies microservices requiring 4. Automation of subprocesses and testing activities
refactoring and offers a means to evaluate the quality
To enhance effectiveness in the microservices-ori-
of microservices concerning their maintainability.
ented testing process, research of this nature has been
Bypinpointing areas of low-level maintainability, this
published, such as the works of Lin et al. [54], Li et al.
approach can enhance microservice-based applica-
[16], Ma et al. [75], Quin and Weyns [51], Wang et al.
tions and supply valuable feedback to development
[69], and Reile et al. [71], proposing tools that auto-
teams.
mate test execution. Research efforts have also been
iv. Security
dedicated to automatic test data generation [13] and
Regarding security, we came across valuable pro- test case generation [49, 17, 104, 105]. In line with
posals like [100], which is aimed at RESTful API fuzz- these proposals, Sotomayor et al. [55] present a com-
ing in microservices systems. Ünver and Britto [44] parison of several tools that can be used to test micro-
propose a suite of security testing tools that integrate services under different testing strategies.
security scanners to audit classified security weak-
5. Complementary architectonic styles
nesses, aligned with recommendations for refactoring
In addition to traditional microservices develop-
faulty code. There are also efforts related to assessing
ment, we identified approaches that involve comple-
intrusion detection in microservices-based systems, as
mentary architectures, such as UTEMS, which
demonstrated by Flora and Antunes [39].
focuses on unit testing of event-driven microservices
Similarly, Wang et al. [67] research automates test
[106]. Targeting this architectural style, Wu et al. [107]
case generation for fuzzing. Another fuzzing
introduce CCTS, a method for microservices verifica-
approach, known as MicroFuzz, developed by Di
tion through contract testing.
etal. [101], focuses on facilitating the implementation
6. Quality characteristics
of existing fuzzing strategies within Microservice soft-
ware. Rather than aiming to enhance these strategies, We found the analysis proposed by Gong and Cai
MicroFuzz is designed to offer support and streamline [42] for creating a quality model for microservices’
their implementation. The tool has demonstrated needs with the support of software quality standards.
effectiveness in identifying genuine vulnerabilities The objective of the proposal is to enhance service
within Microservice environments. quality and improve the overall quality of microser-
vices applications. Lastly, Meng et al. [108] put for-
v. Testing capability
ward a method for modeling and verifying systems
For testing capability, we have the method pro-
based on microservices.
posed by Vassiliou-Gioles [45], which involves intro-
(3) Testing tools
ducing an identifier in the HTTP headers to enhance
the testing capability of microservices. In this section, considering the tools listed in Table
15, we identify the most used tools for testing micros-
(c) Regression testing
ervices. It is important to note that the literature
For this other testing objective, we encounter vari-
mainly focuses on presenting the tools and their usage
ous approaches concerning regression testing. These
context. We found little information regarding com-
include regression test selection [56, 53], prioritiza-
parisons, effectiveness, adoption, or trade-offs.
tion [102], and the automation of this activity [50,
Regarding tools found, Pact is one of the most popular
103].
tools for contract testing, and it is aimed at consumer-
3. Industry perception driven testing [42].
In our selection, we identified two particularly Other popular tools in the industry are Selenium,
interesting studies that provide empirical research by JUnit, and JMeter [107]. Selenium is focused on end-
illustrating the industry’s perception of testing and to-end and system testing [106, 66, 55, 10]. In the case
software quality. of JMeter, it is primarily used for load testing [65, 37,
The first is the study by Bogner et al. [59], who 89, 15, 39, 58] and integration testing [55]. Addition-
conducted 17 interviews with professionals from 10 ally, JUnit is the most used tool in the industry for
different German companies. Their findings highlight conducting unit tests on microservices, according to
that security is the primary quality attribute affected the findings of the study by Waseem et al. [10].
by the use of microservices. Another highly mentioned tool in primary studies
On the other hand, Waseem et al. [10] conducted a is Locust, which aids in creating load tests [43, 65, 87,
mixed-methods study that included a broad survey 99, 39, 63, 98]. Additionally, findings from the study
with 106 responses and six interviews with microser- by Waseem et al. [10] position Mocha as an important
vices specialists. Among their findings, it is high- tool in the industry. Another open-source option for
lighted that end-to-end testing and contract testing are load generation is K6 [74]. When it comes to monitor-
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 569
ing microservices, a valuable practice for assessing the strategies and tools to attain satisfactory levels of auto-
performance of MSA-based systems, it is noted that mation within the microservices paradigm.
one of the most used tools for this purpose is Zipkin Concerning maintainability assessment, Abdelfat-
[75, 56, 76, 89, 15, 10]. tah [83] highlights the lack of specific quality assess-
In the field of fault injection, Istio is regarded as the ment techniques. Current methodologies frequently
ideal tool for this and other purposes, as it presents a overlook the distinct characteristics and complexities
mesh of services [98]. This is evidenced by the signifi- of microservice architecture, leading to shortcomings
cant number of studies utilizing it [37, 65, 14, 71, 38, in maintainability assessment.
98]. There are other fault injection tools mentioned in Regarding integration testing, its complexity pri-
the literature, like ChaosMesh, Gremlin’s ALFI, Lit- marily comes from the high number of interactions
mus, RainMaker, and Filibuster [68]. One option for between components [14] and the developers’ lack of
fault injection capabilities in database queries is AWS knowledge about the characteristics of the operating
Aurora. However, it is important to note that deliber- environment or user behavior [49]. One solution to
ately causing a crash in the database instance can lead address these challenges is the use of mocking tools,
to undesirable consequences, including data corrup- enabling the simulation of specific component behav-
tion, prolonged downtime, or even data loss [68]. iors to facilitate testing.
Considering fuzzers, options include [101] AFL, The implementation of end-to-end testing is
libFuzzer, and honggfuzz. Recent advancements in another challenge; its difficulty lies in creating and
LLMs have introduced tools such as TitanFuzz and maintaining the testing environment. To properly
FuzzGPT, as referenced in [101]. evaluate a microservices-based system, deploying the
entire system is necessary, which entails a high con-
For API testing, Li et al. [58] highlight that Enter-
sumption of resources. Furthermore, restoring the
prise-level API testing primarily consists of code-
environment after testing requires an important
based and tool-based approaches. Code-based API
investment of time and effort [42]. These tests are also
testing predominantly relies on RESTful APIs devel-
considered unstable and prone to failure [16]. They are
oped with frameworks like Spring Boot. On the other
expensive to develop, slow to execute, and require the
hand, tool-based API testing utilizes tools such as Curl
complete deployment of the system [71]. Another
commands, graphical interfaces like Postman or
issue with end-to-end testing is that it can lead to sev-
SoapUI, and performance testing tools like JMeter.
eral problems during the testing process. These
Finally, Sock Shop holds significance in microser-
include delivery delays, the emergence of hard-to-iso-
vices testing research [91], as it is the most used micro-
late errors, and conflicts in assigning responsibilities
services benchmarking system in the literature [37, 43,
[10].
60, 105, 65, 89, 15, 47]. This is due to its fidelity to rep-
A few years ago, it was reported that research on
resent the behavior of a real microservices system [87].
microservices testing primarily focused on functional
(4) Challenges in the testing process aspects rather than characteristics like performance
The industry reports that microservices testing has [40]. However, our selection includes a series of works
important challenges, such as the creation and imple- that address problems associated with evaluating qual-
mentation of manual tests, integration testing, debug- ity attributes such as performance, scalability, security,
ging microservices in containerization platforms, and or reliability [43, 70, 86, 60, 85, 76, 44, 41, 15].
the automation of tests [10]. In the case of manual Cooper et al. [74] mention challenges in integrating
tests, they do not meet the requirements of microser- CI/CD, particularly in performance testing. With
vices as distribution makes manual testing difficult CI/CD advocating frequent software updates, devel-
[13]. This issue impacts various testing levels, such as opers face a dilemma: either conduct time-consuming
regression testing [50], security testing [67], and per- performance tests on potentially outdated systems or
formance anomaly detection [91]. Yılmaz and resort to shorter, less accurate tests that do not offer a
Buzluca [52] also note that the size of a microservices- realistic evaluation of system performance. To compli-
based system generates challenges during testing. Test- cate performance testing further, Cooper et al. [74]
ing a microservice with an extensive number of meth- note that the abundance of diverse services compli-
ods can lead to difficulties and the risk of incomplete cates workload analysis and preparation. This com-
test coverage. plexity brings challenges in guaranteeing system per-
Similarly, Wang et al. [69] and also Huang et al. formance and reliability. Di et al. [101] remark on the
[92] mention that manual testing of microservices is high cost of regression testing, as running all test cases
complex, stressing the need to explore solutions for for the software under test after each change can be
test automation and the development of key technolo- expensive.
gies for microservices-based systems. These research Also, related to performance testing, D’Angelo and
efforts try to enhance software quality, work effi- D’Aloisio [90] mention that many proposed methods
ciency, and improve management. De Angelis et al. for detecting performance anomalies utilize machine
[53] stress that testing activities necessitate specific learning (ML) algorithms. While leveraging these
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

570 BELLO-TREJO et al.
techniques can be effective for anomaly detection, the [78]. According to Detti et al. [37], researchers wishing
training and deployment of ML methods often prove to test their findings on large-scale applications, such
inefficient in terms of the time, computational as those composed of hundreds of microservices, face
resources, and energy consumption they require. a significant limitation: either they work in companies
When discussing anomaly detection, Wang et al. [94] that possess such systems, like Netflix or Google, or
highlight that various system operators have differing they simply do not have access to them. This signifi-
approaches to managing anomalies, making it difficult cantly restricts the possibility of comparative evalua-
for existing techniques to satisfy all operator require- tion for many researchers in this field. Chen et al. [99]
ments simultaneously. While numerous anomaly reinforce this limitation by highlighting that chaos
detection methods have been introduced in recent experiments in the literature are conducted outside
years, implementing them directly in an industrial production environments, and testing without a pro-
environment remains a significant challenge. duction workload is inadequate for uncovering flaws
in resiliency mechanisms.
Regarding resilience testing, Assad et al. [68] point
out a crucial issue with many fault injection tools. While options like Sock Shop are widely recog-
These tools often treat databases merely as container- nized as one of the most used microservices systems
ized services, lacking the capability to inject faults into due to their ability to emulate some aspects of real
database clients. By focusing on the container layer, application behavior, their scope remains limited. This
these tools fall short in replicating real-world scenarios system, like others of its kind, fails to accurately repli-
where databases operate independently of containers. cate the complexity and scale of applications based on
This limitation hampers the effective testing of system hundreds of microservices. Consequently, its use does
resilience in environments where databases exist out- not generate the confidence to fully validate research-
side containers. ers’ findings, especially in scenarios that need more
Concerning fuzzing testing, Di et al. [101] point rigorous and representative evaluations [105, 63]. This
out that adapting fuzzing techniques for microservices highlights the need to develop more advanced and
encounters challenges coming from the differences comprehensive tools that can overcome these limita-
between monolithic and distributed software architec- tions. Rashmi et al. [38] also address this limitation
tures. Existing fuzzers struggle to effectively handle concerning benchmarking tools, discussing their
the complexity of microservices, primarily due to their inherent focus on single-tier applications or, at most,
inability to address the inconsistency issue prevalent in services with two or three tiers.
microservices. This inconsistency is a result of the
unpredictable runtime logic inherent in microservice
5. DISCUSSION
frameworks. Compounded by the decentralized
deployment of microservice applications in separate One of the most significant findings of our research
containers, the communication overhead between the is the challenging nature of defect localization resulting
target applications and the fuzzer is an important fac- from the distributed communication among microser-
tor for achieving efficiency. vices, which leads to increased costs associated with tra-
Zhang et al. [96] also highlight challenges in fault ditional verification methods [16]. In contrast to tradi-
diagnosis, understanding fault diagnosis as the classi- tional architectures such as monolithic styles [42],
fication and localization of faults for failed test cases. microservices present complex dependencies between
Not all logs within a failed test case are linked to faults. services or components, potentially yielding imprecise
These non-fault-related logs constitute a significant testing results when using different testing environ-
portion, impeding diagnosis models from accurately ments. Furthermore, microservices may experience
identifying fault features. Current methods struggle to mutual development effects due to uneven progress in
distinguish between these irrelevant log entries and the development and minor changes in services; the com-
pertinent ones effectively, and also have to deal with plex dependencies among services also create new
disparities in the formats of the logs. challenges related to ensuring the quality of functions,
performance, and system security [16].
Giamattei et al. [63] emphasize challenges in black
box testing, noting that tools often demand separate While prevalent testing techniques, such as integra-
testing sessions for each edge microservice. This tion, performance, or end-to-end tests [107], are
approach becomes less scalable as the number of already well-established, they continue to present new
microservices increases. Moreover, interactions challenges [10, 40, 71, 74]. The same applies to other
between microservices can lead to intricate invocation tests, like regression tests and microservice fault toler-
chains involving internal services within a real-scale ance [14].
application. When these chains are inadequately cov-
The findings highlight that, despite significant
ered by the test suite, failures may go undetected.
advancements in understanding microservice testing,
One of the most concerning challenges in micros- there are fundamental challenges that require collabo-
ervices testing is the lack of systems that represent the ration between academia and industry to address
actual behavior of real microservices-based systems them. Aligning practical industry needs with academic
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 571
proposals can bridge current gaps, aiding in the adop- these processes and streamline the development and
tion of more efficient solutions. management of microservices.
Based on the findings presented in this work, we Interesting new developments powered by AI [82,
propose the following research areas to drive future 94] have also emerged in the last few years of our
work and advance the field of testing in microservices- investigation. We believe this could be a new trend in
based systems: the coming years, as Generative AI becomes more
• automation of test subprocesses and activities prevalent. Additionally, emerging trends in the MAS
architecture, including testing, are discussed in [110].
• security testing
• performance, scalability, and reliability testing
6. THREATS TO VALIDITY
• reference systems are provided for researchers
AND LIMITATIONS
• automation of test-driven development processes
Although we took precautionary measures, our
• studies addressing comparisons of microservices
study presents certain limitations, which we address in
testing tools, along with adoption barriers
this section.
• studies addressing the testing of microservices-
(a) Internal validity
based systems in the context of microservices deploy-
ment, as described in [109]. Internal validity issues refer in this case to problems
As highlighted throughout this work, the develop- in the application of the research methodology that
ment of automation tools is critical for managing the may hinder research control. In this regard, although
increasing complexity of distributed systems. These we utilized an objective strategy supported by a tool for
tools should be able to identify defects in highly extracting search terms, the search strings were still
dynamic environments, reduce manual intervention, manually crafted. Furthermore, our selection criteria
and ensure test repeatability. This enables developers may have imposed constraints on our selection pro-
and testers to detect failures with greater precision and cess.
at a lower cost. It is also worth noting that the synthesized data are
Furthermore, future research is needed to address subject to interpretation, which may introduce bias
the vulnerabilities that arise from the increasing num- into our results and conclusions. However, we con-
ber of system entry points resulting from the modular ducted discussions on data synthesis techniques and
design of microservices. It is worth noting that existing tools to enhance the accuracy of our findings.
research predominantly centers around security Additionally, although we recognize that thematic
aspects using fuzzing testing. Therefore, prioritizing synthesis emerges from codes, there may not be a
the development of tests and analysis tools to mitigate direct link between one or more of them. The thematic
these risks is an important requirement. formulation, based on our domain knowledge related
In terms of performance testing, although it is a to the research object, could have posed a threat to
trend and extensive research dedicated to assessing validity, being one of the limitations of thematic syn-
this quality attribute, a more specific focus is required thesis, as the relationships identified between codes
on simulating the behavior of systems comprising might be inaccurate. This could impact the interpreta-
hundreds of microservices. This approach would lead tions, limiting the analysis. To address this risk, we
to more accurate and reliable performance characteri- conducted a thorough search for references and infor-
zation. Additionally, investigating the relationship mation sources with recognized validity, enabling us to
between performance, scalability, and reliability infer and strengthen these relationships more robustly.
would enhance the quality of microservices-based sys- (b) External validity
tems. This is closely aligned with the necessity of hav-
External validity issues refer to the limited general-
ing microservices systems that simulate the behavior of
ization of findings, which may impact the relevance of
applications from large enterprises such as Netflix or
the study.
Google. This approach would generate more confi-
dence in the results of future research. In this case, the number of manually selected rele-
vant studies for our search query selection may be con-
Lastly, integrating practices such as DevOps,
sidered limited, despite our efforts to identify pertinent
CI/CD, and agile methodologies into microservice
studies at this stage. To mitigate this, we ensured that
testing not only reduces development timelines but
the manually selected studies for our QGS were repre-
also enhances efficiency. These practices focus on
sentative and encompassed all research questions.
continuous quality control by ensuring ongoing evalu-
ation throughout the software development lifecycle, We also encountered restricted access to research
enabling early detection and correction of issues, and studies in certain cases, which could have resulted in
improving the final product quality. The inclusion of the exclusion of relevant studies. Nevertheless, we
these practices is a new trend in the literature; how- mitigated this risk by expanding the study selection
ever, it is important to have more tools that support through a snowball search.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

572 BELLO-TREJO et al.
Finally, we do not consider paper indexing data- Furthermore, we conclude that collaboration
bases such as Scopus and Web of Science, as we between industry and academia is vital to bridging
focused our research on computer science sources; existing gaps and ensuring that proposed solutions are
this could have limited the scope of our research. practical in real-world settings. Only through this syn-
ergy can challenges related to aspects such as scalabil-
ity, security, and performance be effectively addressed.
7. CONCLUSIONS
For our upcoming research, we intend to delve into
In this concluding section, we present a summary a study focused on root cause analysis (RCA) testing
of findings derived from conducting an SLR and ana- within the context of microservices. RCA testing aims
lyzing them through thematic synthesis, resulting in to identify and resolve the underlying causes of prob-
the thematic map presented in Fig. 9. We also reflect lems within microservices-based systems. We observed
on our results and highlight the benefits of our that this is a prevalent topic in microservices testing.
research, which is aimed at practitioners and software Due to its extensive coverage in the literature, we ini-
engineering researchers interested in microservices tially decided to exclude this subject to further detail
development. the rest of the area concerning microservices testing.
Integrating RCA testing into the findings of this study
Our study presents an SLR guided by four research
will provide a comprehensive view of microservices
questions, covering the state of the art in microservice-
testing, as covered in the literature.
based systems testing from 2018 to 2024. We selected
76 studies, 12 of which were obtained via backward In conclusion, our investigation exemplifies that
snowballing. The outcomes of this research reveal key while microservices represent an advancement over
test strategies, challenges, tools, and proposals in monolithic architectures, they present additional
microservices-based testing. The results indicate that challenges that must be addressed for successful adop-
while microservices represent an evolution from tion. Integrating best practices, innovative tools, and a
monolithic and SOA architectures, they also pose new collaborative approach between industry and aca-
challenges concerning testing, security, and perfor- demia are key elements to overcome these challenges.
mance. For researchers and practitioners, the results of this
study can provide a deeper understanding of current
This research provides an overview of the state of
issues and offer guidance for future research and
the art in testing for microservice-based systems, a
development in the field of microservices.
topic gaining increasing significance as more compa-
nies and organizations adopt this architecture for their
applications and services. Through an exhaustive sys-
FUNDING
tematic review and thematic analysis of selected stud-
ies, we have identified critical areas that practitioners This work was supported by ongoing institutional fund-
and researchers may find useful. For practitioners ing. No additional grants to carry out or direct this particu-
interested in microservices development, this research lar research were obtained.
highlights the necessity for automation and standard-
ization in testing. Due to their inherently complex dis-
CONFLICT OF INTEREST
tributed nature, microservices require specific
approaches and specialized tools for effective testing. The authors of this work declare that they have no con-
Improving microservices testing automation has the flicts of interest.
potential to improve system quality and reduce time
and costs.
REFERENCES
Additionally, the research findings highlight the
importance of having simulation and continuous 1. Bello-Trejo, S., Limón, X., Ocharán-Hernández, J.O.,
monitoring tools. These resources are essential for and Hernández-González, L.A., System-oriented
ensuring the proper functioning of distributed systems testing on the microservices architecture: A systematic
literature review, 2024 12th International Conference in
in real-world scenarios, where microservice behavior
Software Engineering Research and Innovation (CONI-
can vary due to scalability or resource availability.
SOFT), Puerto Escondido, Mexico, 2024, IEEE,
Monitoring aid development teams to identify perfor-
2024, pp. 127–136.
mance or security issues early, which prevents critical
https://doi.org/10.1109/conisoft63288.2024.00026
failures that could impact the end-user experience or
2. Fowler, M. and Lewis, J., Microservices, 2014.
system stability.
https://martinfowler.com/articles/microservices.html.
For researchers interested in microservices devel- 3. Newman, S., Building Microservices: Designing Fine-
opment, this study provides a foundation to build new Grained Systems, O’Reilly, 2021.
solutions and advancements. Through a review of pre-
4. Larrucea, X., Santamaria, I., Colomo-Palacios, R.,
vious studies and an analysis of identified gaps, an
and Ebert, Ch., Microservices, IEEE Software, 2018,
opportunity arises to study key areas such as security, vol. 35, no. 3, pp. 96–100.
performance, and scalability of microservices further. https://doi.org/10.1109/ms.2018.2141030
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 573
5. Statista, Organizations’ adoption level of microservices ic and Automation Control Conference (ITNEC), Xi’an,
worldwide in 2021, 2021. https://www.statis- China, 2021, IEEE, 2021, vol. 5, pp. 1306–1309.
ta.com/statistics/1233937/microservices-adoption- https://doi.org/10.1109/itnec52019.2021.9587260
level-organization/.
18. Dragoni, N., Giallorenzo, S., Lafuente, A.L., Maz-
6. Thönes, J., Microservices, IEEE Software, 2015, zara, M., Montesi, F., Mustafin, R., and Safina, L.,
vol.32, no. 1, pp. 116–116. Microservices: Yesterday, today, and tomorrow, Pres-
https://doi.org/10.1109/ms.2015.11 ent and Ulterior Software Engineering, Mazzara, M. and
7. Jamshidi, P., Pahl, C., Mendonca, N.C., Lewis, J., Meyer, B., Eds., Cham: Springer, 2017, pp. 195–216.
and Tilkov, S., Microservices: The journey so far and https://doi.org/10.1007/978-3-319-67425-4_12
challenges ahead, IEEE Software, 2018, vol. 35, no. 3, 19. Ghani, I., Wan-Kadir, W.M.N., Mustafa, A., and
pp.24–35. Babir, M.I., Microservice testing approaches: A sys-
https://doi.org/10.1109/ms.2018.2141039 tematic literature review, Int. J. Integr. Eng., 2019,
8. Di Francesco, P., Malavolta, I., and Lago, P., Re- vol.11, no. 8, pp. 65–80.
search on architecting microservices: Trends, focus, 20. Waseem, M., Liang, P., Marquez, G., and Salle, A.D.,
and potential for industrial adoption, 2017 IEEE Inter- Testing microservices architecture-based applications:
national Conference on Software Architecture (ICSA), A systematic mapping study, 2020 27th Asia-Pacific
Gothenburg, Sweden, 2017, IEEE, 2017, pp. 21–30. Software Engineering Conference (APSEC), Singapore,
https://doi.org/10.1109/icsa.2017.24 2020, IEEE, 2020, pp. 119–128.
9. Soldani, J., Tamburri, D.A., and Van Den Heuvel, W.-J., https://doi.org/10.1109/apsec51365.2020.00020
The pains and gains of microservices: A Systematic 21. Miao, T., Shaafi, A.I., and Song, E., Systematic map-
grey literature review, J. Syst. Software, 2018, vol. 146, ping study of test generation for microservices: Ap-
pp.215–232. proaches, challenges, and impact on system quality,
https://doi.org/10.1016/j.jss.2018.09.082 Electronics, 2025, vol. 14, no. 7.
10. Waseem, M., Liang, P., Shahin, M., Di Salle, A., and https://doi.org/10.3390/electronics14071397
Márquez, G., Design, monitoring, and testing of mi- 22. Silva, F., Lelli, V., Santos, I., and Andrade, R., To-
croservices systems: The practitioners’ perspective, J. wards a fault taxonomy for microservices-based appli-
Syst. Software, 2021, vol. 182, p. 111061. cations, Proceedings of the XXXVI Brazilian Symposium
https://doi.org/10.1016/j.jss.2021.111061 on Software Engineering, New York: Association for
11. Software Engineering, Sommerville, I., Ed., Pearson, Computing Machinery, 2022, pp. 247–256.
2016. https://doi.org/10.1145/3555228.3555245
12. Guide to the Software Engineering Body of Knowledge 23. Li, Sh., Zhang, H., Jia, Z., Zhong, Ch., Zhang, Ch.,
Editorial Committee, Guide to the Software Engineering Shan, Zh., Shen, J., and Babar, M.A., Understanding
Body of Knowledge (SWEBOK), IEEE, 2024, 4th ed. and addressing quality attributes of microservices ar-
chitecture: A systematic literature review, Inf. Software
13. Ding, H., Cheng, L., and Li, Q., An automatic test
Technol., 2021, vol. 131, p. 106449.
data generation method for microservice application,
https://doi.org/10.1016/j.infsof.2020.106449
2020 International Conference on Computer Engineering
and Application (ICCEA), Guangzhou, China, 2020, 24. Kitchenham, B.A., Budgen, D., and Brereton, P., Evi-
IEEE, 2020, pp. 188–191. dence-Based Software Engineering and Systematic Re-
https://doi.org/10.1109/iccea50009.2020.00048 views, Chapman and Hall/CRC, 2015.
https://doi.org/10.1201/b19467
14. Baptista, G., Correia, J., Bento, A., Soares, J., Ferreira, A.,
Duraes, J., Barbosa, R., and Araujo, F., Defektor: An 25. Zhang, H., Babar, M.A., and Tell, P., Identifying rele-
extensible tool for fault injection campaign manage- vant studies in software engineering, Inf. Software
ment in microservice systems, Proceedings of the 38th Technol., 2011, vol. 53, no. 6, pp. 625–637.
ACM/SIGAPP Symposium on Applied Computing, Tal- https://doi.org/10.1016/j.infsof.2010.12.010
linn, 2023, New York: Association for Computing Ma- 26. Wohlin, C., Guidelines for snowballing in systematic
chinery, 2023, pp. 184–187. literature studies and a replication in software engi-
https://doi.org/10.1145/3555776.3578809 neering, Proceedings of the 18th International Confer-
15. Wang, T., Zhang, W., Xu, J., and Gu, Z., Workflow- ence on Evaluation and Assessment in Software Engi-
aware automatic fault diagnosis for microservice-based neering, London, 2014, New York: Association for
applications with statistics, IEEE Trans. Network Ser- Computing Machinery, 2014, p. 38.
vice Manage., 2020, vol. 17, no. 4, pp. 2350–2363. https://doi.org/10.1145/2601248.2601268
https://doi.org/10.1109/tnsm.2020.3022028 27. Cruzes, D.S. and Dybå, T., Research synthesis in soft-
16. Li, H., Wang, J., Dai, H., and Lv, B., Research on mi- ware engineering: A tertiary study, Inf. Software Tech-
croservice application testing system, 2020 IEEE 3rd nol., 2011, vol. 53, no. 5, pp. 440–455.
International Conference on Information Systems and https://doi.org/10.1016/j.infsof.2011.01.004
Computer Aided Education (ICISCAE), Dalian, China, 28. Haddaway, N.R., Macura, B., Whaley, P., and
2020, IEEE, 2020, pp. 363–368. Pullin,A.S., ROSES Reporting standards for system-
https://doi.org/10.1109/iciscae51034.2020.9236829 atic evidence syntheses: Pro forma, flow-diagram and
17. Duan, T., Li, D., Xuan, J., Du, F., Li, J., Du, J., and descriptive summary of the plan and conduct of envi-
Wu, Sh., Design and implementation of intelligent au- ronmental systematic reviews and systematic maps,
tomated testing of microservice application, 2021 Environmental Evidence, 2018, vol. 7, no. 1, p. 7.
IEEE 5th Information Technology,Networking,Electron- https://doi.org/10.1186/s13750-018-0121-7
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

574 BELLO-TREJO et al.
29. Meckenstock, J.-N., Shedding light on the dark side— ACM/SPEC International Conference on Performance
A systematic literature review of the issues in agile soft- Engineering, Edmonton, Canada, 2020, New York: As-
ware development methodology use, J. Syst. Software, sociation for Computing Machinery, 2020, pp. 138–
2024, vol. 211, p. 111966. 149.
https://doi.org/10.1016/j.jss.2024.111966 https://doi.org/10.1145/3358960.3379124
30. Kitchenham, B., Charters, S., et al., Guidelines for 41. Pietrantuono, R., Russo, S., and Guerriero, A., Test-
performing systematic literature reviews in software ing microservice architectures for operational reliabili-
engineering, 2007. ty, Software Testing, Verification and Reliability, 2020,
31. Rohunen, A., Rodriguez, P., Kuvaja, P., Krzanik, L., vol. 30, no. 2, p. e1725.
and Markkula, J., Approaches to agile adoption in large https://doi.org/10.1002/stvr.1725
settings: A comparison of the results from a literature anal-
42. Gong, J. and Cai, L., Analysis for microservice archi-
ysis and an industrial inventory, Product-Focused Software
tecture application quality model and testing method,
Process Improvement, Ali Babar, M., Vierimaa, M., and
2023 26th ACIS International Winter Conference on
Oivo, M., Eds., Lecture Notes in Computer Science,
Software Engineering, Artificial Intelligence, Networking
vol. 6156, Berlin: Springer, 2010, pp. 77–91.
and Parallel/Distributed Computing (SNPD-Winter),
https://doi.org/10.1007/978-3-642-13792-1_8
Talyuan, China, 2023, IEEE, 2023, pp. 141–145.
32. Usman, M., Mendes, E., Weidt, F., and Britto, R., Ef- https://doi.org/10.1109/snpd-win-
fort estimation in agile software development, Proceed- ter57765.2023.10223960
ings of the 10th International Conference on Predictive
43. Camilli, M. and Russo, B., Modeling performance of
Models in Software Engineering, Turin, 2014, New
microservices systems with growth theory, Empirical
York: Association for Computing Machinery, 2014,
Software Eng., 2022, vol. 27, no. 2, p. 39.
pp.82–91.
https://doi.org/10.1007/s10664-021-10088-0
https://doi.org/10.1145/2639490.2639503
44. Ünver, B. and Britto, R., Automatic detection of secu-
33. Dybå, T. and Dingsøyr, T., Empirical studies of agile
rity deficiencies and refactoring advises for microser-
software development: A systematic review, Inf. Soft-
vices, 2023 IEEE/ACM International Conference on
ware Technol., 2008, vol. 50, nos. 9–10, pp. 833–859.
Software and System Processes (ICSSP), Melbourne,
https://doi.org/10.1016/j.infsof.2008.01.006
Australia, 2023, IEEE, 2023, pp. 25–34.
34. Rodgers, M., Sowden, A., Petticrew, M., Arai, L.,
https://doi.org/10.1109/icssp59042.2023.00013
Roberts, H., Britten, N., and Popay, J., Testing meth-
odological guidance on the conduct of narrative syn- 45. Vassiliou-Gioles, T., Quality assurance of micro-ser-
thesis in systematic reviews, Evaluation, 2009, vol. 15, vices—When to trust your micro-service test results?,
no. 1, pp. 49–73. 2021 IEEE 21st International Conference on Software
https://doi.org/10.1177/1356389008097871 Quality, Reliability and Security Companion (QRS-C),
Hainan, China, 2021, IEEE, 2021, pp. 1–6.
35. Popay, J., Roberts, H., Sowden, A., Petticrew, M.,
https://doi.org/10.1109/qrs-c55045.2021.00024
Arai, L., Rodgers, M., Britten, N., Roen, K., Duffy, S., et
al., Guidance on the conduct of narrative synthesis in 46. Wu, N., Zuo, D., and Zhang, Zh., An extensible fault
systematic reviews, A Product from the ESRC Methods tolerance testing framework for microservice-based
Programme Version, 2006, vol. 1, no. 1, p. b92. cloud applications, Proceedings of the 4th International
36. ISO/IEC/IEEE (ISO/IEC/IEEE International Stan- Conference on Communication and Information Process-
dard) 29119-1:2022(E): Software and Systems Engi- ing, Qingdao, China, 2018, New York: Association for
neering—Software Testing—Part 1:General Concepts, Computing Machinery, 2018, pp. 38–42.
2022, pp. 1–60. https://doi.org/10.1145/3290420.3290476
37. Detti, A., Funari, L., and Petrucci, L., μ Bench: An 47. Zhou, X., Peng, X., Xie, T., Sun, J., Ji, Ch., Liu, D.,
open-source factory of benchmark microservice applica- Xiang, Q., and He, Ch., Latent error prediction and
tions, IEEE Trans. Parallel Distrib. Syst., 2023, vol. 34, fault localization for microservice applications by
no. 3, pp. 968–980. learning from system trace logs, Proceedings of the 2019
https://doi.org/10.1109/tpds.2023.3236447 27th ACM Joint Meeting on European Software Engi-
neering Conference and Symposium on the Foundations
38. Rashmi, M.S., Vismaya, R., Patil, A., Rani, G.R.,
of Software Engineering, Tallinn, 2019, New York: As-
Borkade, T.N., and Auradkar, P., Synthetic to real-
sociation for Computing Machinery, 2019, pp. 683–
world: Insights on microservices-based application
694.
benchmarks, 2024 IEEE International Conference on
https://doi.org/10.1145/3338906.3338961
Information Technology, Electronics and Intelligent
Communication Systems (ICITEICS), Bangalore, In- 48. Naik, S. and D’Souza, M., Detection of faults in mi-
dia, 2024, IEEE, 2024, pp. 1–8. croservices using Petri nets, 16th Innovations in Soft-
https://doi.org/10.1109/iciteics61368.2024.10625221 ware Engineering Conference, Allahabad, India, 2023,
39. Flora, J. and Antunes, N., Evaluating intrusion detec- New York: Association for Computing Machinery,
tion for microservice applications: Benchmark, data- 2023, p. 17.
set, and case studies, J. Syst. Software, 2024, vol. 216, https://doi.org/10.1145/3578527.3578541
p.112142. 49. Gazzola, L., Goldstein, M., Mariani, L., Mobilio, M.,
https://doi.org/10.1016/j.jss.2024.112142 Segall, I., Tundo, A., and Ussi, L., ExVivoMicroTest:
40. Eismann, S., Bezemer, C.-P., Shang, W., Okanović, D., ExVivo testing of microservices, Journal of Software:
and Van Hoorn, A., Microservices: A performance tes- Evolution and Process, 2023, vol. 35, no. 4, p. e2452.
ter’s dream or nightmare?, Proceedings of the https://doi.org/10.1002/smr.2452
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 575
50. Kargar, M.J. and Hanifizade, A., Automation of re- 2020, vol. 165, p. 110564.
gression test in microservice architecture, 2018 4th In- https://doi.org/10.1016/j.jss.2020.110564
ternational Conference on Web Research (ICWR), Teh- 61. Leitner, P. and Bezemer, C.-P., An exploratory study
ran, Iran, 2018, IEEE, 2018, pp. 133–137. of the state of practice of performance testing in java-
https://doi.org/10.1109/icwr.2018.8387249 based open source projects, Proceedings of the 8th
51. Quin, F. and Weyns, D., Seabyte: A self-adaptive mi- ACM/SPEC on International Conference on Perfor-
cro-service system artifact for automating a/b testing, mance Engineering, L’Aquila, Italy, 2017, New York:
Proceedings of the 17th Symposium on Software Engi- Association for Computing Machinery, 2017, pp. 373–
neering for Adaptive and Self-Managing Systems, ser. 384.
SEAMS ’22, Pittsburgh, PA, 2022, New York: Associ- https://doi.org/10.1145/3030207.3030213
ation for Computing Machinery, 2022, pp. 77–83. 62. Heinrich, R., Van Hoorn, A., Knoche, H., Li, F.,
https://doi.org/10.1145/3524844.3528081 Lwakatare, L.E., Pahl, C., Schulte, S., and Wettinger, J.,
52. Yılmaz, R. and Buzluca, F., A fuzzy logic-based quali- Performance engineering for microservices: Research
ty model for identifying microservices with low main- challenges and directions, Proceedings of the 8th
tainability, J. Syst. Software, 2024, vol. 216, p. 112143. ACM/SPEC on International Conference on Perfor-
https://doi.org/10.1016/j.jss.2024.112143 mance Engineering Companion, L’Aquila, Italy, 2017,
53. De Angelis, E., De Angelis, G., Pellegrini, A., and New York: Association for Computing Machinery,
Proietti, M., Inferring relations among test programs 2017, pp.223–226.
in microservices applications, 2021 IEEE International https://doi.org/10.1145/3053600.3053653
Conference on Service-Oriented System Engineering 63. Giamattei, L., Guerriero, A., Pietrantuono, R., and
(SOSE), Oxford, 2021, IEEE, 2021, pp. 114–123. Russo, S., Automated functional and robustness test-
https://doi.org/10.1109/sose52839.2021.00018 ing of microservice architectures, J. Syst. Software,
54. Lin, D., Liping, F., Jiajia, H., Qingzhao, T., Chang- 2024, vol. 207, p. 111857.
hua, S., and Xiaohui, Zh., Research on microservice https://doi.org/10.1016/j.jss.2023.111857
application testing based on mock technology, 2020 64. Murino, S., Ferrando, A., and Cabri, G., RVElastic: A
International Conference on Virtual Reality and Intelli- runtime verification framework for microservice sys-
gent Systems (ICVRIS), Zhangjiajie, China, 2020, tems, 2024 32nd International Conference on Enabling
IEEE, 2020, pp. 815–819. Technologies: Infrastructure for Collaborative Enterprises
https://doi.org/10.1109/icvris51417.2020.00200 (WETICE), Reggio Emilia, Italy, 2024, IEEE, 2024,
55. Sotomayor, J.P., Allala, S.Ch., Alt, P., Phillips, J., pp. 62–67.
King, T.M., and Clarke, P.J., Comparison of runtime https://doi.org/10.1109/wetice64632.2024.00020
testing tools for microservices, 2019 IEEE 43rd Annual 65. Karn, R.R., Das, R., Pant, D.R., Heikkonen, J., and
Computer Software and Applications Conference (COM- Kanth, R., Automated testing and resilience of micro-
PSAC), Milwaukee, WI, 2019, IEEE, 2019, vol. 2, service’s network-link using Istio service mesh, 2022
pp.356–361. 31st Conference of Open Innovations Association
https://doi.org/10.1109/compsac.2019.10232 (FRUCT), Helsinki, 2022, IEEE, 2022, pp. 79–88.
56. Chen, L.-Z., Wu, J., Yang, H.-Y., and Zhang, K., A https://doi.org/10.23919/fruct54823.2022.9770890
microservice regression testing selection approach 66. Smith, Sh., Robinson, E., Frederiksen, T., Stevens, T.,
based on belief propagation, J. Cloud Comput., 2023, Cerny, T., Bures, M., and Taibi, D., Benchmarks for
vol. 12, no. 1, p. 20. end-to-end microservices testing, 2023 IEEE Interna-
https://doi.org/10.1186/s13677-023-00398-7 tional Conference on Service-Oriented System Engineer-
57. Vocke, H., The practical test pyramid. https://martin- ing (SOSE), Athens, 2023, IEEE, 2023, pp. 60–66.
fowler.com/articles/practical-test-pyramid.html. Cit- https://doi.org/10.1109/sose58276.2023.00013
ed February 26, 2018. 67. Wang, W., Benea, A., and Ivancic, F., Zero-config
58. Li, N., Wang, J., Chen, Ch., and Hu, H., Application fuzzing for microservices, 2023 38th IEEE/ACM Inter-
of API automation testing based on microservice mode national Conference on Automated Software Engineering
in industry software, International Conference on Algo- (ASE), Luxembourg, 2023, IEEE, 2023, pp. 1840–
rithms Software Engineering and Network Security, 1845.
Nanchang, China, 2024, New York: Association for https://doi.org/10.1109/ase56229.2023.00036
Computing Machinery, 2024, pp. 460–464. 68. Assad, M., Meiklejohn, Ch.S., Miller, H., and Krus-
https://doi.org/10.1145/3677182.3677264 che, S., Can my microservice tolerate an unreliable da-
59. Bogner, J., Fritzsch, J., Wagner, S., and Zimmermann, tabase? Resilience testing with fault injection and visu-
A., Microservices in industry: Insights into technolo- alization, Proceedings of the 2024 IEEE/ACM 46th In-
gies, characteristics, and software quality, 2019 IEEE ternational Conference on Software Engineering:
International Conference on Software Architecture Com- Companion Proceedings, Lisbon, 2024, New York: As-
panion (ICSA-C), Hamburg, 2019, IEEE, 2019, sociation for Computing Machinery, 2024, pp. 54–58.
pp.187–195. https://doi.org/10.1145/3639478.3640021
https://doi.org/10.1109/icsa-c.2019.00041 69. Wang, Ya., Cheng, L., and Sun, X., Design and re-
60. Avritzer, A., Ferme, V., Janes, A., Russo, B., Hoorn, A.V., search of microservice application automation testing
Schulz, H., Menasché, D., and Rufino, V., Scalability framework, 2019 International Conference on Informa-
assessment of microservice architecture deployment tion Technology and Computer Application (ITCA),
configurations: A domain-based approach leveraging Guangzhou, China, 2019, IEEE, 2019, pp. 257–260.
operational profiles and load tests, J. Syst. Software, https://doi.org/10.1109/itca49981.2019.00063
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

576 BELLO-TREJO et al.
70. Lei, Q., Liao, W., Jiang, Yi., Yang, M., and Li, H., Per- (CLOUD), Chicago, 2023, IEEE, 2023, pp. 189–200.
formance and scalability testing strategy based on https://doi.org/10.1109/cloud60044.2023.00030
Kubemark, 2019 IEEE 4th International Conference on 79. Sriraman, A. and Wenisch, T.F., μ suite: A benchmark
Cloud Computing and Big Data Analysis (ICCCBDA), suite for microservices, 2018 IEEE International Sym-
Chengdu, China, 2019, IEEE, 2019, pp. 511–516. posium on Workload Characterization (IISWC), Ra-
https://doi.org/10.1109/icccbda.2019.8725658 leigh, NC, 2018, IEEE, 2018, pp. 1–12.
71. Reile, Ch., Chadha, M., Hauner, V., Jindal, A., https://doi.org/10.1109/iiswc.2018.8573515
Hofmann, B., and Gerndt, M., Bunk8s: Enabling easy 80. Zhou, X., Peng, X., Xie, T., Sun, J., Xu, Ch., Ji, Ch.,
integration testing of microservices in Kubernetes, and Zhao, W., Benchmarking microservice systems for
2022 IEEE International Conference on Software Analy- software engineering research, Proceedings of the 40th
sis, Evolution and Reengineering (SANER), Honolulu, International Conference on Software Engineering: Com-
HI, 2022, IEEE, 2022, pp. 459–463. panion Proceeedings, Gothenburg, Sweden, 2018, New
https://doi.org/10.1109/saner53432.2022.00062 York: Association for Computing Machinery, 2018,
pp.323–324.
72. Janes, A. and Russo, B., Automatic performance mon-
https://doi.org/10.1145/3183440.3194991
itoring and regression testing during the transition
from monolith to microservices, 2019 IEEE Interna- 81. Van Hoorn, A., Aleti, A., Dullmann, T.F., and Pita-
tional Symposium on Software Reliability Engineering krat, T., ORCAS: Efficient resilience benchmarking of
Workshops (ISSREW), Berlin, 2019, IEEE, 2019, microservice architectures, 2018 IEEE International
pp.163–168. Symposium on Software Reliability Engineering Work-
https://doi.org/10.1109/issrew.2019.00067 shops (ISSREW), Memphis, TN, 2018, IEEE, 2018,
pp.146–147.
73. Aktaş, K. and Kilinc, H.H., Interaction prediction and
https://doi.org/10.1109/issrew.2018.00-10
anomaly detection in a microservices-based telecom-
munication platform, Proceedings of the 2024 Interna- 82. Von Kistowski, J., Eismann, S., Schmitt, N., Bauer, A.,
tional Conference on Software and Systems Processes, Grohmann, J., and Kounev, S., TeaStore: A micro-
New York: Association for Computing Machinery, service reference application for benchmarking, mod-
2024, pp. 56–65. eling and resource management research, 2018 IEEE
https://doi.org/10.1145/3666015.3666017 26th International Symposium on Modeling, Analysis,
and Simulation of Computer and Telecommunication
74. Cooper, Q., Krishnamurthy, D., and Amannejad, Ya.,
Systems (MASCOTS), Milwaukee, WI, 2018, IEEE,
Budget aware performance test selection for microser-
2018, pp.223–236.
vices, 2024 IEEE 17th International Conference on
https://doi.org/10.1109/mascots.2018.00030
Cloud Computing (CLOUD), Shenzhen, China, 2024,
83. Abdelfattah, A.S., Fostering microservice maintain-
IEEE, 2024, pp. 376–385.
ability assurance through a comprehensive framework,
https://doi.org/10.1109/cloud62652.2024.00049
2024 IEEE International Conference on Software Main-
75. Ma, Sh., Liu, I., Chen, Ch., and Wang, Yu., Version- tenance and Evolution (ICSME), Flagstaff, AZ, 2024,
based and risk-enabled testing, monitoring, and visu- IEEE, 2024, pp. 838–842.
alization of microservice systems, Journal of Software: https://doi.org/10.1109/icsme58944.2024.00087
Evolution and Process, 2022, vol. 34, no. 10, p. e2429.
84. Almutawa, M., Ghabrah, Q., and Canini, M., Towards
https://doi.org/10.1002/smr.2429
LLM-assisted system testing for microservices, 2024
76. Gan, Yu., Zhang, Ya., Cheng, D., Shetty, A., Rathi, P., IEEE 44th International Conference on Distributed
Katarki, N., Bruno, A., Hu, J., Ritchken, B., Jackson, B., Computing Systems Workshops (ICDCSW), Jersey City,
Hu, K., Pancholi, M., He, Yu., Clancy, B., Colen, Ch., NJ, 2024, IEEE, 2024, pp. 29–34.
Wen, F., Leung, C., Wang, S., Zaruvinsky, L., Espino- https://doi.org/10.1109/icdcsw63686.2024.00011
sa, M., Lin, R., Liu, Zh., Padilla, J., and Delimitrou, Ch.,
85. Das, P., Laigner, R., and Zhou, Y., HawkEDA: A tool
An open-source benchmark suite for microservices
for quantifying data integrity violations in event-driven
and their hardware-software implications for cloud &
microservices, Proceedings of the 15th ACM Interna-
edge systems, Proceedings of the Twenty-Fourth Inter-
tional Conference on Distributed and Event-Based Sys-
national Conference on Architectural Support for Pro-
tems, New York: Association for Computing Machin-
gramming Languages and Operating Systems, Provi-
ery, 2021, pp. 176–179.
dence, RI, 2019, New York: Association for Comput-
https://doi.org/10.1145/3465480.3467838
ing Machinery, 2019, pp. 3–18.
86. Jindal, A., Podolskiy, V., and Gerndt, M., Perfor-
https://doi.org/10.1145/3297858.3304013
mance modeling for cloud microservice applications,
77. Bi, T., Pan, Yi., Jiang, X., Ma, M., and Wang, P., VE- Proceedings of the 2019 ACM/SPEC International Con-
CROsim: A versatile metric-oriented microservice ference on Performance Engineering, Mumbai, India,
fault simulation system (tools and artifact track), 2022 2019, New York: Association for Computing Machin-
IEEE 33rd International Symposium on Software Reli- ery, 2019, pp. 25–32.
ability Engineering (ISSRE), Charlotte, NC, 2022, https://doi.org/10.1145/3297663.3310309
IEEE, 2022, pp. 297–308.
87. Rahman, J. and Lama, P., Predicting the end-to-end
https://doi.org/10.1109/issre55969.2022.00037
tail latency of containerized microservices in the cloud,
78. Sedghpour, M.R.S., Duque, A.O., Cai, X., Skubic, B., 2019 IEEE International Conference on Cloud Engi-
Elmroth, E., Klein, C., and Tordsson, J., HydraGen: neering (IC2E), Prague, 2019, IEEE, 2019, pp. 200–
Amicroservice benchmark generator, 2023 IEEE 16th 210.
International Conference on Cloud Computing https://doi.org/10.1109/ic2e.2019.00034
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

SOFTWARE TESTING ON MICROSERVICES-BASED SYSTEMS 577
88. Giamattei, L., Guerriero, A., Malavolta, I., Mascia, C., 125.
Pietrantuono, R., and Russo, S., Identifying perfor- https://doi.org/10.1145/3663529.3663833
mance issues in microservice architectures through
97. Long, Zh., Wu, G., Chen, X., Cui, Ch., Chen, W., and
causal reasoning, Proceedings of the 5th ACM/IEEE In-
Wei, J., Fitness-guided resilience testing of microser-
ternational Conference on Automation of Software Test
vice-based applications, 2020 IEEE International Con-
(AST 2024), Lisbon, 2024, New York: Association for
ference on Web Services (ICWS), Beijing, 2020, IEEE,
Computing Machinery, 2024, pp. 149–153.
2020, pp. 151–158.
https://doi.org/10.1145/3644032.3644460
https://doi.org/10.1109/icws49710.2020.00027
89. Schulz, H., Angerstein, T., Okanovic, D., and Van
98. Singh, Sh., Muntean, C.H., and Gupta, Sh., Boosting
Hoorn, A., Microservice-tailored generation of ses-
microservice resilience: An evaluation of Istio’s impact
sion-based workload models for representative load
on Kubernetes clusters under chaos, 2024 9th Interna-
testing, 2019 IEEE 27th International Symposium on
tional Conference on Fog and Mobile Edge Computing
Modeling, Analysis, and Simulation of Computer and
(FMEC), Malmö, Sweden, 2024, IEEE, 2024,
Telecommunication Systems (MASCOTS), Rennes,
pp.245–252.
France, 2019, IEEE, 2019, pp. 323–335.
https://doi.org/10.1109/fmec62297.2024.10710237
https://doi.org/10.1109/mascots.2019.00043
99. Chen, H., Chen, P., Yu, G., Li, X., and He, Z., Micro-
90. D’Angelo, A. and d’Aloisio, G., Grammar-based FI: Non-intrusive and prioritized request-level fault
anomaly detection of microservice systems execution injection for microservice applications, IEEE Trans.
traces, Companion of the 15th ACM/SPEC International Dependable Secure Comput., 2024, vol. 21, no. 5,
Conference on Performance Engineering, London, 2024, pp.4921–4938.
New York: Association for Computing Machinery, https://doi.org/10.1109/tdsc.2024.3363902
2024, pp. 77–81.
100.Rattanukul, P., Makaranond, Ch., Watanakulcharus, P.,
https://doi.org/10.1145/3629527.3651844
Ragkhitwetsagul, Ch., Nearunchorn, T., Visoottiv-
91. Hao, J., Chen, P., Chen, J., and Li, X., Multi-task fed- iseth, V., Choetkiertikul, M., and Sunetnanta, T., Mi-
erated learning-based system anomaly detection and crousity: A testing tool for backends for frontends
multi-classification for microservices architecture, Fu- (BFF) microservice systems, 2023 IEEE/ACM 31st In-
ture Gener. Comput. Syst., 2024, vol. 159, pp. 77–90. ternational Conference on Program Comprehension
https://doi.org/10.1016/j.future.2024.05.006 (ICPC), Melbourne, 2023, IEEE, 2023, pp. 74–78.
92. Huang, J., Yang, Ya., Yu, H., Li, J., and Zheng, X., https://doi.org/10.1109/icpc58990.2023.00021
Twin graph-based anomaly detection via attentive 101.Di, P., Liu, B., and Gao, Yi., MicroFuzz: An efficient
multi-modal learning for microservice system, 2023 fuzzing framework for microservices, Proceedings of the
38th IEEE/ACM International Conference on Automat- 46th International Conference on Software Engineering:
ed Software Engineering (ASE), Luxembourg, 2023, Software Engineering in Practice, Lisbon, 2024, New
IEEE, 2023, pp. 66–78. York: Association for Computing Machinery, 2024,
https://doi.org/10.1109/ase56229.2023.00138 pp.216–227.
93. Li, Zh., Zhao, J., and Kang, J., Multi-source anomaly https://doi.org/10.1145/3639477.3639723
detection for microservice systems, Proceedings of the 102.Chen, L., Yu, X., Wu, J., and Yang, H., CIPC: A
2024 IEEE/ACM 46th International Conference on Soft- change impact propagation computing based tech-
ware Engineering: Companion Proceedings, Lisbon, nique for microservice regression testing prioritization,
2024, New York: Association for Computing Machin- Mobile Information Systems, 2021, vol. 2021, no. 1,
ery, 2024, pp. 414–415. p.2912240.
https://doi.org/10.1145/3639478.3643535 https://doi.org/10.1155/2021/2912240
94. Wang, Ch., Huang, T., Li, M., Chen, P., and Chen, Zh., 103.Elsner, D., Bertagnolli, D., Pretschner, A., and Klaus, R.,
A Bayesian LSTM based active anomaly detection ser- Challenges in regression test selection for end-to-end
vice for large online systems, Proceedings of the 15th testing of microservice-based software systems, Pro-
Asia-Pacific Symposium on Internetware, Macau, Chi- ceedings of the 3rd ACM/IEEE International Conference
na, 2024, New York: Association for Computing Ma- on Automation of Software Test, Pittsburgh, PA, 2022,
chinery, 2024, pp. 407–416. New York: Association for Computing Machinery,
https://doi.org/10.1145/3671016.3674818 2022, pp. 1–5.
https://doi.org/10.1145/3524481.3527217
95. Zhou, X., Peng, X., Xie, T., Sun, J., Ji, Ch., Li, W., and
Ding, D., Fault analysis and debugging of microservice 104.Quenum, J.G. and Aknine, S., Towards executable
systems: Industrial survey, benchmark system, and specifications for microservices, 2018 IEEE Interna-
empirical study, IEEE Trans. Software Eng., 2021, tional Conference on Services Computing (SCC), San
vol.47, no. 2, pp. 243–260. Francisco, 2018, IEEE, 2018, pp. 41–48.
https://doi.org/10.1109/tse.2018.2887384 https://doi.org/10.1109/scc.2018.00013
96. Zhang, Sh., Zhu, J., Hao, B., Sun, Yo., Nie, X., Zhu, J., 105.Giamattei, L., Guerriero, A., Pietrantuono, R., and
Liu, X., Li, X., Ma, Yu., and Pei, D., Fault diagnosis Russo, S., Automated grey-box testing of microservice
for test alarms in microservices through multi-source architectures, 2022 IEEE 22nd International Confer-
data, Companion Proceedings of the 32nd ACM Interna- ence on Software Quality, Reliability and Security
tional Conference on the Foundations of Software Engi- (QRS), Guangzhou, China, 2022, IEEE, 2022,
neering, Porto de Galinhas, Brazil, 2024, New York: pp.640–650.
Association for Computing Machinery, 2024, pp. 115– https://doi.org/10.1109/qrs57517.2022.00070
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025

578 BELLO-TREJO et al.
106.Ma, S.-P., Yang, Y.-Y., Lee, S.-J., and Yeh, H.-W., 109.Niño-Martínez, V.M., Ocharán-Hernández, J.O.,
UTEMS: A unit testing scheme for event-driven mi- Limón, X., and Pérez-Arriaga, J.C., A microservice
croservices, 2023 10th International Conference on De- deployment guide, Program. Comput. Software, 2022,
pendable Systems and Their Applications (DSA), Tokyo, vol. 48, no. 8, pp. 632–645.
2023, IEEE, 2023, pp. 591–592. https://doi.org/10.1134/s0361768822080151
https://doi.org/10.1109/dsa59317.2023.00085
110.Stojanov, Z., Hristoski, I., Stojanov, J., and Stojkov, A.,
107.Wu, C.-F., Ma, S.-P., Shau, A.-C., and Yeh, H.-W.,
Testing for event-driven microservices based on con- A tertiary study on microservices: Research trends and
sumer-driven contracts and state models, 2022 29th recommendations, Program. Comput. Software, 2023,
Asia-Pacific Software Engineering Conference (APSEC), vol. 49, no. 8, pp. 796–821.
IEEE, 2022, pp. 467–471. https://doi.org/10.1134/s0361768823080200
https://doi.org/10.1109/apsec57359.2022.00064
108.Meng, X., Duan, X., Tao, W., Luan, Ya., Zhang, J.,
Publisher’s Note. Pleiades Publishing remains
and Wu, D., Modeling and verification of industrial
neutral with regard to jurisdictional claims in
microservice architecture based on formal methods,
published maps and institutional affiliations.
2021 China Automation Congress (CAC), Beijing, 2021,
IEEE, 2021, pp. 3776–3780. AI tools may have been used in the translation or
https://doi.org/10.1109/cac53003.2021.9727653 editing of this article.
PROGRAMMING AND COMPUTER SOFTWARE Vol. 51 No. 8 2025