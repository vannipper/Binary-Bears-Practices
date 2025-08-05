for _ in range(i := int(input())):
    total = 0
    y1, y2 = map(int, input().split())
    for i in range(y1, y2 + 1):
        if i % 4 == 0 and not i in [1700, 1800, 1900, 2100]:
            total += 1
    if total != 1:
        print(f'There are {total} leap years from {y1} to {y2}.')
    else:
        print(f'There is {total} leap year from {y1} to {y2}.')
