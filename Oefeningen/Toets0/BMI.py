# invoer
lengte = float(input())
naam_1 = str(input(''))
gewicht_1 = float(input())
naam_2 = str(input(''))
gewicht_2 = float(input())

# bmi's
bmi_1 = gewicht_1 / (lengte * lengte)
bmi_2 = gewicht_2 / (lengte * lengte)

# sorteren van bmi's
if bmi_1 > bmi_2:
    bmi = bmi_1
    naam = naam_1
else:
    bmi = bmi_2
    naam = naam_2

# sorteren van grootste bmi in klasse's
boodschap = 'heeft ondergewicht'
if bmi >= 30:
    boodschap = 'is obees'
elif bmi >= 25 and bmi < 30:
    boodschap = 'heeft overgewicht'
elif bmi >= 18.5 and bmi < 25:
    boodschap = 'heeft een gezond gewicht'
else:
    boodschap = 'heeft ondergewicht'

# uitvoer
print('{} heeft het hoogste BMI ({:.2f}) en {}.'.format(naam, bmi, boodschap))