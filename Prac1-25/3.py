for _ in range(int(input())):
    l = input().replace('(', '( ').replace(')', ' )').split()
    while(len(l) > 1):
        for ind, val in enumerate(l):
            if val == ')':
                templist = l[(ind - 4):ind]
                o1, o2, op = int(templist[2]), int(templist[3]), templist[1]
                for _ in range(5):
                    l.pop(ind - 4)
                if op == '+':
                    l.insert(ind - 4, str(o1 + o2))
                elif op == '-':
                    l.insert(ind - 4, str(o1 - o2))
                elif op == '*':
                    l.insert(ind - 4, str(o1 * o2))
                else:
                    l.insert(ind - 4, str(o1 ** o2))
                break
    print(int(l[0]))
