# Basic Exception Handling

'''try and except The try block lets you 
test a block of code for errors. The except block lets you handle the error.'''

try:
    # Code that may raise an exception
    x = 1 / 0
except ZeroDivisionError as e:
    # Code that runs if the exception occurs
    print(f"Caught an exception: {e}")

'''else The else block lets you execute code 
if no exceptions were raised.'''

try:
    x = 10 / 2
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
else:
    print("No exceptions occurred, result is:", x)

'''finally The finally block lets you execute code, regardless 
of whether an exception was raised or not.'''

try:
    x = 1 / 1
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
finally:
    print("This code runs no matter what")



# Raising Exceptions

'''You can raise an exception using the raise statement. '''

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Common Built-in Exceptions

'''
ArithmeticError: Base class for all arithmetic errors.
ZeroDivisionError: Raised when dividing by zero.
IndexError: Raised when accessing an invalid index in a list.
KeyError: Raised when accessing a non-existent key in a dictionary.
NameError: Raised when using a variable that hasn't been defined.
TypeError: Raised when an operation or function is applied to an object of inappropriate type.
ValueError: Raised when a function receives an argument of the right type but inappropriate value.
FileNotFoundError: Raised when trying to open a file that doesn't exist.
IOError: Raised when an I/O operation fails.
ImportError: Raised when an import statement fails.

'''

# Example: Multiple Exceptions

'''Single except block:'''

try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"Caught an exception: {e}")

'''Multiple except blocks:'''

try:
    x = int("abc")
except ValueError as e:
    print(f"Caught a ValueError: {e}")
except TypeError as e:
    print(f"Caught a TypeError: {e}")


# Custom Exceptions

class CustomError(Exception):
    pass

def example_function(x):
    if x < 0:
        raise CustomError("Negative value is not allowed")

try:
    example_function(-1)
except CustomError as e:
    print(f"Caught a custom exception: {e}")
