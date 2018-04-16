from WarRules import *
from BartokRules import *
from Player import Player
from Dealer import Dealer

class Transition():
    def __init__(self, guard, end, updateGuard = None):
        self.guard = guard
        self.end   = end
        self.actions = []
        self.updateGuard = updateGuard

    def addactions(self, f):
        self.actions.append(f)

    def update(self, gameResources):
        if self.updateGuard is not None:
            self.guard = gameResources[self.updateGuard]

class State():
    def __init__(self, name, gameResources, updateGuard=None):
        self.updateGuard = updateGuard
        self.gameResources = gameResources
        self.name = name
        self.transitions = []

    def addtransition(self, transition):
         self.transitions.append(transition)

    def step(self):
        for t in self.transitions:
            if t.guard is not None:
                if self.updateGuard is not None:
                    t.update(self.gameResources)
                if(t.guard is True):
                    for action in t.actions:
                        action(self.gameResources)
                    return t.end
 

class Start(State): pass

class End(State):
    def quit(self):
        return True

class FSM():  
    def __init__(self, start):
        self.states = []
        self.start = start
        self.currentstate = start
        self.run()

    def addState(self, state):
        self.states += state

    def run(self):
        while True:
            self.currentstate = self.currentstate.step()
            if isinstance(self.currentstate, End):
                break

class WarMachine():
    def __init__(self):
        self.gameResources = {}
        #win conditions and round end condition
        self.gameResources["isTie"] = False
        self.gameResources["hasCards"] = True
        self.gameResources["emptyHand"] = False
        self.run()

    def run(self): 
        #states
        start = Start("start", self.gameResources)
        roundSetUp = State("roundsetup", self.gameResources)
        newRound = State("newround", self.gameResources)
        player1Turn = State("player1turn", self.gameResources)
        player2Turn = State("player2turn", self.gameResources)
        pickWinner = State("pickwinner", self.gameResources)
        roundEnd = State("roundend", self.gameResources, True)
        end = End("end", self.gameResources,)
         
        #transitions
        #start transitions
        setupT = Transition(True, roundSetUp)
        setupT.addactions(printInstruction)
        setupT.addactions(setUp)
        start.addtransition(setupT)
        #round set up transitions
        roundSetUpT = Transition(True, newRound)
        roundSetUpT.addactions(setUpRound)
        roundSetUp.addtransition(roundSetUpT)
        #new round transitions
        newRoundT = Transition(True, player1Turn)
        newRoundT.addactions(incrementRound)
        newRound.addtransition(newRoundT)
        #player 1 turn transitions
        player1T = Transition(True,player2Turn)
        player1T.addactions(player1PlaysCard)
        player1Turn.addtransition(player1T)
        #player 2 turn transitions
        player2T = Transition(True,pickWinner)
        player2T.addactions(player2PlaysCard)
        player2Turn.addtransition(player2T)
        #pick winner transitions
        winnerT = Transition(True, roundEnd)
        winnerT.addactions(winner)
        pickWinner.addtransition(winnerT)
        #round end transitions
        for k, v in self.gameResources.items():
            print(k, v)
        endGameT = Transition( self.gameResources["emptyHand"], end, "emptyHand")
        endGameT.addactions(printWinner)
        roundEnd.addtransition(endGameT)
        isTieT = Transition(self.gameResources["isTie"], player1Turn, "isTie")
        roundEnd.addtransition(isTieT)
        nextRoundT = Transition(True, newRound)
        roundEnd.addtransition(nextRoundT)


        #setup the fsm
        fsm = FSM(start)

class BartokMachine():
    def __init__(self):
        self.gameResources = {}
        #win conditions and round end condition
        self.gameResources["isTie"] = False
        self.gameResources["hasCards"] = True
        self.gameResources["emptyHand"] = False
        self.run()
    def run(self):
        start = Start("start", self.gameResources)
        roundSetUp = State("roundsetup", self.gameResources)
        playerTurn = State("playerturn", self.gameResources)
        pickWinner = State("pickwinner", self.gameResources)
        roundEnd = State("roundend", self.gameResources, True)
        end = End("end", self.gameResources,)
        
        #transitions
        #start transitions
        setupT = Transition(True, roundSetUp)
        setupT.addactions(printInstruction)
        setupT.addactions(setUp)
        start.addtransition(setupT)
        #round set up transitions
        roundSetUpT = Transition(True, playerTurn)
        roundSetUpT.addactions(setUpRound)
        roundSetUp.addtransition(roundSetUpT)
        #new round transitions
        playerTurnT = Transition(True, pickWinner) 
        playerTurnT.addactions(incrementRound)
        playerTurnT.addactions(printPlayerHand)
        playerTurnT.addactions(playerPicksCard)
        playerTurnT.addactions(playCard)
        playerTurnT.addactions(nextPlayer)
        playerTurn.addtransition(playerTurnT)
        #determine winner transitions
        winnerT = Transition(True, roundEnd)
        winnerT.addactions(winner)
        pickWinner.addtransition(winnerT)
        #round end transitions
        for k, v in self.gameResources.items():
            print(k, v)
        endGameT = Transition( self.gameResources["emptyHand"], end, "emptyHand")
        endGameT.addactions(printWinner)
        roundEnd.addtransition(endGameT)
        isTieT = Transition(self.gameResources["isTie"], playerTurn, "isTie")
        roundEnd.addtransition(isTieT)
        nextRoundT = Transition(True, playerTurn)
        roundEnd.addtransition(playerTurnT)

        #setup the fsm
        fsm = FSM(start)

if  __name__ =='__main__':
    war = WarMachine()
    #try:
        #war = WarM()
    #except:
        #print("\n\nGame Ended unexpectedly.\n")
        #Logger.close()
        #exit()
