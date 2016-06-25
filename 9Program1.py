fhand = open('test.txt')
count = 0
dic = {}
dic2 = {}
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
            if date in dic: dic[date] += 1
            else: dic[date] = 1
            if sender in dic2: dic2[sendername] += 1
            else: dic2[sendername] = 1
            dom = domsplit[1]
            if dom in domains: domains[dom] += 1
            else: domains[dom] = 1
        else: continue
for thing in dic2:
    if dic2[thing] > Largestnum:
        Largestnum = dic2[thing]
        Largest = thing
print "Dates received:", dic
print "Senders:", dic2
print "Domains:", domains
print "Most senders:", Largest
            
