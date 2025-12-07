# Sistema de Métricas Educacionais

O principal objetivo deste trabalho é desenvolver um sistema inteligente capaz de analisar dados educacionais e gerar insights que auxiliem na compreensão do desempenho dos alunos, das demandas do ambiente escolar e do alinhamento das práticas pedagógicas aos Objetivos de Desenvolvimento Sustentável (ODS). O sistema foi projetado para oferecer visualizações claras, métricas relevantes e funcionalidades automatizadas que facilitem a interpretação das informações, contribuindo para a tomada de decisões mais assertivas dentro do contexto educacional.

Como objetivos específicos, busca-se estruturar uma solução completa que inclua a coleta, tratamento, organização e análise dos dados; a implementação de modelos computacionais; e a disponibilização de uma interface intuitiva desenvolvida em Python e Streamlit. Além disso, pretende-se garantir que a ferramenta seja flexível, expansível e capaz de apoiar professores, gestores e pesquisadores em estudos sobre qualidade de ensino, inclusão, desempenho acadêmico e demais temas relacionados aos ODS.

## Integrantes

* André Luiz Santos Moreira da Silva

## Professor

* Prof. Jose Laerte Pires Xavier Junior

## Instruções de utilização
Este sistema foi desenvolvido em Python + Streamlit, com interface totalmente interativa para cadastro de alunos, upload de CSV e análise dos dados educacionais.
<img width="1851" height="791" alt="image" src="https://github.com/user-attachments/assets/0a3d1a63-b162-4a05-9482-dffc225e1b57" />

Abaixo estão todos os requisitos e passos para rodar o projeto localmente.

#### Requisitos do Sistema
Você precisa ter instalado no computador:
> **Python 3.9 ou superior**
> **pip (gerenciador de pacotes do Python)**

#### Bibliotecas Python necessárias
Instale todas de uma vez com:
```python
pip install streamlit pandas numpy chardet matplotlib
```

Ou instale individualmente:
```python
pip install streamlit
pip install pandas
pip install numpy
pip install chardet
pip install matplotlib
```
#### Estrutura do Projeto
O arquivo principal do sistema deve ser nomeado como: **app.py**
Dentro dele, você deve colar exatamente todo o código completo que você enviou (incluindo o CSS e as funções de formulário, upload e tema escuro).

**Exemplo de estrutura:**

meu_projeto/
│── app.py
│── dados_exemplo.csv   (opcional)

#### Como rodar o sistema
Abra o terminal na pasta onde está o arquivo app.py e execute:

```terminal
streamlit run app.py
```
O navegador abrirá automaticamente no endereço:
> http://localhost:8501
    * Trabalhando na preparação dos dados.

