def splits(getal):
    getal = str(getal)
    variabel_1 = 1
    boodschap = ''
    n = 0
    while len(getal) > variabel_1:
        boodschap += getal[n]
        boodschap += ', '
        variabel_1 += 1
        n += 1
    boodschap += getal[n]
    return boodschap


def oplopende_cijfers(getal_1, getal_2, getal_3, getal_4):
    getal = str(getal_1) + str(getal_2) + str(getal_3) + str(getal_4)
    gesorteerd_getal = ''.join(sorted(str(getal)))
    boodschap = splits(gesorteerd_getal)
    return boodschap


def op_af_getallen(getal_1, getal_2, getal_3, getal_4):
    getal_oplopend = str(getal_1) + str(getal_2) + str(getal_3) + str(getal_4)
    getal_aflopend = ''.join(sorted(str(getal_oplopend), reverse=True))
    boodschap = '(\'{}\', \'{}\')'.format(getal_oplopend, getal_aflopend)
    return boodschap


def verschil(getal_1, getal_2):
    verschil = int(getal_1) - int(getal_2)
    return verschil


def kaprekar(getal):
    resultaat = 0
    while resultaat != 6174:
        getal_a = splits(getal)
        print(getal_a)
        getal_b = oplopende_cijfers(getal_a)
        print(getal_b)
        getal_c = op_af_getallen(getal_b)
        resultaat = verschil(getal_c)
        getal_1 = int(getal_c[0])
        getal_2 = int(getal_c[1])
        boodschap = ('{} - {} = {}'.format(getal_1, getal_2, resultaat))
        return boodschap

print(kaprekar(5342))