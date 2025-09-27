n = int(input())
for _ in range(n):
    s = input()
    l1 = []
    for char in s:
        l1.append(char)
    swapAllow = True
    for i in range(len(l1)-1):
        if not swapAllow:
            swapAllow = True
            continue
        if l1[i] == 'A':
            if i + 1 == len(l1):
                break
            if l1[i+1] == 'A':
                continue
            temp = l1[i]
            l1[i] = l1[i+1]
            l1[i+1] = temp
            i += 1
            swapAllow = False
    print(''.join(l1))