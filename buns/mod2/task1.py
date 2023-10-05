numbers=str(input("Введите числа: "))
first_number = ""
second_number = ""
flag = True
for i in range(len(numbers)):
    if flag:
        first_number += numbers[i]
        if numbers[i] == ",":
            first_number = int(first_number[0:len(first_number)-1])
            flag = False
    else:
        second_number += numbers[i]
second_number = int(second_number)
print(first_number%second_number)