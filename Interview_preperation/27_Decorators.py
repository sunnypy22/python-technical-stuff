'''Decorators in Python are a powerful feature that allows you to modify or
     extend the behavior of functions or methods without changing their actual code. 
     They provide a way to wrap another function and enhance its functionality.
'''
### What is a Decorator?
'''
A decorator is a function that takes another function (or method) as its argument
 and returns a new function that typically extends or alters the behavior of the original
   function. Decorators are commonly used for logging, access control, memoization, and more.
'''
### Basic Syntax
'''
Decorators are applied to functions using the `@decorator_name` syntax before the 
function definition.
'''
'''
@decorator_name
def function_name(parameters):
    # Function body
'''

### How Decorators Work
'''
1. **Function Definition**: A decorator is defined as a function that takes a function 
    as an argument.
2. **Wrapper Function**: The decorator returns a wrapper function that adds new behavior.
3. **Function Call**: When the decorated function is called, it actually calls the wrapper
     function, which can execute code before or after the original function.
'''

### Example of a Simple Decorator
'''
Here's a basic example of a decorator that prints messages before and after the function 
    execution:
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
'''
**Output:**
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
'''

### Decorators with Arguments
'''
If you want to pass arguments to your decorator, you need to create a decorator
     factory—a function that returns a decorator.
'''
def repeat(n):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

'''
**Output:**
Hello, Alice!
Hello, Alice!
Hello, Alice!
'''
### Using `functools.wraps`
'''
When creating decorators, it's a good practice to use `functools.wraps` to ensure 
    that the metadata of the original function is preserved (e.g., its name and docstring).
'''
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")

print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: Say hello to someone.

### Decorators with Arguments
'''
To create a decorator that takes arguments, you need to use a decorator factory.
'''
def log(level):
    def decorator_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Log level: {level}")
            return func(*args, **kwargs)
        return wrapper
    return decorator_log

@log("DEBUG")
def process_data(data):
    print(f"Processing {data}")

process_data("sample data")
'''
**Output:**
Log level: DEBUG
Processing sample data
'''
### Class-based Decorators
'''
Decorators can also be implemented as classes with `__call__` methods:
'''
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        result = self.func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()

'''
**Output:**

Something is happening before the function is called.
Hello!
Something is happening after the function is called.
'''
### Summary
'''
- **Decorators** are functions or classes that modify or extend the behavior
     of other functions or methods.
- **Syntax**: Use the `@decorator_name` syntax to apply a decorator.
- **Function Wrapping**: Decorators wrap functions, allowing you to add pre- 
    and post-processing behavior.
- **Decorator Factories**: Create decorators with arguments using nested functions.
- **Preserving Metadata**: Use `functools.wraps` to maintain the original function's
     metadata.
- **Class-based Decorators**: Implement decorators as classes with a `__call__` method.

Decorators are a versatile feature that can help you write cleaner and more maintainable
     code by separating concerns and enhancing functionality.

'''