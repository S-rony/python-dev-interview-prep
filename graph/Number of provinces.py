
class Solution:
    def find_provinces(self, adj):
        self.mat = adj
        self.size = len(adj)

        visited = [False] * self.size
        provinces_count = 0
        for i in range(self.size):
            if visited[i] == False:
                provinces_count += 1
                stack = [i]
                while stack:
                    v = stack.pop()
                    if visited[v] == False:
                        visited[v] = True

                    for i in range(self.size):
                        if self.mat[v][i] == 1 and visited[i] == False:
                            stack.append(i)
        return provinces_count


sol = Solution()
# Example 1
adj1 = [
 [1, 0, 0, 1],
 [0, 1, 1, 0],
 [0, 1, 1, 0],
 [1, 0, 0, 1]
]
print("Provinces in Example 1:", sol.find_provinces(adj1))
# Output aayega: 2
