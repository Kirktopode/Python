fn = raw_input("Enter a file name! ")
linetotal = 0
linecount = 0
try:
	fhand = open(fn)
	for line in fhand:
		line = line.rstrip()
		if line.startswith("Value:"):
			x = line.find(" ")
			linenew = line[x:]
			linedata = float(linenew)
			linetotal = linetotal + linedata
			linecount = linecount + 1
	print "Average value is:", str(linetotal/linecount)
except:
	print "Can't open that, or you're messing with me!"
