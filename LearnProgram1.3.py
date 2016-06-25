grades = [87.0, 94.0, 71.0, 99.0, 82.0, 68.0, 90.0, 76.0, 84.0]
A = 0
B = 0
C = 0
D = 0
gx = 0
g0 = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
g6 = 0
g7 = 0
g8 = 0
itn = 0
itn2 = 0
for grade in grades:
 if grade > 89:
  A = A + 1
 if grade > 79 and grade < 90:
  B = B + 1
 if grade > 69 and grade < 80:
  C = C + 1
 if grade > 59 and grade < 70:
  D = D + 1
 if itn == 0:
  g0 = grade
 if itn == 1:
  g1 = grade
 if itn == 2:
  g2 = grade
 if itn == 3:
  g3 = grade
 if itn == 4:
  g4 = grade
 if itn == 5:
  g5 = grade
 if itn == 6:
  g6 = grade
 if itn == 7:
  g7 = grade
 if itn == 8:
  g8 = grade
 itn = itn + 1
while itn2 < 9:
 if g0 > g1:
     gx = g1
     g1 = g0
     g0 = gx
 if g1 > g2:
     gx = g2
     g2 = g1
     g1 = gx
 if g2 > g3:
     gx = g3
     g3 = g2
     g2 = gx
 if g3 > g4:
     gx = g4
     g4 = g3
     g3 = gx
 if g4 > g5:
     gx = g5
     g5 = g4
     g4 = gx
 if g5 > g6:
     gx = g6
     g6 = g5
     g5 = gx
 if g6 > g7:
     gx = g7
     g7 = g6
     g6 = gx
 if g7 > g8:
     gx = g8
     g8 = g7
     g7 = gx
 itn2 = itn2 + 1
print str(A) + " A"
print str(B) + " B"
print str(C) + " C"
print str(D) + " D"
mean = sum(grades)/(A+B+C+D)
print "Mean = " + str(mean)
print "Median = " + str(g4)


