import math
for i in range(int(input())):
    p, q = map(int, input().split())
    tuples = []
    for b in range(1, q): # What is the correct range to check?
        a = abs((-q*b) / (p*b - q))
        if a.is_integer():
            tuples.append((int(a), b))
    print(f'Case {i + 1}: 1/a + 1/b = {p}/{q}')
    tuples.sort(key=lambda x: x[1])
    for c in tuples:
        print(f'{c[1]} {c[0]}')