fn = raw_input("Enter a file name! ")
try:
    fhand = open(fn)
    receivedcount = 0
    for line in fhand:
        if line.startswith("From"):
            line = line.rstrip()
            words = line.split(" ")
            print "One message received from", words[1]
            receivedcount += 1
    print "\nYou've got " + str(receivedcount) + " mails!"
except:
    print "Can't open that, or you're messing with me!"
