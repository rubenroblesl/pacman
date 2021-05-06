# Rubén A. Robles Leal A00828606
# Alejandro Medrano Torres A00831829
# Reflexion Ruben:
# Esta tarea fue una de las mas retadoras que tuve, ya que fue mucho de pensarle en cómo programar los fantasmas para que fueran inteligentes. Esta semana me ayudó mucho a entender el funcionamiento de python y de los módulos, como el de freegames y de cómo instalarlos en Thonny, pero yo creo que lo más importante fué el aprendizaje que tuve con respecto a github, ya que es una herramienta que estaré utilizando durante el resto de mi carrera y es importante que tenga un buen dominio sobre ella para el trabajo colaborativo en la misma. También, los pull request fueron muy efectivos a la hora de administrar versiones, y aunque al principio fue un poco frustrante, al final todo funciono perfecto.

# Reflexion Alejandro:
# Al momento de realizar este código y los otros códigos anteriores, ya no solo en este curso sino también en actividades pasadas, que la mayor parte del trabajo que se realiza cuando se está desarrollando un código es la investigación. El investigar sobre lo que puedes usar para el código en el que estás trabajando es lo más importante. Tuve varios problemas durante la elaboración del código, ya que no recordaba mucho de Python, había estado usando mucho Matlab. Además de que vi varios conceptos nuevos a los cuales se me complico aprender, ya que no había tenido tampoco programación orientada a objetos. Para resolver este problema tuve que investigar la explicación y el uso que los nuevos conceptos que aprendí tenían, además de que me puse a volver a ver las clases para que el conocimiento se me grabara con mayor fuerza. 

# Fecha 6 de Mayo

# Link del Github: https://github.com/rubenroblesl/pacman

# Se importan las librerias
from random import choice
from turtle import *
from freegames import floor, vector

# Se almacena el score que lleva
state = {'score': 0}

# Hace invisible la direccion
path = Turtle(visible=False)
writer = Turtle(visible=False)

# Direccion del pacman
aim = vector(5, 0)

# Crea pacman en la posicion (-40, -80)
pacman = vector(-40, -100)

#Lista de listas posicion y direccion de cada fantasma
ghosts = [
    [vector(-180, 140), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 140), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

#tablero (0 son negros, 1 son espacios)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
#dibuja un square con su esq. inf. izq en (x,y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()
#
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index
#retornar True si point es un title valido
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)
#si la celda es 0 retorna False - pared 
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False
#retorar True 
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('purple')

    for index in range(len(tiles)):
        tile = tiles[index]
# si el valor es 1
        if tile > 0:
            #calcula la x,y donde se  dibuja el square
            x = (index % 20) * 20 - 200 #(21%20)*20-200=180
            y = 180 - (index // 20) * 20 #180-(21//20)*20=160
            square(x, y) #dibuja el square (-180,160)(-160,160)
#dibuja la menta sobre el square
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    #lista de colores
    colores = ['red','green','brown','white']
    "Move pacman and all ghosts."
    writer.undo()
    valor = state['score']
    writer.write(f'Score: {valor}')
#limpia la ventana
    clear()
#si no es pared ejecuta pacman.move()
    if valid(pacman + aim):
        pacman.move(aim)
#retorna la posición del pacman en el tablero
    index = offset(pacman)
#1 significa camino
    if tiles[index] == 1:
        # a esa posicion le asigna un 2 significa que ya no hay menta ahi
        tiles[index] = 2
        #se incrementa el score
        state['score'] += 1
        #calcula la posición x,y del pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        #dibujar el square sin la menta
        square(x, y)

    up()
    #se va a la poscicion del pacman
    goto(pacman.x + 10, pacman.y + 10)
    #dibuja el pacman
    dot(20, 'yellow')
#[vector(-180, 160), vector(5, 0)],
    k = 0
    for point, course in ghosts:
        #valida si el fantasma point se puede mover en course
        # si fantasma y pacman estan en la misma X
        
        # para no esperar hasta que choque
        if (valid(point + course) and point.y != pacman.y and point.x != pacman.x):
            point.move(course)
        
    # ------------MOVIMIENTO EN X INTELIGENTE-------------
        elif (point.y == pacman.y):
            #Si fantasma esta arriba
            if point.x > pacman.x:
                #si se puede ir abajo
                if valid(point + vector(-5,0)):
                    course.x = -5
                    course.y = 0
            #si esta abajo        
            else:
                if valid(point + vector(5,0)):
                    course.x = 5
                    course.y = 0
                    
    # ------------MOVIMIENTO EN Y INTELIGENTE-------------
        elif (point.x == pacman.x):
            #Si fantasma esta arriba
            if point.y > pacman.y:
                #si se puede ir abajo
                if valid(point + vector(0,-5)):
                    course.x = 0
                    course.y = -5
            #si esta abajo        
            else:
                if valid(point + vector(0,5)):
                    course.x = 0
                    course.y = 5
                        
# -------------------------- SI NO ESTA NI EN MISMA X NI EN MISMA Y -------------------------
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            #plan guarda la nueva dirrección del fantasma
            #ESTO SE DEBE DE MODIFICAR PARA HACER FANTASMAS MÁS LISTOS
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
            
        # para no esperar hasta que choque
        if (valid(point + course) and (point.y == pacman.y or point.x == pacman.x)):
            point.move(course)
#levanta
        up()
        #mueve a la posicion del fantasma
        goto(point.x + 10, point.y + 10)
        #dibuja el fantasma
        dot(15, colores[k])#'red')}
        k = k +1

    update()
#recorre la lista de fantasmas para ver si coinciden las posiciones del pacman o un fantasma
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-120,10)
            writer.write('GAME OVER',font=('Arial',30,'normal'))
            return

    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


#tamaño de la ventana ancho y alto 420,420
#0,0 indica la posicion de la esquina sup. izq. de la ventana 
setup(420, 420, 0, 0)
# esconde la flecha de la turtle default
hideturtle()
#oculta toda forma de dibujar
tracer(False)
#mueve la turtle writer a la posicion 160,160
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
#activar los eventos del teclado 
listen()
#en caso de que el usuario oprima la indicación
#llama a la funcion change con los argumentos indicados
#que indican la nueva dirrección del pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
#llama a la función world - dibuja el tablero
world()
#llama a la función move()
move()
#entra en un loop
done()
