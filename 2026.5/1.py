table = [
    (30, 10),
    (25, 15),
    (18, 20),
    (12, 30),
    (5, 40),
    (-10, 50)
]

max_water = -1.0
best_location = ''

for _ in range(int(input())):
    snowfall, temp, location = input().split(maxsplit=2)
    t = int(temp)
    
    ratio = min(table, key=lambda x: (abs(x[0] - t), -x[0]))[1]
    water = float(snowfall) / ratio

    if water > max_water:
        max_water, best_location = water, location

print(f"More water fell in {best_location} ({max_water:.1f} inches)")
