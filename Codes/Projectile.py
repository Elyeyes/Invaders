from Obstacle import *

class Projectile(pg.sprite.Sprite):
    def __init__(self, position, image, vitesse):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.position = position
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.position[0], self.position[1])
        self.vitesse = vitesse
    def get_center(self):
        return self.position[0] + self.image.get_width() / 2, self.position[1] + self.image.get_height() / 2

    def deplacement(self, Joueur):
        if 2000 > self.position[1] > 0 and Joueur.statut_projectile != 0:
            self.position = (self.position[0], self.position[1] - self.vitesse)
            self.hitbox = self.image.get_rect()
            self.hitbox.topleft = (self.position[0], self.position[1])
        else:
            self.position = (1800, 1800)
            self.hitbox = self.image.get_rect()
            self.hitbox.topleft = (self.position[0], self.position[1])
            Joueur.statut_projectile = 0

