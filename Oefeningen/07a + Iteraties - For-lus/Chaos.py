d = float(input(''))
r = float(input(''))
s = int(input(''))

print(d)
for i in range(s - 1):
    d = t = r * d * (1 - d)
    print(d)