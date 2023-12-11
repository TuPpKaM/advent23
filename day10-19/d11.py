
def both():
    sums_1 = 0
    sums_2 = 0
    grid = []
    galaxs = [] #(x,y)
    size = 1000000
    extra_rows = []
    with open('d11_2.txt') as input: #63590637682, 635832237682 forgot 0 in size lul
        for i_row, li in enumerate(input):
            row = []
            line = li.strip()
            for x, char in enumerate(line):
                row.append(char)
                if char == '#':
                    galaxs.append((x,i_row))
            grid.append(row)
            if all(ele == '.' for ele in row):
                extra_rows.append(i_row)    

    extra_cols = []
    for i in range(len(grid[0])):
        if is_empty_col(grid,i):
            extra_cols.append(i)

    for start in galaxs:
        for end in galaxs:
            distance_1 = abs(start[0]-end[0])+abs(start[1]-end[1])
            distance_2 = distance_1
            for row in extra_rows:
                if is_crossing(start[1],end[1], row):
                    distance_1 += 1
                    distance_2 += size-1
            for col in extra_cols:
                if is_crossing(start[0],end[0], col):
                    distance_1 += 1
                    distance_2 += size-1
            
            sums_1 += distance_1
            sums_2 += distance_2

    print('one',int(sums_1/2))
    print('two',int(sums_2/2))

def is_empty_col(grid,index):
    for row in grid:
        if row[index] != '.':
            return False
    return True

def is_crossing(start, end, point):
    if start >= end:
        if end <= point <= start:
            return True
    else:
        if start <= point <= end:
            return True
    return False

both()