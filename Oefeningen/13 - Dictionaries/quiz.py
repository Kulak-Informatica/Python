def verlaat_ploeg(persoon, ploeg, lijst):
    lijst[ploeg].remove(persoon)
    if lijst[ploeg] == []:
        lijst.pop(ploeg)
    return lijst

def vervoegt_ploeg(persoon, ploeg, lijst):
    if ploeg not in lijst:
        lijst[ploeg] = [persoon]
    else:
        lijst[ploeg].append(persoon)
    return lijst