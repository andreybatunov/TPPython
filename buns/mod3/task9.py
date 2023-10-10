file_input = open("input9.txt", "r")
n = int(file_input.readline())
file_output = open("output9.txt", "w")
coords = [0, 0]
deltas = []
for delta in range(1, int(n**0.5)+1):
    if sum(deltas) + 2*delta <= n:
        deltas += [delta] * 2
    else:
        deltas.append(delta)
if sum(deltas) != n:
    deltas.append(n - sum(deltas))
for i in range(0, len(deltas), 4):
    deltas[i] *= -1
    if i+1 < len(deltas):
        deltas[i+1] *= -1
for i in range(len(deltas)):
    coords_index = 0 if i % 2 == 0 else 1
    coords[coords_index] += deltas[i]
file_output.write(f"{coords[0]} {coords[1]}")
file_input.close()
file_output.close()