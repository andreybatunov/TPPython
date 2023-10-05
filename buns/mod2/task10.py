stroke = input("Введите список слов: ")
answer = ""
for i in range(len(stroke)):
    if i != len(stroke) - 1 and stroke[i+1] == " ":
        answer += stroke[i]
    elif i == len(stroke) - 1:
        answer += stroke[i]
print(answer)