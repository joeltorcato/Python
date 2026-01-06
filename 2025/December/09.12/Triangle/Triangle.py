while True:
    a = float(input("Digite o lado a: "))
    b = float(input("Digite o lado b: "))
    c = float(input("Digite o lado c: "))

    if a + b > c and a + c > b and b + c > a:
        sides = [a, b, c]
        unique = len(set(sides))
        if unique == 1:
            print("Equilátero")
        elif unique == 2:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("Não forma um triângulo")

    continuar = input("Quer testar outro triângulo? (s/n): ").lower()
    if continuar != 's':
        break