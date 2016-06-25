numlist = []
numtotal = 0.0
nummean = 0.0
nummin = 0.0
nummax = 0.0
itn = 0
while 5 == 5:
    x = raw_input("Can I have a number? If finished, type 'done' ")
    if x == "done":
        numlen = len(numlist)
        nummean = numtotal/numlen
        for num in numlist:
            itn = itn + 1
            if itn > 1:
                if num >= nummax:
                    nummax = num
                if num <= nummin:
                    nummin = num
            else:
                nummin = num
                nummax = num
        break
    try:
        x2 = float(x)
        numlist = numlist + [x2]
        numtotal = numtotal + x2
    except:
        print "Invalid input."
print str(numlen) + " numbers totalling " + str(numtotal) + ". The average is " + str(nummean)
print "The minimum and maximum are " + str(nummin) + " and " + str(nummax) + ", respectively."
