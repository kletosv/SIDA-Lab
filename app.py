import streamlit as st
from engine import investigar
from data_cases import CASOS

st.set_page_config(page_title="SIDA Lab 0.2", page_icon="🔎", layout="wide")
st.title("SIDA Lab 0.2")
st.caption("Motor de Investigação Administrativa — laboratório com dados fictícios")

with st.sidebar:
    st.header("Investigação")
    matricula = st.text_input("Matrícula", "TESTE001").strip().upper()
    exercicio = st.selectbox("Exercício", list(range(2026, 2016, -1)), index=3)
    executar = st.button("INVESTIGAR", type="primary", use_container_width=True)
    st.divider()
    st.caption("Casos: TESTE001/2023, TESTE002/2023, TESTE003/2024, TESTE004/2022 e TESTE005/2024.")
    st.caption("Somente dados fictícios. Não inserir dados pessoais reais.")

if executar:
    r = investigar(matricula, exercicio)
    if not r:
        st.error("Matrícula não localizada na base fictícia.")
        st.stop()

    st.subheader(f"{r['servidor']} — {r['matricula']}")
    st.write(f"**Exercício analisado:** {r['exercicio']}")

    cols = st.columns(5)
    for col, (nome, status) in zip(cols, r["etapas"].items()):
        col.metric(nome, status)

    st.divider()
    t1, t2, t3, t4 = st.tabs(["Investigação", "Linha temporal", "Evidências", "Auditoria"])

    with t1:
        a, b = st.columns(2)
        with a:
            st.subheader("Retrato funcional")
            for k, v in r["retrato"].items():
                st.write(f"**{k}:** {v}")
            st.subheader("Notas / códigos")
            st.dataframe(r["notas"], use_container_width=True, hide_index=True)
        with b:
            st.subheader("Regra / enquadramento")
            st.info(r["regra"])
            st.subheader("Diagnóstico")
            status = r["diagnostico"]["status"]
            texto = r["diagnostico"]["texto"]
            if status == "CONFIRMADO":
                st.success(f"{status} — {texto}")
            elif status == "ANÁLISE HUMANA":
                st.error(f"{status} — {texto}")
            else:
                st.warning(f"{status} — {texto}")
            if r["lacunas"]:
                st.subheader("Lacunas / conflitos")
                for x in r["lacunas"]:
                    st.warning(x)

    with t2:
        st.subheader("Linha funcional / temporal")
        st.dataframe(r["linha_funcional"], use_container_width=True, hide_index=True)
        st.caption("Datas de fato, efeito/vigência, ato e publicação devem permanecer distintas quando disponíveis.")

    with t3:
        st.subheader("Proveniência por evidência")
        st.dataframe(r["evidencias"], use_container_width=True, hide_index=True)
        st.caption("LOCALIZADO ≠ VALIDADO ≠ CONCLUÍDO. Não localizado também não significa inexistente.")

    with t4:
        st.subheader("Trilha de decisão")
        for i, passo in enumerate(r["trilha"], 1):
            st.write(f"**{i}.** {passo}")
        st.subheader("Busca adversarial")
        st.write(r["busca_adversarial"])
        st.subheader("Estado da conclusão")
        st.write(r["estado_conclusao"])

    st.divider()
    st.caption("SIDA Lab 0.2 — o motor organiza evidências e aplica somente regras configuradas. Exceções e conflitos podem bloquear a conclusão.")

else:
    st.info("Comece com TESTE001 / 2023 e clique em INVESTIGAR.")
