#Variabelen
Q_1 = 2.0 * (10 ** (-6))
Q_2 = 1.0 * (10 ** (-6))
k = 8.99 * 10 ** 9
straal = float(input('Geef mij alstublieft de lengte van de straal in cm: '))

#Formule
Fc = (k*10**4) * ((Q_1*Q_2)/(straal** 2))

#uitvoer
print(Fc)