i = 0
sum = 0
while((inp := input()) != 'THE END'):
    wordslist = inp.split()
    output = '' 
    for word in wordslist:
        output += str(len(word))
    sum += int(output)
    i += 1
    print(f'Line {i + 1}: {output}')
print(f'Total sum: {sum}')
