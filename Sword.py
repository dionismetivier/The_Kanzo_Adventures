import pygame
import constantes
import math

class Sword():
    def __init__(self, image):
        self.imagen_original = image
        self.imagen = image
        self.angulo = 0
        self.forma = self.imagen.get_rect()

        self.disparar = False

        self.atacando = False
        self.tiempo_ataque = 0
        self.angulo_extra = 0


    def update(self, personaje):
        self.forma.center = personaje.forma.center
        actual = pygame.time.get_ticks()

        if self.atacando:
           tiempo_pasado = actual - self.tiempo_ataque
           if tiempo_pasado > constantes.VELOCIDAD_ATAQUE:
               self.atacando = False
               self.angulo_extra = 0
           else:
               progreso = tiempo_pasado/ constantes.VELOCIDAD_ATAQUE
               self.angulo_extra = progreso * 150

           self.forma.x = self.forma.x + personaje.forma.width/8
           self.rotar_arma(False)
        if personaje.flip == True:
           self.forma.x = self.forma.x - personaje.forma.width / 8
           self.rotar_arma(True)

        #Mover la pistola con el mouse

        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x)) - 90

        self.rotar_arma(personaje.flip)

        self.forma = self.imagen.get_rect()
        self.forma.center = personaje.forma.center

    def rotar_arma(self, rotar):
            if rotar == True:
                imagen_flip = pygame.transform.flip(self.imagen_original,
                                                    True, False)
                self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
            else:
                imagen_flip = pygame.transform.flip(self.imagen_original,
                                                    False, False)
                self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_ARMA, self.forma, 1)

    def iniciar_ataque(self):
        if not self.atacando:
            self.atacando = True
            self.tiempo_ataque = pygame.time.get_ticks()