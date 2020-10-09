from math import pi
tijd = float(input(''))
concentratie = round((pi * tijd) / (pow(tijd, 2) + 2), 4)
print(concentratie)