# import sys
from overlay import *


pg.init()  # initialise pygame objects
pg.display.set_caption('Space Invaders')  # change le nom de la fenetre créée

def quitter(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        print(pg.mouse.get_pos())
        Laser.life = Laser.life - 1
    if event.type == pg.QUIT:
        pg.quit()
        quit()


def space_invaders():
    """
    :return:
    """
    generation_ennemie()
    while True:
        Constants.temps = pg.time.get_ticks()
        if Laser.life > 0:
            affichage()
            collision_ennemie(Projectile_allie)
            collision_ufo(UFO, Projectile_allie)
            collision_projectile(Projectile_allie, Projectile_ennemie)
            collision_allie(Laser, Projectile_ennemie)
        elif Laser.life <= 0:
            game_over_screen()  # game over temporaire
        if Constants.temps - Constants.seuil > Constants.delai:
            deplacement_ennemie(pg.Rect(1520 / 1.25, 0, 400 / 1.25, 1080 / 1.25), pg.Rect(0, 0, 400 / 1.25, 1080 / 1.25))
            Constants.seuil = Constants.temps

        if Constants.temps - Constants.seuil2 > Constants.delai2 and UFO.position[0] < 1800:
            UFO.deplacement()
        elif UFO.position[0] >= 1800:
            UFO.position = (50, 10)
            Constants.seuil2 = Constants.seuil2 + Constants.temps

        pg.display.update()
        for event in pg.event.get():
            # pg.draw.rect(screen, "red", Laser.hitbox1)
            # pg.draw.rect(screen, "red", Laser.hitbox2)
            quitter(event)


space_invaders()
