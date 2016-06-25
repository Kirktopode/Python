t = 0
f = 0
while f == 0:
    ho = raw_input("Hours? ")
    try:
        h = float(ho)
        f2 = 0
        while f2 == 0:
            ra = raw_input("Rate? ")
            try:
                r = float(ra)
                o = 0.0
                if h > 40:
                    o = (h-40.0)/2.0
                print "Pay = " + str(h*r+o*r)
                f = 1
                f2 = 1
            except:
                if t < 5:
                    print "I ain't got time fer yer sass. Let's try this again."
                    t = t + 1
                else:
                    print "I ain't talkinna you no more."
                    f2 = 1
                    f = 1
    except:
        if t < 5:
            print "I ain't got time fer yer sass. Let's try this again."
            t = t + 1
        else:
            print "I ain't talkinna you no more."
            f = 1
