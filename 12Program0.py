import socket
website = raw_input("Which website would you like to look up?")
website = website.rstrip()
webbits = website.split("/")
webdomain = webbits[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((webdomain, 80))
print webbits[2]
mysock.send('GET ' + website + ' HTTP/1.0\n\n')
alldata = 0
linecount = 0
printed = False
while True:
    data = mysock.recv(512)
    alldata += len(data)
    linecount += data.count("\n")
    if (len(data) < 1):
        break
    if printed == False:
        print data[data.find("<HTML>"):]
        printed = True
        continue
    if alldata < 3000:
        print data
print alldata, "CHARACTERS TOTAL IN DOCUMENT."
mysock.close()
