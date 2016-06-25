import random
import time

def iamthepoet():
    alist = ["full", "heavy", "content", "fat", "willful", "skillful", "elegant", "equivocative", "fast", "slow", "buttered", "high", "low", "free", "angry", "pathetic", "rippling", "wavering"]
    nlist = ["pond", "bird", "blanket", "phone", "sock", "sheet", "river", "kangaroo", "horse", "lion", "tiger", "extrovert", "chef", "artisan", "executioner", "writer", "python", "fruit", "banana", "man", "woman", "child"]
    avlist = ["quickly", "angrily", "heavily", "moodily", "placidly", "drunkenly", "belatedly", "softly", "cantankerously"]
    plist = ["on", "over", "in", "at", "along", "above", "about", "across", "behind", "around", "after", "along", "below", "beneath", "beside", "beyond", "by", "down", "for", "near", "off", "out", "onto"]
    vlist = ["eats", "cavorts", "cuts", "prances", "runs", "ponders", "stirs", "licks", "massages", "caresses", "fondles", "pulls", "paddles", "spanks", "reads", "opens", "slides"]
    a1 = alist[random.randint(0, len(alist)-1)]
    a2 = alist[random.randint(0, len(alist)-1)]
    a3 = alist[random.randint(0, len(alist)-1)]
    n1 = nlist[random.randint(0, len(nlist)-1)]
    n2 = nlist[random.randint(0, len(nlist)-1)]
    n3 = nlist[random.randint(0, len(nlist)-1)]
    av = avlist[random.randint(0, len(avlist)-1)]
    p1 = plist[random.randint(0, len(plist)-1)]
    p2 = plist[random.randint(0, len(plist)-1)]
    v1 = vlist[random.randint(0, len(vlist)-1)]
    v2 = vlist[random.randint(0, len(vlist)-1)]
    v3 = vlist[random.randint(0, len(vlist)-1)]
    while a1 == a2:
        a2 = alist[random.randint(0, len(alist)-1)]
    while a2 == a3 or a1 == a3:
        a3 = alist[random.randint(0, len(alist)-1)]
    while n1 == n2:
        n2 = nlist[random.randint(0, len(nlist)-1)]
    while n2 == n3 or n1 == n3:
        n3 = nlist[random.randint(0, len(nlist)-1)]
    while p1 == p2:
        p2 = plist[random.randint(0, len(plist)-1)]
    while v1 == v2:
        v2 = vlist[random.randint(0, len(vlist)-1)]
    while v2 == v3 or v1 == v3:
        v3 = vlist[random.randint(0, len(vlist)-1)]
    aan = "a"
    if a1[0] in ['a', 'e', 'i', 'o', 'u']:
        aan = "an"
    aan2 = "a"
    if a3[0] in ['a', 'e', 'i', 'o', 'u']:
        aan2 = "an"
    return "{} {} {}\n{} {} {} {} {} the {} {}\n{}, the {} {}\nthe {} {} {} {} {} {}".format(aan, a1, n1, aan, a1, n1, v1, p1, a2, n2, av, n1, v2, n2, v3, p2, aan2, a3, n3)

while True:
    x = raw_input("\nEnter most anything to generate a poem which deletes all others.\nYou may also enter \"append\" to add a poem to what you have.\nYou may also copy the poems to a new poem by typing \"copy\".\n")
    if x.lower() == "quit":
        print "Goodbye."
        break
    elif x.lower() == "append":
        file_output = open("poemspawn.txt", "a")
        poemlines = "\n\n"+iamthepoet()
        file_output.writelines(poemlines)
        print "Printed:\n\n{}".format(poemlines)
        file_output.close()
    elif x.lower() == "copy":
        with open("poemspawn.txt", "r") as poems, open("poemspread.txt", "w") as poemdest:
            poemread = poems.readlines()
            print poems.readlines()
            for line in poemread:
                poemdest.write(line)
                print "Copied:{}".format(line.rstrip())
            
    elif x.lower() == "most anything":
        print "\nSmart aleck."
        time.sleep(1)
        file_output =open("poemspawn.txt", "w")
        poemlines = iamthepoet()
        print "Printed: {}".format(poemlines)
        file_output.writelines(poemlines)
        file_output.close
    else:
        file_output =open("poemspawn.txt", "w")
        poemlines = iamthepoet()
        print "Printed:\n\n{}".format(poemlines)
        file_output.writelines(poemlines)
        file_output.close
        
