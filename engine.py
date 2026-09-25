from data_cases import CASOS
from rules import REGRAS

def _media(vals):
    return sum(vals) / len(vals) if vals else None

def _base(c, matricula, exercicio):
    return {
        "servidor": c["servidor"],
        "matricula": matricula,
        "exercicio": exercicio,
        "retrato": c.get("retrato", {}),
        "linha_funcional": c.get("linha_funcional", []),
        "notas": c.get("notas", []),
        "evidencias": c.get("evidencias", []),
        "lacunas": list(c.get("lacunas", [])),
        "trilha": [],
        "busca_adversarial": "Nenhum conflito adicional configurado no cenário fictício.",
        "estado_conclusao": "",
    }

def investigar(matricula, exercicio):
    c = CASOS.get(matricula)
    if not c:
        return None
    r = _base(c, matricula, exercicio)

    r["trilha"].append("Identidade localizada na base fictícia.")
    if not c.get("vinculo_ativo", False):
        r["etapas"] = {"Identidade":"OK","Vínculo":"PENDENTE","Elegibilidade":"PENDENTE","Evidências":"INCOMPLETAS","Conclusão":"BLOQUEADA"}
        r["regra"] = "Sem vínculo confirmado, a investigação não avança para notas/códigos."
        r["diagnostico"] = {"status":"PENDENTE","texto":"Vínculo não confirmado."}
        r["estado_conclusao"] = "Bloqueada pelo portão de vínculo."
        return r

    r["trilha"].append("Vínculo confirmado para o cenário.")
    if not c.get("elegivel", False):
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"NÃO","Evidências":"N/A","Conclusão":"BLOQUEADA"}
        r["regra"] = "Portão de elegibilidade: investigar notas somente quando o vínculo integrar o universo avaliável."
        r["diagnostico"] = {"status":"PENDENTE","texto":"NÃO ESPERADO PELA REGRA para este vínculo/exercício."}
        r["estado_conclusao"] = "Encerrada no portão de elegibilidade."
        return r

    r["trilha"].append("Elegibilidade confirmada.")
    if exercicio != c["exercicio"]:
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"PENDENTE","Evidências":"PENDENTES","Conclusão":"BLOQUEADA"}
        r["regra"] = "Não há cenário de regressão configurado para este exercício."
        r["diagnostico"] = {"status":"PENDENTE","texto":"Exercício fora do cenário configurado."}
        r["estado_conclusao"] = "Bloqueada por ausência de dados do exercício."
        return r

    tipo = c["tipo_caso"]

    if tipo == "saude":
        dias = sum(x["dias"] for x in c["afastamentos"] if x["natureza"] == "saude")
        r["trilha"].append(f"Somados apenas afastamentos de saúde do ciclo: {dias} dias.")
        if dias >= 120 and len(c["notas_homologadas_anteriores"]) >= 2:
            vals = c["notas_homologadas_anteriores"][-2:]
            media = _media(vals)
            reg = REGRAS["SAUDE_120"]
            r["regra"] = f"{reg['id']}: {reg['descricao']}"
            r["diagnostico"] = {"status":"CONFIRMADO","texto":f"Total de {dias} dias. Média das duas últimas notas homologadas ({vals[0]:.2f} e {vals[1]:.2f}) = {media:.2f}."}
            r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"COMPLETAS","Conclusão":"PERMITIDA"}
            r["trilha"] += ["Regra de 120 dias acionada.", "Duas notas homologadas anteriores localizadas.", f"Cálculo executado: {media:.2f}."]
            r["estado_conclusao"] = "Conclusão automática permitida no cenário."
        else:
            r["regra"] = "Regra de saúde não pôde ser concluída."
            r["diagnostico"] = {"status":"PENDENTE","texto":"Faltam requisito temporal ou duas notas homologadas anteriores."}
            r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"INCOMPLETAS","Conclusão":"BLOQUEADA"}
            r["estado_conclusao"] = "Bloqueada por insuficiência de evidências."

    elif tipo == "tip_lac":
        dias = sum(x["dias"] for x in c["afastamentos"] if x["natureza"] == "tip_lac")
        reg = REGRAS["TIP_LAC_NORMAL"]
        r["regra"] = f"{reg['id']}: {reg['descricao']}"
        r["diagnostico"] = {"status":"CONFIRMADO","texto":f"TIP/LAC registrado por {dias} dias no cenário; avaliação normal preservada. Resultado: {c['resultado']}."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"COMPLETAS","Conclusão":"PERMITIDA"}
        r["trilha"] += [f"TIP/LAC identificado: {dias} dias.", "Cenário enquadrado abaixo do limite configurado.", "Avaliação normal preservada."]
        r["estado_conclusao"] = "Conclusão automática permitida no cenário."

    elif tipo == "gestor":
        reg = REGRAS["GESTOR_ADI"]
        r["regra"] = f"{reg['id']}: {reg['descricao']}"
        r["diagnostico"] = {"status":"CONFIRMADO","texto":"Mudança de unidade posterior ao Acompanhamento não altera, neste cenário, o responsável pela ADI: permanece o gestor que realizou o Acompanhamento."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"COMPLETAS","Conclusão":"PERMITIDA"}
        r["trilha"] += ["Acompanhamento identificado antes da mudança.", "Mudança de unidade identificada.", "Responsabilidade da ADI mantida conforme regra configurada."]
        r["estado_conclusao"] = "Conclusão automática permitida no cenário."

    elif tipo == "conflito":
        reg = REGRAS["VERSOES"]
        r["regra"] = f"{reg['id']}: {reg['descricao']}"
        r["diagnostico"] = {"status":"PENDENTE","texto":"DIVERGÊNCIA NÃO RESOLVIDA: há resultados conflitantes e nenhuma relação documental entre as versões."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"CONFLITO","Conclusão":"BLOQUEADA"}
        r["trilha"] += ["Duas publicações preservadas.", "Nenhuma delas foi descartada pela data.", "Ausência de retificação/substituição/anulação impede prevalência automática."]
        r["busca_adversarial"] = "O cenário procura ato de RETIFICAÇÃO, LEIA-SE, ONDE SE LÊ, TORNA SEM EFEITO, SUBSTITUIÇÃO, ALTERAÇÃO ou REPUBLICAÇÃO; nenhum foi configurado."
        r["estado_conclusao"] = "Bloqueada por conflito documental."

    elif tipo == "humana":
        reg = REGRAS["HUMANA"]
        r["regra"] = f"{reg['id']}: {reg['descricao']}"
        r["diagnostico"] = {"status":"ANÁLISE HUMANA","texto":"Evidências organizadas, mas a decisão automática está bloqueada para este enquadramento excepcional."}
        r["etapas"] = {"Identidade":"OK","Vínculo":"OK","Elegibilidade":"OK","Evidências":"COMPLETAS","Conclusão":"HUMANA"}
        r["trilha"] += ["Situação excepcional identificada.", "Evidências suficientes para caracterizar o cenário.", "Motor interrompe a decisão e encaminha para análise humana."]
        r["estado_conclusao"] = "Decisão reservada à análise humana."

    return r
