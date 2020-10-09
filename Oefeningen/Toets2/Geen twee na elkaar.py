def ontdubbelen(woord):
    woord_2 = ''
    te_bekijken = ''
    for i in range(len(woord)):
        if woord[i] != woord[i - 1] or i == 0:
            woord_2 += woord[i]
    return woord_2
print(ontdubbelen('stress'))