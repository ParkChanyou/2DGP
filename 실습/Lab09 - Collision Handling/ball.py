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

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class BigBall(Ball):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = random.randint(50,120)
        self.move_speed = 0
        self.save_fall_speed = self.fall_speed
        self.check = False
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')

    def update(self, frame_time):
        self.y -= frame_time * self.fall_speed
        if self.fall_speed == 0:
            self.x += self.move_speed

    def stop(self):
        if self.check == False:
            self.fall_speed = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def set_speed(self, speed):
        self.move_speed = speed

    def set_pos(self, x, y):
        if self.x + 20 <= x - 90:
            self.check = True
            self.move_speed = 0
            self.fall_speed = self.save_fall_speed
        elif self.x - 20 >= x + 90:
            self.check = True
            self.move_speed = 0
            self.fall_speed = self.save_fall_speed


