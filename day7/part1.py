poker = {'5' : [], '4' : [], 'FH' : [], '3' : [], '2P' : [], '1P' : [], 'HC' : []}
bids = {}
pokerlist = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
sorted_hands = []
bid_sum = 0


def sort_poker_hands(element):
    sorting_key = "AKQJT98765432"
    return [sorting_key.index(char) for char in element]


for line in open("input.txt"):
    line = line.strip().split()
    hand = line[0].strip()
    bid = int(line[1].strip())
    bids[hand] = bid

    if len(set(hand)) == 1:
        poker['5'].append(hand)

    elif len(set(hand)) == 2:
        list_hand = list(set(hand))
        if hand.count(list_hand[0]) == 4 or hand.count(list_hand[1]) == 4:
            poker['4'].append(hand)
        else:
            poker['FH'].append(hand)

    elif len(set(hand)) == 3:
        list_hand = list(set(hand))
        if hand.count(list_hand[0]) == 3 or hand.count(list_hand[1]) == 3 \
                or hand.count(list_hand[2]) == 3:
            poker['3'].append(hand)
        else:
            poker['2P'].append(hand)

    elif len(set(hand)) == 4:
        poker['1P'].append(hand)

    else:
        poker['HC'].append(hand)

for key, value in poker.items():
    if len(poker[key]) == 1:
        sorted_hands.extend(value)
    elif len(poker[key]) > 1:
        sorted_hands.extend(sorted(value, key=sort_poker_hands))


for hand in range(len(sorted_hands)):
    bid_sum += bids[sorted_hands[hand]]*(len(sorted_hands)-hand)


print(bid_sum)



