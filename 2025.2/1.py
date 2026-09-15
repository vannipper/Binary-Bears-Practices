count = 0
for _ in range(int(input())):
    line = input()
    for word in line.split():
        if word.lower().startswith('@britishmonarchy'):
            count += 1
            break

print(f'Total Tweets Containing @BritishMonarchy = {count}')