'''In Python, inheritance allows a class (child class) to inherit attributes and methods
 from another class (parent class). There are several types of inheritance:
'''

'''
1. **Single Inheritance**
2. **Multiple Inheritance**
3. **Multilevel Inheritance**
4. **Hierarchical Inheritance**
5. **Hybrid Inheritance**
'''


### 1. Single Inheritance

'''
In single inheritance, a child class inherits from a single parent class.
'''

#### Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks

### 2. Multiple Inheritance
'''
In multiple inheritance, a child class inherits from more than one parent class.
'''

#### Example:

class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()   # Output: Can fly
duck.swim()  # Output: Can swim

### 3. Multilevel Inheritance
'''
In multilevel inheritance, a child class inherits from another child class, creating
 a chain of inheritance.
'''
#### Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.walk()   # Output: Mammal walks
dog.bark()   # Output: Dog barks

### 4. Hierarchical Inheritance
'''
In hierarchical inheritance, multiple child classes inherit from a single parent class.
'''

#### Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks

cat = Cat()
cat.speak()  # Output: Animal speaks
cat.meow()   # Output: Cat meows

### 5. Hybrid Inheritance
'''
Hybrid inheritance is a combination of two or more types of inheritance.
'''
#### Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Bird(Animal):
    def fly(self):
        print("Bird flies")

class Bat(Mammal, Bird):
    pass

bat = Bat()
bat.speak()  # Output: Animal speaks
bat.walk()   # Output: Mammal walks
bat.fly()    # Output: Bird flies

### Summary
'''
- **Single Inheritance**: Child class inherits from a single parent class.
- **Multiple Inheritance**: Child class inherits from multiple parent classes.
- **Multilevel Inheritance**: Child class inherits from another child class, forming a chain.
- **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.
- **Hybrid Inheritance**: Combination of two or more types of inheritance.
'''