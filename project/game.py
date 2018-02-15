"""
Player class
turn()
isDraw()
score(action)?
Points : number
addPoints(number), removePoints(number)
"""
# player class here

"""
Card class
value:
suit:
face={up, down}
isFaceCard(): Boolean
flip(): turns Face up to down, down to up
"""
# card class here

"""
Deck class
cardContents : card list
shuffle()
"""
# deck class here

"""
Hand class
isRun()
canTake()
"""
# hand class here

"""
Table class
piles: list of list of card
discards: list of card
"""
# table class here

"""
Play class
dealer: d in Player
discard: list of card, ordered
	piles: # only relevant for some games
init(list of Player)
	      i.deck = i.generate(Deck()) 
                              # eg different games exclude different cards
                              # e.g shuffline
	runs() # no centralized order
	isWin()	 : p list in Player # returns the set of players winning
	deal(n:number, p:player)
	draw()
	say(phrase)
	goes_out(player)
"""
# play class here

