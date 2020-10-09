def splits(getal):
    cijfer_1 = int(str(getal)[0])
    cijfer_2 = int(str(getal)[1])
    cijfer_3 = int(str(getal)[2])
    cijfer_4 = int(str(getal)[3])

    return cijfer_1, cijfer_2, cijfer_3, cijfer_4


def oplopende_cijfers(cijfer_1, cijfer_2, cijfer_3, cijfer_4):
    s_1 = min(cijfer_1, cijfer_2, cijfer_3, cijfer_4)
    s_4 = max(cijfer_1, cijfer_2, cijfer_3, cijfer_4)
    k_1 = max(min(cijfer_1, cijfer_2), min(cijfer_1, cijfer_3), min(cijfer_2, cijfer_3))
    k_2 = cijfer_1 + cijfer_2 + cijfer_3 + cijfer_4 - s_1 - s_4 - k_1
    s_2 = min(k_1, k_2)
    s_3 = max(k_1, k_2)

    return s_1, s_2, s_3, s_4


def op_af_getallen(s1, s2, s3, s4):
    op = str(s1) + str(s2) + str(s3) + str(s4)
    af = op[::-1]

    return op, af


def verschil(getal1, getal2):
    verschil = str(int(getal1) - int(getal2))

    return verschil


def kaprekar(getal):
    bewerkingen = ''
    while getal != 6174:
        a, b, c, d = splits(getal)
        w, x, y, z = oplopende_cijfers(a, b, c, d)
        op, af = op_af_getallen(w, x, y, z)
        getal = int(verschil(af, op))
        bewerkingen += af + ' - ' +  op + ' = ' +  str(getal) + '\n'

    return bewerkingen[:-1]


print(kaprekar(5342))