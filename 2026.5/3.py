import math
from fractions import Fraction

while True:
    try:
        line = input()
    except EOFError:
        break
        
    if not line.strip():
        continue
        
    N, C = map(int, line.split())
    if N == 0 and C == 0:
        break

    tokens = []
    while len(tokens) < 2 * C:
        tokens.extend(input().split())

    fractions = [Fraction(int(tokens[i]), int(tokens[i+1])) for i in range(0, 2 * C, 2)]
    total_frac = sum(fractions)
    
    if total_frac > 1:
        print("Too much!")
    elif total_frac == 1 and all((N * f).denominator == 1 for f in fractions):
        print("Just right!")
    else:
        L = math.lcm(*(f.denominator for f in fractions))
        M = N if N % L == 0 else (N // L + 1) * L
            
        k = M - N
        j = M - int(M * total_frac)
        
        r = lambda v: f"{v} rabbit" if v == 1 else f"{v} rabbits"
        
        print(f"Bring {r(k)}, distribute {r(M)}, take {r(j)} home.")
