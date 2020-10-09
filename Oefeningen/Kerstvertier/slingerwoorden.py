def graad(woord):
    woord_1 = ''
    woord_2 = ''
    a = -1
    graad = 0

    for i in range(len(woord)):
        woord_1 += woord[i]
        woord_2 = woord[a] + woord_2
        a -= 1

        if woord_1 == woord_2 and woord_1 != woord:
            graad = len(woord_1)

    return graad


def slinger(woord, aantal):
    graad_2 = graad(woord)
    woord_3 = ''

    if aantal == 0:
        return ''

    elif graad_2 == 0:
        output = woord * aantal
        return output

    else:
        for b in range(0, graad_2):
            woord_3 += woord[b]
        lengte = len(woord) - graad_2
        output = (woord[:lengte] * (aantal - 1)) + woord
        return output

print(slinger('alfalfa', 3))