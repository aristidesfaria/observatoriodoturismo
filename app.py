import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO E ESTILO ---
st.set_page_config(page_title="Turismo Intelligence SaaS", layout="wide")

# Simulação de BLOCO 1: Multi-tenancy & Planos
if "igr_slug" not in st.query_params:
    st.query_params["igr_slug"] = "circuito-das-frutas"

current_tenant = st.query_params["igr_slug"]
plano_ativo = "Premium"  # Simulação de Bloco 1

# --- SIDEBAR: CONTROLE E AUDITORIA (BLOCO 7) ---
with st.sidebar:
    st.image("https://www.turismo.sp.gov.br/ciet/logo.png", width=150)
    st.title(f"IGR: {current_tenant.replace('-', ' ').title()}")
    st.info(f"Plano: {plano_ativo}")
    st.write("**Status de Coleta (Calendário):**")
    st.success("Jan/2026: Concluído")
    st.warning("Fev/2026: Em Coleta")
    st.markdown("---")
    st.caption(f"Log LGPD: Usuário 'Tide' autenticado às {datetime.now().strftime('%H:%M')}")

# --- DASHBOARD PRINCIPAL ---
st.title("🚀 Sistema de Inteligência Turística Regional")
tabs = st.tabs(["Econômico", "Ambiental", "Sociocultural", "Governança", "Demanda", "Configurações"])

# --- BLOCO 2: EIXO ECONÔMICO ---
with tabs[0]:
    st.header("💰 Desempenho Econômico")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Hospedagem (Inventário & Ocupação)")
        # Cadastro de Meios (Bloco 2)
        tipo = st.selectbox("Tipo (SBClass):", ["Hotel", "Resort", "Pousada", "Flat", "Outros"]) [cite: 481]
        uhs = st.number_input("Nº de UHs (Capacidade):", min_value=1) [cite: 500]
        # Dados Mensais
        taxa_ocp = st.slider("Taxa de Ocupação Mensal (%):", 0, 100, 55) [cite: 505]
        revpar = st.number_input("RevPAR Calculado (R$):", help="Receita por Quarto Disponível") [cite: 510, 511]

    with col2:
        st.subheader("Transporte e Empregos")
        pax_rod = st.number_input("Pax Rodoviário (Regular + Fretamento):", min_value=0) [cite: 534, 574]
        # Monitoramento por CNAE (Bloco 2)
        st.write("**Mercado de Trabalho (Novo CAGED)**") [cite: 599, 630]
        admissoes = st.number_input("Admissões (ACTs):", min_value=0)
        desligamentos = st.number_input("Desligamentos (ACTs):", min_value=0)
        st.metric("Saldo de Empregos", admissoes - desligamentos) [cite: 630]

# --- BLOCO 3: EIXO AMBIENTAL ---
with tabs[1]:
    st.header("🌿 Sustentabilidade Ambiental")
    c1, c2 = st.columns(2)
    with c1:
        energia = st.number_input("Consumo de Energia (kWh):", help="Dados da Concessionária") [cite: 693, 694]
        agua = st.number_input("Consumo de Água (m³):", help="Dados Sabesp/Local") [cite: 716, 717]
    with c2:
        residuos = st.number_input("Volume Resíduos Sólidos (kg):") [cite: 767]
        iqa = st.select_slider("Qualidade da Água (IQA/CETESB):", options=[1,2,3,4,5]) [cite: 742, 750]

# --- BLOCO 4 & 5: SOCIOCULTURAL E GOVERNANÇA ---
with tabs[2]:
    st.header("♿ Acessibilidade e Social")
    # Score Automático (Bloco 4)
    check_acess = st.multiselect("Itens de Acessibilidade presentes:", 
                                 ["Física", "Visual", "Auditiva", "Cognitiva", "Digital", "Comunicacional", "Social"]) [cite: 779, 784]
    score_acess = len(check_acess)
    st.metric("Score de Acessibilidade", f"{score_acess}/7") [cite: 794]

with tabs[3]:
    st.header("🏛️ Governança")
    comtur = st.checkbox("COMTUR Ativo e Paritário?") [cite: 860, 861]
    pddt = st.checkbox("Plano Diretor (PDDT) Vigente?") [cite: 881, 883]
    score_gov = (comtur + pddt) * 5
    st.metric("Índice de Governança", f"{score_gov}/10")

# --- BLOCO 6: PESQUISA DE DEMANDA (PERFIL) ---
with tabs[4]:
    st.header("👤 Perfil do Turista (Demanda)")
    with st.form("pesquisa_demanda"):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            origem = st.text_input("Cidade de Origem (IBGE):")
            renda = st.selectbox("Faixa de Renda:", ["Até 2 SM", "2 a 5 SM", "5 a 10 SM", "Acima de 10 SM"])
            permanencia = st.number_input("Dias de Permanência:", min_value=1)
        with col_p2:
            gasto_total = st.number_input("Gasto Total na Viagem (R$):", min_value=0.0)
            gasto_diario = gasto_total / permanencia if permanencia > 0 else 0
            st.write(f"**Gasto Diário Calculado: R$ {gasto_diario:.2f}**")
            satisfacao = st.slider("Satisfação Geral:", 1, 10, 8)
        
        enviar_pesquisa = st.form_submit_button("Registrar Pesquisa de Demanda")

# --- BLOCO 8 & 9: VIEWS ANALÍTICAS ---
if st.button("Gerar Relatório de Performance (Views)"):
    st.toast("Processando Views Analíticas...")
    # Simulação de vw_ocupacao_mensal e vw_perfil_turista
    data_view = {
        "Mês": ["Jan", "Fev"],
        "Ocupação Média (%)": [taxa_ocp, taxa_ocp-5],
        "Gasto Médio (R$)": [gasto_diario, gasto_diario*1.1]
    }
    st.table(pd.DataFrame(data_view))
