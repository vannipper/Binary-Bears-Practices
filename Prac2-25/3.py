def issubset(i, j):
    num1 = str(i)
    num2 = str(j)
    t1 = num1[0:2]
    t2 = num1[1:]
    t3 = num1[0]+num1[2]4.

    if num2 == t1 or num2 == t2 or num2 == t3:
        return True
    
    return False

for itr in range(int(input())):
    numsols = 0
    n = int(input())
    print(f'Test case {itr + 1}')
    for i in range(100, 1000):
        for j in range(10, 100):
            if (i - j == n and issubset(i, j)):
                numsols += 1
                print(f'  {i} - {j} = {n}')
    if numsols == 0:
        print(f'  No solution for d = {n}')
        