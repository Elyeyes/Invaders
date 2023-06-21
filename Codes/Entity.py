from Projectile import *

class Entity:
    def __init__(self, name, image, life, position, velocity):
        self.name = name
        self.image = image
        self.life = life
        self.position = position
        self.velocity = velocity

    def get_center(self):
        return self.position[0] + self.image.get_width() / 2 - 2, self.position[1] + self.image.get_height() / 2

# sous-classe joueur
class Joueur(Entity):
    score_joueur = 0
    statut_projectile = 0
    hitbox1 = pg.Rect(0, 0, 60, 20)
    hitbox2 = pg.Rect(0, 0, 12, 20)
    # fonction déplacement du joueur

    def deplacement(self):
        self.hitbox1 = Joueur.hitbox1
        self.hitbox2 = Joueur.hitbox2
        self.hitbox1.topleft = (self.position[0], self.position[1] + 12)
        self.hitbox2.topleft = (self.position[0] + 24, self.position[1] + 4)
        # print(self.hitbox2.y)

        if 400 / 1.25 <= self.position[0] <= 1520 / 1.25 - 60:
            if pg.key.get_pressed()[pg.K_RIGHT]:
                self.position = (self.position[0] + self.velocity, self.position[1])
                self.hitbox1.topleft = (self.position[0], self.position[1] + 12)
                self.hitbox2.topleft = (self.position[0] + 24, self.position[1] + 4)
            if pg.key.get_pressed()[pg.K_LEFT]:
                self.position = (self.position[0] - self.velocity, self.position[1])

                self.hitbox1.topleft = (self.position[0], self.position[1] + 12)
                self.hitbox2.topleft = (self.position[0] + 24, self.position[1] + 4)

        elif self.position[0] <= 400 / 1.25:
            self.position = (400 / 1.25, self.position[1])
        elif 1520 / 1.25 - 60 <= self.position[0]:
            self.position = (1520 / 1.25 - 60, self.position[1])

    def tir(self, tir):
        if pg.key.get_pressed()[pg.K_SPACE] and tir.position == (1800, 1800):
            tir.position = self.get_center()
            Joueur.statut_projectile = 1
        if Joueur.statut_projectile == 1:
            tir.deplacement(Joueur)


# sous-classe ennemie
class Ennemie(Entity):
    Ennemie_state = 1
    statut_projectile = 0
    Ennemielist = []
    def __init__(self, size, name, image, life, position, velocity, score):
        super().__init__(name, image, life, position, velocity)
        self.size = size
        self.hitbox = pg.Rect(0, 0, self.size[0], self.size[1])
        self.hitbox.topleft = (self.position[0], self.position[1])
        self.score = score
        Ennemie.Ennemielist.append(self)
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

    def tir(self, tir):
        if tir.position == (1800, 1800):
            tir.position = self.get_center()
            Ennemie.statut_projectile = -1
        if Ennemie.statut_projectile == -1:
            tir.deplacement(Ennemie)

class Ufo(Entity):
    hitbox = pg.Rect(0, 0, 64, 20)
    def deplacement(self):
        self.hitbox = Ufo.hitbox
        self.hitbox.topleft = (self.position[0], self.position[1])
        self.position = (self.position[0] + self.velocity, self.position[1])
