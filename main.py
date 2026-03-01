import pygame
from pygame.transform import scale
import constantes
from personaje  import Personaje
import os

#Funciones:
#Escalar imagen

pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
pygame.display.set_caption("The Kanzo Adventures")

def escalar_img (image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen



#Importar imagenes
#Personaje
animaciones = []
for i in range (12):
    img = pygame.image.load(f"Assets//Images//PNG//Wraith_01//PNG Sequences//Walking//Wraith_01_Moving Forward_{i:03d}.png").convert_alpha()
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)


#Crear un Jugador de la clase Personaje
jugador = Personaje(50,50, animaciones)

#definir las variables de movimientos del jugador

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False


#controlar el frame rate
reloj = pygame.time.Clock()

run = True
while run:

    #Para ejecutar a 60 FPS
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    #Calcular el movimiento del jugador

    delta_x = 0
    delta_y = 0


    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #Mover al jugador

    jugador.movimiento(delta_x, delta_y)

    # Actualiza Estado del Jugador
    jugador.update()



    #Dibujar el Jugador
    jugador.dibujar(ventana)



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

         #Para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                 mover_derecha = False
            if event.key == pygame.K_w:
                 mover_arriba = False
            if event.key == pygame.K_s:
                 mover_abajo =  False


    pygame.display.update()

pygame.quit()