'''Modules and packages are fundamental concepts in Python that help organize and manage code.
 They allow for the logical grouping of functionality and code reuse across 
 different parts of a program or even across multiple programs.
'''
### Modules
'''
A module is a single file containing Python code that can be imported and used in other
 Python programs. 
 Modules can contain definitions of functions, classes, and variables, as well as 
 runnable code.
'''
#### Creating a Module
'''
To create a module, simply save a Python file with a `.py` extension.
'''
##### Example: `mymodule.py`

# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

#### Importing a Module
'''
You can import a module using the `import` statement.
'''
##### Example:

# main.py

'''
import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.add(5, 3))       # Output: 8
'''

#### Importing Specific Functions or Variables
'''
You can import specific functions or variables from a module using the `from` keyword.
'''
##### Example:

# main.py
'''
from mymodule import greet, add

print(greet("Bob"))  # Output: Hello, Bob!
print(add(2, 3))     # Output: 5
'''



### Packages
'''
A package is a way of organizing related modules into a directory hierarchy. 
A package is a directory containing an `__init__.py` file 
and other module files. 
The `__init__.py` file can be empty but allows the directory to be recognized as a package.
'''
#### Creating a Package

##### Directory Structure:

'''
mypackage/
    __init__.py
    module1.py
    module2.py
'''


##### Example: `module1.py`

# module1.py

def foo():
    return "foo from module1"

##### Example: `module2.py`

# module2.py

def bar():
    return "bar from module2"

#### Importing from a Package
'''
You can import modules from a package using dot notation.
'''

##### Example:

# main.py

'''
from mypackage import module1, module2

print(module1.foo())  # Output: foo from module1
print(module2.bar())  # Output: bar from module2
'''

#### Importing Specific Functions or Variables from a Package Module

'''
You can import specific functions or variables from a module within a package.
'''

##### Example:

# main.py
'''
from mypackage.module1 import foo
from mypackage.module2 import bar

print(foo())  # Output: foo from module1
print(bar())  # Output: bar from module2
'''

### Namespaces

'''
Modules and packages create namespaces, 
which help avoid naming conflicts by encapsulating the code within distinct contexts.
'''
#### Example:

# mymodule.py
def function():
    return "Function from mymodule"

# anothermodule.py
def function():
    return "Function from anothermodule"

'''

# main.py
import mymodule
import anothermodule

print(mymodule.function())    # Output: Function from mymodule
print(anothermodule.function())  # Output: Function from anothermodule
'''


### Relative Imports


'''
When working within a package, you can use relative imports to import other
 modules from the same package.
'''
##### Example:

'''
# mypackage/module1.py
from .module2 import bar  # Relative import

def foo():
    return bar()

# mypackage/module2.py
def bar():
    return "bar from module2"
'''

#### Using the Package
'''
# main.py
from mypackage.module1 import foo

print(foo())  # Output: bar from module2

'''