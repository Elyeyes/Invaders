from collision import *


def game_over_screen():
    screen.fill((0, 0, 0))
    font = pg.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (1080 / 3 - title.get_width() / 2, 1980 / 3 - title.get_height() / 3))
    screen.blit(restart_button, (1080 / 3 - restart_button.get_width() / 2, 1980 / 3 + restart_button.get_height()))
    screen.blit(quit_button, (1080 / 3 - quit_button.get_width() / 2, 1980 / 3 + quit_button.get_height() / 2))
    pg.display.update()


# fonction scoreboard
def scoreboard():
    nbvie = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagevie = nbvie.render('Life:' + str(Laser.life), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagevie, (20, 20))  # affichage du font
    score = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagescore = score.render('Score:' + str(Joueur.score_joueur), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagescore, (20, 50))  # affichage du font
    time_elapsed = pg.time.get_ticks()
    font = pg.font.Font(pixelfont, 40)
    text = font.render('Time Elapsed: {} ms'.format(time_elapsed), True, "white")
    screen.blit(text, (0, 200))


Explosion1 = Explosion((350, 600))
def affichage():
    screen.fill("black")
    # créer les bordures
    bordure_gauche = pg.Rect(0, 0, 400 / 1.25, 1080 / 1.25)
    bordure_droite = pg.Rect(1520 / 1.25, 0, 400 / 1.25, 1080 / 1.25)
    screen.blit(Projectile_allie.image, Projectile_allie.position)
    screen.blit(Projectile_ennemie.image, Projectile_ennemie.position)
    screen.blit(UFO.image, UFO.position)  # affichage de l'UFO
    screen.blit(Laser.image, Laser.position)  # affichage du Laser
    #affiche les bordures
    pg.draw.rect(screen, "black", bordure_gauche)
    pg.draw.rect(screen, "black", bordure_droite)


    # pg.draw.polygon(screen, "white", explosion)


    autoaffichage()
    Laser.tir(Projectile_allie)
    ennemie_tir()
    generation_obstacle()
    screen.blit(Explosion1.image, Explosion1.position)
    pg.draw.polygon(screen, "green", Obstacle0.area)
    pg.draw.polygon(screen, "green", Obstacle1.area)
    pg.draw.polygon(screen, "green", Obstacle2.area)
    pg.draw.polygon(screen, "green", Obstacle3.area)
    pg.draw.rect(screen, "red", Obstacle1.hitbox1)
    pg.draw.rect(screen, "red", Obstacle1.hitbox2)
    pg.draw.rect(screen, "red", Obstacle1.hitbox3)
    Laser.deplacement()  # appel fonction déplacement dans class joueur (pour le Laser)

    scoreboard()  # appel de la fonction scoreboard
