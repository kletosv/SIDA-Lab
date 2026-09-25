CASOS = {
"TESTE001": {
 "servidor":"Servidor Teste 001",
 "afastamentos_saude":[30,45,45], "notas_homologadas_anteriores":[80.0,90.0],
 "linha_funcional":[{"periodo":"2023","evento":"Vínculo ativo no cenário de teste","fonte":"BASE_FICTICIA"},{"periodo":"2023","evento":"Afastamentos de saúde: 30 + 45 + 45 dias","fonte":"BASE_FICTICIA"}],
 "notas":[{"Exercício":2021,"Resultado":"80,00","Situação":"Homologada"},{"Exercício":2022,"Resultado":"90,00","Situação":"Homologada"},{"Exercício":2023,"Resultado":"0,00","Situação":"Objeto da investigação"}],
 "evidencias":[{"status":"CONFIRMADA","descricao":"Vínculo do cenário","fonte":"BASE_FICTICIA"},{"status":"CONFIRMADA","descricao":"Três afastamentos por saúde","fonte":"BASE_FICTICIA"},{"status":"CONFIRMADA","descricao":"Notas anteriores 80,00 e 90,00","fonte":"BASE_FICTICIA"}], "lacunas":[]},
"TESTE004": {
 "servidor":"Ana Teste",
 "linha_funcional":[{"periodo":"2022","evento":"Vínculo ativo","fonte":"BASE_FICTICIA"}],
 "notas":[{"Exercício":2022,"Resultado":"100,00","Situação":"Publicação A"},{"Exercício":2022,"Resultado":"0,00","Situação":"Publicação B"}],
 "evidencias":[{"status":"CONFIRMADA","descricao":"Publicação A = 100,00","fonte":"DOE_FICTICIO_A"},{"status":"CONFIRMADA","descricao":"Publicação B = 0,00","fonte":"DOE_FICTICIO_B"}],
 "lacunas":["Não foi localizado ato que estabeleça retificação, substituição ou anulação entre as publicações."]},
"TESTE005": {
 "servidor":"Helena Teste",
 "linha_funcional":[{"periodo":"2024","evento":"Situação funcional excepcional","fonte":"BASE_FICTICIA"}],
 "notas":[{"Exercício":2024,"Resultado":"—","Situação":"Análise necessária"}],
 "evidencias":[{"status":"CONFIRMADA","descricao":"Situação funcional excepcional identificada","fonte":"BASE_FICTICIA"}], "lacunas":[]}
}
