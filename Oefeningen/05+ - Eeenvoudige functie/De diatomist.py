# invoer
k_r = float(input())
g_r = float(input())

# formules
from math import pi

n = int((0.83 * (pow(g_r, 2) / pow(k_r, 2))) - 1.9)
opp_k = pi * pow(k_r, 2) * n
opp_g = pi * pow(g_r, 2)
percentage = (opp_k / opp_g) * 100

# uitvoer
print('{} kleine cirkels bedekken {:.2f}% van de grote cirkel'.format(n, percentage))
