f=open("input11.txt", "r")
field_strokes = f.read().split("\n") #for straight wins
k = len(field_strokes)
x_win_stroke, o_win_stroke = "X"*k, "O"*k
field_matrix = [[str(i) for i in field_strokes[j]] for j in range(k)]
field_matrix_t = [[field_matrix[i][j] for i in range(k)] for j in range(k)]
field_strokes_t = ["".join(field_matrix_t[i]) for i in range(k)] #for straight wins
x_win_straight = (x_win_stroke in field_strokes) or (x_win_stroke in field_strokes_t)
o_win_straight = (o_win_stroke in field_strokes) or (o_win_stroke in field_strokes_t)
if x_win_straight or o_win_straight:
    print("X" if x_win_straight else "O")
else:
    first_diag = "".join([str(field_matrix[i][i]) for i in range(k)])
    second_diag = "".join([str(field_strokes[i][j]) if i+j==k-1 else "" for i in range(k) for j in range(k)])
    x_win_diag = (x_win_stroke == first_diag) or (x_win_stroke == second_diag)
    o_win_diag = (o_win_stroke == first_diag) or (o_win_stroke == second_diag)
    if x_win_diag or o_win_diag:
        print("X" if x_win_diag else "O")
    else:
        print("Ничья")