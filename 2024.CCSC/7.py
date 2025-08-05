import math
for _ in range(int(input())):
    qs, num = input().split(',')
    qs = int(qs)
    lenKey = len(num)
    num = len(set(num))
    if qs < num:
        print('Impossible Answer Key!')
        continue
    try:
        print(math.ceil(math.log(0.5, (1 - pow(1 / num, lenKey)))) % 1_000_000)
    except ValueError:
        print(1)