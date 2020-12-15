import os

startpath = 'session15/Tageshoroskope 2020'
os.chdir(startpath)
doclist = []

for i in os.walk('.'):
    for d in i[2]:
        if  d.endswith(".docx"):
            n = startpath +  i[0].replace('.', '') + '/' + d
            doclist.append(n)


print(doclist)