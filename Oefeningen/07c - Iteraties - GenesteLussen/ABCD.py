# 9 want a mag niet 0 zijn
for a in range(9):
    for b in range(10):
        for c in range(10):
            # 9 want d mag niet 0 zijn
            for d in range(9):
                getal_1 = str(a) + str(b) + str(c) + str(d)
                getal_1 = int(getal_1)
                getal_2 = str(d) + str(c) + str(b) + str(a)
                getal_2 = int(getal_2)
                if getal_1 * 4 == getal_2 and (a != b and a != c and a != d and b != c and b != d and c != d):
                    print(getal_1)