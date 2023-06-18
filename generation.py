from Entity import *

UFO = Ufo("UFO", Forme.UFO, 1, (50, 10), vitesse_ennemie)
Laser = Joueur("Laser", Forme.Laser, 3, (744, 800), vitesse_joueur)

# génération automatique des rangées d'ennemies
octopus0 = Ennemie((0, 0), "octopus0", Forme.octopus1, 1, (420, 150), vitesse_ennemie)  # initialise une entité servant de référence pour la position de toutes les autres
def autogeneration():
    for i in range(0, 5):
        for j in range(1, 12):
            if i == 0:
                nomennemie = "Squid"
                png = Forme.squid1
                mul = 8
                size = (32, 20)
            elif i == 1:
                nomennemie = "CrabA"
                png = Forme.crab1
                mul = 2
                size = (44, 24)
            elif i == 2:
                nomennemie = "CrabB"
                png = Forme.crab1
                mul = 2
                size = (44, 24)
            elif i == 3:
                nomennemie = "OctopusA"
                png = Forme.octopus1
                mul = 0
                size = (48, 20)
            else:
                nomennemie = "OctopusB"
                png = Forme.octopus1
                mul = 0
                size = (48, 20)

            autoennemie = nomennemie + str(j)  # nom nouvelle ennemie
            globals()[autoennemie] = Ennemie(size, autoennemie, png, 1, (octopus0.position[0] + j * 58 + mul, octopus0.position[1] + i * 60), vitesse_ennemie)

def autoaffichage():  # Affichage auto des ennemies précédement créée
    for i in range(0, 5):
        for j in range(1, 12):
            if i == 0:
                nomennemie = "Squid"
            elif i == 1:
                nomennemie = "CrabA"
            elif i == 2:
                nomennemie = "CrabB"
            elif i == 3:
                nomennemie = "OctopusA"
            else:
                nomennemie = "OctopusB"
            inst_name = nomennemie + str(j)
            pg.draw.rect(screen, "red", globals()[inst_name].hitbox)
            screen.blit(globals()[inst_name].image, globals()[inst_name].position)


def deplacementennemie(bordure_droite, bordure_gauche):
    octopus0.deplacement(bordure_droite, bordure_gauche)
    for i in range(4, -1, -1):
        for j in range(11, 0, -1):
            if i == 0:
                nomennemie = "Squid"
                mul = 8
            elif i == 1:
                nomennemie = "CrabA"
                mul = 2
            elif i == 2:
                nomennemie = "CrabB"
                mul = 2
            elif i == 3:
                nomennemie = "OctopusA"
                mul = 0
            else:
                nomennemie = "OctopusB"
                mul = 0
            ennemie_deplace = nomennemie + str(j)  # nom nouvelle ennemie
            globals()[ennemie_deplace].position = (octopus0.position[0] + (12-j) * 58 + mul, octopus0.position[1] + i * 60)
            globals()[ennemie_deplace].hitbox_mouvement()
            if (pg.Rect.colliderect(globals()[ennemie_deplace].hitbox, bordure_droite) and Ennemie.Ennemie_state == 1) or (pg.Rect.colliderect(globals()[ennemie_deplace].hitbox, bordure_gauche) and Ennemie.Ennemie_state == -1):
                Ennemie.Ennemie_state = Ennemie.Ennemie_state * -1
                octopus0.position = (octopus0.position[0], octopus0.position[1] + vitesse_horizontale)
