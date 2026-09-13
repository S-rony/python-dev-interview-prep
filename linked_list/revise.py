
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, data, target_value):
        new_node = Node(data)
        temp = self.head

        while temp is not None:
            if temp.data == target_value:
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                temp = temp.next
        print("Target node not found!")








    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node



    def transversal(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

ll = SinglyLinkedList()
ll.insert_at_beg(30)
ll.insert_at_beg(20)
ll.insert_at_beg(10)

ll.transversal()