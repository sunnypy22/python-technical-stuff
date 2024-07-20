'''In Python, a class can contain both methods and attributes. 
Let's define these terms and explore their differences and uses with examples.
'''
### Attributes
'''
Attributes are variables that belong to an object or class. 
They are used to store data related to the objects of the class.
'''
#### Types of Attributes:
'''
1. **Instance Attributes**: Attributes that are specific to an instance (object) of a class.
2. **Class Attributes**: Attributes that are shared by all instances of a class.
'''
#### Example of Attributes:

class Car:
    # Class attribute
    wheels = 4
    
    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model

# Creating an object of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing instance attributes
print(car1.make)  # Output: Toyota
print(car2.model) # Output: Civic

# Accessing class attribute
print(car1.wheels) # Output: 4
print(car2.wheels) # Output: 4

# Modifying class attribute for all instances
Car.wheels = 5
print(car1.wheels) # Output: 5
print(car2.wheels) # Output: 5

### Methods
'''
Methods are functions that belong to a class. They define behaviors or
 actions that objects of the class can perform.
'''
#### Types of Methods:
'''
1. **Instance Methods**: Methods that operate on instance attributes. 
    They require a reference to the instance (`self`) as the first parameter.
2. **Class Methods**: Methods that operate on class attributes. 
    They require a reference to the class (`cls`) as the first parameter.
3. **Static Methods**: Methods that do not operate on instance or class attributes. 
    They don't require a reference to `self` or `cls`.
'''
#### Example of Methods:

class Car:
    # Class attribute
    wheels = 4
    
    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model
    
    # Instance method
    def description(self):
        return f"{self.make} {self.model} with {self.wheels} wheels"
    
    # Class method
    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels
    
    # Static method
    @staticmethod
    def honk():
        return "Honk! Honk!"

# Creating an object of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing instance method
print(car1.description())  # Output: Toyota Camry with 4 wheels
print(car2.description())  # Output: Honda Civic with 4 wheels

# Accessing class method
Car.change_wheels(6)
print(car1.description())  # Output: Toyota Camry with 6 wheels
print(car2.description())  # Output: Honda Civic with 6 wheels

# Accessing static method
print(Car.honk())  # Output: Honk! Honk!

### Summary
'''
- **Attributes**: Variables that store data related to objects of the class.
  - **Instance Attributes**: Specific to an instance of the class.
  - **Class Attributes**: Shared by all instances of the class.

- **Methods**: Functions that define behaviors or actions of objects of the class.
  - **Instance Methods**: Operate on instance attributes and require `self`.
  - **Class Methods**: Operate on class attributes and require `cls`.
  - **Static Methods**: Do not operate on instance or class attributes and do 
  not require `self` or `cls`.
'''