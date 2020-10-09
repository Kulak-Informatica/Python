aantal_doden = int(input(''))


A = B = C = D = E = F = G = H = I = J = 0
for i in range(aantal_doden):
    invoer = input('')
    if invoer == 'A':
        A = 1
    elif invoer == 'B':
        B = 1
    elif invoer == 'C':
        C = 1
    elif invoer == 'D':
        D = 1
    elif invoer == 'E':
        E = 1
    elif invoer == 'F':
        F = 1
    elif invoer == 'G':
        G = 1
    elif invoer == 'H':
        H = 1
    elif invoer == 'I':
        I = 1
    elif invoer == 'J':
        J = 1
fles = (A * pow(2, 0)) + (B * pow(2, 1)) + (C * pow(2, 2)) + (D * pow(2, 3)) + (E * pow(2, 4)) + (F * pow(2, 5)) + (G * pow(2, 6)) + (H * pow(2, 7)) + (I * pow(2, 8)) + (J * pow(2, 9))
print('Fles #{} is vergiftigd.'.format(fles))

