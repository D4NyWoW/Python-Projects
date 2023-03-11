import PyPDF2
import sys

with open('dummy.pdf', 'rb') as file: # convert file object to binary mode
    reader = PyPDF2.PdfReader(file) # so that can read the file binary module
    #print(len(reader.pages))
    page = reader.getPage(0)
    writer = PyPDF2.PdfFileWriter() # to write the object in memory
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

inputs = sys.argv[1:] # is going to grab all the arguments besides pdf.py, it's going to grab all into a list call inputs
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf) # this merger is going to have all these pdf
    merger.write('super.pdf')

pdf_combiner(inputs)