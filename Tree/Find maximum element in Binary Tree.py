

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

    def pre_order(self, root):
        if root is not None:
            print(root.data,end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(root.data , end= " ")
            self.in_order(root.right)



    def post_order(self,root):
        if root is not None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=" ")

    def maximum_element(self, root):
        if root is None:
            return -float("inf")

        left_max = self.maximum_element(root.left)
        right_max = self.maximum_element(root.right)
        curr_max = root.data
        # curr_max = curr_element = root.data
        if curr_max < left_max:
            curr_max = left_max
        if curr_max < right_max:
            curr_max = right_max

        return curr_max


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
print()
print(root.maximum_element(root))
