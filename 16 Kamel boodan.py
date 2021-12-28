input_n = int(input(""))


def whole_or_not(n):
    list_of_divisions = []
    for i in range(1, ((n // 2) + 1)):
        if n % i == 0:
            list_of_divisions.append(i)
    sum_divions = sum(list_of_divisions)
    if sum_divions == n:
        print("YES")
    else:
        print("NO")


whole_or_not(input_n)