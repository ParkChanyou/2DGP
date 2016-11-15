import random

from pico2d import *

class Items:
    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 2 m
    RUN_SPEED_KMPH = 80.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    coin_image = None
    gem_image = None

    def __init__(self, x, y, type):
        self.x, self.y = x, y + 37
        self.damage = 10
        self.dir = -1
        self.type = type
        if Items.coin_image == None:
            Items.coin_image = load_image('item/item_coin.png')
        if Items.gem_image == None:
            Items.gem_image = load_image('item/item_gem.png')


    def update(self, frame_time):
        distance = Items.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)


    def draw(self):
        if self.type == 1:
            self.coin_image.draw(self.x, self.y)
        elif self.type == 2:
            self.gem_image.draw(self.x, self.y)

    def get_bb(self):
        if self.type == 1:
            return self.x - 32, self.y - 32, self.x + 32, self.y + 32
        if self.type == 2:
            return self.x - 32, self.y - 32, self.x + 32, self.y + 32

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_type(self):
        return self.type