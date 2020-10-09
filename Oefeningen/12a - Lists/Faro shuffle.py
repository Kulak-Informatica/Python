def nieuw_kaartspel(kleuren, lijst_w):
    te_tonen = []
    for i in kleuren:
        for a in lijst_w:
            te_tonen += [i + a]
    return te_tonen

def splits_kaartspel(kaartenlijst):
    deel_1 = []
    deel_2 = []
    if len(kaartenlijst) > 1:
        getal = int(len(kaartenlijst) / 2)
        deel_1.extend(kaartenlijst[0:getal])
        deel_2.extend(kaartenlijst[getal:])

    else:
        deel_2.extend(kaartenlijst)

    return deel_1, deel_2

def faro_shuffle(kaartenlijst_1, kaartenlijst_2):
    i = 0
    nieuwe_lijst = []
    while i < len(kaartenlijst_2):
        if len(kaartenlijst_1) == len(kaartenlijst_2):
            nieuwe_lijst += [kaartenlijst_1[i]]
            nieuwe_lijst += [kaartenlijst_2[i]]

        elif len(kaartenlijst_1) != len(kaartenlijst_2) and i < len(kaartenlijst_1):
            nieuwe_lijst += [kaartenlijst_1[i]]
            nieuwe_lijst += [kaartenlijst_2[i]]

        i += 1

    if len(kaartenlijst_1) != len(kaartenlijst_2):
        nieuwe_lijst += [kaartenlijst_2[i - 1]]
    return nieuwe_lijst

print(faro_shuffle(['blad 1', 'blad 2', 'blad 3', 'steen 1'],['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']))