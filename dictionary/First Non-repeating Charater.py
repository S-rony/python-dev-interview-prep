s = "aabbcdde"
d = {}
count = 0
for  i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for key, val in d.items():
    if val == 1:
        print(key)
        break
