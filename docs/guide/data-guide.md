# Análise exploratória de dados

## Introdução

Uma breve documentação acerca das bases de dados que são utilizadas no projeto. A princípio este documento será utilizado como guia documentado para o agente LLM poder se contextualizar melhor no sistema, onde ele terá acesso a cada detalhe das tabelas. 

## Databases analisadas:

- CRITERIOS.csv
- RAIS ESTABELECIMENTOS.csv
- TOP100_30.csv
- TOP100_15.csv
- SITUACIONAL_2023.csv
- Salários e Visitas.csv
- SITUACIONAL_2023_PIVOT_MEDIAN.csv
- atividade_turistica.csv
- PIVOT_SITUACIONAL.csv
- IBGE.csv
- DESTINATIONS_2023.csv
- TIMELINE_FULL.csv
- QQUADRADO.csv
- Planilha1.csv
- SELO.csv
- TIMELINE_GD.csv
- CORRELACAO.csv
- LANGUAGE.csv
- PIVOT_TOP100C15.csv
- PIVOT_GD.csv
- PIVOT_TOP100C30.csv
- CRITERIOS_SITUACIONAL.csv
- TIMELINE_FULL_DETAIL.csv
- SITUACIONAL_2023_PIVOT.csv
- REMUNERACAO.csv
- RAIS GERAL.csv
- dicionario_dados_agente.csv

## Detalhes deste documento:

- Cada .csv é uma tabela no banco de dados, permanencendo com o nome exato sem a extensão “.csv”;
- As tabelas exibidas neste documento são apenas exemplos mostrando as 5 primeiras linhas da tabela real que está no banco de dados;
- A exploração das colunas representa uma descrição detalhada do que cada coluna em sua respectiva tabela faz.

## Entendendo as bases

### 1 - CRITERIOS.csv

Esta base contém um conjunto detalhado de **diretrizes e critérios técnicos** voltados para a certificação de **destinos turísticos sustentáveis**. O conteúdo está estruturado em seis temas fundamentais: **gestão do destino**, proteção da **natureza e paisagem**, cuidado com o **meio ambiente e clima**, preservação da **cultura e tradição**, promoção do **bem-estar social** e práticas de **comunicação e negócios**.
Cada item estabelece métricas para monitorar impactos ambientais, envolver comunidades locais e garantir a integridade dos ativos culturais e naturais. As informações são apresentadas em formato multilíngue, abrangendo **inglês, português e espanhol**, para facilitar a aplicação internacional das normas. Através de indicadores de sustentabilidade e transparência, o documento busca orientar administradores na criação de um turismo responsável e ético.

| CRITERIO | THEMES | THEME_DESCRIPTION_US | THEME_DESCRIPTION_PT | TOPIC | TOPIC_DESCRIPTION_US | TOPIC_DESCRIPTION_PT | CRITERIA | CRITERIA_TYPE | CRITERIA_NAME_US | CRITERIA_NAME_PT | CRITERIA_DESCRIPTION_US | CRITERIA_DESCRIPTION_PT | ORDEM_1 | ORDEM_2 | THEME_DESCRIPTION_ES | TOPIC_DESCRIPTION_ES | CRITERIA_NAME_ES | CRITERIA_DESCRIPTION_ES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.100000 | 1 | Destination Management | Gerenciamento de destinos | 1.100000 | Commitment & Organisation | Compromisso e organizaÃ§Ã£o | 1.1.01 | C15 | Sustainable destination coordinator | Coordenador de destinos sustentÃ¡veis | A person has 
been assigned the responsibility and authority for the adequate 
implementation and reporting of sustainable destination management. | Uma pessoa foi
 designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | 11,01 | 1,01 | GestiÃ³n del destino | Compromiso y organizaciÃ³n | Coordinador de sostenibilidad | Se ha asignado
 a una persona la responsabilidad y la autoridad para la adecuada 
implementaciÃ³n y reporte de la gestiÃ³n sostenible del destino. |
| 1.200000 | 1 | Destination Management | Gerenciamento de destinos | 1.100000 | Commitment & Organisation | Compromisso e organizaÃ§Ã£o | 1.1.02 | nan | Management structure | Estrutura de gestÃ£o | An adequately 
funded organisation or management structure is responsible for 
coordinating and promoting sustainable tourism development and 
management. It works with a range of bodies in delivering destination 
management and follows principles of sustainability and transparency in 
its operations and transactions. | Uma 
organizaÃ§Ã£o ou estrutura de gerenciamento com financiamento adequado 
Ã© responsÃ¡vel por coordenar e promover o desenvolvimento e o 
gerenciamento do turismo sustentÃ¡vel. Ela trabalha com uma sÃ©rie de 
Ã³rgÃ£os para fornecer gerenciamento de destinos e segue princÃ­pios de 
sustentabilidade e transparÃªncia em suas operaÃ§Ãµes e transaÃ§Ãµes. | 11,02 | 1,02 | GestiÃ³n del destino | Compromiso y organizaciÃ³n | Estructura de gestiÃ³n | Una 
organizaciÃ³n o estructura de gestiÃ³n adecuadamente financiada se 
encarga de coordinar y promover el desarrollo y la gestiÃ³n del turismo 
sostenible. Trabaja con una serie de organismos en la gestiÃ³n del 
destino y sigue los principios de sostenibilidad y transparencia en sus 
operaciones y transacciones. |
| 1.300000 | 1 | Destination Management | Gerenciamento de destinos | 1.100000 | Commitment & Organisation | Compromisso e organizaÃ§Ã£o | 1.1.03 | nan | Trained coordinator/ team | Coordenador/equipe treinada | The person or 
team responsible for destination development and management is 
sufficiently staffed and adequately trained on and/or experienced in 
sustainability issues. | A pessoa ou 
equipe responsÃ¡vel pelo desenvolvimento e gerenciamento do destino tem 
pessoal suficiente e Ã© adequadamente treinada e/ou tem experiÃªncia em 
sustentabilidade problemas. | 11,03 | 1,03 | GestiÃ³n del destino | Compromiso y organizaciÃ³n | Coordinador/equipo capacitado | La persona o 
el equipo responsable del desarrollo y la gestiÃ³n del destino cuenta 
con el personal suficiente y con la formaciÃ³n y/o la experiencia 
adecuadas en materia de sostenibilidad. |
| 1.400000 | 1 | Destination Management | Gerenciamento de destinos | 1.100000 | Commitment & Organisation | Compromisso e organizaÃ§Ã£o | 1.1.04 | nan | Stakeholder involvement | Envolvimento das partes interessadas | The 
destination management organisation or structure involves civil society 
and the private and public sector in sustainable destination management. | A 
organizaÃ§Ã£o ou estrutura de gerenciamento de destinos envolve a 
sociedade civil e a setor pÃºblico e privado no gerenciamento de 
destinos sustentÃ¡veis. | 11,04 | 1,04 | GestiÃ³n del destino | Compromiso y organizaciÃ³n | ParticipaciÃ³n de las partes interesadas (antes de la participaciÃ³n del sector turÃ­stico) | La 
organizaciÃ³n o estructura de gestiÃ³n del destino implica a la sociedad
 civil y a los sectores pÃºblico y privado en la gestiÃ³n sostenible del
 destino. |
| 1.500000 | 1 | Destination Management | Gerenciamento de destinos | 1.200000 | Planning & Development | Planejamento e desenvolvimento | 1.2.05 | C15 | Inventory of destination assets | InventÃ¡rio de ativos de destino | The destination has an inventory of its tourism-oriented assets and attractions including natural and cultural sites. | O destino tem um inventÃ¡rio de seus ativos e atraÃ§Ãµes voltados para o turismo incluindo locais naturais e culturais. | 12,05 | 1,05 | GestiÃ³n del destino | PlanificaciÃ³n y desarrollo | Inventario de activos de destino | El destino 
cuenta con un inventario de sus activos y atracciones orientadas al 
turismo, incluidos los lugares naturales y culturales. |

### Explorando as colunas:

- **CRITERIO, THEMES, TOPIC e CRITERIA:** São identificadores numéricos usados para organizar a hierarquia das informações, indo desde o número do tema mais amplo até o código exato de cada critério individual.
- **THEME_DESCRIPTION_US, _PT e _ES:** Contêm os nomes dos temas principais (as categorias maiores, como "Gerenciamento de destinos") em Inglês, Português e Espanhol.
- **TOPIC_DESCRIPTION_US, _PT e _ES:** Trazem os nomes dos tópicos (as subcategorias dentro de cada tema, como "Compromisso e organização") nos três idiomas.
- **CRITERIA_TYPE:** Indica a classificação, o peso ou a obrigatoriedade do critério por meio de siglas específicas, como "C15", "C30", "O" ou "N/A".
- **CRITERIA_NAME_US, _PT e _ES:** Apresentam o título ou o nome da ação específica que está sendo avaliada (ex: "Coordenador de destinos sustentáveis") em Inglês, Português e Espanhol.
- **CRITERIA_DESCRIPTION_US, _PT e _ES:** Fornecem a explicação detalhada e completa sobre o que o destino turístico precisa fazer para cumprir aquele critério, também traduzida para os três idiomas.
- **ORDEM_1 e ORDEM_2:** São valores numéricos utilizados pelo sistema para classificar e determinar a sequência em que os critérios devem aparecer.

### 2 - RAIS ESTABELECIMENTOS.csv

Está base detalha a infraestrutura econômica dos municípios brsileiros, registrando quantos estabelecimentos (empresas ou unidades produtivas) existem em cada cidade, segmentados por sua atividade econômica específica.

| CODIGO | ESTADO | CIDADE | 00:Ignorado | Categoria | Estabelecimentos |
| --- | --- | --- | --- | --- | --- |
| 310010 | Mg | Abadia dos Dourados | 0 | 12:FabricaÃ§Ã£o de Produtos do Fumo | 0 |
| 310020 | Mg | Abaete | 0 | 12:FabricaÃ§Ã£o de Produtos do Fumo | 0 |
| 310030 | Mg | Abre Campo | 0 | 12:FabricaÃ§Ã£o de Produtos do Fumo | 0 |
| 310040 | Mg | Acaiaca | 0 | 12:FabricaÃ§Ã£o de Produtos do Fumo | 0 |
| 310050 | Mg | Acucena | 0 | 12:FabricaÃ§Ã£o de Produtos do Fumo | 0 |
- **CÓDIGO:** Refere-se ao **Código IBGE do Município** (com 6 dígitos). É a chave de identificação única da cidade, essencial para realizar cruzamentos (JOINs) com outras tabelas, como as de PIB ou IDH.
- **ESTADO:** Contém a sigla da Unidade Federativa (**UF**) à qual o município pertence (ex: "Mg" para Minas Gerais, "Sp" para São Paulo).
- **CIDADE:** O nome oficial do **Município**. É a forma mais fácil de identificação humana, mas menos precisa para consultas automáticas que o código numérico.
- **00:Ignorado:** Geralmente funciona como uma categoria para registros que não possuem uma classificação setorial definida ou como um marcador de controle da base (no seu arquivo, aparece frequentemente com valor "0").
- **Categoria:** Descreve a **Atividade Econômica** do estabelecimento (baseada na CNAE - Classificação Nacional de Atividades Econômicas). Exemplo: "Alimentação", "Serviços de Arquitetura", "Fabricação de Veículos".
- **Estabelecimentos:** Representa a **Quantidade Total** de empresas/unidades ativas para aquela categoria específica naquela cidade. É o dado numérico principal para cálculos de densidade econômica.

### 3 - TOP100_30.csv

Esta base contém os registros de avaliação de destinos turísticos com base em critérios específicos de sustentabilidade e gestão. Em resumo, é um **boletim de desempenho detalhado**, servindo para cruzar as exigências do programa de turismo sustentável com a nota alcançada pelo município, garantindo que as informações estejam traduzidas e padronizadas.

| DESCRICAO | CRITERIO | NOTA | CIDADE | ANO | ESTADO | THEME | THEME_PT | THEME_US | CRITERIA_DESCRIPTION_PT | CRITERIA_DESCRIPTION_US | CRITERIA_NAME_PT | CRITERIA_NAME_US | ORDEM | CHAVE | CODIGO_MUNICIPIO | TOPIC | CRITERIA_DESCRIPTION_ES | CRITERIA_NAME_ES | THEME_ES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sustainable destination coordinator | 1.100000 | 5 | Treze TÃ­lias | 2022 | SC | 1 | Gerenciamento de destinos | Destination Management | Uma pessoa foi 
designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | A person has 
been assigned the responsibility and authority for the adequate 
implementation and reporting of sustainable destination management. | Coordenador de destinos sustentÃ¡veis | Sustainable destination coordinator | 1,01 | TREZE TÃLIAS-SC | 4218509 | 1.100000 | Se ha asignado
 a una persona la responsabilidad y la autoridad para la adecuada 
implementaciÃ³n y reporte de la gestiÃ³n sostenible del destino. | Coordinador de sostenibilidad | GestiÃ³n del destino |
| Nature conservation | 2.100000 | 5 | Treze TÃ­lias | 2022 | SC | 2 | Natureza e cenÃ¡rio | Nature & Scenery | O destino tem um sistema para conservar ecossistemas, habitats e espÃ©cies. | The destination has a system to conserve ecosystems, habitats and species. | ConservaÃ§Ã£o da natureza | Nature conservation | 2,01 | TREZE TÃLIAS-SC | 4218509 | 2.100000 | El destino cuenta con un sistema de conservaciÃ³n de ecosistemas, hÃ¡bitats y especies. | ConservaciÃ³n de la naturaleza | Naturaleza y paisaje |
| Noise | 3.100000 | 5 | Treze TÃ­lias | 2022 | SC | 3 | Meio ambiente e clima | Environment & Climate | O ruÃ­do Ã© adequadamente regulamentado e minimizado | Noise is adequately regulated and minimised; tourism enterprises and visitors are encouraged to minimise noise. | Barulho | Noise | 3,01 | TREZE TÃLIAS-SC | 4218509 | 3.100000 | El ruido estÃ¡ adecuadamente regulado y minimizado; se anima a las empresas turÃ­sticas y a los visitantes a minimizar el ruido. | Ruido | Medio ambiente y clima |
| Light pollution | 3.200000 | 5 | Treze TÃ­lias | 2022 | SC | 3 | Meio ambiente e clima | Environment & Climate | Os impactos da 
poluiÃ§Ã£o luminosa na vida selvagem, na experiÃªncia dos residentes e 
dos visitantes sÃ£o tratados adequadamente. As empresas de turismo e os 
visitantes sÃ£o incentivados a minimizar a poluiÃ§Ã£o luminosa. | Impacts of 
light pollution to wildlife, resident and visitor experience are 
adequately addressed. Tourism enterprises and visitors are encouraged to
 minimise light pollution'. | PoluiÃ§Ã£o luminosa | Light pollution | 3,02 | TREZE TÃLIAS-SC | 4218509 | 3.100000 | Los impactos 
de la contaminaciÃ³n lumÃ­nica en la vida silvestre y en la experiencia 
de los residentes y visitantes se abordan adecuadamente. Se anima a las 
empresas turÃ­sticas y a los visitantes a minimizar la contaminaciÃ³n 
lumÃ­nica. | ContaminaciÃ³n lumÃ­nica | Medio ambiente y clima |
| Community involvement in planning | 5.700000 | 5 | Treze TÃ­lias | 2022 | SC | 5 | Bem-estar social | Social Well-Being | O destino permite e promove a participaÃ§Ã£o pÃºblica no planejamento e na gestÃ£o de destinos sustentÃ¡veis. | The destination enables and promotes public participation in sustainable destination planning and management. | Envolvimento da comunidade em planejamento | Community involvement in planning | 5,07 | TREZE TÃLIAS-SC | 4218509 | 5.200000 | El destino permite y promueve la participaciÃ³n pÃºblica en la planificaciÃ³n y gestiÃ³n sostenible del destino. | ParticipaciÃ³n de la comunidad en la planificaciÃ³n | Bienestar social |

### Explorando as colunas:

- **DESCRICAO:** Nome curto ou título do critério avaliado, originalmente em inglês.
- **CRITERIO:** Código numérico que identifica especificamente o critério (ex: "1.1", "3.8").
- **NOTA:** A pontuação ou grau de sucesso que a cidade obteve na avaliação daquele critério específico.
- **CIDADE:** Nome do município que está sendo avaliado.
- **ANO:** O ano em que a avaliação do município ocorreu (ex: 2022, 2023).
- **ESTADO:** Sigla do estado brasileiro em que a cidade se localiza.
- **THEME:** Código numérico que indica o grande tema (categoria maior) ao qual o critério pertence.
- **THEME_PT, THEME_US, THEME_ES:** O nome do tema principal traduzido para Português, Inglês e Espanhol (ex: "Gerenciamento de destinos").
- **CRITERIA_DESCRIPTION_PT, CRITERIA_DESCRIPTION_US, CRITERIA_DESCRIPTION_ES:** A explicação textual completa e detalhada das exigências daquele critério, apresentada nos três idiomas.
- **CRITERIA_NAME_PT, CRITERIA_NAME_US, CRITERIA_NAME_ES:** O título oficial do critério avaliado, também nos três idiomas (ex: "Coordenador de destinos sustentáveis").
- **ORDEM:** Número decimal utilizado pelo sistema para garantir que os critérios sejam listados na sequência correta.
- **CHAVE:** Um código de texto único para o município, formado pela junção do nome da cidade e seu estado (ex: "TREZE TÍLIAS-SC").
- **CODIGO_MUNICIPIO:** Código numérico oficial de registro da cidade, equivalente ao código IBGE.
- **TOPIC:** Código numérico correspondente ao tópico (a subcategoria) dentro do tema maior ao qual o critério se vincula.

## 4 - TOP100_15.csv

Esta base foca especificamente em um conjunto reduzido dos 15 critérios principais da sustentabilidade. Dessa forma, possuindo a mesma estrutura e colunas da base TOP100_30.csv.

| DESCRICAO | CRITERIO | NOTA | CIDADE | ANO | ESTADO | THEME | THEME_PT | THEME_US | CRITERIA_NAME_PT | CRITERIA_NAME_US | CRITERIA_DESCRIPTION_PT | CRITERIA_DESCRIPTION_US | ORDEM | CHAVE | CODIGO_MUNICIPIO | TOPIC | CRITERIA_NAME_ES | CRITERIA_DESCRIPTION_ES | THEME_ES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sustainable destination coordinator | 1.100000 | 5 | Urubici | 2023 | SC | 1 | Gerenciamento de destinos | Destination Management | Coordenador de destinos sustentÃ¡veis | Sustainable destination coordinator | Uma pessoa foi
 designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | A person has 
been assigned the responsibility and authority for the adequate 
implementation and reporting of sustainable destination management. | 1,01 | URUBICI-SC | 4218905 | 1.100000 | Coordinador de sostenibilidad | Se ha asignado
 a una persona la responsabilidad y la autoridad para la adecuada 
implementaciÃ³n y reporte de la gestiÃ³n sostenible del destino. | GestiÃ³n del destino |
| Inventory of destination assets | 1.500000 | 2,25 | Urubici | 2023 | SC | 1 | Gerenciamento de destinos | Destination Management | InventÃ¡rio de ativos de destino | Inventory of destination assets | O destino tem um inventÃ¡rio de seus ativos e atraÃ§Ãµes voltados para o turismo incluindo locais naturais e culturais. | The destination has an inventory of its tourism-oriented assets and attractions including natural and cultural sites. | 1,05 | URUBICI-SC | 4218905 | 1.200000 | Inventario de activos de destino | El destino 
cuenta con un inventario de sus activos y atracciones orientadas al 
turismo, incluidos los lugares naturales y culturales. | GestiÃ³n del destino |
| Destination Management Policy or Strategy | 1.700000 | 2,75 | Urubici | 2023 | SC | 1 | Gerenciamento de destinos | Destination Management | PolÃ­tica ou estratÃ©gia de gerenciamento de destinos | Destination Management Policy or Strategy | O destino tem 
uma polÃ­tica ou estratÃ©gia de gerenciamento de destino atualizada, 
disponÃ­vel publicamente e plurianual, que aborda questÃµes ambientais, 
sociais, culturais e econÃ´micas. A polÃ­tica Ã© adequada Ã  escala do 
destino, desenvolvida com o envolvimento das partes interessadas e Ã© 
baseada em princÃ­pios de sustentabilidade. Ela estÃ¡ relacionada a e 
influencia polÃ­ticas e aÃ§Ãµes mais amplas de desenvolvimento 
sustentÃ¡vel no destino. | The 
destination has an up-to-date, publicly available, multi-year 
destination management policy or strategy addressing environmental, 
social, cultural and economic issues. The policy is suited to the scale 
of the destination, developed with stakeholder engagement and is based 
on sustainability principles. It relates to and influences wider 
sustainable development policy and action in the destination. | 1,07 | URUBICI-SC | 4218905 | 1.200000 | PolÃ­tica o estrategia de gestiÃ³n de destinos | El destino 
cuenta con una polÃ­tica o estrategia de gestiÃ³n plurianual, 
actualizada y disponible pÃºblicamente, que aborda temas 
medioambientales, sociales, culturales y econÃ³micos. La polÃ­tica se 
desarrolla con la participaciÃ³n de las partes interesadas y se basa en 
los principios de sostenibilidad. Se relaciona e influencia polÃ­ticas 
de desarrollo sostenible y su acciÃ³n en el destino. | GestiÃ³n del destino |
| Tourism impact on nature | 2.200000 | 2,25 | Urubici | 2023 | SC | 2 | Natureza e cenÃ¡rio | Nature & Scenery | Impactos no turismo sobre a natureza | Tourism impacts on nature | O destino mede
 e monitora o impacto do turismo na natureza meio ambiente. Os impactos 
identificados do turismo na natureza sÃ£o respondidos adequadamente. | The 
destination measures and monitors the impact of tourism on the natural 
environment. Identified impacts of tourism on nature are adequately 
responded to. | 2,02 | URUBICI-SC | 4218905 | 2.100000 | Impacto del turismo en la naturaleza | El destino 
mide y monitorea el impacto del turismo en el entorno natural. Se 
responde adecuadamente a los impactos identificados del turismo en la 
naturaleza. | Naturaleza y paisaje |
| Landscape & Scenery | 2.500000 | 2,5 | Urubici | 2023 | SC | 2 | Natureza e cenÃ¡rio | Nature & Scenery | Paisagem e cenÃ¡rio | Landscape & Scenery | As vistas cÃªnicas naturais e rurais sÃ£o protegidas. | Natural and 
rural scenic views are protected; landscape degradation and urban sprawl
 into scenic landscapes is effectively avoided. | 2,05 | URUBICI-SC | 4218905 | 2.100000 | Paisaje y panorama | Se protegen 
las vistas escÃ©nicas naturales y rurales; se evita efectivamente la 
degradaciÃ³n del paisaje y la expansiÃ³n urbana en los paisajes 
escÃ©nicos. | Naturaleza y paisaje |

## 5 - SITUACIONAL_2023.csv

Esta base contém os registros da percepção, opiniões e avaliações dos respondentes locais em relação ao desenvolvimento do turismo na sua cidade. 

| DATA | CODIGO_MUNICIPIO | CIDADE | ESTADO | Q01 | Q02 | Q03 | Q04 | Q05 | Q06 | Q07 | Q08 | Q09 | Q10 | Q11 | Q12 | Q13 | Q14 | Q15 | Q16 | Q17 | Q18 | Q19 | Q20 | Q21 | Q22 | Q23 | Q24 | Q25 | Q26 | Q27 | Q28 | Q29 | Q30 | Q31 | Q32 | Q33 | Q34 | Q35 | Q36 | Q37 | Q38 | Q39 | Q40 | Q41 | Q42 | Q43 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2020-08-04 00:00:00,000 | 4217402 | Schroeder | SC | 8.000000 | 8.000000 | Sim | 7.000000 | 7.000000 | 7.000000 | nan | 8.000000 | 9.000000 | 8.000000 | 7.000000 | 10.000000 | 8.000000 | 8.000000 | 8.000000 | 8.000000 | 7.000000 | 8.000000 | 8.000000 | 4.000000 | 9.000000 | 8.000000 | 7.000000 | 7.000000 | 9.000000 | 9.000000 | 8.000000 | 9.000000 | 8.000000 | 7.000000 | 8.000000 | 8.000000 | 8.000000 | 7.000000 | 7.000000 | Parcialmente | Turista de aventura, ecolÃ³gico, que cuida do municÃ­pio enquanto o conhece. | Morro pelado, Rio do JÃºlio. | Mais forÃ§a 
para aprovaÃ§Ã£o de projetos do turismo perante a prefeitura. Pessoas 
qualificadas para buscar recursos nessa Ã¡rea. (Estadual, federal, 
privado) | PrÃ³xima gestÃ£o do Executivo. | nan | nan | nan |
| 2020-08-17 00:00:00,000 | 4205456 | Forquilhinha | SC | 5.000000 | 8.000000 | Sim | 6.000000 | 7.000000 | 5.000000 | 7.000000 | 3.000000 | 6.000000 | 5.000000 | 4.000000 | 7.000000 | 9.000000 | 5.000000 | nan | 8.000000 | 5.000000 | 10.000000 | 6.000000 | 8.000000 | 8.000000 | 8.000000 | 6.000000 | 9.000000 | 7.000000 | 8.000000 | 9.000000 | 9.000000 | 7.000000 | 6.000000 | nan | nan | nan | nan | 7.000000 | Parcialmente | Turista que busca a experiÃªncia cultural, gastronÃ´mica, festiva, religiosa e lazer. | Apontaria o 
municÃ­pio como um todo, o conjunto da arquitetura alemÃ£, o paisagismo,
 urbanismo e a mobilidade urbana e a cultura e educaÃ§Ã£o do povo. | - Identidade cultural alemÃ£;
- Incentivos na infraestrutura e serviÃ§os;
- Eventos culturais e gastronÃ´micos;
- Parque SÃ£o Francisco de Assis;
- Paisagismo e Sustentabilidade;
- Dr. Zilda Arns e Dom Paulo Evaristo Arns;
... | A falta de planejamento direcionado a identidade turÃ­stica alemÃ£;
A interaÃ§Ã£o entre as trÃªs esferas;
O mal planejamento e execuÃ§Ã£o dos Planos e CÃ³digos do municÃ­pio. | nan | nan | nan |
| 2020-08-25 00:00:00,000 | 4217402 | Schroeder | SC | 7.000000 | 9.000000 | Parcialmente | 5.000000 | 5.000000 | 5.000000 | 7.000000 | 8.000000 | 7.000000 | 7.000000 | 6.000000 | 8.000000 | 10.000000 | 7.000000 | 6.000000 | 7.000000 | 6.000000 | 9.000000 | 7.000000 | 6.000000 | 6.000000 | 6.000000 | 6.000000 | 7.000000 | 6.000000 | 7.000000 | 8.000000 | 7.000000 | 6.000000 | 8.000000 | 8.000000 | 7.000000 | 7.000000 | 7.000000 | 6.000000 | Parcialmente | nan | nan | nan | nan | nan | LINDO E SUSTENTÃVEL! | nan |
| 2020-08-26 00:00:00,000 | 4205902 | Gaspar | SC | 5.000000 | 5.000000 | NÃ£o | 0.000000 | 0.000000 | 0.000000 | nan | 0.000000 | 0.000000 | 8.000000 | 0.000000 | 0.000000 | 8.000000 | nan | nan | nan | nan | 0.000000 | 0.000000 | nan | nan | nan | nan | nan | 0.000000 | 0.000000 | nan | nan | nan | nan | nan | nan | 10.000000 | 1.000000 | nan | Sim | nan | nan | nan | Infraestrutura. | nan | nan | nan |
| 2020-08-26 00:00:00,000 | 4205902 | Gaspar | SC | 8.000000 | 9.000000 | Parcialmente | 8.000000 | 8.000000 | 8.000000 | 7.000000 | 7.000000 | 7.000000 | 9.000000 | 8.000000 | 9.000000 | 9.000000 | 7.000000 | 9.000000 | 7.000000 | 8.000000 | 7.000000 | 7.000000 | 8.000000 | 7.000000 | 9.000000 | 8.000000 | 7.000000 | 7.000000 | 8.000000 | 7.000000 | 8.000000 | 7.000000 | 7.000000 | 7.000000 | 8.000000 | 7.000000 | 7.000000 | 9.000000 | Parcialmente | Todos sÃ£o bem vindos | Parques aquÃ¡ticos; restaurantes; engenhos etc | nan | nan | nan | Lugar ideal para conhecer. | nan |

### Explorando as colunas:

- **Data:** Registra o momento exato em que o respondente finalizou e enviou a pesquisa.
- **Código do Município:** O número oficial de identificação da cidade (equivalente ao código IBGE).
- **Cidade:** O nome do município que está sendo avaliado.
- **Estado:** A sigla da Unidade Federativa (ex: SC, MS) correspondente à cidade.
- O restante das colunas são as perguntas do questionário.

## 6 - Salários e Visitas.csv

Apresenta um levantamento de dados econômicos e de fluxo de visitantes para diversos municípios. O seu conteúdo serve para comparar a remuneração dos trabalhadores dedicados ao setor de turismo com a média salarial geral da cidade, além de quantificar o volume de turistas brasileiros e estrangeiros que cada destino recebe, permitindo analisar o impacto econômico e a atratividade turística de cada local.

| Municipio | SalÃ¡rio MÃ©dio Turismo | SalÃ¡rio MÃ©dio Geral | Visitas Nacionais | Visitas Internacionais |
| --- | --- | --- | --- | --- |
| Amarante | 1372,83 | 3165,43 | 0.000000 | 0.000000 |
| Apodi | 1552,01 | 2394,03 | 251.000000 | 0.000000 |
| Aquidauana | 2044,48 | 2881,29 | 8629.000000 | 1021.000000 |
| Arroio Trinta | nan | 3292,59 | nan | nan |
| Assis Brasil | nan | 2101,8 | 82.000000 | 0.000000 |
- **Municipio:** O nome da cidade ou destino turístico analisado.
- **Salário Médio Turismo:** O valor numérico que representa a média salarial paga especificamente aos trabalhadores do setor de turismo naquele município.
- **Salário Médio Geral:** O valor da média salarial de todos os trabalhadores da cidade, englobando todos os setores da economia local.
- **Visitas Nacionais:** A quantidade registrada de turistas brasileiros (domésticos) que visitaram o destino.
- **Visitas Internacionais:** A quantidade registrada de turistas estrangeiros que visitaram o município.

## 7 - SITUACIONAL_2023_PIVOT_MEDIAN.csv

Esta base atua como uma **consolidação estatística** (focada na mediana/média) das respostas da pesquisa situacional aplicada aos municípios em 2023. Dessa forma, agrupando as informações para apresentar um **resultado único definitivo por cidade para cada pergunta**, calculando a nota central do município em uma questão específica e vinculando o resultado aos grande temas de sustentabilidade.

| ANO | CODIGO_MUNICIPIO | THEME | TOPIC | CRITERIO | NOTA |
| --- | --- | --- | --- | --- | --- |
| 2023 | 4205555 | 6 | 6 | Q28 | 8,25 |
| 2023 | 4205555 | 6 | 6 | Q25 | 5,8888888888888893 |
| 2023 | 4205555 | 6 | 6 | Q32 | 5,4390243902439028 |
| 2023 | 4205555 | 6 | 6 | Q33 | 6,2 |
| 2023 | 4205555 | 6 | 6 | Q27 | 9,0491803278688518 |
- **ANO:** Indica o ano de referência em que a pesquisa e a avaliação foram realizadas (neste caso, 2023).
- **CODIGO_MUNICIPIO:** É o código numérico oficial (padrão IBGE) que identifica exclusivamente a cidade avaliada (ex: "4205555" ou "2411205").
- **THEME:** Um identificador numérico que mostra a qual "Tema" principal de sustentabilidade aquela questão pertence (ex: 6).
- **TOPIC:** Um identificador numérico que vincula a questão a um "Tópico" (uma subcategoria) dentro do tema maior (ex: 6).
- **CRITERIO:** A sigla que identifica a pergunta específica do questionário situacional que foi respondida (ex: "Q25", "Q28", "Q32").
- **NOTA:** O valor numérico decimal que representa a pontuação consolidada (a mediana/média) alcançada pelo município naquela pergunta exata. Por exemplo, uma nota 8,5 ou 5,43 reflete a avaliação geral da cidade para aquele critério.

## 8 - atividade_turistica.csv

Esta base funciona como um i**nventário e mapeamento do nível de desenvolvimento do turismo nos municípios brasileiros**, coletando uma variedade de dados de cada cidade, abrangendo desde a organização política e econômica, até a infraestrutura hoteleira, perfil dos turistas, e detalhamentos especificos sobre aproveitamento de recursos naturais e nauticos.

| UF | MunicÃ­pio | O MunicÃ­pio possui LegislaÃ§Ã£o relacionada ao Turismo? | Quais? | O MunicÃ­pio participa de governanÃ§as regionais e estaduais de turismo? | Quais?_1 | Informar
 as principais parcerias, rede de cooperaÃ§Ã£o, intercÃ¢mbios etc. com 
outros municÃ­pios e/ou entidades regionais, nacionais ou internacionais
 voltados ao desenvolvimento do Turismo. | O MunicÃ­pio participa ou Ã© contemplado em programas ou projetos com o MTur? | Quais?_2 | Informe quais as principais atividades econÃ´micas em seu MunicÃ­pio | Outros, descreva | HÃ¡ um Fundo Municipal de Turismo | Valor disponÃ­vel | NÂº da legislaÃ§Ã£o vigente | O MunicÃ­pio possui Plano Diretor Urbano que contemple o Setor de Turismo | NÃºmero da Lei | O MunicÃ­pio possui Plano Municipal de Turismo e /ou Plano de Desenvolvimento Territorial do Turismo | Ano | O MunicÃ­pio possui Plano de Marketing do Turismo ou outros similares? | Ano_3 | O MunicÃ­pio possui programas, projetos e aÃ§Ãµes acerca da atividade turÃ­stica? | Quais?_4 | Possui gestÃ£o adequada de ResÃ­duos SÃ³lidos? (Conforme Lei nÂº 12.305/2010). | Qual a receita tributÃ¡ria das atividades turÃ­sticas no municÃ­pio? | O municipio possui InventÃ¡rio TurÃ­stico? | Ano da UtilizaÃ§Ã£o | NÂº de hospedagem | NÂº de Leitos | Outros, descreva_5 | Quais os meios de hospedagem mais utilizado pelo turista? | Outros, descreva_6 | Quantos
 meios de hospedagem possuem cadastro no sistema CADASTUR? (Sitema de 
Cadastro de Pessoas FÃ­sicas e JurÃ­dicas que atuam no Setor de 
Turismo). | Qual o perÃ­odo de maior fluxo turÃ­stico? (descreva os meses de Jan-Dez). | Qual o meio de comunicaÃ§Ã£o utilizado para divulgaÃ§Ã£o do destino? | Outros, descreva: | Qual a mÃ©dia do nÃºmero de empregos gerados no setor de hospedagem? | O MunicÃ­pio possui cursos, programas e/ou aÃ§Ãµes de qualificaÃ§Ã£o profissional para o turismo? | Quais?_7 | JÃ¡ houve manifestaÃ§Ã£o de interesse de investidores em empreender no setor de turismo no municÃ­pio? | Quais?_8 | Possui guias e/ou condutores de turismo? | Quantos | O MunicÃ­pio possui locadoras de imÃ³veis, automÃ³veis, embarcaÃ§Ãµes e aeronaves para temporadas? | Quais?_9 | Quantas agÃªncias bancÃ¡rias o municÃ­pio possui? | Quantas casas de cÃ¢mbio o municÃ­pio possui? | Quantos templos de manifestaÃ§Ã£o de fÃ©, igrejas o municÃ­pio possui? | O municÃ­pio possui abastecimento de Ã¡gua, serviÃ§os de esgoto, serviÃ§os de energia, serviÃ§os de coleta de lixo? | Quais?_10 | O municÃ­pio possui aeroporto? | Quais?_11 | Quais os tipos de sistema de Transporte? | Qual a principal forma de acesso ao(s) destino(s) turÃ­stico(s)? | Qual a situaÃ§Ã£o do acesso aos Atrativos TurÃ­sticos do municÃ­pio? | Qual a situaÃ§Ã£o atual da SinalizaÃ§Ã£o TurÃ­stica do municÃ­pio? | O MunicÃ­pio faz parte de alguma rota turÃ­stica? | Quais?_12 | Existe linha regular de transporte turÃ­stico que interligue os principais atrativos? | Descreva as rotas turÃ­sticas | Qual a qualidade da rede de telefonia celular do municÃ­pio? | Qual a qualidade do fornecimento de internet no municÃ­pio? | Quantos prontos socorros pÃºblicos existem? | Quantos prontos socorros privados existem? | Quais sistema de seguranÃ§a e equipamentos que proporcionam Ã  populaÃ§Ã£o e ao turista as garantias bÃ¡sicas do cidadÃ£o? | Outros, descreva_13 | HÃ¡ delegacia de proteÃ§Ã£o ao turista? | Existem locais de embarque e desembarque sinalizados e com acesso em nÃ­vel? | Existem espaÃ§os reservados para pessoa com deficiÃªncia ou mobilidade reduzida? | O 
municÃ­pio dispÃµe de profissionais capacitados para o atendimento de 
pessoas com deficiÃªncia? (ex.: domÃ­nio da LÃ­ngua Brasileira de Sinais
 â LIBRAS). | O municÃ­pio possui acesso ao crÃ©dito do Fundo Geral de Turismo - FUNGETUR? | Qual? | Qual o nÃºmero total de empresas formais do setor do turismo existentes no municÃ­pio? | Qual a mÃ©dia do nÃºmero de empregos gerados no Setor de Turismo? | HÃ¡ uma polÃ­tica de atraÃ§Ã£o de investimentos privados para o setor? | Quem Ã© o responsÃ¡vel? | Valor da arrecadaÃ§Ã£o hÃ¡ dois anos (R$) | AlÃ­quota mÃ©dia do ISS hÃ¡ dois anos (%) | Valor da arrecadaÃ§Ã£o no ano anterior (R$) | AlÃ­quota mÃ©dia do ISS no ano anterior (%) | Quais tipos de PatrimÃ´nio Natural? | HÃ¡ unidades de conservaÃ§Ã£o (federal, estadual e/ou municipal)? | Quais estÃ£o fechadas para uso pÃºblico? | Quais tipos de PatrimÃ´nio Cultural? | NegÃ³cios e eventos | Sol e Praia | Turismo Cultural | Ecoturismo | Turismo de Aventura | Outros, descreva_14 | NegÃ³cios e eventos_15 | Sol e Praia_16 | Turismo Cultural_17 | Ecoturismo_18 | Turismo de Aventura_19 | Outros, descreva_20 | O MunicÃ­pio possui | O MunicÃ­pio possui Ã¡guas termais? | O MunicÃ­pio possui estudo sobre a profundidade desses rios, lagos ou lagoa? | No 
MunicÃ­pio esses rios, lagos ou lagoas sÃ£o navegÃ¡veis, que possui 
possibilidade de equipamentos aquÃ¡ticos como (jet ski, lancha ou 
qualquer outra embarcaÃ§Ã£o) para navegar neles? | Cite o nome desse rio em potencial | O MunicÃ­pio possui pontes sobre o(s) rio(s)? | Cite o nome da ponte, sua altura atÃ© o nÃ­vel da Ã¡gua do rio? | O MunicÃ­pio possuÃ­ marinas/garagens nÃ¡uticas, guarda para barcos? | Informe a quantidade, quais sÃ£o e sua localizaÃ§Ã£o? | Essas estruturas possuem AlvarÃ¡? | Possui LicenÃ§a Ambiental vigente? | O
 MunicÃ­pio possui empresas de comercializaÃ§Ã£o de produtos ou 
serviÃ§os nÃ¡uticos? (stand up, caiaque, surf, pesca, boias, mergulho). | O MunicÃ­pio possui barcos para passeios turÃ­sticos? | Quantos? | O MunicÃ­pio tem Lei que regulamenta a atividade nÃ¡utica? | Qual?_21 | O MunicÃ­pio tem algum projeto nÃ¡utico? | O MunicÃ­pio possui Turismo de Pesca? | Qual?_22 | O MunicÃ­pio possui alguma atividade turÃ­stica de mergulho? | Qual?_23 | O MunicÃ­pio possui alguma atividade turÃ­stica de vela? | Qual?_24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RN | Almino Afonso | Sim | Lei nÂº 386/2011 e Lei nÂº 591/2025 | Sim | IGR Oeste Potiguar | Sebrae/RN | NÃ£o | nan | Agricultura e PecuÃ¡ria, ComÃ©rcio | nan | Sim | 0.000000 | Lei nÂº 591/2025 | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan | NÃ£o | R$ 50.000,00 | NÃ£o | nan | 2 | 23 | nan | Pousada, Casa de amigos/parentes | nan | 0 | Fevereiro/MarÃ§o, Novembro E Dezembro. | Rede sociais, Internet | nan | 30 | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan | 2 | 0 | 16 | Sim | Abastecimento de Ã¡gua, serviÃ§os de esgoto parcial, serviÃ§os de energia e serviÃ§os de coleta de lixo. | NÃ£o | nan | Transporte 
rodoviÃ¡rio de passageiros: (Transporte rodoviÃ¡rio coletivo de 
passageiros, organizaÃ§Ã£o de excursÃµes em veÃ­culos rodoviÃ¡rios 
prÃ³prios, ServiÃ§o de tÃ¡xi e locaÃ§Ã£o de automÃ³veis) | Rodovia | Regular | NÃ£o tem sinalizaÃ§Ã£o turÃ­stica | NÃ£o | nan | NÃ£o | nan | Regular | Regular | 4 | 0 | Postos de saÃºde, Delegacias de PolÃ­cia, Hospitais e defesa civil | nan | NÃ£o | NÃ£o | NÃ£o | Sim | NÃ£o | nan | 10 | 30 | NÃ£o | nan | 314460.140000 | 5.000000 | 228206.000000 | 5.000000 | nan | NÃ£o | nan | Outros | 2.000000 | 6.000000 | 4.000000 | 6.000000 | 5.000000 | nan | nan | nan | nan | nan | nan | nan | Rios | NÃ£o | NÃ£o | NÃ£o | nan | Sim | O municÃ­pio nÃ£o detÃ©m dessas informaÃ§Ãµes. | NÃ£o | nan | NÃ£o | NÃ£o | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan |
| RN | Alto do Rodrigues | Sim | Lei Municipal de CriaÃ§Ã£o do Conselho de Turismo | Sim | Instancia de GovernanÃ§a do SertÃ£o para o mar | a formalizaÃ§Ã£o da IGR  com outros municÃ­pios vizinhos | NÃ£o | nan | ServiÃ§os, Agricultura e PecuÃ¡ria, ComÃ©rcio | nan | NÃ£o | nan | nan | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan | Sim | AÃ§Ã£o de mÃ­dia de incentivo turÃ­stico , parcerias com Feira e eventos de caracterÃ­stica turÃ­stica, eventos locais. | NÃ£o | Em mÃ©dia de 100 mil | Sim | 2025.000000 | 11 | 326 | nan | Hotel, Casa de amigos/parentes, Pousada | nan | 04 | MarÃ§o-Abril , Julho, Outubro | RÃ¡dio e TelevisÃ£o, Rede sociais, Internet, IndicaÃ§Ã£o de parentes/amigos | nan | 50 | NÃ£o | nan | Sim | Alto folia | NÃ£o | nan | Sim | imÃ³veis, automÃ³veis | 3 | 0 | 29 | Sim | serviÃ§os de energia , abastecimento de Ã¡gua , coleta de lixo, serviÃ§os de esgoto | NÃ£o | nan | Transporte 
rodoviÃ¡rio de passageiros: (Transporte rodoviÃ¡rio coletivo de 
passageiros, organizaÃ§Ã£o de excursÃµes em veÃ­culos rodoviÃ¡rios 
prÃ³prios, ServiÃ§o de tÃ¡xi e locaÃ§Ã£o de automÃ³veis) | Rodovia | Boa | NÃ£o tem sinalizaÃ§Ã£o turÃ­stica | Sim | Do sertÃ£o para o mar ( roteiro em processo) | NÃ£o | nan | Ãtima | Ãtima | 1 | 0 | Delegacias de PolÃ­cia, Postos de saÃºde, Hospitais e defesa civil, Postos de polÃ­cia rodoviÃ¡ria | nan | NÃ£o | NÃ£o | NÃ£o | NÃ£o | NÃ£o | nan | 30 | 40 | NÃ£o | nan | 13522520.600000 | 5.000000 | 8827834.550000 | 5.000000 | nan | NÃ£o | nan | HistÃ³rico: 
(edificaÃ§Ãµes tombadas com genuÃ­no fluxo e interesse turÃ­stico e 
histÃ³rico), Equipamentos: (Museus; Pinacotecas; Teatros; Anfiteatros) | 1.000000 | 6.000000 | 3.000000 | 6.000000 | 6.000000 | nan | nan | nan | nan | nan | nan | nan | Rios | NÃ£o | NÃ£o | Sim | Rio Piranhas-aÃ§u | Sim | Popularmente conhecida como, "ponte do rio do Alto! | NÃ£o | nan | NÃ£o | NÃ£o | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan |
| RN | Angicos | Sim | Lei de CriaÃ§Ã£o
 do Conselho Municipal do Turismo - Lei Municipal nÂº 1.183/2021 e Lei 
Municipal de CriaÃ§Ã£o do Fundo Municipal de Turismo - Lei Municipal nÂº
 1.182/2021 | Sim | IGR CABUGI CENTRAL | MunicÃ­pios da IGR CABUGI CENTRAL, IUFERSA, BNB e CDL | Sim | RegionalizaÃ§Ã£o do turismo | ComÃ©rcio, Turismo, Agricultura e PecuÃ¡ria, ServiÃ§os | nan | Sim | 30000.000000 | Lei Municipal nÂº 1182/2021 | NÃ£o | nan | NÃ£o | nan | Sim | 2024.000000 | NÃ£o | nan | NÃ£o | 1.500.000,00 | NÃ£o | nan | 4 | 200 | nan | Pousada, Casa de amigos/parentes | Pousada | 1 | Fevereiro, MarÃ§o, Julho E Outubro | Jornais, RÃ¡dio e TelevisÃ£o, IndicaÃ§Ã£o de parentes/amigos, Rede sociais, Internet | nan | 800 | NÃ£o | nan | NÃ£o | nan | Sim | 1.000000 | NÃ£o | nan | 4 | 0 | 30 | Sim | CAERN | NÃ£o | nan | Transporte 
rodoviÃ¡rio de passageiros: (Transporte rodoviÃ¡rio coletivo de 
passageiros, organizaÃ§Ã£o de excursÃµes em veÃ­culos rodoviÃ¡rios 
prÃ³prios, ServiÃ§o de tÃ¡xi e locaÃ§Ã£o de automÃ³veis) | Rodovia | Boa | Boa | Sim | CABUGI CENTRAL | NÃ£o | nan | Ãtima | Ãtima | 1 | 0 | Hospitais e defesa civil, Postos de saÃºde, Outros, Delegacias de PolÃ­cia | COMPANHIA DA POLICIA MILITAR | NÃ£o | Sim | Sim | Sim | NÃ£o | nan | 10 | 100 | NÃ£o | nan | 1500000.000000 | 2.000000 | 2000000.000000 | 5.000000 | Reservas ecolÃ³gicas, Unidade de ConservaÃ§Ã£o, Parques Naturais | Sim | PARQUE ECOLÃGICO  DE CONSERVAÃÃO DO PICO DO CABUGI | Outros | 1.000000 | 6.000000 | 1.000000 | 1.000000 | 1.000000 | nan | nan | nan | nan | nan | nan | nan | Rios, Lagoas | NÃ£o | NÃ£o | Sim | LAGOA AZUL | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | Sim | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan |
| RN | Apodi | Sim | Fundo Municipal 
de Turismo, Lei de CriaÃ§Ã£o da Secretaria Municipal de Turismo e 
Cultura, Conselho Municipal de Turismo e Projeto da Semana do Turismo 
PedagÃ³gico. | Sim | IGR Oeste Potiguar | CONETUR, IGR OESTE POTIGUAR, ALIANÃA DO OESTE POTIGUAR | NÃ£o | nan | ComÃ©rcio, ServiÃ§os, Agricultura e PecuÃ¡ria, Turismo | nan | Sim | 0.000000 | 1970/2023 | Sim | LEI NÂ° 479/2006, DE 10 DE OUTUBRO DE 2006 | Sim | 2023.000000 | NÃ£o | nan | Sim | PROJETO DO INVENTARIO TURISTICO E ANDAMENTO | NÃ£o | 0 | NÃ£o | nan | 5 | 120 | nan | Hotel, Casa de amigos/parentes, Pousada | nan | 4 | Fevereiro | IndicaÃ§Ã£o de parentes/amigos, Rede sociais, Internet, RÃ¡dio e TelevisÃ£o | nan | 100 | Sim | HOTELARIA, GARÃON, CONDUTOR TURÃSTICO LOCAL | Sim | MIRANTES | Sim | 16.000000 | NÃ£o | nan | 6 | 0 | 27 | Sim | cosern | NÃ£o | nan | Transporte 
rodoviÃ¡rio de passageiros: (Transporte rodoviÃ¡rio coletivo de 
passageiros, organizaÃ§Ã£o de excursÃµes em veÃ­culos rodoviÃ¡rios 
prÃ³prios, ServiÃ§o de tÃ¡xi e locaÃ§Ã£o de automÃ³veis) | Rodovia | Boa | PrecÃ¡ria | Sim | Rota das cavernas | NÃ£o | nan | Boa | Ãtima | 3 | 0 | Corpo de bombeiros, Postos de saÃºde, Delegacias de PolÃ­cia, Hospitais e defesa civil | nan | NÃ£o | NÃ£o | Sim | NÃ£o | NÃ£o | nan | 7 | 100 | NÃ£o | nan | 190000.000000 | 5.000000 | 180000.000000 | 5.000000 | Unidade de ConservaÃ§Ã£o | Sim | casarÃµes, museus | HistÃ³rico: 
(edificaÃ§Ãµes tombadas com genuÃ­no fluxo e interesse turÃ­stico e 
histÃ³rico), Equipamentos: (Museus; Pinacotecas; Teatros; Anfiteatros) | 2.000000 | 6.000000 | 1.000000 | 4.000000 | 5.000000 | nan | nan | nan | nan | nan | nan | nan | Lagoas, Rios | NÃ£o | NÃ£o | Sim | Lagoa do Apodi | Sim | Ponte da Marinha | NÃ£o | nan | NÃ£o | NÃ£o | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan |
| RN | CarnaÃºba dos Dantas | Sim | LEI NÂº979, DE 
27 DE AGOSTO DE 2018 DispÃµe sobre o Fundo Municipal de Turismo, cria o 
Conselho Municipal de Turismo; LEI NÂº 1131, DE 23 DE DEZEMBRO DE 2021 
Cria a Secretaria de Turismo e Desenvolvimento EconÃ´mico | Sim | GEOPARQUE SERIDÃ, IGRS - SeridÃ³ | Governo do Estado | NÃ£o | nan | ComÃ©rcio, ServiÃ§os, Turismo, Agricultura e PecuÃ¡ria, IndÃºstria de base | nan | Sim | 0.000000 | LEI NÂº979, DE 27 DE AGOSTO DE 2018 | NÃ£o | nan | NÃ£o | nan | Sim | 2026.000000 | Sim | Projeto 
turismo pedagÃ³gico; AÃ§Ãµes de revitalizaÃ§Ã£o de trilhas e descoberta 
de novos SÃ­tios arqueolÃ³gicos; Projeto de DivulgaÃ§Ã£o turÃ­stica 
atravÃ©s de vÃ­deos. | NÃ£o | NÃO TENHO A INFORMAÃÃO | Sim | 2023.000000 | 1 | 8 | nan | Casa de amigos/parentes, Camping, Pousada | nan | 0 | Out-Dez. | Outros, Internet, RÃ¡dio e TelevisÃ£o, Rede sociais, IndicaÃ§Ã£o de parentes/amigos | Panfletos; outdoor | 3 | Sim | CapacitaÃ§Ãµes
 e oficinas para empreendedores e prestadores de serviÃ§os turÃ­sticos, 
em parceria com o Sebrae/RN; condutor local; atendimento ao turista, 
hospitalidade e prÃ¡ticas sustentÃ¡veis. | Sim | pousadas, restaurantes | Sim | 14.000000 | NÃ£o | nan | 0 | 0 | 17 | Sim | Sim. O 
MunicÃ­pio conta com abastecimento regular de Ã¡gua, serviÃ§os de 
esgotamento sanitÃ¡rio, fornecimento de energia elÃ©trica e coleta 
periÃ³dica de lixo, atendendo a toda a Ã¡rea urbana e parte da zona 
rural. | NÃ£o | nan | Transporte 
rodoviÃ¡rio de passageiros: (Transporte rodoviÃ¡rio coletivo de 
passageiros, organizaÃ§Ã£o de excursÃµes em veÃ­culos rodoviÃ¡rios 
prÃ³prios, ServiÃ§o de tÃ¡xi e locaÃ§Ã£o de automÃ³veis) | Outros, Rodovia | Boa | Boa | Sim | geoparque SeridÃ³, Religiosa e ArqueolÃ³gica | NÃ£o | nan | Ãtima | Ãtima | 6 | 0 | Delegacias de PolÃ­cia, Postos de saÃºde | nan | NÃ£o | Sim | Sim | Sim | NÃ£o | nan | 0 | 3 | NÃ£o | nan | 871401.620000 | 5.000000 | 386905.620000 | 5.000000 | Parques Naturais, Reservas ecolÃ³gicas, Outros | NÃ£o | nan | Equipamentos: 
(Museus; Pinacotecas; Teatros; Anfiteatros), HistÃ³rico: (edificaÃ§Ãµes 
tombadas com genuÃ­no fluxo e interesse turÃ­stico e histÃ³rico) | 1.000000 | 6.000000 | 1.000000 | 1.000000 | 2.000000 | nan | nan | nan | nan | nan | nan | nan | Rios | NÃ£o | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | NÃ£o | nan | NÃ£o | nan | NÃ£o | nan |

### Explorando as colunas:

**1. Identificação Geográfica**

- **UF e Município:** Indicam o estado e o nome da cidade avaliada.

**2. Gestão, Legislação e Governança**

- **O Município possui Legislação relacionada ao Turismo? / Quais?:** Indica a existência de leis municipais (como criação de conselhos) voltadas ao turismo.
- **O Município participa de governanças regionais e estaduais de turismo? / Quais?_1:** Mostra se a cidade integra circuitos ou polos turísticos regionais.
- **Informar as principais parcerias, rede de cooperação, intercâmbios etc...:** Lista as entidades que ajudam no desenvolvimento local (ex: SEBRAE, SENAC).
- **O Município participa ou é contemplado em programas ou projetos com o MTur? / Quais?_2:** Informa se há apoio ou verba do Ministério do Turismo.

**3. Economia, Planejamento e Arrecadação**

- **Informe quais as principais atividades econômicas em seu Município / Outros, descreva:** Contextualiza a base da economia local (ex: Comércio, Agricultura).
- **Fundo Municipal, Planos e Leis Vigentes:** Diversas colunas detalham se o município possui e quais são os números das leis e os anos de criação para: **Fundo Municipal de Turismo** (e seu **Valor disponível**), **Plano Diretor Urbano**, **Plano Municipal/Territorial de Turismo**, e **Plano de Marketing do Turismo**.
- **Ações e Receitas:** Colunas sobre **O Município possui programas, projetos e ações acerca da atividade turística?** (Quais?_4) e **Qual a receita tributária das atividades turísticas no município?**.
- **Interesse Privado:** Avalia se **Já houve manifestação de interesse de investidores em empreender no setor...** (Quais?_8).

**4. Infraestrutura Hoteleira e Serviços Turísticos**

- **Inventário:** Pergunta se **O município possui Inventário Turístico?** e o **Ano da Utilização**.
- **Hospedagem:** Uma série de colunas quantifica a rede de apoio: **Nº de hospedagem**, **Nº de Leitos**, **Quais os meios de hospedagem mais utilizado pelo turista?** (com colunas Outros para complementação), e **Quantos meios de hospedagem possuem cadastro no sistema CADASTUR?**.
- **Empregos:** Mede **Qual a média do número de empregos gerados no setor de hospedagem?**.
- **Qualificação e Guias:** Analisa se **O Município possui cursos, programas e/ou ações de qualificação profissional...** (Quais?_7) e se **Possui guias e/ou condutores de turismo?** (**Quantos?**).
- **Locação Temporária:** Pergunta se **O Município possui locadoras de imóveis, automóveis, embarcações e aeronaves para temporadas?** (Quais?).

**5. Fluxo de Visitantes e Promoção**

- **Fluxo:** Coluna **Qual o período de maior fluxo turístico?** (mapeia os meses de alta temporada).
- **Comunicação:** Colunas **Qual o meio de comunicação utilizado para divulgação do destino?** e **Outros, descreva:**.

**6. Sustentabilidade e Patrimônio**

- **Resíduos Sólidos:** A coluna **Possui gestão adequada de Resíduos Sólidos?** avalia o saneamento básico de acordo com a lei federal.
- **Patrimônio Cultural:** Avalia áreas **fechadas para uso público?** e **Quais tipos de Patrimônio Cultural?**.

**7. Avaliação dos Segmentos Turísticos**

- Existe um grande bloco de colunas usado para avaliar o foco turístico do município em nichos específicos, que incluem: **Negócios e eventos**, **Sol e Praia**, **Turismo Cultural**, **Ecoturismo**, e **Turismo de Aventura** (estas colunas se repetem com numerações como _15 a _19 para avaliações complementares, acompanhadas de várias colunas **Outros, descreva**) e uma genérica **O Município possui**.

**8. Turismo Náutico e Natureza Hídrica**

- Um bloco final foca detalhadamente em águas e navegação:
    - **O Município possui águas termais?**
    - **O Município possui estudo sobre a profundidade desses rios, lagos ou lagoa?**
    - **Navegabilidade:** Pergunta se **No Município esses rios, lagos ou lagoas são navegáveis... com possibilidade de equipamentos aquáticos...** e pede para **Cite o nome desse rio em potencial**.
    - **Pontes:** Questiona se **O Município possui pontes sobre o(s) rio(s)?** e pede para detalhar: **Cite o nome da ponte, sua altura até o nível da água do rio?**.
    - **Infraestrutura Náutica e Legalidade:** Pergunta se **O Município possuí marinas/garagens náuticas, guarda para barcos?**, exigindo **Informe a quantidade, quais são e sua localização?**, e checa a regularização através das colunas **Essas estruturas possuem Alvará?** e **Possui Licença Ambiental vigente?**.
    - **Comércio Náutico:** Por fim, pergunta se **O Município possui empresas de comercialização de produtos ou serviços náuticos?**.

## 9 - PIVOT_SITUACIONAL.csv

Esta base funciona como um **dicionário de dados ou tabela de referência estrutural** para o questionário situacional. Dessa forma, ela não possui os dados de resultados da pesquisa, mas sim um mapa da estrutura do questionário do sistema, definindo todas as opções de respostas possíveis para cada pergunta, qual peso numérico cada resposta tem e a qual tema da sustentabilidade a pergunta pertence, sendo responsável por traduzir as respostas cruas em métricas para visualização.

| EIXO | ORDEM | ESCALA | QUESTAO | TEXTO | VALOR | GRUPO | GRUPO_ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | NUMERICA | Q01 | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Perfil do Entrevistado | 0 |
| 1 | 1 | NUMERICA | Q01 | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Perfil do Entrevistado | 0 |
| 2 | 2 | NUMERICA | Q01 | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Perfil do Entrevistado | 0 |
| 3 | 3 | NUMERICA | Q01 | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Perfil do Entrevistado | 0 |
| 4 | 4 | NUMERICA | Q01 | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | Perfil do Entrevistado | 0 |

### Explorando as colunas:

- **EIXO:** Um número em formato de texto (ex: "0", "1", "2") que funciona como um identificador para a variação da escala de respostas.
- **ORDEM:** Um valor numérico sequencial (0, 1, 2, 3...) utilizado para organizar e ordenar os dados visualmente.
- **ESCALA:** Indica a natureza da resposta daquela questão, classificando-a, por exemplo, como “NUMERICA”.
- **QUESTAO:** O código curto e único que identifica cada pergunta do questionário (ex: “Q01”, “Q04”, “Q06”).
- **TEXTO:** O enunciado completo e literal da pergunta feita ao entrevistado (ex: *"Nos últimos 5 anos como você avalia o turismo do município?"* ou *"O desenvolvimento do turismo no município é planejado?"*).
- **VALOR:** Neste arquivo, esta coluna repete exatamente o texto da pergunta (o enunciado literal), provavelmente servindo como rótulo de exibição (valor) da métrica nos painéis e gráficos do sistema.
- **GRUPO:** O nome do eixo temático ou categoria de avaliação ao qual a pergunta pertence (ex: “Perfil do entrevistado”, “Gerenciamento de destinos”).
- **GRUPO_ID:** O código numérico correspondente ao grupo temático citado na coluna anterior (ex: 0 para Perfil do Entrevistado, 1 para Gerenciamento de destinos).

## 10 - IBGE.csv

Esta base contém **dados estatísticos e demográficos dos municipios** brasileiros, traçando um “raio-X” completo da realidade socioeconômica, educacional, ambiental e geográfica de cada cidade.

| CIDADE | ESTADO | IMAGEM | POPULACAO | DENSIDADE_DEMOGRAFICA | SALARIO_MEDIO | PESSOAS_OCUPADA | POPULACAO_OCUPADA | PERCENTUAL_MEIO_MINIMO | TAXA_ESCOLARIDADE | IDEB_ANOSINICIAIS | IDEB_ANOSFINAIS | MATRICULAS_FUNDAMENTAL | MATRICULAS_MEDIO | DOCENTES_FUNDAMENTAL | DOCENTES_MEDIO | ESTABELECIMENTOS_FUNDAMENTAL | ESTABELECIMENTOS_MEDIO | PIB | PERCENTUAL_EXTERNAS | IDHM | TOTAL_RECEITAS | TOTAL_DESPESAS | MORTALIDADE | INTERNACOES_DIARREIA | ESTABELECIMENTO_SUS | AREA_URBANA | ESGOTO | ARBORIZACAO | URBANIZACAO | POPULAZAO_RISCO | BIOMA | SISTEMA_COSTEIRO | AREA_TERRITORIAL | REGIAO_INTERMEDIARIA | MESORREGIAO | MICRORREGIAO | CODIGO_MUNICIPIO | SVG_MAPA | LINK_IBGE | TEXTO_POPULACAO | TEXTO_TRABALHO | TEXTO_EDUCACAO | TEXTO_ECONOMIA | TEXTO_SAUDE | TEXTO_MEIO_AMBIENTE | TEXTO_TERRITORIO | _POSSUI_GD | _POSSUI_TOP100C15 | _POSSUI_TOP100C30 | _POSSUI_SITUACIONAL | CIDADE_CAGED | CAGED_MUNICIPIO | CAGED_TURISMO | CAGED_ESTOQUE_MUNICIPIO | CAGED_ESTOQUE_TURISMO | CERTIFICADO | CATEGORIA | Cidade_acento |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Assis Brasil | AC | 1200054.jpg | 8100 | 1,63 | 2,3 | 545 | 7,13 | 47,1 | 85,1 | 4,6 | nan | 2536 | 394 | 92 | 18 | 67 | 2 | 17507,67 | nan | 0,588 | 18177,08 | 17004,91 | 13,95 | 2,3 | 5 | 2,04 | 23,1 | 26,5 | 0 | nan | AmazÃ´nia | NÃ£o pertence | 4979,073 | Rio Branco | Vale do Acre | BrasilÃ©ia | 1200054 | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200054.svg | https://cidades.ibge.gov.br/municipio/1200054 | Em 2022, a 
populaÃ§Ã£o era de 8.100 habitantes e a densidade demogrÃ¡fica era de 
1,63 habitantes por quilÃ´metro quadrado. Na comparaÃ§Ã£o com outros 
municÃ­pios do estado, ficava nas posiÃ§Ãµes 21 e 37 de 22. JÃ¡ na 
comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 3380
 e 10807 de 5570. | Em 2021, o 
salÃ¡rio mÃ©dio mensal era de 2,3 salÃ¡rios mÃ­nimos. A proporÃ§Ã£o de 
pessoas ocupadas em relaÃ§Ã£o Ã  populaÃ§Ã£o total era de 7,13%. Na 
comparaÃ§Ã£o com os outros municÃ­pios do estado, ocupava as posiÃ§Ãµes 3
 de 22 e 9 de 22, respectivamente. JÃ¡ na comparaÃ§Ã£o com cidades do 
paÃ­s todo, ficava na posiÃ§Ã£o 958 de 5570 e 4719 de 5570, 
respectivamente. Considerando domicÃ­lios com rendimentos mensais de 
atÃ© meio salÃ¡rio mÃ­nimo por pessoa, tinha 47,1% da populaÃ§Ã£o nessas
 condiÃ§Ãµes, o que o colocava na posiÃ§Ã£o 10 de 22 dentre as cidades 
do estado e na posiÃ§Ã£o 1869 de 5570 dentre as cidades do Brasil. | Em 2010, a 
taxa de escolarizaÃ§Ã£o de 6 a 14 anos de idade era de 85,1%. Na 
comparaÃ§Ã£o com outros municÃ­pios do estado, ficava na posiÃ§Ã£o 18 de
 22. JÃ¡ na comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava na 
posiÃ§Ã£o 5525 de 5570. Em relaÃ§Ã£o ao IDEB, no ano de 2021, o IDEB 
para os anos iniciais do ensino fundamental na rede pÃºblica era 4,6 e 
para os anos finais, de (nÃ£o hÃ¡ dados). Na comparaÃ§Ã£o com outros 
municÃ­pios do estado, ficava nas posiÃ§Ãµes 16 e (nÃ£o hÃ¡ dados) de 
22. JÃ¡ na comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava nas 
posiÃ§Ãµes 4347 e (nÃ£o hÃ¡ dados) de 5570. | nan | A taxa de 
mortalidade infantil mÃ©dia na cidade Ã© de 13,95 para 1.000 nascidos 
vivos. As internaÃ§Ãµes devido a diarreias sÃ£o de 2,3 para cada 1.000 
habitantes. Comparado com todos os municÃ­pios do estado, fica nas 
posiÃ§Ãµes 14 de 22 e 9 de 22, respectivamente. Quando comparado a 
cidades do Brasil todo, essas posiÃ§Ãµes sÃ£o de 1866 de 5570 e 1400 de 
5570, respectivamente. | Apresenta 
23,1% de domicÃ­lios com esgotamento sanitÃ¡rio adequado, 26,5% de 
domicÃ­lios urbanos em vias pÃºblicas com arborizaÃ§Ã£o e 0% de 
domicÃ­lios urbanos em vias pÃºblicas com urbanizaÃ§Ã£o adequada 
(presenÃ§a de bueiro, calÃ§ada, pavimentaÃ§Ã£o e meio-fio). Quando 
comparado com os outros municÃ­pios do estado, fica na posiÃ§Ã£o 5 de 
22, 9 de 22 e 21 de 22, respectivamente. JÃ¡ quando comparado a outras 
cidades do Brasil, sua posiÃ§Ã£o Ã© 3464 de 5570, 4945 de 5570 e 4835 de
 5570, respectivamente. | Em 2022, a 
Ã¡rea do municÃ­pio era de 4.979,073 kmÂ², o que o coloca na posiÃ§Ã£o 
13 de 22 entre os municÃ­pios do estado e 308 de 5570 entre todos os 
municÃ­pios. | False | False | False | True | 120005 | 2 | 0 | 235 | 5 | nan | D | assis brasil |
| Cruzeiro do Sul | AC | 1200203.jpg | 91888 | 10,46 | 1,8 | 11869 | 13,22 | 44,2 | 94,9 | 5,4 | 4,8 | 18823 | 5412 | 756 | 269 | 148 | 23 | 22934,82 | 88,1 | 0,664 | 139636,41 | 135990,85 | 10,64 | 1 | 40 | 26,91 | 12,7 | 37,9 | 3,7 | nan | AmazÃ´nia | NÃ£o pertence | 8783,47 | Cruzeiro do Sul | Vale do JuruÃ¡ | Cruzeiro do Sul | 1200203 | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200203.svg | https://cidades.ibge.gov.br/municipio/1200203 | Em 2022, a 
populaÃ§Ã£o era de 91.888 habitantes e a densidade demogrÃ¡fica era de 
10,46 habitantes por quilÃ´metro quadrado. Na comparaÃ§Ã£o com outros 
municÃ­pios do estado, ficava nas posiÃ§Ãµes 2 e 5 de 22. JÃ¡ na 
comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 355 e
 8571 de 5570. | Em 2021, o 
salÃ¡rio mÃ©dio mensal era de 1,8 salÃ¡rios mÃ­nimos. A proporÃ§Ã£o de 
pessoas ocupadas em relaÃ§Ã£o Ã  populaÃ§Ã£o total era de 13,22%. Na 
comparaÃ§Ã£o com os outros municÃ­pios do estado, ocupava as posiÃ§Ãµes 
13 de 22 e 3 de 22, respectivamente. JÃ¡ na comparaÃ§Ã£o com cidades do 
paÃ­s todo, ficava na posiÃ§Ã£o 3288 de 5570 e 2851 de 5570, 
respectivamente. Considerando domicÃ­lios com rendimentos mensais de 
atÃ© meio salÃ¡rio mÃ­nimo por pessoa, tinha 44,2% da populaÃ§Ã£o nessas
 condiÃ§Ãµes, o que o colocava na posiÃ§Ã£o 19 de 22 dentre as cidades 
do estado e na posiÃ§Ã£o 2237 de 5570 dentre as cidades do Brasil. | Em 2010, a 
taxa de escolarizaÃ§Ã£o de 6 a 14 anos de idade era de 94,9%. Na 
comparaÃ§Ã£o com outros municÃ­pios do estado, ficava na posiÃ§Ã£o 4 de 
22. JÃ¡ na comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava na 
posiÃ§Ã£o 5043 de 5570. Em relaÃ§Ã£o ao IDEB, no ano de 2021, o IDEB 
para os anos iniciais do ensino fundamental na rede pÃºblica era 5,4 e 
para os anos finais, de 4,8. Na comparaÃ§Ã£o com outros municÃ­pios do 
estado, ficava nas posiÃ§Ãµes 3 e 6 de 22. JÃ¡ na comparaÃ§Ã£o com 
municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 2921 e 2559 de 5570. | Em 2021, o PIB
 per capita era de R$ 22.934,82. Na comparaÃ§Ã£o com outros municÃ­pios 
do estado, ficava nas posiÃ§Ãµes 10 de 22 entre os municÃ­pios do estado
 e na 2846 de 5570 entre todos os municÃ­pios. JÃ¡ o percentual de 
receitas externas em 2015 era de 88,1%, o que o colocava na posiÃ§Ã£o 10
 de 22 entre os municÃ­pios do estado e na 2605 de 5570. Em 2017, o 
total de receitas realizadas foi de R$ 139.636,41 (x1000) e o total de 
despesas empenhadas foi de R$ 135.990,85 (x1000). Isso deixa o 
municÃ­pio nas posiÃ§Ãµes 2 e 2 de 22 entre os municÃ­pios do estado e 
na 629 e 578 de 5570 entre todos os municÃ­pios. | A taxa de 
mortalidade infantil mÃ©dia na cidade Ã© de 10,64 para 1.000 nascidos 
vivos. As internaÃ§Ãµes devido a diarreias sÃ£o de 1 para cada 1.000 
habitantes. Comparado com todos os municÃ­pios do estado, fica nas 
posiÃ§Ãµes 18 de 22 e 14 de 22, respectivamente. Quando comparado a 
cidades do Brasil todo, essas posiÃ§Ãµes sÃ£o de 2610 de 5570 e 2419 de 
5570, respectivamente. | Apresenta 
12,7% de domicÃ­lios com esgotamento sanitÃ¡rio adequado, 37,9% de 
domicÃ­lios urbanos em vias pÃºblicas com arborizaÃ§Ã£o e 3,7% de 
domicÃ­lios urbanos em vias pÃºblicas com urbanizaÃ§Ã£o adequada 
(presenÃ§a de bueiro, calÃ§ada, pavimentaÃ§Ã£o e meio-fio). Quando 
comparado com os outros municÃ­pios do estado, fica na posiÃ§Ã£o 11 de 
22, 6 de 22 e 11 de 22, respectivamente. JÃ¡ quando comparado a outras 
cidades do Brasil, sua posiÃ§Ã£o Ã© 4156 de 5570, 4604 de 5570 e 3719 de
 5570, respectivamente. | Em 2022, a 
Ã¡rea do municÃ­pio era de 8.783,47 kmÂ², o que o coloca na posiÃ§Ã£o 6 
de 22 entre os municÃ­pios do estado e 151 de 5570 entre todos os 
municÃ­pios. | False | False | False | True | 120020 | 61 | -4 | 7390 | 284 | nan | C | cruzeiro do sul |
| EpitaciolÃ¢ndia | AC | 1200252.jpeg | 18757 | 11,35 | 1,7 | 2040 | 10,75 | 42,9 | 93,7 | 5,3 | 5,1 | 2749 | 663 | 98 | 24 | 17 | 2 | 33960,77 | nan | 0,653 | 31996,17 | 29191,83 | 17,06 | 0,2 | 8 | 4,93 | 21,4 | 39,1 | 11 | 4333.000000 | AmazÃ´nia | NÃ£o pertence | 1652,674 | Rio Branco | Vale do Acre | BrasilÃ©ia | 1200252 | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200252.svg | https://cidades.ibge.gov.br/municipio/1200252 | Em 2022, a 
populaÃ§Ã£o era de 18.757 habitantes e a densidade demogrÃ¡fica era de 
11,35 habitantes por quilÃ´metro quadrado. Na comparaÃ§Ã£o com outros 
municÃ­pios do estado, ficava nas posiÃ§Ãµes 9 e 3 de 22. JÃ¡ na 
comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 1801
 e 8345 de 5570. | Em 2021, o 
salÃ¡rio mÃ©dio mensal era de 1,7 salÃ¡rios mÃ­nimos. A proporÃ§Ã£o de 
pessoas ocupadas em relaÃ§Ã£o Ã  populaÃ§Ã£o total era de 10,75%. Na 
comparaÃ§Ã£o com os outros municÃ­pios do estado, ocupava as posiÃ§Ãµes 
17 de 22 e 4 de 22, respectivamente. JÃ¡ na comparaÃ§Ã£o com cidades do 
paÃ­s todo, ficava na posiÃ§Ã£o 3962 de 5570 e 3513 de 5570, 
respectivamente. Considerando domicÃ­lios com rendimentos mensais de 
atÃ© meio salÃ¡rio mÃ­nimo por pessoa, tinha 42,9% da populaÃ§Ã£o nessas
 condiÃ§Ãµes, o que o colocava na posiÃ§Ã£o 20 de 22 dentre as cidades 
do estado e na posiÃ§Ã£o 2373 de 5570 dentre as cidades do Brasil. | Em 2010, a 
taxa de escolarizaÃ§Ã£o de 6 a 14 anos de idade era de 93,7%. Na 
comparaÃ§Ã£o com outros municÃ­pios do estado, ficava na posiÃ§Ã£o 7 de 
22. JÃ¡ na comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava na 
posiÃ§Ã£o 5263 de 5570. Em relaÃ§Ã£o ao IDEB, no ano de 2021, o IDEB 
para os anos iniciais do ensino fundamental na rede pÃºblica era 5,3 e 
para os anos finais, de 5,1. Na comparaÃ§Ã£o com outros municÃ­pios do 
estado, ficava nas posiÃ§Ãµes 5 e 1 de 22. JÃ¡ na comparaÃ§Ã£o com 
municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 3133 e 1607 de 5570. | nan | A taxa de 
mortalidade infantil mÃ©dia na cidade Ã© de 17,06 para 1.000 nascidos 
vivos. As internaÃ§Ãµes devido a diarreias sÃ£o de 0,2 para cada 1.000 
habitantes. Comparado com todos os municÃ­pios do estado, fica nas 
posiÃ§Ãµes 10 de 22 e 17 de 22, respectivamente. Quando comparado a 
cidades do Brasil todo, essas posiÃ§Ãµes sÃ£o de 1335 de 5570 e 4284 de 
5570, respectivamente. | Apresenta 
21,4% de domicÃ­lios com esgotamento sanitÃ¡rio adequado, 39,1% de 
domicÃ­lios urbanos em vias pÃºblicas com arborizaÃ§Ã£o e 11% de 
domicÃ­lios urbanos em vias pÃºblicas com urbanizaÃ§Ã£o adequada 
(presenÃ§a de bueiro, calÃ§ada, pavimentaÃ§Ã£o e meio-fio). Quando 
comparado com os outros municÃ­pios do estado, fica na posiÃ§Ã£o 7 de 
22, 5 de 22 e 2 de 22, respectivamente. JÃ¡ quando comparado a outras 
cidades do Brasil, sua posiÃ§Ã£o Ã© 3558 de 5570, 4548 de 5570 e 2685 de
 5570, respectivamente. | Em 2022, a 
Ã¡rea do municÃ­pio era de 1.652,674 kmÂ², o que o coloca na posiÃ§Ã£o 
22 de 22 entre os municÃ­pios do estado e 893 de 5570 entre todos os 
municÃ­pios. | False | False | False | True | 120025 | 105 | -1 | 2245 | 40 | nan | D | epitaciolandia |
| Rio Branco | AC | 1200401.jpg | 364756 | 41,28 | 3,3 | 106966 | 25,5 | 36,4 | 95,1 | 5,7 | 4,8 | 56946 | 17052 | 2209 | 903 | 189 | 65 | 26119,02 | 64,8 | 0,727 | 884827,27 | 740733,11 | 14,97 | 0,2 | 95 | 87,42 | 56,7 | 13,8 | 20,4 | 33767.000000 | AmazÃ´nia | NÃ£o pertence | 8835,154 | Rio Branco | Vale do Acre | Rio Branco | 1200401 | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200401.svg | https://cidades.ibge.gov.br/municipio/1200401 | Em 2022, a 
populaÃ§Ã£o era de 364.756 habitantes e a densidade demogrÃ¡fica era de 
41,28 habitantes por quilÃ´metro quadrado. Na comparaÃ§Ã£o com outros 
municÃ­pios do estado, ficava nas posiÃ§Ãµes 1 e 1 de 22. JÃ¡ na 
comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 70 e
 3583 de 5570. | Em 2021, o 
salÃ¡rio mÃ©dio mensal era de 3,3 salÃ¡rios mÃ­nimos. A proporÃ§Ã£o de 
pessoas ocupadas em relaÃ§Ã£o Ã  populaÃ§Ã£o total era de 25,5%. Na 
comparaÃ§Ã£o com os outros municÃ­pios do estado, ocupava as posiÃ§Ãµes 1
 de 22 e 1 de 22, respectivamente. JÃ¡ na comparaÃ§Ã£o com cidades do 
paÃ­s todo, ficava na posiÃ§Ã£o 84 de 5570 e 950 de 5570, 
respectivamente. Considerando domicÃ­lios com rendimentos mensais de 
atÃ© meio salÃ¡rio mÃ­nimo por pessoa, tinha 36,4% da populaÃ§Ã£o nessas
 condiÃ§Ãµes, o que o colocava na posiÃ§Ã£o 22 de 22 dentre as cidades 
do estado e na posiÃ§Ã£o 3272 de 5570 dentre as cidades do Brasil. | Em 2010, a 
taxa de escolarizaÃ§Ã£o de 6 a 14 anos de idade era de 95,1%. Na 
comparaÃ§Ã£o com outros municÃ­pios do estado, ficava na posiÃ§Ã£o 2 de 
22. JÃ¡ na comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava na 
posiÃ§Ã£o 4980 de 5570. Em relaÃ§Ã£o ao IDEB, no ano de 2021, o IDEB 
para os anos iniciais do ensino fundamental na rede pÃºblica era 5,7 e 
para os anos finais, de 4,8. Na comparaÃ§Ã£o com outros municÃ­pios do 
estado, ficava nas posiÃ§Ãµes 2 e 6 de 22. JÃ¡ na comparaÃ§Ã£o com 
municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 2234 e 2559 de 5570. | Em 2021, o PIB
 per capita era de R$ 26.119,02. Na comparaÃ§Ã£o com outros municÃ­pios 
do estado, ficava nas posiÃ§Ãµes 6 de 22 entre os municÃ­pios do estado e
 na 2484 de 5570 entre todos os municÃ­pios. JÃ¡ o percentual de 
receitas externas em 2015 era de 64,8%, o que o colocava na posiÃ§Ã£o 11
 de 22 entre os municÃ­pios do estado e na 4710 de 5570. Em 2017, o 
total de receitas realizadas foi de R$ 884.827,27 (x1000) e o total de 
despesas empenhadas foi de R$ 740.733,11 (x1000). Isso deixa o 
municÃ­pio nas posiÃ§Ãµes 1 e 1 de 22 entre os municÃ­pios do estado e 
na 91 e 94 de 5570 entre todos os municÃ­pios. | A taxa de 
mortalidade infantil mÃ©dia na cidade Ã© de 14,97 para 1.000 nascidos 
vivos. As internaÃ§Ãµes devido a diarreias sÃ£o de 0,2 para cada 1.000 
habitantes. Comparado com todos os municÃ­pios do estado, fica nas 
posiÃ§Ãµes 11 de 22 e 17 de 22, respectivamente. Quando comparado a 
cidades do Brasil todo, essas posiÃ§Ãµes sÃ£o de 1668 de 5570 e 4284 de 
5570, respectivamente. | Apresenta 
56,7% de domicÃ­lios com esgotamento sanitÃ¡rio adequado, 13,8% de 
domicÃ­lios urbanos em vias pÃºblicas com arborizaÃ§Ã£o e 20,4% de 
domicÃ­lios urbanos em vias pÃºblicas com urbanizaÃ§Ã£o adequada 
(presenÃ§a de bueiro, calÃ§ada, pavimentaÃ§Ã£o e meio-fio). Quando 
comparado com os outros municÃ­pios do estado, fica na posiÃ§Ã£o 1 de 
22, 12 de 22 e 1 de 22, respectivamente. JÃ¡ quando comparado a outras 
cidades do Brasil, sua posiÃ§Ã£o Ã© 1956 de 5570, 5302 de 5570 e 1826 de
 5570, respectivamente. | Em 2022, a 
Ã¡rea do municÃ­pio era de 8.835,154 kmÂ², o que o coloca na posiÃ§Ã£o 5
 de 22 entre os municÃ­pios do estado e 150 de 5570 entre todos os 
municÃ­pios. | False | False | False | True | 120040 | 2988 | -11 | 67500 | 2557 | nan | D | rio branco |
| Xapuri | AC | 1200708.jpeg | 18243 | 3,41 | 1,8 | 1091 | 5,49 | 45,9 | 87,7 | 5,1 | 5 | 2648 | 609 | 146 | 60 | 49 | 12 | 22902,48 | nan | 0,599 | 35332,64 | 28563,76 | 18,99 | 2,2 | 9 | 3,23 | 27,7 | 14,7 | 4,5 | 484.000000 | AmazÃ´nia | NÃ£o pertence | 5350,586 | Rio Branco | Vale do Acre | BrasilÃ©ia | 1200708 | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200708.svg | https://cidades.ibge.gov.br/municipio/1200708 | Em 2022, a 
populaÃ§Ã£o era de 18.243 habitantes e a densidade demogrÃ¡fica era de 
3,41 habitantes por quilÃ´metro quadrado. Na comparaÃ§Ã£o com outros 
municÃ­pios do estado, ficava nas posiÃ§Ãµes 10 e 25 de 22. JÃ¡ na 
comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 1856
 e 10279 de 5570. | Em 2021, o 
salÃ¡rio mÃ©dio mensal era de 1,8 salÃ¡rios mÃ­nimos. A proporÃ§Ã£o de 
pessoas ocupadas em relaÃ§Ã£o Ã  populaÃ§Ã£o total era de 5,49%. Na 
comparaÃ§Ã£o com os outros municÃ­pios do estado, ocupava as posiÃ§Ãµes 
13 de 22 e 15 de 22, respectivamente. JÃ¡ na comparaÃ§Ã£o com cidades do
 paÃ­s todo, ficava na posiÃ§Ã£o 3288 de 5570 e 5243 de 5570, 
respectivamente. Considerando domicÃ­lios com rendimentos mensais de 
atÃ© meio salÃ¡rio mÃ­nimo por pessoa, tinha 45,9% da populaÃ§Ã£o nessas
 condiÃ§Ãµes, o que o colocava na posiÃ§Ã£o 13 de 22 dentre as cidades 
do estado e na posiÃ§Ã£o 2047 de 5570 dentre as cidades do Brasil. | Em 2010, a 
taxa de escolarizaÃ§Ã£o de 6 a 14 anos de idade era de 87,7%. Na 
comparaÃ§Ã£o com outros municÃ­pios do estado, ficava na posiÃ§Ã£o 15 de
 22. JÃ¡ na comparaÃ§Ã£o com municÃ­pios de todo o paÃ­s, ficava na 
posiÃ§Ã£o 5499 de 5570. Em relaÃ§Ã£o ao IDEB, no ano de 2021, o IDEB 
para os anos iniciais do ensino fundamental na rede pÃºblica era 5,1 e 
para os anos finais, de 5. Na comparaÃ§Ã£o com outros municÃ­pios do 
estado, ficava nas posiÃ§Ãµes 8 e 3 de 22. JÃ¡ na comparaÃ§Ã£o com 
municÃ­pios de todo o paÃ­s, ficava nas posiÃ§Ãµes 3487 e 1937 de 5570. | nan | A taxa de 
mortalidade infantil mÃ©dia na cidade Ã© de 18,99 para 1.000 nascidos 
vivos. As internaÃ§Ãµes devido a diarreias sÃ£o de 2,2 para cada 1.000 
habitantes. Comparado com todos os municÃ­pios do estado, fica nas 
posiÃ§Ãµes 9 de 22 e 10 de 22, respectivamente. Quando comparado a 
cidades do Brasil todo, essas posiÃ§Ãµes sÃ£o de 1090 de 5570 e 1442 de 
5570, respectivamente. | Apresenta 
27,7% de domicÃ­lios com esgotamento sanitÃ¡rio adequado, 14,7% de 
domicÃ­lios urbanos em vias pÃºblicas com arborizaÃ§Ã£o e 4,5% de 
domicÃ­lios urbanos em vias pÃºblicas com urbanizaÃ§Ã£o adequada 
(presenÃ§a de bueiro, calÃ§ada, pavimentaÃ§Ã£o e meio-fio). Quando 
comparado com os outros municÃ­pios do estado, fica na posiÃ§Ã£o 4 de 
22, 11 de 22 e 8 de 22, respectivamente. JÃ¡ quando comparado a outras 
cidades do Brasil, sua posiÃ§Ã£o Ã© 3224 de 5570, 5285 de 5570 e 3588 de
 5570, respectivamente. | Em 2022, a 
Ã¡rea do municÃ­pio era de 5.350,586 kmÂ², o que o coloca na posiÃ§Ã£o 
12 de 22 entre os municÃ­pios do estado e 280 de 5570 entre todos os 
municÃ­pios. | False | False | False | True | 120070 | 84 | 0 | 951 | 29 | nan | D | xapuri |

### Explorando as colunas (as que achei mais importantes):

- **AREA_TERRITORIAL e AREA_URBANA:** O tamanho físico do município (em km²) e o tamanho específico de sua mancha urbana.
- **BIOMA:** O tipo de vegetação predominante (ex: "Mata Atlântica", "Pampa").
- **SISTEMA_COSTEIRO:** Indica se o município pertence à região litorânea.
- **PIB:** O Produto Interno Bruto, a soma das riquezas produzidas na cidade.
- **SALARIO_MEDIO:** A média salarial local medida em salários mínimos.
- **PERCENTUAL_MEIO_MINIMO:** Proporção da população que vive com renda per capita de até meio salário mínimo.
- **PERCENTUAL_EXTERNAS:** O percentual das receitas da prefeitura que dependem de fontes externas (governo estadual/federal).
- **TOTAL_RECEITAS e TOTAL_DESPESAS:** O volume de dinheiro que a prefeitura arrecadou e gastou.
- **_POSSUI_GD, _POSSUI_TOP100C15, _POSSUI_TOP100C30, _POSSUI_SITUACIONAL:** Colunas com os valores "True" ou "False" (Verdadeiro ou Falso) que o sistema usa para saber em quais avaliações de turismo o município possui resultados disponíveis.
- **CERTIFICADO:** O nome do arquivo (ex: "GD_Award_Certificate.pdf") correspondente ao prêmio que a cidade recebeu.
- **CATEGORIA:** Uma classificação por letras (A, B, C) que categoriza o nível ou grupo do destino.

## 11 - DESTINATIONS_2023.csv

Esta base funciona como um **boletim de avaliação detalhado dos destinos turísticos brasileiros** para o ano de 2023, consolidando o nível de conformidade das cidades em relação a um conjunto de critérios de sustentabilidade e gestão. Para cada exigência, a tabela registra se o município cumpriu ou não o requisito.

| CIDADE | ESTADO | PAIS | ANO | CRITERIO | AVALIACAO | ORDEM | THEME | TOPIC | CRITERIA | TOPIC_PT | TOPIC_US | THEME_PT | THEME_US | CHAVE | CODIGO_MUNICIPIO | CRITERIO_US | CRITERIO_PT | THEME_ES | TOPIC_ES | CRITERIO_ES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bombinhas | SC | BRASIL | 2023 | 1.100000 | 2.000000 | 1,01 | 1 | 1.100000 | 1.1.01 | Compromisso e organizaÃ§Ã£o | Commitment & Organisation | Gerenciamento de destinos | Destination Management | BOMBINHAS-SC | 4202453 | Sustainable destination coordinator | Coordenador de destinos sustentÃ¡veis | GestiÃ³n del destino | Compromiso y organizaciÃ³n | Coordinador de sostenibilidad |
| Bombinhas | SC | BRASIL | 2023 | 1.200000 | 2.000000 | 1,02 | 1 | 1.100000 | 1.1.02 | Compromisso e organizaÃ§Ã£o | Commitment & Organisation | Gerenciamento de destinos | Destination Management | BOMBINHAS-SC | 4202453 | Management structure | Estrutura de gestÃ£o | GestiÃ³n del destino | Compromiso y organizaciÃ³n | Estructura de gestiÃ³n |
| Bombinhas | SC | BRASIL | 2023 | 1.300000 | 2.000000 | 1,03 | 1 | 1.100000 | 1.1.03 | Compromisso e organizaÃ§Ã£o | Commitment & Organisation | Gerenciamento de destinos | Destination Management | BOMBINHAS-SC | 4202453 | Trained coordinator/ team | Coordenador/equipe treinada | GestiÃ³n del destino | Compromiso y organizaciÃ³n | Coordinador/equipo capacitado |
| Bombinhas | SC | BRASIL | 2023 | 1.400000 | 2.000000 | 1,04 | 1 | 1.100000 | 1.1.04 | Compromisso e organizaÃ§Ã£o | Commitment & Organisation | Gerenciamento de destinos | Destination Management | BOMBINHAS-SC | 4202453 | Stakeholder involvement | Envolvimento das partes interessadas | GestiÃ³n del destino | Compromiso y organizaciÃ³n | ParticipaciÃ³n de las partes interesadas (antes de la participaciÃ³n del sector turÃ­stico) |
| Bombinhas | SC | BRASIL | 2023 | 1.500000 | 2.000000 | 1,05 | 1 | 1.200000 | 1.2.05 | Planejamento e desenvolvimento | Planning & Development | Gerenciamento de destinos | Destination Management | BOMBINHAS-SC | 4202453 | Inventory of destination assets | InventÃ¡rio de ativos de destino | GestiÃ³n del destino | PlanificaciÃ³n y desarrollo | Inventario de activos de destino |

### Explorando as colunas:

**1. Identificação do Destino**

- **CIDADE:** O nome do município que está sendo avaliado (ex: "Bombinhas").
- **ESTADO:** A sigla da Unidade Federativa da cidade (ex: "SC", "RN").
- **PAIS:** O país onde o destino se localiza (todos marcados como "BRASIL").
- **CODIGO_MUNICIPIO:** O código numérico oficial de registro da cidade, equivalente ao código IBGE (ex: "4202453").
- **CHAVE:** Um código de texto único gerado pelo sistema para identificar o local, formado pelo nome da cidade e estado (ex: "BOMBINHAS-SC").

**2. Dados da Avaliação e Ordenação**

- **ANO:** O ano em que a avaliação de sustentabilidade foi realizada (2023).
- **AVALIACAO:** A nota ou pontuação de desempenho que a cidade alcançou naquele critério específico, geralmente representada por valores como 0, 1, 2, ou deixada em branco para não avaliado/sem dados.
- **CRITERIO:** O código numérico curto usado para identificar a regra avaliada (ex: "1.1", "1.7").
- **CRITERIA:** Um identificador numérico mais detalhado e extenso para o mesmo critério (ex: "1.1.01", "1.2.07").
- **ORDEM:** Valor numérico decimal que o sistema utiliza para ordenar e apresentar os critérios na sequência correta nos painéis (ex: 1,01).

**3. Categorização e Descrições (Português, Inglês e Espanhol)**

- **THEME:** O código numérico do grande tema ao qual o critério pertence (ex: "1" para Gerenciamento de destinos).
- **THEME_PT, THEME_US, THEME_ES:** O título desse tema principal traduzido para Português, Inglês e Espanhol (ex: "Gerenciamento de destinos", "Destination Management", "Gestión del destino").
- **TOPIC:** O código numérico da subcategoria dentro do tema principal (ex: "1.1", "1.3").
- **TOPIC_PT, TOPIC_US, TOPIC_ES:** O nome dessa subcategoria traduzido para os três idiomas (ex: "Compromisso e organização", "Commitment & Organisation", "Compromiso y organización").
- **CRITERIO_PT, CRITERIO_US, CRITERIO_ES:** O título oficial ou nome curto da ação que o destino precisou cumprir, também traduzido nos três idiomas (ex: "Coordenador de destinos sustentáveis", "Sustainable destination coordinator", "Coordinador de sostenibilidad").

## 12 - TIMELINE_FULL.csv

Esta base atua como um histórico de desempenho geral dos destinos turísticos ao longo do tempo, consolidando o resultado final das avaliações das cidades, mostrando de forma resumida quantos pontos o município fez, quantos critérios foram avaliados e sua taxa de sucesso.

| TOTAL | NUMERO_CRITERIOS | APROVEITAMENTO | EIXO | ORDEM | ANO | CODIGO_MUNICIPIO | ORIGEM | CHAVE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 126 | 84 | 0,75 | 2023.100000 | 202301 | 2023 | 4202453 | GD | 2023.1-4202453 |
| 122 | 84 | 0,72619047619047616 | 2023.100000 | 202301 | 2023 | 4208005 | GD | 2023.1-4208005 |
| 95 | 84 | 0,56547619047619047 | 2023.100000 | 202301 | 2023 | 4211702 | GD | 2023.1-4211702 |
| 99 | 84 | 0,5892857142857143 | 2023.100000 | 202301 | 2023 | 2412559 | GD | 2023.1-2412559 |
| 100 | 84 | 0,59523809523809523 | 2023.100000 | 202301 | 2023 | 2414209 | GD | 2023.1-2414209 |

### Explorando as colunas:

- **TOTAL:** Representa a pontuação absoluta total alcançada pelo município na avaliação.
- **NUMERO_CRITERIOS:** Indica a quantidade total de requisitos ou regras que foram submetidos à avaliação naquele ciclo (como 15, 30 ou 84 critérios).
- **APROVEITAMENTO:** É a taxa ou percentual de sucesso e conformidade do destino, calculada a partir do total de pontos (ex: um valor de 0,75 significa 75% de aproveitamento).
- **EIXO:** Um identificador de texto que define o período ou ciclo exato da avaliação (ex: "2023.1" ou "2023.2").
- **ORDEM:** Um valor numérico gerado a partir do eixo (ex: "202301", "202302") usado pelo sistema para classificar e ordenar cronologicamente os ciclos de auditoria.
- **ANO:** Indica o ano em que a referida avaliação do município foi realizada (ex: "2023").
- **CODIGO_MUNICIPIO:** É o código numérico oficial de identificação da cidade, correspondente ao código do IBGE (ex: "4202453").
- **ORIGEM:** Informa a qual programa ou escopo de certificação os dados pertencem, podendo ser "GD" (para os critérios completos do Green Destinations), "TOP100C15" ou "TOP100C30".
- **CHAVE:** Um código de referenciamento exclusivo gerado pelo sistema para unir o período de avaliação com a cidade avaliada (ex: "2023.1-4202453" ou "2023.2-4211306").

## 13 - QQUADRADO.csv

Esta base contém os dados de validação estatística do sistema, resultados de Testes Qui-Quadrado, uma fórmula matemática utilizada para descobrir se existe alguma relação de dependência ou não entre duas variáveis diferentes. Sendo assim, utilizado para cruzar pares de perguntas do questionário situacional (por exemplo, testando a "Q02" contra a "Q08") ou pares de critérios de certificação (como o critério "3.18" contra o "1.1"). O objetivo é provar estatisticamente se a resposta ou o desempenho do municipio em um determinado questio afeta o seu resultado em outro.

| CATEGORIA | IDENTITY_A | IDENTITY_B | CHI2 | P_VALUE | GRAU_LIBERDADE | AREA_CAUDA_SUPERIOR | COEFICIENTE_CONTIGENCIA | RESULTADO | CHAVE_STATS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Green Destinations | 3.18 | 1.1 | 0 | 1 | 0.000000 | nan | 0 | independentes | 3.18-1.1 |
| Green Destinations | 3.18 | 1.10 | 0 | 1 | 0.000000 | nan | 0 | independentes | 3.18-1.10 |
| Green Destinations | 3.18 | 1.11 | 0 | 1 | 0.000000 | nan | 0 | independentes | 3.18-1.11 |
| Green Destinations | 3.18 | 1.12 | 0 | 1 | 0.000000 | nan | 0 | independentes | 3.18-1.12 |
| Green Destinations | 3.18 | 1.13 | 0 | 1 | 0.000000 | nan | 0 | independentes | 3.18-1.13 |

### Explorando as colunas:

- **CATEGORIA:** Indica o escopo ou a origem das variáveis que estão sendo cruzadas, como **"Green Destinations"** (para critérios de certificação) ou **"Situacional"** (para perguntas da pesquisa).
- **IDENTITY_A:** O código de identificação da primeira variável ou pergunta do cruzamento (ex: "3.18" ou "Q02").
- **IDENTITY_B:** O código de identificação da segunda variável ou pergunta que está sendo comparada com a primeira (ex: "1.1" ou "Q08").
- **CHI2:** O valor numérico calculado do próprio teste Qui-Quadrado, que mede a diferença entre os resultados reais obtidos pelas cidades e o que seria matematicamente esperado.
- **P_VALUE:** O "Valor-P", uma métrica estatística fundamental que ajuda a determinar se o resultado do teste tem significância (se é válido e não obra do acaso).
- **GRAU_LIBERDADE:** O número de graus de liberdade usados no cálculo estatístico para aquele cruzamento específico (ex: 0, 5, 30 ou 31).
- **AREA_CAUDA_SUPERIOR:** O valor crítico de referência na tabela da distribuição Qui-Quadrado, usado como limite de corte para o cálculo (muitas vezes vazio em critérios diretos, mas preenchido em questões situacionais).
- **COEFICIENTE_CONTIGENCIA:** Um valor decimal que mede a força da associação entre as duas variáveis testadas.
- **RESULTADO:** A conclusão final e literal do teste estatístico. Nas fontes fornecidas, o resultado demonstra se as duas variáveis são **"independentes"** (ou seja, o resultado de uma não influencia diretamente o resultado da outra).
- **CHAVE_STATS:** Um código de texto único gerado pela junção dos dois identificadores testados (ex: "3.18-1.1" ou "Q02-Q08"), servindo para referenciar rapidamente aquele par no sistema.

## 14 - Planilha1.csv

Esta base lista diversos municipios brasileiros e os classifica de acordo com o seu perfil ou vocação turística, funcionando como um mapeamento que define o papel de cada cidadeno cenário do turismo nacional, dividindo-as em locais com oferta complementar, polos turísticos principais ou bases de apoio logístico.

| Municipio | Categoria |
| --- | --- |
| AbaetÃ© | Municipio Com Oferta TurÃ­stica Complementar |
| Abaetetuba | Municipio Com Oferta TurÃ­stica Complementar |
| AbaÃ­ra | Municipio Com Oferta TurÃ­stica Complementar |
| Abdon Batista | Municipio Com Oferta TurÃ­stica Complementar |
| Abelardo Luz | Municipio Com Oferta TurÃ­stica Complementar |

### Explorando as colunas:

- **Municipio:** Contém o nome da cidade brasileira que está sendo listada (como "Abaeté", "Curitiba", "Gramado" ou "Amparo do Serra").
- **Categoria:** Mostra a classificação oficial da atividade turística daquela cidade. Nesta coluna, os municípios recebem um dos três rótulos abaixo:
    - **Municipio Com Oferta Turística Complementar:** Para cidades que possuem atrações turísticas secundárias ou potencial em desenvolvimento.
    - **Municipio Turístico:** Para destinos já consolidados com forte atividade do setor (como Rio de Janeiro, Porto Seguro e Blumenau).
    - **Municipio De Apoio Ao Turismo:** Para cidades que servem de base estrutural ou logística para regiões turísticas maiores.

## 15 - SELO.csv

Esta base funciona como um banco de links de imagens, associando os destinos turísticos a um selo ou distintivo visual de certificação.

| HAVE | SELO |
| --- | --- |
| BOMBINHAS-SC | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/image/GD-115x115.png |
| ITÃ-SC | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/image/GD-115x115.png |
| ORLEANS-SC | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/image/GD-115x115.png |
| SÃO MIGUEL DO GOSTOSO-RN | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/image/GD-115x115.png |
| TIBAU DO SUL-RN | https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/image/GD-115x115.png |

### Explorando as colunas:

- **CHAVE:** É o identificador único de texto do destino turístico, criado pela junção do nome do município em letras maiúsculas com a sigla do seu estado (ex: "BOMBINHAS-SC", "TIBAU DO SUL-RN"). Este é o mesmo padrão de identificação usado em outros arquivos do sistema para unificar os dados de uma cidade.
- **SELO:** Contém um link direto (endereço URL) na internet que aponta para o arquivo de imagem do selo de certificação. Nos dados apresentados, todos os links direcionam para uma mesma imagem em formato PNG ("GD-115x115.png") hospedada na nuvem, que representa o distintivo visual do Green Destinations concedido ao município.

## 16 - TIMELINE_GD.csv

Esta base é uma pequena tabela de referência estrutural ou um dicionário de ordenação para o sistema, definindo uma hierarquia e a ordem lógica das etapas do processo de certificação de sustentabilidade.

| ETAPA | ORDEM |
| --- | --- |
| 15 CritÃ©rios | 1 |
| 30 CritÃ©rios | 2 |
| Green Destinations | 3 |

### Explorando as colunas:

- **ETAPA:** Contém o nome oficial da fase de certificação ou o nível da avaliação realizada. As três etapas mapeadas no sistema são a avaliação inicial dos "15 Critérios", o corte intermediário dos "30 Critérios" e a auditoria final e completa do "Green Destinations".
- **ORDEM:** Um valor numérico sequencial (1, 2 e 3) correspondente a cada fase. O sistema utiliza esse número exclusivamente para classificar, organizar e desenhar os gráficos na ordem cronológica ou de complexidade correta.

## 17 - CORRELACAO.csv

Esta base funciona como um mapa de conexões estatísticas entre os diferentes critérios da certificação Green Destinations, não apenas listando os dados, mas mostrando como o sucesso de um indicador (como "Gestão de Resíduos") pode estar ligado ao desempenho em outro (como "Satisfação do Visitante").

| CATEGORIA | IDENTITY_A | IDENTITY_B | COEFFICIENT | P_VALUE | RESULTADO | THEME_A | THEME_B | CRITERIO_A | CRITERIO_B | CHAVE_STATS | AREA | COR | ORDEM_RESULTADO | QUI2_RESULTADO | GRUPO_RESULTADO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Green Destinations | 1.1 | 1.10 | nan | nan | NÃ£o Ã© possivel calcular a correlaÃ§Ã£o | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi 
designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | As caracterÃ­sticas, o volume, as atividades e as preferÃªncias dos visitantes sÃ£o monitorados e relatados publicamente. | 1.1-1.10 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.11 | nan | nan | NÃ£o Ã© possivel calcular a correlaÃ§Ã£o | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi 
designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | A satisfaÃ§Ã£o 
dos visitantes com a qualidade e a sustentabilidade da experiÃªncia do 
destino estÃ¡ sendo monitorada e divulgada publicamente. Se necessÃ¡rio,
 sÃ£o tomadas medidas em resposta. | 1.1-1.11 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.12 | nan | nan | NÃ£o Ã© possivel calcular a correlaÃ§Ã£o | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi 
designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | O destino tem um
 sistema de gerenciamento de visitantes que Ã© revisado regularmente. 
SÃ£o tomadas medidas para gerenciar o volume e as atividades dos 
visitantes e para reduzi-los ou aumentÃ¡-los, conforme necessÃ¡rio, em 
determinados momentos e locais, levando em conta e equilibrando as 
necessidades da economia, da comunidade, das culturas e da cultura 
locais. ambiente. | 1.1-1.12 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.13 | nan | nan | NÃ£o Ã© possivel calcular a correlaÃ§Ã£o | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi 
designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | O gerenciamento 
adequado dos visitantes e dos fluxos de visitantes Ã© aplicado para 
otimizar os impactos do turismo dentro e ao redor dos ativos naturais e 
socioculturais do destino. O sistema de gerenciamento refere-se Ã s 
caracterÃ­sticas, Ã  capacidade e Ã  sensibilidade destes ativos. | 1.1-1.13 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.14 | nan | nan | NÃ£o Ã© possivel calcular a correlaÃ§Ã£o | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi 
designada com a responsabilidade e a autoridade para a implementaÃ§Ã£o 
adequada e a comunicaÃ§Ã£o do gerenciamento de destinos sustentÃ¡veis. | Diretrizes para o
 comportamento adequado dos visitantes em eventos culturais e em locais 
sensÃ­veis do ponto de vista cultural e natural sÃ£o desenvolvidas e 
disponibilizadas aos visitantes, guias turÃ­sticos e outros 
profissionais. | 1.1-1.14 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |

### Explorando as colunas:

- **CATEGORIA:** Indica o selo ou padrão ao qual os critérios pertencem (ex: "Green Destinations").
- **IDENTITY_A:** O código numérico identificador do primeiro critério sendo comparado (ex: 1.1).
- **IDENTITY_B:** O código numérico identificador do segundo critério na comparação (ex: 1.10).
- **COEFFICIENT:** O valor numérico da correlação. Indica a força da relação entre os dois critérios.
- **P_VALUE**: Valor de significância estatística. Ajuda a saber se a relação encontrada é real ou fruto do acaso.
- **RESULTADO**: Tradução textual da estatística para humanos (ex: "Correlação Positiva Fraca" ou "Não é possível calcular").
- **THEME_A**: O grande tema ou pilar ao qual o primeiro critério pertence (ex: "Gerenciamento de destinos").
- **THEME_B**: O tema do segundo critério na comparação.
- **CRITERIO_A**: A descrição detalhada e escrita do que se trata o primeiro critério.
- **CRITERIO_B**: A descrição detalhada e escrita do segundo critério.
- **CHAVE_STATS**: Uma chave única combinando os dois IDs (A-B), usada para buscas rápidas e organização no banco de dados.
- AREA**:** Define a área de impacto daquela relação (ex: Meio Ambiente, Cultura).
- **COR:** Código hexadecimal da cor (ex: #FFFFFF). Provavelmente usado para gerar gráficos de calor (heatmaps) no seu dashboard.
- **ORDEM_RESULTADO:** Um número usado para ordenar os resultados por importância ou força da correlação.
- **QUI2_RESULTADO:** Indica o status do teste de Qui-Quadrado (independência entre variáveis).
- **GRUPO_RESULTADO:** Agrupamento final do achado estatístico (ex: "Outros Resultados" ou "Resultados Relevantes").

## 18 - LANGUAGE.csv

Esta base funciona como uma pequena tabela de referência ou dicionário de configuração para o sistema, definindo quais são os idiomas oficiais suportados pela plataforma de dados.

| LAN | UA | E |
| --- | --- | --- |
| PT-BR | nan | nan |
| US-EN | nan | nan |
| ES-SA | nan | nan |

### Explorando as colunas:

**LANGUAGE:** Contém a sigla ou o código padrão que identifica o idioma e a sua respectiva região. Os três valores presentes na lista indicam o suporte para o **Português do Brasil** ("PT-BR"), **Inglês dos Estados Unidos** ("US-EN") e **Espanhol da América do Sul** ("ES-SA").

## 19 - PIVOT_TOP100C15.csv

Esta base funciona como um dicionário de tradução e estruturação de interface para os painéis de avaliação do programa Top 100, possuindo a configuração de como os cabeçalhos e rótulos das tabelas devem ser exibidos no sistema.

| ORDEM | TITULO | LANGUAGE | GRUPO |
| --- | --- | --- | --- |
| 1 | CritÃ©rio | PT-BR | 1 |
| 2 | 2021 | PT-BR | 2 |
| 3 | 2022 | PT-BR | 3 |
| 4 | 2023 | PT-BR | 4 |
| 8 | Criteria | US-EN | 1 |

### Explorando as colunas:

- **ORDEM:** Um valor numérico sequencial (1, 2, 3, 4, etc.) que o sistema utiliza para organizar e exibir os rótulos na ordem correta na tela.
- **TITULO:** O texto literal do cabeçalho que aparecerá para o usuário, como a palavra **"Critério"** (ou **"Criteria"** em inglês) e os anos das avaliações, como **"2021"**, **"2022"** e **"2023"**.
- **LANGUAGE:** O código oficial que identifica o idioma no qual o texto da coluna anterior está escrito, utilizando padrões como **"PT-BR"** para Português do Brasil e **"US-EN"** para Inglês dos Estados Unidos.
- **GRUPO:** Um identificador numérico (1, 2, 3 ou 4) usado para vincular o mesmo conceito em diferentes idiomas. Por exemplo, o grupo 1 representa a coluna de identificação dos critérios independentemente da língua, enquanto o grupo 2 sempre representará a coluna referente ao ano de 2021.

## 20 - PIVOT_GD.csv

Esta base fnciona como um **dicionário de tradução e estruturação de interfae** para os painéis de avaliação da certificação completa do programa Green Destinations.

| ORDEM | TITULO | LANGUAGE | GRUPO | COLUNA |
| --- | --- | --- | --- | --- |
| 0 | TÃ³pico | PT-BR | 1 | TÃ³pico |
| 1 | % Performace | PT-BR | 2 | % Performace |
| 2 | # CritÃ©rios | PT-BR | 3 | # CritÃ©rios |
| 3 | Conformidade total | PT-BR | 4 | Total |
| 4 | Conformidade parcial | PT-BR | 5 | Parcial |

### Explorando as colunas:

- **ORDEM:** Um valor numérico sequencial (de 0 a 20, nos dados apresentados) que o sistema utiliza para organizar e exibir as colunas na sequência correta nos painéis visuais.
- **TITULO:** O texto literal e completo do cabeçalho que aparecerá para o usuário na tela, como **"Conformidade total"**, **"Full compliance"** ou **"No evaluado"**.
- **LANGUAGE:** O código oficial que identifica o idioma no qual o título está escrito, sendo **"PT-BR"** (Português do Brasil), **"US-EN"** (Inglês dos EUA) ou **"ES-SA"** (Espanhol da América do Sul).
- **GRUPO:** Um número identificador (de 1 a 7) que serve para unificar o mesmo conceito em idiomas diferentes. Por exemplo, o grupo 4 sempre representará a coluna de conformidade total, não importando se a interface está em português, inglês ou espanhol.
- **COLUNA:** Um nome curto ou palavra-chave interna (como **"Total"**, **"Parcial"** ou **"Não conforme"**) que o sistema provavelmente utiliza para vincular aquele rótulo traduzido à coluna de dados reais no banco de dados.

## 21 - PIVOT_TOP100C30.csv

Esta base atua como um dicionário de tradução e estruturação de interface, mas diferente do PIVOT_TOPC15 e PIVOT_GD ele é voltado especificamente para os painéis de avaliação do programa Top 100 referentes ao corte de 30 critérios.

| ORDEM | TITULO | LANGUAGE | GRUPO |
| --- | --- | --- | --- |
| 1 | Nome | PT-BR | 1 |
| 2 | 2021 | PT-BR | 2 |
| 3 | 2022 | PT-BR | 3 |
| 4 | 2023 | PT-BR | 4 |
| 8 | Name | US-EN | 1 |

### Explorando as colunas:

- **ORDEM:** Um valor numérico sequencial (como 1, 2, 8, 9) que o sistema utiliza para organizar e definir a posição exata em que esses rótulos serão exibidos na tela.
- **TITULO:** O texto literal do cabeçalho que aparecerá para o usuário na interface, como a palavra **"Nome"** (ou **"Name"** em inglês) e os respectivos anos das avaliações, como **"2021"**, **"2022"** e **"2023"**.
- **LANGUAGE:** O código que identifica o idioma no qual o título está escrito, utilizando o padrão **"PT-BR"** para designar o Português do Brasil e **"US-EN"** para o Inglês dos Estados Unidos.
- **GRUPO:** Um identificador numérico (como 1, 2, 3 ou 4) usado para vincular o mesmo conceito ou coluna de dados em diferentes idiomas. Por exemplo, o grupo 1 sempre representará a coluna com o nome do município (seja "Nome" ou "Name"), enquanto os grupos 2, 3 e 4 representam, respectivamente, os anos de avaliação independentemente do idioma selecionado pelo usuário.

## 22 - CRITERIOS_SITUACIONAL.csv

Esta base funciona como o **dicionário de dados e mapa estrutural do questionário da pesquisa situacional** aplicada aos municípios.

| QUESTAO | GRUPO | CODIGO_ORIGINAL | TEXTO | ESCALA | GRUPO_ID | ORDEM_2 |
| --- | --- | --- | --- | --- | --- | --- |
| Q01 | Perfil do Entrevistado | 0.800000 | Nos Ãºltimos 5 anos como vocÃª avalia o turismo do municÃ­pio? | NUMERICA | 0 | 1 |
| Q02 | Perfil do Entrevistado | 0.900000 | Na sua percepÃ§Ã£o nos prÃ³ximos 5 anos como vocÃª avalia o turismo do municÃ­pio? | NUMERICA | 0 | 2 |
| Q03 | Gerenciamento de destinos | 1.100000 | Conhece as propostas para desenvolvimento turÃ­stico do municÃ­pio? | CATEGORICA | 1 | 3 |
| Q04 | Gerenciamento de destinos | 1.200000 | A estrutura organizacional  (Secretaria/Pasta de Turismo) atende as necessidades do municÃ­pio? | NUMERICA | 1 | 4 |
| Q05 | Gerenciamento de destinos | 1.300000 | O desenvolvimento do turismo no municÃ­pio Ã© planejado? | NUMERICA | 1 | 5 |

### Explorando as colunas:

- **QUESTAO:** É o código de identificação curto e único de cada pergunta no sistema, variando de "Q01" até "Q43".
- **GRUPO:** O nome do eixo temático ou categoria principal à qual a pergunta está vinculada, como "Gerenciamento de destinos", "Natureza e cenário" ou "Expectativa".
- **CODIGO_ORIGINAL:** Um identificador numérico secundário (como "1.1", "3.4" ou "7.7"), que provavelmente faz referência à numeração original da pergunta em alguma metodologia ou versão anterior do questionário.
- **TEXTO:** O enunciado literal e completo da pergunta exata que foi feita na pesquisa (ex: *"Como você avalia a gestão de resíduos sólidos no município?"* ou *"Qual tipo de turista você gostaria que tivesse na cidade?"*).
- **ESCALA:** Define o tipo ou formato de resposta aceita para aquela pergunta, classificando-a como **"NUMERICA"** (notas), **"CATEGORICA"** (múltipla escolha, como sim/não) ou **"ABERTA"** (texto livre escrito pelo usuário).
- **GRUPO_ID:** O código numérico que o sistema utiliza para identificar o eixo temático descrito na coluna "GRUPO" (ex: 1 para "Gerenciamento de destinos", 7 para "Expectativa").
- **ORDEM_2:** Um número sequencial (de 1 a 43) utilizado pelo sistema para garantir que as perguntas sejam ordenadas e exibidas na sequência cronológica e lógica correta nas telas e relatórios.

## 23 - TIMELINE_FULL_DETAIL.csv

Esta base contém os dados de histórico extremamente detalhado sobre o desempenho de cada município avaliado. Dessa forma, mostrando o resultado do município pergunta por pergunta, ou critério por critério. Ela consolida as notas de diferentes programas, como pesquisa situacional local (IDEL) e os diferentes níveis da certificação internacional (Top 100 e Green Destinations), trazendo também as descrições literais dessas regras traduzidas em diferentes idiomas.

| TOTAL | NUMERO_CRITERIOS | APROVEITAMENTO | EIXO | ORDEM | ORIGEM | CHAVE | CRITERIO_ | THEME_NOME | TOPIC_NOME | LANGUAGE | CRITERIO_NOME | ANO | CODIGO_MUNICIPIO | THEME | TOPIC | CRITERIO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6,7166666666666668 | 32 | 0,020989583333333332 | 2023.400000 | 202304 | IDEL | 2023.4-4205555 | Q04 | AnÃ¡lise Situacional | Gerenciamento de destinos | PT-BR | A estrutura organizacional  (Secretaria/Pasta de Turismo) atende as necessidades do municÃ­pio? | 2023 | 4205555 | 1 | 1.000000 | Q04 |
| 7,1159420289855069 | 32 | 0,022237318840579709 | 2023.400000 | 202304 | IDEL | 2023.4-2411205 | Q04 | AnÃ¡lise Situacional | Gerenciamento de destinos | PT-BR | A estrutura organizacional  (Secretaria/Pasta de Turismo) atende as necessidades do municÃ­pio? | 2023 | 2411205 | 1 | 1.000000 | Q04 |
| 6,1956521739130439 | 32 | 0,019361413043478264 | 2023.400000 | 202304 | IDEL | 2023.4-5001102 | Q04 | AnÃ¡lise Situacional | Gerenciamento de destinos | PT-BR | A estrutura organizacional  (Secretaria/Pasta de Turismo) atende as necessidades do municÃ­pio? | 2023 | 5001102 | 1 | 1.000000 | Q04 |
| 6,4516129032258061 | 32 | 0,020161290322580645 | 2023.400000 | 202304 | IDEL | 2023.4-5002159 | Q04 | AnÃ¡lise Situacional | Gerenciamento de destinos | PT-BR | A estrutura organizacional  (Secretaria/Pasta de Turismo) atende as necessidades do municÃ­pio? | 2023 | 5002159 | 1 | 1.000000 | Q04 |
| 6,53125 | 32 | 0,02041015625 | 2023.400000 | 202304 | IDEL | 2023.4-5005202 | Q04 | AnÃ¡lise Situacional | Gerenciamento de destinos | PT-BR | A estrutura organizacional  (Secretaria/Pasta de Turismo) atende as necessidades do municÃ­pio? | 2023 | 5005202 | 1 | 1.000000 | Q04 |

### Explorando as colunas:

**1. Desempenho e Notas**

- **TOTAL:** A nota ou pontuação exata que o município obteve especificamente naquele critério ou questão.
- **NUMERO_CRITERIOS:** A quantidade total de perguntas ou exigências que faziam parte daquele ciclo de avaliação (como 15, 30, 32 ou 84 critérios).
- **APROVEITAMENTO:** A taxa ou o percentual de sucesso que a nota daquela questão representou na avaliação geral do município.

**2. Controle de Ciclos e Origem**

- **EIXO:** O período ou ciclo exato no qual a avaliação ocorreu (ex: "2023.4", "2022.3", "2023.1").
- **ORDEM:** Um valor numérico usado internamente pelo sistema para classificar e ordenar os ciclos cronologicamente de forma correta nos gráficos (ex: "202304").
- **ORIGEM:** Indica o programa ou o escopo a qual a pergunta pertence. Pode ser a pesquisa "IDEL" (Análise Situacional), ou as etapas de certificação "TOP100C15", "TOP100C30" e "GD".
- **ANO:** O ano em que aquela auditoria ou pesquisa foi realizada (ex: "2023", "2022", "2020").

**3. Identificação do Destino**

- **CODIGO_MUNICIPIO:** O código numérico oficial da cidade, correspondente ao registro do IBGE.
- **CHAVE:** Um código gerado pela plataforma que une o ciclo de avaliação com o município avaliado (ex: "2023.4-4205555"), servindo como um elo para cruzar os dados.

**4. Detalhamento do Critério e Tradução**

- **CRITERIO_ e CRITERIO:** São códigos curtos que identificam unicamente qual foi a regra ou a pergunta avaliada (ex: "Q04", "1.1", "3.16"). Na estrutura, ambas as colunas costumam repetir esse identificador final.
- **THEME_NOME e THEME:** A coluna de texto exibe o grande eixo temático da sustentabilidade avaliado (ex: "Gerenciamento de destinos", "Meio ambiente e clima"), enquanto a coluna numérica informa o ID desse tema (ex: "1", "3").
- **TOPIC_NOME e TOPIC:** A coluna de texto informa a subcategoria detalhada dentro daquele tema (ex: "Compromisso e organização", "Planejamento e desenvolvimento"), enquanto a coluna numérica traz o código correspondente (ex: "1.1", "1.2").
- **LANGUAGE:** O idioma oficial no qual o texto do critério está sendo exibido, como **"PT-BR"** (Português do Brasil) ou **"US-EN"** (Inglês dos Estados Unidos).
- **CRITERIO_NOME:** O **enunciado completo e literal** da exigência feita ou da pergunta respondida. Por exemplo: *"A estrutura organizacional (Secretaria/Pasta de Turismo) atende as necessidades do município?"* ou *"O destino tem um inventário de seus ativos e atrações voltados para o turismo..."*.

## 24 - SITUACIONAL_2023_PIVOT.csv

Esta base contém as **respostas reais e detalhadas** da pesquisa situacional aplicada aos municípios, trazendo os resultados das avaliações.

| DATA | CODIGO_MUNICIPIO | CIDADE | ESTADO | QUESTAO | RESPOSTA | GRUPO_ID | ANO | NOTA | THEME | TOPIC | CRITERIO | ESCALA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2020-09-16 00:00:00,000 | 4217402 | Schroeder | SC | Q02 | 8 | 0 | 2020 | 8.000000 | 0 | 0 | Q02 | NUMERICA |
| 2020-09-16 00:00:00,000 | 4217402 | Schroeder | SC | Q19 | 8 | 3 | 2020 | 8.000000 | 3 | 3 | Q19 | NUMERICA |
| 2020-09-16 00:00:00,000 | 4217402 | Schroeder | SC | Q21 | 8 | 3 | 2020 | 8.000000 | 3 | 3 | Q21 | NUMERICA |
| 2020-09-16 00:00:00,000 | 4217402 | Schroeder | SC | Q25 | 8 | 6 | 2020 | 8.000000 | 6 | 6 | Q25 | NUMERICA |
| 2020-09-16 00:00:00,000 | 4217402 | Schroeder | SC | Q26 | 8 | 6 | 2020 | 8.000000 | 6 | 6 | Q26 | NUMERICA |

### Explorando as colunas:

- **DATA:** Registra a data e a hora exatas em que a avaliação ou a resposta foi inserida no sistema.
- **CODIGO_MUNICIPIO:** O código numérico oficial do IBGE usado para identificar a cidade.
- **CIDADE:** O nome por extenso do município que está sendo avaliado.
- **ESTADO:** A sigla da Unidade Federativa à qual a cidade pertence.
- **QUESTAO:** O código curto e único que identifica qual pergunta foi feita (ex: "Q04", "Q36", "Q43").
- **RESPOSTA:** O conteúdo exato da resposta fornecida. Pode assumir diversos formatos: uma nota numérica (ex: "8", "5"), uma categoria textual ("Não", "Parcialmente"), opiniões abertas escritas pelos participantes (ex: "Educação e saúde") ou o rótulo "Sem dados", caso a pergunta não tenha sido respondida.
- **GRUPO_ID:** Um código numérico que aponta a qual eixo temático da sustentabilidade a pergunta pertence.
- **ANO:** O ano de referência do ciclo em que a pesquisa foi aplicada (como 2020, 2021 ou 2023).
- **NOTA:** O valor ou peso estatístico exato da resposta. É preenchido com números nas questões de notas, mas fica vazio nas questões textuais ou não respondidas.
- **THEME:** Coluna estrutural de apoio que repete o código do grupo temático, exigida pelo sistema visual para relacionar dados.
- **TOPIC:** Outra coluna estrutural redundante que também espelha o número do eixo temático.
- **CRITERIO:** Duplica o identificador da questão (como "Q04" ou "Q39") para criar um elo padronizado com as outras planilhas de certificação.
- **ESCALA:** A classificação do formato da pergunta, que indica ao sistema se ela é "NUMERICA" (notas), "CATEGORICA" (múltipla escolha) ou "ABERTA" (texto livre).

## 25 - REMUNERACAO.csv

Esta base complementa a análise do mercado de trabalho, focando não no número de pessoas, mas na massa salairal gerada por cada setor.

| CODIGO | ESTADO | CIDADE | Ano | Atributo | RemuneracaoTotal |
| --- | --- | --- | --- | --- | --- |
| 310010 | MG | ABADIA DOS DOURADOS | 2023 | 06:EXTRAÃÃO DE PETRÃLEO E GÃS NATURAL | 0 |
| 310020 | MG | ABAETE | 2023 | 06:EXTRAÃÃO DE PETRÃLEO E GÃS NATURAL | 0 |
| 310030 | MG | ABRE CAMPO | 2023 | 06:EXTRAÃÃO DE PETRÃLEO E GÃS NATURAL | 0 |
| 310040 | MG | ACAIACA | 2023 | 06:EXTRAÃÃO DE PETRÃLEO E GÃS NATURAL | 0 |
| 310050 | MG | ACUCENA | 2023 | 06:EXTRAÃÃO DE PETRÃLEO E GÃS NATURAL | 0 |

### Explorando as colunas:

- **CODIGO:** Identificador numérico do município estabelecido pelo IBGE, utilizado como chave primária para integrar os dados de remuneração com outras bases do sistema.
- **ESTADO:** Sigla da Unidade Federativa correspondente ao município.
- **CIDADE:** Nome do município, geralmente registrado em letras maiúsculas para manter a padronização da base de dados.
- **Ano:** Período de apuração dos dados. Esta coluna permite ao agente identificar a evolução da renda média e o crescimento econômico do setor ao longo do tempo.
- **Atributo:** Classificação da atividade econômica (CNAE). Permite segmentar a massa salarial para isolar especificamente os ganhos vindos de setores turísticos ou industriais.
- **RemuneracaoTotal:** Representa a soma dos valores pagos em salários para o setor e ano indicados. Valores zerados apontam que não houve registro de pagamento formal de salários naquela categoria específica para a localidade.

## 26 - RAIS GERAL.csv

Esta base diz respeito ao mercado de trabalho, focando na força de trabalho ativa (as pessoas).

| CODIGO | ESTADO | CIDADE | Ano | Atributo | PEA |
| --- | --- | --- | --- | --- | --- |
| 310010 | MG | ABADIA DOS DOURADOS | 2024 | 51:TRANSPORTE AÃREO | 0 |
| 310020 | MG | ABAETE | 2024 | 51:TRANSPORTE AÃREO | 0 |
| 310030 | MG | ABRE CAMPO | 2024 | 51:TRANSPORTE AÃREO | 0 |
| 310040 | MG | ACAIACA | 2024 | 51:TRANSPORTE AÃREO | 0 |
| 310050 | MG | ACUCENA | 2024 | 51:TRANSPORTE AÃREO | 0 |
- **CODIGO:** Corresponde ao código identificador do IBGE para o município.
- **ESTADO:** Indica a sigla da Unidade Federativa onde o município está localizado.
- **CIDADE:** Apresenta o nome completo do município, geralmente padronizado em letras maiúsculas para facilitar a leitura.
- **Ano:** Indica o período ao qual o dado se refere.
- **Atributo:** Detalha o setor econômico ou a classe da CNAE.
- **PEA:** Representa o estoque de empregos formais ou a população ocupada no setor descrito. Valores zerados indicam a inexistência de atividade formal naquela categoria específica para o ano e local registrados.

##