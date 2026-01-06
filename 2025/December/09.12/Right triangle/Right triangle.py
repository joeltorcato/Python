a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if a + b > c and a + c > b and b + c > a:
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("É um triângulo retângulo")
    else:
        print("Não é um triângulo retângulo")
else:
    print("Não forma um triângulo")