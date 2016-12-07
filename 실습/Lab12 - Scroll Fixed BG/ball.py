import random

from pico2d import *

class Ball:

    image = None;

    def __init__(self):
        self.x, self.y = random.randint(200, 790), 60
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


class FreeBall:
    image = None;

    def __init__(self):
        #self.x, self.y = random.randint(200, 790), random.randint(60, 590)
        self.x, self.y = random.randint(200, 3590), random.randint(60, 1490)
        if FreeBall.image == None:
            FreeBall.image = load_image('ball21x21.png')

    def update(self, frame_time):
        pass

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.draw(sx, sy)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self, bg):
        self.bg = bg

    def set_pos(self, x, y):
        self.x = x + self.bg.window_left
        self.y = self.bg.canvas_height - y + self.bg.window_bottom


class BigBall(Ball):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = random.randint(200,300)
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.parent = None


    def stop(self):
        self.fall_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            self.y -= frame_time * self.fall_speed

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def set_parent(self, brick):
        self.parent = brick
        self.rx = self.x - brick.x
        self.ry = self.y - brick.y
        pass