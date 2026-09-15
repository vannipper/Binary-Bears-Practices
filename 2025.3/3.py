import math
n = int(input())
for _ in range (n):
        k0, k1, v, f = map(float, input().split())
        time = v/f * math.log(k0/k1)
        print(f"{time:.3f}h")