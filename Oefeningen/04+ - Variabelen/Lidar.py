#invoer
t_n = float(input('Geef mij de tijd weer in nanoseconden: '))

#constanten
t = t_n * (10 ** -9)
c = 299792458
n = 1.000277

#formule voor de afstand te bepalen
d = (c * t) / (2 * n)

#uitvoer
print(str(d) + ' meter')