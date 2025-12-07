# Sistema de Métricas Educacionais — Análise de Risco de Reprovação


**André Luiz Santos Moreira da Silva, andremoreiradasilva95@gmail.com**

---

Professor:
**Jose Laerte Pires Xavier Junior**
---

_Curso de Ciência de Dados & Inteligência Artificial, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Este projeto desenvolve uma aplicação voltada à ODS 4 – Educação de Qualidade, com o objetivo de auxiliar instituições de ensino a identificar o risco de reprovação e evasão escolar. A solução permite inserir manualmente os dados dos alunos ou carregar um arquivo CSV, utilizando variáveis como nota média, frequência, absenteísmo e participação. Com base nesses dados, o sistema gera métricas e indicadores que ajudam profissionais a compreender o desempenho estudantil e apoiar decisões pedagógicas. O software foi construído em Python com Streamlit e segue práticas de Engenharia de Software, incluindo requisitos definidos, arquitetura documentada, desenvolvimento incremental e versionamento no GitHub._

---


## 1. Introdução

A busca por uma educação inclusiva, equitativa e de qualidade, conforme proposto pela ODS 4, exige que instituições de ensino adotem práticas baseadas em dados para compreender o desempenho e as necessidades de seus alunos. Fatores como nota média, frequência, participação e absenteísmo impactam diretamente o processo de aprendizagem e podem indicar riscos de reprovação ou evasão escolar. No entanto, muitas escolas ainda não possuem ferramentas simples e acessíveis que permitam monitorar esses indicadores de forma rápida e eficiente.

Diante desse cenário, este projeto apresenta uma aplicação desenvolvida em **Python e Streamlit** que possibilita aos profissionais da educação inserir ou importar informações de alunos e visualizar automaticamente métricas relevantes. A solução utiliza um dataset fictício como base conceitual e oferece um painel intuitivo capaz de auxiliar na análise do comportamento acadêmico, favorecendo intervenções pedagógicas mais assertivas.

Além da implementação técnica, o projeto segue os princípios da Engenharia de Software, incluindo elicitação de requisitos, planejamento ágil, modelagem, testes e versionamento. Com isso, busca-se fornecer uma ferramenta funcional que contribua para a promoção de uma educação de qualidade por meio de tecnologia acessível e aplicável ao contexto escolar. 

### 2. Contextualização

A educação desempenha um papel essencial no desenvolvimento social, econômico e humano, sendo considerada um dos principais pilares para a construção de sociedades mais justas e sustentáveis. Dentro desse cenário, a **Organização das Nações Unidas (ONU)** estabeleceu os Objetivos de Desenvolvimento Sustentável, entre eles a **ODS 4 – Educação de Qualidade**, que busca garantir acesso equitativo e oportunidades de aprendizagem ao longo da vida.

Apesar de sua importância, muitas instituições enfrentam dificuldades em **monitorar o desempenho dos alunos** de forma eficiente, especialmente quando se trata de identificar **riscos de reprovação, baixo engajamento ou evasão escolar**. Faltas frequentes, notas baixas e pouca participação são indicadores que, quando analisados corretamente, permitem intervenções mais rápidas e eficazes.

Nesse contexto, o presente trabalho se insere na área de **Engenharia de Software aplicada à educação**, propondo o desenvolvimento de uma aplicação que auxilia profissionais e gestores escolares no acompanhamento do desempenho dos estudantes. Por meio da análise de diferentes métricas acadêmicas e comportamentais, o sistema oferece uma ferramenta prática e acessível para apoio à tomada de decisão, contribuindo diretamente para a melhoria da qualidade educacional.

### 3. Problema

A evasão escolar e a reprovação são desafios persistentes em diversas instituições de ensino, refletindo diretamente na qualidade da educação oferecida. Muitos desses casos poderiam ser evitados caso houvesse um acompanhamento mais consistente dos indicadores de desempenho dos alunos, como frequência, participação, notas e nível de engajamento. No entanto, em grande parte das escolas, esse monitoramento ainda é fragmentado, manual ou pouco estruturado, dificultando a identificação precoce de estudantes em risco.

Além disso, profissionais da educação frequentemente lidam com limitações de tempo e recursos, o que torna complexa a análise contínua de vários alunos simultaneamente. Sem uma visão clara sobre quais métricas impactam diretamente o desempenho, decisões importantes — como intervenções pedagógicas ou ações de apoio — podem ser tomadas de forma tardia.

Nesse contexto educacional, o problema central consiste na falta de um meio eficiente, simples e acessível para consolidar informações dos estudantes e permitir que professores ou gestores identifiquem rapidamente riscos de reprovação ou abandono escolar. A ausência desse acompanhamento sistemático resulta na perda de oportunidades de intervenção, afetando negativamente a trajetória acadêmica dos alunos e o compromisso institucional com uma educação de qualidade.


### 4. Objetivo geral

Desenvolver um sistema inteligente capaz de analisar dados educacionais — como notas, frequência, participação e indicadores de engajamento — para responder à seguinte pergunta orientada a dados: **“Com base no perfil e desempenho do estudante, qual a probabilidade de reprovação ou risco acadêmico?”**

O objetivo principal é transformar dados escolares em informações úteis que auxiliem instituições de ensino a monitorarem o desempenho dos alunos e a identificarem precocemente aqueles que necessitam de intervenção, contribuindo para práticas que promovam uma educação de qualidade.

### 5. Justificativas

O desenvolvimento deste sistema inteligente se justifica pela necessidade crescente de apoiar instituições de ensino na identificação precoce de alunos com risco de reprovação ou evasão. Embora muitas escolas possuam registros de desempenho, frequência e engajamento, esses dados raramente são utilizados de forma integrada para gerar métricas objetivas que apoiem decisões pedagógicas.

A escolha por aprofundar a análise nesses indicadores decorre da importância de tornar o acompanhamento do aluno mais preciso, auxiliando professores e gestores a intervirem no momento certo. Além disso, ao utilizar técnicas de análise de dados e modelos preditivos, o sistema contribui diretamente para o aprimoramento da gestão escolar e para o cumprimento do ODS 4 — Educação de Qualidade, promovendo práticas baseadas em evidências.

A contribuição central deste trabalho está em oferecer uma ferramenta acessível, simples de usar e baseada em dados reais, que possibilita visualizar métricas críticas e estimar a probabilidade de um aluno ser reprovado. Essa abordagem amplia a capacidade da instituição de monitorar seu corpo discente e implementar estratégias preventivas mais eficientes.

## 6. Público alvo

A aplicação foi projetada para ser utilizada por profissionais ligados ao ambiente escolar e à gestão educacional. Esses usuários geralmente possuem conhecimento intermediário sobre tecnologia, lidam diariamente com dados de desempenho dos alunos e ocupam diferentes níveis hierárquicos dentro da instituição. São responsáveis por acompanhar o rendimento escolar, planejar intervenções pedagógicas e monitorar riscos de reprovação ou evasão.

##### Em geral, o público-alvo inclui profissionais com as seguintes características:
* Familiaridade básica a intermediária com computadores e planilhas.
* Necessidade de acessar dados escolares de forma rápida e centralizada.
* Pouco tempo disponível para análises manuais extensas.
* Interesses focados em desempenho estudantil, frequência, comportamento e engajamento.
* Responsabilidade direta ou indireta na tomada de decisões pedagógicas.

#### Personas
**Persona 1 – Coordenadora Pedagógica**

**Nome:** Maria Helena, 42 anos
**Formação:** Pedagogia com pós-graduação em gestão escolar
**Conhecimento tecnológico:** Intermediário

**Motivações:**
1. Identificar rapidamente alunos com risco de reprovação.
2. Tomar decisões baseadas em dados e não apenas em percepções.
3. Organizar intervenções com professores e responsáveis.
   
**Dores:**
1. Falta de ferramentas simples para análise integrada dos dados.
2. Tempo limitado para verificar desempenho aluno por aluno.

**Persona 2 – Professor de Ensino Fundamental**

**Nome:** João Ribeiro, 34 anos
**Formação:** Licenciatura em Matemática
**Conhecimento tecnológico:** Básico

**Motivações:**
1. Acompanhar o progresso dos estudantes de maneira prática.
2. Ver métricas que indiquem quais alunos precisam de reforço.
   
**Dores:**
1. Dificuldade em analisar dados dispersos ou incompletos.
2. Ferramentas pedagógicas pouco integradas ao dia a dia da sala de aula.


## 7. Metodologia
A metodologia adotada neste projeto integra princípios de ciência de dados, engenharia de software e boas práticas de usabilidade para construir um sistema digital capaz de auxiliar instituições escolares na análise de fatores associados à evasão escolar. A seguir detalham-se todas as etapas, ferramentas, processos e tecnologias utilizadas.

### 7.1 Fonte de Dados e Características do Dataset


Para o desenvolvimento, utilizou-se um dataset fictício proveniente da plataforma **Kaggle**, contendo 150 alunos e diversas variáveis relevantes para o estudo da evasão escolar. As variáveis incluídas são:

**ID do Aluno** – identificador único.
**Nome** – referência textual.
**Nota Média** – desempenho acadêmico contínuo (0–10).
**Frequência (%)** – presença registrada nas aulas.
**Atividades Extracurriculares** – participação em atividades adicionais.
**Absenteísmo** – número de faltas.
**Programa de Apoio** – indica suporte institucional.
**Participação nas Aulas (%)** – engajamento qualitativo/quantitativo.
**Evasão (Sim/Não)** – variável-alvo.

Esse conjunto de dados foi selecionado por permitir **análises estatísticas, construção de indicadores escolares e testes de modelagem simples**, sendo apropriado para fins educacionais e demonstração de sistemas de apoio à tomada de decisão.


### 7.2 Ambiente, Frameworks e Bibliotecas Utilizadas

O sistema foi construído totalmente em **Python**, utilizando principalmente:

**Ferramentas principais**
* Streamlit → responsável pela interface web, formulários, painéis interativos, big numbers e organização visual.
* Pandas → manipulação tabular, limpeza de dados, concatenação, filtragem e cálculos estatísticos.
* NumPy → apoio a operações matemáticas auxiliares.
* Matplotlib → geração de gráficos como histogramas, distribuições e análises comparativas.
* Chardet → detecção automática de encoding para leitura robusta de arquivos CSV.
* StringIO → fallback para parsing manual de texto em casos de CSV corrompidos ou com separadores ambíguos.
  
Essas bibliotecas permitem que o sistema funcione tanto com dados carregados automaticamente quanto com inserção manual.

### 7.2 Arquitetura da Aplicação
O código foi organizado em blocos lógicos:

#### 7.2.1. Tema Global e Configuração Visual
Toda a interface utiliza **CSS** customizado para:
* modo escuro (dark mode),
* botões estilizados,
* controles com bordas definidas,
* sliders com barra roxa,
* cartões com sombras,
* painel lateral personalizado.

A estilização amplia a usabilidade, reduz atrito visual e deixa o painel com aparência profissional semelhante a sistemas comerciais.

#### 7.2.2. Leitura Inteligente de CSV
Foi implementada a **função ler_csv_flexivel()**, capaz de:

* detectar encoding automaticamente com chardet,
* testar múltiplos encodings alternativos,
* testar vários delimitadores **(,, ;, \t, |)**,
* utilizar fallback com parsing manual quando necessário,
* prevenir **erros de leitura** via on_bad_lines="skip".

O objetivo foi garantir que qualquer CSV enviado pela escola fosse carregado corretamente, evitando problemas comuns como:
acentuação quebrada, separadores incorretos, colunas fundidas, arquivos salvos em formatos não padronizados.

#### 7.2.3. Session State e Persistência Temporária
Para evitar perda de dados durante a navegação entre seções, utiliza-se st.session_state.data, permitindo:
* armazenamento temporário do dataframe atual,
* adição incremental de alunos,
* reatividade entre operações,
* preservação entre rerenders do Streamlit.

#### 7.2.4. Formulário Manual de Alunos
Foi implementado um formulário robusto, validado e completo que permite cadastrar alunos diretamente no sistema com:
* validação de campos obrigatórios,
* verificação de duplicidade de ID,
* tratamento de entradas incorretas (tipos, limites, formatos),
* sliders visuais para porcentagens,
* botões de rádio compactos para variáveis categóricas,
incremento automático do ID após cada cadastro.

Toda a interface foi otimizada com CSS para reduzir espaços e alinhar elementos.

## 7.3. Processamento e Estruturação dos Dados
Após o carregamento ou cadastro, os dados são padronizados conforme as colunas:

> - ID do Aluno
> - Nome
> - Nota Média
> - Frequência (%)
> - Atividades Extracurriculares
> - Absenteísmo
> - Programa de Apoio
> - Participação nas Aulas (%)
> - Evasão

O sistema trata: conversão numérica coerente, normalização de strings, remoção de espaços e caracteres nocivos, prevenção de duplicatas, manutenção da integridade das variáveis categóricas.

### 7.3.1 Métricas Calculadas no Sistema
Foram adotadas métricas essencialmente descritivas e interpretativas, úteis para identificar padrões relacionados à evasão escolar. Entre elas:

### 7.3.2. Estatísticas Básicas
> - Média geral de notas.
> - Média de frequência.
> - Taxa de evasão.
> - Taxa de participação.
> - Percentual de alunos com atividades extracurriculares.
> - Distribuição de absenteísmo.

### 7.3.3. Indicadores de Risco
> - Correlação entre absenteísmo e evasão.
> - Correlação entre nota média e evasão.
> - Frequência mínima dos evadidos vs. não evadidos.
> - Participação média entre alunos evadidos.
> - Identificação de grupos de risco com base em thresholds.

### 7.3.4. Indicadores de Engajamento

> - média de participação,
> - relação entre atividades extracurriculares e permanência,
> - impacto do programa de apoio.

Todos esses indicadores são exibidos dinamicamente no painel, conforme os dados são alterados.

### 7.3.5. Geração de Gráficos

Utilizando **Matplotlib**, o sistema exibe gráficos como:
> - histograma de notas,
> - histograma de frequência,
> - gráfico de dispersão (ex.: nota × absenteísmo),
> - barras comparando evadidos e não evadidos,
> - análises de distribuição de participação e absenteísmo.

Os gráficos são renderizados em tempo real, integrados ao layout do Streamlit.

### 7.4. Funcionamento Geral do Sistema

O sistema opera em quatro grandes etapas:
**1. Entrada de Dados**
O usuário pode fazer upload de um **CSV com até 200 KB**, ou cadastrar alunos manualmente via formulário.

**2. Validação e Processamento**
Os dados passam por: detecção automática de encoding, identificação do delimitador, conversão de tipos, limpeza de ruído, verificação de duplicidade.

**3. Armazenamento Temporário**
O dataframe é mantido no session_state, permitindo edição contínua.

**4. Visualização e Diagnóstico**
O sistema exibe: tabela completa, big numbers com destaques, gráficos interativos, métricas estatísticas, seções analíticas organizadas.

O sistema utiliza métricas essenciais para avaliar o desempenho e o risco de reprovação dos alunos, incluindo Nota Média, Frequência, Participação nas Aulas, Absenteísmo, presença em Atividades Extracurriculares e participação em Programas de Apoio. A partir dessas informações, a aplicação gera indicadores que auxiliam na identificação de alunos com maior probabilidade de evasão ou baixo desempenho, permitindo intervenções pedagógicas mais assertivas.


## 8. Conclusão
O desenvolvimento deste sistema voltado ao monitoramento do desempenho estudantil demonstra como soluções tecnológicas podem contribuir para a melhoria da educação, alinhando-se diretamente ao ODS 4. A partir da análise de métricas essenciais, o software permite identificar padrões de risco e apoiar tomadas de decisão mais rápidas e assertivas por parte de educadores e gestores. Além disso, o projeto integrou conceitos de engenharia de software, desde a definição do problema até a entrega da solução funcional, reforçando a importância de processos estruturados no desenvolvimento de aplicações voltadas para impacto social. Assim, o trabalho evidencia o potencial da tecnologia como ferramenta para promover uma educação mais inclusiva, eficiente e orientada por dados.


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




