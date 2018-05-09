import WarRules
import BartokRules
import LingerLongerRules
import MyShipSailsRules
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
        setupT.addactions(WarRules.printInstruction)
        setupT.addactions(WarRules.setUp)
        start.addtransition(setupT)
        #round set up transitions
        roundSetUpT = Transition(True, newRound)
        roundSetUpT.addactions(WarRules.setUpRound)
        roundSetUp.addtransition(roundSetUpT)
        #new round transitions
        newRoundT = Transition(True, player1Turn)
        newRoundT.addactions(WarRules.incrementRound)
        newRound.addtransition(newRoundT)
        #player 1 turn transitions
        player1T = Transition(True,player2Turn)
        player1T.addactions(WarRules.player1PlaysCard)
        player1Turn.addtransition(player1T)
        #player 2 turn transitions
        player2T = Transition(True,pickWinner)
        player2T.addactions(WarRules.player2PlaysCard)
        player2Turn.addtransition(player2T)
        #pick winner transitions
        winnerT = Transition(True, roundEnd)
        winnerT.addactions(WarRules.winner)
        pickWinner.addtransition(winnerT)
        #round end transitions
        endGameT = Transition( self.gameResources["emptyHand"], end, "emptyHand")
        endGameT.addactions(WarRules.printWinner)
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
        playerTurn = State("playerturn", self.gameResources)
        pickWinner = State("pickwinner", self.gameResources)
        roundEnd = State("roundend", self.gameResources, True)
        end = End("end", self.gameResources,)
        
        #transitions
        #start transitions
        setupT = Transition(True, playerTurn)
        setupT.addactions(BartokRules.printInstruction)
        setupT.addactions(BartokRules.setUp)
        start.addtransition(setupT)
        #player turn transitions
        playerTurnT = Transition(True, pickWinner)
        playerTurnT.addactions(BartokRules.printPlayerHand)
        playerTurnT.addactions(BartokRules.playerPicksCard)
        playerTurnT.addactions(BartokRules.playCard)
        playerTurnT.addactions(BartokRules.nextPlayer)
        playerTurn.addtransition(playerTurnT)
        #determine winner transitions
        winnerT = Transition(True, roundEnd)
        winnerT.addactions(BartokRules.winner)
        pickWinner.addtransition(winnerT)
        #round end transitions
        endGameT = Transition( self.gameResources["emptyHand"], end, "emptyHand")
        endGameT.addactions(BartokRules.printWinner)
        roundEnd.addtransition(endGameT)
        isTieT = Transition(self.gameResources["isTie"], playerTurn, "isTie")
        roundEnd.addtransition(isTieT)
        nextRoundT = Transition(True, playerTurn)
        roundEnd.addtransition(playerTurnT)

        #setup the fsm
        fsm = FSM(start)

class LingerLongerMachine():
    def __init__(self):
        self.gameResources = {}
        #win conditions and round end condition
        self.gameResources["emptyHand"] = False
        self.gameResources["roundIsNotOver"] = True
        self.gameResources["roundOver"] = True
        self.gameResources["emptydeck"] = False
        self.run()

    def run(self):
        #states
        start = Start("start", self.gameResources)
        roundSetUp = State("roundsetup", self.gameResources)
        newRound = State("newround", self.gameResources)
        playerTurn = State("playerturn", self.gameResources, True)
        pickWinner = State("pickWinner", self.gameResources, True)
        end = End("end", self.gameResources,)

        #transitions
        #start transitions
        setupT = Transition(True, roundSetUp)
        setupT.addactions(LingerLongerRules.printInstruction)
        setupT.addactions(LingerLongerRules.setUp)
        start.addtransition(setupT)
        #round set up transitions
        roundSetUpT = Transition(True, newRound)
        roundSetUpT.addactions(LingerLongerRules.setUpRound)
        roundSetUp.addtransition(roundSetUpT)
        #new round transitions
        newRoundT = Transition(True, playerTurn)
        newRoundT.addactions(LingerLongerRules.incrementRound)
        newRound.addtransition(newRoundT)
        #player turn transitions
        playerT = Transition(self.gameResources["roundIsNotOver"], playerTurn, "roundIsNotOver")
        playerT.addactions(LingerLongerRules.playCard)
        roundendT = Transition(True, pickWinner)
        playerTurn.addtransition(playerT)
        playerTurn.addtransition(roundendT)
        #pick Winner Transitions
        playerwinsgameT = Transition(self.gameResources["emptyHand"], end, "emptyHand")
        playerwinsgameT.addactions(LingerLongerRules.winner)
        playerwinsgameT = Transition(self.gameResources["emptydeck"], end, "emptydeck")
        playerwinsgameT.addactions(LingerLongerRules.winner)
        playerwinsroundT = Transition(True, newRound)
        playerwinsroundT.addactions(LingerLongerRules.roundEnd)
        pickWinner.addtransition(playerwinsgameT)
        pickWinner.addtransition(playerwinsroundT)

        #setup the fsm
        fsm = FSM(start)

class MyShipSailsMachine():
    def __init__(self):
        self.gameResources = {}
        #win conditions and round end condition
        self.gameResources["turnIsNotOver"] = True
        self.gameResources["roundIsNotOver"] = True
        self.gameResources["hasSuit"] = False
        self.gameResources["gameOver"] = False
        self.run()

    def run(self):
        #states
        start = Start("start", self.gameResources)
        roundSetUp = State("roundsetup", self.gameResources)
        newRound = State("newround", self.gameResources)
        playerTurn = State("playerturn", self.gameResources, True)
        pickWinner = State("pickWinner", self.gameResources, True)
        end = End("end", self.gameResources,)

        #transitions
        #start transitions
        setupT = Transition(True, roundSetUp)
        setupT.addactions(MyShipSailsRules.printInstruction)
        setupT.addactions(MyShipSailsRules.setUp)
        start.addtransition(setupT)
        #round set up transitions
        roundSetUpT = Transition(True, newRound)
        roundSetUpT.addactions(MyShipSailsRules.setUpRound)
        roundSetUp.addtransition(roundSetUpT)
        #new round transitions
        newRoundT = Transition(True, playerTurn)
        newRoundT.addactions(MyShipSailsRules.incrementRound)
        newRound.addtransition(newRoundT)
        #player turn transitions
        playerT = Transition(self.gameResources["turnIsNotOver"], playerTurn, "turnIsNotOver")
        playerT.addactions(MyShipSailsRules.printPlayerHand)
        playerT.addactions(MyShipSailsRules.checkHand)
        playerT.addactions(MyShipSailsRules.playerPicksCard)
        roundendT = Transition(True, pickWinner)
        playerTurn.addtransition(playerT)
        playerTurn.addtransition(roundendT)
        #pick Winner Transitions
        playerwinsgameT = Transition(self.gameResources["gameOver"], end, "gameOver")
        playerwinsgameT.addactions(MyShipSailsRules.winner)
        nextplayerT = Transition(self.gameResources["roundIsNotOver"], playerTurn, "roundIsNotOver")
        nextplayerT.addactions(MyShipSailsRules.nextPlayer)
        nextroundT = Transition(True, newRound)
        pickWinner.addtransition(playerwinsgameT)
        pickWinner.addtransition(nextplayerT)
        pickWinner.addtransition(nextroundT)

        #setup the fsm
        fsm = FSM(start)

# if __name__ == "__main__":
#     machine = LingerLongerMachine()
