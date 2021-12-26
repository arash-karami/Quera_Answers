input_n = int(input(""))

for i in range(1, input_n):
    if (2 ** i) > input_n:
        print(2 ** i)
        break

