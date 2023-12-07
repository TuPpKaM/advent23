from functools import total_ordering 

nums = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']
nums = nums[::-1]

@total_ordering
class Cardhand():
    def __init__(self,hand, bid, tier) -> None:
        self.hand = hand
        self.bid = int(bid)
        self.tier = tier

    def __eq__(self, other) -> bool:
        print(other)
        return self.hand == other.hand

    def __lt__(self,other) -> bool:
        if self.tier == other.tier:
            return smaller(self.hand, other.hand) == self.hand
        else:
            return self.tier < other.tier

def smaller(hand1,hand2):
    for i in range(5):
        h1 = nums.index(hand1[i])
        h2 = nums.index(hand2[i])
        if h1 != h2:
            if h1 < h2:
                return hand1
            if h2 < h1:
                return hand2

def two():
    sums = 0
    hands = []
    with open('d7_2.txt') as input:
        for li in input:
            hand, bid = li.strip().split(' ')

            #tier 1=high, 2=pair, 3=twopair, 4=three, 5=house, 6=four, 7= five
            if does_hand_exist(hand, 5):
                used = does_hand_exist(hand,5)
                hands.append(Cardhand(hand,bid,7))

            elif does_hand_exist(hand, 4):
                used = does_hand_exist(hand,4)
                hands.append(Cardhand(hand,bid,6))

            elif does_hand_exist(hand, 3):
                used = does_hand_exist(hand,3)
                if does_hand_exist(hand,2,used):

                    hands.append(Cardhand(hand,bid,5))
                else:
                    hands.append(Cardhand(hand,bid,4))

            elif does_hand_exist(hand,2):
                used = does_hand_exist(hand, 2)
                if does_hand_exist(hand, 2, used):
                    hands.append(Cardhand(hand,bid,3))
                else:
                    hands.append(Cardhand(hand,bid,2))

            else:
                hands.append(Cardhand(hand,bid,1))

    hands.sort()

    for i, hand in enumerate(hands, start=1):
        score = i * hand.bid
        sums += score

    print('two',sums)

def does_hand_exist(hand: str, amount: int, blacklist = []):
    value = []
    j_cnt = hand.count('J') if 'J' not in blacklist else 0

    for num in nums[::-1]:
        if num not in blacklist and not (num == 'J' and j_cnt==2): # problem with JJ
            if hand.count(num) == amount:
                value.append(num)
                return value
            elif hand.count(num)+j_cnt == amount:
                value.append(num)
                value.append('J')
                return value
    return None

two()