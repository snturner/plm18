from Deck import Deck
from Card import Card

class Dealer:
    def dealWar(self, player1, player2):
        deck = Deck()
        player1.hand = deck.cards[:25]
        player2.hand = deck.cards[25:]
    
    def dealBartok(self, players):
        deck = Deck()
        for p in players:
            p.hand = deck.cards[:6]
            deck.cards = deck.cards[6:]

    def deal1Card(deck):
        cardToDeal = deck.cards[0]
        deck.cards = deck.cards[1:]
        return cardToDeal
