import random

from pico2d import *

class Dragon:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 0.3 m
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y= 100, 500
        self.frame = 0
        self.total_frames = 0.0
        self.image= load_image("unit/monster_0.png")
        self.dir = -1
        self.type = 1
        self.hp = 10


    def update(self, frame_time):
        distance = Dragon.RUN_SPEED_PPS * frame_time
        self.total_frames += Dragon.FRAMES_PER_ACTION * Dragon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

        self.y += (self.dir * distance)

        if self.y <= -150:
            self.y = 700


    def draw(self):
        self.image.clip_draw(self.frame * 75, 0, 75, 75, self.x, self.y)


    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_type(self, type):
        self.type = type;
        if self.type == 1:
            self.image = load_image("unit/monster_0.png")
            self.hp = 10
        elif self.type == 2:
            self.image = load_image("unit/monster_1.png")
            self.hp = 20
        elif self.type == 3:
            self.image = load_image("unit/monster_2.png")
            self.hp = 30
        elif self.type == 4:
            self.image = load_image("unit/monster_3.png")
            self.hp = 40

    def set_damage(self, damage):
        self.hp = self.hp - damage
        return self.hp

    def get_bb(self):
        return self.x - 22, self.y - 25, self.x + 22, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class BossDragon():
    PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 0.2 m
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y= 192, 320
        self.frame = 0
        self.total_frames = 0.0
        self.image= load_image("unit/monster_5.png")
        self.dir = -1
        self.type = 1
        self.hp = 200


    def update(self, frame_time):
        distance = BossDragon.RUN_SPEED_PPS * frame_time
        self.total_frames += BossDragon.FRAMES_PER_ACTION * BossDragon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

        #self.y += (self.dir * distance)

        #if self.y <= -150:
        #    self.y = 700


    def draw(self):
        self.image.clip_draw(self.frame * 150, 0, 150, 150, self.x, self.y)


    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_damage(self, damage):
        self.hp = self.hp - damage
        return self.hp

    def get_bb(self):
        return self.x - 74, self.y - 74, self.x + 74, self.y + 74

    def draw_bb(self):
        draw_rectangle(*self.get_bb())