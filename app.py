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

# --- ESTILIZAÇÃO CSS (INTERFACE MODERNA & CLEAN) ---
st.markdown("""
    <style>
    /* Remove padding excessivo do topo */
    .block-container {
        padding-top: 1.5rem;
    }
    /* Estilo dos cards (Expander) */
    .streamlit-expanderHeader {
        font-weight: 600;
        font-size: 16px;
        background-color: #f8f9fa;
        border-radius: 5px;
    }
    /* Estilo da barra de progresso */
    .stProgress > div > div > div > div {
        background-color: #000000;
    }
    /* Fonte das áreas de texto */
    .stTextArea textarea {
        font-family: 'Inter', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DE DADOS (SESSION STATE) ---
# Se for a primeira vez, carrega os dados padrão
if 'cronograma_df' not in st.session_state:
    # Dados Base (Corrigidos e Estruturados)
    data_source = [
        {"id": 1, "Data": "2026-02-16", "Hora": "12h-14h", "Disciplina": "Direito Constitucional", "Temas": "Constitucionalismo, Teoria da Constituição e Classificações; Poder Constituinte (Originário, Derivado, Limites, Mutações).", "Concluido": False, "Notas": ""},
        {"id": 2, "Data": "2026-02-16", "Hora": "20h-22h", "Disciplina": "Direito Penal Geral", "Temas": "Teoria da Norma Penal; Conflito Aparente de Normas; Imunidades; Princípios do Direito Penal.", "Concluido": False, "Notas": ""},
        {"id": 3, "Data": "2026-02-17", "Hora": "12h-14h", "Disciplina": "Direito Tributário", "Temas": "Tributo: conceito e espécies; Princípios Constitucionais Tributários I e II.", "Concluido": False, "Notas": ""},
        {"id": 4, "Data": "2026-02-17", "Hora": "20h-22h", "Disciplina": "Direito Ambiental", "Temas": "Introdução. Conceito. Objeto. Princípios fundamentais; Direito Constitucional Ambiental.", "Concluido": False, "Notas": ""},
        {"id": 5, "Data": "2026-02-18", "Hora": "12h-14h", "Disciplina": "Legislação Penal Especial", "Temas": "Economia Popular e Genocídio; Planejamento Familiar e Parcelamento do Solo Urbano.", "Concluido": False, "Notas": ""},
        {"id": 6, "Data": "2026-02-18", "Hora": "20h-22h", "Disciplina": "Direito Tributário", "Temas": "Imunidades Tributárias II; Obrigação Tributária e Fato Gerador; Crédito Tributário.", "Concluido": False, "Notas": ""},
        {"id": 7, "Data": "2026-02-19", "Hora": "12h-14h", "Disciplina": "Direito Administrativo", "Temas": "Regime jurídico Administrativo/Princípios I e II; Atos Administrativos I e II.", "Concluido": False, "Notas": ""},
        {"id": 8, "Data": "2026-02-19", "Hora": "20h-22h", "Disciplina": "Direito Penal Geral", "Temas": "Teoria do Crime: Noções Gerais; Fato Típico; Ilicitude; Culpabilidade.", "Concluido": False, "Notas": ""},
        {"id": 9, "Data": "2026-02-20", "Hora": "12h-14h", "Disciplina": "Legislação Penal Especial", "Temas": "Legislação Penal Especial II (Art. 9º CPM, Lei Introdução CP); Crimes contra o Estado Democrático.", "Concluido": False, "Notas": ""},
        {"id": 10, "Data": "2026-02-20", "Hora": "20h-22h", "Disciplina": "Leis Penais Especiais", "Temas": "Lei de Drogas I e II; Lavagem de Dinheiro I e II.", "Concluido": False, "Notas": ""},
        {"id": 11, "Data": "2026-02-21", "Hora": "12h-14h", "Disciplina": "Direito Ambiental", "Temas": "A Tríplice Responsabilidade Ambiental; Tutela Processual; Espaços Protegidos.", "Concluido": False, "Notas": ""},
        {"id": 12, "Data": "2026-02-21", "Hora": "20h-22h", "Disciplina": "Direito Penal Geral", "Temas": "Erro; Punibilidade; Prescrição; Iter Criminis.", "Concluido": False, "Notas": ""},
        {"id": 13, "Data": "2026-02-22", "Hora": "12h-14h", "Disciplina": "Direito Tributário", "Temas": "Suspensão, Extinção e Exclusão do Crédito Tributário II e III.", "Concluido": False, "Notas": ""},
        {"id": 14, "Data": "2026-02-22", "Hora": "20h-22h", "Disciplina": "Legislação Penal Especial", "Temas": "Identificação Pessoal e Crimes do CTB.", "Concluido": False, "Notas": ""},
        {"id": 15, "Data": "2026-02-23", "Hora": "12h-14h", "Disciplina": "Direito Ambiental", "Temas": "Direito Florestal e Biodiversidade; Crimes Ambientais; Direito Internacional.", "Concluido": False, "Notas": ""},
        {"id": 16, "Data": "2026-02-23", "Hora": "20h-22h", "Disciplina": "Direito Administrativo", "Temas": "Organização Administrativa I e II; Bens Públicos; Poderes Administrativos.", "Concluido": False, "Notas": ""},
        {"id": 17, "Data": "2026-02-24", "Hora": "12h-14h", "Disciplina": "Direito Constitucional", "Temas": "Direitos Individuais e Sociais; Remédios Constitucionais; Nacionalidade.", "Concluido": False, "Notas": ""},
        {"id": 18, "Data": "2026-02-24", "Hora": "20h-22h", "Disciplina": "Leis Penais Especiais", "Temas": "Organizações Criminosas I e II; Estatuto do Desarmamento I e II.", "Concluido": False, "Notas": ""},
        {"id": 19, "Data": "2026-02-25", "Hora": "12h-14h", "Disciplina": "Legislação Penal Especial", "Temas": "Esporte; HIV; Propriedade Intelectual; Crimes contra ordem tributária.", "Concluido": False, "Notas": ""},
        {"id": 20, "Data": "2026-02-25", "Hora": "20h-22h", "Disciplina": "Direito Tributário", "Temas": "Responsabilidade Tributária III; Garantias e Privilégios; Administração Tributária.", "Concluido": False, "Notas": ""},
         # ... (A lista continua, mas para o exemplo funcionar cortamos aqui. O código completo teria todos os itens)
    ]
    st.session_state.cronograma_df = pd.DataFrame(data_source)

# Função auxiliar para salvar alterações
def save_changes():
    # O Streamlit gerencia o estado automaticamente ao editar os widgets
    pass

df = st.session_state.cronograma_df

# --- SIDEBAR (FILTROS E KPIs) ---
with st.sidebar:
    st.header("Painel de Controle")
    st.markdown("---")
    
    # KPIs Rápidos
    total_tasks = len(df)
    completed_tasks = df['Concluido'].sum()
    progress_val = completed_tasks / total_tasks
    
    st.metric("Metas Totais", total_tasks)
    st.metric("Concluídas", completed_tasks, delta=f"{progress_val*100:.1f}%")
    
    st.markdown("### Filtros")
    # Filtro por Disciplina
    all_disciplines = list(df['Disciplina'].unique())
    selected_discipline = st.multiselect("Filtrar Disciplina", all_disciplines)
    
    # Filtro por Status
    status_filter = st.radio("Status", ["Todos", "Pendentes", "Concluídos"])
    
    st.markdown("---")
    st.caption("Mentoria Delegado PCDF")

# --- APLICAÇÃO DOS FILTROS ---
df_filtered = df.copy()
if selected_discipline:
    df_filtered = df_filtered[df_filtered['Disciplina'].isin(selected_discipline)]
if status_filter == "Pendentes":
    df_filtered = df_filtered[df_filtered['Concluido'] == False]
elif status_filter == "Concluídos":
    df_filtered = df_filtered[df_filtered['Concluido'] == True]

# --- ÁREA PRINCIPAL ---
st.title("Cronograma PCDF")
st.markdown("**Gestão Estratégica de Estudos - Delegado de Polícia**")
st.markdown("---")

# --- DASHBOARD GRÁFICO (NOVO) ---
col_graph1, col_graph2 = st.columns([1, 1])

with col_graph1:
    st.subheader("Progresso Geral")
    # Gráfico de Rosca (Donut Chart) Minimalista
    fig_donut = go.Figure(data=[go.Pie(
        labels=['Concluído', 'Pendente'], 
        values=[completed_tasks, total_tasks - completed_tasks], 
        hole=.7,
        marker_colors=['#2E86C1', '#EAEDED'], # Azul Profissional e Cinza
        textinfo='none'
    )])
    fig_donut.update_layout(
        showlegend=True, 
        height=250, 
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    # Adicionando texto no centro
    fig_donut.add_annotation(text=f"{int(progress_val*100)}%", x=0.5, y=0.5, font_size=40, showarrow=False, font_family="Arial")
    st.plotly_chart(fig_donut, use_container_width=True)

with col_graph2:
    st.subheader("Desempenho por Disciplina")
    # Agrupamento de dados para o gráfico de barras
    progresso_disc = df.groupby('Disciplina')['Concluido'].mean() * 100
    progresso_disc = progresso_disc.sort_values(ascending=True)
    
    fig_bar = px.bar(
        progresso_disc, 
        orientation='h', 
        text_auto='.0f',
        color_discrete_sequence=['#2E86C1']
    )
    fig_bar.update_layout(
        xaxis_title="% Concluído", 
        yaxis_title=None, 
        height=250, 
        margin=dict(t=0, b=0, l=0, r=0),
        xaxis=dict(range=[0, 100], showgrid=False),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig_bar.update_traces(textposition="outside")
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- LISTA DE TAREFAS (EDITÁVEL) ---
st.subheader("Agenda de Estudos")

for index, row in df_filtered.iterrows():
    # Identificador único para cada linha
    row_id = row['id']
    
    # Definição visual do Card
    border_color = "2px solid #2E86C1" if row['Concluido'] else "1px solid #ddd"
    bg_color = "#f0f8ff" if row['Concluido'] else "#ffffff"
    
    # Container customizado para simular um Card
    with st.container():
        # Expander serve como o "Card" que abre
        label_status = "CONCLUÍDO" if row['Concluido'] else "PENDENTE"
        expander_title = f"{row['Data']} | {row['Disciplina']}  —  {label_status}"
        
        with st.expander(expander_title, expanded=False):
            
            c1, c2 = st.columns([2, 1])
            
            # Coluna 1: Conteúdo e Edição
            with c1:
                st.markdown("##### Detalhes da Meta")
                
                # Edição de Data e Hora
                col_date, col_time = st.columns(2)
                new_date = col_date.text_input("Data", value=row['Data'], key=f"date_{row_id}")
                new_time = col_time.text_input("Horário", value=row['Hora'], key=f"time_{row_id}")
                
                # Atualiza o DataFrame se houver mudança
                if new_date != row['Data']:
                    st.session_state.cronograma_df.at[index, 'Data'] = new_date
                if new_time != row['Hora']:
                    st.session_state.cronograma_df.at[index, 'Hora'] = new_time

                st.markdown("**Tópicos:**")
                st.info(row['Temas'])
                
                st.markdown("**Anotações Pessoais:**")
                notes = st.text_area("Registre seus erros ou observações", value=row['Notas'], key=f"note_{row_id}", height=100)
                if notes != row['Notas']:
                    st.session_state.cronograma_df.at[index, 'Notas'] = notes

            # Coluna 2: Ação de Conclusão
            with c2:
                st.markdown("##### Status")
                st.write("") # Espaçamento
                
                # Checkbox Grande estilizado via Streamlit
                is_done = st.checkbox("Marcar como Concluído", value=row['Concluido'], key=f"check_{row_id}")
                
                if is_done != row['Concluido']:
                    st.session_state.cronograma_df.at[index, 'Concluido'] = is_done
                    st.rerun() # Recarrega para atualizar gráficos
                
                if is_done:
                    st.success("Meta Finalizada em: " + datetime.now().strftime("%d/%m %H:%M"))
