import statistics

weekcount, weekdata = 1, []
monthcount, monthdata = 1, []
yeardata = []

running = True
while running:
    line = input().split()
    for value in line:
        if value == '-1.0':
            print(f'Week #{weekcount} = {statistics.mean(weekdata):2f} mi.')
            weekcount += 1
            weekdata = []
        elif value == '-2.0':
            print(f'\nMonth #{monthcount} = {statistics.mean(monthdata):2f} mi.\n')
            monthcount += 1
            monthdata = []
        elif value == '-3.0':
            running = False
        else:
            weekdata.append(float(value))
            monthdata.append(float(value))
            yeardata.append(float(value))

print(f'\nYear to Date for {len(yeardata)} days = {statistics.mean(yeardata):2f} mi.')
