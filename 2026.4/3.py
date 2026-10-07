import math

rates = {
    'velvet': 0.25,
    'straw': 0.35,
    'wool': 0.45
}

for _ in range(int(input())):
    inputList = input().split()
    modelNum = inputList[1]
    material = inputList[2]
    
    size = float(inputList[3])
    if len(inputList) > 4:
        num, denom = inputList[4].split('/')
        size += int(num) / int(denom)

    circumference = size * (25 / 8)
    radius = circumference / (2 * math.pi)

    top_area = math.pi * (radius ** 2)
    middle_area = circumference * 4
    brim_area = (math.pi * ((radius + 3) ** 2)) - top_area

    total_area = top_area + middle_area + brim_area
    price = total_area * rates[material]

    print(f'Model {modelNum} $ {price:.2f}')
