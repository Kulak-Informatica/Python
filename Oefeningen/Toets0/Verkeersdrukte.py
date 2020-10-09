d = float(input(''))
v = float(input(''))
vrachtwagens = min((v * d) / 40, 1)
d = float(input(''))
v = float(input(''))
persoon_auto = min((v * d) / 40, 1)
verschil = (vrachtwagens - persoon_auto)

if min(persoon_auto, vrachtwagens) > 0.7:
    print('zwart')
elif max(persoon_auto, vrachtwagens) > 0.7 and abs(verschil) < 0.2:
    print('rood')
elif abs(verschil) > 0.7:
    print('geel')
else:
    print('groen')