# input
aantal_gebouwen = int(input(''))

# hulpvariabelen
variabel = 0
vorige_hoogte = 0

# for-lus
for i in range(1,aantal_gebouwen + 1):
    naam = input('')
    hoogte = int(input(''))
    if i == 1:
        vorige_hoogte = hoogte
        hoogte_1 = hoogte
        print('{} is zichtbaar van het gelijkvloers tot {} meter.'.format(naam,hoogte))
    if hoogte > hoogte_1 and i == 2:
        print('{} is zichtbaar van {} meter tot {} meter.'.format(naam, hoogte_1 , hoogte))
        vorige_hoogte = hoogte
        maximum_hoogte = hoogte
    if hoogte > vorige_hoogte and i > 2:
        print('{} is zichtbaar van {} meter tot {} meter.'.format(naam, vorige_hoogte, hoogte))
        vorige_hoogte = hoogte