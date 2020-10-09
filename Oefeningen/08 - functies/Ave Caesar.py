def is_letter(n):
    boodschap = False
    n = ord(n)
    if n <= ord('z') and n >= ord('A'):
        boodschap = True
    return boodschap


def roteer_letter(n, hoeveel):
    if is_letter(n) is True:
        geroteerde_n_number = ord(n) + (hoeveel)
        l = ord(n)
        if l >= ord('a') and l <= ord('z') and geroteerde_n_number > 122:
            geroteerde_n = (geroteerde_n_number - 123) + ord('a')
            geroteerde_n = chr(geroteerde_n)
        elif l >= ord('A') and l <= ord('Z') and geroteerde_n_number > 90:
            geroteerde_n = (geroteerde_n_number - 91) + ord('A')
            geroteerde_n = chr(geroteerde_n)
        else:
            geroteerde_n = chr(geroteerde_n_number)
    else:
        geroteerde_n = n
    return geroteerde_n


def versleutel(z, hoeveel):
    zin = ''
    for letter in z:
        if letter == ' ':
            zin += ' '
        elif letter == '.':
            zin += '.'
        elif letter == '?':
            zin += '?'
        elif letter == '!':
            zin += '!'
        else:
            zin += roteer_letter(letter, hoeveel)
    return zin


print(versleutel('w', 8))