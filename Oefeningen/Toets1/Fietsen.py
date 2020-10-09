snelheid_stijn = int(input(''))
snelheid_kaat = int(input(''))
afstand = int(input(''))
seconden = 0

while afstand > 0:
    seconden += 1
    afstand -= snelheid_kaat
    afstand -= snelheid_stijn

print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(seconden))