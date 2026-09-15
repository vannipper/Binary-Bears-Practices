for i in range(int(input())):
    l = list(map(int, input().split()))
    asc = sorted(l)
    dec = sorted(l, reverse=True)
    if (len(set(l)) == 1):
        print(f'List {i + 1} is not ordered.')
    elif (l == asc):
        print(f'List {i + 1} is in ascending order.')
    elif (l == dec):
        print(f'List {i + 1} is in descending order.')
    else:
        print(f'List {i + 1} is not ordered.')