CASOS = {
"TESTE001":{
 "servidor":"Servidor Teste 001","exercicio":2023,"tipo_caso":"saude","vinculo_ativo":True,"elegivel":True,
 "retrato":{"Vínculo":"Ativo","Condição":"Elegível no cenário","Unidade":"Unidade fictícia A","Função":"Cargo fictício"},
 "afastamentos":[{"natureza":"saude","dias":30},{"natureza":"saude","dias":45},{"natureza":"saude","dias":45}],
 "notas_homologadas_anteriores":[80.0,90.0],
 "linha_funcional":[
  {"Fato":"Afastamento saúde","Efeito/Vigência":"2023-02-01 a 2023-03-02","Ato":"ATO-FICT-01","Publicação":"PUB-FICT-01"},
  {"Fato":"Afastamento saúde","Efeito/Vigência":"2023-05-01 a 2023-06-14","Ato":"ATO-FICT-02","Publicação":"PUB-FICT-02"},
  {"Fato":"Afastamento saúde","Efeito/Vigência":"2023-08-01 a 2023-09-14","Ato":"ATO-FICT-03","Publicação":"PUB-FICT-03"}],
 "notas":[{"Exercício":2021,"Resultado":"80,00","Código":"—","Estado":"Homologada"},{"Exercício":2022,"Resultado":"90,00","Código":"—","Estado":"Homologada"},{"Exercício":2023,"Resultado":"0,00","Código":"—","Estado":"Objeto da investigação"}],
 "evidencias":[{"Campo":"Vínculo","Valor":"Ativo","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"},{"Campo":"Afastamentos saúde","Valor":"30+45+45","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"},{"Campo":"Notas anteriores","Valor":"80,00 / 90,00","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"}],"lacunas":[]},

"TESTE002":{
 "servidor":"Maria Teste","exercicio":2023,"tipo_caso":"tip_lac","vinculo_ativo":True,"elegivel":True,"resultado":"92,50",
 "retrato":{"Vínculo":"Ativo","Condição":"Elegível no cenário","Unidade":"Unidade fictícia B","Função":"Cargo fictício"},
 "afastamentos":[{"natureza":"tip_lac","dias":90}],
 "linha_funcional":[{"Fato":"TIP/LAC","Efeito/Vigência":"90 dias no ciclo","Ato":"ATO-FICT-TIP","Publicação":"PUB-FICT-TIP"}],
 "notas":[{"Exercício":2023,"Resultado":"92,50","Código":"—","Estado":"Avaliação normal"}],
 "evidencias":[{"Campo":"TIP/LAC","Valor":"90 dias","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"},{"Campo":"Resultado","Valor":"92,50","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"}],"lacunas":[]},

"TESTE003":{
 "servidor":"Carlos Teste","exercicio":2024,"tipo_caso":"gestor","vinculo_ativo":True,"elegivel":True,
 "retrato":{"Vínculo":"Ativo","Condição":"Elegível no cenário","Mudança":"Unidade após Acompanhamento","Fase":"ADI"},
 "linha_funcional":[{"Fato":"Acompanhamento realizado","Efeito/Vigência":"Antes da mudança","Ato":"REG-FICT-ACOMP","Publicação":"N/A"},{"Fato":"Mudança de unidade","Efeito/Vigência":"Posterior ao Acompanhamento","Ato":"ATO-FICT-MUD","Publicação":"PUB-FICT-MUD"}],
 "notas":[{"Exercício":2024,"Resultado":"—","Código":"—","Estado":"Responsabilidade em análise"}],
 "evidencias":[{"Campo":"Acompanhamento","Valor":"Realizado pelo gestor anterior","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"},{"Campo":"Mudança de unidade","Valor":"Posterior","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"}],"lacunas":[]},

"TESTE004":{
 "servidor":"Ana Teste","exercicio":2022,"tipo_caso":"conflito","vinculo_ativo":True,"elegivel":True,
 "retrato":{"Vínculo":"Ativo","Condição":"Elegível no cenário","Conflito documental":"Sim"},
 "linha_funcional":[{"Fato":"Publicação A","Efeito/Vigência":"2022","Ato":"ATO-A","Publicação":"DOE_FICTICIO_A"},{"Fato":"Publicação B","Efeito/Vigência":"2022","Ato":"ATO-B","Publicação":"DOE_FICTICIO_B"}],
 "notas":[{"Exercício":2022,"Resultado":"100,00","Código":"—","Estado":"Publicação A"},{"Exercício":2022,"Resultado":"0,00","Código":"—","Estado":"Publicação B"}],
 "evidencias":[{"Campo":"Resultado","Valor":"100,00","Fonte":"DOE_FICTICIO_A","Estado":"CONFIRMADO"},{"Campo":"Resultado","Valor":"0,00","Fonte":"DOE_FICTICIO_B","Estado":"CONFIRMADO"}],
 "lacunas":["Não localizado ato que relacione as duas publicações."]},

"TESTE005":{
 "servidor":"Helena Teste","exercicio":2024,"tipo_caso":"humana","vinculo_ativo":True,"elegivel":True,
 "retrato":{"Vínculo":"Ativo","Condição":"Elegível no cenário","Enquadramento":"Exceção configurada para análise humana"},
 "linha_funcional":[{"Fato":"Situação funcional excepcional","Efeito/Vigência":"2024","Ato":"ATO-FICT-EXC","Publicação":"PUB-FICT-EXC"}],
 "notas":[{"Exercício":2024,"Resultado":"—","Código":"—","Estado":"Análise humana"}],
 "evidencias":[{"Campo":"Situação excepcional","Valor":"Identificada","Fonte":"BASE_FICTICIA","Estado":"CONFIRMADO"}],"lacunas":[]}
}
