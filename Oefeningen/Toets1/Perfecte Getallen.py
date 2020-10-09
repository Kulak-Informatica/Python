getal = int(input(''))
boodschap = '1 is geen perfect getal'
som = 1
delers = '1 '

for i in range(2, getal):
    if getal % i == 0:
        som += i
        i = '{} '.format(i)
        variabel = str(i)
        delers = str(delers) + str(i) + ''

if som == getal and getal != 1:
    boodschap = '{} is een perfect getal en de delers zijn {}'.format(getal, delers)

elif som != getal and getal != 1:
    boodschap = '{} is geen perfect getal'. format(getal)

print(boodschap)
