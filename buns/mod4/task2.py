numbers=[int(i) for i in input().split()]
a,n = numbers[0], numbers[1]
def power(a,n):
    if n==0:
        return 1
    else:
        if abs(n)%2==0:
            return power(a*a, n//2) if n>0 else 1 / power(a*a, abs(n)//2)
        else:
            return a * power(a, n-1) if n>0 else 1 / (a * power(a, abs(n)-1))
print(power(a, n))
            