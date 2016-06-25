import os
import csv

mypath = "C:/Users/New Owner/Documents/Practice"
while True:
    infile = raw_input("\nWhat .csv file do you want to split?\n")
    inpath = os.path.join(mypath, infile)
    if infile.lower() == "quit":
        print "Goodbye."
        break
    elif not infile.lower().endswith(".csv"):
        print "Please include the proper file extension so that I can read it."
        continue
    elif not os.path.exists(inpath):
        print "This path does not exist!"
        continue
    else:
        while True:        
            outfile = raw_input("\nWhat would you like to be the base name for the new files?\nFor example, 'base' would become 'base1', 'base2', etc.\n")
            outpath = os.path.join(mypath, outfile)
            if outfile.lower() == "quit":
                print "Type quit again at next input."
                break
            elif not outfile.lower().endswith(".csv"):
                print "If you don't end your file with a '.csv', this isn't going to work."
                continue
            elif outfile.find("/") != -1 or outfile.find('\\') != -1:
                print "Enter only a file name, not a complete file path."
                continue
            while True:
                rowlimit = raw_input("\nHow many rows do you want maximum for each file?\nNOTE: the header is counted as a row for this purpose.")
                #try:
                rowlimit = int(rowlimit)
                if rowlimit == "quit":
                    print "Enter it twice more."
                    break
                elif rowlimit < 2:
                    print "It's gotta be greater than one, buddy."
                    continue
                else:
#Everything before this is good(I'm just using it to figure out which file to split to where, and it gives me the variables I need), everything after needs some work
                    rowspot = 0 #I need this to count when my split is full
                    rowtotal = 0
                    split = 0 #Do I need this?
                    Headrow = [] #Pass the headrow to this one. DONE
                    with open(inpath, "rb") as inspot: #This With statement and contained forloop is just for counting the number of rows
                        myreader = csv.reader(inspot)
                        started = False
                        for row in myreader:
                            if rowtotal == 0: Headrow = row
                            rowtotal += 1
                    with open(inpath, "rb") as inspot:
                        myreader = csv.reader(inspot)
                        splittotal = (rowtotal-1)/(rowlimit-1)
                        for i in range(splittotal):
                            basepath = outpath[0:len(outpath)-4]+str(i)+outpath[len(outpath)-4:] #This should insert the split number in each of the resulting files.
                            with open(basepath, "wb") as outspot:
                                nowlist = [] #I should be able to pass the nowlist, once it's finished, to the splitfiles list. So fill this with rows UNNEEDED?
                                mywriter = csv.writer(outspot)
                                if i != 0:
                                    mywriter.writerow(Headrow)
                                    rowspot += 1
                                    print "Printing header to split {}: {}".format(i, Headrow)
                                #ran = False
                                end = False
                                for row in myreader:
                                    if (rowspot+1) % rowlimit == 0: # and ran:
                                        end = True
                                    print "Printing row to split {}: {}".format(i, row)
                                    mywriter.writerow(row)
                                    rowspot += 1
                                    #ran = True
                                    if end: break
                                print "\nEND SECTION\n"
                #except:
                    #print "Gimme something valid."
                   # continue
                break
            break

    break
                            
                        #Stuff between the red is being worked on
                      #  '''myreader = csv.reader(myspot)
                      #  mywriter = csv.writer(copyspot)
                      #  hiscorelist = []
                      #  for row in myreader:
                      #      print "Input :", row
                      #      maxscore = 0
                      #      for score in row:
                      #          if score.isdigit() and int(score) > maxscore:
                      #              maxscore = int(score)
                      #      row = [row[0], maxscore]
                      #      print "Processing: ", row
                      #      row.reverse()
                      #      hiscorelist.append(row)
                      #  hiscorelist.sort()
                      ##  hiscorelist.reverse()
                       # for score in hiscorelist:
                       #     score.reverse()
                       # print "Printing: ", hiscorelist
                       # mywriter.writerows(hiscorelist)
                    #'''

