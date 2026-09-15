numbers = [5, 2, 8, 1, 9]
maximum = float("-inf")

for i in range(len(numbers)):
    if numbers[i] > maximum:
        max = numbers[i]
print(maximum)