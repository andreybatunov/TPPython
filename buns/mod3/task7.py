stroke = input().split()
print(False if sum([stroke.count(i) for i in stroke])==len(stroke) else True)