import math

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    pos_a = 10 if a == 0 else a
    pos_b = 10 if b == 0 else b

    k = pos_b - pos_a + 1
    print(math.comb(n + k - 3, k - 1))
