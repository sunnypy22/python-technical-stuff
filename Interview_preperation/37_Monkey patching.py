'''Monkey patching in Python refers to the practice of modifying or extending existing
     classes or modules at runtime. It involves altering a class or module's behavior by
       dynamically adding or changing methods, attributes, or functionality. While it can
         be useful for testing or extending functionality, it should be used with caution
           as it can make code harder to understand and maintain.
'''
### When to Use Monkey Patching

'''
- **Testing**: To modify behavior or add mocks/stubs in unit tests.
- **Legacy Code**: To fix bugs or add features to third-party libraries without
     modifying the original code.
- **Prototyping**: To quickly test new ideas or changes without altering
     the original codebase.
'''

### How to Monkey Patch

#### Example 1: Modifying a Class Method

# **Original Class**:
class MyClass:
    def greet(self):
        return "Hello, world!"

# **Monkey Patching**:
# Define a new method
def new_greet(self):
    return "Hello, monkey patched world!"

# Apply monkey patch
MyClass.greet = new_greet

# Usage
obj = MyClass()
print(obj.greet())  # Output: Hello, monkey patched world!

#### Example 2: Modifying a Module Function

# **Original Module (example_module.py)**:
def add(a, b):
    return a + b

# **Monkey Patching**:
'''import example_module '''

# Define a new function
def patched_add(a, b):
    return a * b

# Apply monkey patch
#example_module.add = patched_add

# Usage
#print(example_module.add(2, 3))  # Output: 6

#### Example 3: Patching a Third-Party Library

#Suppose you want to patch a method from a third-party library.

#**Original Third-Party Library**:
# third_party_lib.py
class ThirdPartyClass:
    def method(self):
        return "Original method"

# **Monkey Patching**:
# import third_party_lib

# Define a new method
def patched_method(self):
    return "Patched method"

# Apply monkey patch
# third_party_lib.ThirdPartyClass.method = patched_method

# Usage
# obj = third_party_lib.ThirdPartyClass()
# print(obj.method())  # Output: Patched method

### Pros and Cons of Monkey Patching
'''
**Pros**:
- **Flexibility**: Allows dynamic modification of classes or modules without changing
     the original source code.
- **Testing**: Useful for modifying behavior or adding mocks/stubs in unit tests.

**Cons**:
- **Maintenance**: Can make the codebase harder to understand and maintain.
- **Compatibility**: Changes may not be compatible with future updates of the patched
     class/module.
- **Debugging**: Can lead to subtle bugs and issues that are difficult to trace.
'''