import os
inFile = open("launcher.sh")
outFile = open("result.sh", "w")
for line in inFile:
	new = line.replace("//","")
	outFile.write(new)
inFile.close()
outFile.close()

inFile = open("result.sh")
outFile = open("launcher.sh", "w")
for line in inFile:
	outFile.write(new)
inFile.close()
outFile.close()

os.remove('/home/pi/Desktop/result.sh')