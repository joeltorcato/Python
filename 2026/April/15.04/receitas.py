import os

ficheiro_receitas = "receitas.txt"
receitas = []


def carregar_receitas():
    receitas.clear()
    if not os.path.exists(ficheiro_receitas):
        return
    txt = open(ficheiro_receitas, "r", encoding="utf-8").read()
    txt = (txt or "").replace("\r\n", "\n").strip()
    if not txt:
        return
    t = txt.lower()
    blocos = t.split("=== receita ===")
    for bloco in blocos:
        bloco = bloco.strip()
        if not bloco:
            continue
        r = {"nome": "", "ingredientes": [], "comentarios": [], "avaliacoes": []}
        for linha in bloco.splitlines():
            linha = linha.strip()
            if linha.startswith("nome:"):
                r["nome"] = linha.split("nome:", 1)[1].strip()
            elif linha.startswith("ingredientes:"):
                x = linha.split("ingredientes:", 1)[1].strip()
                r["ingredientes"] = [i.strip() for i in x.split(",") if i.strip()]
            elif linha.startswith("comentarios:"):
                x = linha.split("comentarios:", 1)[1].strip()
                if x and not x.startswith("<sem"):
                    r["comentarios"] = [c.strip() for c in x.split(" | ") if c.strip()]
            elif linha.startswith("avaliacoes:"):
                x = linha.split("avaliacoes:", 1)[1].strip()
                if x:
                    for av in x.split(","):
                        av = av.strip()
                        if not av:
                            continue
                        try:
                            r["avaliacoes"].append(float(av))
                        except:
                            pass
        if r["nome"]:
            receitas.append(r)


def salvar_receitas():
    with open(ficheiro_receitas, "w", encoding="utf-8", newline="") as f:
        for r in receitas:
            f.write("=== receita ===\n")
            f.write(f"nome: {r['nome']}\n")
            f.write(f"ingredientes: {', '.join(r['ingredientes'])}\n")
            c = " | ".join(r["comentarios"]) if r["comentarios"] else "<sem comentário>"
            f.write(f"comentarios: {c}\n")
            a = ", ".join(str(x) for x in r["avaliacoes"]) if r["avaliacoes"] else ""
            f.write(f"avaliacoes: {a}\n\n")


def obter_receita_por_nome(nome):
    n = (nome or "").strip().lower()
    for r in receitas:
        if r["nome"] == n:
            return r
    return None


def adicionar_receita(nome_receita, ingredientes, comentario=None, avaliacao=None):
    nome = (nome_receita or "").strip().lower()
    if not nome:
        print("erro: o nome da receita nao pode ficar vazio.")
        return False
    ing = [(i or "").strip().lower() for i in ingredientes or []]
    ing = [i for i in ing if i]
    if not ing:
        print("erro: a receita deve ter pelo menos um ingrediente.")
        return False
    if obter_receita_por_nome(nome):
        print("erro: ja existe uma receita com esse nome.")
        return False
    r = {"nome": nome, "ingredientes": ing, "comentarios": [], "avaliacoes": []}
    if comentario is not None:
        c = (comentario or "").strip().lower()
        if c:
            r["comentarios"].append(c)
    if avaliacao is not None:
        try:
            r["avaliacoes"].append(float(avaliacao))
        except:
            pass
    receitas.append(r)
    salvar_receitas()
    return True


def pesquisar_receita(palavra_chave):
    chave = (palavra_chave or "").strip().lower()
    if not chave:
        return []
    res = []
    for r in receitas:
        if chave in r["nome"]:
            res.append(r)
            continue
        if any(chave in i for i in r["ingredientes"]):
            res.append(r)
            continue
        if any(chave in c for c in r["comentarios"]):
            res.append(r)
            continue
    return res


def remover_receita(nome_receita):
    r = obter_receita_por_nome(nome_receita)
    if not r:
        return False
    receitas.remove(r)
    salvar_receitas()
    return True


def atualizar_receita(nome_receita, novos_ingredientes=None, novo_comentario=None, nova_avaliacao=None):
    r = obter_receita_por_nome(nome_receita)
    if not r:
        return False
    if novos_ingredientes is not None:
        ing = [(i or "").strip().lower() for i in novos_ingredientes or []]
        ing = [i for i in ing if i]
        if ing:
            r["ingredientes"] = ing
    if novo_comentario is not None:
        c = (novo_comentario or "").strip().lower()
        if c:
            r["comentarios"].append(c)
    if nova_avaliacao is not None:
        try:
            r["avaliacoes"].append(float(nova_avaliacao))
        except:
            pass
    salvar_receitas()
    return True