'''In Python, `__init__.py` and `__all__` serve different but important roles
 in managing modules and packages. Here’s an explanation of each:
'''

### `__init__.py`

'''
The `__init__.py` file is used to mark a directory as a Python package. 
When a directory contains an `__init__.py` file, it becomes a package, and you can
 import modules and sub-packages from it.
'''

#### Purpose of `__init__.py`:

'''
1. **Package Initialization**: It can contain initialization code for the package.
2. **Namespace Control**: It can define what symbols the package exposes to the outside world.
3. **Sub-Package Imports**: It can import modules or sub-packages to make them available when the package is imported.
'''

#### Example of `__init__.py`:

# mypackage/__init__.py

'''
__all__ = ['module1', 'module2']

from .module1 import foo
from .module2 import bar
'''

'''
This example defines the `__all__` attribute to specify the public interface of the
 package, which includes `module1` and `module2`. 
 It also imports `foo` from `module1` and `bar` from `module2` to make them
   available when the package is imported.
'''
### `__all__`

'''
The `__all__` attribute is a list of strings defining the public interface of
 a module or package. It specifies which attributes or modules should be
   imported when `from module import *` or `from package import *` is used.
'''
#### Example of `__all__` in a module:

# mymodule.py

__all__ = ['greet', 'add']

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def _private_function():
    return "This is a private function"

'''
In this example, the `__all__` list specifies that only the `greet` and `add`
 functions should be imported when using `from mymodule import *`. 
 The `_private_function` is excluded from this list and will not be imported.
'''
### Using `__init__.py` and `__all__` Together

'''
When combining these two features, `__init__.py` can use `__all__` to control the public interface of the entire package, while each module within the package can use its own `__all__` to control its own public interface.
'''

#### Directory Structure:

'''
mypackage/
    __init__.py
    module1.py
    module2.py
'''

##### Example: `mypackage/__init__.py`

# mypackage/__init__.py

'''
__all__ = ['module1', 'module2']

from .module1 import foo
from .module2 import bar
'''

##### Example: `mypackage/module1.py`

# mypackage/module1.py

__all__ = ['foo']

def foo():
    return "foo from module1"

def _private():
    return "This is a private function in module1"

##### Example: `mypackage/module2.py`

# mypackage/module2.py

__all__ = ['bar']

def bar():
    return "bar from module2"

def _private():
    return "This is a private function in module2"

#### Usage:

# main.py
'''
from mypackage import *

print(module1.foo())  # Output: foo from module1
print(module2.bar())  # Output: bar from module2

try:
    print(module1._private())
except AttributeError as e:
    print(e)  # Output: 'module' object has no attribute '_private'

try:
    print(module2._private())
except AttributeError as e:
    print(e)  # Output: 'module' object has no attribute '_private'
'''

### Summary
'''
- **`__init__.py`**: Marks a directory as a Python package, can contain initialization
         code, and helps manage the package namespace.
- **`__all__`**: Specifies the public interface of a module or package, 
    controlling what is imported with `from module import *` or `from package import *`.
'''

'''
By using `__init__.py` and `__all__` appropriately, you can create well-organized, 
    maintainable, and easy-to-use Python packages.
'''