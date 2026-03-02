try:
    numero = int(input("escreve um valor inteiro: "))
    print(f"o valor {numero} é um número inteiro.")

except ValueError:
    print("o valor introduzido não é um número inteiro válido.")


