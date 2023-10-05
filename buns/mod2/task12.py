stroke = input("Введите номер телефона: ")
useless = "()- "
for i in range(len(useless)):
    stroke = stroke.replace(useless[i], "")
print(stroke)