def investitude(amount, rate, time):
    print "Principle: $" + str(amount)
    for year in range(time):
        amount += amount*rate
        print "Year " + str(year + 1) + ": $" + str(amount)

amount = input("What dollar amount are you initially investing? ")
rate = input("What is the percent of interest (express as a decimal)? ")
time = input("How many years this compound? ")

investitude(amount, rate, time)
