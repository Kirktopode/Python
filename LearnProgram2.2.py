monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthdayslist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weeknumber = len(weekdays)
monthcount = 0
x = 0
while x == 0:
    datemonth = raw_input("What month? ")
    if datemonth == monthlist[0] or datemonth == monthlist [1] or datemonth == monthlist [2] or datemonth == monthlist [3] or datemonth == monthlist [4] or datemonth == monthlist [5] or datemonth == monthlist [6] or datemonth == monthlist [7] or datemonth == monthlist [8] or datemonth == monthlist [9] or datemonth == monthlist [10] or datemonth == monthlist [11]:
        x2 = 0
        if datemonth == monthlist[0]:
            monthcount = 0
        if datemonth == monthlist[1]:
            monthcount = 1
        if datemonth == monthlist[2]:
            monthcount = 2
        if datemonth == monthlist[3]:
            monthcount = 3
        if datemonth == monthlist[4]:
            monthcount = 4
        if datemonth == monthlist[5]:
            monthcount = 5
        if datemonth == monthlist[6]:
            monthcount = 6
        if datemonth == monthlist[7]:
            monthcount = 7
        if datemonth == monthlist[8]:
            monthcount = 8
        if datemonth == monthlist[9]:
            monthcount = 9
        if datemonth == monthlist[10]:
            monthcount = 10
        if datemonth == monthlist[11]:
            monthcount = 11
        while x2 == 0:
            dateday = input("What day of the month?" )
            if dateday <= monthdayslist[monthcount] and dateday > 0:
                dateday2 = 0
                if datemonth == "February":
                    dateday2 = monthdayslist[0]
                if datemonth == "March":
                    dateday2 = monthdayslist[0] + monthdayslist[1]
                if datemonth == "April":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2]
                if datemonth == "May":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3]
                if datemonth == "June":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4]
                if datemonth == "July":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4] + monthdayslist [5]
                if datemonth == "August":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4] + monthdayslist [5] + monthdayslist [6]
                if datemonth == "September":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4] + monthdayslist [5] + monthdayslist [6] + monthdayslist [7]
                if datemonth == "October":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4] + monthdayslist [5] + monthdayslist [6] + monthdayslist [7] + monthdayslist [8]
                if datemonth == "November":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4] + monthdayslist [5] + monthdayslist [6] + monthdayslist [7] + monthdayslist [8] + monthdayslist [9]
                if datemonth == "December":
                    dateday2 = monthdayslist[0] + monthdayslist[1] + monthdayslist[2] + monthdayslist[3] + monthdayslist [4] + monthdayslist [5] + monthdayslist [6] + monthdayslist [7] + monthdayslist [8] + monthdayslist [9] + monthdayslist [10]
                x2 = 1
                print "The date is " + str(weekdays[(dateday2+dateday+5)%7-1]) + " " + str(datemonth) + " " + str(dateday)
            else:
                print "Invalid date."
                continue
    else:
        print "Invalid month. Check spelling and capitalization."
        continue
        
    
