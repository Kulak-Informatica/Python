straal = float(input('Geef mij de straal: '))

pi = 3.14159

Oppervlakte_cirkel = pi * straal * straal

uitvoer = 'De oppervlakte van een cirkel met straal '
uitvoer += str(straal)
uitvoer += ' is '
uitvoer += str(Oppervlakte_cirkel)

print(uitvoer)