import random

from pico2d import *

class Dragon:
    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 0.5 m
    RUN_SPEED_KMPH = 50.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x,self.y= 100,70
        self.frame = 0
        self.total_frames = 0.0
        self.image= load_image("unit/monster_0.png")
        self.dir = -1


    def update(self, frame_time):
        distance = Dragon.RUN_SPEED_PPS * frame_time
        self.total_frames += Dragon.FRAMES_PER_ACTION * Dragon.ACTION_PER_TIME * frame_time
        self.character_frame = int(self.total_frames) % 4

        self.y += (self.dir * distance)

        if self.y <= -500:
            self.y = 900
    def draw(self):
        self.image.clip_draw(self.frame * 75, 0, 75, 75, self.x, self.y)