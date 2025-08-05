for i in range(int(input())):
    r, c = map(int, input().split())
    total = 0
    for _ in range(r):
        row = list(map(int, input().split()))
        if row == sorted(row):
            total += 1
    print(f'Number of Ascending Rows in Matrix #{i + 1}: {total}')