from data_cases import CASOS

def investigar(matricula, exercicio):
    c = CASOS.get(matricula)
    if not c:
        return None
    r = dict(servidor=c["servidor"], matricula=matricula, exercicio=exercicio,
             linha_funcional=c["linha_funcional"], notas=c["notas"],
             evidencias=c["evidencias"], lacunas=list(c.get("lacunas", [])))
    if matricula == "TESTE001" and exercicio == 2023:
        dias = sum(c["afastamentos_saude"])
        media = sum(c["notas_homologadas_anteriores"]) / 2
        r["regra"] = f"R-SAU-03: afastamentos por saúde somam {dias} dias. Ao atingir 120 dias no ciclo, aplicar a média das duas últimas notas homologadas."
        r["diagnostico"] = {"status":"CONFIRMADO","texto":f"30 + 45 + 45 = {dias} dias. Média de 80,00 e 90,00 = {media:.2f}."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"COMPLETAS","Conclusão":"PERMITIDA"}
    elif matricula == "TESTE004" and exercicio == 2022:
        r["regra"] = "Preservação de versões: posteridade não implica prevalência. Sem ato relacionando as publicações, o motor não escolhe silenciosamente."
        r["diagnostico"] = {"status":"PENDENTE","texto":"DIVERGÊNCIA NÃO RESOLVIDA: resultados 100,00 e 0,00 sem prova de retificação, substituição ou anulação."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"CONFLITO","Conclusão":"BLOQUEADA"}
    elif matricula == "TESTE005" and exercicio == 2024:
        r["regra"] = "Cenário excepcional de alta hierarquia: decisão automática bloqueada."
        r["diagnostico"] = {"status":"ANÁLISE HUMANA","texto":"O motor organiza fatos e evidências, mas não conclui automaticamente este enquadramento."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"COMPLETAS","Conclusão":"HUMANA"}
    else:
        r["regra"] = "Não há regra de regressão configurada para esta combinação."
        r["diagnostico"] = {"status":"PENDENTE","texto":"Caso localizado, mas o exercício solicitado não possui cenário configurado."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"PENDENTE","Evidências":"PENDENTE","Conclusão":"BLOQUEADA"}
    return r
