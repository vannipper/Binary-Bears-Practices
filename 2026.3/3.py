import math

def volume(x):
    return math.pi * (W ** 2) * (x - (x ** 3) / (3 * (L ** 2)))

for potatNum in range(int(input())):
    l, w, s = map(float, input().split())
    s = int(s)

    L = l / 2.0
    W = w / 2.0
    thickness = l / s

    print(f'Potato {potatNum + 1}')

    for k in range(s):
        x1 = -L + k * thickness
        x2 = -L + (k + 1) * thickness

        print(f'  Slice {k + 1} = {(volume(x2) - volume(x1)):.3f}')
