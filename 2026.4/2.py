for _ in range(int(input())):
    open_delim, close_delim = input().split()
    line = input()
    tokens = line.split()
    
    balance = 0
    is_balanced = True
    
    for token in tokens:
        if token == open_delim:
            balance += 1
        elif token == close_delim:
            balance -= 1
        if balance < 0:
            is_balanced = False
            break
            
    if balance != 0:
        is_balanced = False
        
    if is_balanced:
        print(f"{line} is balanced")
    else:
        print(f"{line} is not balanced")
