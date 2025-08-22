for _ in range(int(input())):
    s = input()
    s = s.replace('(', '( ')
    s = s.replace(')', ' )')
    l = s.split()
    while(len(l) > 1):
        # print(f'List: {l}')
        for ind, val in enumerate(l):
            # print(ind, val)
            if val == ')':
                templist = l[(ind - 4):ind]
                # print(f'Templist {templist}')
                o1 = int(templist[2])
                o2 = int(templist[3])
                op = templist[1]
                #print(o1, o2, op)
                for _ in range(5):
                    l.pop(ind - 4)
                #print(list)
                if op == '+':
                    l.insert(ind - 4, str(o1 + o2))
                    break
                elif op == '-':
                    l.insert(ind - 4, str(o1 - o2))
                    break
                elif op == '*':
                    l.insert(ind - 4, str(o1 * o2))
                    break
                else:
                    l.insert(ind - 4, str(o1**o2))
                    break
    print(int(l[0]))

