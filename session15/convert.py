
from pprint import pprint
from docx import Document

doclist = ("session15/Tageshoroskope 2020/April 2020/01 Mi, 01.04.20.docx", "session15/Tageshoroskope 2020/Januar 2020/01 Mi. 01.01.20_.docx")
yearlist =[]

for wordfile in doclist:
    horolist = {"Widder": "", "Stier": "", "Zwilling": "", "Krebs": "", "Löwe": "", "Jungfrau": "", "Waage": "", "Skorpion": "", "Schütze": "", "Steinbock": "", "Wassermann": "", "Fische": ""}
    doc = Document(wordfile)
    start = False
    text = ""

    for paragraph in doc.paragraphs:
        weiter = False

        for tierkreiszeichen in horolist.keys():
            if paragraph.text.startswith(tierkreiszeichen) and start:
                start = False
                horolist[actualZodiac] = text.strip()
                text = ""
            
            if paragraph.text.startswith(tierkreiszeichen) and not start:
                actualZodiac = tierkreiszeichen
                start = True
                weiter = True
                break

        if weiter:
            continue

        if start:
            text += paragraph.text + " "
            text.replace("  ", " ")

    horolist[actualZodiac]=text.strip()
    yearlist.append(horolist)

for tierkreiszeichen in horolist.keys():
    f = open(tierkreiszeichen + ".csv", "w")
    for day in yearlist:
        f.write(f"Datum; {day[tierkreiszeichen]}\n")
    f.close()
        