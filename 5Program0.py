numlist = []
numtotal = 0.0
nummean = 0.0
while 5 == 5:
    x = raw_input("Can I have a number? If not, type 'done' ")
    if x == "done":
        numlen = len(numlist)
        nummean = numtotal/numlen
        break
    try:
        x2 = int(x)
        numlist = numlist + [x2]
        numtotal = numtotal + x2
    except:
        print "Invalid input."
print str(numlen) + " numbers totalling " + str(numtotal) + ". The average is " + str(nummean)
