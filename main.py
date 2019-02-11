from display import *
from draw import *
import math

screen = new_screen(500, 500)
color = [255, 255, 255]
for x in range(500):
    for y in range(500):
        plot(screen, color, x, y)
hey = list()
for x in range(0,251,125):
    hey.append(x)
    hey.append(-x)

for x in hey:
    for y in hey:
        nxy = [250 + x, 250 + y]
        draw_line(nxy[0], nxy[1], 250, 250, screen, [255, 0, 0])


# def draw_tree(level, x, y, length, angle):
#     x1 = int(x + length * math.sin(angle * (math.pi / 180)))
#     y1 = int(y + length * math.cos(angle * (math.pi / 180)))
#     draw_line(x, y, x1, y1, screen, [0, 0, 0])
#     if level < 10:
#         draw_tree(level + 1, x1, y1, length - length * 0.2, angle + 20)
#         draw_tree(level + 1, x1, y1, length - length * 0.2, angle - 20)
#
#
# draw_tree(0, 250, 0, 90, 0)

# plot(screen, [255,0,0], 250, 225)

display(screen)
save_extension(screen, 'img.png')
