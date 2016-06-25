import os

mypath="C:\Users\New Owner\Documents\Practice"

for folder, subfolders, files in os.walk(mypath):
    for item in files:
        if item.lower().endswith(".jpg"):
            size = os.path.getsize(os.path.join(folder, item))
            if size < 2000:
                print "Deleting: {}\nReason: {} bytes\n".format(item, size)
                os.remove(os.path.join(folder, item))
