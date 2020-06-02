import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()
