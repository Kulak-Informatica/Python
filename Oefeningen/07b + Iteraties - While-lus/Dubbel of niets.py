kapitaal = int(input(''))
variabel = 0
inzet = input('')
inzet2 = -2
while inzet != 'stop':
    kleur = input('')
    kleur2 = input('')
    if inzet == 'alles':
        inzet = int(kapitaal)
    else:
        inzet = int(inzet)

    if inzet <= kapitaal and kleur == kleur2:
        kapitaal += inzet
    elif inzet > kapitaal:
        inzet2 = inzet
        inzet = 'stop'
        variabel += 1
    else:
        kapitaal -= inzet

    if inzet != 'stop':
        inzet = input("")

if variabel == 0:
    print("Je eindigt met {} dollar.".format(kapitaal))
else:
    print("Je kunt geen {} dollar inzetten als je maar {} dollar hebt.".format(inzet2, kapitaal))
