for _ in range(int(input())):
    h, m, s = map(int, input().split(':'))
    time = (600 - (((m % 10) * 60) + s)) % 600
    print(time)