def pascalTriangleI(r, c):
    prev = [1]
    row = r
    for i in range(row - 1):
        curr = [1]
        for j in range(len(prev) - 1):
            curr.append(prev[j] + prev[j+1])
        curr.append(1)
        prev = curr
    return curr[c-1]
r = 5
c = 3
print(pascalTriangleI(r,c))


#
# Input: r = 4, c = 2
#
# Output: 3