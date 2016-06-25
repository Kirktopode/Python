import urllib
website = raw_input("What website do you want to visit?")
fhand = urllib.urlopen(website)
chars = 0
pcount = 0
for line in fhand:
    chars += len(line.strip())
    pcount += line.count("<P>")
    if chars < 3000:
        print line.strip()
print chars, "CHARACTERS TOTAL IN DOCUMENT\n" + str(pcount), "<P> TAGS IN DOCUMENT"
