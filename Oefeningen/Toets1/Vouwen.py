dikte_papier = int(input(''))
afstand = int(input(''))
som = 0

while dikte_papier < afstand:
    dikte_papier *= 2
    som += 1

print('Na {} keer vouwen bedraagt de dikte van het papier {} mm.'.format(som, dikte_papier))