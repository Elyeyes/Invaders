from Constants import *

class Projectile(pg.sprite.Sprite):
    def __init__(self, position, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.position = position
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.position[0], self.position[1])

    def get_center(self):
        return self.position[0] + self.image.get_width() / 2, self.position[1] + self.image.get_height() / 2

    def deplacement(self):
        if self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 5)
            self.hitbox = self.image.get_rect()
            self.hitbox.topleft = (self.position[0], self.position[1])
        else:
            self.position = (0, 0)
            self.hitbox = self.image.get_rect()
            self.hitbox.topleft = (self.position[0], self.position[1])
            screen.blit(self.image, self.position)

class Entity:
    def __init__(self, name, image, life, position, velocity):
        self.name = name
        self.image = image
        self.life = life
        self.position = position
        self.velocity = velocity

    def get_center(self):
        return self.position[0] + self.image.get_width() / 2, self.position[1] + self.image.get_height() / 2


# sous-classe joueur
class Joueur(Entity):
    score_joueur = 0
    a = 0
    # fonction déplacement du joueur

    def deplacement(self):
        pg.key.set_repeat(1)  # Permet au touche du clavier de continuer de fonctionner une fois enfoncé
        self.hitbox1 = pg.Rect(0, 0, 60, 20)
        self.hitbox1.topleft = (self.position[0], self.position[1] + 12)
        self.hitbox2 = pg.Rect(0, 0, 12, 20)
        self.hitbox2.topleft = (self.position[0] + 24, self.position[1] + 4)
        # print(self.hitbox2.y)
        if pg.key.get_pressed():
            if 400 / 1.25 <= self.position[0] <= 1520 / 1.25 - 60:
                if pg.key.get_pressed()[pg.K_RIGHT]:
                    self.position = (self.position[0] + self.velocity, self.position[1])
                if pg.key.get_pressed()[pg.K_LEFT]:
                    self.position = (self.position[0] - self.velocity, self.position[1])

            elif self.position[0] <= 400 / 1.25:
                self.position = (400 / 1.25, self.position[1])

            elif 1520 / 1.25 - 60 <= self.position[0]:
                self.position = (1520 / 1.25 - 60, self.position[1])

    def tir(self, Tir):
        if pg.key.get_pressed()[pg.K_SPACE] and Tir.position == (0, 0):
            Tir.position = self.get_center()
            Joueur.a = 1
        if Joueur.a == 1:
            Tir.deplacement()
            screen.blit(Tir.image, Tir .position)

# sous-classe ennemie
class Ennemie(Entity):
    Ennemie_state = 1

    def __init__(self, size, name, image, life, position, velocity):
        super().__init__(name, image, life, position, velocity)
        self.size = size
        self.hitbox = pg.Rect(0, 0, self.size[0], self.size[1])
        self.hitbox.topleft = (self.position[0], self.position[1])

        # pg.draw.rect(screen, "red", self.hitbox)
        # print(self.hitbox.y)

    # fonction déplacement des ennemis
    def deplacement(self):
        if Ennemie.Ennemie_state == 1:
            self.position = (self.position[0] + self.velocity, self.position[1])
        elif Ennemie.Ennemie_state == -1:
            self.position = (self.position[0] - self.velocity, self.position[1])

    #fonction pour que la hitbox suive l'entité
    def hitbox_mouvement(self):
        self.hitbox = pg.Rect(0, 0, self.size[0], self.size[1])
        self.hitbox.topleft = (self.position[0], self.position[1])


class Ufo(Entity):
    def deplacement(self):
        self.hitbox = pg.Rect(0, 0, 64, 20)
        self.hitbox.topleft = (self.position[0], self.position[1])
        # print(self.hitbox.y)
        self.position = (self.position[0] + self.velocity, self.position[1])
        # pg.draw.rect(screen, "red", self.hitbox)
