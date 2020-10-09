def positie_laagste_ascii(tekst):
    minimum = tekst[0]
    for a in range(len(tekst)):
        minimum = min(minimum, tekst[a])
        uitvoer_1 = tekst.find(minimum)
    return uitvoer_1


def sorteer(tekst):
    list = []
    for b in tekst:
        list += b

    list_2 = sorted(list)
    uitvoer_2 = ''

    for c in list_2:
        uitvoer_2 += c
    return uitvoer_2


def is_alfabetisch(tekst):
    check_1 = sorteer(tekst)

    if tekst == check_1:
        return True
    else:
        return  False


print(is_alfabetisch('Beknopt'))