punten_thuisploeg = int(input(''))
punten_uitploeg = int(input(''))
verschil_punten = abs(punten_thuisploeg - punten_uitploeg)
rankingpunten_thuisploeg = -70
rankingpunten_uitploeg = 70

if punten_uitploeg < punten_thuisploeg:
    winnaar = rankingpunten_thuisploeg
    verliezer = rankingpunten_uitploeg
else:
    winnaar = rankingpunten_uitploeg
    verliezer = rankingpunten_thuisploeg

if verschil_punten < 10:
    winnaar += 600
    verliezer += 400
elif verschil_punten >=10 and verschil_punten < 20:
    winnaar += 700
    verliezer += 300
else:
    winnaar += 800
    verliezer += 200

if punten_uitploeg < punten_thuisploeg:
    print('thuisploeg: {:.2f}'.format(winnaar))
    print('  uitploeg: {:.2f}'.format(verliezer))
else:
    print('thuisploeg: {:.2f}'.format(verliezer))
    print('  uitploeg: {:.2f}'.format(winnaar))