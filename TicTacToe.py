import string
import random

from Socket import sendMessage
from Read import getMessage, getUser, getTarget

def startGame(s,user): #s is the openSocket, user is the player calling for the game
    sendMessage(s, "Game Started")
    sendMessage(s,"Player 1 is " + user)
    sendMessage(s, user+", who do you challenge to a game?")
    target = " "
    gameIsPlaying = False;
    testLoop = True
    
    readbuffer = " "
    while testLoop:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            if user == getUser(line):
                message = getMessage(line)
                if ('@'in message):
                    target = getTarget(line)
                    sendMessage(s, "Player 2 is "+target)
                    sendMessage(s, target+", do you accept the challenge?(Y/N)")
                    
            else:
               # if target == getUser(line):
                message = getMessage(line)
                if('y' in message) or ('Y' in message):
                    userChar = ' '
                    targetChar = ' '
                    gameIsPlaying = True
                    begin = firstMove()
                    sendMessage(s,user+", choose a character to use:")
                    if user == getUser(line):
                        userChar = getMessage(line)
                    sendMessage(s,target+", choose a different character to use:")
                    if target == getUser(line) and userChar != getMessage(line):
                        targetChar = getMessage(line)
                    sendMessage(s, user+" chose "+userChar+", while "+target+" chose "+targetChar)
                    if userChar != ' ' and targetChar != ' ':
                        gameIsPlaying == True

                    while gameIsPlaying == True:
                        game = ['#'] *10
                        drawGame(s,game)
                        move = ' '
                        if begin=='1':
                            sendMessage(s,"Your move: "+user)
                            if user==getUser(line):
                                move = getMessage(line)
                            if checkMove(move, game)==True:
                                game[int(move)]=userChar
                            if checkWinner(game,userChar):
                                sendMessage(s,"Hooray! "+user+" has won the game!") 
                                gameIsPlaying = False
                            else:
                                if isBoardFull(game):
                                    sendMessage(s,"The game is a tie!")
                                    gameIsPlaying = False
                                else:
                                    begin=='0'
                        else:
                            sendMessage(s,"Your move: "+target)
                            if target==getUser(line):
                                move = getMessage(line)
                            if checkMove(move,game)==True:
                                game[int(move)]=targetChar
                            if checkWinner(game,targetChar):
                                sendMessage(s, "Hooray! "+target+" has won the game!")
                                gameIsPlaying = False
                            else:
                                if isBoardFull(game):
                                    sendMessage(s, "The game is a tie!")
                                    gameIsPlaying = False
                                else:
                                    begin=='1'
    if(gameIsPlaying == False):
        testLoop = False
        return True

def drawGame(s, game):
    #writes out the game to the chat
    sendMessage(s, ' '+game[7]+' | '+ game[8]+ ' | '+game[9])
    sendMessage(s, '---------')
    sendMessage(s, ' '+game[4]+' | '+game[5]+' | '+game[6])
    sendMessage(s, '---------')
    sendMessage(s, ' '+game[1]+' | '+game[2]+' | '+game[3])

def firstMove():
    if random.randint(0,1)==0:
        return '1'
    else:
        return '2'

def checkMove(move,game):
    if (move in '1 2 3 4 5 6 7 8 9'.split()) and (game[move]== '#'):
        return True

def checkWinner(game, letter):
    return ((game[7] == letter and game[8] == letter and game[9] == letter) or # across the top
            (game[4] == letter and game[5] == letter and game[6] == letter) or # across the middle
            (game[1] == letter and game[2] == letter and game[3] == letter) or # across the bottom
            (game[7] == letter and game[4] == letter and game[1] == letter) or # down the left side
            (game[8] == letter and game[5] == letter and game[2] == letter) or # down the middle
            (game[9] == letter and game[6] == letter and game[3] == letter) or # down the right side
            (game[7] == letter and game[5] == letter and game[3] == letter) or # diagonal
            (game[9] == letter and game[5] == letter and game[1] == letter)) # diagonal


def isBoardFull(game):
    for i in range (1,10):
        if game[i]=='#':
            return False
    return True
