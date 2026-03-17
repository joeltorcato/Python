produtos = {
    "arroz": 1.50,
    "leite": 0.90,
    "pão": 0.30,
    "azeite": 3.20,
    "massa": 1.10,
    "café": 2.50
}

carrinho = {}

print("produtos disponíveis:")
for nome, preco in produtos.items():
    print(f"{nome} - €{preco:.2f}")

while True:
    escolha = input("escolha um produto (ou 'fim' para terminar): ").strip().lower()
    if escolha == "fim":
        break
    if escolha not in produtos:
        print("produto inválido. tente novamente.")
        continue
    try:
        quantidade = int(input(f"quantidade de '{escolha}': "))
        if quantidade <= 0:
            print("quantidade deve ser positiva.")
            continue
    except valueerror:
        print("quantidade inválida.")
        continue
    carrinho[escolha] = carrinho.get(escolha, 0) + quantidade

print("\nresumo da compra:")
total = 0
linhas = []
for nome, quantidade in carrinho.items():
    valor = produtos[nome] * quantidade
    total += valor
    linha = f"{nome}: {quantidade} x €{produtos[nome]:.2f} = €{valor:.2f}"
    print(linha)
    linhas.append(linha)

print(f"valor total: €{total:.2f}")

with open("compra_supermercado.txt", "w", encoding="utf-8") as f:
    for linha in linhas:
        f.write(linha + "\n")
    f.write(f"valor total: €{total:.2f}\n")