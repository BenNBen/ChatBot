import string

def getDate(user):
     f = file("Channels/"+CHANNEL+"/Users/"+user+".txt","wr+")
     date = f.readLine(0)
     return date
 
def getPoints(line):
     f = file("Channels/"+CHANNEL+"/Users/"+user+".txt","wr+")
     points = f.readLine(1)
     print points
     return points
	#separate = line.split(":", 2)
	#message = separate[2]
def addPoint(line):
     f = file("Channels/"+CHANNEL+"/Users/"+user+".txt","wr+")
     points = f.readLine(1)
     value = int(points)+1
     #f.write(
