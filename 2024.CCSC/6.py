import math

def findNeeded(item, amount, rawmats, recipies): # recursive function to get down to the raw materials
    print(recipies.get(item))
    amount = math.ceil(amount / (recipies.get(item)[0] / recipies.get(item)[1]))
    if recipies.get(item)[2] not in rawmats: # recursive case
        return (findNeeded(recipies.get(item)[2], amount, rawmats, recipies))
    else: # base case
        return (amount, recipies.get(item)[2])

for _ in range(int(input())):
    # INPUT SECTION
    buildname = input()
    m, r, p = list(map(int, input().split()))
    rawmats, recipies, products = [], {}, []
    for _ in range(m):
        rawmats.append(input())
        rawmats.append(0)
    for _ in range(r):
        templist = input().split()
        recipies[templist[4]] = (int(templist[3]), int(templist[0]), templist[1])
    for _ in range (p):
        products.append(input().split())
        products[-1][0] = int(products[-1][0])

    # OUTPUT SECITON
    for amount, item in products:
        tempamount, tempraw = findNeeded(item, amount, rawmats, recipies)
        rawmats[rawmats.index(tempraw) + 1] += tempamount
    print(buildname)
    for i in range(0, len(rawmats), 2):
        if rawmats[i+1] != 0:
            print(f'{rawmats[i + 1]} {rawmats[i]}')