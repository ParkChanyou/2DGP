import random

from pico2d import *

class Meteo:
    PIXEL_PER_METER = (10.0 / 1.5)  # 10 pixel 1.5 m
    RUN_SPEED_KMPH = 250.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    warning_image = None
    line_image = None

    def __init__(self, x, y):
        if Meteo.image == None:
            Meteo.image = load_image('etc/meteo.png')
        if Meteo.warning_image == None:
            Meteo.warning_image = load_image('etc/warn_mark.png')
        if Meteo.line_image == None:
            Meteo.line_image = load_image('etc/meteo_laser.png')

        self.x, self.y = x, y + 512
        self.damage = 100
        self.dir = -1
        self.count = 1
        self.line_x, self.line_y = x, y;

    def update(self, frame_time):
        distance = Meteo.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)
        self.count += 1
        if(self.y <= -50):
            self.count = -1;

    def draw(self):
        if self.count >= 0 and self.count <= 10:
            self.warning_image.opacify(self.count % 2)
            self.warning_image.draw(192, 256)
        elif self.count > 30:
            self.line_image.draw(self.line_x, self.line_y + 206)
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 62, self.y - 62, self.x + 62, self.y + 62

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_damage(self):
        return self.damage

    def set_pos(self, x, y):
        self.line_x = x
        self.line_y = y