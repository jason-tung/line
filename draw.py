from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    if x0 > x1:
        draw_line(x1, y1, x0, y0, screen, color)
    else:
        dy = y1 - y0
        dx = x1 - x0
        # 01256
        if dy > 0:
            #o26
            if dy >= dx:
                draw_caseo2(x0, y0, x1, y1, screen, color)
            #o14
            else:
                draw_caseo1(x0, y0, x1, y1, screen, color)
        # o3478
        else:
            #o73
            if -1 * dy >= dx:
                draw_caseo7(x0, y0, x1, y1, screen, color)
            #o84
            else:
                draw_caseo8(x0, y0, x1, y1, screen, color)


def draw_caseo1(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    a = y1 - y0
    b = -(x1 - x0)
    d = 2 * a + b
    while x <= x1:
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += 2 * b
        x += 1
        d += 2 * a


def draw_caseo2(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    a = y1 - y0
    b = -(x1 - x0)
    d = 2 * b + a
    while y <= y1:
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2 * a
        y += 1
        d += 2 * b


def draw_caseo7(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    a = y1 - y0
    b = -(x1 - x0)
    d = a - 2 * b
    while y >= y1:
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2 * a
        y -= 1
        d -= 2 * b


def draw_caseo8(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    a = y1 - y0
    b = -(x1 - x0)
    d = 2 * a - b
    while x <= x1:
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= 2 * b
        x += 1
        d += 2 * a
