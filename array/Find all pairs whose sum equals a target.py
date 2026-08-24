#Find all pairs whose sum equals a target


# output = [(2, 7), (4, 5), (8, 1)]


def sum_pair(arr, target):
    d = {}
    result = []
    for element in range(len(arr)):
        needed = target - arr[element]
        if needed in d:
            result.append((needed, arr[element]))
        else:
            d[arr[element]] = needed
    print(result)
target = 9
arr = [2, 7, 4, 5, 3, 8, 1]
sum_pair(arr,target)