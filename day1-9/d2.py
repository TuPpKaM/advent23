

rmax = 12
gmax = 13
bmax = 14

def one():
    sums = set()
    with open('d2_2.txt') as input:
        for li in input:
            start, line = li.strip().split(':')
            game, number = start.split(' ')
            number = int(number)

            games = line.split(';')
            for game in games:
                colors = game.split(',')
                for color in colors:
                    num , name = color.lstrip().split(' ')
                    num = int(num)
                    if name == 'red':
                        if num > rmax:
                            sums.add(number)
                    if name == 'green':
                        if num > gmax:
                            sums.add(number)
                    if name == 'blue':
                        if num > bmax:
                            sums.add(number)
    
    res = 0
    for i in range(1,101):
        if i not in sums:
            res += i
    print('one', res)



def two():
    sums = 0
    with open('d2_2.txt') as input:
        for li in input:
            start, line = li.strip().split(':')
            game, number = start.split(' ')
            number = int(number)

            games = line.split(';')
            rm = set()
            gm = set()
            bm = set()

            rm.add(1)
            gm.add(1)
            bm.add(1)

            for game in games:
                colors = game.split(',')

                for color in colors:
                    num , name = color.lstrip().split(' ')
                    num = int(num)
                    if name == 'red':
                        rm.add(num)
                    if name == 'green':
                        gm.add(num)
                    if name == 'blue':
                        bm.add(num)

            res = (max(rm)*max(gm)*max(bm))
            #print('res',res)
            sums += res
    
    print('two',sums)

one()
two()