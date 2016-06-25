monthlist = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
monthdayslist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weeknumber = len(weekdays)
daycount = 0
datemonth = raw_input("What month? ")
datemonth = datemonth.lower
if datemonth in monthlist:
    monthnum = monthlist.index(datemonth)
    dateday = raw_input("What day of the month? ")
    try:
    day = int(dateday)
    if day <= monthdayslist[monthnum] and day > 0:
        for days in monthdayslist[:monthnum]:
            daycount += days
        daycount += day + 4
        print "The day of the week is", weekdays[daycount%weeknumber]
    else:
        print "Ain't that many days in that month."
    except:
        print "Invalid input."
else:
    print "Ain't no month."
