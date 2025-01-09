# stack.py

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print('Stack after pushing elements:', s.stack)

s.pop()
print('Stack after popping an element:', s.stack)

peek = s.peek()
print(f'Top element is: {peek}')

print(f'Stack size is: {s.size()}')
