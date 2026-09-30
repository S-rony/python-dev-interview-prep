
class Node:
    def __init__(self, data, prev=None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def rev_traversal(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data)
            temp = temp.prev




obj1 = Node(10)
obj2 = Node(20)
obj3 = Node(30)

obj1.next = obj2
obj2.prev = obj1
obj2.next = obj3
obj3.prev = obj2

dll = DoublyLinkedList()
dll.head = obj1
dll.traversal()
print()
dll.rev_traversal()