import string

def getUser(line):
        separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(":", 2)
	message = separate[2]
	return message
def getTarget(line):
        separate = line.split(":",2)
        target = separate[2].split("@",2)[1]
        return target
