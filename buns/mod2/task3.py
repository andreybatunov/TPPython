numbers = str(input("Введите числа: "))
flag = False
for i in range(len(numbers)):
    if numbers[i] == " " and flag == False:
        first_space_index = i
        flag = True
        continue
    if flag == True and numbers[i] == " ":
        second_space_index = i
a = int(numbers[:first_space_index])
b = int(numbers[first_space_index : second_space_index])
c = int(numbers[second_space_index::])
if (a > b):
    if (a < c):
        print (a)
    elif (c > b):
        print (c)
    else:
        print(b)
elif (c > b):
    print (b)
else:
    if (a > c):
        print(a)
    else:
        print(c)