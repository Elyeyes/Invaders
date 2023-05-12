#import sys
import pygame as pg

pg.init() # initialise pygame objects

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN) #créer une fenetre d'une taille (x,y)
pg.display.set_caption('Space Invaders') #change le nom de la fenetre créée



#définie les couleurs en bash
class ColorsRGB:
    Black = (0,0,0)
    Red = (255,0,0)
    Green = (0,255,0)
    Yellow = (255,255,0)
    Blue = (0,0,255)
    Cyan = (0, 255, 255)
    Magenta =(255,0,255)
    White = (255,255,255)

class forme:
    squid=pg.image.load('squid.png')
    #squid=pg.transform.scale_by(squid,5) #multiplie par 5 taille squid
    crab=pg.image.load('crab.png')
    #crab=pg.transform.scale_by(crab,5) #multiplie par 5 taille squid
    octopus=pg.image.load('octopus.png')
    #octopus=pg.transform.scale_by(octopus,5) #multiplie par 5 taille squid
    UFO=pg.image.load('UFO.png')
    #UFO=pg.transform.scale_by(UFO,5) #multiplie par 5 taille squi
    Laser=pg.image.load('Laser.png')
    #Laser=pg.transform.scale_by(Laser,5) #multiplie par 5 taille squid


class entity(pg.sprite.Sprite):
    def __init__(self, image, life, position):
        super().__init__()
        self.image = image
        self.life = life
        self.position = position
        self.rect = self.image.get_rect(center=(100,50))

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


squid0=entity(forme.squid, 1, (100,100))
for i in range(0, 3):
    for j in range(1, 4):
        nb=3*i+j
        autoEnnemie="squid" + str(nb) #nom nouvelle ennemie
        globals()[autoEnnemie] = entity(forme.squid, 1,(100+j*50,100))

def scoreboard():
    font = pg.font.SysFont(None, 24)
    Score = font.render('Life:'+str(Laser.life), True, 'White')
    screen.blit(Score, (20, 20))
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


#je créer mes entités
squid=entity(forme.squid, 1, (100,100))
crab=entity(forme.crab, 1, (100,142))
octopus=entity(forme.octopus, 1, (100,184))
UFO=entity(forme.UFO, 1, (100,10))
Laser=entity(forme.Laser, 3, (100,500))

while True:
    for i in range(1, 9):
        inst_name ="squid"+str(i)
        screen.blit(forme.squid, globals()[inst_name].position)
    screen.blit(squid.image, squid.position)
    screen.blit(crab.image, crab.position)
    screen.blit(octopus.image, octopus.position)
    screen.blit(UFO.image, UFO.position)
    screen.blit(Laser.image, Laser.position)

    scoreboard()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    pg.display.update()




