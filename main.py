from display import *
from draw import *

screen = new_screen(500,500)
color = [ 0, 255, 0 ]
for x in range(500):
    for y in range(500):
        plot(screen, color, x, y)

display(screen)
save_extension(screen, 'img.png')
