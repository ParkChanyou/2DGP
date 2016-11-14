import random

from pico2d import *

class Background:
    PIXEL_PER_METER = (10.0 / 1)  # 10 pixel 1 m
    RUN_SPEED_KMPH = 50.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.background_frame = 0
        self.image = load_image('background/background_1.png')
        self.first_pos = 0
        self.last_pos = 0

    def draw(self):
        self.image.clip_draw(0, 0, 384, 512, 192, 256 + self.background_frame)
        self.image.clip_draw(0, 0, 384, 512, 192, 768 + self.background_frame)

    def update(self, frame_time):
        distance = Background.RUN_SPEED_PPS * frame_time
        self.background_frame -= distance
        self.last_pos += distance
        degree = self.last_pos - self.first_pos
        degree = degree / 10
        if degree >= 768 and degree < 1536:
            self.image = load_image('background/background_2.png')
        elif degree >= 1536:
            self.image = load_image('background/background_3.png')
        if self.background_frame <= -512:
            self.background_frame = 0

    def degree(self):
        degree = self.last_pos - self.first_pos
        degree = degree / 10
        return degree