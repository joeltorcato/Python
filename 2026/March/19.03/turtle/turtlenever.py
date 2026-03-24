import turtle

tela = turtle.Screen()
tela.title("Turtle")
tela.setup(width=425, height=425, startx=0, starty=0)

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()