def romanizer(numbers):
    # Write your code here
    l1 = []
    for number in numbers:
        tempstr = ""
        tempstr += numerizerLogic(number, 'C', 'D', 'M', 2)
        tempstr += numerizerLogic(number, 'X', 'L', 'C', 1)
        tempstr += numerizerLogic(number, 'I', 'V', 'X', 0)
        
        l1.append(tempstr)
    return l1

def numerizerLogic(number, oneschar, fiveschar, tenschar, base):
    tempstr = ""
    tempnumber = number // (10**base)
    if (base != 0):
        tempnumber = tempnumber % (10**base)
    else:
        tempnumber = tempnumber % 10
    if tempnumber == 0:
        return tempstr

    if tempnumber >= (9):
        tempstr += oneschar
        tempstr+= tenschar
    elif tempnumber >= (4):
        if tempnumber < (5):
            tempstr += oneschar
        tempstr += fiveschar
    if (tempnumber % 5 < 4):
        for _ in range(tempnumber % 5):
            tempstr += oneschar

    return tempstr

if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)
    print(result)