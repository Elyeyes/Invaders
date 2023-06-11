from Entity import *
from Constants import *


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


def autoaffichage():  # Affichage auto des ennemies précédement créée
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