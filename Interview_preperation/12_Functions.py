'''Functions in Python are blocks of reusable code that perform a specific task. 
Functions help in organizing code, avoiding redundancy, and improving readability.
'''

### 1. Defining a Function
'''
You define a function using the `def` keyword followed by the function name and
 parentheses. The block of code within the function is indented.
'''
#### Basic Function Definition

def greet():
    print("Hello, world!")

### 2. Calling a Function

'''
Once a function is defined, you can call it by using its name followed by parentheses.
'''
#### Example:

greet()  # Output: Hello, world!

### 3. Parameters and Arguments
'''
Functions can take parameters (inputs) and return values. 
Parameters are specified within the parentheses in the function definition.
'''
#### Function with Parameters

def greet(name):
    print(f"Hello, {name}!")

#### Calling the Function with Arguments

greet("Alice")  # Output: Hello, Alice!

### 4. Return Statement
'''
Functions can return values using the `return` statement. If no `return` statement is
 provided, the function returns `None` by default.
'''
#### Function with Return Value

def add(a, b):
    return a + b

#### Calling the Function and Using the Return Value

result = add(5, 3)
print(result)  # Output: 8

### 5. Default Parameter Values
'''
You can provide default values for parameters. If an argument is not
 provided for a parameter with a default value, the default value is used.
'''
#### Example:

def greet(name="Guest"):
    print(f"Hello, {name}!")

#### Calling the Function with and without Arguments

greet()           # Output: Hello, Guest!
greet("Alice")    # Output: Hello, Alice!

### 6. Keyword Arguments
'''
You can specify arguments by name when calling a function, which is known as using
 keyword arguments.
'''
#### Example:

def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(name="Alice", age=30)  # Output: Alice is 30 years old.

### 7. Variable-Length Arguments
'''
Functions can accept a variable number of arguments using `*args` for
 positional arguments and `**kwargs` for keyword arguments.
'''
#### Using `*args` for Positional Arguments

def sum_numbers(*args):
    return sum(args)

#### Example:

print(sum_numbers(1, 2, 3, 4))  # Output: 10

#### Using `**kwargs` for Keyword Arguments

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#### Example:

print_info(name="Alice", age=30)
# Output:
# name: Alice
# age: 30

### 8. Lambda Functions
'''
Lambda functions are small anonymous functions defined using the `lambda` keyword. 
They can have any number of arguments but only one expression.
'''
#### Syntax:
'''
lambda arguments: expression
'''
#### Example:

square = lambda x: x ** 2
print(square(5))  # Output: 25

### 9. Function Annotations
'''
Function annotations provide a way to attach metadata to function arguments and return
 values. They are optional and are not enforced by Python.
'''
#### Example:

def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

### 10. Nested Functions
'''
Functions can be defined inside other functions. The inner function is called a 
nested function or inner function.
'''
#### Example:

def outer_function(message):
    def inner_function():
        print(message)
    inner_function()

#### Calling the Outer Function

outer_function("Hello from the inner function!")  # Output: Hello from the inner function!

### 11. Recursive Functions
'''
A recursive function is one that calls itself in order to solve a problem.
'''
#### Example: Factorial Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#### Calling the Recursive Function

print(factorial(5))  # Output: 120
