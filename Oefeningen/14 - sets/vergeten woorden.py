def vergeten_woorden(zin, set):
    zin = zin.split(' ')
    aantal_verplichte_woorden = len(set)

    aantal_gebruikte_woorden = 0
    lijst = []
    for woord in zin:
        if woord in set and woord not in lijst:
            lijst += [woord]
            aantal_gebruikte_woorden += 1


    aantal_vergeten_woorden = 0
    lijst = []
    for woord in set:
        if woord not in zin and woord not in lijst:
            lijst.append(woord)
            aantal_vergeten_woorden += 1


    return aantal_verplichte_woorden, aantal_vergeten_woorden, aantal_gebruikte_woorden


print(vergeten_woorden('',{'python', 'world', 'hello', 'java'}))
print(vergeten_woorden('hello world world world',{'python', 'world', 'hello', 'java'}))