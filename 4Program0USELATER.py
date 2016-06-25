import random


def statroll():
    a = random.randint (1,6)
    b = random.randint (1,6)
    c = random.randint (1,6)
    d = random.randint (1,6)
    e = 0
    if a <= b and a <= c and a <= d:
        e = b + c + d
    elif b <= a and b <= c and b <= d:
        e = a + c + d
    elif c <= b and c <= a and c <= d:
        e = b + a + d
    elif d <= b and d <= c and d <= a:
        e = b + c + a
    return e

st = statroll()
dx = statroll()
cn = statroll()
iq = statroll()
wi = statroll()
ch = statroll()
stmod = (st - 10)/2
dxmod = (dx - 10)/2
cnmod = (cn - 10)/2
iqmod = (iq - 10)/2
wimod = (wi - 10)/2
chmod = (ch - 10)/2
        

def statprint(st, stmod, dx, dxmod, cn, cnmod, iq, iqmod, wi, wimod, ch, chmod):
    print " "
    print "Strength: " + str(st) + " " + str(stmod)
    print "Dexterity: " + str(dx) + " " + str(dxmod)
    print "Constitution: " + str(cn) + " " + str(cnmod)
    print "Intelligence: " + str(iq) + " " + str(iqmod)
    print "Wisdom: " + str(wi) + " " + str(wimod)
    print "Charisma: " + str(ch) + " " + str(chmod)
    print " "

statprint (st, stmod, dx, dxmod, cn, cnmod, iq, iqmod, wi, wimod, ch, chmod)

hpmax = 0
hpnow = 0
gp = 0
bab = 0

cor = 0
while cor == 0:
    clas = input("What is your class? 1. Fighter 2. Rogue 3. Wizard 4. Cleric 5. REROLL STATS ")
    if clas == 1:
        hpmax = 10 + cnmod
        hpnow = hpmax
        gp = 150
        bab = 1
        cor = 1
    elif clas == 2:
        hpmax = 6 + cnmod
        hpnow = hpmax
        gp = 100
        cor = 1
    elif clas == 3:
        hpmax = 4 + cnmod
        if hpmax < 1:
            hpmax = 1
        hpnow = hpmax
        gp = 75
        cor = 1
    elif clas == 4:
        hpmax = 8 + cnmod
        hpnow = hpmax
        gp = 125
        cor = 1
    elif clas == 5:
        print "New Roll:"
        st = statroll()
        dx = statroll()
        cn = statroll()
        iq = statroll()
        wi = statroll()
        ch = statroll()
        stmod = (st - 10)/2
        dxmod = (dx - 10)/2
        cnmod = (cn - 10)/2
        iqmod = (iq - 10)/2
        wimod = (wi - 10)/2
        chmod = (ch - 10)/2
        statprint (st, stmod, dx, dxmod, cn, cnmod, iq, iqmod, wi, wimod, ch, chmod)
    else:
        print " "
        print "Invalid input. Please try again."
        print " "
print " "
print "HP: " + str(hpmax)
print "GP: " + str(gp)
print "Melee Attack: " + str(bab + stmod)
print "Ranged Attack: " + str(bab + dxmod)
print " "
