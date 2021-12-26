input_coardinates = input("").split()

x_mostafa = input_coardinates[0]
y_mostafa = input_coardinates[1]
x_boss = input_coardinates[2]
y_boss = input_coardinates[3]

if x_mostafa == x_boss:
    print("Vertical")
elif y_mostafa == y_boss:
    print("Horizontal")
else:
    print("Try again")
