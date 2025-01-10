class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

# Example
ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
print(ll.display())  # Output: [5, 10, 15]
ll.delete(10)
print(ll.display())  # Output: [5, 15]
