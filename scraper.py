from PyPDF2 import PdfReader

def createPDFReader():
    try:
        pdfPath = input("Enter the path of the Newsletter PDF file: ")
        reader = PdfReader(pdfPath)
    except FileNotFoundError:
        print("The file was not found; your path is most likely incorrect! Please try again.")
        createPDFReader()

createPDFReader()

