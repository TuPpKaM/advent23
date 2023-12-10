from util import caprint, crprint, make_empty_grid, colored_grid_display, make_empty_grid_value
import math
import sys
from matplotlib.path import Path

sys.setrecursionlimit(100000)

ints = [int(x) for x in range(50000)] #just for display

def both():
    sums = 0
    grid = []
    with open('d10_2.txt') as input: # not 1300, to low
        for i_row, li in enumerate(input):
            row = []
            line = li.strip()
            for x, char in enumerate(line):
                row.append(char)
                if char == 'S':
                    start = ((x,i_row)) # x,y
            grid.append(row)

    dist = make_empty_grid_value(w=len(grid[0]), h=len(grid), def_v=math.inf)
    dist[start[1]][start[0]] = 0

    prev = start
    path = []
    path.append((float(start[0]),float(start[1])))
    codes = [Path.MOVETO]
    step(grid, start, prev, dist, path, codes)
    pipes = Path(vertices=path, codes=codes)

    for row in dist:
        for item in row:
            if item != math.inf:
                sums = max(sums,item)

    print('one',int((sums+1)/2))

    marked = []
    for y, row in enumerate(dist):
        for x, item in enumerate(row):
            if item == math.inf and pipes.contains_point((float(x),float(y))):
                marked.append((x,y)) #saved for preview, otherwise just count
    
    colored_grid_display(grid=dist, green=ints, cord_highlights=marked, muted=True)
    print('two',len(marked))

def get_start_pos(grid,start):
    pos = []

    left = ((start[0]-1,start[1]))
    left_sym = ['L','F']
    if within(grid,left) and (grid[left[1]][left[0]] in left_sym):
        pos.append(left)

    righ = ((start[0]+1,start[1]))
    righ_sym = ['-','J','7']
    if within(grid, righ) and (grid[righ[1]][righ[0]] in righ_sym):
        pos.append(righ)    

    top = ((start[0],start[1]-1))
    top_sym = ['|','F','7']
    if within(grid, top) and (grid[top[1]][top[0]] in top_sym):
        pos.append(top)  

    bot = ((start[0],start[1]+1))
    bot_sym = ['|','L','J']
    if within(grid, bot) and (grid[bot[1]][bot[0]] in bot_sym):
        pos.append(bot)  

    return pos[0],pos[1]

def within(grid, start):
    return not (start[0] < 0 or start[0] > len(grid[0])-1 or start[1] < 0 or start[1] > len(grid)-1)

def step(grid, start, prev, dist,path,codes): 
    visited = [(start[0],start[1])]
    pos_1, pos_2 = get_start_pos(grid,start)
    _step(grid, pos_1, prev, dist, visited,path,codes)
    #visited2 = [(start[0],start[1])]    #
    #_step(grid, pos_2, prev, dist, visited2)

def _step(grid, start, prev, dist, visited,path,codes):
    moved = False
    end = []

    if grid[start[1]][start[0]] == '|':
        moved = True
        end.append((start[0], start[1]+1))
        end.append((start[0], start[1]-1))

    elif grid[start[1]][start[0]] == '-':
        moved = True
        end.append((start[0]+1, start[1]))
        end.append((start[0]-1, start[1]))

    elif grid[start[1]][start[0]] == 'L':
        moved = True
        end.append((start[0], start[1]-1))
        end.append((start[0]+1, start[1]))

    elif grid[start[1]][start[0]] == 'J':
        moved = True
        end.append((start[0]-1, start[1]))
        end.append((start[0], start[1]-1))

    elif grid[start[1]][start[0]] == '7':
        moved = True
        end.append((start[0], start[1]+1))
        end.append((start[0]-1, start[1]))

    elif grid[start[1]][start[0]] == 'F':
        moved = True
        end.append((start[0], start[1]+1))
        end.append((start[0]+1, start[1])) 

    if moved:
        # didn't need min(). Could just divide the pipe length in two and get the "apex".
        dist[start[1]][start[0]] = min(dist[prev[1]][prev[0]]+1, dist[start[1]][start[0]])
        visited.append(start) #p1
        path.append((float(start[0]),float(start[1]))) #p2
        codes.append(Path.LINETO) #p2
        for e in end:
            if not (e[0] < 0 or e[0] > len(grid) or e[1] < 0 or e[1] > len(grid[0]) or e in visited):
                _step(grid, start=e, prev=start, dist=dist, visited=visited, path=path, codes=codes)

    return

def find_cluster(dist,start): #not used in final
    cluster = set()
    cluster.add(start)
    _find_cluster(dist,start,cluster)
    return cluster

def _find_cluster(dist,start,cluster): #not used in final
    pos = [(start[0],start[1]-1),(start[0],start[1]+1),(start[0]-1,start[1]),(start[0]+1,start[1])]

    for p in pos:
        if p not in cluster and within(dist,p):
            if dist[p[1]][p[0]] == math.inf:
                cluster.add(p)
                cluster.update(_find_cluster(dist,p,cluster))
    
    return cluster

both()