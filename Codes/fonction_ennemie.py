from generation_ennemie import *

def autoaffichage():
    """
    Affichage auto des ennemies précédement créée si leur vie est supérieur à 1
    :return:
    """
    for Ennemies in Ennemie.Ennemielist[1:]:
        if Ennemies.life > 0:
            # pg.draw.rect(screen, "red", globals()[affiche_ennemie].hitbox)
            screen.blit(Ennemies.image, Ennemies.position)

def ennemie_tir():
    for i, Ennemies in enumerate(Ennemie.Ennemielist[1:]):
        print(Ennemies.name, Ennemies.Ennemielist[(i % 11) + 45].name)
        if (Ennemies.life > 0 and Ennemies.Ennemielist[(i + 11) % 55 +1].position == (0, -100)) or Ennemies.Ennemielist[(i % 11) + 45].position == Ennemies.position:
            Ennemies.tir(Projectile_ennemie)
            Ennemie.statut_projectile = -1
