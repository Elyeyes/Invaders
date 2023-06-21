from generation import *

def generation_ennemie():
    """
    génération automatique des rangées d'ennemies
    :return:
    """
    for i in range(0, 5):
        for j in range(1, 12):
            if i == 0:
                nomennemie = "Squid"
                png = Forme.squid1
                mul = 8
                size = (32, 20)
                score = 30
            elif i == 1:
                nomennemie = "CrabA"
                png = Forme.crab1
                mul = 2
                size = (44, 24)
                score = 20
            elif i == 2:
                nomennemie = "CrabB"
                png = Forme.crab1
                mul = 2
                size = (44, 24)
                score = 20
            elif i == 3:
                nomennemie = "OctopusA"
                png = Forme.octopus1
                mul = 0
                size = (48, 20)
                score = 10
            else:
                nomennemie = "OctopusB"
                png = Forme.octopus1
                mul = 0
                size = (48, 20)
                score = 10
            autoennemie = nomennemie + str(j)  # nom nouvelle ennemie
            globals()[autoennemie] = Ennemie(size, autoennemie, png, 1, (octopus0.position[0] + j * 58 + mul, octopus0.position[1] + i * 60), Constants.vitesse_ennemie, score)

def deplacement_ennemie(bordure_droite, bordure_gauche):
    """
    Gère le déplacement des ennemies, si ils arrivent à une limite ils changent de sens
    :param bordure_droite: limite droite décidé dans la fonction affichage
    :param bordure_gauche: limite gauche décidé dans la fonction affichage
    :return:
    """
    octopus0.deplacement()
    for i in range(4, -1, -1):
        for j in range(11, 0, -1):
            if i == 0:
                nomennemie = "Squid"
                mul = 8
                a = Forme.squid1
                b = Forme.squid2
            elif i == 1:
                nomennemie = "CrabA"
                mul = 1
                a = Forme.crab1
                b = Forme.crab2
            elif i == 2:
                nomennemie = "CrabB"
                mul = 1
                a = Forme.crab1
                b = Forme.crab2
            elif i == 3:
                nomennemie = "OctopusA"
                mul = 0
                a = Forme.octopus1
                b = Forme.octopus2
            else:
                nomennemie = "OctopusB"
                mul = 0
                a = Forme.octopus1
                b = Forme.octopus2
            ennemie = nomennemie + str(j)  # nom nouvelle ennemielife
            if globals()[ennemie].life > 0:
                globals()[ennemie].position = (octopus0.position[0] + (12 - j) * 58 + mul, octopus0.position[1] + i * 60)
                if globals()[ennemie].image == a:
                    globals()[ennemie].image = b
                else:
                    globals()[ennemie].image = a
                if (pg.Rect.colliderect(globals()[ennemie].hitbox, bordure_droite) and Ennemie.Ennemie_state == 1) or \
                        (pg.Rect.colliderect(globals()[ennemie].hitbox, bordure_gauche) and Ennemie.Ennemie_state == -1):
                    Ennemie.Ennemie_state = Ennemie.Ennemie_state * -1
                    octopus0.position = (octopus0.position[0], octopus0.position[1] + Constants.vitesse_horizontale)
            globals()[ennemie].hitbox_mouvement()
