#Indien vader werd opgegeven, print je: Krokodil geeft kind terug.
#Indien krokodil werd opgegeven, print je: Krokodil eet kind op.
#In alle andere geval toon je: Moe van het denken.
# invoer
naam = input('Geef een naam: ')

# if en else
if naam == 'vader':
    boodschap = 'Krokodil geeft kind terug.'
elif naam == 'krokodil':
    boodschap = 'Krokodil eet kind op.'
else:
    boodschap = 'Moe van het denken.'

# uitvoer
print(boodschap)