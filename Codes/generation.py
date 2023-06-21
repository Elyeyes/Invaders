from Entity import *

UFO = Ufo("UFO", Forme.UFO, 1, (50, 10), 2)
Laser = Joueur("Laser", Forme.Laser, 3, (744, 800), Constants.vitesse_joueur)
Projectile_allie = Projectile((1800, 1800), Forme.Projectile, 5)
Projectile_ennemie = Projectile((1800, 8000), Forme.Projectile, -0.3)
octopus0 = Ennemie((0, 0), "octopus0", Forme.octopus1, 1, (420, 150), Constants.vitesse_ennemie, 0)  # initialise une entité servant de référence pour la position de toutes les autres

def generation_obstacle():
    """
    genère les 4 obtacles
    :return:
    """
    for i in range(0, 4):
        nom = ((370 + i * 225, 570), (390 + i * 225, 550), (470 + i * 225, 550), (490 + i * 225, 570),
               (490 + i * 225, 670), (470 + i * 225, 670), (450 + i * 225, 650), (410 + i * 225, 650),
               (390 + i * 225, 670), (370 + i * 225, 670))
        pg.draw.polygon(screen, "green", nom)



Obstacle0 = Obstacle("Obstacle0", (370 + 0 * 225, 570))
Obstacle1 = Obstacle("Obstacle1", (370 + 1 * 225, 570))
Obstacle2 = Obstacle("Obstacle2", (370 + 2 * 225, 570))
Obstacle3 = Obstacle("Obstacle1", (370 + 3 * 225, 570))
