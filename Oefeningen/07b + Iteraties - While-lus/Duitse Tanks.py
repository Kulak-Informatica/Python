serienummer = int(input(''))
maximum = serienummer
aantal = 0

while serienummer >= 0:
    serienummer = int(input(''))
    maximum = max(maximum, serienummer)
    aantal += 1

formule = round((((aantal + 1) * maximum) / aantal) - 1)

print('Het aantal geproduceerde tanks wordt geschat op {}.'.format(formule))