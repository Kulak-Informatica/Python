def bepaal_hittegolven(filex):
    file = open(filex, "r")
    x = file.read()
    x = x.split(' ')

    file = []
    for i in x:
        if not (i == '' or i == '\n'):
            file += [i]

    hoeveelheid = 0
    warmedagen = 0
    hetedagen = 0
    getal = 1
    startdag = 0
    stopdag = ''
    tuplelijst = []
    for i in file:
        i = int(i)
        if i >= 30:
            warmedagen += 1
            hetedagen += 1
            if startdag == 0:
                startdag = getal

        elif i >= 25:
            warmedagen += 1
            if startdag == 0:
                startdag = getal

        else:
            if warmedagen >= 5 and hetedagen >= 3:
                stopdag = getal - 1
                tuplelijst += [(startdag, stopdag)]
                hoeveelheid += 1
                warmedagen = 0
                hetedagen = 0
                startdag = 0
            else:
                warmedagen = 0
                hetedagen = 0
                startdag = 0
        getal += 1

    return hoeveelheid, tuplelijst