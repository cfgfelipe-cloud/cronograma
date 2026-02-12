import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="PCDF Delegado - Mentor", layout="wide")

# Dados do Cronograma Completo
cronograma = [
    {"Data": "16/02", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Constitucionalismo; Teoria da Const.; Poder Constituinte."},
    {"Data": "16/02", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Teoria da Norma; Conflito Aparente; Imunidades; Principios."},
    {"Data": "17/02", "Hora": "12h-14h", "Disciplina": "Dir. Tributario", "Temas": "Tributo: conceito e especies; Principios I e II; Imunidades I."},
    {"Data": "17/02", "Hora": "20h-22h", "Disciplina": "Dir. Ambiental", "Temas": "Introducao; Principios; Const. Ambiental; PNMA e SISNAMA."},
    {"Data": "18/02", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Economia Popular; Genocidio; Planejamento Familiar."},
    {"Data": "18/02", "Hora": "20h-22h", "Disciplina": "Dir. Tributario", "Temas": "Imunidades II; Obrigacao e Fato Gerador; Credito e Lancamento."},
    {"Data": "19/02", "Hora": "12h-14h", "Disciplina": "Dir. Administrativo", "Temas": "Regime Juridico; Principios; Atos Administrativos I/II."},
    {"Data": "19/02", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Teoria do Crime: Fato Tipico, Ilicitude e Culpabilidade."},
    {"Data": "20/02", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Art. 9 CPM; Intro CP; Contravencoes; Estado Democratico."},
    {"Data": "20/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Lei de Drogas I/II; Lavagem de Dinheiro I/II."},
    {"Data": "21/02", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Triplice Resp.; Tutela Proc.; Espacos Protegidos; Rec. Hidricos."},
    {"Data": "21/02", "Hora": "20h-22h", "Disciplina": "Dir. Penal Geral", "Temas": "Erro; Punibilidade; Prescricao; Iter Criminis."},
    {"Data": "22/02", "Hora": "12h-14h", "Disciplina": "Dir. Tributario", "Temas": "Suspensao/Extincao/Exclusao I/II; Responsabilidade I/II."},
    {"Data": "22/02", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Identificacao Pessoal e Crimes do CTB."},
    {"Data": "23/02", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Direito Florestal; Biodiversidade; Crimes Ambientais; Internacional."},
    {"Data": "23/02", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Organizacao Administrativa; Bens Publicos; Poderes."},
    {"Data": "24/02", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Dir. Individuais/Sociais; Remedios; Nacionalidade/Politicos."},
    {"Data": "24/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Organizacoes Criminosas I/II; Estatuto do Desarmamento I/II."},
    {"Data": "25/02", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Esporte; HIV; Prop. Intelectual; Crimes Ordem Tributaria."},
    {"Data": "25/02", "Hora": "20h-22h", "Disciplina": "Dir. Tributario", "Temas": "Resp. III; Garantias do Credito; Admin. Tributaria; Reforma Trib."},
    {"Data": "26/02", "Hora": "12h-14h", "Disciplina": "Dir. Ambiental", "Temas": "Mudancas Climaticas; Patrimonio Cultural; Tendencias."},
    {"Data": "26/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Abuso de Autoridade I/II; Resp. Civil; Crimes Hediondos."},
    {"Data": "27/02", "Hora": "12h-14h", "Disciplina": "Dir. Constitucional", "Temas": "Controle Constitucionalidade I/II; Federalismo; Competencias."},
    {"Data": "27/02", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Resp. Civil Estado I/II; Licitacoes e Contratos I/II."},
    {"Data": "28/02", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Crimes contra a Vida I/II/III; Lesoes Corporais."},
    {"Data": "28/02", "Hora": "20h-22h", "Disciplina": "Leis Penais Esp.", "Temas": "Maria da Penha; ECA; Crimes Ambientais; Tortura."},
    {"Data": "01/03", "Hora": "12h-14h", "Disciplina": "Dir. Administrativo", "Temas": "Licitacoes III/IV; Improbidade Administrativa I/II."},
    {"Data": "01/03", "Hora": "20h-22h", "Disciplina": "Dir. Constitucional", "Temas": "Poder Legislativo; Processo Leg.; Executivo; Judiciario."},
    {"Data": "02/03", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Criminalistica I/II; Documentos; Antropologia I."},
    {"Data": "02/03", "Hora": "20h-22h", "Disciplina": "Dir. Administrativo", "Temas": "Agentes Publicos I/II; Servicos Publicos I/II."},
    {"Data": "03/03", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Antropologia II; Traumatologia (Instr. e PAF)."},
    {"Data": "03/03", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Sistema Unico de Seguranca Publica (SUSP)."},
    {"Data": "04/03", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Honra; Liberdade Individual I/II; Patrimonio I."},
    {"Data": "04/03", "Hora": "20h-22h", "Disciplina": "Medicina Legal", "Temas": "Asfixiologia; Temperatura/Eletricidade; Toxicologia I."},
    {"Data": "05/03", "Hora": "12h-14h", "Disciplina": "Dir. Civil", "Temas": "Pessoa Natural; Direitos da Personalidade I/II/III."},
    {"Data": "05/03", "Hora": "20h-22h", "Disciplina": "Medicina Legal", "Temas": "Toxicologia II; Tanatologia; Cronotanatognose I/II."},
    {"Data": "06/03", "Hora": "12h-14h", "Disciplina": "Medicina Legal", "Temas": "Sexologia Forense I/II/III."},
    {"Data": "06/03", "Hora": "20h-22h", "Disciplina": "Dir. Empresarial", "Temas": "Teoria Empresa; Empresario; Estabelecimento."},
    {"Data": "07/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Identificacao de comando e Estrutura-padrao."},
    {"Data": "07/03", "Hora": "20h-22h", "Disciplina": "Dir. Penal Especial", "Temas": "Patrimonio II/III/IV; Dignidade Sexual I/II."},
    {"Data": "08/03", "Hora": "12h-14h", "Disciplina": "Dir. Penal Especial", "Temas": "Paz Publica; Fe Publica I/II; Administracao I/II/III."},
    {"Data": "08/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P2: Padrao CEBRASPE; Coerencia/Coesao."},
    {"Data": "09/03", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Convencoes Merida, Palermo, Viena e Pacto San Jose."},
    {"Data": "09/03", "Hora": "20h-22h", "Disciplina": "Dir. Civil", "Temas": "Bens; Defeitos; Prescricao; Obrigacoes I."},
    {"Data": "10/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Questao-modelo (Admin/Const/Jurisprudencia)."},
    {"Data": "10/03", "Hora": "20h-22h", "Disciplina": "Dir. Empresarial", "Temas": "Teoria Societaria; Personificadas; Nao Personificadas."},
    {"Data": "11/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P2: Questao-modelo (Penal/Processo Penal)."},
    {"Data": "11/03", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Disposicoes Preliminares; Inquerito; ANPP; Acao Penal."},
    {"Data": "12/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Identificacao de Peca; Checklist Estrutura."},
    {"Data": "12/03", "Hora": "20h-22h", "Disciplina": "Dir. Civil", "Temas": "Obrigacoes II; Teoria Geral dos Contratos I/II; Especies."},
    {"Data": "13/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Portaria/Despacho; Diligencias Iniciais."},
    {"Data": "13/03", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Tribunais Superiores: Informativos Consolidados."},
    {"Data": "14/03", "Hora": "12h-14h", "Disciplina": "Dir. Empresarial", "Temas": "Limitada; S/A; Operacoes Societarias; Desconsideracao."},
    {"Data": "14/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Busca/Apreensao; Cadeia Custodia."},
    {"Data": "15/03", "Hora": "12h-14h", "Disciplina": "Dir. Humanos", "Temas": "Introducao; Fundamentos; Caracteristicas; Geracoes."},
    {"Data": "15/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Interceptacao; Quebra Sigilo; Motivacao."},
    {"Data": "16/03", "Hora": "12h-14h", "Disciplina": "Dir. Proc. Penal", "Temas": "Denuncia/Queixa; Competencia I/II; Prisao Flagrante."},
    {"Data": "16/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Prisao Preventiva; Temporaria; Cautelares."},
    {"Data": "17/03", "Hora": "12h-14h", "Disciplina": "Dir. Civil", "Temas": "Posse; Usucapiao; Familia; Sucessoes I/II; Resp. Civil."},
    {"Data": "17/03", "Hora": "20h-22h", "Disciplina": "Prova Discursiva", "Temas": "P3: Relatorio Final; Indiciamento."},
    {"Data": "18/03", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Conhecimentos DF; Politica Mulheres; Primeiros Socorros."},
    {"Data": "18/03", "Hora": "20h-22h", "Disciplina": "Dir. Humanos", "Temas": "Convencionalidade; DUDH; Pacto Civis."},
    {"Data": "19/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Criminalidade Economica; Medidas Patrimoniais."},
    {"Data": "19/03", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Preventiva/Domiciliar; Liberdade Provisoria; Temporaria."},
    {"Data": "20/03", "Hora": "12h-14h", "Disciplina": "Prova Discursiva", "Temas": "P3: Revisao Pecas; Estrategia de Prova."},
    {"Data": "20/03", "Hora": "20h-22h", "Disciplina": "Leg. Especial", "Temas": "Lei Organica Nacional das Policias Civis."},
    {"Data": "21/03", "Hora": "12h-14h", "Disciplina": "Dir. Empresarial", "Temas": "MEI/ME/EPP; Titulos de Credito; Falencia."},
    {"Data": "21/03", "Hora": "20h-22h", "Disciplina": "Dir. Humanos", "Temas": "Pacto Sociais; CADH; Comissao IDH."},
    {"Data": "22/03", "Hora": "12h-14h", "Disciplina": "Leg. Especial", "Temas": "Regime Disciplinar PF e PCDF (Lei 15.047/2024)."},
    {"Data": "22/03", "Hora": "20h-22h", "Disciplina": "Dir. Proc. Penal", "Temas": "Comunicacao; Procedimento; Provas; Recursos."},
    {"Data": "23/03", "Hora": "12h-14h", "Disciplina": "Dir. Humanos", "Temas": "Corte IDH; Casos Brasil; Povos Tradicionais; Empresas."}
]

# Inicialização do estado
if 'concluidos' not in st.session_state:
    st.session_state.concluidos = [False] * len(cronograma)

# Interface
st.title("🎯 PCDF - Delegado de Polícia | Mentor Digital")
st.markdown("---")

# Métricas
total = len(cronograma)
feitos = sum(st.session_state.concluidos)
progresso = feitos / total

c1, c2 = st.columns([1, 2])
with c1:
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = progresso * 100,
        title = {'text': "Progresso Geral (%)"},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#00CC96"}}
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Atividades do Cronograma")
    for i, item in enumerate(cronograma):
        with st.expander(f"{item['Data']} - {item['Disciplina']} {'✅' if st.session_state.concluidos[i] else '⏳'}"):
            st.write(f"**Hora:** {item['Hora']}")
            st.write(f"**Temas:** {item['Temas']}")
            st.session_state.concluidos[i] = st.checkbox("Marcar como concluído", value=st.session_state.concluidos[i], key=f"ch_{i}")
