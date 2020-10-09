# invoer
a = float(input('Geef mij de waarde van a: '))
b = float(input('Geef mij de waarde van b: '))

# constanten
e1 = pow(10,1)
e2 = pow(10,2)
e3 = pow(10,3)
e4 = pow(10,4)
a2 = a * e1
b2 = b * e1
a3 = a * e2
b3 = b * e2
a4 = a * e3
b4 = b * e3
a5 = a * e4
b5 = b * e4

# som
ab = a + b
ab2 = a2 + b2
ab3 = a3 + b3
ab4 = a4 + b4
ab5 = a5 + b5

# uitvoer
print('{:>6d}'.format(int(a)) + ' + ' + '{:<6d}'.format(int(b)) + ' = ' + str(int(ab)))
print('{:>6d}'.format(int(a2)) + ' + ' + '{:<6d}'.format(int(b2)) + ' = ' + str(int(ab2)))
print('{:>6d}'.format(int(a3)) + ' + ' + '{:<6d}'.format(int(b3)) + ' = ' + str(int(ab3)))
print('{:>6d}'.format(int(a4)) + ' + ' + '{:<6d}'.format(int(b4)) + ' = ' + str(int(ab4)))
print('{:>6d}'.format(int(a5)) + ' + ' + '{:<6d}'.format(int(b5)) + ' = ' + str(int(ab5)))