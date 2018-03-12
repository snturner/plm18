import Deck, Card
class Dealer:
    Deck deck
    
    def dealWar(self, player1, player2):
        player1.hand = deck[:25]
        player2.hand = deck[25:]
    
    def dealBartok(self, players):
        for p in players:
            p.hand = deck[:6]
            deck = deck[6:]
    def Card deal1Card():
        cardToDeal = deck[0]
        deck = deck[1:]
        return cardToDeal

