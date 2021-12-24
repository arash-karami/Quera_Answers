list_of_numbers = []

def input_process():
    while True:
        input_numbers = input("> ")
        list_of_numbers.append(input_numbers)
        if input_numbers == "0":
            break


def print_process():
    list_of_numbers.reverse()
    for i in list_of_numbers[1:]:
        print(i)

input_process()
print_process()

