# invoer
r = float(input())
v = float(input())

# constante
µ = 398600.4418 * (10 ** 9)

# teller van formule afstand
t_a = µ * r

# noemer van formule afstand
n_a = (2 * µ) - (r * (v ** 2))

# formule a
a = t_a / n_a

# formule periode
from math import sqrt, pi
p = (2 * pi) * (sqrt((a ** 3) / µ))

# formule omwenteling van de as
p_d = int(p / 86400)
p_u = int(((p / 86400) - p_d) * 24)
p_m = int(((((p / 86400) - p_d) * 24) - p_u) * 60)

# uitvoer
print('grote as: {} meter'.format(a))
print('periode: {} seconden'.format(p))
print('periode: {} dagen, {} uren en {} minuten'.format(p_d, p_u, p_m))
