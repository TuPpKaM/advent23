def both():
    races_1 = []
    races_2 = []
    dist_1 = []
    dist_2 = []
    with open('d6_2.txt') as input:
        for li in input:
            start, line = li.strip().split(':')
            if start.startswith('Time'):
                races_1 = [int (x) for x in line.split()]
                races_2.append(int(''.join([x for x in line.split()])))
                
            if start.startswith('Dist'):
                dist_1 = [int (x) for x in line.split()]
                dist_2.append(int(''.join([x for x in line.split()])))
    
    print('one',calc_pts(races_1,dist_1))
    print('two',calc_pts(races_2,dist_2))

def calc_pts(races,dist):
    sums = 1
    for i, _ in enumerate(races):
        points = calc_btn(races[i],dist[i])
        sums *= points
    return sums

def calc_btn(time,distance):
    sums = 0
    for t in range(time+1):
        ress = _calc_btn(time,distance,t)
        if ress:
            sums += ress
    return sums

def _calc_btn(ti,distance,btn_hold):
    hold = btn_hold
    time = ti-btn_hold
    if hold < 0 or time < 0:
        return None
    dist = hold*time
    if dist > distance:
        return 1

both()