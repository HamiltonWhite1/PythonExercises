def opposite(number):
    opposite_num = 0
    if number > 0:
        opposite_num = -abs(number)
    elif number < 0:
        opposite_num = abs(number)

    return opposite_num
opposite(-9)