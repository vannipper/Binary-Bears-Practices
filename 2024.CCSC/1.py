def toint(char):
    try:
        return int(char)
    except ValueError:
        return 0
    
for _ in range(int(input())):
    print(sum(toint(i) for i in input()))