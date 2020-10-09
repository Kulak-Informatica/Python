def volgende_rij(lijst):
    te_tonen = []
    for i in range(len(lijst) - 1):
        kleuren = ['R', 'G', 'Y']
        if lijst[i] == lijst[i + 1]:
            te_tonen += [lijst[i]]

        else:
            kleuren.remove(lijst[i])
            kleuren.remove(lijst[i + 1])
            te_tonen += [kleuren[0]]

    return te_tonen

def driehoek(rij):
    variabel = rij
    lijst = [rij]
    for i in range(len(rij) - 1):
        variabel = volgende_rij(variabel)
        lijst += [variabel]

    return lijst

def kleuren(driehoek):
    rood, groen, geel = 0, 0, 0
    for i in range(len(driehoek)):
        for a in range(len(driehoek[i])):
            if driehoek[i][a] == 'R':
                rood += 1
            elif driehoek[i][a] == 'G':
                groen += 1
            else:
                geel += 1
    return groen, rood, geel

print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))