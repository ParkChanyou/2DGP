import random

from pico2d import *

class CharacterBullet:
    image = None
    def __init__(self, x, y):
        if CharacterBullet.image == None:
            CharacterBullet.image = load_image('bullet/bullet_1.png')
        self.x, self.y = x, y + 37
        self.damage = 10


    def update(self, level):
        """
        if level == 1:
            CharacterBullet.image = load_image('bullet/bullet_1.png')
        if level == 2:
            CharacterBullet.image = load_image('bullet/bullet_2.png')
        if level == 3:
            CharacterBullet.image = load_image('bullet/bullet_3.png')
        if level == 4:
            CharacterBullet.image = load_image('bullet/bullet_4.png')
        if level == 5:
            CharacterBullet.image = load_image('bullet/bullet_5.png')
        """

        self.y += 1


    def draw(self):
        self.image.draw(self.x, self.y)

class MonsterBullet:
    image = None
    def __init__(self, x, y):
        if MonsterBullet.image == None:
            MonsterBullet.image = load_image('bullet/enemy_bullet_1.png')
        self.x, self.y = x, y + 26

    def update(self):
        self.y -= 1

    def draw(self):
        self.image.draw(self.x, self.y)