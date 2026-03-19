import pdfplumber
from docx import Document




#I only created this so I can test how the pdf reader works

#file:///

url = r"https://learn.madisoncollege.edu/d2l/le/dropbox/77056/202659/DownloadAttachment?fid=6718639"



file_path = r"C:\Users\basil\Downloads\Chris Peterson_CompSci2_Fall 25.pdf"
word_doc = r"C:\Users\basil\Downloads\Botany of Baking Updated Sp 26.docx"

def pdf_transcript_v2(user_input):
    all_pages = []

    if "file:///" in user_input:
        user_input = user_input.replace("file:///", "")
    
    file_name = user_input.rsplit('\\')[-1].rsplit('.')[0]

    
    with pdfplumber.open(user_input) as docx:
         for page in docx.pages:
            formatted = f"\n\n-- Page: {page.page_number} --\n"
            all_pages.append(formatted)
            all_pages.append(page.extract_text())
            

         full_text = "\n".join(all_pages)
         print(full_text)

pdf_transcript_v2(file_path)
         


def word_docx_transcript(user_input):
    document = Document(user_input)
    all_pages = []

    file_name = user_input.rsplit("\\")[-1].rsplit(".")[0]

    for paragraph in document.paragraphs:
        print(paragraph.text)
        all_pages.append(paragraph.text)
        
    
    for table in document.tables:
        for row in table.rows:
            row_text = ' | '.join(cell.text.strip() for cell in row.cells)
            if row_text.strip():
                all_pages.append(row_text)
    
    full_text = "\n".join(all_pages)















