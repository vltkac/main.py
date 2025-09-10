class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self): # O(1)
        return self.head is None

    def print(self): # O(N)
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.value, end=' -> ')

            temp_node = temp_node.next

        print()

    def push_end(self, data):
        if not self.is_empty(): # O(1)
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

        else: # O(1)
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node


new_list = SinglyLinkedList()
new_list.push_end(0)
new_list.push_end(1)
new_list.push_end(100)

new_list.print()