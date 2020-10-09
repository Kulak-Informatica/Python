#variabelen
b = float(input('Geef mij de breedte in meter: '))
l = float(input('Geef mij de hoogte in meter: '))
c = float(input('Geef mij de hoeveel kubieke meter graan per hectare: '))
r = float(input('Geef mij de straal van de silo: '))
h = float(input('Geef mij de hoogte van de silo: '))

#pi
pi = 3.1415926535897931

#breuk
T = (b * l * c)
N = (pi * r * r * h) * 10000

#aantal silo's
aantal_silos = int((T / N) + 0.99999999999999)
#Hoogte laatste silo
hoogte_silo = (T / (pi * r * r * 10000)) % h

#uitvoer
print(str(aantal_silos))
print(str(hoogte_silo))