import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(math.perm(n, k))