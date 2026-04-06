import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Configuração da Página conforme padrão acadêmico/formal
st.set_page_config(page_title="Monitoramento RITS-SP", layout="wide")

st.title("📊 Sistema de Coleta de Indicadores de Sustentabilidade")
st.subheader("Rede de Inteligência do Turismo Sustentável do Estado de São Paulo (RITS-SP)")

# Conexão com Google Sheets (Requer configuração de Secrets no Streamlit Cloud)
conn = st.connection("gsheets", type=GSheetsConnection)

# --- BLOCO 1: IDENTIFICAÇÃO (MULTI-TENANCY) ---
with st.sidebar:
    st.header("Identificação")
    igr_nome = st.selectbox("IGR Responsável:", ["Circuito das Frutas", "Litoral Norte", "Pérola do Mantiqueira", "Entre Serras e Águas"])
    municipio_nome = st.text_input("Município Respondente:")
    codigo_ibge = st.text_input("Código IBGE (7 dígitos):")
    mes_ref = st.selectbox("Mês de Referência:", ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
    ano_ref = st.number_input("Ano:", min_value=2024, max_value=2030, value=2026)

# Criando as Abas por Eixos da Matriz
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Eixo 1: Econômico", 
    "🌿 Eixo 2: Ambiental", 
    "🤝 Eixo 3: Sociocultural", 
    "🏛️ Eixo 4: Governança"
])

# --- EIXO 1: ECONÔMICO ---
with tab1:
    st.header("Indicadores Econômicos")
    
    st.subheader("Sazonalidade e Fluxo")
    col1, col2 = st.columns(2)
    with col1:
        taxa_ocupa = st.number_input("Taxa de ocupação dos meios de hospedagem (%)", min_value=0.0, max_value=100.0)
        pax_rodov = st.number_input("Chegadas de passageiros em terminais rodoviários", min_value=0)
    with col2:
        pax_aereo = st.number_input("Chegadas de passageiros nos aeroportos", min_value=0)
        pax_fretam = st.number_input("Chegadas em ônibus de fretamento (eventual/turístico)", min_value=0)

    st.subheader("Empregos e Benefícios")
    col3, col4 = st.columns(2)
    with col3:
        caged_estoque = st.number_input("Estoque de empregos formais diretos (ACTs)", min_value=0)
        caged_saldo = st.number_input("Saldo de empregos (Admissões - Desligamentos)")
    with col4:
        iss_turismo = st.number_input("Arrecadação de ISS em ACTs (R$)", min_value=0.0)

# --- EIXO 2: AMBIENTAL ---
with tab2:
    st.header("Indicadores Ambientais")
    
    col_amb1, col_amb2 = st.columns(2)
    with col_amb1:
        st.write("**Gestão de Energia (kWh)**")
        energ_res = st.number_input("Consumo Residencial", min_value=0.0)
        energ_com = st.number_input("Consumo Comercial", min_value=0.0)
        
        st.write("**Gestão de Águas e Esgoto (m³)**")
        agua_res = st.number_input("Consumo de Água Residencial", min_value=0.0)
        agua_com = st.number_input("Consumo de Água Comercial", min_value=0.0)
        esgoto_col = st.number_input("Volume de Esgoto Coletado", min_value=0.0)
        esgoto_tra = st.number_input("Volume de Esgoto Tratado", min_value=0.0)

    with col_amb2:
        st.write("**Qualidade e Resíduos**")
        balneab = st.select_slider("Classificação da Balneabilidade/Qualidade Águas", options=["Péssima", "Ruim", "Regular", "Boa", "Ótima"])
        residuos_vol = st.number_input("Volume de resíduos sólidos coletados (kg)", min_value=0.0)
        aterro_qual = st.slider("Qualidade dos aterros (Nota IQR 0-10)", 0.0, 10.0, 5.0)

# --- EIXO 3: SOCIOCULTURAL ---
with tab3:
    st.header("Indicadores Socioculturais")
    
    st.subheader("Acessibilidade")
    col_soc1, col_soc2 = st.columns(2)
    with col_soc1:
        acess_score = st.multiselect("Inventário de acessibilidades presentes:", ["Física", "Visual", "Auditiva", "Cognitiva", "Digital", "Comunicacional", "Social"])
        uh_adapt = st.number_input("Proporção de UHs adaptadas (%)", min_value=0.0, max_value=100.0)
    with col_soc2:
        guias_cap = st.number_input("Proporção de guias capacitados para PcD (%)", min_value=0.0, max_value=100.0)

    st.subheader("Satisfação Local")
    sat_morador = st.slider("Satisfação do morador com os impactos do turismo (Nota 1-10)", 1, 10, 5)

# --- EIXO 4: GOVERNANÇA ---
with tab4:
    st.header("Indicadores de Governança")
    
    gov_pddt = st.radio("O Plano Diretor (PDDT) está atualizado e operante?", ["Sim", "Não", "Em elaboração"])
    gov_comtur = st.radio("O COMTUR existe e realiza atividades regulares?", ["Sim", "Não"])
    gov_soc_civil = st.radio("Associações da Sociedade Civil participam da agenda governamental?", ["Sim", "Não"])
    gov_manejo = st.radio("O Plano de Manejo (se houver) está atualizado?", ["Sim", "Não", "Não se aplica"])

# --- BOTÃO DE ENVIO ---
st.markdown("---")
if st.button("🚀 TABULAR DADOS NA PLANILHA"):
    # Organizando os dados para a planilha
    nova_linha = {
        "Data Envio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "IGR": igr_nome, "Município": municipio_nome, "IBGE": codigo_ibge, "Mês": mes_ref, "Ano": ano_ref,
        "Taxa Ocupação": taxa_ocupa, "Pax Rodov": pax_rodov, "Pax Aereo": pax_aereo, "Pax Fretam": pax_fretam,
        "Estoque Empregos": caged_estoque, "Saldo Empregos": caged_saldo, "Arrecadação ISS": iss_turismo,
        "Energia Res": energ_res, "Energia Com": energ_com, "Agua Res": agua_res, "Esgoto Tratado": esgoto_tra,
        "Qualidade Água": balneab, "Residuos": residuos_vol, "Satisfação": sat_morador,
        "PDDT": gov_pddt, "COMTUR": gov_comtur
    }
    
    # Comandos para salvar no Google Sheets via st.connection
    try:
        existing_data = conn.read(worksheet="Respostas", ttl=5)
        updated_df = pd.concat([existing_data, pd.DataFrame([nova_linha])], ignore_index=True)
        conn.update(worksheet="Respostas", data=updated_df)
        st.success("Dados tabulados com sucesso na Planilha do Observatório!")
    except:
        st.error("Erro de conexão. Verifique as credenciais do Google Sheets nos Secrets.")
