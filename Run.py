import string
from Read import getUser, getMessage, getTarget
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from TicTacToe import startGame

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
                        print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
                        print user + " typed :" + message
                        if ('@'in message):
                                        target = getTarget(line)
                                        print "target is " + target
                        if("!tictactoe" in message):
                                        startGame(s,user)
                                        break

                        if ("megabot1195" in message) or ("Megabot1195" in message):
                                sendMessage(s, "Now that's a name I've not heard in a long time. A long time.")
                                break
			if ("you suck" in message) or ("u suck" in message):
				sendMessage(s, "No, you suck!")
				break
                                
			if "Sonic" in message: 
                                sendMessage(s, "BOOM???")
                                break

