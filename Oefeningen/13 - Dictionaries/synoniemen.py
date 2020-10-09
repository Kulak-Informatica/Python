def synoniemen(zin, synoniemen):
    zin_2 = zin.split(' ')
    nieuwe_zin = ''
    a = 0
    lengte = len(zin_2)
    for i in zin_2:
        if i in synoniemen:
            nieuwe_zin += str(synoniemen.get(i))
        else:
            nieuwe_zin += str(i)
        a += 1
        if a != len(zin_2):
            nieuwe_zin += ' '

    return nieuwe_zin

print(synoniemen('op school heb je best geen slechte manieren',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))