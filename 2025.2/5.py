import datetime as dt

for _ in range(int(input())):
    l1 = input().replace(',', '').split()
    monthstring = l1[0].lower()
    
    if monthstring.lower() == 'january':
        l1[0] = 1
    elif monthstring.lower() == 'february':
        l1[0] = 2
    elif monthstring.lower() == 'march':
        l1[0] = 3
    elif monthstring.lower() == 'april':
        l1[0] = 4
    elif monthstring.lower() == 'may':
        l1[0] = 5
    elif monthstring.lower() == 'june':
        l1[0] = 6
    elif monthstring.lower() == 'july':
        l1[0] = 7
    elif monthstring.lower() == 'august':
        l1[0] = 8
    elif monthstring.lower() == 'september':
        l1[0] = 9
    elif monthstring.lower() == 'october':
        l1[0] = 10
    elif monthstring.lower() == 'november':
        l1[0] = 11
    else:
        l1[0] = 12
    
    l1 = list(map(int, l1))
    d1 = dt.datetime(l1[2], l1[0], l1[1])
    print(f'{d1.strftime("%A")}, {d1.strftime("%B")} {l1[1]}, {l1[2]}')