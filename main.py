# import sys
import pygame as pg
from overlay import *


pg.init()  # initialise pygame objects
pg.display.set_caption('Space Invaders')  # change le nom de la fenetre créée
clock = pg.time.Clock()


class Projectile(pg.sprite.Sprite):
    def __init__(self, position, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.center = [self.position[0], self.position[1]]
        pg.draw.rect(screen, "white", (Projectile, (500, 812)))

    def update(self):
        self.rect.y = -5



"""
    code de chat gpt
    self.mask = pg.mask.from_surface(pg.image.load(mask_file).convert_alpha())

    def collide_with(self, other):
        return pg.sprite.collide_mask(self, other)
    In this example, the Entity class is defined with an additional mask_file parameter that specifies the file path to the custom mask image. The mask attribute is set to the mask image using the pg.mask.from_surface() function.
The collide_with() method is also defined to check for collisions between two Entity objects using their masks, using the pg.sprite.collide_mask() function.
With this implementation, the Entity object will have a hitbox that matches the shape of the mask image, instead of a rectangular hitbox that encloses the entire sprite. This can be useful for games that require more precise collision detection.


class tir:
    def __init__(self, position,image):
        self.image=image
        self.position=position

class block:
    def __init__(self, position):
        self.pixel=pixel





class spaceinvaders:
    def __init__(self):
        pg.init()"""






"""if (condition collision):
        life=life-1
if (condition collision squid):
    score=score+30
if (condition collision crab):
    score=score+20
if (condition collision octopus):
    score=score+10
if (condition collision UFO):
    score=score+100"""


autogeneration()

def quitter():
    if event.type == pg.MOUSEBUTTONDOWN:
        print(pg.mouse.get_pos())
        Laser.life = Laser.life - 1
    if event.type == pg.QUIT:
        pg.quit()
        quit()

while True:
    affichage()
    pg.display.update()
    for event in pg.event.get():
        Laser.deplacement()  # appel fonction déplacement dans class joueur (pour le Laser)
        #pg.draw.rect(screen, "red", Laser.hitbox1)
        #pg.draw.rect(screen, "red", Laser.hitbox2)
        quitter()
        pg.key.set_repeat(1)  # Permet au touche du clavier de continuer de fonctionner une fois enfoncé
