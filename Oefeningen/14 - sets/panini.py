def verzamel(naam, set, dictionaire):
    dicti = dictionaire
    if naam not in set:
        set.add(naam)
        return set, dictionaire

    else:
        key = 0
        for value in dicti.values():
            key += 1
            if naam in value:
                print(dictionaire[key])

print(verzamel('Bosmans',{'Staelens', 'Bosmans', 'Weber', 'Scifo'},{2: {'Bosmans'}}))