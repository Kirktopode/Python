thing = raw_input("Can I have some words prease? ")
thingsmall = raw_input("How about something shorter? ")
slen = len(thingsmall)
if slen == 1:
    if thingsmall.isalpha():
        sup = thingsmall.upper()
        slow = thingsmall.lower()
        lcount = thing.count(slow)
        ucount = thing.count(sup)
        print "There is/are", str(lcount), "of", '"' + slow + '"', "and", str(ucount), "of", '"' + sup + '"', "in the bigger words."
    else:
        scount = thing.count(thingsmall)
        print "There is/are " + str(scount) + ' of "' + thingsmall + '" in the bigger words.'
else:
    scount = thing.count(thingsmall)
    print "There is/are " + str(scount) + ' of "' + thingsmall + '" in the bigger words.'
