import streamlit as st
import pandas as pd
import numpy as np
import chardet
from io import StringIO
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
#  TEMA GLOBAL
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Sistema Escolar", layout="wide")

st.markdown("""
<style>

    body, .stApp {
        background-color: #000000 !important;
        color: white !important;
    }

    * { color: white !important; }

    section[data-testid="stSidebar"] {
        background-color: #111111 !important;
    }

    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] select {
        background-color: #222222 !important;
        color: white !important;
        border: 1px solid #5609CE !important;
        border-radius: 6px !important;
    }

    section[data-testid="stSidebar"] .stButton>button {
        background-color: #5609CE !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 8px 18px !important;
        border: none !important;
        font-weight: bold !important;
    }

    h1, h2, h3, h4 {
        color: #C6B5FF !important;
        font-weight: 900 !important;
    }

    .subtitulo-escola {
        font-size: 18px !important;
        color: #C6B5FF !important;
        margin-top: -15px !important;
        margin-bottom: 25px !important;
        opacity: .8;
    }

    /* BIG NUMBERS */
    .big-card {
        background: linear-gradient(135deg, #1a1a1a, #111111);
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        border: 1px solid #3A2A70;
        box-shadow: 0px 0px 12px rgba(130, 90, 255, 0.25);
        transition: 0.3s ease;
    }

    .big-card:hover {
        transform: scale(1.04);
        box-shadow: 0px 0px 18px rgba(130, 90, 255, 0.45);
    }

    .big-number {
        font-size: 40px;
        font-weight: 900;
        color: #C6B5FF !important;
        margin-bottom: 6px;
    }

    .big-label {
        font-size: 15px;
        opacity: .7;
    }

    /* Cards */
    .card {
        background: #111111;
        border-radius: 14px;
        padding: 25px;
        border: 1px solid #3A2A70;
        box-shadow: 0px 0px 12px rgba(130,90,255,0.18);
        margin-bottom: 20px;
    }

    /* BOTÃO DE UPLOAD CSV - FUNDO BRANCO, TEXTO PRETO (SOBRESCREVE O * GERAL) */
    div[data-testid="stFileUploader"] button {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ffffff !important;
        border-radius: 6px !important;
    }
    
    /* Texto DENTRO do botão (o <p>) - PRETO */
    div[data-testid="stFileUploader"] button p {
        color: #000000 !important !important;
    }
    
    /* Ícone dentro do botão */
    div[data-testid="stFileUploader"] button svg {
        color: #000000 !important;
    }
    
    /* Hover no botão */
    div[data-testid="stFileUploader"] button:hover {
        background-color: #f0f0f0 !important;
        border-color: #f0f0f0 !important;
    }
    
    /* Caixa de drag and drop - mantém fundo preto, texto branco */
    div[data-testid="stFileUploader"] > div:first-child {
        background-color: #000000 !important;
        border: 2px dashed #ffffff !important;
        border-radius: 8px !important;
        padding: 30px 20px !important;
        text-align: center !important;
    }
    
    /* Texto dentro da caixa drag and drop */
    div[data-testid="stFileUploader"] > div:first-child div {
        color: white !important;
    }
    
    /* Texto específico "Limit 200KB per file • CSV" */
    div[data-testid="stFileUploader"] > div:first-child > div > div > div + div {
        color: #cccccc !important;
    }

    /* CAIXAS DE SELEÇÃO (SELECTBOX) - TEXTO BRANCO, BORDA BRANCA */
    .stSelectbox > div > div {
        background-color: #000000 !important;
        border: 1px solid white !important;
        border-radius: 6px !important;
    }
    
    /* TEXTO DENTRO DA CAIXA DE SELEÇÃO - BRANCO */
    .stSelectbox > div > div > div {
        color: white !important;
    }

    /* OPÇÕES DO DROPDOWN - FUNDO PRETO, TEXTO BRANCO */
    div[role="listbox"] div {
        background-color: #000000 !important;
        color: white !important;
    }

            
    /* INPUTS DE TEXTO/NÚMERO - FUNDO PRETO, TEXTO BRANCO, BORDA BRANCA */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    input[type="text"],
    input[type="number"] {
        background-color: #000000 !important;
        color: white !important;
        border: 1px solid white !important;
        border-radius: 6px !important;
    }

    /* BOTÃO "Adicionar Aluno" ESPECÍFICO DO FORMULÁRIO */
    form button[kind="secondary"],
    form button[type="submit"],
    div[data-testid="stForm"] button {
        background-color: #000000 !important;
        color: white !important;
        border: 1px solid white !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        margin-top: 10px !important;
        width: 100% !important;
        padding: 10px !important;
    }

    /* SLIDERS - FUNDO PRETO, BORDA BRANCA, BARRA ROXA */
    .stSlider > div {
        border: 1px solid white !important;
        border-radius: 6px !important;
        padding: 8px !important;
        background-color: #000000 !important;
    }
    
    /* BARRA DO SLIDER - ROXA */
    .stSlider > div > div > div > div > div {
        background-color: #5609CE !important;
    }

    /* TEXTO DOS SLIDERS (Frequência e Participação) */
    .stSlider label {
        color: white !important;
    }

    /* GARANTINDO QUE O "NOME DO ALUNO" TENHA BORDA BRANCA */
    .stTextInput input {
        border: 1px solid white !important;
        background-color: #000000 !important;
        color: white !important;
    }

    /* BOTÃO DE ADICIONAR ALUNO VISÍVEL */
    button:has(> div > p:contains("Adicionar Aluno")),
    button:has(> p:contains("Adicionar Aluno")) {
        background-color: #000000 !important;
        color: white !important;
        border: 1px solid white !important !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        margin-top: 10px !important;
        width: 100% !important;
        padding: 10px !important;
    }
    
        /* ====== AJUSTES ESPECÍFICOS PARA O FORMULÁRIO ====== */
    /* Reduz espaçamento entre os radio buttons */
    .stRadio > div {
        gap: 5px !important;  /* Reduz o espaço entre os botões */
        margin-bottom: 0.5rem !important;  /* Reduz margem inferior */
    }
    
    /* Ajusta tamanho dos botões de rádio */
    .stRadio > div > label {
        padding: 6px 12px !important;  /* Reduz padding */
        font-size: 14px !important;    /* Texto um pouco menor */
    }
    
    /* Remove margem extra entre as perguntas categóricas */
    .stRadio {
        margin-bottom: 0.8rem !important;
    }
    
    /* Ajusta o container do formulário para reduzir espaços */
    .stForm {
        padding-bottom: 0 !important;
    }
    
    /* Move o botão "Adicionar Aluno" para mais perto */
    form button[type="submit"] {
        margin-top: 5px !important;  /* Reduz margem superior */
        margin-bottom: 5px !important;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# FUNÇÃO CSV FLEXÍVEL
# ---------------------------------------------------------------------------
def ler_csv_flexivel(uploaded_file):
    raw = uploaded_file.read()
    uploaded_file.seek(0)
    detect = chardet.detect(raw)
    encoding_detectado = detect["encoding"] or "latin1"

    encodings_teste = [encoding_detectado, "utf-8", "utf-8-sig", "latin1", "cp1252"]
    delimitadores = [",", ";", "\t", "|"]

    for enc in encodings_teste:
        for sep in delimitadores:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, encoding=enc, sep=sep, engine="python", on_bad_lines="skip")
                if df.shape[1] > 1 and df.shape[0] > 0:
                    df.columns = [c.strip() for c in df.columns]
                    return df
            except:
                continue

    texto = raw.decode(encoding_detectado or "latin1", errors="replace")
    linhas = texto.splitlines()
    first = linhas[0]
    sep = max([",", ";", "\t", "|"], key=lambda s: first.count(s))
    df = pd.read_csv(StringIO("\n".join(linhas)), sep=sep, engine="python")
    df.columns = [c.strip() for c in df.columns]
    return df

# ---------------------------------------------------------------------------
# COLUNAS PADRÃO
# ---------------------------------------------------------------------------
COLUNAS = [
    "ID do Aluno", "Nome", "Nota Média", "Frequência (%)",
    "Atividades Extracurriculares", "Absenteísmo",
    "Programa de Apoio", "Participação nas Aulas (%)", "Evasão"
]

# ---------------------------------------------------------------------------
# ESCOLA CONFIGURÁVEL
# ---------------------------------------------------------------------------
st.sidebar.title("Configurações")
nome_escola = st.sidebar.text_input("Nome da Escola", "Escola Exemplo")

# ---------------------------------------------------------------------------
# INICIAR DATAFRAME GLOBAL
# ---------------------------------------------------------------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=COLUNAS)

# ---------------------------------------------------------------------------
# FORMULÁRIO MANUAL
# ---------------------------------------------------------------------------
def formulario_inserir():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Adicionar Aluno Manualmente")
    
    # Inicializar session state para os campos, se não existirem
    if 'id_aluno' not in st.session_state:
        st.session_state.id_aluno = "1"
    if 'nome' not in st.session_state:
        st.session_state.nome = ""
    if 'nota_media' not in st.session_state:
        st.session_state.nota_media = "0.0"
    if 'absenteismo' not in st.session_state:
        st.session_state.absenteismo = "0"
    if 'freq' not in st.session_state:
        st.session_state.freq = 80
    if 'participacao' not in st.session_state:
        st.session_state.participacao = 70
    if 'atividades' not in st.session_state:
        st.session_state.atividades = "Não"
    if 'programa' not in st.session_state:
        st.session_state.programa = "Não"
    if 'evasao' not in st.session_state:
        st.session_state.evasao = "Não"

    with st.form("form_aluno"):
        # Linha 1: ID e Nome
        col1a, col2a = st.columns(2)
        with col1a:
            id_aluno = st.text_input("ID do Aluno *", value=st.session_state.get('id_aluno', "1"))
        with col2a:
            nome = st.text_input("Nome do Aluno *", value=st.session_state.get('nome', ""))
        
        # Linha 2: Nota Média e Absenteísmo (lado a lado)
        col1b, col2b = st.columns(2)
        with col1b:
            nota_media = st.text_input("Nota Média (0 a 10) *", value=st.session_state.get('nota_media', "0.0"))
        with col2b:
            absenteismo = st.text_input("Absenteísmo (faltas) *", value=st.session_state.get('absenteismo', "0"))
        
        # Linha 3: Frequência e Participação (lado a lado)
        col1c, col2c = st.columns(2)
        with col1c:
            freq = st.slider("Frequência (%) *", 0, 100, value=st.session_state.get('freq', 80))
        with col2c:
            participacao = st.slider("Participação nas Aulas (%) *", 0, 100, value=st.session_state.get('participacao', 70))
        
        # Linha 4: Perguntas categóricas
        col1d, col2d, col3d = st.columns(3)
        with col1d:
            programa = st.radio("Programa de Apoio? *", ["Sim", "Não"], index=1, horizontal=True, key="programa_radio")
        with col2d:
            atividades = st.radio("Atividades Extracurriculares? *", ["Sim", "Não"], index=1, horizontal=True, key="atividades_radio")
        with col3d:
            evasao = st.radio("Evasão (abandonou?) *", ["Não", "Sim"], index=0, horizontal=True, key="evasao_radio")
        
        st.markdown("*** Campos obrigatórios*")
        enviar = st.form_submit_button("Adicionar Aluno")

    if enviar:
        # Validar campos obrigatórios
        erros = []
        
        # Validar ID do Aluno
        if not id_aluno or not id_aluno.strip():
            erros.append("❌ ID do Aluno é obrigatório")
        elif not id_aluno.isdigit():
            erros.append("❌ ID do Aluno deve ser um número")
        
        # Validar Nome
        if not nome or not nome.strip():
            erros.append("❌ Nome do Aluno é obrigatório")
        
        # Validar Nota Média
        if not nota_media or not nota_media.strip():
            erros.append("❌ Nota Média é obrigatória")
        else:
            try:
                nota = float(nota_media.replace(',', '.'))
                if nota < 0 or nota > 10:
                    erros.append("❌ Nota Média deve estar entre 0 e 10")
            except ValueError:
                erros.append("❌ Nota Média deve ser um número válido")
        
        # Validar Absenteísmo
        if not absenteismo or not absenteismo.strip():
            erros.append("❌ Absenteísmo é obrigatório")
        elif not absenteismo.isdigit():
            erros.append("❌ Absenteísmo deve ser um número inteiro")
        else:
            faltas = int(absenteismo)
            if faltas < 0:
                erros.append("❌ Absenteísmo não pode ser negativo")
        
        # Se houver erros, mostrar todos
        if erros:
            for erro in erros:
                st.error(erro)
        else:
            # Converter os valores de string para os tipos corretos
            try:
                novo = {
                    "ID do Aluno": int(id_aluno),
                    "Nome": nome.strip(),
                    "Nota Média": float(nota_media.replace(',', '.')),
                    "Frequência (%)": freq,
                    "Atividades Extracurriculares": atividades,
                    "Absenteísmo": int(absenteismo),
                    "Programa de Apoio": programa,
                    "Participação nas Aulas (%)": participacao,
                    "Evasão": evasao
                }
                
                # Verificar se ID já existe
                if int(id_aluno) in st.session_state.data["ID do Aluno"].values:
                    st.error(f"❌ ID {id_aluno} já existe! Use um ID diferente.")
                else:
                    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([novo])], ignore_index=True)
                    st.success("✅ Aluno adicionado com sucesso!")
                    
                    # Incrementar ID automaticamente
                    st.session_state.id_aluno = str(int(id_aluno) + 1)
                    # Limpar nome para próximo cadastro
                    st.session_state.nome = ""
                    # Resetar outros valores
                    st.session_state.nota_media = "0.0"
                    st.session_state.absenteismo = "0"
                    st.session_state.freq = 80
                    st.session_state.participacao = 70
                    
            except ValueError as e:
                st.error(f"❌ Erro ao converter valores: {e}. Certifique-se de que os dados são válidos.")
            except Exception as e:
                st.error(f"❌ Erro inesperado: {e}")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# UPLOAD CSV (APENAS UMA VEZ!)
# ---------------------------------------------------------------------------
def upload_csv():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Enviar Base CSV")
    
    st.write("**Escolha o arquivo CSV**")
    
    arquivo = st.file_uploader(
        "Escolha o arquivo CSV", 
        type=["csv"],
        label_visibility="collapsed"
    )

    if arquivo:
        df = ler_csv_flexivel(arquivo)

        if set(df.columns) != set(COLUNAS):
            st.error("❌ O CSV não tem as colunas corretas.")
            st.write("Esperado:", COLUNAS)
            st.write("Recebido:", list(df.columns))
            return

        st.session_state.data = df
        st.success("✅ Base carregada com sucesso!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# CLASSIFICAÇÕES E INDICADORES
# ---------------------------------------------------------------------------
def criar_faixas(df):
    df = df.copy()
    df["Faixa Frequência"] = pd.cut(df["Frequência (%)"],
                                    bins=[0,60,75,90,100],
                                    labels=["Crítica (<60%)","Baixa (60-75%)","Média (75-90%)","Alta (>90%)"])
    df["Faixa Faltas"] = pd.cut(df["Absenteísmo"],
                                bins=[0,3,7,15,9999],
                                labels=["Baixo (0-3)","Moderado (4-7)","Alto (8-15)","Crítico (>15)"])
    df["Faixa Nota"] = pd.cut(df["Nota Média"],
                              bins=[0,5,7,9,10],
                              labels=["Crítica (<5)","Baixa (5-7)","Boa (7-9)","Excelente (9-10)"])
    return df


def gerar_indicadores(df):
    return {
        "Total Alunos": len(df),
        "% Evasão": (df["Evasão"] == "Sim").mean() * 100 if len(df) else 0,
        "Nota Média Geral": df["Nota Média"].mean(),
        "Frequência Média": df["Frequência (%)"].mean(),
        "Faltas Médias": df["Absenteísmo"].mean(),
    }


def classificar_risco(df):
    df = df.copy()
    df["Risco de Reprovação"] = ""
    for i in df.index:
        if df.at[i,"Frequência (%)"] < 60 or df.at[i,"Nota Média"] < 5 or df.at[i,"Absenteísmo"] > 15:
            df.at[i,"Risco de Reprovação"] = "ALTO RISCO"
        elif df.at[i,"Frequência (%)"] < 75 or df.at[i,"Nota Média"] < 7 or df.at[i,"Absenteísmo"] > 7:
            df.at[i,"Risco de Reprovação"] = "MÉDIO RISCO"
        elif df.at[i,"Frequência (%)"] < 90 or df.at[i,"Nota Média"] < 9 or df.at[i,"Absenteísmo"] > 3:
            df.at[i,"Risco de Reprovação"] = "BAIXO RISCO"
        else:
            df.at[i,"Risco de Reprovação"] = "SEM RISCO"
    return df


# ---------------------------------------------------------------------------
# GRÁFICOS COM FUNDO PRETO + CORES EM DEGRADÊ
# ---------------------------------------------------------------------------

def configurar_tema(ax, titulo):
    ax.set_facecolor("black")
    ax.figure.set_facecolor("black")

    ax.set_title(titulo, color="white", fontsize=14, fontweight="bold")

    ax.tick_params(colors="white")
    ax.grid(color="gray", linestyle="dotted", alpha=0.4)

    legend = ax.legend()
    if legend:
        for text in legend.get_texts():
            text.set_color("white")

def grafico_evasao(df):
    valores = df["Evasão"].value_counts()
    fig, ax = plt.subplots(figsize=(5,5))
    
    # Cores para evasão: Vermelho (negativo) vs Verde (positivo)
    cores_evasao = ["#FF6B6B", "#4CAF50"]  # Vermelho para "Sim", Verde para "Não"
    
    # Garantir a ordem correta
    labels_ordenados = ["Não", "Sim"] if "Não" in valores.index else valores.index
    valores_ordenados = [valores.get(label, 0) for label in labels_ordenados]
    
    ax.pie(
        valores_ordenados,
        labels=labels_ordenados,
        autopct="%1.1f%%",
        colors=cores_evasao[:len(labels_ordenados)],
        textprops={"color":"white"},
        wedgeprops={"linewidth": 1, "edgecolor": "black"}
    )

    ax.legend(labels_ordenados, loc="lower left")
    configurar_tema(ax, f"Evasão")

    return fig

def grafico_frequencia(df):
    valores = df["Faixa Frequência"].value_counts()
    
    # Ordenar as categorias da pior para a melhor
    ordem_categorias = ["Crítica (<60%)", "Baixa (60-75%)", "Média (75-90%)", "Alta (>90%)"]
    valores = valores.reindex(ordem_categorias, fill_value=0)
    
    fig, ax = plt.subplots()
    
    # Degradê de Vermelho → Laranja → Amarelo → Verde
    # Do pior (vermelho) para o melhor (verde)
    cores_frequencia = ["#FF4444", "#FFA726", "#FFD740", "#4CAF50"]
    
    barras = ax.bar(valores.index, valores.values, color=cores_frequencia)
    
    # Adicionar valores nas barras
    for barra in barras:
        altura = barra.get_height()
        if altura > 0:
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                   f'{int(altura)}', ha='center', va='bottom', color='white', fontweight='bold')
    
    configurar_tema(ax, f"Faixas de Frequência")
    plt.xticks(rotation=45)
    
    return fig

def grafico_faltas(df):
    valores = df["Faixa Faltas"].value_counts()
    
    # Ordenar as categorias da melhor para a pior
    ordem_categorias = ["Baixo (0-3)", "Moderado (4-7)", "Alto (8-15)", "Crítico (>15)"]
    valores = valores.reindex(ordem_categorias, fill_value=0)
    
    fig, ax = plt.subplots()
    
    # Degradê de Verde → Amarelo → Laranja → Vermelho
    # Do melhor (verde) para o pior (vermelho)
    cores_faltas = ["#4CAF50", "#FFD740", "#FFA726", "#FF4444"]
    
    barras = ax.bar(valores.index, valores.values, color=cores_faltas)
    
    # Adicionar valores nas barras
    for barra in barras:
        altura = barra.get_height()
        if altura > 0:
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                   f'{int(altura)}', ha='center', va='bottom', color='white', fontweight='bold')
    
    configurar_tema(ax, f"Faixas de Faltas — {nome_escola}")
    plt.xticks(rotation=45)
    
    return fig

def grafico_risco(df):
    valores = df["Risco de Reprovação"].value_counts()
    
    # Ordenar as categorias do pior para o melhor
    ordem_categorias = ["ALTO RISCO", "MÉDIO RISCO", "BAIXO RISCO", "SEM RISCO"]
    valores = valores.reindex(ordem_categorias, fill_value=0)
    
    fig, ax = plt.subplots()
    
    # Degradê de Vermelho → Laranja → Amarelo → Verde
    # Do pior (vermelho) para o melhor (verde)
    cores_risco = ["#FF4444", "#FFA726", "#FFD740", "#4CAF50"]
    
    barras = ax.bar(valores.index, valores.values, color=cores_risco)
    
    # Adicionar valores nas barras
    for barra in barras:
        altura = barra.get_height()
        if altura > 0:
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                   f'{int(altura)}', ha='center', va='bottom', color='white', fontweight='bold')
    
    configurar_tema(ax, f"Risco de Reprovação — {nome_escola}")
    plt.xticks(rotation=15)
    
    return fig

def grafico_notas(df):
    """Novo gráfico para faixas de nota"""
    valores = df["Faixa Nota"].value_counts()
    
    # Ordenar as categorias da pior para a melhor
    ordem_categorias = ["Crítica (<5)", "Baixa (5-7)", "Boa (7-9)", "Excelente (9-10)"]
    valores = valores.reindex(ordem_categorias, fill_value=0)
    
    fig, ax = plt.subplots()
    
    # Degradê de Vermelho → Laranja → Amarelo → Verde
    # Do pior (vermelho) para o melhor (verde)
    cores_notas = ["#FF4444", "#FFA726", "#FFD740", "#4CAF50"]
    
    barras = ax.bar(valores.index, valores.values, color=cores_notas)
    
    # Adicionar valores nas barras
    for barra in barras:
        altura = barra.get_height()
        if altura > 0:
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                   f'{int(altura)}', ha='center', va='bottom', color='white', fontweight='bold')
    
    configurar_tema(ax, f"Faixas de Nota — {nome_escola}")
    plt.xticks(rotation=45)
    
    return fig


# ---------------------------------------------------------------------------
# INTERFACE PRINCIPAL
# ---------------------------------------------------------------------------
st.title(f"Sistema de Análise da Educação")
st.markdown(
    f"<div class='subtitulo-escola'>Indicadores acadêmicos e operacionais da escola <b>{nome_escola}</b></div>",
    unsafe_allow_html=True
)

aba = st.tabs(["Inserir Aluno", "Enviar CSV", "Base Atual"])

with aba[0]:
    formulario_inserir()

with aba[1]:
    upload_csv()  # CORRETO: Chamando a função upload_csv

with aba[2]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Base Atual de Alunos")
    st.dataframe(st.session_state.data, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# SE TIVER DADOS, MOSTRAR PAINEL
# ---------------------------------------------------------------------------
df = st.session_state.data

if len(df) > 0:
    st.markdown("## Painel de Indicadores")

    df_bi = classificar_risco(criar_faixas(df))
    indicadores = gerar_indicadores(df_bi)

    # BIG NUMBERS
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class='big-card'>
            <div class='big-number'>{indicadores['Total Alunos']}</div>
            <div class='big-label'>Total de Alunos</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='big-card'>
            <div class='big-number'>{indicadores['% Evasão']:.1f}%</div>
            <div class='big-label'>Evasão Geral</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class='big-card'>
            <div class='big-number'>{indicadores['Nota Média Geral']:.2f}</div>
            <div class='big-label'>Nota Média Geral</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class='big-card'>
            <div class='big-number'>{indicadores['Frequência Média']:.1f}%</div>
            <div class='big-label'>Frequência Média</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    g1, g2 = st.columns(2)
    g1.pyplot(grafico_evasao(df_bi))
    g2.pyplot(grafico_frequencia(df_bi))

    g3, g4 = st.columns(2)
    g3.pyplot(grafico_faltas(df_bi))
    g4.pyplot(grafico_risco(df_bi))

    st.markdown("---")

    st.subheader(" Classificação de Risco de Reprovação")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.dataframe(df_bi[[
        "ID do Aluno","Nome","Nota Média","Frequência (%)",
        "Absenteísmo","Risco de Reprovação"
    ]], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)