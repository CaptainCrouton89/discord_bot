import requests, PyPDF2
import fitz

def get_text(pdf, page_num, encrypted=False):
    if pdf.isEncrypted:
        pdf.decrypt("")
    return pdf.getPage(page_num).extractText()

# url = 'http://www.asx.com.au/asxpdf/20171103/pdf/43nyyw9r820c6r.pdf'
# response = requests.get(url)
# my_raw_data = response.content

# with open("my_pdf.pdf", 'wb') as my_data:
#     my_data.write(my_raw_data)

doc = fitz.open("Heart Rush.pdf")
toc = doc.get_toc()
all_sections = {}
for section in toc:
    # all_sections[section[1]] = doc[section[2]].get_text().replace("\n", "")[:-1]
    all_sections[section[1]] = doc[section[2]].get_text(sort=True)

for section, text in all_sections.items():
    with open(f"rules/{section}.txt", "w+") as f:
        f.write(text)

# print(doc[2].get_text())
# print(doc[2].get_text("blocks"))