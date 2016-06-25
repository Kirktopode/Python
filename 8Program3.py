fn = raw_input("Enter a file name! ")
try:
    fhand = open(fn)
    for line in fhand:
        line = line.rstrip()
        print line
except:
    print "Can't open that, or you're messing with me!"
