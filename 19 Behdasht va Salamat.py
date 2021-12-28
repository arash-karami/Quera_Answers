mark_input = int(input(""))
days_input = int(input(""))

if days_input == 0:
    print(20)
elif days_input <= 7:
    print(mark_input)
else:
    calulation = mark_input - days_input
    if calulation < 0:
        print(0)
    else:
        print(calulation)

