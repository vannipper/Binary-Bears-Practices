for matrix in range(int(input())):
    seen = set()
    found = False
    for rows in range(int(input().split()[0])):
        s = sum(map(int, input().split()))
        if s in seen:
            print('no')
            found = True
            break
        seen.add(s)

    if not found:
        print('yes')