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
            hiscorelist = []
            for row in myreader:
                print "Input :", row
                maxscore = 0
                for score in row:
                    if score.isdigit() and int(score) > maxscore:
                        maxscore = int(score)
                row = [row[0], maxscore]
                print "Processing: ", row
                row.reverse()
                hiscorelist.append(row)
            hiscorelist.sort()
            hiscorelist.reverse()
            for score in hiscorelist:
                score.reverse()
            print "Printing: ", hiscorelist
            mywriter.writerows(hiscorelist)
            
