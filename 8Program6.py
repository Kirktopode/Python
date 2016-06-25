numlist = []
while True:
    num = raw_input("Gimme a number unless yer done.")
    try:
        num = float(num)
        numlist += [num]
    except:
        if num == "done":
            break
        else:
            print "Tell me something I understand, ya big palooka."
print "Yer max is", str(max(numlist)) + "\nYer min is", str(min(numlist))
