def fruitstuk_toevoegen(fruitmand, fruit):
    for i in fruitmand:
        if (len(i) != len(fruit)) and (fruit not in fruitmand):
            fruitmand += [fruit]
        elif len(i) == len(fruit) and (fruit not in fruitmand):
            plaats = fruitmand.index(i)
            fruitmand[plaats] = fruit
    fruitmand.sort(key = len)
    return fruitmand

def maak_fruitmand(lijst_fruit):
    fruitmand = [lijst_fruit[0]]
    for a in lijst_fruit[1:]:
        fruitmand = fruitstuk_toevoegen(fruitmand, a)
    return fruitmand


print(maak_fruitmand(['bes', 'appel', 'framboos']))