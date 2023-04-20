class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head

    def print1(self):
        current = self.head
        if self.head != None:
            while True:
                print(current.data)
                current = current.next
                if current == self.head:
                    break

l1 = LinkedList()
l1.add(5)
l1.add(6)
l1.add(7)
l1.add(8)
l1.add(9)

print("Circular Linked List")
l1.print1()