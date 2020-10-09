def hoogtemeters(lijst_h):
    hoogte_verschil = []
    for i in range(len(lijst_h)):
        if i < len(lijst_h) - 1:
            verschil = lijst_h[i + 1] - lijst_h[i]
            hoogte_verschil += [verschil]
    return hoogte_verschil

def dalen_en_stijgen(hoogteverschillen):
    negatief = 0
    positief = 0
    for i in hoogteverschillen:
        if i < 0:
            negatief += abs(i)
        elif i > 0:
            positief += abs(i)
    return negatief, positief

print(dalen_en_stijgen([-761, 286, -113, 649, -547]))