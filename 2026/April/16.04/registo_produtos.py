import ficheiros


def obter_produto(codigo):
    p = ficheiros.ler_produtos()
    if codigo not in p:
        raise ValueError("produto nao existe no catalogo.")
    return p[codigo]


def listar_produtos():
    p = ficheiros.ler_produtos()
    return [(c, n, pre) for c, (n, pre) in sorted(p.items())]


def registar_produto(codigo, nome, preco, stock_inicial):
    p = ficheiros.ler_produtos()
    if codigo in p:
        raise ValueError("codigo ja existe no catalogo. use atualizacao de preco ou selecione outro codigo.")
    p[codigo] = (nome, preco)
    ficheiros.guardar_produtos(p)
    s = ficheiros.ler_stock()
    s[codigo] = int(stock_inicial)
    ficheiros.guardar_stock(s)


def atualizar_preco(codigo, novo_preco):
    p = ficheiros.ler_produtos()
    if codigo not in p:
        raise ValueError("produto nao existe no catalogo.")
    nome, _ = p[codigo]
    p[codigo] = (nome, novo_preco)
    ficheiros.guardar_produtos(p)

