fhand = open('test.txt')
count = 0
dic = {}
for line in fhand:
    line = line.rstrip()
    lwords = line.split(" ")
    for lword in lwords:
        lword = lword.lower()
        if lword in dic:
            dic[lword] += 1
        else:
            dic[lword] = 1
print dic
            
            
        
        
