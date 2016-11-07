import json

ranking_data = [
    {'time':4.3, 'x':20, 'y':20},
    {'time':5.3, 'x':20, 'y':20},
    {'time':6.3, 'x':20, 'y':20},
    {'time':7.3, 'x':20, 'y':20},
    {'time':8.3, 'x':20, 'y':20},
    {'time':9.3, 'x':20, 'y':20},
    {'time':10.3, 'x':20, 'y':20},
    {'time':11.3, 'x':20, 'y':20},
    {'time':12.3, 'x':20, 'y':20},
    {'time':13.3, 'x':20, 'y':20},
    {'time':14.3, 'x':20, 'y':20},
    {'time':15.5, 'x':40, 'y':100}
]

def my_sort(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]['time'] < a[j]['time']:
                a[i], a[j] = a[j], a[i]


def draw_ranking():

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    print('[RANKING]')
    my_sort(ranking_data)
    for data in ranking_data[:10]:
        print('(Time:%4.1f,  x:%3d,  y:%3d)' %(data['time'], data['x'], data['y']))


draw_ranking()