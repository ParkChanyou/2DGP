import random

from pico2d import *

class Character:
    def __init__(self):
        self.x, self.y =192, 50
        self.character_frame = 0
        self.image = load_image('unit/character.png')
        self.bKeyDown = False

    def update(self):
        self.character_frame = (self.character_frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.character_frame * 75, 0, 75, 75, self.x, 50)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if (event.key) == (SDLK_LEFT):
                print("왼쪽방향키 호출")
                self.x -= 1
            elif (event.key) == (SDLK_RIGHT):
                print("오른쪽방향키 호출")
                self.x += 1
