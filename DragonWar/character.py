import random

from pico2d import *

class Character:
    def __init__(self):
        self.x, self.y =192, 50
        self.character_frame = 0
        self.image = load_image('unit/character.png')
        self.dir = 1
        self.leftkey = False
        self.rightkey = False
        self.hp = 100
        self.level = 1

    def update(self):
        self.character_frame = (self.character_frame + 1) % 4

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

        if self.leftkey == True:
            self.x += (self.dir * 5)
        elif self.rightkey == True:
            self.x += (self.dir * 5)

    def changelevel(self):
        print("%d", self.level)
        self.level += 1
        if self.level > 5:
            self.level = 1