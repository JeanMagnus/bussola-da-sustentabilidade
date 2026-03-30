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

| CRITERIO | THEMES | THEME_DESCRIPTION_US | THEME_DESCRIPTION_PT | THEME_DESCRIPTION_ES | TOPIC | TOPIC_DESCRIPTION_US | TOPIC_DESCRIPTION_PT | TOPIC_DESCRIPTION_ES | CRITERIA | CRITERIA_TYPE | CRITERIA_NAME_US | CRITERIA_NAME_PT | CRITERIA_NAME_ES | CRITERIA_DESCRIPTION_US | CRITERIA_DESCRIPTION_PT | CRITERIA_DESCRIPTION_ES | ORDEM_1 | ORDEM_2 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1.1 | 1 | Destination Management | Gerenciamento de destinos | Gestión del destino | 1.1 | Commitment & Organisation | Compromisso e organização | Compromiso y organización | 1.1.01 | C15 | Sustainable destination coordinator | Coordenador de destinos sustentáveis | Coordinador de sostenibilidad | A person has been assigned the responsibility and authority for the adequate implementation and reporting of sustainable destination management. | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | Se ha asignado a una persona la responsabilidad y la autoridad para la adecuada implementación y reporte de la gestión sostenible del destino. | 11,01 | 1,01 |
| 1.2 | 1 | Destination Management | Gerenciamento de destinos | Gestión del destino | 1.1 | Commitment & Organisation | Compromisso e organização | Compromiso y organización | 1.1.02 | nan | Management structure | Estrutura de gestão | Estructura de gestión | An adequately funded organisation or management structure is responsible for coordinating and promoting sustainable tourism development and management. | Uma organização ou estrutura de gerenciamento com financiamento adequado é responsável por coordenar e promover o desenvolvimento e o gerenciamento do turismo sustentável. | Una organización o estructura de gestión adecuadamente financiada se encarga de coordinar y promover el desarrollo y la gestión del turismo sostenible. | 11,02 | 1,02 |
| 1.3 | 1 | Destination Management | Gerenciamento de destinos | Gestión del destino | 1.1 | Commitment & Organisation | Compromisso e organização | Compromiso y organización | 1.1.03 | nan | Trained coordinator/ team | Coordenador/equipe treinada | Coordinador/equipo capacitado | The person or team responsible for destination development and management is sufficiently staffed and adequately trained on and/or experienced in sustainability issues. | A pessoa ou equipe responsável pelo desenvolvimento e gerenciamento do destino tem pessoal suficiente e é adequadamente treinada e/ou tem experiência em sustentabilidade problemas. | La persona o el equipo responsable del desarrollo y la gestión del destino cuenta con el personal suficiente y con la formación y/o la experiencia adecuadas en materia de sostenibilidad. | 11,03 | 1,03 |
| 1.4 | 1 | Destination Management | Gerenciamento de destinos | Gestión del destino | 1.1 | Commitment & Organisation | Compromisso e organização | Compromiso y organización | 1.1.04 | nan | Stakeholder involvement | Envolvimento das partes interessadas | Participación de las partes interesadas | The destination management organisation or structure involves civil society and the private and public sector in sustainable destination management. | A organização ou estrutura de gerenciamento de destinos envolve a sociedade civil e a setor público e privado no gerenciamento de destinos sustentáveis. | La organización o estructura de gestión del destino implica a la sociedad civil y a los sectores público y privado en la gestión sostenible del destino. | 11,04 | 1,04 |
| 1.5 | 1 | Destination Management | Gerenciamento de destinos | Gestión del destino | 1.2 | Planning & Development | Planejamento e desenvolvimento | Planificación y desarrollo | 1.2.05 | C15 | Inventory of destination assets | Inventário de ativos de destino | Inventario de activos de destino | The destination has an inventory of its tourism-oriented assets and attractions including natural and cultural sites. | O destino tem um inventário de seus ativos e atrações voltados para o turismo incluindo locais naturais e culturais. | El destino cuenta con un inventario de sus activos y atracciones orientadas al turismo, incluidos los lugares naturales y culturales. | 12,05 | 1,05 |

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
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sustainable destination coordinator | 1.1 | 5 | Treze Tílias | 2022 | SC | 1 | Gerenciamento de destinos | Destination Management | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | A person has been assigned the responsibility and authority for the adequate implementation and reporting of sustainable destination management. | Coordenador de destinos sustentáveis | Sustainable destination coordinator | 1,01 | TREZE TÍLIAS-SC | 4218509 | 1.1 | Se ha asignado a una persona la responsabilidad y la autoridad para la adecuada implementación y reporte de la gestión sostenible del destino. | Coordinador de sostenibilidad | Gestión del destino |
| Nature conservation | 2.1 | 5 | Treze Tílias | 2022 | SC | 2 | Natureza e cenário | Nature & Scenery | O destino tem um sistema para conservar ecossistemas, habitats e espécies. | The destination has a system to conserve ecosystems, habitats and species. | Conservação da natureza | Nature conservation | 2,01 | TREZE TÍLIAS-SC | 4218509 | 2.1 | El destino cuenta con un sistema de conservación de ecosistemas, hábitats y especies. | Conservación de la naturaleza | Naturaleza y paisaje |
| Noise | 3.1 | 5 | Treze Tílias | 2022 | SC | 3 | Meio ambiente e clima | Environment & Climate | O ruído é adequadamente regulamentado e minimizado | Noise is adequately regulated and minimised; tourism enterprises and visitors are encouraged to minimise noise. | Barulho | Noise | 3,01 | TREZE TÍLIAS-SC | 4218509 | 3.1 | El ruido está adecuadamente regulado y minimizado; se anima a las empresas turísticas y a los visitantes a minimizar el ruido. | Ruido | Medio ambiente y clima |
| Light pollution | 3.2 | 5 | Treze Tílias | 2022 | SC | 3 | Meio ambiente e clima | Environment & Climate | Os impactos da poluição luminosa na vida selvagem, na experiência dos residentes e dos visitantes são tratados adequadamente. As empresas de turismo e os visitantes são incentivados a minimizar a poluição luminosa. | Impacts of light pollution to wildlife, resident and visitor experience are adequately addressed. Tourism enterprises and visitors are encouraged to minimise light pollution. | Poluição luminosa | Light pollution | 3,02 | TREZE TÍLIAS-SC | 4218509 | 3.1 | Los impactos de la contaminación lumínica en la vida silvestre y en la experiencia de los residentes y visitantes se abordan adecuadamente. Se anima a las empresas turísticas y a los visitantes a minimizar la contaminación lumínica. | Contaminación lumínica | Medio ambiente y clima |
| Community involvement in planning | 5.7 | 5 | Treze Tílias | 2022 | SC | 5 | Bem-estar social | Social Well-Being | O destino permite e promove a participação pública no planejamento e na gestão de destinos sustentáveis. | The destination enables and promotes public participation in sustainable destination planning and management. | Envolvimento da comunidade em planejamento | Community involvement in planning | 5,07 | TREZE TÍLIAS-SC | 4218509 | 5.2 | El destino permite y promueve la participación pública en la planificación y gestión sostenible del destino. | Participación de la comunidad en la planificación | Bienestar social |

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

| DESCRICAO | CRITERIO | NOTA | CIDADE | ANO | ESTADO | THEME | THEME_PT | THEME_US | CRITERIA_NAME_PT | CRITERIA_NAME_US | CRITERIA_DESCRIPTION_PT | CRITERIA_DESCRIPTION_US | ORDEM | CHAVE | CODIGO_MUNICIPIO | TOPIC | CRITERIA_NAME_ES | CRITERIA_DESCRIPTION_ES | THEME_ES |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sustainable destination coordinator | 1.1 | 5 | Urubici | 2023 | SC | 1 | Gerenciamento de destinos | Destination Management | Coordenador de destinos sustentáveis | Sustainable destination coordinator | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | A person has been assigned the responsibility and authority for the adequate implementation and reporting of sustainable destination management. | 1,01 | URUBICI-SC | 4218905 | 1.1 | Coordinador de sostenibilidad | Se ha asignado a una persona la responsabilidad y la autoridad para la adecuada implementación y reporte de la gestión sostenible del destino. | Gestión del destino |
| Inventory of destination assets | 1.5 | 2,25 | Urubici | 2023 | SC | 1 | Gerenciamento de destinos | Destination Management | Inventário de ativos de destino | Inventory of destination assets | O destino tem um inventário de seus ativos e atrações voltados para o turismo incluindo locais naturais e culturais. | The destination has an inventory of its tourism-oriented assets and attractions including natural and cultural sites. | 1,05 | URUBICI-SC | 4218905 | 1.2 | Inventario de activos de destino | El destino cuenta con un inventario de sus activos y atracciones orientadas al turismo, incluidos los lugares naturales y culturales. | Gestión del destino |
| Destination Management Policy or Strategy | 1.7 | 2,75 | Urubici | 2023 | SC | 1 | Gerenciamento de destinos | Destination Management | Política ou estratégia de gerenciamento de destinos | Destination Management Policy or Strategy | O destino tem uma política ou estratégia de gerenciamento de destino atualizada, disponível publicamente e plurianual, que aborda questões ambientais, sociais, culturais e econômicas. | The destination has an up-to-date, publicly available, multi-year destination management policy or strategy addressing environmental, social, cultural and economic issues. | 1,07 | URUBICI-SC | 4218905 | 1.2 | Política o estrategia de gestión de destinos | El destino cuenta con una política o estrategia de gestión plurianual, actualizada y disponible públicamente, que aborda temas medioambientales, sociales, culturales y económicos. | Gestión del destino |
| Tourism impact on nature | 2.2 | 2,25 | Urubici | 2023 | SC | 2 | Natureza e cenário | Nature & Scenery | Impactos no turismo sobre a natureza | Tourism impacts on nature | O destino mede e monitora o impacto do turismo na natureza meio ambiente. Os impactos identificados do turismo na natureza são respondidos adequadamente. | The destination measures and monitors the impact of tourism on the natural environment. Identified impacts of tourism on nature are adequately responded to. | 2,02 | URUBICI-SC | 4218905 | 2.1 | Impacto del turismo en la naturaleza | El destino mide y monitorea el impacto del turismo en el entorno natural. Se responde adecuadamente a los impactos identificados del turismo en la naturaleza. | Naturaleza y paisaje |
| Landscape & Scenery | 2.5 | 2,5 | Urubici | 2023 | SC | 2 | Natureza e cenário | Nature & Scenery | Paisagem e cenário | Landscape & Scenery | As vistas cênicas naturais e rurais são protegidas. | Natural and rural scenic views are protected; landscape degradation and urban sprawl into scenic landscapes is effectively avoided. | 2,05 | URUBICI-SC | 4218905 | 2.1 | Paisaje y panorama | Se protegen las vistas escénicas naturales y rurales; se evita efectivamente la degradación del paisaje y la expansión urbana en los paisajes escénicos. | Naturaleza y paisaje |

## 5 - SITUACIONAL_2023.csv

Esta base contém os registros da percepção, opiniões e avaliações dos respondentes locais em relação ao desenvolvimento do turismo na sua cidade. 

| DATA | CODIGO_MUNICIPIO | CIDADE | ESTADO | Q01 | Q02 | Q03 | Q04 | Q05 | Q06 | Q07 | Q08 | Q09 | Q10 | Q11 | Q12 | Q13 | Q14 | Q15 | Q16 | Q17 | Q18 | Q19 | Q20 | Q21 | Q22 | Q23 | Q24 | Q25 | Q26 | Q27 | Q28 | Q29 | Q30 | Q31 | Q32 | Q33 | Q34 | Q35 | Q36 | Q37 | Q38 | Q39 | Q40 | Q41 | Q42 | Q43 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2020-08-04 | 4217402 | Schroeder | SC | 8 | 8 | Sim | 7 | 7 | 7 | nan | 8 | 9 | 8 | 7 | 10 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 4 | 9 | 8 | 7 | 7 | 9 | 9 | 8 | 9 | 8 | 7 | 8 | 8 | 8 | 7 | 7 | Parcialmente | Turista de aventura, ecológico, que cuida do município enquanto o conhece. | Morro pelado, Rio do Júlio. | Mais força para aprovação de projetos do turismo perante a prefeitura. Pessoas qualificadas para buscar recursos nessa área. (Estadual, federal, privado) | Próxima gestão do Executivo. | nan | nan | nan |
| 2020-08-17 | 4205456 | Forquilhinha | SC | 5 | 8 | Sim | 6 | 7 | 5 | 7 | 3 | 6 | 5 | 4 | 7 | 9 | 5 | nan | 8 | 5 | 10 | 6 | 8 | 8 | 8 | 6 | 9 | 7 | 8 | 9 | 9 | 7 | 6 | nan | nan | nan | nan | 7 | Parcialmente | Turista que busca a experiência cultural, gastronômica, festiva, religiosa e lazer. | Apontaria o município como um todo, o conjunto da arquitetura alemã, o paisagismo, urbanismo e a mobilidade urbana e a cultura e educação do povo. | - Identidade cultural alemã; - Incentivos na infraestrutura e serviços; - Eventos culturais e gastronômicos; - Parque São Francisco de Assis; - Paisagismo e Sustentabilidade; - Dr. Zilda Arns e Dom Paulo Evaristo Arns; | A falta de planejamento direcionado a identidade turística alemã; A interação entre as três esferas; O mal planejamento e execução dos Planos e Códigos do município. | nan | nan | nan |
| 2020-08-25 | 4217402 | Schroeder | SC | 7 | 9 | Parcialmente | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 6 | 8 | 10 | 7 | 6 | 7 | 6 | 9 | 7 | 6 | 6 | 6 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 8 | 8 | 7 | 7 | 7 | 6 | Parcialmente | nan | nan | nan | nan | nan | LINDO E SUSTENTÁVEL! | nan |
| 2020-08-26 | 4205902 | Gaspar | SC | 5 | 5 | Não | 0 | 0 | 0 | nan | 0 | 0 | 8 | 0 | 0 | 8 | nan | nan | nan | nan | 0 | 0 | nan | nan | nan | nan | nan | 0 | 0 | nan | nan | nan | nan | nan | nan | 10 | 1 | nan | Sim | nan | nan | nan | Infraestrutura. | nan | nan | nan |
| 2020-08-26 | 4205902 | Gaspar | SC | 8 | 9 | Parcialmente | 8 | 8 | 8 | 7 | 7 | 7 | 9 | 8 | 9 | 9 | 7 | 9 | 7 | 8 | 7 | 7 | 8 | 7 | 9 | 8 | 7 | 7 | 8 | 7 | 8 | 7 | 7 | 7 | 8 | 7 | 7 | 9 | Parcialmente | Todos são bem vindos | Parques aquáticos; restaurantes; engenhos etc | nan | nan | nan | Lugar ideal para conhecer. | nan |

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

Esta base funciona como um **inventário e mapeamento do nível de desenvolvimento do turismo nos municípios brasileiros**, coletando uma variedade de dados de cada cidade, abrangendo desde a organização política e econômica, até a infraestrutura hoteleira, perfil dos turistas, e detalhamentos especificos sobre aproveitamento de recursos naturais e nauticos.

| UF | Município | O Município possui Legislação relacionada ao Turismo? | Quais? | O Município participa de governanças regionais e estaduais de turismo? | Quais?_1 | Informar as principais parcerias, rede de cooperação, intercâmbios etc. | O Município participa ou é contemplado em programas ou projetos com o MTur? | Quais?_2 | Informe quais as principais atividades econômicas em seu Município | Outros, descreva | Há um Fundo Municipal de Turismo | Valor disponível | Nº da legislação vigente | O Município possui Plano Diretor Urbano que contemple o Setor de Turismo | Número da Lei | O Município possui Plano Municipal de Turismo e /ou Plano de Desenvolvimento Territorial do Turismo | Ano | O Município possui Plano de Marketing do Turismo ou outros similares? | Ano_3 | O Município possui programas, projetos e ações acerca da atividade turística? | Quais?_4 | Possui gestão adequada de Resíduos Sólidos? | Qual a receita tributária das atividades turísticas no município? | O municipio possui Inventário Turístico? | Ano da Utilização | Nº de hospedagem | Nº de Leitos | Outros, descreva_5 | Quais os meios de hospedagem mais utilizado pelo turista? | Outros, descreva_6 | Quantos meios de hospedagem possuem cadastro no sistema CADASTUR? | Qual o período de maior fluxo turístico? | Qual o meio de comunicação utilizado para divulgação do destino? | Outros, descreva: | Qual a média do número de empregos gerados no setor de hospedagem? | O Município possui cursos, programas e/ou ações de qualificação profissional para o turismo? | Quais?_7 | Já houve manifestação de interesse de investidores em empreender no setor de turismo no município? | Quais?_8 | Possui guias e/ou condutores de turismo? | Quantos | O Município possui locadoras de imóveis, automóveis, embarcações e aeronaves para temporadas? | Quais?_9 | Quantas agências bancárias o município possui? | Quantas casas de câmbio o município possui? | Quantos templos de manifestação de fé, igrejas o município possui? | O município possui abastecimento de água, serviços de esgoto, serviços de energia, serviços de coleta de lixo? | Quais?_10 | O município possui aeroporto? | Quais?_11 | Quais os tipos de sistema de Transporte? | Qual a principal forma de acesso ao(s) destino(s) turístico(s)? | Qual a situação do acesso aos Atrativos Turísticos do município? | Qual a situação atual da Sinalização Turística do município? | O Município faz parte de alguma rota turística? | Quais?_12 | Existe linha regular de transporte turístico que interligue os principais atrativos? | Descreva as rotas turísticas | Qual a qualidade da rede de telefonia celular do município? | Qual a qualidade do fornecimento de internet no município? | Quantos prontos socorros públicos existem? | Quantos prontos socorros privados existem? | Quais sistema de segurança e equipamentos que proporcionam à população e ao turista as garantias básicas do cidadão? | Outros, descreva_13 | Há delegacia de proteção ao turista? | Existem locais de embarque e desembarque sinalizados e com acesso em nível? | Existem espaços reservados para pessoa com deficiência ou mobilidade reduzida? | O município dispõe de profissionais capacitados para o atendimento de pessoas com deficiência? | O município possui acesso ao crédito do Fundo Geral de Turismo - FUNGETUR? | Qual? | Qual o número total de empresas formais do setor do turismo existentes no município? | Qual a média do número de empregos gerados no Setor de Turismo? | Há uma política de atração de investimentos privados para o setor? | Quem é o responsável? | Valor da arrecadação há dois anos (R$) | Alíquota média do ISS há dois anos (%) | Valor da arrecadação no ano anterior (R$) | Alíquota média do ISS no ano anterior (%) | Quais tipos de Patrimônio Natural? | Há unidades de conservação (federal, estadual e/ou municipal)? | Quais estão fechadas para uso público? | Quais tipos de Patrimônio Cultural? | Negócios e eventos | Sol e Praia | Turismo Cultural | Ecoturismo | Turismo de Aventura | Outros, descreva_14 | Negócios e eventos_15 | Sol e Praia_16 | Turismo Cultural_17 | Ecoturismo_18 | Turismo de Aventura_19 | Outros, descreva_20 | O Município possui | O Município possui águas termais? | O Município possui estudo sobre a profundidade desses rios, lagos ou lagoa? | No Município esses rios, lagos ou lagoas são navegáveis? | Cite o nome desse rio em potencial | O Município possui pontes sobre o(s) rio(s)? | Cite o nome da ponte, sua altura até o nível da água do rio? | O Município possuí marinas/garagens náuticas, guarda para barcos? | Informe a quantidade, quais são e sua localização? | Essas estruturas possuem Alvará? | Possui Licença Ambiental vigente? | O Município possui empresas de comercialização de produtos ou serviços náuticos? | O Município possui barcos para passeios turísticos? | Quantos? | O Município tem Lei que regulamenta a atividade náutica? | Qual?_21 | O Município tem algum projeto náutico? | O Município possui Turismo de Pesca? | Qual?_22 | O Município possui alguma atividade turística de mergulho? | Qual?_23 | O Município possui alguma atividade turística de vela? | Qual?_24 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RN | Almino Afonso | Sim | Lei nº 386/2011 e Lei nº 591/2025 | Sim | IGR Oeste Potiguar | Sebrae/RN | Não | nan | Agricultura e Pecuária, Comércio | nan | Sim | 0 | Lei nº 591/2025 | Não | nan | Não | nan | Não | nan | Não | nan | Não | R$ 50.000,00 | Não | nan | 2 | 23 | nan | Pousada, Casa de amigos/parentes | nan | 0 | Fevereiro/Março, Novembro E Dezembro. | Rede sociais, Internet | nan | 30 | Não | nan | Não | nan | Não | nan | Não | nan | 2 | 0 | 16 | Sim | Abastecimento de água, serviços de esgoto parcial, serviços de energia e coleta de lixo. | Não | nan | Rodoviário coletivo, táxi, locação | Rodovia | Regular | Não tem sinalização | Não | nan | Não | nan | Regular | Regular | 4 | 0 | Postos de saúde, Delegacias, Hospitais, Defesa civil | nan | Não | Não | Não | Sim | Não | nan | 10 | 30 | Não | nan | 314460.14 | 5 | 228206 | 5 | nan | Não | nan | Outros | 2 | 6 | 4 | 6 | 5 | nan | nan | nan | nan | nan | nan | nan | Rios | Não | Não | Não | nan | Sim | Sem informação | Não | nan | Não | Não | Não | Não | nan | Não | nan | Não | Não | nan | Não | nan | Não | nan |
| RN | Alto do Rodrigues | Sim | Lei Municipal do Conselho | Sim | IGR Sertão para o Mar | Formalização da IGR | Não | nan | Serviços, Agricultura e Pecuária, Comércio | nan | Não | nan | nan | Não | nan | Não | nan | Não | nan | Sim | Ações de mídia, parcerias eventos | Não | 100 mil | Sim | 2025 | 11 | 326 | nan | Hotel, Casa de amigos, Pousada | nan | 04 | Março-Abril, Julho, Outubro | Rádio, TV, Redes sociais, Internet | nan | 50 | Não | nan | Sim | Alto folia | Não | nan | Sim | Imóveis, automóveis | 3 | 0 | 29 | Sim | Energia, água, lixo, esgoto | Não | nan | Rodoviário coletivo, táxi, locação | Rodovia | Boa | Não tem sinalização | Sim | Do sertão para o mar | Não | nan | Ótima | Ótima | 1 | 0 | Delegacias, Postos de saúde, Hospitais, Rodoviária | nan | Não | Não | Não | Não | Não | nan | 30 | 40 | Não | nan | 13522520.6 | 5 | 8827834.55 | 5 | nan | Não | nan | Histórico / Equipamentos | 1 | 6 | 3 | 6 | 6 | nan | nan | nan | nan | nan | nan | nan | Rios | Não | Não | Sim | Rio Piranhas-açu | Sim | Ponte do rio do Alto | Não | nan | Não | Não | Não | Não | nan | Não | nan | Não | Não | nan | Não | nan | Não | nan |
| RN | Angicos | Sim | Lei nº 1.183/2021 e Lei nº 1.182/2021 | Sim | IGR CABUGI CENTRAL | Municípios IGR, UFERSA, BNB, CDL | Sim | Regionalização | Comércio, Turismo, Agricultura, Serviços | nan | Sim | 30000 | Lei nº 1182/2021 | Não | nan | Não | nan | Sim | 2024 | Não | nan | Não | 1.500.000,00 | Não | nan | 4 | 200 | nan | Pousada, Casa de amigos | Pousada | 1 | Fev, Mar, Jul, Out | Jornais, Rádio, TV, Redes sociais, Internet | nan | 800 | Não | nan | Não | nan | Sim | 1 | Não | nan | 4 | 0 | 30 | Sim | CAERN | Não | nan | Rodoviário coletivo, táxi, locação | Rodovia | Boa | Boa | Sim | CABUGI CENTRAL | Não | nan | Ótima | Ótima | 1 | 0 | Hospitais, Defesa civil, Postos de saúde, Delegacias | Cia PM | Não | Sim | Sim | Sim | Não | nan | 10 | 100 | Não | nan | 1500000 | 2 | 2000000 | 5 | Reservas, Unidade de Cons., Parques | Sim | Parque Pico do Cabugi | Outros | 1 | 6 | 1 | 1 | 1 | nan | nan | nan | nan | nan | nan | nan | Rios, Lagoas | Não | Não | Sim | LAGOA AZUL | Não | nan | Não | nan | Não | Não | Sim | Não | nan | Não | nan | Não | Não | nan | Não | nan | Não | nan |
| RN | Apodi | Sim | Fundo, Criação de Secretaria, Conselho e Semana Turismo | Sim | IGR Oeste Potiguar | CONETUR, IGR OESTE, ALIANÇA | Não | nan | Comércio, Serviços, Agricultura, Turismo | nan | Sim | 0 | 1970/2023 | Sim | Lei nº 479/2006 | Sim | 2023 | Não | nan | Sim | Projeto Inventário em andamento | Não | 0 | Não | nan | 5 | 120 | nan | Hotel, Casa de amigos, Pousada | nan | 4 | Fevereiro | Indicação, Redes sociais, Internet, Rádio, TV | nan | 100 | Sim | Hotelaria, Garçom, Condutor local | Sim | MIRANTES | Sim | 16 | Não | nan | 6 | 0 | 27 | Sim | Cosern | Não | nan | Rodoviário coletivo, táxi, locação | Rodovia | Boa | Precária | Sim | Rota das cavernas | Não | nan | Boa | Ótima | 3 | 0 | Bombeiros, Postos de saúde, Delegacias, Hospitais | nan | Não | Não | Sim | Não | Não | nan | 7 | 100 | Não | nan | 190000 | 5 | 180000 | 5 | Unidade de Conservação | Sim | Casarões, museus | Histórico / Equipamentos | 2 | 6 | 1 | 4 | 5 | nan | nan | nan | nan | nan | nan | nan | Lagoas, Rios | Não | Não | Sim | Lagoa do Apodi | Sim | Ponte da Marinha | Não | nan | Não | Não | Não | Não | nan | Não | nan | Não | Não | nan | Não | nan | Não | nan |
| RN | Carnaúba dos Dantas | Sim | Lei nº 979/2018 e Lei nº 1131/2021 | Sim | GEOPARQUE SERIDÓ, IGRS | Governo do Estado | Não | nan | Comércio, Serviços, Turismo, Agricultura, Indústria | nan | Sim | 0 | Lei nº 979/2018 | Não | nan | Não | nan | Sim | 2026 | Sim | Turismo pedagógico, trilhas, arqueologia | Não | Não informado | Sim | 2023 | 1 | 8 | nan | Casa de amigos, Camping, Pousada | nan | 0 | Out-Dez | Internet, Rádio, TV, Redes sociais, Indicação | Panfletos; outdoor | 3 | Sim | Oficinas Sebrae, Condutor local, Hospitalidade | Sim | Pousadas, restaurantes | Sim | 14 | Não | nan | 0 | 0 | 17 | Sim | Abastecimento, Esgoto, Energia, Coleta lixo | Não | nan | Rodoviário coletivo, táxi, locação | Outros, Rodovia | Boa | Boa | Sim | Geoparque Seridó, Religiosa e Arqueológica | Não | nan | Ótima | Ótima | 6 | 0 | Delegacias, Postos de saúde | nan | Não | Sim | Sim | Sim | Não | nan | 0 | 3 | Não | nan | 871401.62 | 5 | 386905.62 | 5 | Parques, Reservas, Outros | Não | nan | Equipamentos / Histórico | 1 | 6 | 1 | 1 | 2 | nan | nan | nan | nan | nan | nan | nan | Rios | Não | Não | Não | nan | Não | nan | Não | nan | Não | Não | Não | Não | nan | Não | nan | Não | Não | nan | Não | nan | Não | nan |

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
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Assis Brasil | AC | 1200054.jpg | 8100 | 1,63 | 2,3 | 545 | 7,13 | 47,1 | 85,1 | 4,6 | nan | 2536 | 394 | 92 | 18 | 67 | 2 | 17507,67 | nan | 0,588 | 18177,08 | 17004,91 | 13,95 | 2,3 | 5 | 2,04 | 23,1 | 26,5 | 0 | nan | Amazônia | Não pertence | 4979,073 | Rio Branco | Vale do Acre | Brasiléia | 1200054 | [Link](https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200054.svg) | [Link](https://cidades.ibge.gov.br/municipio/1200054) | Em 2022, a população era de 8.100 habitantes e a densidade demográfica era de 1,63 hab/km². | Em 2021, o salário médio mensal era de 2,3 salários mínimos. A proporção de pessoas ocupadas era de 7,13%. | Em 2010, a taxa de escolarização de 6 a 14 anos era de 85,1%. IDEB 2021 anos iniciais: 4,6. | nan | Mortalidade infantil: 13,95 por 1.000. Internações por diarreia: 2,3 por 1.000. | Esgotamento adequado: 23,1%. Arborização: 26,5%. Urbanização adequada: 0%. | Área de 4.979,073 km², posição 13 de 22 no estado. | False | False | False | True | 120005 | 2 | 0 | 235 | 5 | nan | D | assis brasil |
| Cruzeiro do Sul | AC | 1200203.jpg | 91888 | 10,46 | 1,8 | 11869 | 13,22 | 44,2 | 94,9 | 5,4 | 4,8 | 18823 | 5412 | 756 | 269 | 148 | 23 | 22934,82 | 88,1 | 0,664 | 139636,41 | 135990,85 | 10,64 | 1 | 40 | 26,91 | 12,7 | 37,9 | 3,7 | nan | Amazônia | Não pertence | 8783,47 | Cruzeiro do Sul | Vale do Juruá | Cruzeiro do Sul | 1200203 | [Link](https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200203.svg) | [Link](https://cidades.ibge.gov.br/municipio/1200203) | Em 2022, a população era de 91.888 habitantes e a densidade demográfica era de 10,46 hab/km². | Em 2021, o salário médio mensal era de 1,8 salários mínimos. A proporção de pessoas ocupadas era de 13,22%. | Em 2010, a taxa de escolarização era de 94,9%. IDEB 2021: 5,4 (iniciais) e 4,8 (finais). | PIB per capita (2021): R$ 22.934,82. Receitas externas (2015): 88,1%. | Mortalidade infantil: 10,64 por 1.000. Internações por diarreia: 1 por 1.000. | Esgotamento adequado: 12,7%. Arborização: 37,9%. Urbanização adequada: 3,7%. | Área de 8.783,47 km², posição 6 de 22 no estado. | False | False | False | True | 120020 | 61 | -4 | 7390 | 284 | nan | C | cruzeiro do sul |
| Epitaciolândia | AC | 1200252.jpeg | 18757 | 11,35 | 1,7 | 2040 | 10,75 | 42,9 | 93,7 | 5,3 | 5,1 | 2749 | 663 | 98 | 24 | 17 | 2 | 33960,77 | nan | 0,653 | 31996,17 | 29191,83 | 17,06 | 0,2 | 8 | 4,93 | 21,4 | 39,1 | 11 | 4333 | Amazônia | Não pertence | 1652,674 | Rio Branco | Vale do Acre | Brasiléia | 1200252 | [Link](https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200252.svg) | [Link](https://cidades.ibge.gov.br/municipio/1200252) | Em 2022, a população era de 18.757 habitantes e a densidade demográfica era de 11,35 hab/km². | Em 2021, o salário médio mensal era de 1,7 salários mínimos. A proporção de pessoas ocupadas era de 10,75%. | Em 2010, a taxa de escolarização era de 93,7%. IDEB 2021: 5,3 (iniciais) e 5,1 (finais). | nan | Mortalidade infantil: 17,06 por 1.000. Internações por diarreia: 0,2 por 1.000. | Esgotamento adequado: 21,4%. Arborização: 39,1%. Urbanização adequada: 11%. | Área de 1.652,674 km², posição 22 de 22 no estado. | False | False | False | True | 120025 | 105 | -1 | 2245 | 40 | nan | D | epitaciolandia |
| Rio Branco | AC | 1200401.jpg | 364756 | 41,28 | 3,3 | 106966 | 25,5 | 36,4 | 95,1 | 5,7 | 4,8 | 56946 | 17052 | 2209 | 903 | 189 | 65 | 26119,02 | 64,8 | 0,727 | 884827,27 | 740733,11 | 14,97 | 0,2 | 95 | 87,42 | 56,7 | 13,8 | 20,4 | 33767 | Amazônia | Não pertence | 8835,154 | Rio Branco | Vale do Acre | Rio Branco | 1200401 | [Link](https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200401.svg) | [Link](https://cidades.ibge.gov.br/municipio/1200401) | Em 2022, a população era de 364.756 habitantes e a densidade demográfica era de 41,28 hab/km². | Em 2021, o salário médio mensal era de 3,3 salários mínimos. A proporção de pessoas ocupadas era de 25,5%. | Em 2010, a taxa de escolarização era de 95,1%. IDEB 2021: 5,7 (iniciais) e 4,8 (finais). | PIB per capita (2021): R$ 26.119,02. Receitas externas (2015): 64,8%. | Mortalidade infantil: 14,97 por 1.000. Internações por diarreia: 0,2 por 1.000. | Esgotamento adequado: 56,7%. Arborização: 13,8%. Urbanização adequada: 20,4%. | Área de 8.835,154 km², capital do estado. | False | False | False | True | 120040 | 2988 | -11 | 67500 | 2557 | nan | D | rio branco |
| Xapuri | AC | 1200708.jpeg | 18243 | 3,41 | 1,8 | 1091 | 5,49 | 45,9 | 87,7 | 5,1 | 5 | 2648 | 609 | 146 | 60 | 49 | 12 | 22902,48 | nan | 0,599 | 35332,64 | 28563,76 | 18,99 | 2,2 | 9 | 3,23 | 27,7 | 14,7 | 4,5 | 484 | Amazônia | Não pertence | 5350,586 | Rio Branco | Vale do Acre | Brasiléia | 1200708 | [Link](https://lohmannesilva.blob.core.windows.net/$web/projeto/green_destinations/svg/1200708.svg) | [Link](https://cidades.ibge.gov.br/municipio/1200708) | Em 2022, a população era de 18.243 habitantes e a densidade demográfica era de 3,41 hab/km². | Em 2021, o salário médio mensal era de 1,8 salários mínimos. A proporção de pessoas ocupadas era de 5,49%. | Em 2010, a taxa de escolarização era de 87,7%. IDEB 2021: 5,1 (iniciais) e 5 (finais). | nan | Mortalidade infantil: 18,99 por 1.000. Internações por diarreia: 2,2 por 1.000. | Esgotamento adequado: 27,7%. Arborização: 14,7%. Urbanização adequada: 4,5%. | Área de 5.350,586 km², posição 12 de 22 no estado. | False | False | False | True | 120070 | 84 | 0 | 951 | 29 | nan | D | xapuri |

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
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Green Destinations | 1.1 | 1.10 | nan | nan | Não é possível calcular a correlação | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | As características, o volume, as atividades e as preferências dos visitantes são monitorados e relatados publicamente. | 1.1-1.10 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.11 | nan | nan | Não é possível calcular a correlação | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | A satisfação dos visitantes com a qualidade e a sustentabilidade da experiência do destino está sendo monitorada e divulgada publicamente. Se necessário, são tomadas medidas em resposta. | 1.1-1.11 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.12 | nan | nan | Não é possível calcular a correlação | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | O destino tem um sistema de gerenciamento de visitantes que é revisado regularmente. São tomadas medidas para gerenciar o volume e as atividades dos visitantes e para reduzi-los ou aumentá-los, conforme necessário, em determinados momentos e locais, levando em conta e equilibrando as necessidades da economia, da comunidade, das culturas e do cultura locais. ambiente. | 1.1-1.12 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.13 | nan | nan | Não é possível calcular a correlação | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | O gerenciamento adequado dos visitantes e dos fluxos de visitantes é aplicado para otimizar os impactos do turismo dentro e ao redor dos ativos naturais e socioculturais do destino. O sistema de gerenciamento refere-se às características, à capacidade e à sensibilidade destes ativos. | 1.1-1.13 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |
| Green Destinations | 1.1 | 1.14 | nan | nan | Não é possível calcular a correlação | Gerenciamento de destinos | Gerenciamento de destinos | Uma pessoa foi designada com a responsabilidade e a autoridade para a implementação adequada e a comunicação do gerenciamento de destinos sustentáveis. | Diretrizes para o comportamento adequado dos visitantes em eventos culturais e em locais sensíveis do ponto de vista cultural e natural são desenvolvidas e disponibilizadas aos visitantes, guias turísticos e outros profissionais. | 1.1-1.14 | Gerenciamento de destinos | #FFFFFF | 0 | independentes | Outros Resultados |

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