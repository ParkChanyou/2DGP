import game_framework
from pico2d import *


import main_state
import title_state
import json


name = "RankingState"
image = None
fone = None
f = None
data = None

def enter():
    global image, font, f, data
    image = load_image('blackboard.png')
    font = load_font('ENCR10B.TTF')
    f = open('score.txt', 'r')
    data = json.load(f)
    f.close()

def exit():
    global image
    del(image)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)



def update(frame_time):
    pass


def draw(frame_time):
    global image, font, data
    clear_canvas()
    image.draw(400, 300)
    count = 0
    for name, time in sorted(data.items(), key=lambda data: data[1], reverse=True):
        count += 1
        if count <= 10:
            font.draw(200, 500 - (count * 40), 'Name: %s, Time: %3.2f' % (name, time))
    update_canvas()

