from Entity import *

ufo = Ufo("UFO", Forme.UFO, 1, (50, 10), vitesse_ennemie)
laser = Joueur("Laser", Forme.Laser, 3, (744, 800), vitesse_joueur)
projectile_allie = Projectile((0, 0), Forme.Projectile)

octopus0 = Ennemie((0, 0), "octopus0", Forme.octopus1, 1, (420, 150), vitesse_ennemie)  # initialise une entité servant de référence pour la position de toutes les autres
def autogeneration():
    """Génère automatiquement des rangées d'ennemies
    """
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

def autoaffichage():
    """Affiche automatiquement les ennemies précédement créés
    """
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
            affiche_ennemie = nomennemie + str(j)
            if globals()[affiche_ennemie].life > 0:
                #pg.draw.rect(screen, "red", globals()[affiche_ennemie].hitbox)
                screen.blit(globals()[affiche_ennemie].image, globals()[affiche_ennemie].position)


def deplacement_ennemie(bordure_droite, bordure_gauche):
    """Permet le deplacement des ennemies horizontalements et lors d'un contact avec une bordure, ils changent de direction et avancent vers le joueur.

    Parameters
    ----------
    bordure_droite : rect
        zone que les ennemies ne pourront pas dépasser par la droite
    bordure_gauche : rect
        zone que les ennemies ne pourront pas dépasser par la gauche
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
            ennemie_deplace = nomennemie + str(j)  # nom nouvelle ennemielife
            if globals()[ennemie_deplace].life > 0:
                globals()[ennemie_deplace].position = (octopus0.position[0] + (12-j) * 58 + mul, octopus0.position[1] + i * 60)
                if globals()[ennemie_deplace].image == a:
                    globals()[ennemie_deplace].image = b
                else:
                    globals()[ennemie_deplace].image = a
                if (pg.Rect.colliderect(globals()[ennemie_deplace].hitbox, bordure_droite) and Ennemie.Ennemie_state == 1) or (pg.Rect.colliderect(globals()[ennemie_deplace].hitbox, bordure_gauche) and Ennemie.Ennemie_state == -1):
                    Ennemie.Ennemie_state = Ennemie.Ennemie_state * -1
                    octopus0.position = (octopus0.position[0], octopus0.position[1] + vitesse_horizontale)
            globals()[ennemie_deplace].hitbox_mouvement()

def collision(Projectile_allie):
    """Permet la collision entre le projectile et les ennemies

    Parameters
    ----------
    Projectile_allie : class
        projectile que le joueur tir
    """
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
            ennemie = nomennemie + str(j)
            #pg.draw.rect(screen, "red", globals()[affiche_ennemie].hitbox)
            if pg.Rect.colliderect(globals()[ennemie].hitbox, Projectile_allie.hitbox):
                Joueur.a = 0
                globals()[ennemie].position = (0, 0)
                globals()[ennemie].life = 0
                Projectile_allie.position = (0, 0)
                #vitesse_ennemie = vitesse_ennemie + 50
