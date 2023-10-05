stroke = input("Введите символ и число: ")
i = stroke[:1]
n = int(stroke[2:])
if n < 0 and ord(i) + n < 97:
    offset = 26 - abs(n)%26
elif n < 0 and ord(i) + n >= 97:
    offset = 0 - abs(n)%26
else:
    offset = n % 26
print(chr(ord(i) + offset))
