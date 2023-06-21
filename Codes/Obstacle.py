from Explosion import *
class Obstacle():
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.area = ((0 + self.position[0], 0 + self.position[1]), (20 + self.position[0], -20 + self.position[1]), (100 + self.position[0], -20 + self.position[1]), (120 + self.position[0], 0 + self.position[1]),
                    (120 + self.position[0], 100 + self.position[1]), (100 + self.position[0], 100 + self.position[1]), (80 + self.position[0], 80 + self.position[1]), (40 + self.position[0], 80 + self.position[1]),
                    (20 + self.position[0], 100 + self.position[1]), (0 + self.position[0], 100 + self.position[1]))
        self.hitbox1 = pg.Rect(self.area[1][0], self.area[1][1], 80, 110)
        self.hitbox1.topleft = (self.area[1])

        self.hitbox2 = pg.Rect(self.area[0][0], self.area[0][1], 20, 110)
        self.hitbox2.topleft = (self.area[0][0], self.area[0][1] - 10)

        self.hitbox3 = pg.Rect(self.area[2][0], self.area[2][1], 20, 110)
        self.hitbox3.topleft = (self.area[2][0], self.area[2][1] + 10)

# Obstacletest = Obstacle("Obstacletest", (300, 500))