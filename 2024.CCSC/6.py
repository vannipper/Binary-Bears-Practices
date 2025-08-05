for e in range(int(input())):
    l1 = []
    for h in range(int(input())):
        for n in range(int(input())):
            l1.append(input().split())
        l1.sort(key=lambda x: float(x[2]))
    print(f'Event {e + 1}: Gold - {l1[0][0]} ({l1[0][1]})\n')
    print(f'Event {e + 1}: Silver - {l1[1][0]} ({l1[1][1]})\n')
    print(f'Event {e + 1}: Bronze - {l1[2][0]} ({l1[2][1]})\n')