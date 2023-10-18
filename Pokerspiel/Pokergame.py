import random

list_type = ['Kreuz', 'Herz', 'Pik', 'Karo']  # Kreuz,Herz,Pik,Karo
list_ranks = ['Ace', 'King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2]
outs = ['RoyalFlush', 'StraightFlush', 'FourOfAKind', 'FullHouse',
        'Flush', 'Straight', 'ThreeOfAKind', 'TwoPairs', 'Pair', 'HighCard']

list_PokerCards = []
checkedRanks = []
dict_stat = []


def generateCard(list_type, list_ranks):
    for type in list_type:
        for rank in list_ranks:
            list_PokerCards.append({'TYPE': type, 'RANKS': rank})

    random.shuffle(list_PokerCards)  # shuffles the filled card array


def getFiveCards(cards):  # get five random cards
    count = 0
    for x in range(5):
        place = random.randint(0, len(cards) - 1 - count)
        count += 1
        cards[place], cards[len(cards) - 1 - x] = cards[len(cards) - 1 - x], cards[place]

    return cards[-5:]


def checkedRanks(cards, ranks):
    amounts = []
    for rank in ranks:
        amounts.append({'amount': len(list(filter(lambda card: card['ranks'] == ranks, cards))), 'rank': rank})
    global checkedRanks
    checkedRanks = amounts


def checkpair():
    pairs = list(filter(lambda amount: amount['amount'] == 2, checkedRanks))
    return pairs


def checkthree():
    pairs = list(filter(lambda amount: amount['amount'] == 3, checkedRanks))
    return pairs


def checkfour():
    pairs = list(filter(lambda amount: amount['amount'] == 4, checkedRanks))
    return pairs


def main():
    generateCard(list_type, list_ranks)
    print((getFiveCards(list_PokerCards)))
    #print(checkedRanks(getFiveCards(list_PokerCards), list_ranks))


if __name__ == '__main__':
    main()
