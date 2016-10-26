import random

from pico2d import *

class DragonWarrior:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 0.1 m
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y =192, 50
        self.character_frame = 0
        self.total_frames = 0.0
        self.image = load_image('unit/character.png')
        self.dir = 1
        self.leftkey = False
        self.rightkey = False
        self.hp = 100
        self.level = 1

    def update(self, frame_time):
        distance = DragonWarrior.RUN_SPEED_PPS * frame_time
        self.total_frames += DragonWarrior.FRAMES_PER_ACTION * DragonWarrior.ACTION_PER_TIME * frame_time
        self.character_frame = int(self.total_frames) % 4

        if self.leftkey == True:
            self.x = max(0, self.x + (self.dir * distance))
        elif self.rightkey == True:
            self.x = min(384, self.x + (self.dir * distance))


    def draw(self):
        self.image.clip_draw(self.character_frame * 75, 0, 75, 75, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.dir = -1
            self.leftkey = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.dir = 1
            self.leftkey = False

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.rightkey = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.rightkey = False

    def changelevel(self):
        print("불렛 레벨 : %d" %(self.level))
        self.level += 1
        if self.level > 5:
            self.level = 1