import math

x = float(input(''))

if x == 2:
    print('{:.2f} is nulpunt van f'.format(x))
elif x > 2:
    functiewaarde = math.sqrt(x - 2)
    print('f({:.2f}) = {:.2f}'.format(x,functiewaarde))
else:
    print('{:.2f} ∉ dom(f)'.format(x))