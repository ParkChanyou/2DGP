import game_framework
from pico2d import *

import main_state
import title_state

name = "RankingState"
image = None
black_image = None
fone = None


def enter():
    global image, black_image
    global font
    global grid
    if image == None :
        image = load_image('background/background_1.png')
    if black_image == None :
        black_image = load_image('background/black.png')
    font = load_font('etc/barun.ttf', 20)

def exit():
    global image
    global black_image
    global grid
    global font
    #del(image)
    #del(black_image)
    #del(font)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                #game_framework.quit()
                game_framework.change_state(title_state)



def draw():
    global image, black_image
    clear_canvas()
    image.draw(192, 256)
    black_image.opacify(0.6)
    black_image.draw(192, 256)
    draw_ranking()
    update_canvas()

def draw_ranking():
    def my_sort(a):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i]['Degree'] < a[j]['Degree']:
                    a[i], a[j] = a[j], a[i]

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    print('[RANKING]')
    my_sort(ranking_data)

    for data in ranking_data[:10]:
        print('(Score:%4d,  Degree:%4d)' % (data['Score'], data['Degree']))

    y = 0
    for data in ranking_data[:10]:
        font.draw(66, 450 - 40 * y, '(Score:%4d,  Degree:%4d)' % (data['Score'], data['Degree']), (255, 255, 255))
        y += 1



def update():
    pass


def pause():
    pass


def resume():
    pass






