invoer = input('')
list = []
while invoer != 'STOP':
    if invoer == '?' and len(list) != 0:
        print(list[0])
        del(list[0])
    elif invoer != '?':
        list += [invoer]
    invoer = input('')
if len(list) == 0:
    print()
