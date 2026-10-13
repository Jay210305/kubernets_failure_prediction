| Revista     | Innovación y Software      |     |      |     |                                  |     |
| ----------- | -------------------------- | --- | ---- | --- | -------------------------------- | --- |
|             |                            |     |      |     | Esta obra está bajo una Licencia |     |
| Vol. 5, No. | 2, Mes Septiembre-Febrero, |     | 2024 |     |                                  |     |
|             |                            |     |      |     | Creative Commons Atribución      |     |
ISSN: 2708-0935
4.0 Internacional.
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
Identificadores persistentes:
| Tipo de | artículo: Artículos | originales |     |     |     |     |
| ------- | ------------------- | ---------- | --- | --- | --- | --- |
DOI:10.48168/innosoft.s16.a177
| Temática: | Inteligencia | Artificial |     |     |     |     |
| --------- | ------------ | ---------- | --- | --- | --- | --- |
ARK:
Recibido: 19/05/2024 | Aceptado: 06/08/2024 | Publicado: 30/09/2024 ark:/42411/s16/a177
PURL: 42411/s16/a177
Inteligencia artificial en la gestión predictiva de incidentes de TI
| Artificial | intelligence |     | in predictive | IT incident | management |     |
| ---------- | ------------ | --- | ------------- | ----------- | ---------- | --- |
Luigui Jampierre Amaya Jave1[0009-0001-3170-6298]*, Roger Alejandro Querevalú
Galán2[0009-0002-2479-1081], Alberto Carlos Mendoza de los Santos3[0000-0002-0469-915X]
1Universidad Nacional de Trujillo. Trujillo, Perú. ljamayaj@unitru.edu.pe
2Universidad Nacional de Trujillo. Trujillo, Perú. rquerevalu@unitru.edu.pe
3Universidad Nacional de Trujillo. Trujillo, Perú. correo@dominio.com
∗Autor
|     | para correspondencia: |     | amendozad@unitru.edu.pe |     |     |     |
| --- | --------------------- | --- | ----------------------- | --- | --- | --- |
Resumen
Esta revisión sistemática sintetiza la literatura sobre la aplicación de la inteligencia artificial (IA) en la gestión
predictiva de incidentes de Tecnologías de la Información (TI). El estudio se enfoca en evaluar la capacidad
predictiva de las soluciones basadas en IA y en identificar áreas de oportunidad para investigaciones futuras.
Utilizando la metodología PRISMA, se realizaron búsquedas exhaustivas en bases de datos académicas utili-
zando ecuaciones de búsqueda específicas. Se seleccionaron 15 artículos que abordan el tema desde diferentes
perspectivas, destacando el uso de técnicas avanzadas como machine learning, deep learning y transformadores
para mejorar la precisión en la predicción de incidentes de TI. Además, se exploró cómo la IA para Operaciones
de TI (AIOps) facilita la automatización y gestión proactiva de incidentes, optimizando así la eficiencia opera-
tiva y la disponibilidad del sistema. Los hallazgos resaltan la efectividad de estas tecnologías en la reducción
del tiempo de resolución de incidentes y en la mejora de la resiliencia organizacional frente a desafíos tecnoló-
gicos emergentes. En conjunto, esta revisión subraya la importancia de la innovación continua y la integración
estratégica de IA en la gestión de servicios de TI para mejorar la eficiencia operativa y fortalecer la capacidad
| de adaptación | de las | organizaciones. |     |     |     |     |
| ------------- | ------ | --------------- | --- | --- | --- | --- |
Palabras claves: incidentes de TI, inteligencia artificial, gestión predictiva.
Abstract
This systematic review synthesizes the literature on the application of Artificial Intelligence (AI) in predictive
incident management in Information Technology (IT). The study focuses on evaluating the predictive capability
of AI-based solutions and identifying areas for future research. Using the PRISMA methodology, comprehensive
searches were conducted in academic databases using specific search equations. Fifteen articles were selected
that addressed the topic from various perspectives, highlighting the use of advanced techniques such as machine
learning, deep learning, and transformers to enhance accuracy in predicting IT incidents. Furthermore, it ex-
plored how AI for IT Operations (AIOps) facilitates the automation and proactive management of incidents,
thereby optimizing operational efficiency and system availability. The findings underscore the effectiveness of
thesetechnologiesinreducingincidentresolutiontimesandimprovingorganizationalresilienceagainstemerging
technological challenges. Overall, this review emphasizes the importance of continuous innovation and strategic
integration of AI in IT service management to enhance operational efficiency and strengthen organizational
adaptability.
| Facultad    | de Ingeniería |           |      |     |     | 85  |
| ----------- | ------------- | --------- | ---- | --- | --- | --- |
| Universidad | La Salle,     | Arequipa, | Perú |     |     |     |
facin.innosoft@ulasalle.edu.pe

Revista Innovación y Software
Vol. 5, No. 2, Mes Septiembre-Febrero, 2024
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
Keywords: IT incidents, artificial intelligence, predictive management.
Introducción
Enestetrabajosedescribenlasaplicacionesdelainteligenciaartificial(IA)enlagestiónpredictivadeincidentes
deTecnologíasdelaInformación(TI).Lagestióndeincidentesesuncomponentecríticoparaelfuncionamiento
eficiente de las organizaciones, ya que los incidentes de TI pueden causar interrupciones significativas en los
servicios y operaciones. La capacidad de predecir y gestionar incidentes antes de que ocurran ofrece ventajas
sustanciales, reduciendo tiempos de inactividad y mejorando la eficiencia operativa.
La inteligencia artificial ha emergido como una herramienta poderosa en este ámbito, hasta el punto de que
existen algunas diseñadas para las operaciones de TI conocidas como AIOps (Inteligencia Artificial para Ope-
raciones). Varios estudios [1–5]. han sugerido que las AIOps están siendo utilizadas por las empresas para
afrontar los cambios y los incidentes de TI generados por estos. Además, según Remil [1,2] se empiezan a
explorar soluciones como el Descubrimiento de Subgrupos para analizar comportamientos más específicos. Sin
embargo, la literatura carece de una revisión sistemática que consolide estos esfuerzos y evalúe la efectividad
de las soluciones propuestas.
Enlaeraactual,lasinnovacionestecnológicashantransformadosignificativamentelamaneraenqueseabordan
losdesafíosrelacionadosconlaseguridadylasaludeneltrabajo.Desdeeldesarrollodesistemasdeinformación
avanzadoshastalaaplicacióndetécnicasdeaprendizajeautomáticoparalapredicciónderiesgos,laintegración
de tecnología se ha convertido en un pilar fundamental para mejorar los estándares de seguridad laboral [6,7].
Estasiniciativasnosolobuscanmitigarriesgosprevisibles,comolosrelacionadosconlatecnología,sinotambién
mejorar la gestión de incidentes mediante el uso de sistemas web especializados [8,9]. Este contexto refleja un
esfuerzo continuo por parte de diversas industrias para adaptarse y responder proactivamente a los desafíos
emergentes en materia prevención de riesgos.
Laintegracióndelainteligenciaartificial(IA)enlagestiónpredictivadeincidentesdetecnologíadelainforma-
ción (TI) representa un avance crucial en la mejora de la seguridad y eficiencia operativa en diversos contextos
organizacionales. Desde la prevención de pérdidas de datos críticos hasta la optimización de procesos internos
mediante la adopción de prácticas como ITIL V4 y el uso de mesas de ayuda basadas en IA, la aplicación de
tecnologías emergentes está redefiniendo los paradigmas tradicionales de gestión de incidentes [10–12].
Además, la investigación continúa explorando el potencial de la IA en la transformación de procesos educativos
y en la optimización de la interacción humano-IA para la creación de valor en ecosistemas de servicios [12,13].
Facultad de Ingeniería 86
Universidad La Salle, Arequipa, Perú
facin.innosoft@ulasalle.edu.pe

| Revista     | Innovación y Software      |     |      |     |     |     |
| ----------- | -------------------------- | --- | ---- | --- | --- | --- |
| Vol. 5, No. | 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
Este contexto subraya la importancia de una revisión sistemática para comprender a fondo las contribuciones
actuales y las tendencias futuras de la IA en la gestión proactiva de incidentes de TI.
El objetivo de este trabajo es revisar y sintetizar la literatura existente sobre la aplicación de IA en la gestión
predictiva de incidentes de TI. Se evalúa la capacidad predictiva de las soluciones basadas en IA y se identifican
áreas de oportunidad para futuras investigaciones. Este estudio se justifica por la necesidad de reducir los
tiempos de inactividad, minimizar los costos asociados a los incidentes de TI y mejorar la satisfacción del
usuario mediante la implementación de soluciones predictivas basadas en IA. En este contexto, se investiga
¿cómo se utiliza la inteligencia artificial para predecir incidentes de TI? y ¿qué tan efectiva es en mejorar la
| gestión  | de servicios    | de TI? |            |     |     |     |
| -------- | --------------- | ------ | ---------- | --- | --- | --- |
| Concepto | de Inteligencia |        | Artificial |     |     |     |
La Inteligencia Artificial (IA) se define como la capacidad de una máquina para imitar el comportamiento
humano, incluyendo habilidades como el aprendizaje, la toma de decisiones, el reconocimiento de patrones
y la resolución de problemas. En términos simples, la IA permite que las computadoras realicen tareas que
normalmente requieren inteligencia humana. Estas tareas pueden variar desde juegos y diagnósticos médicos
| hasta conducción | autónoma   |      | y procesamiento | del lenguaje | natural [14]. |     |
| ---------------- | ---------- | ---- | --------------- | ------------ | ------------- | --- |
| Inteligencia     | Artificial | para | Operaciones     | de TI        |               |     |
La Inteligencia Artificial para Operaciones de TI (AIOps, por sus siglas en inglés) se refiere al uso de IA
para mejorar y automatizar las operaciones de tecnología de la información. AIOps combina el aprendizaje
automático, el análisis de big data y otras tecnologías de IA para identificar, diagnosticar y resolver problemas
enentornosdeTIdemaneramáseficienteyproactiva[15].Estoincluyelacapacidaddepredecirincidentesantes
de que ocurran, lo que puede minimizar el tiempo de inactividad y mejorar la disponibilidad del sistema [16].
| Incidentes | de TI |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- |
Los incidentes de TI son eventos no planificados que causan una interrupción o una reducción en la calidad
del servicio de una infraestructura de tecnología de la información. Estos incidentes pueden variar desde fallos
en el hardware, problemas de red, errores de software, hasta ciberataques que comprometen la seguridad de
los datos [17]. La gestión efectiva de estos incidentes es crucial para minimizar el impacto en las operaciones
| comerciales | y asegurar | la continuidad | del | negocio [18]. |     |     |
| ----------- | ---------- | -------------- | --- | ------------- | --- | --- |
Con el avance de la inteligencia artificial, las técnicas predictivas están comenzando a jugar un papel signi-
ficativo en la gestión de incidentes de TI. Al analizar grandes volúmenes de datos y detectar patrones, los
sistemas basados en IA pueden anticipar posibles fallos antes de que ocurran, permitiendo una intervención
preventiva. Esto no solo mejora la eficiencia operativa, sino que también puede reducir significativamente los
| Facultad    | de Ingeniería |           |      |     |     | 87  |
| ----------- | ------------- | --------- | ---- | --- | --- | --- |
| Universidad | La Salle,     | Arequipa, | Perú |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |     |      |     |     |
| ------------------ | -------------------------- | --- | ---- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, |     | 2024 |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
costos asociados con el tiempo de inactividad y la pérdida de productividad [19].
| Gestión | de servicios | TIC |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
La gestión de servicios de tecnologías de la información (TIC) implica la implementación y administración
de servicios de TI que satisfacen las necesidades de una organización. Esta disciplina incluye un conjunto de
políticas y procedimientos diseñados para planificar, diseñar, entregar, operar y controlar los servicios de TI
| para clientes | internos | y externos | [20,21]. |     |     |
| ------------- | -------- | ---------- | -------- | --- | --- |
La inteligencia artificial (IA) está revolucionando la gestión de servicios de TI al mejorar la capacidad de
predicción y automatización de incidentes, optimizando la eficiencia operativa y la disponibilidad del sistema.
La integración de tecnologías como el aprendizaje automático y los sistemas de IA en operaciones de TI
(AIOps) permite una gestión proactiva y automatizada, reduciendo significativamente el tiempo de resolución
| de incidentes | y aumentando | la resiliencia | organizacional | [22]. |     |
| ------------- | ------------ | -------------- | -------------- | ----- | --- |
Servicio
En el contexto tecnológico contemporáneo, un servicio se define como una funcionalidad proporcionada por
sistemas informáticos que permite satisfacer necesidades específicas de usuarios o aplicaciones, generalmente
accesible a través de interfaces estandarizadas y protocolos de comunicación. Estos servicios pueden incluir
desde plataformas de inteligencia artificial que facilitan el procesamiento de datos y la toma de decisiones
automatizada,hastainfraestructurasdecómputoenlanubequeofrecenrecursosescalablessegúndemanda[23].
Esta definición destaca la importancia de la flexibilidad y la interoperabilidad para adaptarse a las exigencias
| cambiantes | del entorno | tecnológico | actual. |     |     |
| ---------- | ----------- | ----------- | ------- | --- | --- |
Metodología
Para el desarrollo de la presente revisión se empleó la metodología PRISMA. A continuación, en la Figura 1 se
| muestra     | un diagrama   | de flujo explicando | la misma. |     |     |
| ----------- | ------------- | ------------------- | --------- | --- | --- |
| Facultad    | de Ingeniería |                     |           |     | 88  |
| Universidad | La Salle,     | Arequipa,           | Perú      |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |      |     |     |     |     |
| ------------------ | -------------------------- | ---- | --- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, | 2024 |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|             |                     | Figura 1. Diagrama | de flujo de | la metodología | PRISMA. |     |
| ----------- | ------------------- | ------------------ | ----------- | -------------- | ------- | --- |
| Facultad    | de Ingeniería       |                    |             |                |         | 89  |
| Universidad | La Salle, Arequipa, | Perú               |             |                |         |     |
facin.innosoft@ulasalle.edu.pe

| Revista     | Innovación | y Software          |     |     |      |     |     |     |     |     |     |     |
| ----------- | ---------- | ------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Vol. 5, No. | 2, Mes     | Septiembre-Febrero, |     |     | 2024 |     |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
| Ecuaciones |     | de búsqueda |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Para iniciar el proceso de búsqueda, se utilizaron conectores booleanos que integran las diferentes variables del
estudio. Para aumentar la precisión en la búsqueda de literatura científica, se diseñó un protocolo que combina
los términos predefinidos con los operadores booleanos detallados en la Tabla 1.
|     |     |             |     | Tabla | 1. Ecuación | de     | búsqueda | por      | cada base | de datos. |     |     |
| --- | --- | ----------- | --- | ----- | ----------- | ------ | -------- | -------- | --------- | --------- | --- | --- |
|     |     | Repositorio |     |       |             | Cadena | de       | búsqueda |           |           |     |     |
Google Académico “inteligenciaartificial” “prevencióndeincidentes”
SCOPUS
|     |     |     |     |     |     | (TITLE-ABS-KEY |               |     | (“artificial |            | intelligence”) |     |
| --- | --- | --- | --- | --- | --- | -------------- | ------------- | --- | ------------ | ---------- | -------------- | --- |
|     |     |     |     |     |     | AND            | TITLE-ABS-KEY |     |              | (“incident | manage-        |     |
ment”))
| Criterios | de  | inclusión |     | y exclusión |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Los criterios de inclusión y exclusión son directrices específicas establecidas para realizar una revisión biblio-
gráfica o un artículo de revisión. Su propósito es decidir qué estudios o artículos serán incluidos y cuáles serán
descartados durante la revisión. Estos criterios son fundamentales para asegurar la pertinencia y calidad de los
estudios seleccionados para el análisis. Todos los criterios de inclusión se presentan en la Tabla 2, mientras que
| los criterios | de  | exclusión | se  | detallan | en la     | Tabla    | 3.           |               |      |                    |     |     |
| ------------- | --- | --------- | --- | -------- | --------- | -------- | ------------ | ------------- | ---- | ------------------ | --- | --- |
|               |     |           |     |          |           | Tabla 2. | Criterios    | de inclusión. |      |                    |     |     |
|               |     |           | N°  |          | Criterios |          | de inclusión |               |      |                    |     |     |
|               |     |           | CI1 |          | Artículos | que      | abordan      | el            | tema | de la inteligencia |     |     |
artificialenlagestiónpredictivadeincidentesde
TI.
CI2
|         |     |             |     |            | Artículos                                  |           | redactados | en  | español | e inglés. |     |     |
| ------- | --- | ----------- | --- | ---------- | ------------------------------------------ | --------- | ---------- | --- | ------- | --------- | --- | --- |
|         |     |             | CI3 |            | Artículospublicadosentrelosaños2019y2024.. |           |            |     |         |           |     |     |
|         |     |             | aCI | = criterio | de                                         | inclusión |            |     |         |           |     |     |
| Proceso | de  | recolección |     | de         | información                                |           |            |     |         |           |     |     |
Las búsquedas se llevaron a cabo utilizando las directrices de inclusión descritas en la Tabla 2, junto con la
combinación de los términos “artificial intelligence” y “incident management” en las bases de datos Google
Scholar y SCOPUS, empleando operadores booleanos AND y OR. Aunque estas búsquedas generaron pocos
resultados, algunos redundantes o de escaso valor para la revisión, proporcionaron una comprensión amplia del
tema.
| Facultad    | de Ingeniería |        |           |     |      |     |     |     |     |     |     | 90  |
| ----------- | ------------- | ------ | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Universidad | La            | Salle, | Arequipa, |     | Perú |     |     |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación |                            | y Software |      |     |     |     |     |     |     |
| ------------------ | -------------------------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, |            | 2024 |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|     |     |     | Tabla     | 3. Criterios  | de exclusión. |          |        |     |     |
| --- | --- | --- | --------- | ------------- | ------------- | -------- | ------ | --- | --- |
|     |     | N°  | Criterios | de exclusión  |               |          |        |     |     |
|     |     | CE1 | Artículos | no publicados | entre         | los años | 2019 y |     |     |
2024.
CE2
|     |     |     | Artículos | duplicados. |                  |     |            |     |     |
| --- | --- | --- | --------- | ----------- | ---------------- | --- | ---------- | --- | --- |
|     |     | CE3 | Artículos | que no      | tienen similitud | con | el tema de |     |     |
investigación.
|     |     | CE4 | Artículos               | que no | son de libre | acceso. |     |     |     |
| --- | --- | --- | ----------------------- | ------ | ------------ | ------- | --- | --- | --- |
|     |     | aCE | = criterio de exclusión |        |              |         |     |     |     |
EnlaTabla4sepresentaundesglosedelosartículoscorrespondientesacadabasededatosymotordebúsqueda
| empleados | como | referencia. |                     |           |           |              |              |     |     |
| --------- | ---- | ----------- | ------------------- | --------- | --------- | ------------ | ------------ | --- | --- |
|           |      | Tabla 4.    | Artículos depurados | empleando | criterios | de inclusión | y exclusión. |     |     |
Base de datos Artículos Aplicando Aplicando Aplicando Aplicando
|     |     |     | encontrados | CE1 | CE2 |     | CE3 | CE4 |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
en total
| Google | Académico |     | 153 | 116 | 116 |     | 21  | 11  |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPUS |           |     | 93  | 47  | 44  |     | 7   | 4   |     |
TOTAL
|     |     |     | 246 | 163 | 160 |     | 28  | 15  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Se implementaron diversos filtros en las publicaciones y revistas científicas seleccionadas (ver Figura 2), si-
| guiendo     | las directrices | de inclusión | y exclusión | establecidas. |     |     |     |     |     |
| ----------- | --------------- | ------------ | ----------- | ------------- | --- | --- | --- | --- | --- |
| Facultad    | de Ingeniería   |              |             |               |     |     |     |     | 91  |
| Universidad | La Salle,       | Arequipa,    | Perú        |               |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |      |     |     |     |     |
| ------------------ | -------------------------- | ---- | --- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, | 2024 |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|             |                     | Figura 2. Diagrama | de flujo PRISMA | aplicado a | este artículo |     |
| ----------- | ------------------- | ------------------ | --------------- | ---------- | ------------- | --- |
| Facultad    | de Ingeniería       |                    |                 |            |               | 92  |
| Universidad | La Salle, Arequipa, | Perú               |                 |            |               |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |     |      |     |     |     |     |     |     |
| ------------------ | -------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
Resultados
Se identificaron 15 artículos para realizar una exploración exhaustiva y examen detallado del tema de investi-
gación. Posterior al examen, se presenta un resumen en la Tabla 1 que detalla los hallazgos obtenidos.
|     |        |              | Tabla | 5. Análisis | de los artículos | académicos |     |     |     |
| --- | ------ | ------------ | ----- | ----------- | ---------------- | ---------- | --- | --- | --- |
| N°  | Título | del artículo |       | Resultados  |                  |            |     |     |     |
1 “An Empirical Analysis Este estudio usa técnicas avanzadas como machine learning,
of State-of-Art Classi- deep learning y transformadores para predecir incidentes de
fication Models in an TI, siendo pionero en aplicar estas tecnologías en la gestión
IT Incident Severity deservicios.Seevaluarondiversasfuentesdeincidentes,des-
Prediction Framework” tacandolasarquitecturasdetransformadoresyXGBoostpor
|     | (2023) |     |     | sualtaprecisión.Seempleóremuestreoydatossintéticospa- |               |                  |           |                 |     |
| --- | ------ | --- | --- | ----------------------------------------------------- | ------------- | ---------------- | --------- | --------------- | --- |
|     |        |     |     | ra abordar                                            | desafíos      | de desequilibrio | de datos, | logrando me-    |     |
|     |        |     |     | joras significativas                                  |               | y proponiendo    | un marco  | para reducir el |     |
|     |        |     |     | tiempo                                                | de resolución | de incidentes    | mediante  | predicción.     |     |
2 “ExploringtheTransfor- Este artículo examina cómo la integración de Inteligencia
mative Benefits of In- Artificial en la Base de Datos de Gestión de Configuración
tegrating Artificial Inte- (CMDB) está transformando la gestión de servicios de TI.
lligence into Configura- Explora desde conceptos básicos hasta aplicaciones avanza-
tion Management Data- dascomoeldescubrimientoautomatizadoylagestiónproac-
base (CMDB)” (2024) tiva de incidentes y cambios. Destaca por ofrecer una com-
|             |               |           |      | prensión      | profunda   | de los beneficios | que la IA              | aporta al me- |     |
| ----------- | ------------- | --------- | ---- | ------------- | ---------- | ----------------- | ---------------------- | ------------- | --- |
|             |               |           |      | jorar la      | eficiencia | operativa         | y facilitar decisiones | informadas    |     |
|             |               |           |      | en la gestión | de         | infraestructuras  | de TI.                 |               |     |
| Facultad    | de Ingeniería |           |      |               |            |                   |                        |               | 93  |
| Universidad | La Salle,     | Arequipa, | Perú |               |            |                   |                        |               |     |
facin.innosoft@ulasalle.edu.pe

| Revista | Innovación y Software             |     |      |     |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vol.    | 5, No. 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|     | N° Título | del artículo |     | Resultados |     |     |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
3 “How Can Subgroup Este estudio mejora la supervisión de sistemas de TI con
DiscoveryHelpAIOps?” técnicas avanzadas de AIOps. Subraya las limitaciones de
(2021) los motores de inferencia basados en reglas y sugiere el Des-
|     |     |     |     | cubrimiento | de               | Subgrupos  |          | como una     | innovadora |               | técnica de |     |
| --- | --- | --- | --- | ----------- | ---------------- | ---------- | -------- | ------------ | ---------- | ------------- | ---------- | --- |
|     |     |     |     | minería     | de datos         | para       | entender |              | modelos    | predictivos.  | Este       |     |
|     |     |     |     | enfoque     | avanza           | al ofrecer | nuevas   | perspectivas |            | para          | automa-    |     |
|     |     |     |     | tizar y     | gestionar        | incidentes |          | en TI,       | integrando | conocimientos |            |     |
|     |     |     |     | prácticos   | e investigativos |            | para     | resolver     | desafíos.  |               |            |     |
4 “Mining Java Memory Este estudio utiliza AIOps con un enfoque en el Descubri-
Errors using Subjective miento de Subgrupos (SD), una técnica de minería de datos.
Interesting Subgroups Desarrolla un marco específico para SD que maneja concep-
with Hierarchical Tar- tos jerárquicos, diseñado para identificar patrones en datos
gets” (2023) de incidentes como errores de memoria en sistemas ERP. Se
|     |     |     |     | valida | en escenarios |     | reales,   | mejorando | la detección |         | automa- |     |
| --- | --- | --- | --- | ------ | ------------- | --- | --------- | --------- | ------------ | ------- | ------- | --- |
|     |     |     |     | tizada | y diagnóstico |     | de causas | raíz.     | Subraya      | futuras | mejoras |     |
eneficienciacomputacionalyexpansiónaotroscasosdeuso.
5 “On the Difficulty of UtilizaInteligenciaArtificialparaOperaciones(AIOps)para
Identifying Incident- mejorar la gestión de cambios en empresas, enfocándose en
Inducing Changes” fortalecerlatrazabilidadentrecambioseincidentesmediante
(2024) métodos precisos validados con datos históricos y evaluacio-
|     |     |     |     | nes prácticas. |            | Destaca | la complejidad |     | inherente      |     | a esta tarea |     |
| --- | --- | --- | --- | -------------- | ---------- | ------- | -------------- | --- | -------------- | --- | ------------ | --- |
|     |     |     |     | debido         | al impacto | del     | contexto       | en  | la efectividad |     | de los méto- |     |
dosdeAIOps,evidenciadopordiferenciassignificativasentre
|             |               |           |      | resultados | históricos |     | y evaluaciones |     | en tiempo | real. |     |     |
| ----------- | ------------- | --------- | ---- | ---------- | ---------- | --- | -------------- | --- | --------- | ----- | --- | --- |
| Facultad    | de Ingeniería |           |      |            |            |     |                |     |           |       |     | 94  |
| Universidad | La Salle,     | Arequipa, | Perú |            |            |     |                |     |           |       |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista | Innovación y Software             |     |      |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| Vol.    | 5, No. 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|     | N° Título | del artículo |     | Resultados |     |     |     |     |     |
| --- | --------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
6 “Optimizing IT opera- Este estudio evaluó cómo las empresas pueden beneficiarse
tionswithAIOps:anin- deAIOpsenaplicacionescríticasysuimplementaciónenTI.
vestigation into the op- Secerrólabrechaexplorandosuadopciónrealconunestudio
portunities and challen- de caso. Se destaca la etapa inicial de adopción empresarial
ges for enterprise adop- de AIOps y la importancia de un proceso continuo alineado
tion” (2023) con objetivos empresariales. Se plantean preguntas sobre la
|     |     |     |     | autonomía       | de decisiones | de AI          | y la responsabilidad | legal en       |     |
| --- | --- | --- | --- | --------------- | ------------- | -------------- | -------------------- | -------------- | --- |
|     |     |     |     | las operaciones | de            | TI, reflejando | un enfoque           | integral hacia |     |
|     |     |     |     | los desafíos    | y avances     | futuros.       |                      |                |     |
7 “Towards Intelligent Este estudio aborda la gestión de incidentes en servicios de
Incident Management: nubeconlaadopcióndeAIOpsparamejorarlacomprensión
Why We Need It and ymitigacióndeincidentescríticos.Seidentificandesafíosco-
How We Make It” mo la falta de dependencias detalladas entre servicios y la
(2020) evaluación imprecisa del estado de los recursos. Introduce el
|     |     |     |     | marco         | IcM BRAIN     | para optimizar | la eficiencia | en la gestión    |     |
| --- | --- | --- | --- | ------------- | ------------- | -------------- | ------------- | ---------------- | --- |
|     |     |     |     | de incidentes | en Microsoft, | sugiriendo     | áreas         | para futuras in- |     |
|     |     |     |     | vestigaciones | y mejoras     | en sistemas    | de nube       | resilientes.     |     |
8 “Implementación de una La investigación implementa una mesa de ayuda basada en
mesa de ayuda basada ITILV4paraoptimizarlosprocesosinternosdeTI,mejoran-
en ITIL v4 para agilizar dolagestióndeincidenciasycambios.Sedestacalanovedad
los procesos internos de de usar el modelo TI Manager Engine para administrar re-
TI” (2022) motamente los equipos, reduciendo tiempos de atención y
|     |     |     |     | asegurando | un control | efectivo   | de cambios,  | lo cual supera      |     |
| --- | --- | --- | --- | ---------- | ---------- | ---------- | ------------ | ------------------- | --- |
|     |     |     |     | soluciones | similares  | al mejorar | la calidad y | eficiencia del ser- |     |
vicio.
| Facultad    | de Ingeniería |           |      |     |     |     |     |     | 95  |
| ----------- | ------------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| Universidad | La Salle,     | Arequipa, | Perú |     |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |     |      |     |     |     |     |     |     |
| ------------------ | -------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
| N°  | Título | del artículo |     | Resultados |     |     |     |     |     |
| --- | ------ | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
9 “La Inteligencia Artifi- El artículo explora la aplicación de la Inteligencia Artificial
cial en la transforma- (IA) en diversas áreas universitarias, incluyendo la comu-
ción de procesos univer- nidad académica, la oferta educativa, la investigación, y la
sitarios” (2019) cultura deportiva, evaluando su impacto en la toma de de-
|     |     |     |     | cisiones    | y propuestas. | También         | se analizan | los beneficios y |     |
| --- | --- | --- | --- | ----------- | ------------- | --------------- | ----------- | ---------------- | --- |
|     |     |     |     | desventajas | de integrar   | esta tecnología | en los      | procesos uni-    |     |
versitarios.
10 “Mejorar un modelo de El proyecto de investigación mejora un modelo de gestión de
gestión de incidentes de incidentes de seguridad mediante una base de conocimiento
seguridad estándar, me- de ataques a servicios web en entornos IoT, utilizando tec-
diante el uso de una ba- nologías Honeypot, Big Data y bases de datos distribuidas
se de conocimiento de en Blockchain, para facilitar el manejo de eventos de seguri-
ataques a servicios web dad informática. Este modelo proactivo gestiona incidentes
en ambientes IoT, cons- en ambientes señuelo para definir controles que mitiguen su
truida con tecnologías impacto en ambientes productivos. Se seleccionaron e imple-
Honeypot, Big data y mentaron herramientas tecnológicas, se analizaron modelos
basesdedatosdistribui- y buenas prácticas, y se validó el nuevo modelo de gestión,
das sobre Blockchain, logrando una gestión más eficiente de los incidentes de segu-
|             | que           | facilite el  | manejo de | ridad. |     |     |     |     |     |
| ----------- | ------------- | ------------ | --------- | ------ | --- | --- | --- | --- | --- |
|             | eventos       | de seguridad | in-       |        |     |     |     |     |     |
|             | formática.”   | (2022)       |           |        |     |     |     |     |     |
| Facultad    | de Ingeniería |              |           |        |     |     |     |     | 96  |
| Universidad | La Salle,     | Arequipa,    | Perú      |        |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista | Innovación y Software             |     |      |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Vol.    | 5, No. 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|     | N° Título | del artículo |     | Resultados |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
11 “Desarrollo de una Guía Esteproyectodesarrollaunaguíaparaabordarincidentesde
para el abordaje de In- ciberseguridad en infraestructuras críticas industriales, que
cidentes de Cibersegu- abarque la prevención, mitigación y análisis forense de estos
ridad en Infraestructu- incidentes. Los sistemas de control industrial, integrados con
ras Críticas Industria- tecnologías modernas como Big Data y IoT, están expuestos
les” (2021) a riesgos significativos. El proyecto, realizado por la Univer-
|     |     |     |     | sidad Abierta | Interamericana, |     | la Universidad | Nacional | de la |     |
| --- | --- | --- | --- | ------------- | --------------- | --- | -------------- | -------- | ----- | --- |
DefensaylaUniversidadFASTA,secentraendesarrollarre-
|     |     |     |     | comendaciones | para        | la seguridad | en estos            | sistemas.      | La guía  |     |
| --- | --- | --- | --- | ------------- | ----------- | ------------ | ------------------- | -------------- | -------- | --- |
|     |     |     |     | ayudará       | a gestionar | la seguridad | en infraestructuras |                | vitales, |     |
|     |     |     |     | como plantas  | de energía  | y agua,      | mejorando           | su resiliencia | an-      |     |
te ciberamenazas.
12 “Implantación de un sis- El sistema web desarrollado para la gestión de accidentes e
temadeinformaciónba- incidentes en la compañía minera de Cusco representa una
sado en la web de re- novedad y mejora en su campo al ofrecer una solución inte-
gistro y gestión de acci- gral que facilita el registro, seguimiento y análisis de datos
dentes e incidentes para en tiempo real. Su superioridad frente a soluciones similares
lamejoradeindicadores radica en su enfoque cuantitativo, diseño no experimental,
de seguridad en el tra- y su capacidad de automatizar procesos, lo que incrementa
bajo en una compaÒÌa significativamente la eficiencia y precisión en la gestión de
minera en la ciudad de la seguridad laboral, reduciendo la frecuencia y severidad de
|             | Cusco”        | (2022)    |      | los accidentes. |     |     |     |     |     |     |
| ----------- | ------------- | --------- | ---- | --------------- | --- | --- | --- | --- | --- | --- |
| Facultad    | de Ingeniería |           |      |                 |     |     |     |     |     | 97  |
| Universidad | La Salle,     | Arequipa, | Perú |                 |     |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista | Innovación y Software             |     |      |     |     |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vol.    | 5, No. 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|     | N° Título | del artículo |     | Resultados |     |     |     |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
13 “Predicción de riesgos La investigación de Wilmer Jesus Agamez Julio introduce
en salud para personas unanovedadenelcampodelasaludpúblicaaldesarrollarun
conobesidadempleando modelo de predicción de riesgos de salud para personas con
técnicas de aprendizaje obesidad, utilizando técnicas de aprendizaje de máquinas.
de máquinas” (2022) Este modelo destaca por su capacidad de analizar patrones
decomportamientoylainteracciónconlossistemasdesalud
|     |     |     |     | colombianos,    |            | permitiendo |               | una          | predicción     | precisa  | y              | escalable |     |
| --- | --- | --- | --- | --------------- | ---------- | ----------- | ------------- | ------------ | -------------- | -------- | -------------- | --------- | --- |
|     |     |     |     | de eventos      | adversos.  |             | Su            | superioridad |                | respecto | a soluciones   |           |     |
|     |     |     |     | similares       | reside     | en          | su enfoque    |              | preventivo,    |          | proporcionando |           |     |
|     |     |     |     | una herramienta |            | robusta     |               | para         | la formulación |          | de políticas   | de        |     |
|     |     |     |     | salud más       | eficientes |             | y proactivas. |              |                |          |                |           |     |
14 “Innovaciones tecnológi- La investigación de Diana Vanessa Moreno Avila presenta
cas en la seguridad y sa- una revisión exhaustiva sobre la implementación de tecno-
lud en el trabajo en Co- logías innovadoras en seguridad y salud en el trabajo (SST)
lombia una revisión do- enColombia,destacandoelusodeinteligenciaartificial,IoT,
cumental” (2024) drones y realidad virtual. Este estudio es innovador al pro-
|     |     |     |     | porcionar              | una   | guía           | de implementación |               |                | para   | empresas,  | abor-    |     |
| --- | --- | --- | --- | ---------------------- | ----- | -------------- | ----------------- | ------------- | -------------- | ------ | ---------- | -------- | --- |
|     |     |     |     | dando                  | desde | el diagnóstico |                   | hasta         | la evaluación. |        | Su         | superio- |     |
|     |     |     |     | ridad frente           |       | a soluciones   |                   | similares     | radica         | en     | su enfoque | sis-     |     |
|     |     |     |     | temático               | y su  | capacidad      |                   | para          | identificar    | y      | superar    | desafíos |     |
|     |     |     |     | específicos            | de    | inversión      | y                 | capacitación, |                | lo que | permite    | mejo-    |     |
|     |     |     |     | rar significativamente |       |                | la                | eficiencia    | y seguridad    |        | en el      | entorno  |     |
laboral.
| Facultad    | de Ingeniería |           |      |     |     |     |     |     |     |     |     |     | 98  |
| ----------- | ------------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Universidad | La Salle,     | Arequipa, | Perú |     |     |     |     |     |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista | Innovación y Software             |     |      |     |     |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vol.    | 5, No. 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |     |     |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
|     | N° Título | del artículo |     | Resultados |     |     |     |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15 “La prevención en la El ensayo sobre la prevención de pérdida de datos e infor-
pérdidadedatoseinfor- mación en la vigilancia privada se distingue por su enfoque
mación, vital en la vigi- en la implementación de políticas específicas y el uso de tec-
lancia privada” (2021) nologías avanzadas como Big Data, inteligencia artificial y
|     |     |     |     | Machine | Learning. |     | Estas | herramientas |     | no solo | fortalecen | la  |     |
| --- | --- | --- | --- | ------- | --------- | --- | ----- | ------------ | --- | ------- | ---------- | --- | --- |
seguridaddelosdatos,sinoquetambiénmejoranlaeficiencia
|     |     |     |     | operativa         | y la            | capacidad  |               | predictiva       | ante        | posibles      | incidentes |          |     |
| --- | --- | --- | --- | ----------------- | --------------- | ---------- | ------------- | ---------------- | ----------- | ------------- | ---------- | -------- | --- |
|     |     |     |     | de fuga           | de información. |            |               | Además,          | el análisis |               | detallado  | del      |     |
|     |     |     |     | valor estratégico |                 | de         | los datos     | dentro           | del         | contexto      | de         | la segu- |     |
|     |     |     |     | ridad privada     |                 | representa |               | una contribución |             | significativa |            | para     |     |
|     |     |     |     | establecer        | prácticas       |            | de prevención |                  | más         | efectivas.    |            |          |     |
Discusion
Losresultadosindicanqueelusodetécnicasavanzadascomomachinelearning,deeplearningytransformadores
para predecir incidentes de TI ha demostrado ser altamente eficaz, destacando las arquitecturas de transfor-
madores por su alta precisión [24]. Este enfoque en la gestión de servicios de TI no solo mejora la precisión
de las predicciones, sino que también introduce un marco que reduce el tiempo de resolución de incidentes.
Los resultados indican que, mediante el uso de remuestreo y datos sintéticos, es posible abordar los desafíos de
desequilibrio de datos, logrando mejoras significativas en la precisión de las predicciones.
La integración de la Inteligencia Artificial en la Base de Datos de Gestión de Configuración (CMDB) está
revolucionando la gestión de servicios de TI [25]. La IA facilita el descubrimiento automatizado y la gestión
proactiva de incidentes y cambios, mejorando la eficiencia operativa y las decisiones informadas en la gestión
de infraestructuras de TI. Este estudio resalta cómo la IA puede ofrecer una comprensión más profunda de los
beneficios operativos, permitiendo una gestión más eficiente y proactiva de los sistemas de TI.
Además, se destaca las limitaciones de los motores de inferencia basados en reglas tradicionales y propone el
Descubrimiento de Subgrupos como una técnica innovadora de minería de datos para mejorar la comprensión
delosmodelospredictivos[1,2].Esteenfoqueproporcionanuevasperspectivasparalaautomatizaciónygestión
de incidentes en TI, integrando conocimientos prácticos e investigativos para abordar desafíos específicos. La
implementación de estas técnicas avanzadas de AIOps muestra un avance significativo en la automatización y
| la gestión  | eficiente de  | incidentes. |      |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Facultad    | de Ingeniería |             |      |     |     |     |     |     |     |     |     |     | 99  |
| Universidad | La Salle,     | Arequipa,   | Perú |     |     |     |     |     |     |     |     |     |     |
facin.innosoft@ulasalle.edu.pe

Revista Innovación y Software
Vol. 5, No. 2, Mes Septiembre-Febrero, 2024
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
La evaluación de cómo las empresas pueden beneficiarse de AIOps en aplicaciones críticas de TI revela que
la adopción de estas tecnologías aún está en sus etapas iniciales. El estudio de caso destaca la necesidad de
ver AIOps como un proceso continuo alineado con los objetivos empresariales. Se plantean cuestiones sobre la
autonomíadelasdecisionesdeIAylaresponsabilidadlegalenlasoperacionesdeTI,subrayandolaimportancia
de un enfoque integral para enfrentar los desafíos y aprovechar los avances futuros en AIOps.
Conclusiones
El análisis de diversos estudios en la gestión de incidentes de TI revela avances significativos y contribuciones
clave que impulsan el campo hacia adelante. Uno de los principales hallazgos es el efecto transformador de las
tecnologíasemergentes,comoelMachineLearning,InteligenciaArtificialylostransformadores,enlapredicción
precisa de incidentes. Estas herramientas no solo mejoran la capacidad de anticiparse a problemas, sino que
también permiten una respuesta más rápida y eficiente.
Además, la integración de Inteligencia Artificial en la Base de Datos de Gestión de Configuración (CMDB) ha
facilitado una gestión más proactiva de configuraciones y cambios, optimizando así los recursos y fortaleciendo
la estabilidad operativa. Este avance se traduce en una mayor agilidad para adaptarse a entornos dinámicos y
una reducción notable en el tiempo de resolución de problemas.
Otro punto destacado es el uso innovador del Descubrimiento de Subgrupos en la supervisión de sistemas de
TI. Esta técnica no solo mejora la automatización de la detección de anomalías, sino que también enriquece la
comprensión de los modelos predictivos, ofreciendo nuevas perspectivas para la gestión proactiva de incidentes.
En términos de detección y diagnóstico de errores, los estudios revisados enfatizan la eficacia de AIOps en
la identificación y mitigación de errores críticos, como los relacionados con sistemas ERP. Esta capacidad no
solo mejora la eficiencia operativa, sino que también fortalece la resiliencia organizacional frente a desafíos
complejos.
Finalmente, se identifican desafíos significativos en la gestión de cambios, subrayando la necesidad de mejorar
la trazabilidad entre cambios e incidentes para optimizar la respuesta organizacional. Este aspecto sugiere
oportunidadesparafuturasinvestigacionesorientadasafortalecerlasprácticasdegestióndecambiosymejorar
la adaptabilidad de las organizaciones a entornos tecnológicos cambiantes.
En conjunto, estas conclusiones consolidan el panorama actual de la gestión de incidentes de TI y destacan
la importancia de la innovación continua y la integración estratégica de tecnologías emergentes. Estos avances
no solo mejoran la eficiencia operativa, sino que también fortalecen la capacidad de las organizaciones para
Facultad de Ingeniería 100
Universidad La Salle, Arequipa, Perú
facin.innosoft@ulasalle.edu.pe

| Revista Innovación |        | y Software          |      |     |     |     |
| ------------------ | ------ | ------------------- | ---- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes | Septiembre-Febrero, | 2024 |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
enfrentar desafíos tecnológicos emergentes en un entorno digital dinámico.
| Contribución |     | de Autoría |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- |
Luigui Jampierre Amaya Jave: Conceptualización, Metodología, Investigación, Análisis formal, Validación,
Roger Alejan-
Redacción - borrador original, Curación de datos, Escritura, revisión y edición, Visualización.
dro Querevalú Galán:Conceptualización,Metodología,Investigación,Análisisformal,Validación,Redacción
-borradororiginal,Curacióndedatos,Escritura,revisiónyedición,Visualización.Alberto Carlos Mendoza
de los Santos: Redacción - borrador original, Curación de datos, Validación, Visualización.
Referencias
[1] Y. Remil, “How can subgroup discovery help aiops?” in ASE 2021: Proceedings of the 36th IEEE/ACM In-
ternational Conference on Automated Software Engineering,INSALyon,CNRS,LIRISUMR5205,France.
| Infologic | R&D, | Bourg-lès-Valence, |     | France, Sep. | 2021. |     |
| --------- | ---- | ------------------ | --- | ------------ | ----- | --- |
[2] Y. Remil, A. Bendimerad, M. Chambard, R. Mathonat, and M. Plantevit, “Mining java memory errors
using subjective interesting subgroups with hierarchical targets,” in IEEE International Conference on
Data Mining Workshops (ICDM Workshops), Shanghai, China, Dec. 2023.
[3] E. Kapel, L. Cruz, D. Spinellis, and A. van Deursen, “On the difficulty of identifying incident-inducing
changes,” in 46th International Conference on Software Engineering: Software Engineering in Practice
| (ICSE-SEIP’24). |     | Lisbon, | Portugal: | ACM, | 2024, p. 11. |     |
| --------------- | --- | ------- | --------- | ---- | ------------ | --- |
[4] M. G. Locher, “Optimizing it operations with aiops: an investigation into the opportunities and challenges
for enterprise adoption,” Master’s thesis, ZHAW Zürcher Hochschule für Angewandte Wissenschaften,
| Winterthur, |     | Switzerland, | 2023. |     |     |     |
| ----------- | --- | ------------ | ----- | --- | --- | --- |
[5] Z. Chen, Y. Kang, L. Li, and X. Zhang, “Towards intelligent incident management: Why we need it and
how we make it,” in 28th ACM Joint European Software Engineering Conference and Symposium on the
Foundations of Software Engineering (ESEC/FSE ’20). Virtual Event, USA: ACM, 2020, p. 11.
[6] D. V. M. Avila, “Innovaciones tecnológicas en la seguridad y salud en el trabajo en colombia: una revisión
documental,” Master’s thesis, Universidad Santo Tomás, Bucaramanga, Colombia, 2024.
[7] W. J. A. Julio, “Predicción de riesgos en salud, para personas con obesidad, empleando técnicas de apren-
dizaje de máquinas,” Master’s thesis, Facultad de Minas, Universidad Nacional de Colombia, Medellín,
| Colombia,   | 2022.         |           |      |     |     |     |
| ----------- | ------------- | --------- | ---- | --- | --- | --- |
| Facultad    | de Ingeniería |           |      |     |     | 101 |
| Universidad | La Salle,     | Arequipa, | Perú |     |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |     |      |     |     |     |     |
| ------------------ | -------------------------- | --- | ---- | --- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
[8] H. C. Laguna, “Implantación de un sistema de información basado en la web de registro y gestión de
accidentes e incidentes para la mejora de indicadores de seguridad en el trabajo en una compañía minera
| en la | ciudad de cusco | - 2022,” | Lima, Perú, | 2023. |     |     |     |
| ----- | --------------- | -------- | ----------- | ----- | --- | --- | --- |
[9] J. Kamlofsky, G. Gonzalez, and S. Trigo, “Desarrollo de una guía para el abordaje de incidentes de ciber-
seguridad en infraestructuras críticas industriales,” in XXIII Workshop de Investigadores en Ciencias de
la Computación, RedUNCI - UNdeC, Buenos Aires, Argentina, Apr. 2021.
[10] D. E. V. nas Reyes, “La prevención en la pérdida de datos e información, vital en la vigilancia privada,”
Ensayo Académico, Facultad de Relaciones Internacionales, Estrategia y Seguridad, Programa Adminis-
| tración | de la Seguridad, | Bogotá | D.C., | Colombia, | 2021. |     |     |
| ------- | ---------------- | ------ | ----- | --------- | ----- | --- | --- |
[11] C. A. P. Álvarez and M. F. Lasprilla, “Mejorar un modelo de gestión de incidentes de seguridad estándar,
mediante el uso de una base de conocimiento de ataques a servicios web en ambientes iot, construida
con tecnologías honeypot, big data y bases de datos distribuidas sobre blockchain, que facilite el manejo
de eventos de seguridad informática,” Master’s thesis, Instituto Tecnológico Metropolitano, Facultad de
| Ingenierías, | Medellín, | Colombia, | 2022. |     |     |     |     |
| ------------ | --------- | --------- | ----- | --- | --- | --- | --- |
[12] R.O.C.Dávila,“Implementacióndeunamesadeayudabasadaenitilv4paraagilizarlosprocesosinternos
| de ti,” | Pimentel, Perú, | 2022. |     |     |     |     |     |
| ------- | --------------- | ----- | --- | --- | --- | --- | --- |
[13] Y. S. Martínez, “La inteligencia artificial en la transformación de procesos universitarios,” Tecnología e
| Innovación | en Educación | Superior, | vol. | 1, no. | 2, pp. 1–10, Oct. | 2019. |     |
| ---------- | ------------ | --------- | ---- | ------ | ----------------- | ----- | --- |
[14] S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 4th ed. Pearson, 2020.
[15] G. Kaur and M. Kaur, “Aiops: Predictive analytics for it operations,” International Journal of Computer
| Applications, | vol. 177, | no. 15, | pp. 25–30, | 2019. |     |     |     |
| ------------- | --------- | ------- | ---------- | ----- | --- | --- | --- |
[16] D. R. Gagne, “Leveraging aiops for proactive it incident management,” IT Professional, vol. 22, no. 2, pp.
| 45–52, | 2020. |     |     |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- | --- | --- |
[17] T. L. Gonsalves and S. T. Parab, “It incident management: A case study,” Procedia Computer Science,
| vol. | 167, pp. 1575–1584, | 2020. |     |     |     |     |     |
| ---- | ------------------- | ----- | --- | --- | --- | --- | --- |
[18] J. K. Bedi, “Effective it incident management,” IT Professional, vol. 21, no. 3, pp. 55–63, 2019.
[19] P. Gupta and R. Ramesh, “Predictive analytics for it incident management,” Journal of Network and
| Computer    | Applications,       | vol. 156, | pp. | 102–115, | 2021. |     |     |
| ----------- | ------------------- | --------- | --- | -------- | ----- | --- | --- |
| Facultad    | de Ingeniería       |           |     |          |       |     | 102 |
| Universidad | La Salle, Arequipa, | Perú      |     |          |       |     |     |
facin.innosoft@ulasalle.edu.pe

| Revista Innovación | y Software                 |     |      |     |     |     |
| ------------------ | -------------------------- | --- | ---- | --- | --- | --- |
| Vol. 5, No.        | 2, Mes Septiembre-Febrero, |     | 2024 |     |     |     |
ISSN: 2708-0935
Pág. 85-103
https://revistas.ulasalle.edu.pe/innosoft
[20] A.Bilgihanet al.,“Raise:Leveragingresponsibleaiforserviceexcellence,” Journal of Service Management,
2020.
[21] V. Kaartemo and A. Helkkula, “Human–ai resource relations in value cocreation in service ecosystems,”
| Journal | of Service Management, |     | 2020. |     |     |     |
| ------- | ---------------------- | --- | ----- | --- | --- | --- |
[22] D. V. M. Avila, “Innovaciones tecnológicas en la seguridad y salud en el trabajo en colombia: una revisión
| documental,” | Journal | of Safety | Management, | 2024. |     |     |
| ------------ | ------- | --------- | ----------- | ----- | --- | --- |
[23] Y. S. Martínez, “La inteligencia artificial en la transformación de procesos universitarios,” Tecnología e
| Innovación | en Educación | Superior, | vol. 1, | no. 2, pp. 1–10, Oct. | 2019. |     |
| ---------- | ------------ | --------- | ------- | --------------------- | ----- | --- |
[24] S. Ahmed et al., “An empirical analysis of state-of-art classification models in an it incident severity
prediction framework,” Applied Sciences, vol. 13, no. 6, p. 3843, Mar. 2023. [Online]. Available:
https://doi.org/10.3390/app13063843
[25] Y. Chinthapatla, “Exploring the transformative benefits of integrating artificial intelligence into configu-
ration management database (cmdb),” International Journal of Management, IT & Engineering, vol. 14,
| no.         | 2, Feb. 2024.       |      |     |     |     |     |
| ----------- | ------------------- | ---- | --- | --- | --- | --- |
| Facultad    | de Ingeniería       |      |     |     |     | 103 |
| Universidad | La Salle, Arequipa, | Perú |     |     |     |     |
facin.innosoft@ulasalle.edu.pe