import math
for i in range(int(input())):
    print(f'Tournament {i +1}')
    l1 = list(map(int, input().split()))
    for j in range(len(l1) - 1):
        offset = l1[0] - 2**(int(math.log(l1[0],2)))
        num = l1[0] + offset - (l1[j + 1]) + 1
        if l1[j+1] <= offset:
            print(f'  Seed {l1[j+1]} gets a bye.')
        else:
            print(f'  Seed {l1[j+1]} plays seed {num}.')