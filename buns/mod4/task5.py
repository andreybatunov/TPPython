def count_symbols(s):
    counts = {}
    for char in s:
        if char not in counts.values() and ('a'<=char<='z' or 'A'<=char<='Z'):
            counts.update({char : s.count(char)})
    return dict(sorted(counts.items(), key=lambda x: x[1]))

filename = input()
f = open(filename, 'r')
out = open("output.txt", 'w')
stroke = f.read()
counts = count_symbols(stroke)
data = [f'{key}: {counts[key]}' for key in counts.keys()]
out.write('\n'.join(data))
out.close()
f.close()