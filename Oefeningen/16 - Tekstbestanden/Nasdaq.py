def lees_aandeel(filex):
    files = str(filex)
    file = open(files, "r")
    x = file.read()
    x = x.split('\n')
    lijst = []
    for i in x:
        lijn = i.split(';')
        lijn[5] = lijn[5].replace(',', '')
        lijst += [lijn]
    file.close()
    return lijst

def selecteer_kolom(woord, filex):
    lijst = lees_aandeel(filex)
    index = lijst[0].index(woord)
    nieuwelijst = []
    for i in lijst[1:]:
        nieuwelijst += [float(i[index])]
    return nieuwelijst

print(lees_aandeel('Apple.txt'))