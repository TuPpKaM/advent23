from collections import defaultdict

def one():
    seads = []
    parse = False
    dest = defaultdict(int)
    with open('d5_2.txt') as input:
        for row, li in enumerate(input):
            line = li.strip()

            if row == 0:
                seads = [int(x) for x in li.strip().split(':')[1].split()]

            elif parse and line:
                ranges = line.split()
                des = int(ranges[0])
                sou = int(ranges[1])
                ral = int(ranges[2])

                for num in seads:
                    if num >= sou and num < sou+ral:
                        dest[num] = (num-sou)+des

            else:
                if not line:
                    new_num = []
                    for num in seads:
                        if dest[num] > 0:
                            new_num.append(dest[num])
                        else:
                            new_num.append(num)
                    parse = False
                    seads = new_num
                    dest = defaultdict(int)
                else:
                    parse = True

    print('one', min(seads))

def two():
    seeds = defaultdict(int) # [number] = range (amount)
    parse = False
    dest = defaultdict(int) # [number] = ( range (amount), difference )
    blacklist = []
    with open('d5_2.txt') as input:
        for row, li in enumerate(input):
            line = li.strip()
            
            if row == 0:
                inp = li.strip().split(':')[1].split()
                x = 0
                for _ in range(10):
                    n1 = int(inp[x])
                    n2 = int(inp[x+1])
                    x += 2
                    seeds[n1] = n2

            elif parse and line:
                ranges = line.split()
                des = int(ranges[0])
                sou = int(ranges[1])
                ral = int(ranges[2])
                
                dest[sou] = (ral,des-sou)

                split = divide(dest,seeds)
                seeds = defaultdict(int)
                for k,v in split.items():
                    seeds[k] = v

                delete_list = []
                add_dict = defaultdict(int)
                for k2, tup in dest.items():
                    for k1,v1 in seeds.items():
                        if k1 not in blacklist and k1>=k2 and k1<k2+tup[0]-1:
                            add_dict[k1+tup[1]] = v1
                            blacklist.append(k1+tup[1])
                            delete_list.append(k1)
                    
                for i in delete_list:
                    del seeds[i]

                seeds.update(add_dict)
                add_dict = defaultdict(int)

            else:
                if not line:
                    if row != 1:
                        parse = False
                        dest = defaultdict(int)
                        blacklist = []
                else:
                    parse = True

    del seeds[0] #WHY DO I NEED THIS????
    print('two', min(seeds))

def divide(dest, seads):
    pairs = defaultdict(int)
    blacklist = []
    for num, added in seads.items():
        for d1, tul in dest.items():
            split = _divide(d1, tul[0]+d1-1, num, num+added-1)
            if split:
                blacklist.append(num)
                for k,v in split.items():
                    pairs[k] = v

    for num, added in seads.items(): #horrible
        if not pairs.get(num) and num not in blacklist:
            pairs[num] = added

    return pairs

def _divide(d1,d2,n1,n2): # horrible x 2
    pairs = defaultdict(int)
    if (d1<n1 and d2<n1) or (d1>n2 and d2>n2):
        return None
    
    if d2>=n1 and d2<n2 and d1<=n1:
        n_range = d2-n1+1
        pairs[n1] = n_range
        numbers_left = n2-n1+1-n_range
        if numbers_left > 0:
            pairs[n1+n_range] = numbers_left

    elif d1<=n1 and d2>=n2:
        n_range = n2-n1+1
        pairs[n1] = n_range

    elif d1>n1 and d2>=n2:
        n_range = d1-n1
        pairs[n1] = n_range

        numbers_left = n2-n1+1-n_range
        if numbers_left > 0:
            pairs[n1+n_range] = numbers_left

    elif d1>n1 and d2<n2: # tripple split
        bot_range = d1-n1
        pairs[n1] = bot_range

        mid_range = d2-d1+1
        pairs[d1] = mid_range

        top_range = n2-d2
        pairs[d2+1] = top_range
        
    return pairs

one()
two()