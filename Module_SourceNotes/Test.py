import pypdf

#I only created this so I can test how the pdf reader works

# def pdf_transcriptv2(self):
read_pdf = pypdf.PdfReader(r"C:\Users\basil\Downloads\The_other_side_of_slavery.pdf")

page = read_pdf.pages[3]

print(page.extract_text())

# for pages in read_pdf.pages:
#     print(pages.extract_text())