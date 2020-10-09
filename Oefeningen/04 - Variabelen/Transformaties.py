#variabelen
a = float(input('Geef mij de waarde van a: '))
b = float(input('Geef mij de waarde van b: '))
c = 3
d = 4
fx = 'f(x) = 2(x - 3)^2 + 4'
gx = 'g(x) = 2(x - ' + str(int(c+a)) + ')^2 + ' + str(int(d+b))

#uitvoer
print(fx)
print(gx)