'''Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" 
to design software. 
It involves organizing code into reusable and related units called classes and objects. 
'''

### Core Concepts of OOP

'''
1. **Class**
2. **Object**
3. **Inheritance**
4. **Encapsulation**
5. **Polymorphism**
6. **Abstraction**
'''

### 1. Class
'''
A class is a blueprint for creating objects. 
It defines a set of attributes and methods that the objects created from the class can have.
'''
#### Example:

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

### 2. Object
'''
An object is an instance of a class. 
It is created using the class and can have its own unique attributes and behaviors.
'''
#### Example:

dog = Animal("Dog")
print(dog.name)  # Output: Dog

### 3. Inheritance
'''
Inheritance allows a class to inherit attributes and methods from another class.
 This promotes code reusability.
'''
#### Example:

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

#### Usage:

dog = Dog("Dog")
cat = Cat("Cat")
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

### 4. Encapsulation
'''
Encapsulation restricts access to certain components of an object, 
which can prevent the accidental modification of data. 
It is achieved by using private and protected access modifiers.
'''
#### Example:

class Car:
    def __init__(self, make, model):
        self._make = make          # Protected attribute
        self.__model = model       # Private attribute
    
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

#### Usage:

car = Car("Toyota", "Camry")
print(car._make)         # Output: Toyota
print(car.get_model())   # Output: Camry

### 5. Polymorphism
'''
Polymorphism allows methods to be used interchangeably between different classes that
 share the same method name. It allows objects of different types
   to be treated as objects of a common super type.
'''
#### Example:

class Bird:
    def fly(self):
        return "Bird is flying"
    
class Airplane:
    def fly(self):
        return "Airplane is flying"

def make_it_fly(flying_object):
    return flying_object.fly()

#### Usage:

bird = Bird()
airplane = Airplane()
print(make_it_fly(bird))      # Output: Bird is flying
print(make_it_fly(airplane))  # Output: Airplane is flying

### 6. Abstraction
'''
Abstraction hides complex implementation details and shows only the necessary
 features of an object. It is achieved using abstract classes and interfaces.
'''
#### Example:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

#### Usage:

rectangle = Rectangle(5, 10)
print(rectangle.area())  # Output: 50

### Summary
'''
Object-Oriented Programming (OOP) is a powerful way to structure and organize code
 by bundling related properties and behaviors into individual objects.

- **Class**: Blueprint for creating objects with attributes and methods.
- **Object**: Instance of a class.
- **Inheritance**: Mechanism to create a new class using details of an existing class
     without modifying it.
- **Encapsulation**: Restriction of direct access to some of an object's components.
- **Polymorphism**: Ability to process objects differently based on their data type or class.
- **Abstraction**: Hiding the internal implementation and showing only the necessary parts.
'''