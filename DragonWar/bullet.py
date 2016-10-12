import random

from pico2d import *

class CharacterBullet:
    def __init__(self, x, y):
        self.image = load_image('bullet/bullet_5.png')
        self.x, self.y = x, y + 37
        #if select == 1:
        #    self.image = load_image('bullet/bullet_1.png')
        #    self.x, self.y = x, y + 37
        #if select == 2:
        #    self.image = load_image('bullet/bullet_2.png')
        #    self.x, self.y = x, y + 57
        #if select == 3:
        #    self.image = load_image('bullet/bullet_3.png')
        #    self.x, self.y = x, y + 61
        #if select == 4:
        #    self.image = load_image('bullet/bullet_4.png')
        #    self.x, self.y = x, y + 61
        #if select == 5:
        #    self.image = load_image('bullet/bullet_5.png')
        #    self.x, self.y = x, y + 64

    def update(self):
        self.y += 1

    def draw(self):
        self.image.draw(self.x, self.y)

class MonsterBullet:
    def __init__(self, x, y):
        self.image = load_image('bullet/enemy_bullet_1.png')
        self.x, self.y = x, y + 26

    def update(self):
        self.y -= 1

    def draw(self):
        self.image.draw(self.x, self.y)