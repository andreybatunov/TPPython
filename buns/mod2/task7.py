stroke = input("Введите строку: ")
count_0 = 0
count_1 = 0
for i in range(len(stroke)):
    if stroke[i] == "0":
        count_0 += 1
    else:
        count_1 += 1
if count_0 == count_1:
    print("yes")
else:
    print("no")
