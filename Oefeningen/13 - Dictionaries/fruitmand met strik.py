def fruitmand_maken(lijst_1):
    lijst = lijst_1[::-1]
    dictionaire = {}
    for i in lijst:
        if len(i) in dictionaire:
            if lijst.index(i) < lijst.index(dictionaire[len(i)]):
                dictionaire[len(i)] = i

        else:
            dictionaire[len(i)] = i

    return dictionaire

def fruitmand_inpakken(dict):
    dictionaire = dict
    lijst = []
    for value in dictionaire.values():
        lijst += [value]
    lijst.sort(key=len)
    return lijst

print(fruitmand_maken(['banaan', 'aardbei', 'kiwi', 'peer', 'appel', 'bes', 'sinaasappel', 'framboos']))