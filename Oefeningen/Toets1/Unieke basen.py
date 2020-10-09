aantal = int(input(''))
eerste_base = input('')
opslaan = str(eerste_base + ' ')

for i in range(aantal - 1):
    base_2 = input('')
    if eerste_base != base_2 and (base_2 not in opslaan):
        opslaan += base_2 + ' '

lengte = int(len(opslaan) / 2)

if lengte == 1:
    print('De DNA-keting bevat 1 soort base: {}'. format(opslaan))
else:
    print('De DNA-keting bevat {} verschillende soorten basen: {}'.format(lengte, opslaan))