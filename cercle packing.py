import pygame
import numpy as np
import time
import os


class Cercle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 1

        self.growing = True

    def show(self):
        # on affiche le cercle
        pygame.draw.circle(surface, blanc, (self.x, self.y), self.r, 1)

    def grow(self):
        if self.growing:
            self.r += 1

    def borders(self):
        # return True si le cercle sort du cadre
        return self.x - self.r < 0 or self.x + self.r > L or self.y - self.r < 0 or self.y + self.r > H

    def other_cercles(self, cercles):
        # return True si le cercle touche un autre cercle
        for other in cercles:

            # on s'assure que l'on ne compare pas le meme cercle
            if other != self:

                # on calcule la distance entre les 2 cercles
                d = np.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

                if d < other.r + self.r:
                    return True


def new_cercle():
    x = np.random.randint(0, L)
    y = np.random.randint(0, H)

    for cercle in cercles:
        d = np.sqrt((x - cercle.x)**2 + (y - cercle.y)**2)

        # si le nouveau cercle est a l'interieur d'un autre : break
        if d < cercle.r:
            return False

    return Cercle(x, y)


def draw():

    # on créer un nouveau cercle
    cercle = new_cercle()
    while cercle is False:
        cercle = new_cercle()
    cercles.append(cercle)

    # on affiche tout les cercles
    for cercle in cercles:

        # on actualise les cercles s'ils grandissent encore
        if cercle.growing:

            # s'il touche le bord on arrete
            if cercle.borders():
                cercle.growing = False

            # s'il touche un autre cercle on arrete
            if cercle.other_cercles(cercles):
                cercle.growing = False

        # la fonction grow ne se lance que si growing = True
        cercle.grow()
        # on affiche tout les cercles
        cercle.show()


def save(surface, doc_name):

    path = 'C:/Users/simon/Documents/IPSA/A2/python/Pygame/'

    if doc_name not in os.listdir(path):
        os.mkdir(doc_name)
    else:
        os.chdir(path + doc_name)
        pygame.image.save(surface, str(round(time.time(), 1)) + ".jpeg")


# ----------------------------------------------------------------------------------------------------------------------
# initialisation constante
H = 500
L = 700
n = 4


blanc = (255, 255, 255)
gris = (150, 150, 150)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)

# initialisation environnement
cercles = []

# initialisation fenetre
pygame.init()
pygame.display.set_caption("A*")
surface = pygame.display.set_mode((L, H))


# ----------------------------------------------------------------------------------------------------------------------
# boucle infinie
launched = 1
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = 0

    surface.fill(noir)

    draw()

    pygame.display.flip()
    pygame.time.wait(10)
