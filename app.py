import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

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
    {"Data": "16/02/2026", "Hora": "12h-14h", "Disciplina": "Aula Inaugural / Boas-vindas", "Temas": "Apresentação do coordenador; Boas-vindas; Explicação do formato; Apresentação da carreira.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/02/2026", "Hora": "08h-12h", "Disciplina": "Direito Constitucional", "Temas": "Constitucionalismo, Teoria da Constituição e Classificações; Poder Constituinte (Originário, Derivado, Limites, Mutações); Normas Constitucionais e Hermenêutica; Teoria Geral dos Direitos Fundamentais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/02/2026", "Hora": "14h-18h", "Disciplina": "Direito Tributário", "Temas": "Tributo: conceito e espécies; Princípios Constitucionais Tributários I; Princípios Constitucionais Tributários II; Imunidades Tributárias I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/02/2026", "Hora": "08h-12h", "Disciplina": "Direito Penal Geral", "Temas": "Teoria da Norma Penal; Conflito Aparente de Normas; Imunidades; Princípios do Direito Penal.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/02/2026", "Hora": "14h-18h", "Disciplina": "Direito Ambiental", "Temas": "Introdução. Conceito. Objeto. Princípios fundamentais; Direito Constitucional Ambiental; Política Nacional do Meio Ambiente (PNMA) e SISNAMA; Licenciamento Ambiental.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/02/2026", "Hora": "08h-12h", "Disciplina": "Legislação Penal Especial", "Temas": "Economia Popular e Genocídio; Planejamento Familiar e Parcelamento do Solo Urbano.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/02/2026", "Hora": "14h-18h", "Disciplina": "Direito Tributário", "Temas": "Imunidades Tributárias II; Obrigação Tributária e Fato Gerador; Crédito Tributário e Lançamento Tributário; Suspensão, Extinção e Exclusão do Crédito Tributário I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "01/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Administrativo", "Temas": "Regime jurídico Administrativo/Princípios I; Regime jurídico Administrativo/Princípios II; Atos Administrativos I; Atos Administrativos II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "01/03/2026", "Hora": "14h-18h", "Disciplina": "Direito Penal Geral", "Temas": "Teoria do Crime: Noções Gerais; Teoria do Crime: Fato Típico; Teoria do Crime: Ilicitude; Teoria Geral do Crime: Culpabilidade.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/03/2026", "Hora": "08h-12h", "Disciplina": "Legislação Penal Especial", "Temas": "Legislação Penal Especial II (Art. 9º do CPM, Lei de Introdução ao CP e Contravenções); Crimes contra o Estado Democrático de Direito.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/03/2026", "Hora": "14h-18h", "Disciplina": "Leis Penais Especiais", "Temas": "Lei de Drogas I; Lei de Drogas II; Lavagem de Dinheiro I; Lavagem de Dinheiro II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "08/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Ambiental", "Temas": "A Tríplice Responsabilidade Ambiental; Tutela Processual do Meio Ambiente; Espaços Territoriais Especialmente Protegidos; Direito dos Recursos Hídricos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "08/03/2026", "Hora": "14h-18h", "Disciplina": "Direito Penal Geral", "Temas": "Erro; Punibilidade; Prescrição; Iter Criminis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Tributário", "Temas": "Suspensão, Extinção e Exclusão do Crédito Tributário II; Suspensão, Extinção e Exclusão do Crédito Tributário III; Responsabilidade Tributária I; Responsabilidade Tributária II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/03/2026", "Hora": "14h-18h", "Disciplina": "Legislação Penal Especial", "Temas": "Legislação Penal Especial III (Identificação Pessoal e Crimes do CTB).", "Concluido": False, "Anotacoes": ""},
    {"Data": "15/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Ambiental", "Temas": "Direito Florestal e Biodiversidade; Direito Ambiental Urbano e Resíduos Sólidos; Crimes Ambientais; Direito Ambiental Internacional.", "Concluido": False, "Anotacoes": ""},
    {"Data": "15/03/2026", "Hora": "14h-18h", "Disciplina": "Direito Administrativo", "Temas": "Organização Administrativa I; Organização Administrativa II; Bens Públicos; Poderes Administrativos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Constitucional", "Temas": "Direitos Individuais e Sociais em Espécie; Remédios Constitucionais; Nacionalidade e Direitos Políticos; Controle de Constitucionalidade - Parte I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/03/2026", "Hora": "14h-18h", "Disciplina": "Leis Penais Especiais", "Temas": "Organizações Criminosas I; Organizações Criminosas II; Estatuto do Desarmamento I; Estatuto do Desarmamento II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/03/2026", "Hora": "08h-12h", "Disciplina": "Legislação Penal Especial", "Temas": "Legislação Penal Especial IV (Esporte, HIV e Propriedade Intelectual); Crimes contra a ordem tributária.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/03/2026", "Hora": "14h-18h", "Disciplina": "Direito Tributário", "Temas": "Responsabilidade Tributária III; Garantias e Privilégios do Crédito Tributário; Administração Tributária; Principais Pontos de IPTU, ITBI, ISS e ITCMD; ICMS e IBS; Reforma Tributária.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Ambiental", "Temas": "Mudanças Climáticas; Tutela do Patrimônio Cultural; Meio Ambiente e Atividades Econômicas; Atualidades e Tendências.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/03/2026", "Hora": "14h-18h", "Disciplina": "Leis Penais Especiais", "Temas": "Abuso de Autoridade I; Abuso de Autoridade II; Responsabilidade Civil do Estado; Lei de Crimes Hediondos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "29/03/2026", "Hora": "08h-12h", "Disciplina": "Direito Constitucional", "Temas": "Controle de Constitucionalidade - Parte II; Controle de Constitucionalidade - Parte III; Organização do Estado e Federalismo; Repartição de Competências.", "Concluido": False, "Anotacoes": ""},
    {"Data": "29/03/2026", "Hora": "14h-18h", "Disciplina": "Direito Administrativo", "Temas": "Responsabilidade Civil do Estado I; Responsabilidade Civil do Estado II; Licitações e Contratos I; Licitações e Contratos II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "04/04/2026", "Hora": "08h-12h", "Disciplina": "Direito Penal Parte Especial", "Temas": "Introdução à Parte Especial. Crimes contra a Vida I; Crimes contra a Vida II; Crimes contra a Vida III; Lesões Corporais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "04/04/2026", "Hora": "14h-18h", "Disciplina": "Leis Penais Especiais", "Temas": "Lei Maria da Penha; ECA: Atos Infracionais; ECA: Crimes; Lei de Crimes Ambientais; Lei de Interceptação Telefônica; Lei de Tortura.", "Concluido": False, "Anotacoes": ""},
    {"Data": "05/04/2026", "Hora": "08h-12h", "Disciplina": "Direito Administrativo", "Temas": "Licitações e Contratos III; Licitações e Contratos IV; Improbidade Administrativa I; Improbidade Administrativa II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "05/04/2026", "Hora": "14h-18h", "Disciplina": "Direito Constitucional", "Temas": "Poder Legislativo; Processo Legislativo; Poder Executivo; Poder Judiciário; Defesa do Estado e Ordem Econômica/Social.", "Concluido": False, "Anotacoes": ""},
    {"Data": "11/04/2026", "Hora": "08h-12h", "Disciplina": "Medicina Legal", "Temas": "Legislação. Criminalística I; Criminalística II; Documentos Médico-Legais; Antropologia Forense I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "11/04/2026", "Hora": "14h-18h", "Disciplina": "Direito Administrativo", "Temas": "Agentes Públicos I; Agentes Públicos II; Serviços Públicos I; Serviços Públicos II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "12/04/2026", "Hora": "08h-12h", "Disciplina": "Medicina Legal", "Temas": "Antropologia Forense II; Traumatologia Forense: Instrumentos; Ações mistas; PAF.", "Concluido": False, "Anotacoes": ""},
    {"Data": "12/04/2026", "Hora": "14h-18h", "Disciplina": "Legislação Penal Especial", "Temas": "Sistema Único de Segurança Pública (SUSP).", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/04/2026", "Hora": "08h-12h", "Disciplina": "Direito Penal Parte Especial", "Temas": "Crimes contra a Honra; Crimes contra a Liberdade Individual I; Crimes contra a Liberdade Individual II; Crimes contra o Patrimônio I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/04/2026", "Hora": "14h-18h", "Disciplina": "Medicina Legal", "Temas": "Traumatologia Forense: Asfixiologia; Temperatura e eletricidade; Baropatias; Toxicologia I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/04/2026", "Hora": "08h-12h", "Disciplina": "Direito Civil", "Temas": "Pessoa Natural; Direitos da Personalidade I; Direitos da Personalidade II; Direitos da Personalidade III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/04/2026", "Hora": "14h-18h", "Disciplina": "Medicina Legal", "Temas": "Traumatologia Forense: Toxicologia II; Tanatologia Forense; Cronotanatognose I; Cronotanatognose II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "25/04/2026", "Hora": "08h-12h", "Disciplina": "Medicina Legal", "Temas": "Sexologia Forense I; Sexologia Forense II; Sexologia Forense III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "25/04/2026", "Hora": "14h-18h", "Disciplina": "Direito Empresarial", "Temas": "Direito Comercial: origem e evolução; Empresário; Estabelecimento Empresarial; Institutos Complementares.", "Concluido": False, "Anotacoes": ""},
    {"Data": "26/04/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 1 — QUESTÕES DISCURSIVAS (P2): Identificação do comando; Estrutura-padrão.", "Concluido": False, "Anotacoes": ""},
    {"Data": "26/04/2026", "Hora": "14h-18h", "Disciplina": "Direito Penal Parte Especial", "Temas": "Crimes contra o Patrimônio II; Crimes contra o Patrimônio III; Crimes contra o Patrimônio IV; Crimes contra a Dignidade Sexual I; Crimes contra a Dignidade Sexual II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "02/05/2026", "Hora": "08h-12h", "Disciplina": "Direito Penal Parte Especial", "Temas": "Crimes contra a Paz Pública; Crimes contra a Fé Pública I; Crimes contra a Fé Pública II; Crimes contra a Administração Pública I; Crimes contra a Administração Pública II; Crimes contra a Administração Pública III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "02/05/2026", "Hora": "14h-18h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 1 — QUESTÕES DISCURSIVAS (P2): Padrão CEBRASPE; Treino guiado.", "Concluido": False, "Anotacoes": ""},
    {"Data": "03/05/2026", "Hora": "08h-12h", "Disciplina": "Legislação Penal Especial", "Temas": "Convenções de Mérida, Palermo, Viena e Pacto de San José.", "Concluido": False, "Anotacoes": ""},
    {"Data": "03/05/2026", "Hora": "14h-18h", "Disciplina": "Direito Civil", "Temas": "Bens jurídicos; Defeitos do Negócio Jurídico; Prescrição e Decadência; Direito das Obrigações I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "09/05/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 1 — QUESTÕES DISCURSIVAS (P2): Questão-modelo (Admin/Constitucional); Recortes funcionais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "09/05/2026", "Hora": "14h-18h", "Disciplina": "Direito Empresarial", "Temas": "Teoria geral do direito societário; Sociedades personificadas; Sociedades não personificadas; Sociedade simples e Cooperativa.", "Concluido": False, "Anotacoes": ""},
    {"Data": "10/05/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 1 — QUESTÕES DISCURSIVAS (P2): Questão-modelo (Penal/Processo Penal).", "Concluido": False, "Anotacoes": ""},
    {"Data": "10/05/2026", "Hora": "14h-18h", "Disciplina": "Direito Processual Penal", "Temas": "Disposições preliminares; Inquérito Policial; Acordo de não persecução penal; Ação Penal.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/05/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Identificação da peça; Checklist de estrutura.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/05/2026", "Hora": "14h-18h", "Disciplina": "Direito Civil", "Temas": "Direito das Obrigações II; Teoria Geral dos Contratos I; Teoria Geral dos Contratos II; Temas de contratos em espécie.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/05/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 1: Portaria/Despacho; Diligências iniciais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/05/2026", "Hora": "14h-18h", "Disciplina": "Legislação Penal Especial", "Temas": "Tribunais superiores: institutos de Penal/Processo Penal + Constitucional.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/05/2026", "Hora": "08h-12h", "Disciplina": "Direito Empresarial", "Temas": "Sociedade limitada; Sociedade anônima; Sociedades coligadas; Transformação, Incorporação, Fusão, Cisão.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/05/2026", "Hora": "14h-18h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 2: Representação por busca e apreensão; Cadeia de custódia.", "Concluido": False, "Anotacoes": ""},
    {"Data": "24/05/2026", "Hora": "08h-12h", "Disciplina": "Direitos Humanos", "Temas": "Introdução aos Direitos Humanos; Fundamentos; Características; Teoria Geracional.", "Concluido": False, "Anotacoes": ""},
    {"Data": "24/05/2026", "Hora": "14h-18h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 3: Representação por interceptação; Quebra de sigilo.", "Concluido": False, "Anotacoes": ""},
    {"Data": "30/05/2026", "Hora": "08h-12h", "Disciplina": "Direito Processual Penal", "Temas": "Denúncia e Queixa; Competência I; Competência II; Prisões: Parte geral e prisão em flagrante.", "Concluido": False, "Anotacoes": ""},
    {"Data": "30/05/2026", "Hora": "14h-18h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 4: Representação por prisão preventiva; Prisão temporária.", "Concluido": False, "Anotacoes": ""},
    {"Data": "31/05/2026", "Hora": "08h-12h", "Disciplina": "Direito Civil", "Temas": "Direitos Reais: Posse; Direitos Reais: Usucapião e Propriedade; Temas de Direito de Família; Sucessões I; Sucessões II; Responsabilidade Civil.", "Concluido": False, "Anotacoes": ""},
    {"Data": "31/05/2026", "Hora": "14h-18h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 5: Relatório final de inquérito; Indiciamento.", "Concluido": False, "Anotacoes": ""},
    {"Data": "06/06/2026", "Hora": "08h-12h", "Disciplina": "Legislação Penal Especial", "Temas": "Unificação: Conhecimentos do DF, Política para Mulheres e Primeiros Socorros.", "Concluido": False, "Anotacoes": ""},
    {"Data": "06/06/2026", "Hora": "14h-18h", "Disciplina": "Direitos Humanos", "Temas": "Direitos Internacional dos DH; Controle de Convencionalidade; DUDH; Pacto Internacional de Direitos Civis e Políticos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/06/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 6: Criminalidade econômica; Medidas patrimoniais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/06/2026", "Hora": "14h-18h", "Disciplina": "Direito Processual Penal", "Temas": "Prisão preventiva e domiciliar; Medidas cautelares diversas; Liberdade provisória; Prisão temporária; Sujeitos processuais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "13/06/2026", "Hora": "08h-12h", "Disciplina": "Prova Discursiva", "Temas": "MÓDULO 2 — PEÇAS PRÁTICO-PROFISSIONAIS (P3): Peça 7 (Revisão); Fechamento e estratégia.", "Concluido": False, "Anotacoes": ""},
    {"Data": "13/06/2026", "Hora": "14h-18h", "Disciplina": "Legislação Penal Especial", "Temas": "Lei Orgânica Nacional das Polícias Civis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/06/2026", "Hora": "08h-12h", "Disciplina": "Direito Empresarial", "Temas": "Microempreendedor individual; Títulos de crédito; Recuperação judicial e falência.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/06/2026", "Hora": "14h-18h", "Disciplina": "Direitos Humanos", "Temas": "Pacto Internacional de Direitos Econômicos; Sistema Interamericano; Convenção Americana; Comissão Interamericana.", "Concluido": False, "Anotacoes": ""}
    ]
    st.session_state.cronograma_df = pd.DataFrame(data_source)

df = st.session_state.cronograma_df

# --- SIDEBAR (CONTROLE) ---
with st.sidebar:
    st.title("Painel de Metas")
    
    # KPIs
    total = len(df)
    feitos = df['Concluido'].sum()
    progresso = feitos / total if total > 0 else 0
    
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
    # Use index to identify row in full dataframe
    real_index = idx
    
    icon = "✅" if row['Concluido'] else "📅"
    
    with st.expander(f"{icon} {row['Data']} | {row['Disciplina']}", expanded=False):
        c1, c2 = st.columns([3, 1])
        
        with c1:
            col_d, col_h = st.columns(2)
            
            new_date = col_d.text_input("Data", value=row['Data'], key=f"d_{real_index}")
            new_time = col_h.text_input("Horário", value=row['Hora'], key=f"h_{real_index}")
            
            if new_date != row['Data']:
                st.session_state.cronograma_df.at[real_index, 'Data'] = new_date
            if new_time != row['Hora']:
                st.session_state.cronograma_df.at[real_index, 'Hora'] = new_time
            
            st.markdown(f"**Tópicos:**")
            st.info(row['Temas'])
            
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
