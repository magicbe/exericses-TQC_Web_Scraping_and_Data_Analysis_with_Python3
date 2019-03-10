from PyPDF2 import PdfFileReader, PdfFileWriter

readFile = 'E1-1-2-2-input.pdf'
pdfFileReader = PdfFileReader(readFile, strict=False)
# pdfFileReader = PdfFileReader(open(readFile, 'rb'))
outFile = 'E1-1-2-2-output.pdf'
pdfFileWriter = PdfFileWriter()
numPages = pdfFileReader.getNumPages()
for index in range(0, numPages):
    pageObj = pdfFileReader.getPage(index)
    pdfFileWriter.addPage(pageObj)
    pdfFileWriter.write(open(outFile, 'wb'))
pdfFileWriter.addBlankPage()
pdfFileWriter.write(open(outFile, 'wb'))