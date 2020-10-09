def behoort_tot_taal(zin, set):
    boodschap = False
    lengte = 0
    for letter in zin:
        if letter == ' ' or letter in set:
            lengte += 1

    if len(zin) == lengte:
        boodschap = True

    return boodschap


def is_onleesbaar(zin, set):
    boodschap = False
    woord = ''
    for letter in zin:
        if letter == ' ' or letter not in set:
            woord += str(letter)

    if woord == zin:
        boodschap = True

    return boodschap


def perfect_woord(zin, set):
    lijst = []
    for letter in zin:
        if letter == ' ' or (letter not in lijst and letter in set):
            lijst.append(letter)
        else:
            return False
    return True




print(behoort_tot_taal('do well', {'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(behoort_tot_taal('ambigu', {'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(is_onleesbaar('do well', {'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(is_onleesbaar('ambigu', {'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(perfect_woord('do well', {'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(perfect_woord('ambigu', {'o', 'd', 'e', 'l', 'w', 'r', 'h'}))