# invoer
aantal_getallen = int(input('aantal getallen: '))
som = 0
maximum = 0

for i in range(aantal_getallen):
    random_getal = int(input('getal: '))
    if i == 0:
        maximum = random_getal
    elif random_getal > maximum:
        maximum = random_getal
    som += random_getal

gemiddelde = round((som/aantal_getallen), 2)
print('Het grootste getal is {:d} en het gemiddelde is {}'.format(maximum, gemiddelde))