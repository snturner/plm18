import Hand
import Card
class PlayerBartok:
	# DiscardPile pile
	Card hand
	
	def __init__(self):

		
	def isDraw(self, cardsList, pile):
		# ??
	def turn(self, cardsList, lastCard, pile):
		# ...
	
	def printHand():
		int i = 0
		for card in hand:
			if card.value < 11:
				print(i += 1 + ") " + card.value + " " + card.suit)
			if card.value == 11:
				print(i += 1 + ") " + "J" + " " + card.suit)
			if card.value == 12:
				print(i += 1 + ") " + "Q" + " " + card.suit)
			if card.value == 13:
				print(i += 1 + ") " + "K" + " " + card.suit)
			if card.value == 14:
				print(i += 1 + ") " + "A" + " " + card.suit)
			

