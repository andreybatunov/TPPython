numbers = input().split()
counts = {}
for number in numbers:
    counts.update({str(number):numbers.count(number)})
if sum(counts.values())==len(counts):
    print("Все числа разные")
elif sum(counts.values())>len(counts) and len(counts)!=1:
    print("Есть равные и неравные числа")
else:
    print("Все числа равны")
    