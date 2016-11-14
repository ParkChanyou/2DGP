import random
import json
import os

from pico2d import *

import game_framework
import title_state
import ranking_state
from background_map import Background
from character import DragonWarrior
from monster import Dragon
from bullet import CharacterBullet, MonsterBullet
from meteo import Meteo



name = "MainState"

font = None
background = None
dragonwarrior = None
character_bullets = []
monsters = []
monster_bullets = []
meteos = []


current_time = 0.0


def enter():
    global background, dragonwarrior, monsters
    background = Background()
    dragonwarrior = DragonWarrior()
    monsters = create_monster_team()


def exit():
    global background, dragonwarrior, monsters, character_bullets, monster_bullets
    del(background)
    del(dragonwarrior)
    del(character_bullets)


def pause():
    pass


def resume():
    pass


def handle_events():
    global character_bullets

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
            character_bullets.append(cBullets)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            dragonwarrior.changelevel()


def update():
    global monsters
    global current_time, meteos

    show_cursor()

    frame_time = get_frame_time()

    background.update(frame_time)
    dragonwarrior.update(frame_time)

    degree = background.degree()
    print(degree)

    if current_time >= 15 and current_time <= 15.1:
        meteo = Meteo(dragonwarrior.x, dragonwarrior.y)
        meteos.append(meteo)

    for meteo in meteos:
        meteo.update(frame_time)

    if len(monsters) == 0:
        monsters = create_monster_team()

    for monster in monsters:
        monster.update(frame_time)
        if monster.y <= -50:
            monsters = create_monster_team()
        if collide(monster, dragonwarrior):
            print("캐릭터와 몬스터 충돌")

    create_monster_bullet()

    for cbullet in character_bullets:
        cbullet.update(frame_time)
        cbullet.change_bullet(dragonwarrior.get_level())
        if cbullet.y >= 550:
            character_bullets.remove(cbullet)
        for monster in monsters:
            if collide(monster, cbullet):
                #print("총알과 몬스터 충돌")
                if monster.set_damage(cbullet.get_damage()) <= 0:
                    monsters.remove(monster)
                character_bullets.remove(cbullet)


def draw():
    clear_canvas()

    background.draw()
    dragonwarrior.draw()
    dragonwarrior.draw_bb()

    for monster in monsters:
        monster.draw()
        monster.draw_bb()

    for cbullet in character_bullets:
        cbullet.draw()
        cbullet.draw_bb()

    for meteo in meteos:
        meteo.draw()

    update_canvas()


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def create_monster_team():
    team = []

    monster1 = Dragon()
    monster1.set_pos(38.4*1, 900)
    monster1.set_type(random.randint(1, 4))
    team.append(monster1)

    monster2 = Dragon()
    monster2.set_pos(38.4*3, 900)
    monster2.set_type(random.randint(1, 4))
    team.append(monster2)

    monster3 = Dragon()
    monster3.set_pos(38.4*5, 900)
    monster3.set_type(random.randint(1, 4))
    team.append(monster3)

    monster4 = Dragon()
    monster4.set_pos(38.4*7, 900)
    monster4.set_type(random.randint(1, 4))
    team.append(monster4)

    monster5 = Dragon()
    monster5.set_pos(38.4*9, 900)
    monster5.set_type(random.randint(1, 4))
    team.append(monster5)

    return team


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def create_monster_bullet():
    pass
