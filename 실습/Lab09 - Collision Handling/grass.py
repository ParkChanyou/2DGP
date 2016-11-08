import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x, self.y = 400, 30

    def draw(self):
        self.image.draw(400, 30)

    def get_bb(self):
        return self.x - 399, self.y - 30, self.x + 399, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

