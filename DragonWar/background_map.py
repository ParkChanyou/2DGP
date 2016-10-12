import random

from pico2d import *

class Background:
    def __init__(self):
        self.background_frame = 0
        self.image = load_image('background/background_1.png')

    def draw(self):
        self.image.clip_draw(0, 0, 384, 512, 192, 256 + self.background_frame)
        self.image.clip_draw(0, 0, 384, 512, 192, 768 + self.background_frame)

    def update(self):
        self.background_frame -= 0.2
        if self.background_frame <= -512:
            self.background_frame = 0