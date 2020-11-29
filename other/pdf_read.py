#!/usr/bin/env python3

import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
#* 19

pageObj = pdfReader.getPage(0)
pageObj.extractText()

pdfFileObj.close()