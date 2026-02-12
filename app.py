import streamlit as st
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cronograma PCDF",
    page_icon="👮‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS (MODO DARK/CLEAN) ---
st.markdown("""
    <style>
    .stTextArea textarea {
        font-size: 14px;
        background-color: #f0f2f6;
    }
    .stExpander {
        border: 1px solid #e6e6e6;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS (COM TÓPICOS COMPLETOS) ---
# Aqui incluí os textos completos conforme sua solicitação original
data_app = [
    {
        "Data": "16/02", "Hora": "12h-14h", "Disciplina": "Direito Constitucional",
        "Temas": "Constitucionalismo, Teoria da Constituição e Classificações; Poder Constituinte (Originário, Derivado, Limites, Mutações); Normas Constitucionais e Hermenêutica."
    },
    {
        "Data": "16/02", "Hora": "20h-22h", "Disciplina": "Direito Penal Geral",
        "Temas": "Teoria da Norma Penal; Conflito Aparente de Normas; Imunidades; Princípios do Direito Penal."
    },
    {
        "Data": "17/02", "Hora": "12h-14h", "Disciplina": "Direito Tributário",
        "Temas": "Tributo: conceito e espécies; Princípios Constitucionais Tributários I; Princípios Constitucionais Tributários II; Imunidades Tributárias I."
    },
    {
        "Data": "17/02", "Hora": "20h-22h", "Disciplina": "Direito Ambiental",
        "Temas": "Introdução. Conceito. Objeto. Princípios fundamentais; Direito Constitucional Ambiental; Política Nacional do Meio Ambiente (PNMA) e SISNAMA; Licenciamento Ambiental."
    },
    {
        "Data": "18/02", "Hora": "12h-14h", "Disciplina": "Legislação Penal Especial",
        "Temas": "Economia Popular e Genocídio; Planejamento Familiar e Parcelamento do Solo Urbano."
    },
    {
        "Data": "18/02", "Hora": "20h-22h", "Disciplina": "Direito Tributário",
        "Temas": "Imunidades Tributárias II; Obrigação Tributária e Fato Gerador; Crédito Tributário e Lançamento Tributário; Suspensão, Extinção e Exclusão do Crédito Tributário I."
    },
    {
        "Data": "19/02", "Hora": "12h-14h", "Disciplina": "Direito Administrativo",
        "Temas": "Regime jurídico Administrativo/Princípios I; Regime jurídico Administrativo/Princípios II; Atos Administrativos I; Atos Administrativos II."
    },
    {
        "Data": "19/02", "Hora": "20h-22h", "Disciplina": "Direito Penal Geral",
        "Temas": "Teoria do Crime: Noções Gerais; Teoria do Crime: Fato Típico; Teoria do Crime: Ilicitude; Teoria Geral do Crime: Culpabilidade."
    },
    {
        "Data": "20/02", "Hora": "12h-14h", "Disciplina": "Legislação Penal Especial",
        "Temas": "Legislação Penal Especial II (Art. 9º do CPM, Lei de Introdução ao CP e Contravenções); Crimes contra o Estado Democrático de Direito."
    },
    {
        "Data": "20/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Especiais",
        "Temas": "Lei de Drogas I; Lei de Drogas II; Lavagem de Dinheiro I; Lavagem de Dinheiro II."
    },
    {
        "Data": "21/02", "Hora": "12h-14h", "Disciplina": "Direito Ambiental",
        "Temas": "A Tríplice Responsabilidade Ambiental; Tutela Processual do Meio Ambiente; Espaços Territoriais Especialmente Protegidos; Direito dos Recursos Hídricos."
    },
    {
        "Data": "21/02", "Hora": "20h-22h", "Disciplina": "Direito Penal Geral",
        "Temas": "Erro; Punibilidade; Prescrição; Iter Criminis."
    },
    {
        "Data": "22/02", "Hora": "12h-14h", "Disciplina": "Direito Tributário",
        "Temas": "Suspensão, Extinção e Exclusão do Crédito Tributário II; Suspensão, Extinção e Exclusão do Crédito Tributário III; Responsabilidade Tributária I; Responsabilidade Tributária II."
    },
    {
        "Data": "22/02", "Hora": "20h-22h", "Disciplina": "Legislação Penal Especial",
        "Temas": "Legislação Penal Especial III (Identificação Pessoal e Crimes do CTB)."
    },
    {
        "Data": "23/02", "Hora": "12h-14h", "Disciplina": "Direito Ambiental",
        "Temas": "Direito Florestal e Biodiversidade; Direito Ambiental Urbano e Resíduos Sólidos; Crimes Ambientais; Direito Ambiental Internacional."
    },
    {
        "Data": "23/02", "Hora": "20h-22h", "Disciplina": "Direito Administrativo",
        "Temas": "Organização Administrativa I; Organização Administrativa II; Bens Públicos; Poderes Administrativos."
    },
    {
        "Data": "24/02", "Hora": "12h-14h", "Disciplina": "Direito Constitucional",
        "Temas": "Direitos Individuais e Sociais em Espécie (Foco: Art. 5º e 6º); Mínimo Existencial vs. Reserva do Possível; Remédios Constitucionais; Nacionalidade e Direitos Políticos; Controle de Constitucionalidade - Parte I."
    },
    {
        "Data": "24/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Especiais",
        "Temas": "Organizações Criminosas I; Organizações Criminosas II; Estatuto do Desarmamento I; Estatuto do Desarmamento II."
    }
    # Adicione os demais dias seguindo este padrão...
]

# --- GERENCIAMENTO DE ESTADO ---
# Inicializa as variáveis se elas não existirem
if 'concluidos' not in st.session_state:
    st.session_state.concluidos = [False] * len(data_app)

if 'notas' not in st.session_state:
    st.session_state.notas = [""] * len(data_app)

# --- BARRA LATERAL (SIDEBAR) - MÉTRICAS ---
with st.sidebar:
    st.title("📊 Painel de Controle")
    st.markdown("---")
    
    # Cálculos
    total = len(data_app)
    feitos = sum(st.session_state.concluidos)
    progresso = feitos / total
    
    # Gráfico de Velocímetro
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = progresso * 100,
        number = {'suffix': "%", 'font': {'size': 25}},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00C0F2"}, # Azul Ciano Moderno
            'steps': [{'range': [0, 100], 'color': "lightgray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"**Metas Cumpridas:** {feitos}/{total}")
    
    # Barra de Progresso Linear
    st.progress(progresso)
    
    st.info("💡 **Dica:** Utilize o campo de notas para registrar artigos de lei que você errou nas questões.")

# --- ÁREA PRINCIPAL ---
st.markdown("# 📅 Cronograma PCDF - Delegado")
st.markdown("### *Planejamento Estratégico de Estudos*")
st.markdown("---")

# Iteração sobre os dados para criar os cards
for i, item in enumerate(data_app):
    
    # Definição visual baseada no status
    is_done = st.session_state.concluidos[i]
    status_icon = "✅" if is_done else "📝"
    status_color = "green" if is_done else "orange"
    
    # Expander (Card Expansível)
    with st.expander(f"{status_icon} {item['Data']} | {item['Disciplina']}", expanded=False):
        
        # Layout interno: Coluna de Conteúdo vs Coluna de Ação
        c1, c2 = st.columns([3, 1.5])
        
        with c1:
            st.markdown(f"**⏰ Horário:** {item['Hora']}")
            st.markdown("### 📚 Tópicos a Estudar:")
            
            # Formatação bonita dos tópicos (bullet points)
            topicos_limpos = item['Temas'].replace(";", "\n- ").replace(".", ".\n- ")
            st.markdown(f"- {topicos_limpos}")
            
            st.markdown("---")
            st.markdown("**📝 Suas Anotações:**")
            
            # Campo de Notas Persistente
            st.session_state.notas[i] = st.text_area(
                label="Notas do dia",
                value=st.session_state.notas[i],
                placeholder="Ex: Revisar Súmula 567 STJ; Errei questão sobre Fato Típico...",
                height=100,
                key=f"nota_{i}",
                label_visibility="collapsed"
            )

        with c2:
            st.markdown("### Controle")
            st.write("---")
            
            # Checkbox Grande
            concluido = st.checkbox(
                "Finalizar Meta",
                value=st.session_state.concluidos[i],
                key=f"check_{i}"
            )
            st.session_state.concluidos[i] = concluido
            
            if concluido:
                st.success("Meta Batida! 🚀")
            else:
                st.warning("Pendente")

st.markdown("---")
st.caption("Desenvolvido por Mentor Cronograma | PCDF 2026")
