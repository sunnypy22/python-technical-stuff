'''In Python, errors that occur during program execution are represented by exceptions.
 Each exception has a specific name that describes the type of error encountered. 
 Here’s a list of common Python exception names, along with a brief description of each:
'''
### Built-in Exceptions

'''
1. **`Exception`**: The base class for all built-in exceptions. 
Custom exceptions should inherit from this class.

2. **`ArithmeticError`**: Base class for errors related to numeric calculations.
   - **`ZeroDivisionError`**: Raised when dividing by zero.
   - **`OverflowError`**: Raised when a calculation exceeds the limits of the numeric type.
   - **`FloatingPointError`**: Raised when a floating-point operation fails.

3. **`AttributeError`**: Raised when an attribute reference or assignment fails.

4. **`FileNotFoundError`**: Raised when a file or directory is requested but cannot be found.

5. **`IOError`**: Raised when an I/O operation (e.g., reading or writing a file) fails. 
In Python 3.x, it is often replaced by `OSError`.

6. **`ImportError`**: Raised when an import statement fails to find the module definition.
   - **`ModuleNotFoundError`**: Raised when a module could not be found 
   (introduced in Python 3.6).

7. **`IndexError`**: Raised when a sequence subscript is out of range.

8. **`KeyError`**: Raised when a dictionary key is not found.

9. **`MemoryError`**: Raised when an operation runs out of memory.

10. **`NameError`**: Raised when a local or global name is not found.

11. **`NotImplementedError`**: Raised when an abstract method requires implementation.

12. **`OSError`**: Base class for operating system-related errors.
    - **`FileExistsError`**: Raised when trying to create a file or directory that
      already exists.
    - **`PermissionError`**: Raised when trying to open a file in write mode or modify a
      file without appropriate permissions.

13. **`RuntimeError`**: Raised for errors that do not fall into other categories.
    - **`RecursionError`**: Raised when the maximum recursion depth is exceeded.

14. **`StopIteration`**: Raised to signal the end of an iteration.

15. **`SyntaxError`**: Raised when the parser encounters a syntax error.
    - **`IndentationError`**: A subclass of `SyntaxError` raised for indentation errors.
    - **`TabError`**: Raised when inconsistent use of tabs and spaces is detected.

16. **`TypeError`**: Raised when an operation or function is applied to an object of 
inappropriate type.

17. **`ValueError`**: Raised when a function receives an argument of the right type 
but inappropriate value.

18. **`Warning`**: Base class for warning messages.
    - **`DeprecationWarning`**: Raised when a feature is deprecated.
    - **`UserWarning`**: Raised for user-defined warnings.
    - **`SyntaxWarning`**: Raised for syntax-related warnings.
'''
### Handling Exceptions
'''
To handle exceptions in Python, you use a `try` block to wrap the code that might
 raise an exception, and `except` blocks to handle specific exceptions. You can also use `finally` to execute code regardless of whether an exception was raised or not.
'''
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the exception
    print(f"An error occurred: {e}")
finally:
    # Code that runs no matter what
    print("Execution completed.")

### Custom Exceptions
'''
You can also define your own exceptions by subclassing the `Exception` class.
'''
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"CustomError: {e}")
