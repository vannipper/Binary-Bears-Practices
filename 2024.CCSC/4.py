i = 0
e = int(input())
while(i < e):
    num = int(input())
    sum = 0
    length = len(str(num))
    for char in str(num):
        sum += pow(int(char), length)

    if sum == num:
        print(f'Case #{i + 1}" YES')
        continue

    print(f'Case #{i + 1}: NO')