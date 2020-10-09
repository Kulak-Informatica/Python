def bereken_prijs(boodschap):

    te_tonen_boodschap = ''
    prijs = ''
    variabel = False
    for i in range(len(boodschap)):
        if boodschap[i] == '<':
            variabel = True

        if variabel == True:
            prijs += boodschap[i]
        else:
            te_tonen_boodschap += boodschap[i]

    prijs = prijs.replace('<', '')
    prijs = prijs.replace('>', '')
    prijs = float(prijs) * int(len(te_tonen_boodschap))

    return te_tonen_boodschap, prijs

def toon_boodschappen(boodschappen):
    boodschappen = boodschappen.split('>')
    totale_prijs = 0
    te_tonen = ''
    for i in range(len(boodschappen) - 1):
        boodschap, prijs = bereken_prijs(boodschappen[i])
        totale_prijs = float(totale_prijs) + float(prijs)
        te_tonen += boodschap
        if i != len(boodschappen) - 2:
            te_tonen += '\n'
    te_tonen = str(totale_prijs) + '\n' + str(te_tonen)
    return str(te_tonen)