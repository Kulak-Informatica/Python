string = ''
lengte = 0
aantal = int(input(''))
for i in range(aantal):
    inputx = str(input(''))
    if i == 0:
        lengte = len(inputx)
    string += inputx

zin = ''
getal1 = []
getal2 = []
for i in range(aantal):
    getal1 += [lengte * i]
    getal2 += [(lengte * i) + lengte - 1]
for i in range(1, lengte * aantal - 1):
    if i == lengte - 1 or i == (lengte * aantal) - lengte:
        pass
    else:
        symbolen = ''
        if i < lengte - 1:
            symbolen += string[i - 1]
            symbolen += string[i + 1]
            symbolen += string[i + lengte]
        elif i in getal1:
            symbolen += string[i + lengte]
            symbolen += string[i + 1]
            symbolen += string[i - lengte]
        elif i in getal2:
            symbolen += string[i + lengte]
            symbolen += string[i - 1]
            symbolen += string[i - lengte]
        elif i > (lengte * aantal) - lengte:
            symbolen += string[i - 1]
            symbolen += string[i + 1]
            symbolen += string[i - lengte]
        else:
            symbolen += string[i - 1]
            symbolen += string[i + 1]
            symbolen += string[i - lengte]
            symbolen += string[i + lengte]
            #print(string[i - 1], string[i], string[i + 1])
        for b in range(len(symbolen)):
            count = symbolen.count(symbolen[b])
            if count == 3:
                #print(symbolen, i / aantal, string[i])
                if (ord(symbolen[b]) >= 65 and ord(symbolen[b]) <= 90) or (ord(symbolen[b]) >= 97 and ord(symbolen[b]) <= 122):
                    zin += string[i].upper()
                elif ord(symbolen[b]) >= 48 and ord(symbolen[b]) <= 57:
                    zin += string[i].lower()
                else:
                    zin += string[i]
                break
print(zin)