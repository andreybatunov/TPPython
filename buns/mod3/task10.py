size = int(input())
matrix = [[str(i) for i in range(1,size + 1)] for i in range(1,size+1)]
matrix_t = [[matrix[i][j] for i in range(size)] for j in range(size)]
for i in range(size):
    print(*[matrix[i][j]+"," if j!=size-1 else matrix[i][j] for j in range(size)])
print("\n")
for i in range(size):
    print(*[matrix_t[i][j]+"," if j!=size-1 else matrix_t[i][j] for j in range(size)])