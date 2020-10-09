# invoer
x = float(input('Geef mij een x-waarde: '))
y = float(input('Geef mij een y-waarde: '))

# formule
linkerlid = abs(abs(x) - abs(y))
rechterlid = abs(x - y)

# uitvoer
print(str(round(linkerlid, 4)) + ' \N{LESS-THAN OR EQUAL TO} ' + str(round(rechterlid, 4)))
