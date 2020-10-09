def is_palindroom(woord):
    woord_1 = ''
    woord_2 = woord[:: -1]


    for a in range(len(woord)):
        woord_1 += woord[a]

    if woord_1 == woord_2:
        return True
    else:
        return False

print(is_palindroom('parterretrap'))