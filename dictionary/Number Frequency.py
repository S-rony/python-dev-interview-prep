arr = [1, 2, 2, 3, 1, 4, 2]

d = {}
for element in arr:
    if element not in d:
        d[element] = 1
    else:
        d[element] += 1
print(d)