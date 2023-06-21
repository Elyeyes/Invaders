from Constants import *

class Explosion():
    Explosionlist = []

    def __init__(self, position):
        self.image = Forme.Explosion
        self.position = position[0] + self.image.get_width() / 2, position[1] + self.image.get_height() / 2
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.position[0], self.position[1])
        Explosion.Explosionlist.append(self)

    def get_center(self):
        return self.position[0] + self.image.get_width() / 2, self.position[1] + self.image.get_height() / 2

