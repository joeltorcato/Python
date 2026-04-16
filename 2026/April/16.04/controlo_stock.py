import ficheiros


def listar_stock():
    p = ficheiros.ler_produtos()
    s = ficheiros.ler_stock()
    return [(c, n, int(s.get(c, 0))) for c, (n, _) in sorted(p.items())]


def adicionar_stock(codigo, quantidade):
    q = int(quantidade)
    if q <= 0:
        raise ValueError("quantidade a adicionar deve ser positiva.")
    if codigo not in ficheiros.ler_produtos():
        raise ValueError("produto nao existe no catalogo.")
    s = ficheiros.ler_stock()
    s[codigo] = int(s.get(codigo, 0)) + q
    ficheiros.guardar_stock(s)


def reduzir_stock(codigo, quantidade):
    q = int(quantidade)
    if q <= 0:
        raise ValueError("quantidade a vender deve ser positiva.")
    if codigo not in ficheiros.ler_produtos():
        raise ValueError("produto nao existe no catalogo.")
    s = ficheiros.ler_stock()
    disp = int(s.get(codigo, 0))
    if disp < q:
        raise ValueError(f"stock insuficiente. disponivel: {disp}.")
    s[codigo] = disp - q
    ficheiros.guardar_stock(s)

