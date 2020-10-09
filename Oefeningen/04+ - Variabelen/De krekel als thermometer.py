#input
tjirps = float(input('Geef mij het aantal waargenomen tjirps per minuut: '))

#formule
Fahrenheit = 50 + (( tjirps - 40 ) / 4 )
Celcius = 10 + (( tjirps - 40 ) / 7 )

#uitvoer
print('temperatuur (Fahrenheit): ' + str(Fahrenheit))
print('temperatuur (Celsius): ' + str(Celcius))
