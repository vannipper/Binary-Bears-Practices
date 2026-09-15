def isLeap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

for _ in range(int(input())):
    y1 = int(input())
    counter = 0
    for year in range(y1 + 1, 3000):
        if (isLeap(year)):
            counter += 2
        else:
            counter += 1

        if (counter % 7 == 0 and (isLeap(year) == isLeap(y1))):
            print(f'Calendar for {y1} can next be reused in {year}.')
            break