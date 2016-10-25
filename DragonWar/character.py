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

        if self.leftkey == True:
            self.x = max(0, self.x + (self.dir))
        elif self.rightkey == True:
            self.x = min(384, self.x + (self.dir))

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
        print("%d", self.level)
        self.level += 1
        if self.level > 5:
            self.level = 1