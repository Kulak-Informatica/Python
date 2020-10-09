n = int(input(''))

helft_lifters = int(n/2)
maximum = 0

for i in range(1,helft_lifters + 1):
    score_1 = float(input(''))
    if i == 0:
        maximum = score_1
    elif score_1 > maximum:
        maximum = score_1

variabel = 0
for i in range(helft_lifters + 1, n + 1):
    score_2 = float(input(''))
    if score_2 > maximum and variabel == 0:
        variabel += 1
        maximum = score_2
    elif i == n and variabel == 0:
        maximum = score_2
print(maximum)