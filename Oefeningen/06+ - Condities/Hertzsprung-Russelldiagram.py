# invoer
temperatuur = float(input())
lichtkracht = float(input())

# if en else
ster = ''
if lichtkracht > 10000:
    ster = 'superreuzen (a)'
elif lichtkracht > 1000:
    ster = 'superreuzen (b)'
elif lichtkracht > 100 and temperatuur < 7500:
    ster = 'heldere reuzen'
elif lichtkracht > 10 and temperatuur < 6000:
    ster = 'reuzen'
elif (lichtkracht > 0.0001 and lichtkracht < 0.01 and temperatuur > 5000) or (lichtkracht < 0.0001 and temperatuur > 3000):
    ster = 'witte dwergen'
else:
    ster = 'hoofdreeks'

# uitvoer
print(ster)