import random

from pico2d import *

class CharacterBullet:
    PIXEL_PER_METER = (10.0 / 2)  # 10 pixel 2 m
    RUN_SPEED_KMPH = 300.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self, x, y):
        if CharacterBullet.image == None:
            CharacterBullet.image = load_image('bullet/bullet_1.png')
        self.x, self.y = x, y + 37
        self.damage = 10
        self.dir = 1
        self.level = 1


    def update(self, frame_time):
        distance = CharacterBullet.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)


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
            return self.x - 35, self.y - 60, self.x + 35, self.y + 60
        if self.level == 5:
            return self.x - 35, self.y - 60, self.x + 35, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def change_bullet(self, level):
        self.level = level
        if self.level == 1:
            CharacterBullet.image = load_image('bullet/bullet_1.png')
            self.damage = 10
        if self.level == 2:
            CharacterBullet.image = load_image('bullet/bullet_2.png')
            self.damage = 15
        if self.level == 3:
            CharacterBullet.image = load_image('bullet/bullet_3.png')
            self.damage = 20
        if self.level == 4:
            CharacterBullet.image = load_image('bullet/bullet_4_1.png')
            self.damage = 30
        if self.level == 5:
            CharacterBullet.image = load_image('bullet/bullet_5_1.png')
            self.damage = 40

"""
class MonsterBullet:
    PIXEL_PER_METER = (10.0 / 1)  # 10 pixel 2 m
    RUN_SPEED_KMPH = 200.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self, x, y):
        if MonsterBullet.image == None:
            MonsterBullet.image = load_image('bullet/enemy_bullet_1.png')
        self.x, self.y = x, y - 26
        self.damage = 10
        self.dir = -1

    def update(self, frame_time):
        distance = MonsterBullet.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 26, self.y - 26, self.x + 26, self.y + 26

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class BossBullet:
    PIXEL_PER_METER = (10.0 / 1)  # 10 pixel 2 m
    RUN_SPEED_KMPH = 200.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self, x, y):
        if BossBullet.image == None:
            BossBullet.image = load_image('bullet/enemy_bullet_1.png')
        self.x, self.y = x, y - 26
        self.damage = 10
        self.dir = -1
        self.pattern = 1

    def update(self, frame_time):
        distance = BossBullet.RUN_SPEED_PPS * frame_time
        if self.pattern == 1:
            self.y += (self.dir * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 26, self.y - 26, self.x + 26, self.y + 26

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def pattern(self, pattern):
        self.pattern = pattern
        if self.pattern == 1:
            BossBullet.image = load_image('bullet/enemy_bullet_1.png')
        elif self.pattern == 2:
            BossBullet.image = load_image('bullet/enemy_bullet_2.png')
"""
