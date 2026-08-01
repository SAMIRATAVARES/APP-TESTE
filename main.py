import streamlit as st

# 1. Configuração da página (SEO básico e layout)
st.set_page_config(
    page_title="Processamento e Automação de Dados para Pequenas Empresas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Estilização CSS Minimalista e Responsiva
st.markdown("""
    <style>
    /* Oculta elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fontes e espaçamento geral */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #2D3748;
    }
    
    /* Estilo dos Cards de Serviços */
    .service-card {
        background-color: #F7FAFC;
        padding: 24px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin-bottom: 16px;
    }
    
    .service-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1A202C;
        margin-bottom: 8px;
    }
    
    .service-desc {
        font-size: 0.95rem;
        color: #4A5568;
        line-height: 1.5;
    }

    /* Ajuste para imagens */
    .stImage > img {
        border-radius: 8px;
        object-fit: cover;
    }
    
    /* Estilo da seção de Contato */
    .contact-box {
        background-color: #EDF2F7;
        padding: 32px;
        border-radius: 8px;
        text-align: center;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO / HERO SECTION ---
st.title("Transforme Dados em Decisões Inteligentes")
st.caption("Soluções acessíveis de automação e processamento de dados para pequenas empresas.")

st.markdown("---")

# --- SOBRE / PROPÓSITO ---
st.markdown("""
Elimine rotinas manuais e relatórios trabalhosos. Ajudamos a sua empresa a organizar, 
processar e estruturar informações para que você foque no que realmente importa: **crescer o seu negócio**.
""")

st.write("") # Espaçamento

# --- SEÇÃO DE SERVIÇOS E IMAGENS ---
st.header("Nossos Serviços")

col1, col2 = st.columns(2, gap="large")

with col1:
    # Espaço para Imagem 1 (Local ou URL)
    # Substitua "https://via.placeholder.com/600x400" pelo caminho da sua imagem (ex: "assets/servico1.jpg")
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80", 
        caption="Automação e Tratamento de Dados", 
        use_container_width=True
    )
    
    st.markdown("""
    <div class="service-card">
        <div class="service-title">⚡ Automação e Limpeza de Dados</div>
        <div class="service-desc">
            Transformamos planilhas bagunçadas e dados brutos em bases limpas, organizadas e prontas para uso.
            Reduza erros manuais e economize horas de trabalho semanal da sua equipe.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Espaço para Imagem 2 (Local ou URL)
    # Substitua "https://via.placeholder.com/600x400" pelo caminho da sua imagem (ex: "assets/servico2.jpg")
    st.image(
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80", 
        caption="Relatórios e Visualização", 
        use_container_width=True
    )
    
    st.markdown("""
    <div class="service-card">
        <div class="service-title">📊 Relatórios Automatizados</div>
        <div class="service-desc">
            Consolidação de dados de diferentes fontes em relatórios claros e diretos ao ponto. 
            Acompanhe seus principais indicadores sem complicação.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SEÇÃO DE CONTATO ---
st.header("Fale Conosco")
st.write("Entre em contato para entender como podemos automatizar os processos da sua empresa.")

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown("""
    **Canais Diretos:**
    * 📧 **E-mail:** contato@suaempresa.com.br
    * 📱 **WhatsApp:** (11) 99999-9999
    * 📍 **Atendimento:** Online para todo o Brasil
    """)

with contact_col2:
    # Formulário simples para captura de leads
    with st.form("contact_form"):
        nome = st.text_input("Seu Nome")
        email = st.text_input("Seu E-mail")
        mensagem = st.text_area("Como podemos ajudar?")
        submit = st.form_submit_button("Enviar Mensagem")
        
        if submit:
            if nome and email and mensagem:
                st.success("Obrigado! Retornaremos o contato em breve.")
            else:
                st.warning("Por favor, preencha todos os campos.")

# --- RODAPÉ ---
st.markdown("<br><hr><center><small>© 2026 Processamento de Dados. Todos os direitos reservados.</small></center>", unsafe_allow_html=True)