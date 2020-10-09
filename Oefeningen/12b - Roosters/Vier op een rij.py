def printbaar_rek(rek):
    lijst = ''
    lengte = len(rek) - 1
    for a in range(lengte, -1, -1):
        for b in range(len(rek[a])):
            lijst += str(rek[a][b])

        if a != 0:
            lijst += '\n'

    return lijst

def speel(kleur, plaats, bestaand_rek):
    for i in range(len(bestaand_rek)):
        if 'O' == bestaand_rek[i][plaats]:
            bestaand_rek[i][plaats] = str(kleur)
            break

    return bestaand_rek

print(speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))