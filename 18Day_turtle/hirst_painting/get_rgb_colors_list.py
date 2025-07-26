import colorgram

colors = colorgram.extract('image.jpg', 64)
rgb_colors = []

# first_color = colors[0]
# rgb = first_color.rgb
# print(rgb)
# r_num = rgb.r
# g_num = rgb.g
# b_num = rgb.b
# rgb_num = tuple((r_num, g_num, b_num))
# print(rgb_num)

for i in colors:
    rgb_colors.append(tuple((i.rgb.r, i.rgb.g, i.rgb.b)))

print(rgb_colors)

