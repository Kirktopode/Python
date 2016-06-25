while True:
    fn = raw_input("Enter a file name or enter 'done'.\n>>")
    alchar = {}
    charcount = 0
    try:
        fhand = open(fn)
        for line in fhand:
            line = line.rstrip()
            line = line.lower()
            for char in line:
                if char.isalpha():
                    if char in alchar:
                        alchar[char] += 1
                    else:
                        alchar[char] = 1
                    charcount += 1
                else: continue
        chartups = alchar.items()
        tupchars = []
        for key, value in chartups:
            tupchars.append((value,key))
        chartups.sort()
        tupchars.sort(reverse = True)
        for tup in tupchars:
            print str(tup[1]) + ":" + str(tup[0]), "----->", str(round((float(tup[0])/charcount)*100, 2)) + "%"
    except:
        if fn == "done":
            print "Goodbye."
            break
        print "Can't open that, or you're messing with me!"
