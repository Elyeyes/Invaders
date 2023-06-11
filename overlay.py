import pygame as pg
from generation import *

def game_over_screen():
   screen.fill((0, 0, 0))
   font = pg.font.SysFont('arial', 40)
   title = font.render('Game Over', True, (255, 255, 255))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (1080/3 - title.get_width()/2, 1980/3 - title.get_height()/3))
   screen.blit(restart_button, (1080/3 - restart_button.get_width()/2, 1980/3 + restart_button.get_height()))
   screen.blit(quit_button, (1080/3 - quit_button.get_width()/2, 1980/3 + quit_button.get_height()/2))
   pg.display.update()

# fonction scoreboard
def scoreboard():
    nbvie = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagevie = nbvie.render('Life:' + str(Laser.life), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagevie, (20, 20))  # affichage du font
    score = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagescore = score.render('Score:' + str(variable_score), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagescore, (20, 50))  # affichage du font

def affichage():
    screen.fill("black")
    autoaffichage()
    for i in range(0, 4):
        nom = "polygon" + str(i)
        nom = ((370 + i * 225, 570), (390 + i * 225, 550), (470 + i * 225, 550), (490 + i * 225, 570),
               (490 + i * 225, 670), (470 + i * 225, 670), (450 + i * 225, 650), (410 + i * 225, 650),
               (390 + i * 225, 670), (370 + i * 225, 670))
        pg.draw.polygon(screen, "green", nom)
    screen.blit(UFO.image, UFO.position)  # affichage de l'UFO
    screen.blit(Laser.image, Laser.position)  # affichage du joueur
    UFO.deplacement()
    # créer les bordures
    screen.fill("black", (0, 0, 400 / 1.25, 1080 / 1.25))
    screen.fill("black", (1520 / 1.25, 0, 400 / 1.25, 1080 / 1.25))

    scoreboard()  # appel de la fonction scoreboard
    if Laser.life <= 0:
        game_over_screen()  # game over temporaire
