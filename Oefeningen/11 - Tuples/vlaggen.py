def vlag(richting, kleuren):
    variabel = 0
    boodschap = ''
    if richting == 'verticaal':
        for i in range(len(kleuren)):
            if variabel == (len(kleuren) - 1):
                boodschap += kleuren[i]

            else:
                boodschap += kleuren[i]
                boodschap += ' | '
                variabel += 1

    else:
        for i in range(len(kleuren)):
            if variabel == (len(kleuren) - 1):
                boodschap += kleuren[i]

            else:
                boodschap += kleuren[i]
                boodschap += '\n-\n'
                variabel += 1
    return boodschap

print(vlag('verticaal',('zwart', 'geel', 'rood')))