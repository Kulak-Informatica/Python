gewenste_snelheid = int(input(''))
actuele_snelheid = int(input(''))
rem_snelheid = actuele_snelheid
aantal_rembewegingen = 0

while rem_snelheid >= gewenste_snelheid:
    rem_snelheid = rem_snelheid - (0.3 * rem_snelheid)
    aantal_rembewegingen += 1

print('na {} rembewegingen is de snelheid {:.2f}'.format(aantal_rembewegingen, rem_snelheid))