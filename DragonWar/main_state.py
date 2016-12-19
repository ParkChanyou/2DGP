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
from bullet import CharacterBullet
from meteo import Meteo
from item import Items



name = "MainState"

font = None
background = None
dragonwarrior = None
character_bullets = []
monsters = []
monster_bullets = []
meteos = []
items = []


current_time = 0.0

boss_degree = 1792


def enter():
    global font, background, dragonwarrior, monsters
    font = load_font('etc/barun.ttf')
    background = Background()
    dragonwarrior = DragonWarrior()
    monsters = create_monster_team()



def exit():
    global background, dragonwarrior, monsters, character_bullets, monster_bullets

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    ranking_data.append({'Score':dragonwarrior.score, 'Degree':background.degree()})

    f = open('ranking_data.txt', 'w')
    json.dump(ranking_data, f)
    f.close()

    #del(background)
    #del(dragonwarrior)
    #del(character_bullets)
    #del(monsters)


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
        elif dragonwarrior.die == True:
            game_framework.change_state(ranking_state)
        else:
            dragonwarrior.handle_event(event)

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            cBullets = CharacterBullet(dragonwarrior.x, dragonwarrior.y)
            character_bullets.append(cBullets)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            dragonwarrior.changelevel()


def update():
    global monsters, character_bullets
    global current_time, meteos
    global boss_degree

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

    if degree < boss_degree:
        if len(monsters) == 0:
            monsters = create_monster_team()
        for monster in monsters:
            monster.update(frame_time)
            if monster.y <= -50:
                monsters = create_monster_team()
            if collide(monster, dragonwarrior):
                print("캐릭터와 몬스터 충돌")
                dragonwarrior.die = True;

    for cbullet in character_bullets:
        cbullet.update(frame_time)
        cbullet.change_bullet(dragonwarrior.level)
        if cbullet.y >= 550:
            character_bullets.remove(cbullet)
        for monster in monsters:
            if collide(monster, cbullet):
                #print("총알과 몬스터 충돌")
                if monster.set_damage(cbullet.damage) <= 0:
                    monsters.remove(monster)
                    score_increase(monster.type)
                    randint = random.randint(0, 100)
                    if randint >= 0 and randint <= 70:
                        item = Items(monster.x, monster.y, 1)
                    elif randint > 70 and randint <= 100:
                        item = Items(monster.x, monster.y, 2)
                    items.append(item)
                if character_bullets.count(cbullet) >= 1:
                    character_bullets.remove(cbullet)

    for item in items:
        item.update(frame_time)
        if item.y <= -50:
            items.remove(item)
        if collide(item, dragonwarrior):
            if item.type == 1:
                score_increase(10)
            elif item.type == 2:
                level = dragonwarrior.level
                if level < 5:
                    level += 1
                dragonwarrior.set_level(level)
            items.remove(item)


def draw():
    clear_canvas()

    background.draw()
    dragonwarrior.draw()
    #dragonwarrior.draw_bb()

    degree = background.degree()

    font.draw(270, 480, 'Score: %d' % dragonwarrior.score)
    font.draw(250, 450, 'Degree: %4.1d' % degree)

    for monster in monsters:
        if degree < boss_degree:
            monster.draw()
            #monster.draw_bb()

    for cbullet in character_bullets:
        cbullet.draw()
        #cbullet.draw_bb()

    for meteo in meteos:
        meteo.draw()

    for item in items:
        item.draw()

    update_canvas()


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def create_monster_team():
    team = []

    monster1 = Dragon()
    monster1.set_pos(38.4*1, 700)
    monster1.set_type(random.randint(1, 4))
    team.append(monster1)

    monster2 = Dragon()
    monster2.set_pos(38.4*3, 700)
    monster2.set_type(random.randint(1, 4))
    team.append(monster2)

    monster3 = Dragon()
    monster3.set_pos(38.4*5, 700)
    monster3.set_type(random.randint(1, 4))
    team.append(monster3)

    monster4 = Dragon()
    monster4.set_pos(38.4*7, 700)
    monster4.set_type(random.randint(1, 4))
    team.append(monster4)

    monster5 = Dragon()
    monster5.set_pos(38.4*9, 700)
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

def score_increase(score):
    scores = dragonwarrior.score
    scores += score
    dragonwarrior.set_score(scores)