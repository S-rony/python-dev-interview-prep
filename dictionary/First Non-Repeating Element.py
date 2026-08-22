d = {}
arr = [4, 5, 1, 2, 1, 4, 5]
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for keys, values in d.items():
    if values == 1:
        print(keys)
        break

