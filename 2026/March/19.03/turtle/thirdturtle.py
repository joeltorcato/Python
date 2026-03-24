import turtle

_joel = turtle.Turtle()
_joel.color("red", "green")

_joel.width(5)

_joel.begin_fill()

for x in range(4):
    _joel.forward(100)
    _joel.left(90)

_joel.end_fill()

_joel.setpos(100, -50)
_joel.shape("circle")


turtle.done()
