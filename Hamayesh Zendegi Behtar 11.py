row_number_input = input("").split()
list_input = list(map(int, row_number_input))
row = list_input[0]
number = list_input[1]


def row_number_calculator():
    output = ""
    if number > 10:
        output += "Left"
    elif number <= 10:
        output += "Right"

    row_calculator = abs(row - 10) + 1
    output += f" {row_calculator}"

    if number <= 10:
        output += f" {number}"
    elif number > 10:
        number_calculator = abs(20 - number) + 1
        output += f" {number_calculator}"
    print(output)


row_number_calculator()
