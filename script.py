txt = open("captured.dat")
inFile = txt.read()
origLines = inFile.split("\n")
newLines = ""

for line in origLines:
	parts = line.split(" ")
	inputDevice = parts[0][:-1]
	code = parts[1]
	event = parts[2]
	value = parts[3][:-1]

	strEvent = str(int("0x"+event,16))
	strValue = str(int("0x"+value, 16))
	newLines += "sendevent "+inputDevice+" " +code+ " "+ strEvent + " "+ strValue+"\n"

print newLines
