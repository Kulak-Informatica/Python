def dronken_voeren(woord):
    uitkomst = ''
    for i in range(len(woord)):
        if i == 0:
            uitkomst += woord[i]
        elif i % 2 == 0:
            uitkomst += woord[i].upper()
        elif uitkomst[i - 1] in 'AEIOU':
            uitkomst += woord[i].upper()
        else:
            uitkomst += woord[i].lower()
    return uitkomst