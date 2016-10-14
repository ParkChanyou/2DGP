import game_framework
from pico2d import *

import main_state

name = "TitleState"
image = None


def enter():
    global image
    global game_start_image
    image = load_image('etc/title.png')
    game_start_image = load_image('etc/game_start_button.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
                #game_framework.pop_state()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif (event.type) == (SDL_MOUSEBUTTONDOWN):
                print(event.x, event.y)
                if event.x >= 137 and event.x <= 247 and event.y >= 389 and event.y <= 495:
                    print("click")
                    game_framework.change_state(main_state)



def draw():
    clear_canvas()
    image.draw(192, 256)
    game_start_image.draw(192, 70)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






