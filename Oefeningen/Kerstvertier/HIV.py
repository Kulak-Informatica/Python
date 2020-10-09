eiwit = input('')
m = int(input())
n = int(input())

getalreeks = '0123456789'
variabel = 0
bijhouden_afwijkingen = 0
while variabel != n:
    invoer = input('')
    getal = ''
    afwijkingsletters = ''
    for i in range(len(invoer)):
        if invoer[i] in getalreeks:
            getal += str(invoer[i])
        else:
            afwijkingsletters += str(invoer[i])

    getal = int(getal)
    if eiwit[getal - 1] in afwijkingsletters:
        bijhouden_afwijkingen += 1

    variabel += 1

if bijhouden_afwijkingen >= m:
    print('positief ({})'.format(bijhouden_afwijkingen))

else:
    print('negatief ({})'.format(bijhouden_afwijkingen))