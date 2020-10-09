def versleutel_woord(woord, ascii_nummer):
    woord_2 = ''
    for i in range(len(woord)):
        ascii_letter = chr(ord(woord[i].upper()) + ascii_nummer)

        if ascii_letter == '@':
            ascii_letter = ' '
        elif ascii_letter == ' ':
            ascii_letter = '@'

        woord_2 += ascii_letter

    return woord_2

def versleutel_zin(zin, ascii_nummer):
    zin_2 = ''
    zin = zin.split(' ')
    for i in range(len(zin)):
        if i < len(zin) - 1 :
            zin_2 += versleutel_woord(zin[i], ascii_nummer)
            zin_2 += '@'
        else:
            zin_2 += versleutel_woord(zin[i], ascii_nummer)

    return zin_2