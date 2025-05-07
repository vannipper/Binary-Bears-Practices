
barricades = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    #print(f'{x1} {y1} {x2} {y2}')
    if x1 / x2 > 0:
        barricades.append(-1)
    else:
        slope = (y2-y1) / (x2-x1)
        barricades.append(-slope*x1 + y1)

if barricades.count(-1) != len(barricades):
    barricades = sorted(barricades)
    while (barricades[0] < 0):
        barricades.pop(0)
    print(barricades[0])
else:
    print(-1)