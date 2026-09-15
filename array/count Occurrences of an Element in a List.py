numbers = [10, 20, 10, 30, 20, 40]
count = 0
target = 10
for i in range(len(numbers)):
        if numbers[i] == target:
            count+= 1
print(count)