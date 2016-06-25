fn = raw_input("Enter a file name! ")
try:
    fhand = open(fn)
    words = []
    for line in fhand:
        line = line.rstrip()
        words += line.split(" ")
    words.sort()
    print words
except:
    print "Can't open that, or you're messing with me!"
