def rgb_to_color(rgb):
    val = int(rgb[1:], 16)
    return (val >> 16) & 0xff, (val >> 8) & 0xff, val & 0xff

def color_to_rgb(color):
    return "#" + "".join(map(lambda x: hex(int(x))[2:].zfill(2), color))

def interp(a, b, t):
    return a + t*(b - a)

for i in range(loops := int(input())):
    rgb1, rgb2, t_total, t_curr = tuple(input().split())
    frac = float(t_curr) / float(t_total)
    col1 = rgb_to_color(rgb1)
    col2 = rgb_to_color(rgb2)
    it_color = map(lambda x: interp(x[0], x[1], frac), zip(col1, col2))
    print(color_to_rgb(it_color))
