import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:\Users\New Owner\Documents\Python Learning\Practice"

inputfilename = os.path.join(path, "garbegeyPDF.pdf")
inputfile = PdfFileReader(file(inputfilename, "rb"))

outputPDF = PdfFileWriter()

inputpages = inputfile.getNumPages()

for pagenum in range(inputpages):
    page = inputfile.getPage(pagenum)
    page.rotateCounterClockwise(90*pagenum)
    outputPDF.addPage(page)

print "Rotating pages by {} degrees".format(inputpages*90)
print "Title:", inputfile.getDocumentInfo().creator

outputfilename = os.path.join(path, "Spinny.pdf")
outputfile = file(outputfilename, "wb")

outputPDF.write(outputfile)
outputfile.close()
