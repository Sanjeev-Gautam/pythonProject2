# A singly linked list is a linear collection of data elements, called nodes,
# each pointing to the next node by means of a pointer.
# It is a data structure consisting of a collection of nodes which together represent a sequence.
# In a singly linked list, each node stores a reference to an object and a reference to the next node in the list.
# The last node has a reference to null, indicating the end of the list. It is also known as Singly linked chain.

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def print1(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next

l1 = LinkedList()
l1.add(8)
l1.add(7)
l1.add(3)
l1.add(5)
l1.add(6)
print("Lets print single Linked list")
l1.print1()








#     def print_list(self):
#         curr_node = self.head
#         while curr_node:
#             print(curr_node.data)
#             curr_node = curr_node.next
#
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()