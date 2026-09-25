# SIDA Lab 0.2

Segunda versão do laboratório funcional do SIDA/ELÚCIDA.

## Mudança principal
A 0.1 demonstrava comportamentos com lógica fortemente ligada às matrículas de teste.  
A 0.2 separa:
- dados dos casos (`data_cases.py`);
- regras (`rules.py`);
- motor (`engine.py`);
- interface (`app.py`).

O motor recebe fatos estruturados e aplica o tipo de regra configurado, preservando evidências, lacunas, conflitos e trilha de decisão.

## Casos
- TESTE001 / 2023 — saúde: 30+45+45 = 120; média 80+90 = 85.
- TESTE002 / 2023 — TIP/LAC 90 dias; avaliação normal no cenário homologado.
- TESTE003 / 2024 — mudança de unidade após Acompanhamento; responsabilidade ADI preservada no cenário.
- TESTE004 / 2022 — conflito 100 x 0; conclusão bloqueada.
- TESTE005 / 2024 — exceção; análise humana.

## Princípios
- localizar != validar != concluir
- não localizado != inexistente
- posteridade != prevalência
- código e nota são campos distintos
- proveniência por evidência
- decisão humana preservada

**Somente dados fictícios. Não inserir credenciais ou dados pessoais reais no repositório público.**
