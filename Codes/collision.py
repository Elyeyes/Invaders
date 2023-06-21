from fonction_ennemie import *

explosion = (
(395, 300),
(390, 295),
(396, 296),
(397, 290),
(401, 295),
(406, 292),
(404, 297),
(410, 300.0),
(404, 302),
(406, 307),
(401, 304),
(397, 309),
(396, 303),
(390, 304),
)

def collision_ennemie(projectile_allie):
    """
    Fonction qui vérifie pour chaques ennemies si il est touché par le projectile tiré par le joueur,
    et si oui lui enlève de la vie et n'est plus affiché, aussi le projectile disparait.
    :param projectile_allie:
    :return:
    """
    for Ennemies in Ennemie.Ennemielist[1:]:
        if Ennemies.life > 0:
            # pg.draw.rect(screen, "red", Ennemies.hitbox)
            screen.blit(Ennemies.image, Ennemies.position)
            # pg.draw.rect(screen, "red", Ennemies.hitbox)
            if pg.Rect.colliderect(Ennemies.hitbox, projectile_allie.hitbox):
                Joueur.statut_projectile = 0
                projectile_allie.position = (1800, 1800)
                projectile_allie.hitbox.topleft = (projectile_allie.position[0], projectile_allie.position[1])
                Ennemies.position = (0, -100)
                Ennemies.life = 0
                Constants.delai = Constants.delai - 10
                Constants.vitesse_ennemie = Constants.vitesse_ennemie + 5
                Joueur.score_joueur += Ennemies.score


def collision_ufo(UFO, projectile_allie):
    if pg.Rect.colliderect(UFO.hitbox, projectile_allie.hitbox):
        Joueur.statut_projectile = 0
        projectile_allie.position = (1800, 1800)
        projectile_allie.hitbox.topleft = projectile_allie.position
        UFO.position = (50, 10)
        Joueur.score_joueur += 100

def collision_projectile(projectile_allie, projectile_ennemie):
    if pg.Rect.colliderect(projectile_ennemie.hitbox, projectile_allie.hitbox):
        Joueur.statut_projectile = 0
        Ennemie.statut_projectile = 0
        projectile_allie.position = (1800, 1800)
        projectile_ennemie.position = (1800, 15000)
        projectile_allie.hitbox.topleft = projectile_allie.position
        projectile_ennemie.hitbox.topleft = projectile_ennemie.position

def collision_allie(laser, projectile_ennemie):
    if pg.Rect.colliderect(projectile_ennemie.hitbox, laser.hitbox1) or pg.Rect.colliderect(projectile_ennemie.hitbox, laser.hitbox2):
        Ennemie.statut_projectile = 0
        projectile_ennemie.position = (1800, 15000)
        projectile_ennemie.hitbox.topleft = projectile_ennemie.position
        laser.life = laser.life - 1

def collision_obstacle(projectile):
    for i in range(0, 4):
        nom = ((370 + i * 225, 570), (390 + i * 225, 550), (470 + i * 225, 550), (490 + i * 225, 570),
               (490 + i * 225, 670), (470 + i * 225, 670), (450 + i * 225, 650), (410 + i * 225, 650),
               (390 + i * 225, 670), (370 + i * 225, 670))
        for j in range(len(nom)-1):
            print(nom[j], nom[j+1])

collision_obstacle(Projectile_allie)
