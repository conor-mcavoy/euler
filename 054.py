f = open("p054_poker.txt", "r")
hands = []
cont = True
while True:
    hands.append(f.readline()[:-1])
    if hands[-1] == "":
        break
f.close()
hands = hands[:-1]
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['S', 'D', 'H', 'C']

def numerize(card):
    if card == 'A':
        return 14
    if card == 'K':
        return 13
    if card == 'Q':
        return 12
    if card == 'J':
        return 11
    if card == 'T':
        return 10
    return int(card)

def unnumerize(num):
    return cards[num - 2]

def top(hand):
    for card in cards[::-1]:
        if card in hand:
            return numerize(card)

def flush(hand):
    for suit in suits:
        if hand.count(suit) == 5:
            return True
    return False

def straight(hand):
    topCard = top(hand)
    if topCard < 6:
        return False
    for card in cards[topCard - 6:topCard - 2]:
        if card not in hand:
            return False
    return True

def straightFlush(hand):
    if flush(hand) and straight(hand):
        return True
    return False

def royalFlush(hand):
    if straightFlush(hand) and 'A' in hand:
        return True
    return False

def fourOfAKind(hand):
    for card in cards:
        if hand.count(card) == 4:
            return (True, numerize(card))
    return (False, None)

def fullHouse(hand):
    for card in cards:
        if hand.count(card) == 3:
            hand.replace(card, '')
            for card2 in cards:
                if hand.count(card2) == 2:
                    return (True, numerize(card))
    return (False, None)

def threeOfAKind(hand):
    for card in cards:
        if hand.count(card) == 3:
            return (True, numerize(card))
    return (False, None)

def twoPairs(hand):
    for card in cards:
        if hand.count(card) == 2:
            for card2 in cards:
                if card2 != card and hand.count(card2) == 2:
                    return (True, max(numerize(card), numerize(card2)),\
                            min(numerize(card), numerize(card2)),\
                            top(hand.replace(card, '').replace(card2, '')))
    return (False, None, None, None)

def onePair(hand):
    for card in cards:
        if hand.count(card) == 2:
            return (True, numerize(card), top(hand.replace(card, '')),\
                    top(hand.replace(unnumerize(top(hand.replace(card, ''))), '')),\
                    top(hand.replace(unnumerize(top(hand.replace(unnumerize(top(hand.replace(card, ''))), ''))), '')))
    return (False, None, None, None, None)

def hand1Wins(hand1, hand2):
    top1 = top(hand1)
    top2 = top(hand2)
    
    if royalFlush(hand1) != royalFlush(hand2):
        return (royalFlush(hand1), "royal flush")
    
    if straightFlush(hand1) != straightFlush(hand2):
        return (straightFlush(hand1), "straight flush")
    elif straightFlush(hand1):
        return (top1 > top2, "two straight flushes")

    has_4oaK1, tiebreak1 = fourOfAKind(hand1)
    has_4oaK2, tiebreak2 = fourOfAKind(hand2)
    if has_4oaK1 != has_4oaK2: #one of the hands has 4oaK
        return (has_4oaK1, "four of a kind")
    elif has_4oaK1: #both of the hands have 4oaK
        return (tiebreak1 > tiebreak2, "two four of a kinds") #both must have diff 4oaKs, so which is larger?

    has_FH1, tiebreak1 = fullHouse(hand1)
    has_FH2, tiebreak2 = fullHouse(hand2)
    if has_FH1 != has_FH2:
        return (has_FH1, "full house")
    elif has_FH1:
        return (tiebreak1 > tiebreak2, "two full houses")

    if flush(hand1) != flush(hand2):
        return (flush(hand1), "flush")
    elif flush(hand1):
        return (top1 > top2, "two flushes")

    if straight(hand1) != straight(hand2):
        return (straight(hand1), "straight")
    elif straight(hand1):
        return (top1 > top2, "two straights")

    
    has_3oaK1, tiebreak1 = threeOfAKind(hand1)
    has_3oaK2, tiebreak2 = threeOfAKind(hand2)
    if has_3oaK1 != has_3oaK2: #one of the hands has 3oaK
        return (has_3oaK1, "three of a kind")
    elif has_3oaK1: #both of the hands have 3oaK
        return (tiebreak1 > tiebreak2, "two three of a kinds") #which has the higher 3oaK?

    has_2P1, bestPair1, worstPair1, other1 = twoPairs(hand1)
    has_2P2, bestPair2, worstPair2, other2 = twoPairs(hand2)
    if has_2P1 != has_2P2:
        return (has_2P1, "two pairs")
    elif has_2P1:
        if bestPair1 != bestPair2:
            return (bestPair1 > bestPair2, "two two pairs")
        elif worstPair1 != worstPair2:
            return (worstPair1 > worstPair2, "two two pairs")
        return (other1 > other2, "two two pairs")

    has_1P1, pair1, first1, second1, third1 = onePair(hand1)
    has_1P2, pair2, first2, second2, third2 = onePair(hand2)
    if has_1P1 != has_1P2:
        return (has_1P1, "one pair")
    elif has_1P1:
        if pair1 != pair2:
            return (pair1 > pair2, "two one pairs")
        elif first1 != first2:
            return (first1 > first2, "two one pairs")
        elif second1 != second2:
            return (second1 > second2, "two one pairs")
        return (third1 > third2, "two one pairs")

    while top1 == top2:
        hand1 = hand1.replace(unnumerize(top1), '')
        hand2 = hand2.replace(unnumerize(top2), '')
        top1 = top(hand1)
        top2 = top(hand2)
    return (top1 > top2, "high card")

t = 0
for handPair in hands:
    h1 = handPair[:14]
    h2 = handPair[15:]
    if hand1Wins(h1, h2)[0]:
        t += 1
print(t)
