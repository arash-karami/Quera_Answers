n_input = int(input(""))
factoriel = 1

if n_input > 1:
    for i in range(1, (n_input + 1)):
        factoriel = factoriel * i
print(factoriel)