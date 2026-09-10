#rReturn the indices of the elements in the array whose sum is equal to the target.

def two_sum(arr, target):
    d = {}
    for i in range(len(arr)):
        needed_num = target - arr[i]
        if needed_num in d:
            return [d[needed_num] , i]
        else:
            d[arr[i]] = i


arr = [1, 3, 5, -7, 6, -3]
target = 0
print(two_sum(arr, target))