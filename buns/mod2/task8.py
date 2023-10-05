stroke = input("Введите строку и символ: ")
s = stroke[:len(stroke)-2]
i = stroke[len(stroke)-1::]
count_i = 0
for j in range(len(s)):
    if s[j] != i:
        break
    else:
        count_i += 1
print(count_i)
    