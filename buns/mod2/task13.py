stroke = input("Введите штрих-код: ")
even_sum = 0
odd_sum = 0
flag = True
for i in range(len(stroke)):
    if flag:
        odd_sum += int(stroke[i])
        flag = False
    else:
        even_sum += int(stroke[i])
        flag = True
summ = odd_sum + 3 * even_sum
if summ % 10 == 0:
    print("yes")
else:
    print("no")