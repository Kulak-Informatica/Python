def ik_heb_gemoord(lijst, moordenaar):
    if len(lijst) == 1:
        return moordenaar, lijst

    elif len(lijst) == 2:
        plaats_moordenaar = lijst.index(moordenaar)
        if plaats_moordenaar == 0:
            lijst.pop(1)
        else:
            lijst.pop(0)
        return moordenaar, lijst

    else:
        plaats_moordenaar = lijst.index(moordenaar)
        if plaats_moordenaar == (len(lijst) - 1):
            lijst.pop(0)
        else:
            lijst.pop((plaats_moordenaar + 1))

        plaats_2_moordenaar = lijst.index(moordenaar)
        if plaats_2_moordenaar == (len(lijst) - 1):
            te_vermoorden = lijst[0]
        else:
            te_vermoorden = lijst[(plaats_2_moordenaar + 1)]

        return te_vermoorden, lijst

def ik_ben_vermoord(lijst, vermoorde):
    if len(lijst) == 1:
        return vermoorde, lijst

    elif len(lijst) == 2:
        plaats_vermoorde = lijst.index(vermoorde)
        lijst.pop(plaats_vermoorde)
        return lijst[0], lijst

    else:
        plaats_vermoorde = lijst.index(vermoorde)
        if plaats_vermoorde == (len(lijst) - 1):
            volgende = lijst[0]
        else:
            volgende = lijst[plaats_vermoorde + 1]
        lijst.pop(plaats_vermoorde)

        return volgende, lijst