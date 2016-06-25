import re
fhand = open("test.txt")
datlist = []
for line in fhand:
    line = line.rstrip()
    if re.search("^New Revision: ([0-9]+)", line):
        x = re.findall("^New Revision: ([0-9]+)", line)
        x = float(x[0])
        print "Value:", x
        datlist.append(x)
datav = sum(datlist)/len(datlist)
print "==============\nAVERAGE:", datav
end = raw_input("Press enter when done.")
