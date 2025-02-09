from pico2d import *

import game_framework


from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass
from brick import Brick



name = "collision"

boy = None
balls = None
big_balls = None
grass = None
brick = None

def create_world():
    global boy, grass, balls, big_balls, brick
    boy = Boy()
    big_balls = [BigBall() for i in range(10)]
    balls = [Ball() for i in range(10)]
    balls = big_balls + balls
    grass = Grass()
    brick = Brick()
    pass


def destroy_world():
    global boy, grass, balls, big_balls, brick

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)
    del(brick)



def enter():
    open_canvas()
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
            else:
                boy.handle_event(event)



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
    pass


def update(frame_time):
    boy.update(frame_time)
    brick.update(frame_time)
    for ball in balls:
        ball.update(frame_time)

    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)

    for ball in big_balls:
        if collide(grass, ball):
            ball.stop()
        if collide(brick, ball):
            ball.stop()
            brick_x, brick_y = brick.get_pos()
            ball.set_pos(brick_x, brick_y)
            ball.set_speed(brick.get_speed())


    pass



def draw(frame_time):
    clear_canvas()
    grass.draw()
    boy.draw()
    brick.draw()
    for ball in balls:
        ball.draw()

    grass.draw_bb()
    boy.draw_bb()
    brick.draw_bb()
    for ball in balls:
        ball.draw_bb()
    pass

    update_canvas()






