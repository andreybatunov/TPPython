stroke = input("Введите доменное имя сайта: ")
current_domen = ""
for i in range(len(stroke) - 1, -1, -1):
    if stroke[i] != ".":
        current_domen = stroke[i] + current_domen
    else:
        print(current_domen)
        current_domen = ""
print(current_domen)