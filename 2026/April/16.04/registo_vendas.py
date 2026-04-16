from datetime import date as dt
from decimal import Decimal as d

import ficheiros
from controlo_stock import reduzir_stock
from registo_produtos import obter_produto


def registar_venda(codigo, quantidade, data_iso=None):
    q = int(quantidade)
    if q <= 0:
        raise ValueError("quantidade a vender deve ser positiva.")
    nome, preco_unitario = obter_produto(codigo)
    if data_iso is None:
        data_iso = dt.today().isoformat()
    reduzir_stock(codigo, q)
    total = preco_unitario * d(q)
    ficheiros.append_venda(data_iso, codigo, nome, q, preco_unitario, total)
    return total


def total_vendas_dia(data_iso):
    t = d("0.00")
    for v in ficheiros.ler_vendas():
        if v["data"] == data_iso:
            t += v["total"]
    return t


def listar_vendas_dia(data_iso):
    return [v for v in ficheiros.ler_vendas() if v["data"] == data_iso]

