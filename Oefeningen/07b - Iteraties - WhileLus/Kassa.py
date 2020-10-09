invoer = float(input(''))
som = invoer

while invoer != 0:
    invoer = float(input(''))
    som += invoer

print('De totale prijs is € {:.2f}'.format(som))