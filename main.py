from Data_Structure.Linked_list import Single_linked_list
from Data_Structure.Linked_list import CircularLinkedList
from Data_Structure.Linked_list import DoublyLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

def reverse_list(head):
    prev_node = None
    curr_node = head

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    head = prev_node
    return head

# Create a singly linked list
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

# Print the original list
print("Original List:")
my_list.print_list()

# Reverse the list
my_list.head = reverse_list(my_list.head)

# Print the reversed list
print("Reversed List:")
my_list.print_list()

def main():
    single_list = Single_linked_list
    double_list = DoublyLinkedList
    circular_list = CircularLinkedList


if __name__ == "__main__":
    main()
