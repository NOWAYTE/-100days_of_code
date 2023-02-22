import math


def paint_calc(height, width, cover):
    area = height * width
    numb_of_cans = math.ceil(area / cover)
    print(f"you will need {numb_of_cans}")


test_height = int(input("Height of wall"))
test_width = int(input("Width of wall"))
coverage = 5

paint_calc(height=test_height, width=test_width, cover=coverage)
