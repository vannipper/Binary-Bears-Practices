n = int(input())

while n != 0:
    new_vals = input().split()
    for i, val in enumerate(new_vals):
        new_vals[i] = float(val)

    grades = []
    for i in range(n):
        grades.append(int(input()))

    total = 0
    for grade in grades:
        total += grade
    oldmean = total / n

    total = 0
    for grade in grades:
        current = grade - oldmean
        current *= current
        total += current
    total /= (n - 1)
    oldsigma = total**(1/2)

    zvals = []
    for value in grades:
        zvals.append((value - oldmean) / oldsigma)
    
    newgrades = []
    for i in range(n):
        newgrades.append(int(new_vals[0] + (zvals[i] * new_vals[1])))
    newgrades.sort()
    for val in newgrades:
        if val < 0:
            val = 0
        print(val)
    n = int(input())
