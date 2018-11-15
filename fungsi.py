import math


def sudut(panjang_x, panjang_y):
    if (panjang_y == 0):
        sudut2 = 90

    elif (panjang_x == 0):
        sudut2 = 0

    else:
        rad = math.atan(panjang_x/panjang_y)
        sudut1 = rad * (180 / (22 / 7))
        sudut2 = round(sudut1, 2)

    return sudut2
