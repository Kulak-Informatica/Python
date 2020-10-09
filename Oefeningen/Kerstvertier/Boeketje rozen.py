aantal_rw = int(input())
aantal_wb = int(input())
teken = input('')

blauwe_rozen, witte_rozen, rode_rozen = aantal_wb, 0, aantal_rw
variabel = formule = False

while variabel == False:
    witte_rozen += 1
    blauwe_rozen -= 1
    rode_rozen -= 1

    if (teken == '>' and (rode_rozen + blauwe_rozen) > (witte_rozen + blauwe_rozen)) or (teken == '<' and (rode_rozen + blauwe_rozen) < (witte_rozen + blauwe_rozen)):
        formule = True

    if (rode_rozen + witte_rozen == aantal_rw) and (witte_rozen + blauwe_rozen == aantal_wb) and (formule == True) and (witte_rozen > 1) and (rode_rozen > 1) and (blauwe_rozen > 1):
        variabel = True

print(blauwe_rozen)
print(witte_rozen)
print(rode_rozen)