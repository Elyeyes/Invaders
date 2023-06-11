# import sys
import pygame as pg

velocity_ennemie = 5
velocity_joueur = 1
variable_score = 0
class Entity:
    def __init__(self, name, image, life, position, velocity):
        self.name = name
        self.image = image
        self.life = life
        self.position = position
        self.velocity = velocity

    def get_center(self):
        return self.position[0]+self.image.get_width()/2,self.position[1]+self.image.get_height()/2


# sous-classe joueur
class joueur(Entity):
    score_joueur = 0
    # fonction déplacement du joueur

    def deplacement(self):
        self.hitbox1 = pg.Rect(0,0,60,20)
        self.hitbox1.topleft = (self.position[0], self.position[1]+12)
        self.hitbox2 = pg.Rect(0,0,12,20)
        self.hitbox2.topleft = (self.position[0]+24, self.position[1]+4)
        #print(self.hitbox2.y)
        if pg.key.get_pressed():
            if 400 / 1.25 <= self.position[0] <= 1520 / 1.25 - 60:
                if pg.key.get_pressed()[pg.K_RIGHT]:
                    self.position = (self.position[0] + self.velocity, self.position[1])
                if pg.key.get_pressed()[pg.K_LEFT]:
                    self.position = (self.position[0] - self.velocity, self.position[1])

            elif self.position[0] <= 400 / 1.25:
                self.position = (400 / 1.25, self.position[1])

            elif 1520 / 1.25 - 60 <= self.position[0]:
                self.position = (1520 / 1.25 - 60, self.position[1])



# sous-classe ennemie
class Ennemie(Entity):
    # fonction déplacement des ennemis
    def deplacement(self):
        self.position = (self.position[0] + self.velocity, self.position[1])


class UFO(Entity):
    def deplacement(self):
        self.position = (self.position[0] + self.velocity, self.position[1])

