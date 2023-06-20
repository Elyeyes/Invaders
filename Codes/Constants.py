import pygame as pg

vitesse_ennemie = 10
vitesse_joueur = 1
variable_score = 0
vitesse_horizontale = 10

delai=600

screen = pg.display.set_mode((1920 / 1.25, 1080 / 1.25))  # créer une fenetre d'une taille (x,y), #on divise par 1.25 car la mise à l'echelle et de 125%
pixelfont = "Police/Pixel Coleco.otf"

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
    squid1 = pg.image.load('Images/squid1.png')
    crab1 = pg.image.load('Images/crab1.png')
    octopus1 = pg.image.load('Images/octopus1.png')
    squid2 = pg.image.load('Images/squid2.png')
    crab2 = pg.image.load('Images/crab2.png')
    octopus2 = pg.image.load('Images/octopus2.png')
    UFO = pg.image.load('Images/UFO.png')
    Laser = pg.image.load('Images/Laser.png')
    Projectile = pg.image.load('Images/projectile.png')