woord_1 = input('')
woord_2 = input('')

prefix = ''
suffix = ''
haakskes = ''

if len(woord_1) < len(woord_2):
    kortste_woord = woord_1
    langste_woord = woord_2
else:
    kortste_woord = woord_2
    langste_woord = woord_1


for a in range(len(kortste_woord)):
    if woord_1[a] == woord_2[a]:
        prefix += woord_1[a]
    else:
        break

for c in range(-1, -len(kortste_woord)-1, -1):
    if woord_1[c] == woord_2[c]:
        suffix = woord_1[c] + suffix
    else:
        break

print('{}┏{}┓'.format(len(prefix) * ' ', midden_1))
print('{}┫{}┣{}'.format(prefix, (len(langst)- len(sufix) - len(prefix)) * ' ', sufix))
print('{}┗{}{}{}┛'.format(len(prefix) * ' ', aantal_l * ' ', midden_2, aantal_r * ' '))

