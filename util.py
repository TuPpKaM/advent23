from colorama import Fore

def caprint(*values: str, sep='', end = '', **kwargs):
    "append same row"
    if len(values)%2 != 0:
        raise Exception(f'uneven args, len: `{len(values)}. Needs to be \'color\',\'text\'` ')

    foreground = Fore.WHITE
    for arg in values:
        match arg:
            case 'R' | 'r':
                foreground = Fore.RED
            case 'G' | 'g':
                foreground = Fore.GREEN
            case 'B' | 'b':
                foreground = Fore.BLUE
            case 'W' | 'w':
                foreground = Fore.WHITE
            case 'Y' | 'y':
                foreground = Fore.YELLOW
            case _:
                print(foreground, arg, sep=sep, end=end, **kwargs)

def crprint(*values: str, sep='', end = '', **kwargs):
    "new row"
    if len(values)%2 != 0:
        raise Exception(f'uneven args, len: `{len(values)}. Needs to be \'color\',\'text\'` ')

    foreground = Fore.WHITE
    for arg in values:
        match arg:
            case 'R' | 'r':
                foreground = Fore.RED
            case 'G' | 'g':
                foreground = Fore.GREEN
            case 'B' | 'b':
                foreground = Fore.BLUE
            case 'W' | 'w':
                foreground = Fore.WHITE
            case 'Y' | 'y':
                foreground = Fore.YELLOW
            case _:
                print(foreground, arg, sep=sep, end=end, **kwargs)
    print('')

def make_empty_grid(w: int,h: int):
    "basic w x h , all 0"
    grid = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append(0)
        grid.append(row)
    return grid

def colored_grid_display(grid: list | None = None, grid_w: int | None = None, grid_h: int | None = None,
                         cord_highlights: list | None = None, cord_color:str | None = 'y',
                         red: list | None = None, green: list | None = None, blue: list | None = None,
                         muted = False):
    if not grid:
        if not grid_w or not grid_h:
            raise Exception('missing grid or size args to create a blank one')
        grid = make_empty_grid(grid_w,grid_h)

    for row, row_ in enumerate(grid):
        print('')
        for col, item in enumerate(row_):
            color = 'w'
            if red and item in red:
                color = 'r'
            if green and item in green:
                color = 'g'
            if blue and item in blue:
                color = 'b'

            if cord_highlights:
                for cord in cord_highlights:
                    if cord[0] == col and cord[1] == row:
                        color = cord_color

            caprint(color, item, sep='', end = '')

    print('\n')

    if not muted:
        if red:
            crprint('B', 'Red: ','w', red)

        if green:
            crprint('B', 'Green: ','w', green)

        if blue:
            crprint('B', 'Blue: ','w', blue)

        if cord_highlights:
            crprint('B', 'Cordinates highlighted: ','w', cord_highlights)

        crprint('B', 'Grid width: ','w', len(grid[0]))
        crprint('B', 'Grid height: ','w', len(grid))

if __name__ == '__main__':
    
    crprint('r', 'red', 'b', 'blue')
    crprint('r', 'red', 'b', 'blue')
    crprint('r', 'red', 'b', 'blue')

    grid = [[0,1,2],[0,1,2],[0,2,1],[0,5,1]]
    wrong = [0,2]
    corr= [1]
    pos = [(0,3)]

    colored_grid_display(grid, cord_highlights=pos, muted=True)
    colored_grid_display(grid_w=3, grid_h=5,cord_highlights=[(1,1)])
    colored_grid_display(grid, cord_highlights=pos, red=wrong, green=corr)