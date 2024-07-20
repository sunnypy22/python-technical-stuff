'''A context manager in Python is a construct that allows you to allocate and release
     resources precisely when you want to. The most common example of a context manager 
     is the `with` statement, which simplifies resource management and exception handling 
     by ensuring that resources are properly cleaned up after use.
'''
### What is a Context Manager?
'''
A context manager is an object that defines the methods `__enter__` and `__exit__` which 
are used by the `with` statement to set up and tear down resources, respectively.
'''

### How Context Managers Work
'''
1. **Entering**: The `__enter__` method is called when the execution flow enters the context
     of the `with` statement. It can return a value that can be used within the `with` block.

2. **Exiting**: The `__exit__` method is called when the execution flow leaves the context of
     the `with` statement. It can handle exceptions and perform cleanup actions. If it returns
       `True`, it suppresses the exception; if it returns `False` or `None`, the exception is
         propagated.
'''
### Built-in Context Managers
'''
Python provides several built-in context managers for managing resources such as files, locks,
 and network connections. For example, file handling is done using a context manager to
   ensure the file is properly closed after operations are completed.
'''

# **Example with File Handling**:
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
# File is automatically closed after exiting the `with` block

### Custom Context Managers
'''
You can create custom context managers by defining a class with `__enter__` and `__exit__` 
    methods or by using the `contextlib` module to create a context manager with a generator
      function.
'''

# **Custom Context Manager Using a Class**:
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Value returned can be used within the `with` block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Handle exception if needed
        return False  # Do not suppress exceptions

# Usage
with MyContextManager() as cm:
    print("Inside the context")


# **Custom Context Manager Using `contextlib`**:
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield  # Yield control back to the `with` block
    finally:
        print("Exiting the context")

# Usage
with my_context_manager() as cm:
    print("Inside the context")

### Key Points
'''
- **Resource Management**: Context managers simplify resource management and ensure that 
    resources are properly cleaned up after use, reducing the risk of resource leaks.
- **Exception Handling**: The `__exit__` method can handle exceptions that occur within
     the `with` block, allowing for proper cleanup and error handling.
- **Custom Context Managers**: You can create your own context managers either by defining
     a class with `__enter__` and `__exit__` methods or by using the `contextlib` module
       with a generator function.
'''

### Summary

'''
- **Context Managers**: Facilitate resource management by ensuring that resources are 
    acquired and released properly.
- **Common Use Cases**: File handling, network connections, database connections, and
     locking mechanisms.
- **Custom Context Managers**: Can be created using classes or generator functions to
     handle specific resource management needs.
'''