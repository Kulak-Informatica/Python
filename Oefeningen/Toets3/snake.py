def beweeg(tuples, zet):
    lijst = list(tuples)
    if zet == '<':
        lijst[0] -= 1
    elif zet == '>':
        lijst[0] += 1
    elif zet == '^':
        lijst[1] += 1
    else:
        lijst[1] -= 1

    return tuple(lijst)


def teruggekeerd(lijst):
    if (lijst[0] == '^' and lijst[1] == 'v') or (lijst[0] == 'v' and lijst[1] == '^') or (lijst[0] == '<' and lijst[1] == '>') or (lijst[0] == '>' and lijst[1] == '<'):
        return True
    else:
        return False


def laatste_levende_positie(pijltjes):
    positie = (0, 0, 0)
    xy = positie[1:]
    i = 0

    variabel = False
    while variabel == False and i != len(pijltjes):
        xy = beweeg(xy, pijltjes[i])
        if i != len(pijltjes) - 1:
            variabel = teruggekeerd([pijltjes[i], pijltjes[i + 1]])
        i += 1

    return i, xy[0], xy[1]

print(laatste_levende_positie(['v', 'v', '<', '^', '>', 'v', '<', '<', '<', 'v', '^', '>', '<']))