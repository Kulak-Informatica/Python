def hint(probeersel, te_zoeken):
    uitvoer = ''
    for i in range(len(probeersel)):
        if probeersel[i] == te_zoeken[i]:
            upper = probeersel[i].upper()
            uitvoer += upper
        elif probeersel[i] in te_zoeken:
            uitvoer += probeersel[i]
        else:
            uitvoer += '.'
    return uitvoer

print(hint('spoed', 'depri'))