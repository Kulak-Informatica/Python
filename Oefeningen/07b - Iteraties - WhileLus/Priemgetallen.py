priemgetal = int(input(''))

variabel = 0

if priemgetal > 1:
    while variabel == 0:
        for i in range(1,priemgetal):
            if priemgetal % i == 0:
                variabel += 1
    if variabel > 1:
        print('{} is geen priemgetal'.format(priemgetal))
    else:
        print('{} is een priemgetal'.format(priemgetal))
else:
    print('{} is geen priemgetal'.format(priemgetal))