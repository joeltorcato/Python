import turtle
import random

janela = turtle.Screen()
janela.bgcolor("white")
caneta = turtle.Turtle()
caneta.speed(0)

cores = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta"]
formas = ["circulo", "quadrado", "triangulo"]

for _ in range(10):
    cor = random.choice(cores)
    forma = random.choice(formas)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    caneta.penup()
    caneta.goto(x, y)
    caneta.pendown()
    caneta.color(cor)
    caneta.begin_fill()
    if forma == "circulo":
        raio = random.randint(20, 60)
        caneta.circle(raio)
    elif forma == "quadrado":
        lado = random.randint(30, 80)
        for _ in range(4):
            caneta.forward(lado)
            caneta.left(90)
    elif forma == "triangulo":
        lado = random.randint(30, 80)
        for _ in range(3):
            caneta.forward(lado)
            caneta.left(120)
    caneta.end_fill()

caneta.hideturtle()
turtle.done()
