#variabelen
Invoer = float(input('Geef mij het aantal dagen in sol weer: '))
Factor = 88775.244/86400
MD_AD = Invoer * Factor
DIS = MD_AD * 86400
Dagen = int(DIS // 86400)
Uren = int((MD_AD - Dagen) * 24)
Minuten = int(( DIS - ( Dagen* 86400 ) - ( Uren * 3600 )) / 60)
Seconden = int( DIS - ( Dagen* 86400 ) - ( Uren * 3600 ) - ( Minuten * 60))

#uitvoer
print(str(int(Invoer)) + ' sol = ' + str(Dagen) + ' dagen, ' + str(Uren) + ' uren, ' + str(Minuten) + ' minuten en ' + str(Seconden) + ' seconden')