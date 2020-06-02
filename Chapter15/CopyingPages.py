import PyPDF2

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# Create a new PdfFileWriter object, which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

# Get the Page object by calling getPage() on a PdfFileReader object
# Then pass that Page object to your PdfFileWriter’s addPage() method
# We do this for pdf1File then pdf2File
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# When you’re done copying pages, write a new PDF called combinedminutes.pdf by
# passing a File object to the PdfFileWriter’s write() method
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
