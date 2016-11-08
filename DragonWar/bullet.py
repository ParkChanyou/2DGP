import random

from pico2d import *

class CharacterBullet:
    image = None
    def __init__(self, x, y):
        if CharacterBullet.image == None:
            CharacterBullet.image = load_image('bullet/bullet_1.png')
        self.x, self.y = x, y + 37
        self.damage = 10
        self.dir = 1
        self.level = 1


    def update(self, level):
        self.level = level
        if self.level == 1:
            CharacterBullet.image = load_image('bullet/bullet_1.png')
        if self.level == 2:
            CharacterBullet.image = load_image('bullet/bullet_2.png')
        if self.level == 3:
            CharacterBullet.image = load_image('bullet/bullet_3.png')
        if self.level == 4:
            CharacterBullet.image = load_image('bullet/bullet_4.png')
        if self.level == 5:
            CharacterBullet.image = load_image('bullet/bullet_5.png')

        self.y += self.dir


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        if self.level == 1:
            return self.x - 15, self.y - 34, self.x + 15, self.y + 34
        if self.level == 2:
            return self.x - 23, self.y - 50, self.x + 23, self.y + 50
        if self.level == 3:
            return self.x - 35, self.y - 60, self.x + 35, self.y + 60
        if self.level == 4:
            return self.x - 64, self.y - 60, self.x + 64, self.y + 60
        if self.level == 5:
            return self.x - 62, self.y - 62, self.x + 62, self.y + 62

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class MonsterBullet:
    image = None
    def __init__(self, x, y):
        if MonsterBullet.image == None:
            MonsterBullet.image = load_image('bullet/enemy_bullet_1.png')
        self.x, self.y = x, y + 26
        self.damage = 10
        self.dir = -1

    def update(self):
        self.y += self.dir

    def draw(self):
        self.image.draw(self.x, self.y)