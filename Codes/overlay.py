from generation import *

def menu_screen(): 
    """Permet l'affichage des éléments présents sur le menu
    """
    screen.fill((0,0,0))
    font = pg.font.SysFont(pixelfont, 40)
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    play_txt = font.render('PLAY', True, (255,255, 255))
    play_width = play_txt.get_width()
    play_height = play_txt.get_height()
    play = pg.transform.scale(play_txt, (int(play_width*3), int(play_height*3)))
    quit_txt = font.render('QUIT', True, (255, 255, 255))
    quit_width = quit_txt.get_width()
    quit_height = quit_txt.get_height()
    quit = pg.transform.scale(quit_txt, (int(quit_width*3), int(quit_height*3)))

    if width / 2.8 <= mouse[0] <= width / 2.8 + 450 and height / 2 <= mouse[1] <= height / 2 + 100:
        pg.draw.rect(screen, (58 , 60 , 64), [width / 2.8, height / 2, 450, 100], 0)
            
    else:
        pg.draw.rect(screen, (79 , 82 , 87), [width / 2.8, height / 2, 450, 100], 0)
        
    
    screen.blit(play, [screen.get_rect().centerx - 1.5*play_width, height / 2 + play_height/2])

    if width / 2.8 <= mouse[0] <= width / 2.8 + 450 and height / 2 + 200 <= mouse[1] <= height / 2 + 300:
        pg.draw.rect(screen, (58 , 60 , 64), [width / 2.8, height / 2 + 200, 450, 100], 0)
          
    else:
        pg.draw.rect(screen, (79 , 82 , 87), [width / 2.8, height / 2 + 200, 450, 100], 0)
    
    
    screen.blit(quit, [screen.get_rect().centerx - 1.5*quit_width, height / 2 + quit_height/2 + 200])
    
    logo_img = pg.image.load('Images/logo.png')
    logo_width = logo_img.get_width()
    logo_height = logo_img.get_height()
    logo = pg.transform.scale(logo_img, (int(logo_width*0.6),int(logo_height*0.6)))
    screen.blit(logo, (1920 / 1.25 /2 - logo.get_width()/2, 1080 / 1.25 /2 - 1.5*logo.get_height()))

def game_over_screen():
    """Permet l'affichage des éléments présents sur l'écran de game over
    """
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
    """Permet l'affichage des informations utiles pour le joueur
    """
    nbvie = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagevie = nbvie.render('Life:' + str(laser.life), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagevie, (20, 20))  # affichage du font
    score = pg.font.Font(pixelfont, 30)  # création d'un font
    affichagescore = score.render('Score:' + str(variable_score), True, 'White')  # ajout d'un texte sur le font
    screen.blit(affichagescore, (20, 50))  # affichage du font
    # time_elapsed = pg.time.get_ticks()
    # font = pg.font.Font(pixelfont, 40)
    # text = font.render('Time Elapsed: {} ms'.format(time_elapsed), True, "white")
    # screen.blit(text, (0, 200))



def affichage():
    """Permet l'affichage du menu, du jeu et de l'écran de game over au bon mement
    """
    menu_screen()
    if pg.key.get_pressed()[pg.K_SPACE]:

        screen.fill("black")
        bordure_gauche = pg.Rect(0, 0, 400 / 1.25, 1080 / 1.25)
        bordure_droite = pg.Rect(1520 / 1.25, 0, 400 / 1.25, 1080 / 1.25)
        # créer les bordures
        pg.draw.rect(screen, "black", bordure_gauche)
        pg.draw.rect(screen, "black", bordure_droite)
        autoaffichage()
        screen.blit(ufo.image, ufo.position)  # affichage de l'UFO
        screen.blit(laser.image, laser.position)  # affichage du Laser
        laser.tir(projectile_allie)
        for i in range(0, 4):
            nom = ((370 + i * 225, 570), (390 + i * 225, 550), (470 + i * 225, 550), (490 + i * 225, 570),
                (490 + i * 225, 670), (470 + i * 225, 670), (450 + i * 225, 650), (410 + i * 225, 650),
                (390 + i * 225, 670), (370 + i * 225, 670))
            pg.draw.polygon(screen, "green", nom)




        scoreboard()  # appel de la fonction scoreboard









