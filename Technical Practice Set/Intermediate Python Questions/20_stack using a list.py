'''Implementing a stack using a list in Python is straightforward since Python lists 
provide the necessary methods to support stack 
operations like push, pop, and peek. Here’s a simple implementation of a stack using a list:
'''

# Stack Implementation

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack)  # Output: Stack after pushes: [1, 2, 3]

print("Top element is:", stack.peek())  # Output: Top element is: 3

print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Stack after pop:", stack)       # Output: Stack after pop: [1, 2]

print("Stack size:", stack.size())     # Output: Stack size: 2

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

stack.pop()
stack.pop()
print("Is stack empty after popping all elements?", stack.is_empty())  # Output: Is stack empty after popping all elements? True

'''
Explanation
Initialization: The __init__ method initializes an empty list self.items to store the
 stack elements.

is_empty: Checks if the stack is empty by verifying if self.items has zero length.

push: Adds an element to the top of the stack using the append method.

pop: Removes and returns the top element of the stack using the pop method of the list.
 If the stack is empty, it raises an IndexError.

peek: Returns the top element of the stack without removing it.
 If the stack is empty, it raises an IndexError.

size: Returns the number of elements in the stack by returning the length of self.items.

str: Returns a string representation of the stack for easier debugging and visualization.

== Example Usage ==

Push Operations: stack.push(1), stack.push(2), stack.push(3) adds 
elements 1, 2, and 3 to the stack.

Peek Operation: stack.peek() returns the top element, which is 3.

Pop Operation: stack.pop() removes and returns the top element, which is 3.

Size Check: stack.size() returns the number of elements in the stack.

Empty Check: stack.is_empty() checks if the stack is empty.

'''