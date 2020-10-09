import random
random.seed(1)

n = random.randint(1, 100)
gok = random.randint(1, 100)

maximum = 100
minimum = 1
telling = 0

while n != gok:
    if gok < n:
        telling += 1
        print('[{},{}] --> computer gokt {}'.format(minimum, maximum, gok))
        minimum = gok + 1
        gok = random.randint(minimum,maximum)

    elif gok >= n:
        telling += 1
        print('[{},{}] --> computer gokt {}'.format(minimum, maximum, gok))
        maximum = gok - 1
        gok = random.randint(minimum, maximum)

if n == gok:
    telling += 1

    print('[{},{}] --> computer gokt {}'.format(minimum, maximum, gok))
    print('computer had {} pogingen nodig om het getal {} te raden.'.format(telling, n))