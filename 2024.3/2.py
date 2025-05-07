cases = int(input())
for i in range(cases):
    num = input()
    string = ""
    cur = str(num)[0]
    count = 0
    for digit in str(num):
        if cur == digit:
            count += 1
        else:
            string += str(count) + cur
            count = 1
            cur = digit
    string += str(count) + cur
    print(string)