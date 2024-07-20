'''In Python, scope refers to the region of a program where a particular variable can be
 accessed. Variables in Python can have different scopes,
   depending on where they are defined and how they are used. 
'''
### 1. Local Scope
'''
A variable declared inside a function is in the local scope of that function. 
It is accessible only within that function and not outside of it.
'''
#### Example:

def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
# print(x)  # Error: NameError, x is not defined outside the function

### 2. Enclosing Scope (Nonlocal)
'''
Enclosing scope refers to the scope of any enclosing functions,
 i.e., functions defined inside other functions. 
 Variables defined in the enclosing function are accessible within the
   nested function, but they are not global.
'''
#### Example:

def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        print(x)  # Accessing enclosing variable

    inner_function()

outer_function()  # Output: 10

#### Using `nonlocal` Keyword
'''
You can use the `nonlocal` keyword to modify a variable in the enclosing scope
 from within a nested function.
'''
##### Example:

def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        nonlocal x
        x = 20  # Modifying enclosing variable

    inner_function()
    print(x)

outer_function()  # Output: 20

### 3. Global Scope
'''
A variable declared at the top level of a script or module is in the global scope. 
It can be accessed from any part of the code, 
including functions, unless shadowed by a local variable of the same name.
'''
#### Example:

x = 10  # Global variable

def my_function():
    print(x)  # Accessing global variable

my_function()  # Output: 10
print(x)  # Output: 10

#### Using `global` Keyword
'''
You can use the `global` keyword to modify a global variable from within a function.
'''
##### Example:

x = 10  # Global variable

def my_function():
    global x
    x = 20  # Modifying global variable

my_function()
print(x)  # Output: 20

### 4. Built-in Scope
'''
The built-in scope contains the names of all built-in functions and variables provided
 by Python. This scope is always available in any Python program.
'''
#### Example:

print(len("Hello"))  # len is a built-in function

### 5. LEGB Rule
'''
Python follows the LEGB rule to resolve variable names. The order of resolution is:
'''
'''
1. **Local**: The innermost scope, which includes variables defined inside the current function.
2. **Enclosing**: Any enclosing functions' scope, i.e., functions within functions.
3. **Global**: The top-level scope, which includes variables defined at the module level.
4. **Built-in**: The built-in scope, which includes built-in functions and exceptions.
'''
#### Example:

x = "global"

def outer_function():
    x = "enclosing"

    def inner_function():
        x = "local"
        print(x)  # Local scope

    inner_function()
    print(x)  # Enclosing scope

outer_function()
print(x)  # Global scope

#### Output:
'''
local
enclosing
global
'''
