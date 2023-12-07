import random
suits = ['clubs', 'hearts', 'spades', 'diamonds']  # Kreuz, Herz, Pik, Karo
ranks = ['Ace', 'King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2]
outs = ['RoyalFlush', 'StraightFlush', 'FourOfAKind', 'FullHouse',
        'Flush', 'Straight', 'ThreeOfAKind', 'TwoPairs', 'Pair', 'HighCard']
checkedRanks = []


def generateCards(suits, ranks):
    cards = []

    for suit in suits:
        for rank in ranks:
            cards.append({'suit': suit, 'rank': rank})

    random.shuffle(cards)  # shuffle the filled cards array

    return cards

def getFiveCards(cards):  # get five random cards
    gezogen = 0
    for x in range(5):
        stelle = random.randint(0, len(cards)-1-gezogen)
        gezogen += 1

        cards[stelle], cards[len(cards)-1-x] = cards[len(cards)-1-x], cards[stelle]

    return cards[-5:]

#chat gpt
def checkRanks(cards, ranks):
    amounts = []
    for rank in ranks: # Die Methode itertiert über jeden Kartenrang in der Liste ranks
        amounts.append({'amount':
                        len(list(filter(lambda card: card['rank'] == rank, cards))), 'rank': rank})
        #filter: es filtert die karten in cards die den akutellen rang haben
        #len zählt die anzahl der karten die den aktuellen Rang entsprechen
        # ein dictionary wird estellt, das die Anzahl der karten amount und den Rang ranks speichert
        # diese wid in der lsite amounts hinzugefügt
        #amounts wird in die globale varialb checkedranks hinzugefügt

    global checkedRanks
    checkedRanks = amounts

def checkPairs(cards):
    pairs = list(filter(lambda amount:  amount['amount'] == 2, checkedRanks))
    return pairs  # return list of pairs, can be one or be two

def checkThree():
    pairs = list(filter(lambda amount:  amount['amount'] == 3, checkedRanks))
    return pairs  # return list of three

def checkFour():
    pairs = list(filter(lambda amount:  amount['amount'] == 4, checkedRanks))
    return pairs  # return list of three

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))

def checkStraight(cards):
    numbers = []
    for card in cards:
        if(card['rank'] == 'Ace'):
            numbers.append(14)
        elif(card['rank'] == 'King'):
            numbers.append(13)
        elif(card['rank'] == 'Queen'):
            numbers.append(12)
        elif(card['rank'] == 'Jack'):
            numbers.append(11)
        else:
            numbers.append(card['rank'])

    return checkConsecutive(numbers)

def getStraightSorted(cards):
    numbers = []
    for card in cards:
        if(card['rank'] == 'Ace'):
            numbers.append(14)
        elif(card['rank'] == 'King'):
            numbers.append(13)
        elif(card['rank'] == 'Queen'):
            numbers.append(12)
        elif(card['rank'] == 'Jack'):
            numbers.append(11)
        else:
            numbers.append(card['rank'])
    return sorted(numbers)

def checkFlush(cards, suits):
    amounts = []
    for suit in suits:
        amounts.append({'amount':
                        len(list(filter(lambda card: card['suit'] == suit, cards))), 'suit': suit})
    pairs = list(filter(lambda amount:  amount['amount'] == 5, amounts))

    # print(amounts)
    return pairs  # return list of three

def checkFullHouse(cards, ranks):
    isThree = len(checkThree()) == 1 if True else False
    isTwo = len(checkPairs()) == 1 if True else False

    return isThree and isTwo

def checkStraightFlush(cards, suits):
    isStraight = checkStraight(cards)
    isFlush = len(checkFlush(cards, suits)) == 1 if True else False

    return isStraight and isFlush

def checkRoyalFlush(cards, suits):
    if(checkStraightFlush(cards, suits)):
        return getStraightSorted(cards) == list(range(10, 14+1))

    return False

def checkMyCards(cards, ranks, suits):
    checkRanks(cards, ranks)
    if(checkRoyalFlush(cards, suits)):
        return 'RoyalFlush'
    if(checkStraightFlush(cards, suits)):
        return 'StraightFlush'
    if(len(checkFour()) == 1):
        return 'FourOfAKind'
    if(checkFullHouse(cards, ranks)):
        return 'FullHouse'
    if(checkFlush(cards, suits)):
        return 'Flush'
    if(checkStraight(cards)):
        return 'Straight'
    if(checkThree()):
        return 'ThreeOfAKind'
    if(len(checkPairs(cards)) == 2):
        return 'TwoPairs'
    if(len(checkPairs()) == 1):
        return 'Pair'
    else:
        return 'HighCard'

def makeStats(ranks, suits, many):
    myDict = dict()
    myDictPro = dict()

    for i in outs:
        myDict[i] = 0
    for x in range(0, many):
        cards = getFiveCards(generateCards(suits, ranks))
        myDict[checkMyCards(cards, ranks, suits)] += 1
        print(x)
    for key in myDict:
        myDictPro[key] = round((myDict[key]/many)*100,7)

    print(myDictPro)
    print(myDict)

if __name__ == "__main__":
    print(generateCards(suits,ranks))

    #makeStats(ranks, suits, 1000000)