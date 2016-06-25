unilist = [

['California Institute of Technology', 2175, 37704],

['Harvard', 19627, 39849],

['Massachusetts Institute of Technology', 10566, 40732],

['Princeton', 7802, 37000],

['Rice', 5879, 35551],

['Stanford', 19535, 40569],

['Yale', 11701, 40500]

]

def unilyzer(unilist):
    stucountlist = []
    tuitionlist = []
    for lis in unilist:
        stucountlist.append(lis[1])
        tuitionlist.append(lis[2])
    return stucountlist, tuitionlist

def mean(lis):
    total = 0.0
    for num in lis:
        total += num
    return total/len(lis)

def median(lis):
    lis.sort()
    lislen = len(lis)
    if lislen % 2 == 0:
        return (lis[lislen/2]+lis[lislen/2 - 1])/2.0
    return lis[lislen/2]

listwarps = unilyzer(unilist)
mean1 = mean(listwarps[0])
mean2 = mean(listwarps[1])
lis1 = listwarps[0]
lis2 = listwarps[1]
median1 = median(lis1)
median2 = median(lis2)

print "Mean of student numbers:", mean1, "\nMedian of student numbers:", median1
print "Mean of tuition:", mean2, "\nMedian of tuition:", median2
