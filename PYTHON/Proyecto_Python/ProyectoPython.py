#!/usr/bin/python3


# -------------------------------------------#
# _____Universidad de Costa Rica_____#
# __Escuela de Ingenieria Electrica___#
# ___Proyecto final de Python___#

# Autores:
# Ximena Cespedes Quesada B91969
# Aroon Sanabria Torres B97205
# Carlos Andres Cordero Retana B92317

# Descripcion del programa:

""" El siguiente programa se encarga de
crear un juego. Gracias a las librerias
mostradas se logra crear diferentes objetos
a partir de sus clases como una pantalla,
margen, rotulos, un jugador ,principal (rana),
jugadores secundarios (pajaros y moscas). DEntro
de estas clases se definen ciertos atrubutos
y metodos para que estos objetos se puedan mover
en la pantalla principal.Asimismo, haciendo uso
de diferentes funciones, se logra determinar si dos
objetos colisionan, o qué musica se desea poner etc.
Por ultimo, también se crean 2 menus, los cuales
permiten correr el juego, mostrar el highscore,
mostrar cómo se juga, regresar al menu principal o
salir del juego.
"""


import turtle
import random
import math
import pygame
from pygame import mixer
from time import sleep


# En esta clase se crean los objetos: "puntaje:#" y "nivel: #"
class rotulos(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(x, y)
        self.score = 0

    def marcador_up(self, texto):
        self.clear()
        self.write(
            '{} : {}'.format(texto, self.score),
            False, align='left', font=('Arial', 14, 'normal')
            )

    def cambiar_puntaje(self, points, texto):
        self.score += points
        self.marcador_up(texto)
        return self.score


# En esta clase se crea el margen del juego
class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        # Caracteristicas del Borde
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

# Crear el borde con sus dimensiones
    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


# Creacion de la clase de la rana (jugador principal)
class rana(turtle.Turtle):

    # funcion del jugador
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("ranita.gif")
        self.color("white")
        self.speed = 8

    # EL jugador se mueve
    def move(self):
        self.forward(self.speed)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1


# Creacion de la clase para las moscas
class Mosca(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("mosca.gif")
        self.speed = 8
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        # Si tocan el borde se devuelven
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


# Creacion de la clase para los pajaros malvados
class pajaromalo (turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        # atributos
        self.penup()
        self.speed(0)
        self.shape("pajaromalo.gif")
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self, speed):

        self.forward(speed)
        # Si tocan el borde se devuelven
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


# Funcion para la musica de fondo
def musica_de_fondo(volumen, cancion):
    pygame.init()
    mixer.music.load(cancion)  # Carga la cancion
    mixer.music.set_volume(volumen)  # Configura el volumen
    mixer.music.play(loops=-1)  # Play a la cancion y se repite
# Funcion para los efectos musicales


def musica_efectos(volumen, cancion):
    pygame.init()
    mixer.music.load(cancion)  # Carga la cancion
    mixer.music.set_volume(volumen)  # Configura el volumen
    mixer.music.play()  # Play a la cancion y suena solo una vez


# Funcion para las colisiones
def isCollision(t1, t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a**2) + (b**2))
    if distance < 35:
        return True
    else:
        return False


# Funcion que se usa para realizar la escritura con pygame.
def escritura(espacio, texto, tamano, ejex, ejey):

    letra = pygame.font.SysFont("Arial", tamano)  # Tipo de letra y tamano
    # Caracteristicas de la letra
    conf_letra = letra.render(texto, True, (0, 0, 0))
    conf_espacio = conf_letra.get_rect()  # Poner el texto en un cuadrado
    conf_espacio.midtop = (ejex, ejey)  # Colocar el caudrada y el texto
    espacio.blit(conf_letra, conf_espacio)


# En esta funcion se corre el juego
def mainprogram():
    """ Cuando se llama a esta funcion, se corre
    el juego.

    """

    # Se crea la pantalla
    wn = turtle.Screen()
    # Se incluyen las tres figuras para usarlas luego
    wn.addshape("ranita.gif")
    wn.addshape("mosca.gif")
    wn.addshape("pajaromalo.gif")
    # Se pone esta imagen en el background
    wn.bgpic("pantalla.jpeg")
    # Titulo del juego
    wn.title("Atrapa Moscas")
    # Se guardan estos sonidos para usarlos luego
    sound_goals = pygame.mixer.Sound("pacman-eating-ghost.ogg")
    sound_obst = pygame.mixer.Sound("kirby-death.ogg")
    # Creacion de objetos
    player = rana()
    border = Border()
    game = rotulos(-290, 310)
    niveles = rotulos(225, 310)

    # Se crean 3 moscas en el nivel 1
    moscas = []
    for count in range(3):
        moscas.append(Mosca())

    # Se crean 4 pajaros malvados en el nivel 1
    obstacles = []
    for count in range(4):
        obstacles.append(pajaromalo())

    # Se dibuja el borde
    border.draw_border()

    # Creacion de la musica de fondo
    musica_de_fondo(0.5, "kirby-sand-canyon.mp3")

    # Inicio del puntaje
    score = 0

    # El modulo turtle empieza a escuchar al teclado
    turtle.listen()
    turtle.onkey(player.turnleft, "Left")
    turtle.onkey(player.turnright, "Right")
    turtle.onkey(player.increasespeed, "Up")

    # No ocurrido una colision
    breakk = 0

    # Acelerar el juego
    wn.tracer(1)

    # Valor inicial del nivel
    nivel = 0

    # Aqui se inicia el juego.
    while True:

        wn.update()
        # Si ocurre una colision, pasa esto.
        if breakk == 1:
            pygame.mixer.music.stop()
            sound_obst.play()
            sleep(2)
            handle = open("scores.txt", "a+")
            handle.write("{}\n".format(score))
            handle.close()
            handl = open("scores.txt", "r")
            strlist = handl.readlines()
            scores = []
            for line in strlist:
                if line == "\n":
                    continue
                else:
                    fixed = line.rstrip()
                    scores.append(int(fixed))
            scores.sort(reverse=True)
            # Se extrae el highscore actual y se guarda
            highscore = scores[0]
            handlew = open("highscore.txt", "w")
            handlew.write("{}\n".format(highscore))
            handlew.close()
            break

        # Si el jugador no ha perdido, hace esto
        player.move()
        # Las moscas se mueve en cada iteracion
        for moscaa in moscas:
            moscaa.move()

            if isCollision(player, moscaa):
                sound_goals.play()
                moscaa.jump()
                score = game.cambiar_puntaje(10, "Puntaje")

        # Los pajaros se mueven en cada iteracion
        for obstacle in obstacles:
            # Nivel 1
            if score < 20:
                if nivel == 0:
                    nivel = 1
                    niveles.cambiar_puntaje(1, "Nivel")
                obstacle.move(1)  # Se mueve una distancia de 1
            # Nivel 2
            if score >= 20 and score < 40:
                if nivel == 1:
                    obstacles[0].hideturtle()
                    obstacles[1].hideturtle()
                    obstacles[2].hideturtle()
                    obstacles[3].hideturtle()
                    moscas[2].hideturtle()
                    moscas = moscas[:-1]
                    nivel = 2
                    niveles.cambiar_puntaje(1, "Nivel")  # Nivel: 2
                    obstacles = []
                    for count in range(7):
                        obstacles.append(pajaromalo())

                obstacle.move(12)
            # Nivel 3
            else:
                if nivel == 2:
                    obstacles[0].hideturtle()
                    obstacles[1].hideturtle()
                    obstacles[2].hideturtle()
                    obstacles[3].hideturtle()
                    obstacles[4].hideturtle()
                    obstacles[5].hideturtle()
                    obstacles[6].hideturtle()
                    moscas[1].hideturtle()
                    moscas = moscas[:-1]
                    nivel = 3
                    niveles.cambiar_puntaje(1, "Nivel")
                    obstacles = []
                    for count in range(10):
                        obstacles.append(pajaromalo())
                # Velocidad de los pajaros en el nivel 3
                obstacle.move(17)

            # Si hay colision con un pajaro malo
            if isCollision(player, obstacle):
                breakk = 1
                break

            # Si hay colision con el borde
            elif (player.xcor() > 290 or player.xcor() < -290
                  or player.ycor() > 290 or player.ycor() < -290):
                breakk = 1
                break

    # Se limpia la pantalla y se escribe Game Over y el score obtenido
    game.clear()
    game.goto(0, 0)
    game.write(
        "Game Over", False, align="center",
        font=("Arial", 30, "normal"))
    game.goto(0, -50)
    game.write(
        "Final score: {}".format(game.score),
        False, align="center", font=("Arial", 20, "normal"))
    sleep(1)
    player.goto(0, 0)
    player.speed = 0
    wn.clear()

    #  Se abre el menu auxiliar
    menu_aux(score)


# En esta funcion se encuentra en el menu principal
def mainmenu():
    """
    Cuando se llama a esta funcion, se crea el menu
    principal.
    """

    # Se crea la pantalla del menu principal
    window_width = 600
    window_height = 400
    window = pygame.display.set_mode((window_width, window_height))
    pantalla = pygame.image.load("fondoprincipal.jpeg").convert()
    window.blit(pantalla, [0, 0])
    pygame.display.set_caption("FLIES CATCHER")

    # Musica del menu
    musica_de_fondo(0.5, "musicafondo.mp3")

    # Tipo de letra
    font = pygame.font.SysFont("Arial", 24)

    # Tamano de botones
    button_width = 200
    button_height = 50
    button_margin = 20

    # Se crean los 4 botones del menu principal
    play_button_rect = pygame.Rect((window_width - button_width) / 2,
                                   (window_height - 4 * button_height -
                                   3 * button_margin) / 2,
                                   button_width, button_height)
    play_button_text = font.render("Play", True, (255, 255, 255))

    highscore_button_rect = play_button_rect.move(0,
                                                  button_height
                                                  + button_margin)
    highscore_button_text = font.render("Highscore", True,
                                        (255, 255, 255))

    how_to_play_button_rect = highscore_button_rect.move(0,
                                                         button_height
                                                         + button_margin)
    how_to_play_button_text = font.render("How to play",
                                          True, (255, 255, 255))

    quit_button_rect = how_to_play_button_rect.move(0,
                                                    button_height
                                                    + button_margin)
    quit_button_text = font.render("Quit", True, (0, 0, 0))

    running = True

    #  En cada iteracion se pregunta cual boton (evento) fue estripado
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # Si se estripa "Play"
                if play_button_rect.collidepoint(event.pos):
                    pygame.display.quit()
                    mainprogram()

                # Si se estripa "highscore"
                elif highscore_button_rect.collidepoint(event.pos):
                    highscore()

                # Si se estripa "how to play"
                elif how_to_play_button_rect.collidepoint(event.pos):
                    how_play()
                # Si se estripa "Quit"
                elif quit_button_rect.collidepoint(event.pos):
                    running = False

        #  Se dibujan los botones
        pygame.draw.rect(window, (255, 0, 0), play_button_rect)
        window.blit(play_button_text,
                    play_button_rect.move(
                                          (button_width -
                                           play_button_text.get_width()) / 2,
                                          (button_height -
                                           play_button_text.get_height()) / 2))

        pygame.draw.rect(window, (0, 255, 0), highscore_button_rect)
        window.blit(highscore_button_text,
                    highscore_button_rect.move((button_width -
                                                highscore_button_text.
                                                get_width()
                                                ) / 2, (button_height -
                                                        highscore_button_text.
                                                        get_height()) / 2))

        pygame.draw.rect(window, (0, 0, 255), how_to_play_button_rect)
        window.blit(how_to_play_button_text,
                    how_to_play_button_rect.move(
                        (button_width - how_to_play_button_text.get_width())
                        / 2, (button_height -
                              how_to_play_button_text.get_height()) / 2))

        pygame.draw.rect(window, (255, 255, 255), quit_button_rect)
        window.blit(quit_button_text,
                    quit_button_rect.move(
                        (button_width - quit_button_text.get_width())
                        / 2, (button_height -
                              quit_button_text.get_height()) / 2))

        # Se actualiza la pantalla
        pygame.display.update()
    # Se sale del juego
    pygame.quit()


# Cuando se pierde, se abre este menu auxiliar
def menu_aux(final_score):
    """
    Cuando se llama a esta funcion, se abre el
    menu auxiliar
    """

    # Tamano del menu
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 700

    # Colores del menu
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Tipo de letra
    FONT = pygame.font.SysFont(None, 45)

    # Se crea la pantalla
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Titulo en la pantalla
    pygame.display.set_caption("Game Over")

    # Se crea el titulo con el puntaje final
    final_score_label = FONT.render(
                                    "Final Score: {}".format(final_score),
                                    True, WHITE)

    # Se crean los botones : "play again" y "Back to Menu"
    play_again_btn = pygame.Rect(
                                 WINDOW_WIDTH // 2 - 100,
                                 WINDOW_HEIGHT // 2, 200, 50)
    play_again_label = FONT.render("Play Again", True, BLACK)
    back_to_menu_btn = pygame.Rect(WINDOW_WIDTH // 2 - 100,
                                   WINDOW_HEIGHT // 2 + 60, 200, 50)
    back_to_menu_label = FONT.render("Back to Menu", True, BLACK)

    # Hasta que el usuario estripe en la "X", el loop sigue operando.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the play again or back to menu button was cl
                if play_again_btn.collidepoint(event.pos):
                    pygame.display.quit()
                    mainprogram()
                elif back_to_menu_btn.collidepoint(event.pos):
                    pygame.display.quit()
                    mainmenu()
                    running = False

        # Se colorea la pantallade negro
        screen.fill(BLACK)

        # Se dibujan los botones y sus labels en la pantalla
        screen.blit(final_score_label,
                    (WINDOW_WIDTH // 2 -
                     final_score_label.get_width() // 2,
                     WINDOW_HEIGHT // 4))
        pygame.draw.rect(screen, WHITE, play_again_btn)
        screen.blit(play_again_label,
                    (play_again_btn.x + play_again_btn.width // 2 -
                     play_again_label.get_width() // 2,
                     play_again_btn.y + play_again_btn.height // 2 -
                     play_again_label.get_height() // 2))
        pygame.draw.rect(screen, WHITE, back_to_menu_btn)
        screen.blit(back_to_menu_label,
                    (back_to_menu_btn.x +
                     back_to_menu_btn.width // 2 -
                     back_to_menu_label.get_width() // 2,
                     back_to_menu_btn.y +
                     back_to_menu_btn.height // 2 -
                     back_to_menu_label.get_height() // 2))

        # Se actualiza la panatlla
        pygame.display.flip()

    # Se termina le ejecucion
    pygame.quit()


# Se accede a esta funcion al estripar el boton: how to play
def how_play():

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the font
    FONT_SIZE = 32
    font = pygame.font.Font(None, FONT_SIZE)

    # Fondo de pantalla
    window_width = 600
    window_height = 400
    window = pygame.display.set_mode((window_width, window_height))

    # Fondo de pantalla princial
    pantalla = pygame.image.load("pantalla.jpeg").convert()
    window.blit(pantalla, [0, 0])
    # Caption de la pantalla
    pygame.display.set_caption('Instrucciones')
    escritura(window, "Instrucciones del juego", 26, 600//2, (300/2)-70)
    archivo_abrir = "instr.txt"  # Archivo instrucciones
    archivo_instr = open(archivo_abrir, 'r')  # Abre el archivo

    # Determina cantidad de lineas del archivo
    with open(archivo_abrir) as doc:
        lineas = sum(1 for linea in doc)

    # Imprime cada linea a partir de un pto inicial
    pt_inicial = -50
    for i in range(lineas):
        cant_lineas = archivo_instr.readline()  # Lee una linea
        cant_lineas = cant_lineas.rstrip('\n')  # Quitar salto de linea
        # Imprime linea en pantalla
        escritura(window, cant_lineas, 15, 600//2, (400/2) + pt_inicial)

        pt_inicial += 20
    # Actualizacion de la pantalla
    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainmenu()
                running = False
        # Create the title
        title = font.render("How to play", True, (0, 0, 0))
        title_rect = title.get_rect(center=(SCREEN_WIDTH/2, 50))
        screen.blit(title, title_rect)


#  Se accede a esta funcion al estripar el boton: highscore
def highscore():
    # Se crea la pantalla del highscore
    pantalla = pygame.image.load("pantalla.jpeg").convert()
    screen = pygame.display.set_mode((600, 400))  # Dimensiones
    screen.blit(pantalla, [0, 0])
    pygame.display.set_caption('Highscore')  # caption
    escritura(screen, "Highscore", 26, 300, 50)  # Escritura en la pantalla

    # Se extrae el highscore actual
    handle = open("highscore.txt", "r")
    highvalue = handle.readline()
    fixed = highvalue.strip()
    # Se escribe en pantalla
    escritura(screen, fixed, 60, 600//2, (300/2) - 50)
    pygame.display.flip()  # Actualizacion de la pantalla
    running = True
    # Hasta que el usuario estripe en la X el loop seguira
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainmenu()
                running = False


if __name__ == "__main__":
    pygame.init()
    # Se inicializa el bucle
    mainmenu()
