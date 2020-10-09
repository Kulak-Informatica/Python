# invoer
hendel = input('')
brug = input('')

# if en else
doden = 0
if hendel == 'ja' and brug == 'ja':
    doden = 2
elif hendel == 'nee' and brug == 'ja':
    doden = 1
elif hendel == 'ja' and brug == 'nee':
    doden = 1
else:
    doden = 5

# uitvoer
print(doden)