import random
import requests
import json


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.fillWhoCanBeatMe()

    def __str__(self):
        return self.hand

    def fillWhoCanBeatMe(self):
        if self.hand == "stein":
            self.whoCanBeatMe = ["papier", "spock"]
        elif self.hand == "papier":
            self.whoCanBeatMe = ["schere", "echse"]
        elif self.hand == "schere":
            self.whoCanBeatMe = ["stein", "spock"]
        elif self.hand == "echse":
            self.whoCanBeatMe = ["stein", "schere"]
        elif self.hand == "spock":
            self.whoCanBeatMe = ["papier", "echse"]

    def isBeatenBy(self, otherHand):
        return otherHand.hand in self.whoCanBeatMe


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None

    def __str__(self):
        return self.name

    def isBeatenBy(self, otherPlayer):
        return self.hand.isBeatenBy(otherPlayer.hand)



class Game:

    def __init__(self, *args):
        if len(args) == 2:
            self.player1 = Player("Computer")
            self.player2 = args[0]
            self.pointsToWin = args[1]
        else:
            self.player1 = args[0]
            self.player2 = args[1]
            self.pointsToWin = args[2]

        Stein = Hand("stein")
        Papier = Hand("papier")
        Schere = Hand("schere")
        Echse = Hand("echse")
        Spock = Hand("spock")
        self.hands = [Stein, Papier, Schere, Echse, Spock]

        self.stats = {'rock': 0, 'paper': 0,
                      'scissors': 0, 'lizzard': 0, 'spock': 0}

        self.player1Wins = 0
        self.player2Wins = 0
        self.rounds = 0
        self.chosenHands = {}
        for hand in self.hands:
            self.chosenHands[hand.hand] = 0


    def play(self):
        while self.player1Wins < self.pointsToWin and self.player2Wins < self.pointsToWin:
            if self.player1.name == "Computer":
                hand1 = random.choice(self.hands)
            else:
                hand1 = Hand(input("Player1, bitte ihre Wahl angeben:"))

            hand2 = Hand(input("Player2,bitte ihre Wahl angeben:"))
            self.chosenHands[hand2.hand] += 1
            self.playOneRound(hand1, hand2)
        if self.player1Wins > self.player2Wins:
            print(self.player1.name + "gewinnt!")
        else:
            print(self.player2.name + "gewinnt!")

    def playOneRound(self, hand1, hand2):
        self.player1.hand = hand1
        self.player2.hand = hand2
        self.rounds += 1
        if self.player1.isBeatenBy(self.player2):
            self.player2Wins += 1
            print(self.player2.name + " wins this round!")
        elif self.player2.isBeatenBy(self.player1):
            self.player1Wins += 1
            print(self.player1.name + " wins this round!")
        else:
            print("This round is a tie!")


    def returnOneRound(self, hand1String):
        self.stats[hand1String] += 1
        self.player1.hand = Hand(hand1String)
        self.player2.hand = random.choice(self.hands)
        self.player2.hand = Hand(self.playComputer())
        self.rounds += 1
        if self.player1.isBeatenBy(self.player2):
            self.player2Wins += 1
            return self.player2.name + " wins this round!"
        elif self.player2.isBeatenBy(self.player1):
            self.player1Wins += 1
            return self.player1.name + " wins this round!"
            print(self.stats)
        else:
            return "This round is a tie!"
            print(self.stats)


    def playComputer(self):
        print(self.data)
        print(self.data['rock'])
        print(self.data['paper'])
        print(self.data['scissors'])
        print(self.data['lizzard'])
        print(self.data['spock'])
        return random.choices(
            population=['rock', 'paper', 'scissors', 'lizzard', 'spock'],
            weights=[self.data['rock'], self.data['paper'],
                     self.data['scissors'], self.data['lizzard'], self.data['spock']],
            k=1)[0]


if __name__ == "__main__":

    player_comp = Player("You")
    player_me = Player("Me")

    game = Game(player_me, 2)
    game.play()



