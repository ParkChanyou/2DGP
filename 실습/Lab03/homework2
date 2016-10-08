from pico2d import *
import math

def handle_events():
    global running
    global cx, cy
    global r
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cx, cy = event.x, 599 - event.y
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a:
                r = min(r + 10, 300)
            elif event.key == SDLK_d:
                r = max(r - 10, 20)



open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')



running = True
x, y = 100, 100
frame = 0
show_cursor()

degree = 0
cx, cy = 400, 300
r = 100

while (running):
    clear_canvas()
    grass.draw(400, 30)

    #print('degree = ', degree)
    degree = (degree + 4) % 360

    x = cx + r * math.cos(2 * math.pi * degree / 360)
    y = cy + r * math.sin(2 * math.pi * degree / 360)

    character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.01)
    handle_events()

close_canvas()




