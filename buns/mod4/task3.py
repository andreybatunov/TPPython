numbers = [int(i) for i in input().split()]
a, b = numbers[0], numbers[1]
def nod(a, b):
    if (a == b):
        return a
    else:
        if a > b:
            return nod(a-b, b)
        else:
            return nod(a, b-a)
print(nod(a,b))