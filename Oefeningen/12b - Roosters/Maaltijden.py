def dagprijs(gewenst):
    middagmaal = 5.3
    soep = 1.7
    vieruurtje = 2.3
    rekening = 0

    for a in range(len(gewenst)):
        if gewenst[a] == 'middagmaal':
            rekening += middagmaal * int(gewenst[a + 1])

        elif gewenst[a] == 'soep':
            rekening += soep * int(gewenst[a + 1])

        elif gewenst[a] == 'vieruurtje':
            rekening += vieruurtje * int(gewenst[a + 1])

    return rekening

def weekprijs(gewenst_1):
    rekening_1 = 0
    for i in range(len(gewenst_1)):
        rekening_1 += dagprijs(gewenst_1[i])

    return rekening_1
print(weekprijs((('middagmaal', 2, 'soep', 2, 'vieruurtje', 2), ('middagmaal', 1, 'soep', 1), ('soep', 3, 'vieruurtje', 3), ('middagmaal', 3, 'soep', 1), ('middagmaal', 3, 'soep', 3, 'vieruurtje', 1))))