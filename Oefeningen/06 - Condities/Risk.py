# invoer
a1 = int(input())
a2 = int(input())
a3 = int(input())
v1 = int(input())
v2 = int(input())

# som
a = a1 + a2 + a3

# if en else
aantal_legers_a = 0
aantal_legers_v = 0

if (max(a1, a2, a3) > max(v1, v2)):
    aantal_legers_v = aantal_legers_v + 1
if (max(a1, a2, a3) < max(v1, v2)):
    aantal_legers_a = aantal_legers_a + 1
if (max(a1, a2, a3) == max(v1, v2)):
    aantal_legers_a = aantal_legers_a + 1
if (a - min(a1, a2, a3) - max(a1, a2, a3)) > min(v1, v2):
    aantal_legers_v = aantal_legers_v + 1
if (a - min(a1, a2, a3) - max(a1, a2, a3)) < min(v1, v2):
    aantal_legers_a = aantal_legers_a + 1
if (a - min(a1, a2, a3) - max(a1, a2, a3) == min(v1, v2)):
    aantal_legers_a = aantal_legers_a + 1

# woordspelletje
if aantal_legers_a == 1:
    leger_a = 'leger'
else:
    leger_a = 'legers'
if aantal_legers_v == 1:
    leger_v = 'leger'
else:
    leger_v = 'legers'

# uitvoer
print('aanvaller verliest {} {}, verdediger verliest {} {}'.format(aantal_legers_a, leger_a, aantal_legers_v, leger_v))