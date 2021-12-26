input_numbers = input("").split()
list_input_numbers = list(map(int, input_numbers))


def determine_time():
    a_time = list_input_numbers[0]
    b_time = list_input_numbers[1]
    repeat = list_input_numbers[2]
    if (repeat % 2) != 0:
        even_repeat = repeat - 1
        calculation_1 = ((even_repeat // 2) * (a_time + b_time)) + a_time
        print(calculation_1)
    else:
        calculation_2 = (repeat // 2) * (a_time + b_time)
        print(calculation_2)


determine_time()
