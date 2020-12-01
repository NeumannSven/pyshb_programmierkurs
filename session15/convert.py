
from pprint import pprint
from docx import Document

#doc = Document("session15/Tageshoroskope 2020/April 2020/01 Mi, 01.04.20.docx")

doc = Document("session15/Tageshoroskope 2020/Januar 2020/01 Mi. 01.01.20_.docx")
horolist = {"Widder": "", "Stier": "", "Zwilling": "", "Krebs": "", "Löwe": "", "Jungfrau": "", "Waage": "", "Skorpion": "", "Schütze": "", "Steinbock": "", "Wassermann": "", "Fische": ""}

start = False
text = ""

for paragraph in doc.paragraphs:
    weiter = False

    for tierkreiszeichen in horolist.keys():
        if paragraph.text.startswith(tierkreiszeichen) and start:
            start = False
            horolist[actualZodiac] = text
            text = ""
        
        if paragraph.text.startswith(tierkreiszeichen) and not start:
            actualZodiac = tierkreiszeichen
            start = True
            weiter = True
            break

    if weiter:
        continue

    if start:
        text += paragraph.text

horolist[actualZodiac]=text
pprint(horolist)
    