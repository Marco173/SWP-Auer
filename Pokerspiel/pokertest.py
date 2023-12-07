import unittest
from Pokergame import (generateCards, getFiveCards, checkRanks,
                        checkPairs, checkThree, checkFour,
                        checkConsecutive, checkStraight,
                        getStraightSorted, checkFlush,
                        checkFullHouse, checkStraightFlush,
                         checkRoyalFlush, checkMyCards, makeStats)


class TestPoker(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.suits = ['clubs', 'hearts', 'spades', 'diamonds']
            cls.ranks = ['Ace', 'King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2]

        def test_generateCards(self):
            cards = generateCards(self.suits, self.ranks)
            self.assertEqual(len(cards), len(self.suits) * len(self.ranks))

        def test_getFiveCards(self):
            cards = generateCards(self.suits, self.ranks)
            five_cards = getFiveCards(cards)
            self.assertEqual(len(five_cards), 5)

        # Add more tests for the remaining functions


if __name__ == '__main__':
        unittest.main()

