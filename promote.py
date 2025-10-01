import streamlit as st
import time

def pula_linha(quantas=1, pixels=40):
    """
    Esta função pula linhas dentro de um site streamlit.
    quantas: Quantidade de linhas;
    pixels: Quanto espaço você quer pular; 
    """
    for i in range(1, quantas+1):
        st.markdown(f"""<div style="margin-top: {pixels}px"><div>""", unsafe_allow_html=True)


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
            font-size: 2.5rem;
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

# st.markdown(""" 
# <section class="section-container" id="trajetoria">
#     <h2 class="section-title">Minha Trajetória em Dados & IA</h2>
#     <p class="section-lead">
#         Minha carreira é focada em aplicar **Machine Learning**, **IA Generativa** e soluções em **Cloud** para impulsionar a estratégia de negócios e a eficiência operacional.
#     </p>

#     <div class="timeline-item">
#         <h3 class="timeline-title">Experiência no Mercado Financeiro (1 Ano - Itaú)</h3>
#         <p class="timeline-subtitle">Modelagem Preditiva, Engenharia de Dados e Automação</p>
        
#         <dl class="tech-list">
#             <dt class="tech-category">Ações e Resultados-Chave</dt>
#             <dd class="tech-detail">
#                 Desenvolvimento de modelos de **Machine Learning** e análises com **SAS** e Big Data para decisões estratégicas.
#             </dd>
#             <dd class="tech-detail">
#                 Construção e gerenciamento de *pipelines* robustos em **AWS** (S3, Glue, Step Functions), focando em escalabilidade e qualidade de dados.
#             </dd>
#             <dd class="tech-detail">
#                 Criação de soluções de **automação** (Excel/VBA) e desenvolvimento *front-end* básico com **Javascript**.
#             </dd>

#             <dt class="tech-category">Tecnologias Principais</dt>
#             <dd class="tech-detail">
#                 <span class="tech-badge">Python (Pandas)</span>
#                 <span class="tech-badge">PySpark</span>
#                 <span class="tech-badge">SQL / MySQL</span>
#                 <span class="tech-badge">SAS</span>
#                 <span class="tech-badge">C</span>
#                 <span class="tech-badge">AWS KIT</span>
#                 <span class="tech-badge">Javascript</span>
#             </dd>
#         </dl>
#     </div>

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
# </section>
# """
#             , unsafe_allow_html=True)



# --- Seção 1: Minha Trajetória em Dados & IA ---
st.title("Felipe Borges | Portfólio de Dados & IA")

st.write("---") # Linha divisória

# Variáveis
MY_EMAIL = "seu.email@exemplo.com"
MY_LINKEDIN_URL = "https:/linkedin.com/in/felipe-bmda/"

st.header("Fale Comigo")
st.subheader("Propostas | Parcerias | Dúvidas")

# --- Botão 1: EMAIL ---
st.markdown(
f"""
<a href="mailto:{MY_EMAIL}" style="text-decoration: none;">
    <div style='
        background-color: #ff4b4b; 
        color: white; 
        padding: 12px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 18px; 
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
        margin-bottom: 15px; 
        cursor: pointer;
    '>
        ✉️ Email (Contato Formal)
    </div>
</a>
""", 
unsafe_allow_html=True
)

# --- Botão 2: LINKEDIN ---
st.markdown(
f"""
<a href="{MY_LINKEDIN_URL}" target="_blank" style="text-decoration: none;">
    <div style='
        background-color: #0077B5; 
        color: white; 
        padding: 12px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 18px; 
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
        margin-bottom: 15px; 
        cursor: pointer;
    '>
        🔗 LinkedIn (Conexão Profissional)
    </div>
</a>
""", 
unsafe_allow_html=True
)

# # --- Botão 3: WHATSAPP ---
# st.markdown(
# f"""
# <a href="https://wa.me/{MY_WHATSAPP_NUM}" target="_blank" style="text-decoration: none;">
#     <div style='
#         background-color: #25D366; 
#         color: white; 
#         padding: 12px; 
#         border-radius: 8px; 
#         text-align: center; 
#         font-size: 18px; 
#         font-weight: bold;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
#         cursor: pointer;
#     '>
#         💬 WhatsApp (Rápido e Direto)
#     </div>
# </a>
# """, 
# unsafe_allow_html=True
# )



st.write("---")

# Seção: Experiência no Itaú com storytelling
st.header("🏦 Experiência no Itaú Unibanco")

st.markdown("""
Durante meu estágio no Itaú, participei de projetos de **automação**, **engenharia de dados** e criei soluções que melhoraram a **eficiência operacional** da equipe. Abaixo estão alguns indicadores ilustrativos para representar esse impacto.
""")

# KPIs simulados
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Dados Processados", "25M+", "↑ 18%")
with col2:
    st.metric("⚙️ Processos Automatizados", "15", "↑ 50%")
with col3:
    st.metric("⏱️ Tempo Economizado", "120+ horas/mês", "↑ 35%")

import pandas as pd
import random

st.title("Análise de Vendas por Categoria de Produto")

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

# Seção: Habilidades técnicas organizadas
st.header("Habilidades ")

st.markdown("Minhas habilidades estão agrupadas em quatro áreas principais:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔧 Infraestrutura Cloud")
    st.markdown("""
    - AWS (Glue, S3, Athena)
    - Microsoft Excel & VBA (Avançado)
    - 
    """)

    st.subheader("📈 Dados & Análises")
    st.markdown("""
    - Criação de dashboards
    - Análise, recuperação e tratamento de dados
    - Relatórios de dados automatizados 
    """)

with col2:
    st.subheader("💻 Programação")
    st.markdown("""
    - Python
    - SQL
    - Javascript
    - C
    - PySpark
    - Bash
    """)

    st.subheader("🤖 Inteligência Artificial")
    st.markdown("""
    - Modelos Preditivos
    - IA Generativa
    - Transformers (RAG, etc.)
    """)

st.write("---")

st.header("Habilidades Chave")
st.markdown("""
- **Microsoft 365 - Excel
- **Cloud & Dados:** **AWS**, **PySpark**, **AWS Glue**, S3, Athena
- **Programação:** **Python**, **SQL**, C, Javascript
- **IA/ML:** **IA Generativa**, **Transformers**, **RAG**, Modelos Preditivos
- **Metodologias:** **CI/CD**, **Containerização**, **Resolução de Problemas**
""")

st.subheader("Experiência Profissional com LLMs")
st.markdown("""
- **Modelagem Preditiva:** Utilizei **Machine Learning** com **SAS** e ferramentas de Big Data para prever tendências e comportamentos de mercado.
- **Engenharia de Dados & Cloud:** Construí pipelines robustos com **PySpark** e o **AWS KIT (S3, Glue, Step Functions)** para automatizar a ingestão e o processamento de dados, **manipulando grandes volumes de dados no AWS Glue para garantir escalabilidade e eficiência.**
- **Automação de Rotinas:** Desenvolvi soluções com **Excel/VBA** para otimizar fluxos de trabalho internos, liberando tempo para análises mais profundas.
""")

st.subheader("Especialização em IA Generativa")
st.markdown("""
- **IA Generativa Estratégica:** Apliquei **IA Generativa** para resolver problemas de negócio de forma inovadora. Utilizei a arquitetura **RAG** para permitir que modelos tivessem acesso a dados confidenciais e manuais da empresa, garantindo respostas seguras e precisas.
- **Desenvolvimento High-code & Low-code:** Tenho experiência prática com linguagens de programação**.
- Experiência prática na aplicação de **RAG (Retrieval Augmented Generation)** utilizando a **API do modelo GPT**. 
""")

# Seção de Certificado
linha_1 = pula_linha()
st.write("""<h2 style="text-align: center; font-size: 32px"; margin-top: 2em;>Certificados & Badges</h2> """, unsafe_allow_html=True)
st.write("""<p style="text-align: center;">Conhecimento aprofundado e comprovado em IA Generativa.</p>""", unsafe_allow_html=True)
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
    if st.button("Festejar a finalização do portfólio!"):

        st.balloons()








