kaart = int(input(''))
som = kaart

while kaart != 0 and som < 21:
    kaart = int(input(''))
    som += kaart

if som > 21:
    print('Verbrand ({})'.format(som))
if som == 21:
    print('Gewonnen!')
if som < 21:
    print('Voorzichtig gespeeld ({})'.format(som))