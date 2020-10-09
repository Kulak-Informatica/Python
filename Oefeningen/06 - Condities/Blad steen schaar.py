# invoer
p1 = input('')
p2 = input('')

# if en else
if (p1 == 'blad' and p2 == 'steen') or (p1 == 'steen' and p2 == 'schaar') or (p1 == 'schaar' and p2 == 'blad'):
    print('speler 1 wint')
elif (p1 == p2):
    print('onbeslist')
else:
    print('speler 2 wint')