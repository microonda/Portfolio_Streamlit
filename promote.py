import streamlit as st
import time

def pula_linha(quantas=1, pixels=20):
    """
    Esta função pula linhas dentro de um site streamlit.
    quantas: Quantidade de linhas;
    pixels: Quanto espaço você quer pular; 
    """
    st.write(f"<div style='height: {pixels}px;'></div>" * quantas, unsafe_allow_html=True)


st.set_page_config(
    page_title="Meu Portfólio de Dados & IA",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
    /* Estilos Gerais */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
    }
    .stApp {
        background-color: #121212;
    }
    .st-emotion-cache-1cypcdb {
        color: #f7a61d;
    }

    /* Animação para os cards de use-case */
    .slide-in-right {
        animation: slide-in-right 0.8s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }

    @keyframes slide-in-right {
        0% {
            transform: translateX(1000px);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }

    /* Estilo dos Cards */
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    .card h3 {
        color: #f7a61d;
    }
    .card-text {
        font-size: 1.1em;
        line-height: 1.6;
    }
    .st-emotion-cache-1av2dcr {
        gap: 0px;
    }
    
            // CTA Button
    .hero {
            padding: 2.5rem 1rem;
        }
        .hero h1 {
            font-size: 5.5rem;
            margin-bottom: 1rem;
            margin-top: 1rem;
            font-weight: 700;
        }
        .hero p {
            font-size: 1.1rem;
            color: #3333333;
            max-width: 600px;
            margin: 0 auto 1.5rem auto;
        }
        .cta-button {
            text-align: center;
            padding: 1rem 2rem;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #6a0dad, #00bfff);
            color: white;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .cta-button:hover {
            opacity: 0.9;
        }

    /* Layout responsivo para colunas */
    @media (max-width: 600px) {
        .st-emotion-cache-ocqbe5 {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)


# Trajetória em dados


#     <div class="timeline-item">
#         <h3 class="timeline-title">Experiência Profissional com LLMs</h3>
#         <p class="timeline-subtitle">IA Generativa para Negócios</p>
#         <p class="tech-detail">
#             Aplicação prática de **RAG (Retrieval Augmented Generation)** utilizando a **API do modelo GPT**. Foco na criação de soluções de **IA Generativa** que endereçam problemas de negócio, como otimização de processos de informação.
#         </p>
#         <div class="tech-detail">
#             <span class="tech-badge">RAG</span>
#             <span class="tech-badge">API GPT</span>
#             <span class="tech-badge">IA Generativa</span>
#         </div>
#     </div>
#             , unsafe_allow_html=True)



# --- Seção 1: Minha Trajetória em Dados & IA ---
st.title("| Felipe Borges")
st.header(" | Portfólio de Dados & IA")
# st.write("---")

# Seção de Certificado
st.write("""<h2 style="text-align: center; font-size: 32px"; margin-top: 2em;>Certificados & Badges</h2> """, unsafe_allow_html=True)
st.write("""<p style="text-align: center;">Conhecimento aprofundado e comprovado em Inteligência Artificial.</p>""", unsafe_allow_html=True)
linha_2 = pula_linha()

cols = st.columns(4)
urls = [
    "./assets/Certificado_Batalha_de_Dados.png",
    "./assets/Certificado_Praticioner_Generative_AI.png",
    "./assets/Certificado_Quantum_Computing.png",
    "./assets/Certificado_Business_Analytics.png"
]
captions = [
    "Certificado de Evento **Hackaton Batalha de Dados**",
    "Certificado em I.A. **Generativa Associate**",
    "Certificado em **Computação Quântica**",
    "Certificado em **Business Analytics**"
]

for col, url, caption in zip(cols, urls, captions):
    with col:
        st.image(url, caption=caption, width=300)



# Seção: Habilidades técnicas organizadas
st.header("Soft & Hard Skills ")

st.markdown("Habilidades analíticas estão agrupadas em quatro áreas principais:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Dados")
    st.markdown("""
    - Criação de dashboards automáticos
    - Análise, governança e tratamento de dados
    - Relatórios e planilhas automatizadas 
    """)

    st.subheader("🔧 Computação em nuvem (cloud computing)")
    st.markdown("""
    - Amazon Web Services **[AWS]** (Glue, S3, Athena)
    - Microsoft Excel Avançado & VBA (Automação de Planilhas)
    - SQL, MySQL e PostgreSQL (Banco de Dados Relacional) 
    """)

with col2:
    st.subheader("💻 Programação & Desenvolvimento")
    st.markdown("""
    - Python
    - PySpark
    - SQL & MySQL
    - C & C++
    - Bash Scripting
    - Lua
    """)

    st.subheader("🤖 Inteligência Artificial")
    st.markdown("""
    - Modelos Preditivos e Machine Learning
    - I.A Generativa
    - Transformers (LLMs, RAG, RLHF etc.)
    """)


# Seção: Experiência no Itaú com storytelling
st.subheader("🏦 Experiência no Itaú Unibanco")

st.markdown("""
Durante meu estágio no Itaú, participei de projetos de **automação**, **engenharia de dados** e criei soluções que melhoraram a eficiência operacional da equipe. Abaixo estão alguns indicadores 100% ilustrativos para representar esse impacto.
""")
st.write("---")


# KPIs simulados
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Dados Processados", "25M+", "↑ 18%")
with col2:
    st.metric("⚙️ Processos Automatizados", "15", "↑ 50%")
with col3:
    st.metric("⏱️ Tempo Economizado", "120+ horas/mês", "↑ 35%")

st.write("---")


st.markdown("## Experiência Profissional com LLMs (Large Language Models)")
st.write("**Modelagem Preditiva:** Utilizei **Machine Learning** e ferramentas de Big Data para prever tendências e comportamentos dos clientes.")
st.write("**Engenharia de Dados & Cloud:** Construí pipelines robustos com **PySpark** e o Amazon Web Services (AWS), principalmente o **AWS KIT (S3, Glue, Step Functions)** para automatizar a ingestão e o processamento de dados, **manipulando grandes volumes de dados para garantir escalabilidade nos projetos.**")
st.write("**Automação de Rotinas:** Desenvolvi soluções com **Excel/VBA** para otimizar fluxos de trabalho internos, automatizando tarefas repetitivas e melhorando a eficiência da equipe.")
st.write("**Criação de Dashboards:** Criei dashboards interativos para monitorar Indicadores e facilitar a tomada de decisões estratégicas.")

st.markdown("## Especialização em IA Generativa")
st.write("""**Desenvolvimento High-code & Low-code:** Tenho experiência prática com linguagens de programação de baixo nível, como C, **Python e Lua.**""")
st.write("""Experiência prática na aplicação de **RAG (Retrieval Augmented Generation)** utilizando a **API do modelo GPT 4.0**.""")
st.write("""Hands-on experience on LangChain scripts and multimodel interfaces implementation (LLama, LLMs, Ollama) with **open-source models.**""")


st.write("---")

import pandas as pd
import random

st.title("Exemplo de planilha separada por Categoria de Produto")

df = pd.DataFrame({
    "Produto": ["Smartphone", "Laptop", "Tablet", "Fones de Ouvido", "Câmera Digital", "Smartwatch"],
    "Janeiro": [random.randint(50, 200) for _ in range(6)],
    "Fevereiro": [random.randint(50, 200) for _ in range(6)],
    "Março": [random.randint(50, 200) for _ in range(6)],
    "Abril": [random.randint(50, 200) for _ in range(6)],
    "Maio": [random.randint(50, 200) for _ in range(6)],
    "Junho": [random.randint(50, 200) for _ in range(6)],
})

df_vendas = df.set_index("Produto").T

st.subheader("Volume Total de Vendas por Categoria")
st.bar_chart(df_vendas)

st.subheader("Tendência Mensal de Vendas por Categoria")
st.line_chart(df_vendas)

st.subheader("Distribuição Mensal Acumulada das Vendas")
st.area_chart(df_vendas)

st.subheader("Resumo Estatístico")
st.dataframe(df_vendas.describe().T.style.format("{:.1f}"))

st.write("---")

# # --- Código HTML e CSS do rodapé
# footer_html = f"""
#     <style>
#         .footer {{
#             "background-color": #f0f2f6;
#             "padding": 15px;
#             "text-align": center;
#             "font-size": 14px;
#             "color": #555;
#             "border-top": 1px solid #e0e0e0;
#         }}
#         .footer a {{
#             "color": #007bff;
#             "text-decoration": none;
#         }}
#     </style>
#     <footer class="footer"><p style="text-align: center;">© 2025 | Todos os direitos reservados.</p></footer>
# """

# # Renderiza o HTML e CSS usando st.html
# st.markdown(footer_html, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Botão secreto do portfólio!"):

        st.balloons()










