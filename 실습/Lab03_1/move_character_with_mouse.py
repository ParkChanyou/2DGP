from pico2d import *
import math

def handle_events():
    global running
    global x, y
    global rad
    global angle
    global radian
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a:
                rad = rad + 10
                if rad >= 300:
                    rad = 300
            elif event.key == SDLK_d:
                rad = rad - 10
                if rad <= 20:
                    rad = 20
            elif event.key == SDLK_LEFT:
                x = x - 10
            elif event.key == SDLK_RIGHT:
                x = x + 10
            elif event.key == SDLK_UP:
                y = y + 10
            elif event.key == SDLK_DOWN:
                y = y - 10



open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')



running = True
x, y = 400, 300
rad = 100
angle = 0
radian = math.pi / 180
frame = 0
show_cursor()
while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, math.cos(angle * radian) * rad + x, math.sin(angle * radian) * rad + y)
    update_canvas()
    frame = (frame + 1) % 8
    angle = angle + 10
    if angle >= 360:
        angle = 0
    delay(0.05)
    handle_events()

close_canvas()




