def dubbels(list):
    list_2 = []
    for i in list:
        if list.count(i) > 1 and (i not in list_2):
            list_2 += [i]
    return list_2

print(dubbels([(-1, 0), 2, 3, 3, 2, 'jan', 'jan']))