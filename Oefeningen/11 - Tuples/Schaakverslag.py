def geldige_zet(zet):
    list_1 = ['K', 'D', 'T', 'L', 'P']
    list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_3 = ['1', '2', '3', '4', '5', '6', '7', '8']
    boodschap = False

    if len(zet) == 2:
        if zet[0] in list_2 and zet[1] in list_3:
            boodschap = True

    elif len(zet) == 3:
        if zet[0] in list_1 and zet[1] in list_2 and zet[2] in list_3:
            boodschap = True

    return boodschap

def geldige_zetten(zetten):
    boodschap = True
    for i in range(len(zetten)):
        if geldige_zet(zetten[i]) == False:
            boodschap = False

    return boodschap

print(geldige_zetten(('f8', 'Dd3', 'Pa3', 'Pf3')))