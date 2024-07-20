'''Magic methods in Python, also known as dunder (double underscore) methods, 
are special methods that are predefined in Python. 
They are called automatically when specific operations are performed on objects. 
These methods allow objects to implement or emulate certain behaviors and can
 be overridden to customize these behaviors.
'''
### Common Magic Methods

'''
1. **__init__(self, ...)**: Constructor method for initializing new objects.
2. **__str__(self)**: Defines the string representation of an object, used by `str()`.
3. **__repr__(self)**: Defines the "official" string representation of an object, used by `repr()`.
4. **__len__(self)**: Called by `len()`.
5. **__getitem__(self, key)**: Called to retrieve an item.
6. **__setitem__(self, key, value)**: Called to set an item.
7. **__delitem__(self, key)**: Called to delete an item.
8. **__iter__(self)**: Called when an iterator is required for a container.
9. **__next__(self)**: Returns the next item from an iterator.
10. **__contains__(self, item)**: Called to implement membership test operators (`in` and `not in`).
'''
### Arithmetic Magic Methods

'''
1. **__add__(self, other)**: Implements addition (`+`).
2. **__sub__(self, other)**: Implements subtraction (`-`).
3. **__mul__(self, other)**: Implements multiplication (`*`).
4. **__truediv__(self, other)**: Implements true division (`/`).
5. **__floordiv__(self, other)**: Implements floor division (`//`).
6. **__mod__(self, other)**: Implements modulo (`%`).
7. **__pow__(self, other)**: Implements exponentiation (`**`).
8. **__lt__(self, other)**: Implements less than (`<`).
9. **__le__(self, other)**: Implements less than or equal to (`<=`).
10. **__eq__(self, other)**: Implements equal to (`==`).
11. **__ne__(self, other)**: Implements not equal to (`!=`).
12. **__gt__(self, other)**: Implements greater than (`>`).
13. **__ge__(self, other)**: Implements greater than or equal to (`>=`).
'''

### Example Usage

#### 1. __init__, __str__, and __repr__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):
        return f"Person({self.name!r}, {self.age!r})"

p = Person("Alice", 30)
print(str(p))  # Output: Person(name=Alice, age=30)
print(repr(p)) # Output: Person('Alice', 30)

#### 2. __add__ and __mul__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)
print(v1 * 3)   # Output: Vector(6, 9)

#### 3. __getitem__, __setitem__, and __delitem__

class CustomList:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]
    
    def __repr__(self):
        return repr(self.items)

cl = CustomList()
cl.items = [1, 2, 3, 4]
print(cl[1])    # Output: 2
cl[1] = 20
print(cl)       # Output: [1, 20, 3, 4]
del cl[1]
print(cl)       # Output: [1, 3, 4]