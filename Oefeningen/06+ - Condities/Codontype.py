# invoer
codon_input = input('')

# if en else
description = ''

if codon_input == 'AUG':
    discription = 'start'
elif codon_input == 'UAG' or codon_input == 'UGA' or codon_input == 'UAA':
    discription = 'stop'
elif len(codon_input) != 3:
    discription = 'non-valid'
else:
    discription = 'normal'

# uitvoer
print('The codon {} is a {} codon.'.format(codon_input, discription))