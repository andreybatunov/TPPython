stroke = input("Введите слово: ")
def count_symbols(s):
    counts = {}
    for char in s:
        if char not in counts.values():
            counts.update({char : s.count(char)})
    return counts

def is_palindrom(counts):
    odd_count = 0
    for value in counts.values():
        if value%2!=0:
            odd_count+=1
    return True if odd_count<=1 else False

counts = count_symbols(stroke)
if is_palindrom(counts):
    left = [key * (counts[key] // 2) if counts[key] % 2 == 0 else "" for key in counts.keys()]
    right = left[::-1]
    mid = [key * counts[key] if counts[key] % 2 != 0 else "" for key in counts.keys()]
    print(f'Из строки можно составить палиндром: {"".join(left)}{"".join(mid)}{"".join(right)}')
else:
    print("Строка не является палиндромом")