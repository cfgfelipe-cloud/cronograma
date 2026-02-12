import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Configuração da Página (Visual Moderno) ---
st.set_page_config(
    page_title="Cronograma PCDF",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS Personalizado para um visual mais limpo (Opcional) ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 2rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- DADOS DO CRONOGRAMA ---
data_app = [
    {"Data": "16/02", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Constitucionalismo; Teoria da Const.; Poder Constituinte.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/02", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Teoria da Norma; Conflito Aparente; Imunidades; Principios.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/02", "Hora": "12h-14h", "Disciplina": "Dir. Tributario", "Temas": "Tributo: conceito e especies; Principios I e II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/02", "Hora": "20h-22h", "Disciplina": "Dir. Ambiental", "Temas": "Introducao; Principios; Const. Ambiental; PNMA e SISNAMA.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/02", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Economia Popular; Genocidio; Planejamento Familiar.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/02", "Hora": "20h-22h", "Disciplina": "Dir. Tributario", "Temas": "Imunidades II; Obrigacao e Fato Gerador; Credito e Lancamento.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/02", "Hora": "12h-14h", "Disciplina": "Dir. Administrativo", "Temas": "Regime Juridico; Principios; Atos Administrativos I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/02", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Teoria do Crime: Fato Tipico, Ilicitude e Culpabilidade.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/02", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Art. 9 CPM; Intro CP; Contravencoes; Estado Democratico.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Lei de Drogas I/II; Lavagem de Dinheiro I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/02", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Triplice Resp.; Tutela Proc.; Espacos Protegidos; Rec. Hidricos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/02", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Erro; Punibilidade; Prescricao; Iter Criminis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/02", "Hora": "12h-14h", "Disciplina": "Dir. Tributario", "Temas": "Suspensao/Extincao/Exclusao I/II; Responsabilidade I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/02", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Identificacao Pessoal e Crimes do CTB.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/02", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Direito Florestal; Biodiversidade; Crimes Ambientais; Internacional.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/02", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Organizacao Administrativa; Bens Publicos; Poderes.", "Concluido": False, "Anotacoes": ""},
    {"Data": "24/02", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Dir. Individuais/Sociais; Remedios; Nacionalidade/Politicos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "24/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Organizacoes Criminosas I/II; Estatuto do Desarmamento I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "25/02", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Esporte; HIV; Prop. Intelectual; Crimes Ordem Tributaria.", "Concluido": False, "Anotacoes": ""},
    {"Data": "25/02", "Hora": "20h-22h", "Disciplina": "Dir. Tributario", "Temas": "Resp. III; Garantias do Credito; Admin. Tributaria; Reforma Trib.", "Concluido": False, "Anotacoes": ""},
    {"Data": "26/02", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Mudancas Climaticas; Patrimonio Cultural; Tendencias.", "Concluido": False, "Anotacoes": ""},
    {"Data": "26/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Abuso de Autoridade I/II; Resp. Civil; Crimes Hediondos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "27/02", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Controle Constitucionalidade I/II; Federalismo; Competencias.", "Concluido": False, "Anotacoes": ""},
    {"Data": "27/02", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Resp. Civil Estado I/II; Licitacoes e Contratos I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/02", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Crimes contra a Vida I/II/III; Lesoes Corporais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "28/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Maria da Penha; ECA; Crimes Ambientais; Interceptacao; Tortura.", "Concluido": False, "Anotacoes": ""},
    {"Data": "01/03", "Hora": "12h-14h", "Disciplina": "Dir. Administrativo", "Temas": "Licitacoes III/IV; Improbidade Administrativa I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "01/03", "Hora": "20h-22h", "Disciplina": "Dir. Constitucional", "Temas": "Poder Legislativo; Processo Leg.; Executivo; Judiciario.", "Concluido": False, "Anotacoes": ""},
    {"Data": "02/03", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Criminalistica I/II; Documentos; Antropologia I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "02/03", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Agentes Publicos I/II; Servicos Publicos I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "03/03", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Antropologia II; Traumatologia (Instr. e PAF).", "Concluido": False, "Anotacoes": ""},
    {"Data": "03/03", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Sistema Unico de Seguranca Publica (SUSP).", "Concluido": False, "Anotacoes": ""},
    {"Data": "04/03", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Honra; Liberdade Individual I/II; Patrimonio I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "04/03", "Hora": "20h-22h", "Disciplina": "Medicina Legal", "Temas": "Asfixiologia; Temperatura/Eletricidade; Baropatias; Toxicologia I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "05/03", "Hora": "12h-14h", "Disciplina": "Dir. Civil", "Temas": "Pessoa Natural; Direitos da Personalidade I/II/III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "05/03", "Hora": "20h-22h", "Disciplina": "Medicina Legal", "Temas": "Toxicologia II; Tanatologia; Cronotanatognose I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "06/03", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Sexologia Forense I/II/III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "06/03", "Hora": "20h-22h", "Disciplina": "Dir. Empresarial", "Temas": "Teoria Empresa; Empresario; Estabelecimento; Inst. Complementares.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Identificacao de comando e Estrutura-padrao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "07/03", "Hora": "20h-22h", "Disciplina": "Dir. Penal Especial", "Temas": "Patrimonio II/III/IV; Dignidade Sexual I/II.", "Concluido": False, "Anotacoes": ""},
    {"Data": "08/03", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Paz Publica; Fe Publica I/II; Administracao I/II/III.", "Concluido": False, "Anotacoes": ""},
    {"Data": "08/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P2: Padrao CEBRASPE; Coerencia/Coesao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "09/03", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Convencoes Merida, Palermo, Viena e Pacto San Jose.", "Concluido": False, "Anotacoes": ""},
    {"Data": "09/03", "Hora": "20h-22h", "Disciplina": "Dir. Civil", "Temas": "Bens; Defeitos; Prescricao; Obrigacoes I.", "Concluido": False, "Anotacoes": ""},
    {"Data": "10/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Questao-modelo (Admin/Const/Jurisprudencia).", "Concluido": False, "Anotacoes": ""},
    {"Data": "10/03", "Hora": "20h-22h", "Disciplina": "Dir. Empresarial", "Temas": "Teoria Societaria; Personificadas; Nao Personificadas; Cooperativa.", "Concluido": False, "Anotacoes": ""},
    {"Data": "11/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Questao-modelo (Penal/Processo Penal).", "Concluido": False, "Anotacoes": ""},
    {"Data": "11/03", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Disposicoes Preliminares; Inquerito; ANPP; Acao Penal.", "Concluido": False, "Anotacoes": ""},
    {"Data": "12/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Identificacao de Peca; Checklist Estrutura.", "Concluido": False, "Anotacoes": ""},
    {"Data": "12/03", "Hora": "20h-22h", "Disciplina": "Dir. Civil", "Temas": "Obrigacoes II; Teoria Geral dos Contratos I/II; Especies.", "Concluido": False, "Anotacoes": ""},
    {"Data": "13/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Portaria/Despacho; Diligencias Iniciais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "13/03", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Tribunais Superiores: Informativos Consolidados.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/03", "Hora": "12h-14h", "Disciplina": "Dir. Empresarial", "Temas": "Limitada; S/A; Operacoes Societarias; Desconsideracao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "14/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Busca/Apreensao; Cadeia Custodia.", "Concluido": False, "Anotacoes": ""},
    {"Data": "15/03", "Hora": "12h-14h", "Disciplina": "Dir. Humanos", "Temas": "Introducao; Fundamentos; Caracteristicas; Geracoes.", "Concluido": False, "Anotacoes": ""},
    {"Data": "15/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Interceptacao; Quebra Sigilo; Motivacao.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/03", "Hora": "12h-14h", "Disciplina": "Dir. Proc. Penal", "Temas": "Denuncia/Queixa; Competencia I/II; Prisao Flagrante.", "Concluido": False, "Anotacoes": ""},
    {"Data": "16/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Prisao Preventiva; Temporaria; Cautelares.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/03", "Hora": "12h-14h", "Disciplina": "Dir. Civil", "Temas": "Posse; Usucapiao; Familia; Sucessoes I/II; Resp. Civil.", "Concluido": False, "Anotacoes": ""},
    {"Data": "17/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Relatorio Final; Indiciamento.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/03", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Conhecimentos DF; Politica Mulheres; Primeiros Socorros.", "Concluido": False, "Anotacoes": ""},
    {"Data": "18/03", "Hora": "20h-22h", "Disciplina": "Dir. Humanos", "Temas": "Convencionalidade; DUDH; Pacto Civis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Criminalidade Economica; Medidas Patrimoniais.", "Concluido": False, "Anotacoes": ""},
    {"Data": "19/03", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Preventiva/Domiciliar; Liberdade Provisoria; Temporaria.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Revisao Pecas; Estrategia de Prova.", "Concluido": False, "Anotacoes": ""},
    {"Data": "20/03", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Lei Organica Nacional das Policias Civis.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/03", "Hora": "12h-14h", "Disciplina": "Dir. Empresarial", "Temas": "MEI/ME/EPP; Titulos de Credito; Falencia.", "Concluido": False, "Anotacoes": ""},
    {"Data": "21/03", "Hora": "20h-22h", "Disciplina": "Dir. Humanos", "Temas": "Pacto Sociais; CADH; Comissao IDH.", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/03", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Regime Disciplinar PF e PCDF (Lei 15.047/2024).", "Concluido": False, "Anotacoes": ""},
    {"Data": "22/03", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Comunicacao; Procedimento; Provas; Recursos.", "Concluido": False, "Anotacoes": ""},
    {"Data": "23/03", "Hora": "12h-14h", "Disciplina": "Dir. Humanos", "Temas": "Corte IDH; Casos Brasil; Povos Tradicionais; Empresas.", "Concluido": False, "Anotacoes": ""}
]


# --- GERENCIAMENTO DE ESTADO (Session State) ---
if 'concluidos' not in st.session_state:
    st.session_state.concluidos = [False] * len(data_app)

# --- CÁLCULO DE MÉTRICAS ---
total_metas = len(data_app)
metas_concluidas = sum(st.session_state.concluidos)
progresso_percentual = (metas_concluidas / total_metas) * 100

# --- INTERFACE PRINCIPAL ---

# Título Principal
st.markdown("# 📅 Cronograma PCDF")
st.markdown("### Acompanhamento Estratégico - Reta Final")
st.divider()

# --- DASHBOARD DE PROGRESSO (Header Moderno) ---
# Usando colunas para criar "cards" de métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de Metas", value=total_metas, delta="Ciclo Teórico")
with col2:
    st.metric(label="Concluídas", value=metas_concluidas, delta=f"{metas_concluidas} blocos")
with col3:
    st.metric(label="Progresso Geral", value=f"{progresso_percentual:.1f}%")

# --- GRÁFICO DE VELOCÍMETRO (Modernizado) ---
# Layout de duas colunas: Gráfico à esquerda, Lista à direita
chart_col, list_col = st.columns([1.5, 3])

with chart_col:
    st.markdown("#### Desempenho Atual")
    # Gráfico Plotly com visual mais limpo e cores modernas
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = progresso_percentual,
        number = {'suffix': "%", 'font': {'size': 40, 'color': "#29B5E8"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 0, 'tickcolor': "white"}, # Remove ticks
            'bar': {'color': "#29B5E8", 'thickness': 0.75}, # Cor moderna (Azul claro)
            'bgcolor': "#EAEAEA", # Fundo cinza claro para contraste
            'borderwidth': 0,
            'bordercolor': "white",
            'steps': [
                {'range': [0, 100], 'color': '#F0F2F6'} # Fundo sutil
            ],
        }
    ))
    # Remove margens e fundo do gráfico para um visual "flutuante"
    fig.update_layout(
        height=350, 
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'family': "Arial, sans-serif"}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Barra de progresso simples como complemento visual
    st.progress(progresso_percentual / 100)


# --- LISTA DE TAREFAS (Visual Limpo com Ícones) ---
with list_col:
    st.markdown("#### Blocos de Estudo")
    
    for i, item in enumerate(data_app):
        # Define o ícone e a cor do status com base na conclusão
        status_icon = "✅" if st.session_state.concluidos[i] else "⏳"
        
        # Expander com título formatado
        with st.expander(f"{status_icon} {item['Data']} | {item['Disciplina']}"):
            
            # Cria colunas internas para organizar a informação dentro do expander
            info_col, action_col = st.columns([3, 1])
            
            with info_col:
                st.markdown(f"**⏰ Horário:** {item['Hora']}")
                st.markdown(f"**📚 Temas Programáticos:**")
                # Formata os temas como uma lista para melhor leitura
                temas_lista = item['Temas'].replace(';', '\n- ')
                st.markdown(f"- {temas_lista}")
                
            with action_col:
                st.markdown("##### Status")
                # Checkbox com chave única para controle de estado
                st.session_state.concluidos[i] = st.checkbox(
                    "Concluído", 
                    value=st.session_state.concluidos[i], 
                    key=f"check_{i}"
                )
