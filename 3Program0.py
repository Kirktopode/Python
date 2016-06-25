h = input("Hours? ")
r = input("Rate? ")
o = 0.0
if h > 40:
    o = (h-40.0)/2.0
print "Pay = " + str(h*r+o*r)
