import PyPDF2 , os

pdf_directory = input('\n'"Enter absolute path to PDF folder: ").strip()
output_csv = "pdf-page-count.csv"
lst = os.listdir(pdf_directory)
lst.sort()

for filename in lst:
    if filename.endswith('.pdf'):
        file = (os.path.join(pdf_directory, filename))
        pdfFileObj = open(file,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages

        with open  (output_csv, "a") as f:
            print(filename, ",", num_pages, "pages", file=f)

print('\n'"Done! Your page count csv has been created.")
