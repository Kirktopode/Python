fhand = open('test.txt')
count = 0
datesdic = {}
senderdic = {}
domains = {}
Largestnum = 0
Largest = None
for line in fhand:
    line = line.rstrip()
    lwords = line.split(" ")
    if len(lwords) < 3:
        continue
    else:
        if lwords[0] == "From":
            date = lwords[2]
            sender = lwords[1]
            domsplit = sender.split(".")
            sendername = domsplit[0]
            if date in datesdic: datesdic[date] += 1
            else: datesdic[date] = 1
            if sendername in senderdic: senderdic[sendername] += 1
            else: senderdic[sendername] = 1
            dom = domsplit[1]
            if dom in domains: domains[dom] += 1
            else: domains[dom] = 1
        else: continue
tuplelist = senderdic.items()
numLargest = 0
for tup in tuplelist:
    if tup[1] > numLargest:
        numLargest = tup[1]
        Largest2 = tup[0]
tuplist2 = []
for key, val in senderdic.items():
    tuplist2.append((val,key))
tuplist2.sort()
x = len(tuplist2)-1
tuplarge = tuple(tuplist2[x])
tuplargename = tuplarge [1]
for thing in senderdic:
    if senderdic[thing] > Largestnum:
        Largestnum = senderdic[thing]
        Largest = thing
print "Dates received:", datesdic
print "Senders:", senderdic
print "Domains:", domains
print "Most senders:", Largest
print "But my other code says this is the most senders:", Largest2
print "My most interesting code says this is the most senders:", tuplargename
