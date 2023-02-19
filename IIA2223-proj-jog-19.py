# Grupo 19
# João Santos nº 57103
# Paulo Bolinhas nº 56300
# Rui Martins nº 56283

import random
projTudo_19 = __import__("IIA2223-proj-tudo-19")
import jogar
from jogos import alphabeta_cutoff_search_new

def fa_bacoco(game, state):
    return random.choice(state.moves())


def fa_belarmino(state, player):
    score = 0
    if player == 1:
        piecesList = state.white
    else:
        piecesList = state.black
    
    for piece in piecesList:
        if player == 1:
            score += int(piece[1])**int(piece[1])
        else:
            score += (9-int(piece[1]))**(9-int(piece[1]))
    
    return score

def fa_belarminoPlus(state, player):
    score = 0
    alphabet = ["a","b","c","d","e","f","g","h"]

    if player == 1:
        piecesList = state.white
    else:
        piecesList = state.black
    
    for piece in piecesList:
        if player == 1:
            # score += int(piece[1])**int(piece[1])
            if piece[1] == '8':
                score += 10
                
            if piece[1] == '6' or piece[1] == '7':
                score += 6
            
            if piece[1] == '4' or piece[1] == '5':
                score += 4
        
            for pieceBlack in state.black:
                if pieceBlack[1] == '2' or pieceBlack[1] == '3' or pieceBlack[1] == '4':
                    score -= 7
                
                if pieceBlack[1] == '5' or pieceBlack[1] == '6':
                    score -= 4
                
        else:
            # score += (9-int(piece[1]))**(9-int(piece[1]))
            if piece[1] == '1':
                score += 10
                
            if piece[1] == '3' or piece[1] == '2':
                score += 6
            
            if piece[1] == '5' or piece[1] == '4':
                score += 4
                
            for pieceWhite in state.white:
                if pieceWhite[1] == '7' or pieceWhite[1] == '6' or pieceWhite[1] == '5':
                    score -= 7
                
                if pieceWhite[1] == '4' or pieceWhite[1] == '3':
                    score -= 4
    
    return score


def fa_mediano(state, player):
    score = 0
    alphabet = ["a","b","c","d","e","f","g","h"]

    if player == 1:
        piecesList = state.white
    else:
        piecesList = state.black
    
    for piece in piecesList:
        if player == 1:
            score += int(piece[1])*100000
            
            if piece[1] == '8':
                score += 10000000
                
            if piece[1] == '6' or piece[1] == '7':
                score += 700000
            
            if piece[1] == '4' or piece[1] == '5':
                score += 400000
        
            for pieceBlack in state.black:
                if pieceBlack[1] == '2' or pieceBlack[1] == '3' or pieceBlack[1] == '4':
                    score -= 700000
                
                if pieceBlack[1] == '5' or pieceBlack[1] == '6':
                    score -= 500000
            
            # caso 'a'
            if piece[0] == 'a':
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1)) in state.black:
                    score -= 400000
            
             # caso 'h'        
            elif piece[0] == 'h':
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1)) in state.black:
                    score -= 400000
            
            elif(piece[0] != 'a' and piece[0] != 'h'):
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1)) in state.black:
                    score -= 400000
                
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1)) in state.black:
                    score -= 400000
                
        else:
            score += int(piece[1])*100000
            if piece[1] == '1':
                score += 10000000
                
            if piece[1] == '3' or piece[1] == '2':
                score += 700000
            
            if piece[1] == '5' or piece[1] == '4':
                score += 400000
                
            for pieceWhite in state.white:
                if pieceWhite[1] == '7' or pieceWhite[1] == '6' or pieceWhite[1] == '5':
                    score -= 700000
                
                if pieceWhite[1] == '4' or pieceWhite[1] == '3':
                    score -= 500000
            
            # caso 'a'
            if piece[0] == 'a':
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1)) in state.white:
                    score -= 400000
            
             # caso 'h'        
            elif piece[0] == 'h':
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1)) in state.white:
                    score -= 400000
            
            elif(piece[0] != 'a' and piece[0] != 'h'):
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1)) in state.white:
                    score -= 400000
                
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1)) in state.white:
                    score -= 400000
    
    return score



def func_aval_19(state, player):
    score = 0
    alphabet = ["a","b","c","d","e","f","g","h"]

    if player == 1:
        piecesList = state.white
    else:
        piecesList = state.black
    
    for piece in piecesList:
        if player == 1:
            
            if piece[1] == '8':
                score += 10000000000
                
            if piece[1] == '7':
                score += 900000

            if piece[1] == '6':
                score += 700000
            
            if piece[1] == '5':
                score += 500000

            if piece[1] == '4':
                score += 300000
        
            for pieceBlack in state.black:
                if pieceBlack[1] == '2':
                    score -= 900000
                
                if pieceBlack[1] == '3':
                    score -= 700000
                
                if pieceBlack[1] == '4':
                    score -= 500000

                if pieceBlack[1] == '5':
                    score -= 300000

                if pieceBlack[1] == '6':
                    score -= 100000
            
            # linha defesa
            nDef = 0
            for elem in state.white:
                if elem[1] == '1':
                    nDef += 1
            
            if nDef < 6:
                if (piece[1] == '2'):
                    score -= 700000
                 
            
             # caso 'a'
            if piece[0] == 'a':
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1)) in state.black:
                    score -= 700000
                if ((alphabet[alphabet.index(piece[0])+2] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)):
                    score -= 700000
            
             # caso 'h'        
            elif piece[0] == 'h':
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1)) in state.black:
                    score -= 700000
                if ((alphabet[alphabet.index(piece[0])-2] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white)):
                    score -= 700000

            if piece[0] == 'b':
                if ((alphabet[alphabet.index(piece[0])+2] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white)):                    
                    score -= 700000
            
            if piece[0] == 'g':
                if ((alphabet[alphabet.index(piece[0])-2] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)):                    
                    score -= 700000
            
            elif(piece[0] != 'a' and piece[0] != 'h'):
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1)) in state.black:
                    score -= 700000
                
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1)) in state.black:
                    score -= 700000

                if(piece[0] != 'b' and piece[0] != 'g'):
                    if ((alphabet[alphabet.index(piece[0])-2] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white) 
                    or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])+1) in state.white)
                    or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)
                    or (alphabet[alphabet.index(piece[0])+2] + str(int(piece[1])+2)) in state.black and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])+1) in state.white)):
                        score -= 700000
                
        else:
            
            if piece[1] == '1':
                score += 10000000000
                
            if piece[1] == '2':
                score += 900000

            if piece[1] == '3':
                score += 700000
            
            if piece[1] == '4':
                score += 500000

            if piece[1] == '5':
                score += 300000
        
            for pieceWhite in state.white:
                if pieceWhite[1] == '7':
                    score -= 900000
                
                if pieceWhite[1] == '6':
                    score -= 700000
                
                if pieceWhite[1] == '5':
                    score -= 500000

                if pieceWhite[1] == '4':
                    score -= 300000

                if pieceWhite[1] == '3':
                    score -= 100000
            
            # linha defesa
            nDef = 0
            for elem in state.white:
                if elem[1] == '8':
                    nDef += 1
            
            if nDef < 6:
                if (piece[1] == '7'):
                    score -= 700000
                
            
             # caso 'a'
            if piece[0] == 'a':
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1)) in state.white:
                    score -= 700000
                if ((alphabet[alphabet.index(piece[0])+2] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)):
                    score -= 700000
            
             # caso 'h'        
            elif piece[0] == 'h':
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1)) in state.white:
                    score -= 700000
                if ((alphabet[alphabet.index(piece[0])-2] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black)):
                    score -= 700000

            if piece[0] == 'b':
                if ((alphabet[alphabet.index(piece[0])+2] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black)):                    
                    score -= 700000
            
            if piece[0] == 'g':
                if ((alphabet[alphabet.index(piece[0])-2] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black)
                or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)):                    
                    score -= 700000
            
            elif(piece[0] != 'a' and piece[0] != 'h'):
                if (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1)) in state.white:
                    score -= 700000
                
                if (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1)) in state.white:
                    score -= 700000

                if(piece[0] != 'b' and piece[0] != 'g'):
                    if ((alphabet[alphabet.index(piece[0])-2] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black) 
                    or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])-1] + str(int(piece[1])-1) in state.black)
                    or (alphabet[alphabet.index(piece[0])] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)
                    or (alphabet[alphabet.index(piece[0])+2] + str(int(piece[1])-2)) in state.white and (alphabet[alphabet.index(piece[0])+1] + str(int(piece[1])-1) in state.black)):
                        score -= 700000
                
    return score

belarmino = jogar.Jogador("Belarmino",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,0,eval_fn=fa_belarmino))

belarminoPlus = jogar.Jogador("BelarminoPlus",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,0,eval_fn=fa_belarminoPlus))


mediano = jogar.Jogador("Mediano",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,2,eval_fn=fa_mediano))


tomala = jogar.Jogador("TomaLáa",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,2,eval_fn=func_aval_19))


bacoco = jogar.Jogador("Bacoco", fa_bacoco)

game = projTudo_19.JogoBT_19()

jogo1 = jogar.joga11(game, mediano, tomala)
print(jogo1)
    
jogar.mostraJogo(game, jogo1, True, True)

for i in range(10):
    todosJog = [tomala, mediano]
    campeonato = jogar.faz_campeonato(game, todosJog, nsec=10)