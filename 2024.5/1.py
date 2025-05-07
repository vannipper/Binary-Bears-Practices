for i in range(reps := int(input())):
    print(f'{i+1} {list(map(int, input().split())).sort()}')