tweet = input('')
uitvoer = ''
variabel = False
for i in range(len(tweet)):
    if tweet[i] == '#':
        variabel = True

    while variabel == True:
        for a in range(i + 1, len(tweet)):
            uitvoer += tweet[a]
            if tweet[a] == ' ':
                variabel = False
                break
uitvoer = uitvoer.strip().replace(' ', '\n')

print(uitvoer)