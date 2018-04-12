# Abstracted class

from Deck import Deck
from Card import Card

class Dealer:
    def __init__(self):
        self.deck = Deck()

    # def dealWar(self, player1, player2):
    #     deck = Deck()
    #     player1.hand = deck.cards[:25]
    #     player2.hand = deck.cards[25:]
    
    # def dealBartok(self, players, numPlayers):
    #     for i in range(0, numPlayers):
    #         players[i].hand = self.deck.cards[:6]
    #         self.deck.cards = self.deck.cards[6:]

    def dealCard(self):
        cardToDeal = self.deck.cards[0]
        self.deck.cards = self.deck.cards[1:]
        return cardToDeal

    def dealHand(self, players, numPlayers, numCards):
        for i in range(0, numPlayers):
            for k in range(0, numCards):
                players[i].hand.append(self.dealCard())
