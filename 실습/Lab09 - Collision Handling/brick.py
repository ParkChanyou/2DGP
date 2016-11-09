import random

from pico2d import *

class Brick:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(200, 790), 200
        self.speed = 100
        self.dir = 1
        self.distance = 0
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')

    def update(self, frame_time):
        self.distance = self.dir * frame_time * self.speed
        self.x += self.distance

        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_speed(self):
        return self.distance

    def get_pos(self):
        return self.x, self.y