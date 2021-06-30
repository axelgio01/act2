"""

Snake, classic arcade game.

"""

from random import randrange, shuffle
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Arreglo con las posibles en las que se puede mover la comida
# Derecha, Izquierda, Arriba, Abajo, una unidad cada uno
directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]

# Se agregan 6 posibles colores
colors = ['yellow', 'green', 'blue', 'black', 'orange', 'pink']
# Se usa la funcion shuffle para que los colores queden en posiciones aleatorias
shuffle(colors)
# Se establecen los colores de la comida y de la serpiente
foodColor = colors[0]
snakeColor = colors[1]

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def isValid(pos):
    "Determina si una posicion arbitraria pos es valida en el tablero"
    return pos.x <= 190 and pos.x >= -180 and pos.y <= 190 and pos.y >= -180


def moveFood():
    "Mueve la comida cada 5 movimientos que realiza la serpiente"
    # Permitir que se vea food en el scope actual
    global food
    # General una posicion aleatoria para la direccion
    pos = randrange(0, len(directions) - 1)
    # Posicion aleatoria a la que se moveria
    check = food + directions[pos]
    # Se comprueba que sea una posicion valida
    if isValid(check):
        food = check
    else:
        # Si no es valida se considera la posicion contraria en el arreglo
        food += directions[pos ^ 1]
    ontimer(moveFood, 500)


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()