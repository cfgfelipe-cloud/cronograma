import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cronograma PCDF",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILIZAÇÃO CSS (INTERFACE MODERNA) ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; }
    .stExpander { border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .streamlit-expanderHeader { font-weight: 600; font-size: 15px; color: #333; }
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; color: #1f2937; }
    .stTextArea textarea { background-color: #f9fafb; border: 1px solid #d1d5db; }
    </style>
""", unsafe_allow_html=True)

# --- DADOS DO CRONOGRAMA ---
if 'cronograma_df' not in st.session_state:
    data_source = [
    {"Data": "16/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Constitucionalismo; Teoria da Const.; Poder Constituinte.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Teoria da Norma; Conflito Aparente; Imunidades; Principios.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Tributario", "Temas": "Tributo: conceito e especies; Principios I e II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Ambiental", "Temas": "Introducao; Principios; Const. Ambiental; PNMA e SISNAMA.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/02/2026", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Economia Popular; Genocidio; Planejamento Familiar.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Tributario", "Temas": "Imunidades II; Obrigacao e Fato Gerador; Credito e Lancamento.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Administrativo", "Temas": "Regime Juridico; Principios; Atos Administrativos I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Teoria do Crime: Fato Tipico, Ilicitude e Culpabilidade.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/02/2026", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Art. 9 CPM; Intro CP; Contravencoes; Estado Democratico.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/02/2026", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Lei de Drogas I/II; Lavagem de Dinheiro I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Triplice Resp.; Tutela Proc.; Espacos Protegidos; Rec. Hidricos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Erro; Punibilidade; Prescricao; Iter Criminis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Tributario", "Temas": "Suspensao/Extincao/Exclusao I/II; Responsabilidade I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/02/2026", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Identificacao Pessoal e Crimes do CTB.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Direito Florestal; Biodiversidade; Crimes Ambientais; Internacional.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Organizacao Administrativa; Bens Publicos; Poderes.", "Concluido": False, "Anotacoes": ""},
    {"Data": "24/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Dir. Individuais/Sociais; Remedios; Nacionalidade/Politicos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "24/02/2026", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Organizacoes Criminosas I/II; Estatuto do Desarmamento I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "25/02/2026", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Esporte; HIV; Prop. Intelectual; Crimes Ordem Tributaria.", "Concluido": False, "Anotacoes": ""},
    {"Data": "25/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Tributario", "Temas": "Resp. III; Garantias do Credito; Admin. Tributaria; Reforma Trib.", "Concluido": False, "Anotacoes": ""},
    {"Data": "26/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Mudancas Climaticas; Patrimonio Cultural; Tendencias.", "Concluido": False, "Anotacoes": ""},
    {"Data": "26/02/2026", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Abuso de Autoridade I/II; Resp. Civil; Crimes Hediondos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "27/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Controle Constitucionalidade I/II; Federalismo; Competencias.", "Concluido": False, "Anotacoes": ""},
    {"Data": "27/02/2026", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Resp. Civil Estado I/II; Licitacoes e Contratos I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/02/2026", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Crimes contra a Vida I/II/III; Lesoes Corporais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/02/2026", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Maria da Penha; ECA; Crimes Ambientais; Interceptacao; Tortura.", "Concluido": False, "Anotacoes": ""},
    {"Data": "01/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Administrativo", "Temas": "Licitacoes III/IV; Improbidade Administrativa I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "01/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Constitucional", "Temas": "Poder Legislativo; Processo Leg.; Executivo; Judiciario.", "Concluido": False, "Anotacoes": ""},
    {"Data": "02/03/2026", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Criminalistica I/II; Documentos; Antropologia I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "02/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Agentes Publicos I/II; Servicos Publicos I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "03/03/2026", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Antropologia II; Traumatologia (Instr. e PAF).", "Concluido": False, "Anotacoes": ""},
    {"Data": "03/03/2026", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Sistema Unico de Seguranca Publica (SUSP).", "Concluido": False, "Anotacoes": ""},
    {"Data": "04/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Honra; Liberdade Individual I/II; Patrimonio I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "04/03/2026", "Hora": "20h-22h", "Disciplina": "Medicina Legal", "Temas": "Asfixiologia; Temperatura/Eletricidade; Baropatias; Toxicologia I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "05/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Civil", "Temas": "Pessoa Natural; Direitos da Personalidade I/II/III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "05/03/2026", "Hora": "20h-22h", "Disciplina": "Medicina Legal", "Temas": "Toxicologia II; Tanatologia; Cronotanatognose I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "06/03/2026", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Sexologia Forense I/II/III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "06/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Empresarial", "Temas": "Teoria Empresa; Empresario; Estabelecimento; Inst. Complementares.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Identificacao de comando e Estrutura-padrao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Penal Especial", "Temas": "Patrimonio II/III/IV; Dignidade Sexual I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "08/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Paz Publica; Fe Publica I/II; Administracao I/II/III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "08/03/2026", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P2: Padrao CEBRASPE; Coerencia/Coesao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "09/03/2026", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Convencoes Merida, Palermo, Viena e Pacto San Jose.", "Concluido": False, "Anotacoes": ""},
    {"Data": "09/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Civil", "Temas": "Bens; Defeitos; Prescricao; Obrigacoes I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "10/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Questao-modelo (Admin/Const/Jurisprudencia).", "Concluido": False, "Anotacoes": ""},
    {"Data": "10/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Empresarial", "Temas": "Teoria Societaria; Personificadas; Nao Personificadas; Cooperativa.", "Concluido": False, "Anotacoes": ""},
    {"Data": "11/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Questao-modelo (Penal/Processo Penal).", "Concluido": False, "Anotacoes": ""},
    {"Data": "11/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Disposicoes Preliminares; Inquerito; ANPP; Acao Penal.", "Concluido": False, "Anotacoes": ""},
    {"Data": "12/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Identificacao de Peca; Checklist Estrutura.", "Concluido": False, "Anotacoes": ""},
    {"Data": "12/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Civil", "Temas": "Obrigacoes II; Teoria Geral dos Contratos I/II; Especies.", "Concluido": False, "Anotacoes": ""},
    {"Data": "13/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Portaria/Despacho; Diligencias Iniciais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "13/03/2026", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Tribunais Superiores: Informativos Consolidados.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Empresarial", "Temas": "Limitada; S/A; Operacoes Societarias; Desconsideracao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/03/2026", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Busca/Apreensao; Cadeia Custodia.", "Concluido": False, "Anotacoes": ""},
    {"Data": "15/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Humanos", "Temas": "Introducao; Fundamentos; Caracteristicas; Geracoes.", "Concluido": False, "Anotacoes": ""},
    {"Data": "15/03/2026", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Interceptacao; Quebra Sigilo; Motivacao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Proc. Penal", "Temas": "Denuncia/Queixa; Competencia I/II; Prisao Flagrante.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/03/2026", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Prisao Preventiva; Temporaria; Cautelares.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Civil", "Temas": "Posse; Usucapiao; Familia; Sucessoes I/II; Resp. Civil.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/03/2026", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Relatorio Final; Indiciamento.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/03/2026", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Conhecimentos DF; Politica Mulheres; Primeiros Socorros.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Humanos", "Temas": "Convencionalidade; DUDH; Pacto Civis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Criminalidade Economica; Medidas Patrimoniais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Preventiva/Domiciliar; Liberdade Provisoria; Temporaria.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/03/2026", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Revisao Pecas; Estrategia de Prova.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/03/2026", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Lei Organica Nacional das Policias Civis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Empresarial", "Temas": "MEI/ME/EPP; Titulos de Credito; Falencia.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Humanos", "Temas": "Pacto Sociais; CADH; Comissao IDH.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/03/2026", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Regime Disciplinar PF e PCDF (Lei 15.047/2024).", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/03/2026", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Comunicacao; Procedimento; Provas; Recursos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/03/2026", "Hora": "12h-14h", "Disciplina": "Dir. Humanos", "Temas": "Corte IDH; Casos Brasil; Povos Tradicionais; Empresas.", "Concluido": False, "Anotacoes": ""}
    ]
    st.session_state.cronograma_df = pd.DataFrame(data_source)

df = st.session_state.cronograma_df

# --- SIDEBAR (CONTROLE) ---
with st.sidebar:
    st.title("Painel de Metas")
    
    # KPIs
    total = len(df)
    feitos = df['Concluido'].sum()
    progresso = feitos / total
    
    st.metric("Total", total)
    st.metric("Concluídas", feitos)
    
    # Barra de Progresso
    st.progress(progresso)
    
    st.markdown("### Filtrar")
    filtro_status = st.radio("Mostrar:", ["Todas", "Pendentes", "Concluídas"])

# Aplicação de Filtros
if filtro_status == "Pendentes":
    df_view = df[df['Concluido'] == False]
elif filtro_status == "Concluídas":
    df_view = df[df['Concluido'] == True]
else:
    df_view = df

# --- TÍTULO E DASHBOARD ---
st.title("Cronograma PCDF")
st.markdown("**Acompanhamento de Estudos - Delegado**")
st.markdown("---")

# Gráficos
col1, col2 = st.columns(2)
with col1:
    st.subheader("Progresso Geral")
    fig = go.Figure(go.Pie(
        labels=['Concluído', 'Pendente'], 
        values=[feitos, total-feitos], 
        hole=.6,
        marker_colors=['#0ea5e9', '#f3f4f6'],
        textinfo='none'
    ))
    fig.update_layout(height=220, margin=dict(t=0, b=0, l=0, r=0), showlegend=True)
    # Texto Central
    fig.add_annotation(text=f"{int(progresso*100)}%", x=0.5, y=0.5, font_size=30, showarrow=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Por Disciplina")
    # Agrupa dados para gráfico de barras
    df_disc = df.groupby('Disciplina')['Concluido'].sum().reset_index()
    fig_bar = px.bar(
        df_disc, 
        x='Concluido', 
        y='Disciplina', 
        orientation='h',
        color_discrete_sequence=['#0ea5e9']
    )
    fig_bar.update_layout(height=220, margin=dict(t=0, b=0, l=0, r=0), xaxis_title=None, yaxis_title=None)
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- LISTA DE TAREFAS ---
st.subheader("Sessões de Estudo")

for idx, row in df_view.iterrows():
    # Identificador único para cada linha no session_state
    real_index = idx
    
    # Estilo condicional
    icon = "✅" if row['Concluido'] else "📅"
    
    with st.expander(f"{icon} {row['Data']} | {row['Disciplina']}", expanded=False):
        c1, c2 = st.columns([3, 1])
        
        with c1:
            # Edição de Data e Hora
            col_d, col_h = st.columns(2)
            
            # Input de Data (Mantendo formato texto para flexibilidade DD/MM/AAAA)
            new_date = col_d.text_input("Data", value=row['Data'], key=f"d_{real_index}")
            new_time = col_h.text_input("Horário", value=row['Hora'], key=f"h_{real_index}")
            
            if new_date != row['Data']:
                st.session_state.cronograma_df.at[real_index, 'Data'] = new_date
            if new_time != row['Hora']:
                st.session_state.cronograma_df.at[real_index, 'Hora'] = new_time
            
            st.markdown(f"**Tópicos:**")
            st.info(row['Temas'])
            
            # Anotações
            notes = st.text_area("Anotações:", value=row['Anotacoes'], key=f"n_{real_index}", height=100)
            if notes != row['Anotacoes']:
                st.session_state.cronograma_df.at[real_index, 'Anotacoes'] = notes
        
        with c2:
            st.write("")
            st.write("")
            is_done = st.checkbox("Concluído", value=row['Concluido'], key=f"c_{real_index}")
            if is_done != row['Concluido']:
                st.session_state.cronograma_df.at[real_index, 'Concluido'] = is_done
                st.rerun()
