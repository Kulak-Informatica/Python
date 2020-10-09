def gift_inschrijven(klas, dictionaire):
    if klas[0] in dictionaire:
        dictionaire[str(klas[0])] += klas[1]
    else:
        dictionaire[str(klas[0])] = klas[1]
    return dictionaire

print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))