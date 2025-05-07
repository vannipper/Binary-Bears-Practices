def checkBalanced(snum):
        stack = []
        for char in snum:
            if char == '(':
                stack.insert(0, ')')
            elif char == '[':
                stack.insert(0, ']')
            else:
                if stack[0] != char:
                    return False
        return True

strings = []
for _ in range(iter := int(input())):
    strings.append(input())

for snum in strings:
    if checkBalanced(snum):
        print(f"{snum} is balanced")
    else:
        print(f"{snum} is not balanced")
    