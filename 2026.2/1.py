for _ in range(int(input())):
    r, c = map(int, input().split())
    matrix = []

    for _ in range(r):
        matrix.append(list(map(int, input().split())))

    for col in range(c):
        for row in range(r):
            print(matrix[row][col], end=' ')
        print()
