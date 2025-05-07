s = input()
count = 0
for index in range(len(s)):
    try:
        if s[index:index+3] == ":-)":
            count += 1
    except:
        continue
print(count)