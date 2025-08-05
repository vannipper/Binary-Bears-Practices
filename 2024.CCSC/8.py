for i in range(int(input())):
    s1 = input()
    print(f'Line {i + 1}: words={len(s1.split())} chars={len(s1.replace(' ', ''))} gap width={(80 - len(s1.replace(' ', ''))) // ((len(s1.split()) - 1))}')