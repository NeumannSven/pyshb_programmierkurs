
from docx import Document
doc = Document("session15/test.docx")

for paragraph in doc.paragraphs:
    print(paragraph.text)

