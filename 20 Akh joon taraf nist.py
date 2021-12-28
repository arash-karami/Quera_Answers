week_days = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
days = []
count = 0
input_1 = input("")
input_first = input("").split()
input_2 = input("")
input_second = input("").split()
input_3 = input("")
input_third = input("").split()

for i in input_first:
    days.append(i)
for j in input_second:
    days.append(j)
for k in input_third:
    days.append(k)

for i in week_days:
    if i not in days:
        count += 1
print(count)
