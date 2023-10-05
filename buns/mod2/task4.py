n = float(input("Введите число: "))
hex_alf = "0123456789ABCDEF"
bin_number = ''
oct_number = ''
hex_number = ''
if n != int(n) or n == 0:
    print("Неверный ввод")
else:
    n = int(n)
    n8 = int(n)
    n16 = int(n)
    while n > 0:
        bin_number = str(n % 2) + bin_number
        n = n // 2
    while n8 > 0:
        oct_number = str(n8 % 8) + oct_number
        n8 = n8 // 8
    while n16 > 0:
        hex_number = hex_alf[n16 % 16] + hex_number
        n16 = n16 // 16
print(f"{bin_number}, {oct_number}, {hex_number}")