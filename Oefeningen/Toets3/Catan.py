ruilmarkt = {'goud': {'wol', 'steen', 'erts'}, 'wol': {'hout', 'steen', 'erts'}, 'erts': {'hout', 'steen'}, 'steen': {'hout', 'graan'}}

def wisselen_mogelijk(ruilmarkt, grondstof, verzameldegrondstoffen):
    lengte = len(ruilmarkt[grondstof])
    for i in ruilmarkt[grondstof]:
        if i in verzameldegrondstoffen:
            lengte -= 1
    if lengte == 0:
        return True
    else:
        return False

def bereken_ruilmiddelen(ruilmarkt, lijst):
    lijstdict = {}
    for i in lijst:
        for b in ruilmarkt[i]:
            if b in lijstdict:
                lijstdict[b] += 1
            else:
                lijstdict[b] = 1

    return lijstdict


def wisselen(ruilmarkt, grondstof, bezit):
    if wisselen_mogelijk(ruilmarkt, grondstof, bezit) == True:
        hoeveelheid = bereken_ruilmiddelen(ruilmarkt, [grondstof])

        for key, value in hoeveelheid.items():
            for i in range(value):
                index = bezit.index(key)
                bezit.pop(index)
        bezit += [grondstof]

    return bezit
