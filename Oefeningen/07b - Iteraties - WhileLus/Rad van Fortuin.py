woord = str(input(''))
bedrag = int(input(''))
som = 0
letter = str(input(''))
voorgaande_letter = ''
while letter in woord and voorgaande_letter != letter:
    som += bedrag
    voorgaande_letter = letter
    letter = str(input(''))

print(som)