### `super()`
'''
- **Purpose**: The `super()` function is used to call methods from a parent
     class from within a subclass. This is particularly useful for extending or
       modifying the behavior of inherited methods.
- **Usage**: It helps in calling the parent class's method and is often used in method
     overriding and when dealing with multiple inheritance.
'''
'''
**Basic Syntax**:
super().method_name(arguments)
'''


# **Example**:
class Parent:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value from Parent: {self.value}")

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # Calls Parent's __init__
        self.extra = extra

    def show(self):
        super().show()  # Calls Parent's show
        print(f"Extra value from Child: {self.extra}")

# Usage
child = Child(10, 20)
child.show()
'''
**Output**:
Value from Parent: 10
Extra value from Child: 20
'''
'''
**Key Points**:
- `super()` allows access to methods in a parent class without explicitly naming it.
- Useful in cooperative multiple inheritance where classes share common methods.
'''

### `object()`

'''
- **Purpose**: The `object()` function is the base class for all new-style classes in Python.
    It provides a common base class with default implementations of some methods like
   `__str__()`, `__repr__()`, and `__eq__()`.
- **Usage**: You can use `object()` to explicitly create a new-style class or to invoke 
    the base class methods.

**Basic Syntax**:
class MyClass(object):
    pass
'''

# **Example**:
class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass object with name: {self.name}"

# Usage
obj = MyClass("Test")
print(obj)
'''
**Output**:
MyClass object with name: Test
'''

'''
**Key Points**:
- In Python 3, all classes implicitly inherit from `object`, so `object()` is often
     not needed.
- In Python 2, using `object()` was necessary to create new-style classes.
'''

### Closures

'''
- **Purpose**: Closures are functions that capture and remember the values of variables from
     their surrounding lexical scope even after the scope has finished executing. They
       allow the function to have access to its outer function’s scope.

**Concept**:
- A closure occurs when a nested function references variables from its enclosing function.
- Useful for maintaining state between function calls without using global variables.
'''

# **Example**:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Usage
closure = outer_function(10)
result = closure(5)  # Here, x is 10 and y is 5
print(result)  # Output: 15

'''
**Key Points**:
- The `inner_function` in this example is a closure because it remembers the value of `x` 
from its enclosing `outer_function`.
- Closures are often used in decorators and other scenarios where state needs to be preserved.
'''
### Summary

'''
- **`super()`**: Used to call methods from a parent class, allowing you to extend or 
    modify inherited methods. Essential for method overriding and cooperative multiple 
        inheritance.
- **`object()`**: The base class for all new-style classes in Python. It provides default
     implementations of core methods and is implicit in Python 3.
- **Closures**: Functions that capture and retain references to variables from their 
    enclosing scope, allowing them to maintain state across multiple calls.
'''