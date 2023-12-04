from util import caprint, crprint, make_empty_grid, colored_grid_display
import re

def one():
    sums = 0
    with open('d4_2.txt') as input:
        for li in input:
            start, line = li.strip().split(':')

            game_num = re.findall(r'\d+', start)
            game_num = int(game_num[0])

            win_, you_ = line.split('|')
            win = win_.split(' ') #should have been .split()
            you = you_.split(' ') #should have been .split()

            score = 0
            for num in you:
                if num != '': #split() solves this
                    if num in win:
                        if score < 1:
                            score = 1
                        else:
                            score += score

            sums += score

    print('one', sums)

def two():
    sums = 0
    scores = {}
    extra_wins = {}
    for _ in range(1,200):
        extra_wins[_] = 0

    with open('d4_2.txt') as input:
        for li in input:
            start, line = li.strip().split(':')

            game_num = re.findall(r'\d+', start)
            game_num = int(game_num[0])

            win_, you_ = line.split('|')
            win = win_.split()
            you = you_.split()

            score = 0
            for num in you:
                if num in win:
                    score += 1

            scores[game_num] = score
            for i in range (game_num+1, game_num+score+1, 1):
                extra_wins[i] += 1
                if extra_wins[game_num] > 0:
                    extra_wins[i] += extra_wins[game_num]

    for num , amount in extra_wins.items():
        sums += amount

    sums += 199

    print('two', sums)

one()
two()