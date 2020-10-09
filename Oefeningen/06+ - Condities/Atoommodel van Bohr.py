# invoer
aantal_e = int(input())

# if en else
schil = ''
if aantal_e > 124:
    schil = 'Q'
elif aantal_e > 92:
    schil = 'P'
elif aantal_e > 60:
    schil = 'O'
elif aantal_e > 28:
    schil = 'N'
elif aantal_e > 10:
    schil = 'M'
elif aantal_e > 2:
    schil = 'L'
else:
    schil = 'K'

# uitvoer
print('De {}-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(schil, aantal_e))