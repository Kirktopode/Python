def isLeapYear(year):
    if year%4 == 0:
        print str(year), "is a leap year."
        print str(year-1), "is not a leap year."
        print str(year+1), "is not a leap year."
    elif (year+1)%4 == 0:
        print str(year), "is not a leap year."
        print str(year-1), "is not a leap year."
        print str(year+1), "is a leap year."
    elif (year-1)%4 == 0:
        print str(year), "is not a leap year."
        print str(year-1), "is a leap year."
        print str(year+1), "is not a leap year."
    else:
        print str(year), "is not a leap year."
        print str(year-1), "is not a leap year."
        print str(year+1), "is not a leap year."
yearnow = raw_input("What year?")
try:
    yearnow = int(yearnow)
    isLeapYear(yearnow)
except:
    print "Invalid input."
