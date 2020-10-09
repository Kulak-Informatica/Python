# invoer
a = float(input('Geef mij 1 van de 2 lengtes van de rechthoekszijdes: '))
b = float(input('Geef mij de andere lengte van de rechthoekszijde: '))

# formule
from math import sqrt

c = sqrt((pow(a,2)) + (pow(b,2)))

#uitvoer
print('In een rechthoekige driekhoek met rechthoekzijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'.format(a, b, c))