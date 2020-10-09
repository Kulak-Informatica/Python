temp1 = float(input(''))

if temp1 >= 25 and temp1 < 30:
    warme_dagen = 1
    tropische_dagen = 0
elif temp1 >= 30:
    warme_dagen = 1
    tropische_dagen = 1
else:
    warme_dagen = 0
    tropische_dagen = 0

variabel = temp1
aantal = 0

while variabel != 'stop':
    temp = input('')
    if temp != 'stop':
        temp = float(temp)
        if temp >= 25 and temp < 30:
            warme_dagen += 1
        elif temp >= 30:
            warme_dagen += 1
            tropische_dagen += 1
        if warme_dagen >= 5 and tropische_dagen >=3:
            aantal =+ 1
            warme_dagen = 0
            tropische_dagen = 0
        elif temp < 25:
            warme_dagen = 0
            tropische_dagen = 0
        variabel = temp
    else: variabel = 'stop'

if aantal > 0:
    print('heat wave')
else:
    print('no heat wave')