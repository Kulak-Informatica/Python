def tel_woorden(zin):
    telling = 0
    for i in range(len(zin)):
        if zin[i] == ' ':
            telling += 1
        #elif zin[i] == '. ':
            #telling += 1
        elif zin[i] == '.':
            telling += 1
    return telling

def langste_zin(zinnen):
    langste_zin = 0
    zin = 0
    bijhouden = 0

    for i in range(len(zinnen)):
        if bijhouden == 0 and zinnen[i] == '.':
            langste_zin = tel_woorden(zinnen[:i + 1])
            bijhouden += 1
            a = i + 2

        elif bijhouden > 0 and zinnen[i] == '.':
            zin = tel_woorden(zinnen[a: i + 1])
            a = i + 2

        if zin > langste_zin:
            langste_zin = zin
    return langste_zin

print(langste_zin('De kaaimantaks zou de financiële sluiproutes naar belastingsparadijzen droogleggen. Veel woorden maar weinig daden, lijkt me, afgaand op wat hier is gezegd. Kortom, de belastingparadijzen en het einde van de belastingparadijzen zijn niet aan de orde. Tenzij de regering alsnog orde op zaken stelt. Maar in lopende zaken is dat niet vanzelfsprekend.'))