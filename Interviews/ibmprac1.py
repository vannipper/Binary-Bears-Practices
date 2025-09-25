def getOneBits(n):
    # Write your code here 
    l1 = []
    tempstr = str(bin(n)).lstrip('0b')
    print(tempstr)
    for i, bit in enumerate(tempstr):
        print(i, bit)
        if bit == '1':
            l1.append(i + 1)
    l1.insert(0, len(l1))
    return l1      

if __name__ == '__main__':

    n = int(input().strip())

    result = getOneBits(n)
    print(result)