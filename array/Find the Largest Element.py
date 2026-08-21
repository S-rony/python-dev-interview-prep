arr = [10, 25, 7, 42, 18]

max = 0
for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]
print(max)