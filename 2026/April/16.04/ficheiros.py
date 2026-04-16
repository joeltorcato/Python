import csv
import os
from decimal import Decimal as d
from decimal import InvalidOperation as io

delim = ";"
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, "dados")
produtos_path = os.path.join(data_dir, "produtos.txt")
stock_path = os.path.join(data_dir, "stock.txt")
vendas_path = os.path.join(data_dir, "vendas.txt")


def init_arquivos():
    os.makedirs(data_dir, exist_ok=True)
    if not os.path.exists(produtos_path):
        with open(produtos_path, "w", encoding="utf-8", newline="") as f:
            f.write(f"codigo{delim}nome{delim}preco\n")
    if not os.path.exists(stock_path):
        with open(stock_path, "w", encoding="utf-8", newline="") as f:
            f.write(f"codigo{delim}quantidade\n")
    if not os.path.exists(vendas_path):
        with open(vendas_path, "w", encoding="utf-8", newline="") as f:
            f.write(f"data{delim}codigo{delim}nome{delim}quantidade{delim}preco_unitario{delim}total\n")


def parse_decimal(x):
    s = str(x).strip().replace(",", ".")
    try:
        return d(s).quantize(d("0.01"))
    except io as e:
        raise ValueError("preco invalido") from e


def parse_int(x):
    try:
        return int(str(x).strip())
    except ValueError as e:
        raise ValueError("quantidade invalida") from e


def ler_produtos():
    init_arquivos()
    r = {}
    with open(produtos_path, "r", encoding="utf-8", newline="") as f:
        for row in csv.reader(f, delimiter=delim):
            if not row or row[0].strip().lower() == "codigo":
                continue
            if len(row) < 3:
                continue
            c = row[0].strip()
            n = row[1].strip()
            p = parse_decimal(row[2])
            r[c] = (n, p)
    return r


def guardar_produtos(produtos):
    init_arquivos()
    linhas = []
    for c in sorted(produtos.keys()):
        n, p = produtos[c]
        linhas.append([c, n, f"{p.quantize(d('0.01')):.2f}"])
    with open(produtos_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=delim)
        w.writerow(["codigo", "nome", "preco"])
        w.writerows(linhas)


def ler_stock():
    init_arquivos()
    r = {}
    with open(stock_path, "r", encoding="utf-8", newline="") as f:
        for row in csv.reader(f, delimiter=delim):
            if not row or row[0].strip().lower() == "codigo":
                continue
            if len(row) < 2:
                continue
            c = row[0].strip()
            q = parse_int(row[1])
            r[c] = q
    return r


def guardar_stock(stock):
    init_arquivos()
    linhas = []
    for c in sorted(stock.keys()):
        linhas.append([c, str(int(stock[c]))])
    with open(stock_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=delim)
        w.writerow(["codigo", "quantidade"])
        w.writerows(linhas)


def ler_vendas():
    init_arquivos()
    r = []
    with open(vendas_path, "r", encoding="utf-8", newline="") as f:
        for row in csv.reader(f, delimiter=delim):
            if not row or row[0].strip().lower() == "data":
                continue
            if len(row) < 6:
                continue
            r.append(
                {
                    "data": row[0].strip(),
                    "codigo": row[1].strip(),
                    "nome": row[2].strip(),
                    "quantidade": parse_int(row[3]),
                    "preco_unitario": parse_decimal(row[4]),
                    "total": parse_decimal(row[5]),
                }
            )
    return r


def append_venda(data, codigo, nome, quantidade, preco_unitario, total):
    init_arquivos()
    linha = delim.join(
        [
            str(data),
            str(codigo),
            str(nome),
            str(int(quantidade)),
            f"{preco_unitario.quantize(d('0.01')):.2f}",
            f"{total.quantize(d('0.01')):.2f}",
        ]
    )
    with open(vendas_path, "a", encoding="utf-8", newline="") as f:
        f.write(linha + "\n")


def format_moeda(x):
    return f"{parse_decimal(x):.2f}"

