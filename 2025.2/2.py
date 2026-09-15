l1 = 'qwertyuiop['
l2 = 'asdfghjkl;'
l3 = 'zxcvbnm,'

for _ in range(int(input())):
    line = input()

    if line[0] == 'E':
        line = line[2:]
        out = ''
        for c in line:
            if c in l1:
                out += l1[l1.index(c) + 1]
            elif c in l2:
                out += l2[l2.index(c) + 1]
            elif c in l3:
                out += l3[l3.index(c) + 1]
            else:
                out += c
        print(out)
    elif line[0] == 'D':
        line = line[2:]
        out = ''
        for c in line:
            if c in l1:
                out += l1[l1.index(c) - 1]
            elif c in l2:
                out += l2[l2.index(c) - 1]
            elif c in l3:
                out += l3[l3.index(c) - 1]
            else:
                out += c
        print(out)