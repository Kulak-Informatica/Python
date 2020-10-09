def germaniseer(zin):
    germaans = ''
    for i in range(len(zin)):
        if zin[i - 1] == ' ':
            germaans += zin[i].upper()
        else:
            germaans += zin[i]
    return germaans

print(germaniseer('Het is ok'))