a=float(input("Введите число: "))
perimeter = format(a*4, ".2f")
area = format(a**2, ".2f")
diagonal = format((2*a**2)**0.5, ".2f")
print(f"{perimeter}, {area}, {diagonal}")
