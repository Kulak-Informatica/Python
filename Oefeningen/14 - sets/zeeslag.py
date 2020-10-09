def boot_overlappend(set_boot, set_vloot):
    boodschap = True
    for zet in set_boot:
        if zet not in set_vloot:
            boodschap = False
        else:
            boodschap = True
            break

    return boodschap


def boot_toevoegen(set_boot, set_vloot):
    string = ''
    for plaats in set_boot:
        TF = boot_overlappend({plaats}, set_vloot)
        if TF == True and string == '':
            string += '!'

    if string != '!':
        for plaats in set_boot:
            set_vloot.add(plaats)
    return set_vloot


def vuur(zet, bord):
    if zet in bord:
        bord.remove(zet)
        return True, bord

    else:
        return False, bord





print(boot_overlappend({'B4', 'A4', 'C4'}, {'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_overlappend({'F4', 'F5', 'F6', 'F3'}, {'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_toevoegen({'B4', 'A4', 'C4'}, {'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_toevoegen({'F4', 'F5', 'F6', 'F3'}, {'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(vuur('I7', {'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))
print(vuur('F8', {'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))
