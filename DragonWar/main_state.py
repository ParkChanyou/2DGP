import random
import json
import os

from pico2d import *

import game_framework
import title_state
from background_map import Background
from character import Character



name = "MainState"

font = None
background = None
character = None
character_bullet = []
monsters = []
monster_bullet = []





def enter():
    global background, character, monsters
    background = Background()
    character = Character()


def exit():
    global background, character, monsters, character_bullet, monster_bullet
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            character.handle_event(event)


def update():
    background.update()
    character.update()

    hide_cursor()


def draw():
    clear_canvas()

    background.draw()
    character.draw()

    update_canvas()





