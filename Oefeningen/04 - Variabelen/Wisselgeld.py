#Variabelen
a = 100
b = 50
c = 20
d = 10
e = 5
f = 2
g = 1
bedrag = float(input('Welk bedrag wil je in een hoeveelheid Eurostukken verdelen: '))

#Formules
rest1 = bedrag % a
rest2 = rest1 % b
rest3 = rest2 % c
rest4 = rest3 % d
rest5 = rest4 % e
rest6 = rest5 % f
uitkomst1 = (bedrag // a)
uitkomst2 = rest1 // b
uitkomst3 = rest2 // c
uitkomst4 = rest3 // d
uitkomst5 = rest4 // e
uitkomst6 = rest5 // f
uitkomst7 = rest6 // g


#Uitvoer
print(str(int(bedrag)) + ' cent kan je omwisselen in ' + str(int(uitkomst1 + uitkomst2 + uitkomst3 + uitkomst4 + uitkomst5 + uitkomst6 + uitkomst7)) + ' muntstukken')