from pico2d import *

import game_framework


from boy import FreeBoy as Boy # import Boy class from boy.py
from background import FixedBackground as Background
from ball import FreeBall


name = "scroll_state"

boy = None
background = None
balls = None

def create_world():
    global boy, background, balls, big_balls
    boy = Boy()
    background = Background()

    balls = [FreeBall() for i in range(100)]

    background.set_center_object(boy)
    boy.set_background(background)

    for ball in balls:
        ball.set_background(background)


def destroy_world():
    global boy, background, balls
    del(boy)
    del(background)
    del(balls)


def enter():
    open_canvas(800, 600)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


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
                game_framework.quit()
            elif event.type == SDL_MOUSEBUTTONDOWN:
                create_ball(event.x, event.y)
            else:
                boy.handle_event(event)
                background.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def create_ball(x, y):
    global balls

    new_ball = [FreeBall() for i in range(1)]
    for ball in new_ball:
        ball.set_background(background)
        ball.set_pos(x, y)
    balls = new_ball + balls


def update(frame_time):
    show_cursor()

    boy.update(frame_time)
    background.update(frame_time)

    for ball in balls:
        ball.update(frame_time)


    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            boy.eat(ball)



def draw(frame_time):
    clear_canvas()

    ball_count = 0

    background.draw()
    boy.draw()
    for ball in balls:
        ball.draw()
        ball_count += 1
    debug_print('ball count=%d' % (ball_count))
    update_canvas()






