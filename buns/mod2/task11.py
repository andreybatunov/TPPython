stroke = input("Введите последовательность целых чисел: ")
stroke = stroke.replace(" ", "")
past = ""
flag = False
for i in range(len(stroke)):
    if stroke[i] in past:
        flag = True
        break
    else:
        past += stroke[i]
print(flag)