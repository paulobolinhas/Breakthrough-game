# Grupo 19
# João Santos nº 57103
# Paulo Bolinhas nº 56300
# Rui Martins nº 56283

from collections import namedtuple
import copy
from random import *

from jogos import Game

state = namedtuple('EstadoBT', 'to_move, white, black')

class EstadoBT_19(state):

    def __init__(self, to_move, white, black):
        self.isOver = self.finished()
        self.winner = self.winner()
        
    # 1 - white; 2 - black; 0 - not over
    def winner(self):
        if self.isOver == 0:
            if (self.to_move == 1):
                return 1
            else:
                return 2
        return 0

    def moves(self):

        listMoves = list()
        alphabet = ["a","b","c","d","e","f","g","h"]

        if self.to_move == 1:
            for moveW in self.white:
                abovePos = moveW[0] + str(int(moveW[-1])+1) 
                if(abovePos not in self.white and abovePos not in self.black and int(abovePos[-1]) < 9):
                    listMoves.append(moveW + '-' + abovePos)
                if(moveW[0] == 'a'):
                    diagRPos = alphabet[alphabet.index(moveW[0])+1] + str(int(moveW[-1])+1) 
                    if(diagRPos not in self.white and int(diagRPos[-1]) < 9):
                        listMoves.append(moveW + '-' + diagRPos)
                elif(moveW[0] == 'h'):
                    diagLPos = alphabet[alphabet.index(moveW[0])-1] + str(int(moveW[-1])+1) 
                    if(diagLPos not in self.white and int(diagLPos[-1]) < 9):
                        listMoves.append(moveW + '-' + diagLPos)
                else:
                    diagRPos = alphabet[alphabet.index(moveW[0])+1] + str(int(moveW[-1])+1)
                    diagLPos = alphabet[alphabet.index(moveW[0])-1] + str(int(moveW[-1])+1)
                    if(diagRPos not in self.white and int(diagRPos[-1]) < 9):
                        listMoves.append(moveW + '-' + diagRPos)
                    if(diagLPos not in self.white and int(diagLPos[-1]) < 9):
                        listMoves.append(moveW + '-' + diagLPos)
        else:
            for moveB in self.black:
                underPos = moveB[0] + str(int(moveB[-1])-1) 
                if(underPos not in self.white and underPos not in self.black and int(underPos[-1]) > 0):
                    listMoves.append(moveB + '-' + underPos)
                if(moveB[0] == 'a'):
                    diagRPos = alphabet[alphabet.index(moveB[0])+1] + str(int(moveB[-1])-1) 
                    if(diagRPos not in self.black and int(diagRPos[-1]) > 0):
                        listMoves.append(moveB + '-' + diagRPos)
                elif(moveB[0] == 'h'):
                    diagLPos = alphabet[alphabet.index(moveB[0])-1] + str(int(moveB[-1])-1) 
                    if(diagLPos not in self.black and int(diagLPos[-1]) > 0):
                        listMoves.append(moveB + '-' + diagLPos)
                else:
                    diagRPos = alphabet[alphabet.index(moveB[0])+1] + str(int(moveB[-1])-1)
                    diagLPos = alphabet[alphabet.index(moveB[0])-1] + str(int(moveB[-1])-1)
                    if(diagRPos not in self.black and int(diagRPos[-1]) > 0):
                        listMoves.append(moveB + '-' + diagRPos)
                    if(diagLPos not in self.black and int(diagLPos[-1]) > 0):
                        listMoves.append(moveB + '-' + diagLPos)

        listMoves.sort()

        return listMoves
    
    def compute_utility(self, player):
        "If player wins in this state, return 1; if otherplayer wins return -1; else return 0."
        if (self.isOver == 0):
            if (player == self.winner):
             return 1
            else:
                return -1
        else:
            return 0

    def displayAux(self, x, y):
        dic = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
        posAtual = dic.get(y) + str(x)
        if(posAtual in self.white):
            if(y == 8):
                return 'W'
            return 'W '
        elif(posAtual in self.black):
            if(y == 8):
                return 'B'
            return 'B '
        else:
            if(y == 8):
                return '.'
            return '. '

    def display(self):
        print("-----------------")
        for x in reversed(range(1, 9)):
            print(str(x) + "|", end="")
            for y in reversed(range(1, 9)):
                print(self.displayAux(x,9-y), end = "")
                if(y == 1):
                    print()
        print("-+---------------")
        print(" |a b c d e f g h")

    def finished(self):
        if self.to_move == 1:
            for checkWin in self.white:
                if checkWin[-1] == '8':
                    return 0
        if self.to_move == 2:
            for checkWin in self.black:
                if checkWin[-1] == '1':
                    return 0
        return 1  
        
        
class JogoBT_19(Game):
    """Play Breakthrough on an 8 x 8 board, with Max (first to_move) playing 'B'.
    """
    def list_init(self, to_moveType) :
        abc = ["a","b","c","d","e","f","g","h"]
        
        if to_moveType == "W" :
            joinedList = list(map(lambda x : [x+"1", x+"2"], abc))
            return [item for sublist in joinedList for item in sublist]
        else :
            joinedList = list(map(lambda x : [x+"7", x+"8"], abc))
            return [item for sublist in joinedList for item in sublist]
            
            
    def __init__(self,n=8):
        self.initial = EstadoBT_19(to_move = 1, white = self.list_init("W"), black = self.list_init("B"))
        self.board = [(x, y) for x in range(8, 0)
                             for y in range(8, 0)]
        pass
    
    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        "If the player is S and .utility == 1 then return .utility"
        "Otherwise return the symmetric. Note that the symmetric of 0 is 0"
        "Note that player might be different from the player within the state that has just virtually played"
        return state.compute_utility(player)
        
    def actions(self, state):
        return state.moves()

    def result(self, state, move):
        newState = copy.deepcopy(state)

        varIn = move[0]+move[1]
        varOut = move[-2]+move[-1]

        if varIn in newState.white:
            if(varOut in newState.black):
                newState.black.remove(varOut)
            newState.white.remove(varIn)
            newState.white.append(varOut)
            newState.white.sort()

        if varIn in newState.black:
            if(varOut in newState.white):
                newState.white.remove(varOut)
            newState.black.remove(varIn)
            newState.black.append(varOut)
            newState.black.sort()
        
        newState.isOver = newState.finished()
        
        if(newState.isOver == 1) :
            if newState.to_move == 1:
                nextto_move = 2
            else:
                nextto_move = 1
                
            return EstadoBT_19(to_move = nextto_move, white = newState.white, black = newState.black)
        else :
            return EstadoBT_19(to_move = state.to_move, white = newState.white, black = newState.black)

    def terminal_test(self, state):
        isOver = state.finished() == 0
        if(isOver):
            return True 
        else:
            return False

    def display(self, state):
        state.display()
        if state.isOver == 1 :
            if state.to_move == 1 :
                nextPlayer = 'W'
            else :
                nextPlayer = 'B'
            print("--NEXT PLAYER:", nextPlayer)
    
    def executa(self, estado, listaJogadas):
        "executa varias jogadas sobre um estado dado"
        "devolve o estado final "
        s = estado
        for j in listaJogadas:
            s = self.result(s, j)
        return s
    
