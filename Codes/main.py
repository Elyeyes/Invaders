# import sys
from overlay import *


pg.init()  # initialise pygame objects
pg.display.set_caption('Space Invaders')  # change le nom de la fenetre créée

def quitter(event):
    """Permet la fermeture de la fenetre créée au lancement du programme
    """
    if event.type == pg.MOUSEBUTTONDOWN:
        print(pg.mouse.get_pos())
        laser.life = laser.life - 1
    if event.type == pg.QUIT:
        pg.quit()
        quit()


"""if (condition collision):
        life=life-1
if (condition collision squid):x²
if (condition collision crab):
    score=score+20
if (condition collision octopus):
    score=score+10
if (condition collision UFO):
    score=score+100"""


seuil = pg.time.get_ticks()

seuil2 = pg.time.get_ticks()
delai2 = 5
autogeneration()


def space_invaders(seuil, seuil2):
    """Permet de lancer une fenetre et d'y faire fonctionner le jeu

    Parameters
    ----------
    seuil1 : int
        nombre de milliseconds depuis le lancement du programme
    seuil2 : int
        nombre de milliseconds depuis le lancement du programme
    """
    autogeneration()
    while True:
        temps = pg.time.get_ticks()
        collision(projectile_allie)
        if laser.life > 0:
            affichage()
        elif laser.life <= 0:
            game_over_screen()  # game over temporaire
        if temps - seuil > delai:
            deplacement_ennemie(pg.Rect(1520 / 1.25, 0, 400 / 1.25, 1080 / 1.25), pg.Rect(0, 0, 400 / 1.25, 1080 / 1.25))
            seuil = temps
        ufo.deplacement()

        pg.display.update()
        if temps - seuil2 > delai2:
            seuil2 = temps

        for event in pg.event.get():
            laser.deplacement()  # appel fonction déplacement dans class joueur (pour le Laser)
            # pg.draw.rect(screen, "red", Laser.hitbox1)
            # pg.draw.rect(screen, "red", Laser.hitbox2)
            quitter(event)


space_invaders(seuil, seuil2)

