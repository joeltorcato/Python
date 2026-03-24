import turtle

lado = int(input("indique o tamanho do lado do quadrado: "))

janela = turtle.Screen()
janela.bgcolor("white")

caneta = turtle.Turtle()
caneta.color("grey")
caneta.pensize(2)
caneta.speed(3)

caneta.begin_fill()
caneta.fillcolor("grey")
for _ in range(4):
    caneta.forward(lado)
    caneta.right(90)
caneta.end_fill()

caneta.hideturtle()
turtle.done()
