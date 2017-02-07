import string
import os, sys

from Socket import sendMessage
from Settings import CHANNEL

def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	#sendMessage(s, "Successfully joined chat")
        #sendMessage(s, "Please make sure to comment in order to recieve a daily point.")
        if os.path.isdir("Channels")==False:
                os.mkdir("Channels",0777)
        if os.path.isdir("./Channels/"+CHANNEL)==False:
                os.mkdir("./Channels/"+CHANNEL,0777)
        path = "./Channels/"+CHANNEL+"/Users"
        if os.path.isdir("./Channels/"+CHANNEL+"/Users") == False:
                os.mkdir(path, 0777)
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
