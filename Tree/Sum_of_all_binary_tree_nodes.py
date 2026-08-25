from itertools import count


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def pre_order(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    def post_order(self, root):
        if root is not None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=" ")

    def count_total_nodes(self, root):
        count = 0
        if root is not None:
            left_count = self.count_total_nodes(root.left)
            right_count = self.count_total_nodes(root.right)
            count = left_count + right_count + 1
        return count

    def sum_of_nodes(self,root):
        if root is None:
            return 0
        left_sum = self.sum_of_nodes(root.left)
        right_sum = self.sum_of_nodes(root.right)
        current_node = root.data
        return left_sum + right_sum + current_node




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.pre_order(root)
print()
root.in_order(root)
print()
root.post_order(root)
print()
print(root.sum_of_nodes(root))

