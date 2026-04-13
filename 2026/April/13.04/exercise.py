import turtle


tim = turtle.Turtle()
screen = turtle.Screen()

def up():
    tim.setheading(90)
    tim.forward(10)
    
def down():
    tim.setheading(270) # 270 graus é para baixo
    tim.forward(100)
    
def left():
    tim.setheading(180)
    tim.forward(100)
    
def right():
    tim.setheading(0)
    tim.forward(100)
    
screen.listen() # Permite que a tela escute os eventos de teclado
screen.onkey(up, "up") # Associa a função 'up' à tecla de seta para cima
screen.onkey(down, "down") # Associa a função 'down' à tecla
screen.onkey(left, "left") # Associa a função 'left' à tecla de seta para esquerda
screen.onkey(right, "right") # Associa a função 'right' à tecla de seta para direita

screen.mainloop() # Mantém a janela aberta para ouvir os eventos de teclado