n = int(input(''))

# is modulo 0 bij het delen van n door alle getallen van 2 tot getal zelf
# zolang de modulo verschillend van 0 is, zijn we goed bezig.
i = 2
while (n // i != n/i) and i < (n // 2) + 1:
    i += 1

if i == (n // 2 + 1):
    print(str(n) + ' is een priemgetal')
else:
    print(str(n) + ' is geen priemgetal')