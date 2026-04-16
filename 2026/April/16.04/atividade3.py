from datetime import date as dt
from decimal import Decimal as d

import ficheiros
import controlo_stock
import registo_produtos
import registo_vendas


def ler_decimal(p):
    while True:
        s = input(p).strip().replace(",", ".")
        try:
            return d(s).quantize(d("0.01"))
        except:
            print("valor invalido. exemplo: 1,50 ou 1.50")


def ler_int(p):
    while True:
        s = input(p).strip()
        try:
            return int(s)
        except:
            print("numero invalido. use apenas inteiros.")


def ler_data(p):
    while True:
        s = input(p).strip()
        if not s:
            return dt.today().isoformat()
        try:
            dt.fromisoformat(s)
            return s
        except:
            print("data invalida. use o formato yyyy-mm-dd (ex.: 2026-04-16).")


def main():
    ficheiros.init_arquivos()
    while True:
        print("\n=== loja de conveniencia (gestao por ficheiros de texto) ===")
        print("1. registar novo produto no catalogo")
        print("2. atualizar preco de um produto")
        print("3. adicionar stock (entrada) a um produto")
        print("4. registar venda (baixa de stock)")
        print("5. ver stock atual")
        print("6. total de vendas diarias")
        print("0. sair")
        opcao = input("escolha uma opcao: ").strip()
        try:
            if opcao == "1":
                codigo = input("codigo do produto: ").strip()
                nome = input("nome do produto: ").strip()
                preco = ler_decimal("preco do produto: ")
                stock_inicial = ler_int("stock inicial (inteiro >= 0): ")
                if stock_inicial < 0:
                    raise ValueError("o stock inicial nao pode ser negativo.")
                registo_produtos.registar_produto(codigo, nome, preco, stock_inicial)
                print("produto registado com sucesso.")
            elif opcao == "2":
                codigo = input("codigo do produto: ").strip()
                novo_preco = ler_decimal("novo preco: ")
                registo_produtos.atualizar_preco(codigo, novo_preco)
                print("preco atualizado com sucesso.")
            elif opcao == "3":
                codigo = input("codigo do produto: ").strip()
                qtd = ler_int("quantidade a adicionar: ")
                controlo_stock.adicionar_stock(codigo, qtd)
                print("stock atualizado com sucesso.")
            elif opcao == "4":
                codigo = input("codigo do produto: ").strip()
                qtd = ler_int("quantidade a vender: ")
                total = registo_vendas.registar_venda(codigo, qtd)
                print(f"venda registada. total: {ficheiros.format_moeda(total)}")
            elif opcao == "5":
                itens = controlo_stock.listar_stock()
                if not itens:
                    print("sem produtos no catalogo.")
                else:
                    print("\ncodigo | nome | stock")
                    for codigo, nome, quant in itens:
                        print(f"{codigo} | {nome} | {quant}")
            elif opcao == "6":
                data_iso = ler_data("data (yyyy-mm-dd) [enter = hoje]: ")
                total = registo_vendas.total_vendas_dia(data_iso)
                print(f"total de vendas em {data_iso}: {ficheiros.format_moeda(total)}")
            elif opcao == "0":
                print("a terminar...")
                break
            else:
                print("opcao invalida. tente novamente.")
        except ValueError as e:
            print(f"erro: {e}")


if __name__ == "__main__":
    main()

