import streamlit as st
from engine import investigar

st.set_page_config(page_title="SIDA Lab 0.1", page_icon="🔎", layout="wide")
st.title("SIDA Lab 0.1")
st.caption("Motor de Investigação Administrativa — protótipo com dados fictícios")

with st.sidebar:
    st.header("Investigação")
    matricula = st.text_input("Matrícula", "TESTE001")
    exercicio = st.selectbox("Exercício", list(range(2025, 2018, -1)), index=2)
    executar = st.button("INVESTIGAR", type="primary", use_container_width=True)
    st.caption("Testes: TESTE001/2023, TESTE004/2022 e TESTE005/2024.")

if executar:
    r = investigar(matricula.strip().upper(), exercicio)
    if not r:
        st.error("Caso não localizado na base de testes.")
        st.stop()

    st.subheader(f"{r['servidor']} — {r['matricula']}")
    st.write(f"**Exercício:** {r['exercicio']}")
    cols = st.columns(5)
    for col, (nome, status) in zip(cols, r["etapas"].items()):
        col.metric(nome, status)

    st.divider()
    a, b = st.columns(2)
    with a:
        st.subheader("Linha funcional")
        for x in r["linha_funcional"]:
            st.write(f"**{x['periodo']}** — {x['evento']}  \nFonte: `{x['fonte']}`")
        st.subheader("Notas / códigos")
        st.dataframe(r["notas"], use_container_width=True, hide_index=True)
    with b:
        st.subheader("Evidências")
        for x in r["evidencias"]:
            st.write(f"- **{x['status']}** — {x['descricao']} — `{x['fonte']}`")
        st.subheader("Regra aplicada")
        st.info(r["regra"])
        if r["lacunas"]:
            st.subheader("Lacunas / conflitos")
            for x in r["lacunas"]:
                st.warning(x)

    st.divider()
    st.subheader("Diagnóstico")
    status, texto = r["diagnostico"]["status"], r["diagnostico"]["texto"]
    if status == "CONFIRMADO":
        st.success(f"{status} — {texto}")
    elif status == "ANÁLISE HUMANA":
        st.error(f"{status} — {texto}")
    else:
        st.warning(f"{status} — {texto}")
    st.caption("Princípio: localizar ≠ validar ≠ concluir.")
else:
    st.info("Comece com TESTE001 / 2023 e clique em INVESTIGAR.")
