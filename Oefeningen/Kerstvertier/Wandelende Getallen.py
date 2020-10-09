import math


invoer_2 = str(input(''))
invoer = str(invoer_2.replace('.', ''))
x_coordinaat = 0
y_coordinaat = 0

for i in range(len(invoer)):
    hoek = (36 * int(invoer[i]))

    if int(invoer[i]) < 3 and int(invoer[i]) > 0:
        waarde_x = math.cos(math.radians(90 - hoek))
        waarde_y = math.cos(math.radians(hoek))
        x_coordinaat += waarde_x
        y_coordinaat += waarde_y

    elif int(invoer[i]) >= 3 and int(invoer[i]) < 5:
        waarde_x = math.sin(math.radians(180 - hoek))
        waarde_y = math.cos(math.radians(180 - hoek))
        x_coordinaat += waarde_x
        y_coordinaat -= waarde_y

    elif int(invoer[i]) == 5:
        x_coordinaat += 0
        y_coordinaat -= 1

    elif int(invoer[i]) == 0:
        x_coordinaat += 0
        y_coordinaat += 1

    elif int(invoer[i]) <= 7 and int(invoer[i]) > 5:
        waarde_x = math.sin(math.radians(hoek - 180))
        waarde_y = math.cos(math.radians(hoek - 180))
        x_coordinaat -= waarde_x
        y_coordinaat -= waarde_y

    elif int(invoer[i]) > 7:
        waarde_x = math.sin(math.radians(360 - hoek))
        waarde_y = math.cos(math.radians(360 - hoek))
        x_coordinaat -= waarde_x
        y_coordinaat += waarde_y

print('Getal {} wandelt naar positie ({:.2f}, {:.2f}).'.format(invoer_2, x_coordinaat, y_coordinaat))