import os
import csv

mypath = "C:/Users/New Owner/Documents/Practice"
while True:
    myfile = raw_input("\nWhat .csv file do you want to look at?\n")
    newpath = os.path.join(mypath, myfile)
    copypath = "C:/Users/New Owner/Documents/Practice/copythings.csv"
    if myfile.lower() == "quit":
        print "Goodbye."
        break
    elif not myfile.lower().endswith(".csv"):
        print "Please include the proper file extension so that I can read it."
        continue
    elif not os.path.exists(newpath):
        print "This file does not exist!"
        continue
    else:
        with open(newpath, "rb") as myspot, open(copypath, "wb") as copyspot:
            myreader = csv.reader(myspot)
            mywriter = csv.writer(copyspot)
            for row in myreader:
                if row[0] == "Traveler":
                    row.append("Class")
                elif row[1].lower().count("fighting") > 0:
                    row.append("Adventurer")
                else:
                    row.append("Other")
                print "Copying :", row
                mywriter.writerow(row)
