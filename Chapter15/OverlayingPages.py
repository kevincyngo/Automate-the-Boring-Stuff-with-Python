import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')

# Make a PdfFileReader object of meetingminutes.pdf
pdfReader = PyPDF2.PdfFileReader(minutesFile)

# We call getPage(0) to get a Page object for the first page and store this object in minutesFirstPage
minutesFirstPage = pdfReader.getPage(0)

# We then make a PdfFileReader object for watermark.pdf
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

# Call mergePage() on minutesFirstPage
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

# Then we loop through the rest of the pages in meetingminutes.pdf and add them to the PdfFileWriter object
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
