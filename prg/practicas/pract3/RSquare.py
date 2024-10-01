import turtle
import math

def inicializa_tortuga():
    turtle.setup(width=800,height=800)  # Crea ventana de 800 x 800
    turtle.speed(0)                     # Velocidad maxima
    turtle.pencolor("#101010")          # Color del lapiz
    turtle.fillcolor("#2c95b5")         # Color del fondo
    turtle.width(2)                     # Ancho del trazo

def finaliza_tortuga():
    turtle.hideturtle()         # Ocultar tortuga
    turtle.done()               # Desbloquear la ventana grafica
    try:
        turtle.bye()
    except turtle.Terminator:
        pass    
    
def dibuja_cuadrado(lado,x,y):
    # Posicionar la tortuga.
    # El centro de la pantalla es (0,0), por tanto para que el cuadrado este
    # centrado, la esquina sup. izqda.  debe situarse en (-lado//2, -lado//2)
    turtle.up()
    turtle.setpos(x-lado//2,y-lado//2)
    turtle.down()

    # Dibujar y rellenar cuadrado
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.end_fill()
    
def RSquareA(n,x,y,l):
    if n == 1:
        dibuja_cuadrado(l,x,y)
    else:
        RSquareA(n-1,x+l//2,y+l//2,l/2)
        RSquareA(n-1,x+l//2,y-l//2,l/2)
        RSquareA(n-1,x-l//2,y+l//2,l/2)
        RSquareA(n-1,x-l//2, y-l//2,l/2)
        dibuja_cuadrado(l,x,y)
        
def RSquareB(n,x,y,l):
    if n == 1:
        dibuja_cuadrado(l,x,y)
    else:
        dibuja_cuadrado(l,x,y)
        RSquareB(n-1,x+l//2,y+l//2,l/2)
        RSquareB(n-1,x+l//2,y-l//2,l/2)
        RSquareB(n-1,x-l//2,y+l//2,l/2)
        RSquareB(n-1,x-l//2, y-l//2,l/2)


if __name__ == '__main__':
    x = input('Que tipo de RSquare quieres (pulsa enter para finalizar): ')
    while x not in ['a','b','A','B','']:
        print('Tiene que ser A o B (pulsa enter para finalizar)')
        x = input('Que tipo de RSquare quieres: ')
    if x == '':
        print('chaao')
    else:
        if x in ['a','A']:
            n = int(input('Que orden quieres: '))
            inicializa_tortuga()
            RSquareA(n,0,0,400)
            finaliza_tortuga()
        if x in ['b','B']:
            n = int(input('Que orden quieres: '))
            inicializa_tortuga()
            RSquareB(n,0,0,400)
            finaliza_tortuga()