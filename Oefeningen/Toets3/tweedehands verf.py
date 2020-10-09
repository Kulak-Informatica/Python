def kleur_toevoegen(lijst, kleur):
    if kleur == 'rood':
        lijst[0] += 1

    elif kleur == 'groen':
        lijst[1] += 1

    else:
        lijst[2] += 1

    return lijst

def is_wit(lijst):
    if (lijst[0] == lijst[1]) and (lijst[1] == lijst[2]):
        return True
    else:
        return False

def verf_verzamelen(lijst):
    lijst_k = [0, 0, 0]
    a = 0
    for i in lijst:
        lijst_k = kleur_toevoegen(lijst_k, str(i))
        variabel = is_wit(lijst_k)
        a += 1
        if variabel == True:
            return a, lijst_k


print(verf_verzamelen(['rood', 'groen', 'rood', 'rood', 'rood', 'rood', 'rood', 'rood', 'rood', 'blauw', 'blauw', 'rood', 'rood', 'groen', 'groen', 'blauw', 'blauw', 'groen', 'groen']))