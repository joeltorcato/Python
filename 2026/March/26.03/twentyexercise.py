import turtle

forma = input("escolha a forma (quadrado, circulo, retangulo): ").strip().lower()

caneta = turtle.Turtle()
caneta.speed(3)

if forma == "quadrado":
    lado = int(input("tamanho do lado do quadrado: "))
    for _ in range(4):
        caneta.forward(lado)
        caneta.left(90)
elif forma == "circulo":
    raio = int(input("tamanho do raio do circulo: "))
    caneta.circle(raio)
elif forma == "retangulo":
    lado1 = int(input("tamanho do primeiro lado do retangulo: "))
    lado2 = int(input("tamanho do segundo lado do retangulo: "))
    for _ in range(2):
        caneta.forward(lado1)
        caneta.left(90)
        caneta.forward(lado2)
        caneta.left(90)
else:
    print("forma inválida.")

caneta.hideturtle()
turtle.done()
