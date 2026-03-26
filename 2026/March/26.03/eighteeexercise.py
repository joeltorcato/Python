import turtle

lado = 200
janela = turtle.Screen()
janela.bgcolor("white")
caneta = turtle.Turtle()
caneta.speed(0)

# quadrado grande preto
caneta.penup()
caneta.goto(-lado/2, -lado/2)
caneta.pendown()
caneta.color("black")
caneta.begin_fill()
for _ in range(4):
    caneta.forward(lado)
    caneta.left(90)
caneta.end_fill()

tamanho = lado // 2
cores = ["red", "green", "blue", "yellow"]
posicoes = [(-lado/2, 0), (0, 0), (-lado/2, -lado/2), (0, -lado/2)]

for i in range(4):
    caneta.penup()
    caneta.goto(posicoes[i])
    caneta.pendown()
    caneta.color(cores[i])
    caneta.begin_fill()
    for _ in range(4):
        caneta.forward(tamanho)
        caneta.left(90)
    caneta.end_fill()

caneta.hideturtle()
turtle.done()