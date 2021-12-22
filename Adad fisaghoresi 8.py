input_1 = int(input(""))
input_2 = int(input(""))
input_3 = int(input(""))


def pythagorean_numbers(x, y, z):
    cal_1 = ((x ** 2) + (y ** 2))
    cal_2 = ((x ** 2) - (y ** 2))
    cal_3 = ((y ** 2) - (x ** 2))
    if cal_1 == (z ** 2):
        print("YES")
    elif cal_2 == (z ** 2):
        print("YES")
    elif cal_3 == (z ** 2):
        print("YES")
    else:
        print("NO")


pythagorean_numbers(input_1, input_2, input_3)
