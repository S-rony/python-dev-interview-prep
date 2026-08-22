arr = [10, 25, 7, 42, 18]
min = float("inf")
for  i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)