import os

FICHEIRO_RECEITAS = "receitas.txt"
receitas = []


def carregar_receitas():
    """Carrega as receitas existentes do ficheiro de texto."""
    if not os.path.exists(FICHEIRO_RECEITAS):
        return

    with open(FICHEIRO_RECEITAS, "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read().strip()

    if not conteudo:
        return

    blocos = conteudo.split("\n=== RECEITA ===\n")
    for bloco in blocos:
        if not bloco.strip():
            continue

        receita = {
            "nome": "",
            "ingredientes": [],
            "comentarios": [],
            "avaliacoes": [],
        }

        for linha in bloco.splitlines():
            if linha.startswith("Nome: "):
                receita["nome"] = linha.replace("Nome: ", "", 1).strip()
            elif linha.startswith("Ingredientes: "):
                ingredientes_texto = linha.replace("Ingredientes: ", "", 1)
                receita["ingredientes"] = [item.strip() for item in ingredientes_texto.split(",") if item.strip()]
            elif linha.startswith("Comentarios: "):
                comentarios_texto = linha.replace("Comentarios: ", "", 1)
                receita["comentarios"] = [item.strip() for item in comentarios_texto.split(" | ") if item.strip() and item.strip() != "<sem comentário>"]
            elif linha.startswith("Avaliacoes: "):
                avaliacoes_texto = linha.replace("Avaliacoes: ", "", 1)
                for avaliacao in avaliacoes_texto.split(","):
                    avaliacao = avaliacao.strip()
                    if avaliacao:
                        try:
                            receita["avaliacoes"].append(float(avaliacao))
                        except ValueError:
                            pass

        receitas.append(receita)


def salvar_receitas():
    #Salva todas as receitas no ficheiro de texto.
    with open(FICHEIRO_RECEITAS, "w", encoding="utf-8") as ficheiro:
        for receita in receitas:
            ficheiro.write("=== RECEITA ===\n")
            ficheiro.write(f"Nome: {receita['nome']}\n")
            ficheiro.write(f"Ingredientes: {', '.join(receita['ingredientes'])}\n")
            comentario_texto = " | ".join(receita["comentarios"]) if receita["comentarios"] else "<sem comentário>"
            ficheiro.write(f"Comentarios: {comentario_texto}\n")
            avaliacoes_texto = ", ".join(str(av) for av in receita["avaliacoes"]) if receita["avaliacoes"] else ""
            ficheiro.write(f"Avaliacoes: {avaliacoes_texto}\n")
            ficheiro.write("\n")


def obter_receita_por_nome(nome_receita):
    """Retorna a receita com o nome exato ou None se não existir."""
    for receita in receitas:
        if receita["nome"].lower() == nome_receita.lower():
            return receita
    return None


def adicionar_receita(nome_receita, ingredientes, comentario=None, avaliacao=None):
    """Adiciona uma nova receita e grava no ficheiro."""
    if not nome_receita.strip():
        print("Erro: o nome da receita não pode ficar vazio.")
        return False

    if not ingredientes:
        print("Erro: a receita deve ter pelo menos um ingrediente.")
        return False

    if obter_receita_por_nome(nome_receita):
        print("Erro: já existe uma receita com esse nome.")
        return False

    nova_receita = {
        "nome": nome_receita.strip(),
        "ingredientes": [item.strip() for item in ingredientes if item.strip()],
        "comentarios": [],
        "avaliacoes": [],
    }

    if comentario and comentario.strip():
        nova_receita["comentarios"].append(comentario.strip())

    if avaliacao is not None:
        nova_receita["avaliacoes"].append(avaliacao)

    receitas.append(nova_receita)
    salvar_receitas()
    return True


def pesquisar_receita(palavra_chave):
    """Retorna a lista de receitas que correspondem à palavra-chave."""
    chave = palavra_chave.strip().lower()
    resultados = []

    for receita in receitas:
        if chave in receita["nome"].lower():
            resultados.append(receita)
            continue

        if any(chave in ingrediente.lower() for ingrediente in receita["ingredientes"]):
            resultados.append(receita)
            continue

        if any(chave in comentario.lower() for comentario in receita["comentarios"]):
            resultados.append(receita)
            continue

    return resultados


def remover_receita(nome_receita):
    #Remove uma receita e atualiza o ficheiro.
    receita = obter_receita_por_nome(nome_receita)
    if receita:
        receitas.remove(receita)
        salvar_receitas()
        return True
    return False


def atualizar_receita(nome_receita, novos_ingredientes=None, novo_comentario=None, nova_avaliacao=None):
    """Atualiza dados de uma receita existente."""
    receita = obter_receita_por_nome(nome_receita)
    if not receita:
        return False

    if novos_ingredientes is not None and novos_ingredientes:
        receita["ingredientes"] = [item.strip() for item in novos_ingredientes if item.strip()]

    if novo_comentario and novo_comentario.strip():
        receita["comentarios"].append(novo_comentario.strip())

    if nova_avaliacao is not None:
        receita["avaliacoes"].append(nova_avaliacao)

    salvar_receitas()
    return True