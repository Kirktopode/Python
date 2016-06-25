import random
Awins = 0.0
for i in range(10000):
 ran1 = random.random()
 ran2 = random.random()
 ran3 = random.random()
 if (ran1 <= .87 and ran2 <= .65) or (ran2 <= .65 and ran3 <= .17) or (ran1 <= .87 and ran3 <= .17):
  Awins = Awins + 1.0
Achance = (Awins/100.0)
print "Candidate A has a " + str(Achance) + "% chance of winning."
print "Candidate B has a " + str(100-Achance) + "% chance of winning."
