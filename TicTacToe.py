import string
import random

from Socket import sendMessage
from Read import getMessage, getUser, getTarget

def startGame(s,user): #s is the openSocket, user is the player calling for the game
    sendMessage(s, "Game Started")
    sendMessage(s,"Player 1 is " + user)
    sendMessage(s, user+", who do you challenge to a game?")
    gameIsPlaying = True

    readbuffer = " "
    while True:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            #print(line)
            if user == getUser(line):
                message = getMessage(line)
                print user + " typed :" + message
                if ('@'in message):
                    target = getTarget(line)
                    print "target is " + target
                sendMessage(s, "Player 2 is "+target)
                sendMessage(s, target+", do you accept the challenge?(Y/N)")
            if target ==getUser(line):
                message = getMessage(line)
                if('y' in message) or ('Y' in message):
                    gameIsPlaying = True
                    
            while gameIsPlaying:
                game = [' '] *10
                drawGame(s, game)
                begin = firstMove()
                if begin == '1':
                    sendMessage(s, user+", please choose a character to use:")
                else:
                    sendMessage(s, target+", please choose a character to use:")
                break
    


def drawGame(s, game):
    #writes out the game to the chat
    sendMessage(s, '  |  |  ')
    sendMessage(s, ' '+game[7]+' | '+ game[8]+ ' | '+game[9])
    sendMessage(s, '  |  |  ')
    sendMessage(s, '---------')
    sendMessage(s, '  |  |  ')
    sendMessage(s, ' '+game[4]+' | '+game[5]+' | '+game[6])
    sendMessage(s, '  |  |  ')
    sendMessage(s, '---------')
    sendMessage(s, '  |  |  ')
    sendMessage(s, ' '+game[1]+' | '+game[2]+' | '+game[3])
    sendMessage(s, '  |  |  ')

def firstMove():
    if random.randint(0,1)==0:
        return '1'
    else:
        return '2'

#def getCharacter():
