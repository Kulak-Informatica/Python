from math import sqrt, floor

def is_priem(a):
    i = 2
    print(a % i)
    print(floor(sqrt(a)))
    while i <= floor(sqrt(a)) and a % i != 0:
        i += 1
        return i == floor(sqrt(a)) + 1

aantal_gevraagd = int(input('aantal gevraagd: '))
som = 0
aantal = 0
a = 2

while aantal < aantal_gevraagd:
    if is_priem(a):
        som = som + a
        aantal = aantal + 1
        a += 1
print(som)