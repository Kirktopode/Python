import re
while True:
    hand = open('test.txt')
    try:
        x = raw_input("Enter a real expression.\n>>")
        count = 0
        for line in hand:
            line = line.rstrip()
            if re.search(x, line):
                print line
                count += 1
        print count, "lines matched your entry."
        
    except:
        print "Try that again."
