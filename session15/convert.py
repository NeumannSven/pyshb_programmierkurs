import os
from pprint import pprint
from docx import Document

startpath = 'session15/Tageshoroskope 2020'
doclist = []
yearlist =[]

for i in os.walk(startpath):
    for d in i[2]:
        if  d.endswith(".docx"):
            n = i[0].replace('./', '') + '/' + d
            doclist.append(n)
            print(n)


for wordfile in doclist:
    horolist = {"Widder": "", "Stier": "", "Zwilling": "", "Krebs": "", "Löwe": "", "Jungfrau": "", "Waage": "", "Skorpion": "", "Schütze": "", "Steinbock": "", "Wassermann": "", "Fische": ""}
    doc = Document(wordfile)
    start = False
    text = ""
    

    for paragraph in doc.paragraphs:
        if paragraph.text.startswith("Tageshoroskop für"):
            datum = paragraph.text.replace("Tageshoroskop für", '').strip()
        weiter = False

        for tierkreiszeichen in horolist.keys():
            if paragraph.text.startswith(tierkreiszeichen) and start:
                start = False
                horolist[actualZodiac] = datum, text.strip()
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

    horolist[actualZodiac]=datum, text.strip()
    yearlist.append(horolist)

for tierkreiszeichen in horolist.keys():
    f = open(tierkreiszeichen + ".csv", "w")
    for day in yearlist:
        # print(day[tierkreiszeichen])
        # if len(day[tierkreiszeichen]) > 1:
        #     f.write(f"{{{day[tierkreiszeichen][0]}|{day[tierkreiszeichen][1]}}}\n")
        # else:
        #     f.write(f"{{{day[tierkreiszeichen][0]}| }}\n")
        # if len(day[tierkreiszeichen]) <= 1:
        #     print("-------\n")
        #     print(day[tierkreiszeichen])
        #     print("\n" + tierkreiszeichen + "\n-------\n")
        f.write(f"{day[tierkreiszeichen]}\n")
    f.close()
        