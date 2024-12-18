import pdfplumber

def createPDF():
    try:
        pdfPath = input("Enter the path of the Newsletter PDF file: ")
        pdf = pdfplumber.open(pdfPath)
        return pdf
    except FileNotFoundError or TypeError:
        print("The file was not found; your path is most likely incorrect! Please try again.")
        createPDF()

pdf = createPDF()

print("\n")
print("-----------------------------")
print("\n")

for page in pdf.pages:
    text = page
    clean_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
    print(clean_text.extract_text())

print("\n")
print("-----------------------------")
print("\n")



