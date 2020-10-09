# input
hoed_1 = input('')
hoed_2 = input('')
persoon = int(input())

# if en else
kleur_1 = ''
kleur_2 = ''
if hoed_1 == 'zwart' and hoed_2 == 'wit' and persoon == 2:
    kleur_1 = 'wit'
    kleur_2 = 'wit'
elif hoed_1 == 'zwart' and hoed_2 == 'wit' and persoon == 1:
    kleur_1 = 'zwart'
    kleur_2 = 'zwart'
elif hoed_1 == 'wit' and hoed_2 == 'wit' and persoon == 2:
    kleur_1 = 'wit'
    kleur_2 = 'zwart'
elif hoed_1 == 'wit' and hoed_2 == 'wit' and persoon == 1:
    kleur_1 = 'zwart'
    kleur_2 = 'wit'
elif hoed_1 == 'wit' and hoed_2 == 'zwart' and persoon == 2:
    kleur_1 = 'zwart'
    kleur_2 = 'zwart'
elif hoed_1 == 'wit' and hoed_2 == 'zwart' and persoon == 1:
    kleur_1 = 'wit'
    kleur_2 = 'wit'
elif hoed_1 == 'zwart' and hoed_2 == 'zwart' and persoon == 2:
    kleur_1 = 'zwart'
    kleur_2 = 'wit'
else:
    kleur_1 = 'wit'
    kleur_2 = 'zwart'

# uitvoer
print(kleur_1)
print(kleur_2)