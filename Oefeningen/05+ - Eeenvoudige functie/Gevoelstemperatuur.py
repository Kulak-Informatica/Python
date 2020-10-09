# invoer
temp = float(input('Luchtemperatuur in graden celcius: '))
winds = float(input('Wndsnelheid in km/u: ')) / 3.6

# uitvoer
print(13.12 + (0.6215 * temp) + (((0.3965 * temp) - 11.37)*(3.6 * winds) **0.16))