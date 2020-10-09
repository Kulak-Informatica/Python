# invoer
orkaan = float(input('Geef me de snelheid: '))

# if en else

if orkaan >= 250:
    print('categorie 5')
elif orkaan >= 210 and orkaan <= 249:
    print('categorie 4')
elif orkaan >= 178 and orkaan <= 209:
    print('categorie 3')
elif orkaan >= 154 and orkaan <= 177:
    print('categorie 2')
elif orkaan >= 119 and orkaan <= 153:
    print('categorie 1')
else:
    print('geen orkaan')