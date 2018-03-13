from Deck import Deck
from Card import Card

class Dealer:
    def __init__(self):
        self.deck = Deck()

    def dealWar(self, player1, player2):
        deck = Deck()
        player1.hand = deck.cards[:25]
        player2.hand = deck.cards[25:]
    
    def dealBartok(self, players):
        for p in players:
            p.hand = self.deck.cards[:6]
            self.deck.cards = self.deck.cards[6:]

    def deal1Card(self):
        cardToDeal = self.deck.cards[0]
        self.deck.cards = self.deck.cards[1:]
        return cardToDeal
