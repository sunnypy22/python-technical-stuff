'''
In Python, `@staticmethod`, `@classmethod`, and `@property` are decorators 
    used to define methods within a class. Each serves a different purpose and 
    provides distinct functionality for how methods interact with class instances and
      class data. Here’s a detailed overview of each:
'''
### 1. `@staticmethod`
'''
- **Purpose**: Defines a method that does not require access to the instance (`self`) 
    or the class (`cls`). It behaves like a regular function but belongs to the class’s 
    namespace.
- **Usage**: Used when you want a method that performs a function related to the class
     but does not need to access or modify class or instance-specific data.
'''

# **Example:**

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Usage
result = MathUtils.add(5, 3)
print(result)  # Output: 8
'''
**Key Points:**
- `@staticmethod` methods do not receive an implicit first argument 
    (neither `self` nor `cls`).
- They can be called on the class itself or on an instance.

### 2. `@classmethod`

- **Purpose**: Defines a method that receives the class (`cls`) as its first argument,
     instead of the instance (`self`). This allows the method to access and modify
         class-level attributes and methods.
- **Usage**: Used for factory methods that instantiate objects using different parameters
     or to modify class-level data.
'''
# **Example:**

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def create_person(cls, name):
        return cls(name)

    @classmethod
    def get_population(cls):
        return cls.population

# Usage
person1 = Person.create_person("Alice")
print(person1.name)  # Output: Alice
print(Person.get_population())  # Output: 1
'''
**Key Points:**
- `@classmethod` methods receive `cls` as their first argument, which represents the 
    class and not the instance.
- They can modify class state and are often used for factory methods.
'''

### 3. `@property`
'''
- **Purpose**: Defines a method that can be accessed like an attribute. It allows you
     to define a method that is accessed with dot notation but behaves like a data attribute.
- **Usage**: Used to control access to instance attributes and to provide read-only 
    attributes or computed properties.
'''

# **Example:**

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)

# Usage
circle = Circle(5)
print(circle.radius)  # Output: 5
print(circle.area)    # Output: 78.53981633974483

circle.radius = 10
print(circle.area)    # Output: 314.1592653589793
'''
**Key Points:**
- `@property` allows a method to be accessed like an attribute, providing a 
    way to implement getters, setters, and deleters.
- Use `@property` for read-only attributes and `@attribute_name.setter` for writable
     attributes.
'''
### Summary

'''
- **`@staticmethod`**: For methods that don’t need access to class or instance data.
     Called on the class or instance.
- **`@classmethod`**: For methods that need to access or modify class state.
     Receives the class (`cls`) as the first argument.
- **`@property`**: For methods that should be accessed like attributes, providing controlled
     access to instance attributes with optional setters and deleters.
'''