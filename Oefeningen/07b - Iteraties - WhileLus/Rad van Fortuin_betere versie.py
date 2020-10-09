woord = input('')
bedrag = int(input(''))

gewonnen_bedrag = 0
geraden_letters = ''

letter = input()

while (letter in woord) and (letter not in geraden_letters):
    gewonnen_bedrag += bedrag
    geraden_letters += letter
    letter = input('')

print(gewonnen_bedrag)