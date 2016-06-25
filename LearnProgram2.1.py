thing = raw_input("Can I have some words prease? ")
thingsmall = raw_input("How about just one character? ")
num = 0
darkchar = "0"
uplow = 2
lowcount = 0
highcount = 0
if thingsmall == "a":
    darkchar = "A"
    uplow = 0
if thingsmall == "b":
    darkchar = "B"
    uplow = 0
if thingsmall == "c":
    darkchar = "C"
    uplow = 0
if thingsmall == "d":
    darkchar = "D"
    uplow = 0
if thingsmall == "e":
    darkchar = "E"
    uplow = 0
if thingsmall == "f":
    darkchar = "F"
    uplow = 0
if thingsmall == "g":
    darkchar = "G"
    uplow = 0
if thingsmall == "h":
    darkchar = "H"
    uplow = 0
if thingsmall == "i":
    darkchar = "I"
    uplow = 0
if thingsmall == "j":
    darkchar = "J"
    uplow = 0
if thingsmall == "k":
    darkchar = "K"
    uplow = 0
if thingsmall == "l":
    darkchar = "L"
    uplow = 0
if thingsmall == "m":
    darkchar = "M"
    uplow = 0
if thingsmall == "n":
    darkchar = "N"
    uplow = 0
if thingsmall == "o":
    darkchar = "O"
    uplow = 0
if thingsmall == "p":
    darkchar = "P"
    uplow = 0
if thingsmall == "q":
    darkchar = "Q"
    uplow = 0
if thingsmall == "r":
    darkchar = "R"
    uplow = 0
if thingsmall == "s":
    darkchar = "S"
    uplow = 0
if thingsmall == "t":
    darkchar = "T"
    uplow = 0
if thingsmall == "u":
    darkchar = "U"
    uplow = 0
if thingsmall == "v":
    darkchar = "V"
    uplow = 0
if thingsmall == "w":
    darkchar = "W"
    uplow = 0
if thingsmall == "x":
    darkchar = "X"
    uplow = 0
if thingsmall == "y":
    darkchar = "Y"
    uplow = 0
if thingsmall == "z":
    darkchar = "Z"
    uplow = 0
if thingsmall == "A":
    darkchar = "a"
    uplow = 1
if thingsmall == "B":
    darkchar = "b"
    uplow = 1
if thingsmall == "C":
    darkchar = "c"
    uplow = 1
if thingsmall == "D":
    darkchar = "d"
    uplow = 1
if thingsmall == "E":
    darkchar = "e"
    uplow = 1
if thingsmall == "F":
    darkchar = "f"
    uplow = 1
if thingsmall == "G":
    darkchar = "g"
    uplow = 1
if thingsmall == "H":
    darkchar = "h"
    uplow = 1
if thingsmall == "I":
    darkchar = "i"
    uplow = 1
if thingsmall == "J":
    darkchar = "j"
    uplow = 1
if thingsmall == "K":
    darkchar = "k"
    uplow = 1
if thingsmall == "L":
    darkchar = "l"
    uplow = 1
if thingsmall == "M":
    darkchar = "m"
    uplow = 1
if thingsmall == "N":
    darkchar = "n"
    uplow = 1
if thingsmall == "O":
    darkchar = "o"
    uplow = 1
if thingsmall == "P":
    darkchar = "p"
    uplow = 1
if thingsmall == "Q":
    darkchar = "q"
    uplow = 1
if thingsmall == "R":
    darkchar = "r"
    uplow = 1
if thingsmall == "S":
    darkchar = "s"
    uplow = 1
if thingsmall == "T":
    darkchar = "t"
    uplow = 1
if thingsmall == "U":
    darkchar = "u"
    uplow = 1
if thingsmall == "V":
    darkchar = "v"
    uplow = 1
if thingsmall == "W":
    darkchar = "w"
    uplow = 1
if thingsmall == "X":
    darkchar = "x"
    uplow = 1
if thingsmall == "Y":
    darkchar = "y"
    uplow = 1
if thingsmall == "Z":
    darkchar = "z"
    uplow = 1
for char in thing:
    if char == thingsmall:
        num = num + 1
    if darkchar != "0":
        if char == darkchar:
            if uplow == 0:
                highcount = highcount + 1
            if uplow == 1:
                lowcount = lowcount + 1
print "There are " + str(num) + ' of "' + str(thingsmall) + '" in that there words.'
if darkchar != "0":
    if uplow == 0:
        if highcount > 0:
            print "There are also " + str(highcount) + ' of "' + str(darkchar) + '"'
    if uplow == 1:
        if lowcount > 0:
            print "There are also " + str(lowcount) + ' of "' + str(darkchar) + '"'
