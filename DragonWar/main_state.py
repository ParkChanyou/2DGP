import random
import json
import os

from pico2d import *

import game_framework
import title_state
from background_map import Background
from character import DragonWarrior
from monster import Dragon
from bullet import *



name = "MainState"

font = None
background = None
dragonwarrior = None
character_bullet = []
monsters = []
monster_bullet = []


current_time = 0.0


def enter():
    global background, dragonwarrior, monsters
    background = Background()
    dragonwarrior = DragonWarrior()
    monsters = Dragon()


def exit():
    global background, dragonwarrior, monsters, character_bullet, monster_bullet
    del(background)
    del(dragonwarrior)
    del(character_bullet)


def pause():
    pass


def resume():
    pass


def handle_events():
    global character_bullet

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            dragonwarrior.handle_event(event)

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            cBullets = CharacterBullet(dragonwarrior.x, dragonwarrior.y)
            character_bullet.append(cBullets)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            dragonwarrior.changelevel()


def update():
    global monsters

    show_cursor()

    frame_time = get_frame_time()

    background.update()
    dragonwarrior.update(frame_time)

    #임시로 넣어본 몬스터
    monsters.update(frame_time)

    for cbullet in character_bullet:
        cbullet.update(dragonwarrior.level)

        if cbullet.y >= 550:
            character_bullet.remove(cbullet)


def draw():
    clear_canvas()

    background.draw()
    dragonwarrior.draw()
    monsters.draw()

    for cbullet in character_bullet:
        cbullet.draw()

    update_canvas()


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



