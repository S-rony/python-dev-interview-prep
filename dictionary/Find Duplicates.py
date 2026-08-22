arr = [1, 2, 3, 2, 4, 5, 1, 6, 3]
#output = 1,2,3
d = {}
for ele in arr:
    if ele not in d:
        d[ele] = 1
    else:
        d[ele] += 1

for keys,values in d.items():
    if values > 1:
        print(keys)