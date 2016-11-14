import game_framework
from pico2d import *

import main_state
import title_state

name = "RankingState"
image = None
black_image = None


def enter():
    global image
    global game_start_image
    global grid
    image = load_image('background/background_1.png')
    black_image = load_image('background/black.png')


def exit():
    global image
    global black_image
    global grid
    del(image)
    del(black_image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)



def draw():
    clear_canvas()
    image.draw(192, 256)
    black_image.opacify(0.5)
    black_image.draw(192, 256)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






