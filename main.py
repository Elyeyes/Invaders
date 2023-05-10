#import sys
import pygame as pg

pg.init() # initialise pygame objects
screen =pg.display.set_mode((800, 600)) #créer une fenetre d'une taille (x,y)
pg.display.set_caption('Space Invaders') #change le nom de la fenetre créée


#définie les couleurs en bash
class ColorsTerminal:
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta =  "\033[35m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"

#définie les couleurs en bash
class ColorsRGB:
    Black = (0,0,0)
    Red = (255,0,0)
    Green = (0,255,0)
    Yellow = (255,255,0)
    Blue = (0,0,255)
    Cyan = (0, 255, 255)
    Magenta =  (255,0,255)
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
    """tir1=
    tir2="""


class entity(pg.sprite.Sprite):
    def __init__(self, image, life, position):
        super().__init__()
        self.image=image
        self.life=life
        self.position=position
        self.rect=self.image.get_rect(center=(100,50))

    def deplacement(self, position, a):

    def __repr__(self, image, life, position):
        self.image=image
        self.life=life
        self.position=position
        #self.rect=self.image.get_rect(center=(100, 50))
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

class scoreboard:
    def __init__(self, score=0, life=3):
        self.score=score
        self.life=life
        pygame.init()
    
    def __repr__(self):
        


class spaceinvaders:
    def __init__(self):
        pg.init()"""

#je créer mes entités
squid=entity(forme.squid, 1, (100,100))
crab=entity(forme.crab, 1, (100,142))
octopus=entity(forme.octopus, 1, (100,184))
UFO=entity(forme.UFO, 1, (100,10))
Laser=entity(forme.Laser, 3, (100,500))

while True:
    screen.fill("black")
    screen.blit(squid.image, squid.position)
    screen.blit(crab.image, crab.position)
    screen.blit(octopus.image, octopus.position)
    screen.blit(UFO.image, UFO.position)
    screen.blit(Laser.image, Laser.position)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    pg.display.update()


