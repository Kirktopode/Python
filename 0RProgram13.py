import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:\Users\New Owner\Documents\Python Learning\Practice"

inputfilename = os.path.join(path, "GarbegeyPDF.pdf")
inputfile = PdfFileReader(file(inputfilename, "rb"))

print "Number of pages:", inputfile.getNumPages()
print "Title:", inputfile.getDocumentInfo().creator

outputPDF = PdfFileWriter()

for page in range(inputfile.getNumPages()):
    if page%5 == 0:
        outputPDF.addPage(inputfile.getPage(page))

outputfilename = os.path.join(path, "GarbegeyPDF.pdf")
outputfile = file(outputfilename, "wb")
outputPDF.write(outputfile)
outputfile.close()
