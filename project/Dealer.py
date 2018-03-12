from Deck import Deck
from Card import Card

class Dealer:
    deck = Deck()
    
    def dealWar(self, player1, player2):
        player1.hand = deck.cards[:25]
        player2.hand = deck.cards[25:]
    
    def dealBartok(self, players):
        for p in players:
            p.hand = deck.cards[:6]
            deck = deck.cards[6:]
def Card deal1Card():
        cardToDeal = deck.cards[0]
        deck = deck.cards[1:]
        return cardToDeal
