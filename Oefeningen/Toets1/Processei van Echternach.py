aantal = int(input(''))
stappen_vooruit = 2
stappen_achteruit = 0
plaats = 2
bijgehouden = 1
bijgehouden_vooruit = 1
bijgehouden_achteruit = 0

while bijgehouden != aantal:
    bijgehouden += 1
    bijgehouden_achteruit += 1
    stappen_achteruit += (1 * bijgehouden_achteruit)
    if bijgehouden == aantal:
        break
    else:
        bijgehouden += 1
        bijgehouden_vooruit += 1
        stappen_vooruit += (2 * bijgehouden_vooruit)

plaats = stappen_vooruit - stappen_achteruit

print(plaats)