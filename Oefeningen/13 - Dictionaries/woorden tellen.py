def woord_frequentie(zin):
    dictionaire = {}
    woord = ''
    for a in range(len(zin)):
        if zin[a].lower() == '.' or zin[a].lower() == ' ':
            if woord in dictionaire:
                dictionaire[woord] += 1
            elif woord != '':
                dictionaire[woord] = 1
            woord = ''
        else:
            woord += str(zin[a].lower())
    return dictionaire

def woorden_per_frequentie(zin):
    dictionaire_wegwerp = woord_frequentie(zin)
    dictionaire = {}
    for key, value in dictionaire_wegwerp.items():
        if value in dictionaire:
            dictionaire[value] += [key]
        else:
            dictionaire[value] = [key]

    return dictionaire

def meest_gebruikte_woorden(zin):
    dictionaire = woorden_per_frequentie(zin)
    vorige = 0
    for i in dictionaire.keys():
        getal = int(i)
        maximum = max(getal, vorige)
        vorige = maximum

    return dictionaire.get(maximum)
print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))