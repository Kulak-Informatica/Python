def doe_maar_gewoon(woord):
    woord_2 = ''

    for i in range(len(woord)):
        if i < (len(woord) - 1):
            if woord[i + 1] == woord[i].lower():
                woord_2 += woord[i].lower()
            else:
                woord_2 += woord[i]
        else:
            woord_2 += woord[i]
    return woord_2

print(doe_maar_gewoon('stresSsymptOom'))