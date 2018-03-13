import Card
class PlayerBartok:
	
	def __init__(self):
		self.x = 2
		self.hand = []
		self.players = []
		
	def isDraw(self, cardsList, pile):
		self.x = 3

	def turn(self, cardsList, lastCard, pile):
		self.x = 3

	def printHand(self):
		i = 0
		for card in self.hand:
			if card.value < 11:
				print(i + ") " + card.value + " " + card.suit)
			if card.value == 11:
				print(i  + ") " + "J" + " " + card.suit)
			if card.value == 12:
				print(i + ") " + "Q" + " " + card.suit)
			if card.value == 13:
				print(i + ") " + "K" + " " + card.suit)
			if card.value == 14:
				print(i + ") " + "A" + " " + card.suit)
			i += 1
			


			