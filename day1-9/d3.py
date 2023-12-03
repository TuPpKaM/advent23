class data():

    def __init__(self, row, start, stop, value) -> None:
        self.row = row
        self.start = start
        self.stop = stop
        self.value = value

    def __str__(self) -> str:
        return 'row:'+str(self.row)+'  start:'+str(self.start)+'  stop:'+str(self.stop) +'  value:'+str(self.value)+ '  '

def one():
    sums = 0
    numbers = []
    symbols =  []
    row_num = 0
    with open('d3_2.txt') as input:
        for li in input:
            row_num += 1
            line = li.strip()
            nums = []

            for i, char in enumerate(line):
                if char.isdigit():
                    nums.append(char)
                else:
                    if not char == '.':
                        symbols.append(data(row_num, i, i, char))
                    if nums:
                        add_num(numbers, nums, row_num, i)
                        nums = []
            if nums: #complete number when row ends
                add_num(numbers, nums, row_num, i)
                nums = []

    for number in numbers:
        if adjacent(symbols, number):
            sums += number.value
    
    print(sums)

def two():
    sums = 0
    numbers = []
    symbols =  []
    row_num = 0
    with open('d3_2.txt') as input:
        for li in input:
            row_num += 1
            line = li.strip()
            nums = []

            for i, char in enumerate(line):
                if char.isdigit():
                    nums.append(char)
                else:
                    if not char == '.':
                        symbols.append(data(row_num, i, i, char))
                    if nums:
                        add_num(numbers, nums, row_num, i)
                        nums = []
            if nums: #complete number when row ends
                add_num(numbers, nums, row_num, i)

    for symbol in symbols:
        if symbol.value == '*':
            result = adjacent2(numbers, symbol)
            if len(result) == 2:
                multi = 1
                for r in result:
                    multi *= r
                sums += multi
    
    print(sums)

def add_num(numbers, nums, row_num, i):
    si= ''
    for n in nums:
        si += n
    siffra = int(si)
    numbers.append(data(row_num,i-len(nums),i,siffra))
    nums = []

def adjacent(symbols, data):
    next_to = False
    indxs = set()
    for i in range(data.start-1, data.stop+1, 1):
        indxs.add(i)

    for sym in symbols:
        if abs(sym.row-data.row) < 2:
            if sym.start in indxs:
                next_to = True
            if sym.stop in indxs:
                next_to = True
    return next_to

def adjacent2(numbers, gear):
    result = set()
    for num in numbers:
        indxs = []
        for i in range(num.start-1, num.stop+1, 1):
            indxs.append(i)

        if abs(num.row-gear.row) < 2:
            if gear.start in indxs:
                result.add(num.value)
            if gear.stop in indxs:
                result.add(num.value)
    return result

one()
two()