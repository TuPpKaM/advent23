 
digit = ['1','2','3','4','5','6','7','8','9','0']
digit2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','zero']


def one():
    sums = 0
    with open('d1_2.txt') as input:
        for li in input:
            line = li.strip()
            nums = []
            num = ''
            for char in line:
                if char in digit:
                    nums.append(char)
            sums += int(nums[0]+nums[-1])

    print(sums)

def two():
    sums = 0
    with open('d1_2.txt') as input:
        for li in input:
            line = li.strip()
            nums = []
            word = ''
            for char in line:
                if char in digit:
                    nums.append(char)
                    word = ''
                else:
                    word += char
                    for d in digit2:
                        if d in word:
                            nums.append(digit[digit2.index(d)])
                            word = word[-1]
            sums += int(nums[0]+nums[-1])
            
    print(sums)

one()
two()