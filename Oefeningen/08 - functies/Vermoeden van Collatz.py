def volgend_collatz_getal(n):
    volgend_getal = n
    if (volgend_getal % 2 == 0):
        volgend_getal = volgend_getal / 2
    else:
        volgend_getal = (volgend_getal * 3) + 1
    return int(volgend_getal)

def collatz(n):
    aantal = 1
    while n > 1:
        n = volgend_collatz_getal(n)
        aantal += 1
    return aantal

print(collatz(12))