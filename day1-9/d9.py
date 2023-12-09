def both():
    sums_1 = 0
    sums_2 = 0
    readings = []
    with open('d9_2.txt') as input:
        for li in input:
            line = li.strip()
            reading = [int(x) for x in line.split()]
            readings.append(reading)

    for reading in readings:
        sums_1 += get_next(reading,1)
        sums_2 += get_next(reading,2)

    print('one',sums_1)
    print('two',sums_2)

def get_next(reading: list, part: int):
    results = []
    results.append(reading)

    list_ = results[0]
    while not all(ele == 0 for ele in list_):
        list_ = _reduce(list_)
        results.append(list_)

    if part == 1:
        return part1(results)
    if part == 2:
        return part2(results)
    
def _reduce(reading: list):
    new = []
    for i, num in enumerate(reading):
        if i>0 and i<len(reading):
            new.append(reading[i]-reading[i-1])
    return new

def part1(results: list):
    prev_list = None
    for line in results[::-1]:
        if prev_list:
            line.append(prev_list[-1]+line[-1])
        else:
            line.append(0)
        prev_list = line
    return results[0][-1]

def part2(results: list):
    prev_list = None
    for line in results[::-1]:
        if prev_list:
            line.insert(0, line[0]-prev_list[0])
        else:
            line.insert(0, 0)
        prev_list = line
    return results[0][0]

both()