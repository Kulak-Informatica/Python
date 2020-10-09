harshadgetal = int(input(''))

# teller
teller = harshadgetal

# noemer
noemer = 0
digits = list(str(harshadgetal))
for a in digits:
    noemer += int(a)

# deling + if statement
if teller % noemer == 0:
    print('{} is een Harshadgetal'.format(harshadgetal))

else:
    print('{} is geen Harshadgetal'.format(harshadgetal))