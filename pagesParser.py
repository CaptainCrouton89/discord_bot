import requests, PyPDF2

def get_text(pdf, page_num, encrypted=False):
    if pdf.isEncrypted:
        pdf.decrypt("")
    return pdf.getPage(page_num).extractText()

# url = 'http://www.asx.com.au/asxpdf/20171103/pdf/43nyyw9r820c6r.pdf'
# response = requests.get(url)
# my_raw_data = response.content

# with open("my_pdf.pdf", 'wb') as my_data:
#     my_data.write(my_raw_data)

open_pdf_file = open("Heart Rush.pdf", 'rb')
pdf = PyPDF2.PdfFileReader(open_pdf_file)
print(get_text(pdf, 2))