# import sys
import pygame as pg

pg.init()  # initialise pygame objects
screen = pg.display.set_mode((1920 / 1.25, 1080 / 1.25), pg.FULLSCREEN)  # créer une fenetre d'une taille (x,y), #on divise par 1.25 car la mise à l'echelle et de 125%
pg.display.set_caption('Space Invaders')  # change le nom de la fenetre créée

pixelfont = "Pixel Coleco.otf"
velocity_ennemie = 5
velocity_joueur = 1
variable_score = 0


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


"""class Forme:
    def __init__(self,squid:Entity,)
    if self.squid.etat=="""


class Forme:
    squid1 = pg.image.load('squid1.png')
    crab1 = pg.image.load('crab1.png')
    octopus1 = pg.image.load('octopus1.png')
    squid2 = pg.image.load('squid2.png')
    crab2 = pg.image.load('crab2.png')
    octopus2 = pg.image.load('octopus2.png')
    UFO = pg.image.load('UFO.png')
    Laser = pg.image.load('Laser.png')


class Entity:
    def __init__(self, name, image, life, position, velocity):
        self.name = name
        self.image = image
        self.life = life
        self.position = position
        self.velocity = velocity


# sous-classe joueur
class joueur(Entity):
    score_joueur = 0

    # fonction déplacement du joueur
    def deplacement(self):
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

UFO = UFO("UFO", Forme.UFO, 1, (50, 10), velocity_ennemie)
Laser = joueur("Laser", Forme.Laser, 3, (744, 800), velocity_joueur)


# génération automatique des rangées d'ennemies
def autogeneration():
    octopus0 = Ennemie("octopus0", Forme.octopus1, 1, (430, 180), velocity_ennemie)  # initialise une entité servant de référence pour la position de toutes les autres
    for i in range(0, 5):
        for j in range(1, 12):
            if i == 0:
                nomennemie = "squid"
                png = Forme.squid1
                mul = 8
            elif i == 1:
                nomennemie = "crabA"
                png = Forme.crab1
                mul = 2
            elif i == 2:
                nomennemie = "crabB"
                png = Forme.crab1
                mul = 2
            elif i == 3:
                nomennemie = "octopusA"
                png = Forme.octopus1
                mul = 0
            else:
                nomennemie = "octopusB"
                png = Forme.octopus1
                mul = 0
            autoennemie = nomennemie + str(j)  # nom nouvelle ennemie
            globals()[autoennemie] = Ennemie(autoennemie, png, 1, (octopus0.position[0] + j * 58 + mul, octopus0.position[1] + i * 60), velocity_ennemie)
    # Affichage auto des ennemies précédement créée
    for i in range(0, 5):
        for j in range(1, 12):
            if i == 0:
                nomennemie = "squid"
            elif i == 1:
                nomennemie = "crabA"
            elif i == 2:
                nomennemie = "crabB"
            elif i == 3:
                nomennemie = "octopusA"
            else:
                nomennemie = "octopusB"
            inst_name = nomennemie + str(j)
            screen.blit(globals()[inst_name].image, globals()[inst_name].position)


# fonction scoreboard
def scoreboard():
    nbvie = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagevie = nbvie.render('Life:' + str(Laser.life), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagevie, (20, 20))  # affichage du font
    score = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagescore = score.render('Score:' + str(variable_score), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagescore, (20, 50))  # affichage du font

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


def affichage():
    screen.fill("black")
    autogeneration()
    screen.blit(UFO.image, UFO.position)  # affichage de l'UFO
    screen.blit(Laser.image, Laser.position)  # affichage du joueur
    # créer les bordures
    screen.fill("black", (0, 0, 400 / 1.25, 1080 / 1.25))
    screen.fill("black", (1520 / 1.25, 0, 400 / 1.25, 1080 / 1.25))
    scoreboard()  # appel de la fonction scoreboard
    if Laser.life <= 0:
        screen.fill(ColorsRGB.Purple)  # game over temporaire


while True:
    affichage()
    pg.display.update()
    pg.time.Clock().tick(500)
    pg.key.set_repeat(1)  # Permet au touche du clavier de continuer de fonctionner une fois enfoncé
    for event in pg.event.get():
        Laser.deplacement()  # appel fonction déplacement dans class joueur (pour le Laser)
        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            Laser.life = Laser.life - 1
        if event.type == pg.QUIT:
            pg.quit()
            quit()
