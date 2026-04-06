import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da Página
st.set_page_config(page_title="Coleta de Dados RITS-SP", layout="wide")

# Título e Cabeçalho Institucional
st.title("📊 Portal de Monitoramento do Turismo - Regional SP")
st.subheader("Rede de Inteligência do Turismo Sustentável (RITS-SP)")
st.markdown("---")

# --- SEÇÃO 1: IDENTIFICAÇÃO ---
with st.expander("📝 Seção 1: Identificação da IGR e Responsável", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        igr_nome = st.selectbox("Selecione a IGR:", ["Circuito das Frutas", "Litoral Norte", "Pérola do Mantiqueira", "Entre Serras e Águas", "Outros"])
        municipio = st.text_input("Município de Referência:")
    with col2:
        responsavel = st.text_input("Nome do Responsável:")
        email = st.text_input("E-mail Institucional:")

# --- SEÇÃO 2: INDICADORES ECONÔMICOS ---
with st.expander("💰 Seção 2: Desempenho Econômico (Mensal)"):
    st.info("Consolide os dados coletados junto aos meios de hospedagem e bases oficiais.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("**Hospedagem (Dados Primários)**")
        uhs = st.number_input("Nº de UHs Disponíveis:", min_value=0)
        diarias = st.number_input("Total de Diárias Vendidas:", min_value=0)
        hospedes = st.number_input("Total de Hóspedes no Mês:", min_value=0)
    with c2:
        st.write("**Fluxo (Dados Secundários)**")
        rodoviario = st.number_input("Desembarques Rodoviários:", min_value=0)
        aereo = st.number_input("Desembarques Aeroportos (se houver):", min_value=0)
        fretamento = st.number_input("Passageiros Fretamento (ANTT):", min_value=0)
    with c3:
        st.write("**Mercado de Trabalho (Novo CAGED)**")
        estoque = st.number_input("Estoque de Empregos ACTs:", min_value=0)
        saldo = st.number_input("Saldo de Empregos (Admissões - Desligamentos):")

# --- SEÇÃO 3: SUSTENTABILIDADE AMBIENTAL ---
with st.expander("🌿 Seção 3: Indicadores Ambientais (Semestral)"):
    col_a, col_b = st.columns(2)
    with col_a:
        energia = st.number_input("Consumo Energia Comercial (kWh):", min_value=0.0)
        agua = st.number_input("Consumo Água Comercial (m³):", min_value=0.0)
    with col_b:
        esgoto = st.number_input("Volume Esgoto Tratado (m³):", min_value=0.0)
        residuos = st.number_input("Volume Resíduos Sólidos Coletados (kg):", min_value=0.0)

# --- SEÇÃO 4 & 5: SOCIOCULTURAL E GOVERNANÇA ---
with st.expander("⚖️ Seções 4 e 5: Sociocultural e Governança (Anual)"):
    st.write("**Acessibilidade e Participação**")
    acessibilidade = st.multiselect("Tipos de Acessibilidade monitorados no destino:", 
                                    ["Física", "Visual", "Auditiva", "Cognitiva", "Digital", "Comunicacional", "Social"])
    comtur = st.radio("O COMTUR está ativo e paritário?", ("Sim", "Não"))
    pddt = st.date_input("Data da última atualização do Plano Diretor (PDDT):")

# --- FINALIZAÇÃO E LGPD ---
st.markdown("---")
st.warning("⚠️ **Conformidade LGPD:** Ao enviar, você confirma que os dados seguem a Lei nº 13.709/2018.")
concordo = st.checkbox("Declaro que as informações são fidedignas e autorizo o uso para fins de inteligência turística.")

if st.button("ENVIAR DADOS PARA O OBSERVATÓRIO"):
    if concordo:
        # Aqui o código salvaria em um Google Sheets ou Banco de Dados
        st.success(f"Dados da IGR {igr_nome} enviados com sucesso para o Professor Tide!")
    else:
        st.error("Você precisa aceitar os termos da LGPD para enviar.")
