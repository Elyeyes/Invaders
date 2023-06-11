import pygame as pg

screen = pg.display.set_mode((1920 / 1.25, 1080 / 1.25))  # créer une fenetre d'une taille (x,y), #on divise par 1.25 car la mise à l'echelle et de 125%
pixelfont = "Pixel Coleco.otf"

# définie les couleurs en bash
class ColorsRGB:
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Yellow = (255, 255, 0)
    Blue = (0, 0, 255)
    Purple = (102, 0, 102)
    Magenta = (255, 0, 255)
    White = (255, 255, 255)

class Forme:
    squid1 = pg.image.load('squid1.png')
    crab1 = pg.image.load('crab1.png')
    octopus1 = pg.image.load('octopus1.png')
    squid2 = pg.image.load('squid2.png')
    crab2 = pg.image.load('crab2.png')
    octopus2 = pg.image.load('octopus2.png')
    UFO = pg.image.load('UFO.png')
    Laser = pg.image.load('Laser.png')
    Projectile = pg.image.load('projectile.png')