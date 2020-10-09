import math
def binnen_of_buiten(middelpuntco, puntcirkel, tezoeken):
    afstand_1 = math.sqrt(((middelpuntco[0] - puntcirkel[0]) ** 2) + ((middelpuntco[1] - puntcirkel[1]) ** 2))
    afstand_2 = math.sqrt(((middelpuntco[0] - tezoeken[0]) ** 2) + ((middelpuntco[1] - tezoeken[1]) ** 2))

    if afstand_1 > afstand_2:
        boodschap = 'binnen'
    elif afstand_2 > afstand_1:
        boodschap = 'buiten'
    else:
        boodschap = 'op'
    afstand_2 = round(afstand_2, 4)

    return boodschap, afstand_2
print()