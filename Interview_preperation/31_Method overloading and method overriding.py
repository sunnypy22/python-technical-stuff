'''Method overloading and method overriding are important concepts in 
object-oriented programming that deal with how methods in classes can 
be used and extended. Here’s a detailed explanation of both concepts:
'''

### Method Overloading

'''
**Definition**: Method overloading allows a class to have more than one 
method with the same name but different parameters (i.e., different numbers or
 types of arguments). This feature is often found in statically-typed languages
   like Java or C++. 

**Python Context**: Python does not support traditional method overloading 
like some other languages. Instead, Python supports default arguments and 
variable-length argument lists to achieve similar functionality.
'''

# **Examples**:

# 1. **Using Default Arguments**:
class Math:
    def add(self, a, b, c=0):
        return a + b + c

math = Math()
print(math.add(2, 3))        # Output: 5 (c is default to 0)
print(math.add(2, 3, 4))     # Output: 9

# 2. **Using `*args` and `**kwargs`**:
class Math:
    def add(self, *args):
        return sum(args)

math = Math()
print(math.add(1, 2))        # Output: 3
print(math.add(1, 2, 3, 4))  # Output: 10

'''
**Key Points**:
- Python handles method overloading by using default arguments or variable-length 
argument lists.
- Multiple methods with the same name but different parameter lists are not allowed.
'''


### Method Overriding

'''
**Definition**: Method overriding occurs when a subclass provides a specific implementation 
    of a method that is already defined in its superclass. This allows a subclass to 
    modify or extend the behavior of methods inherited from its superclass.

**Usage**: Method overriding is used to implement specific functionality in subclasses
 while maintaining a consistent interface with the superclass.
'''

# **Example**:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
'''
# **Output**:
Dog barks
Cat meows
'''

'''
**Key Points**:
- In method overriding, the method in the subclass has the same name and signature as the
     method in the superclass.
- You can use the `super()` function to call the method from the superclass if needed.
'''

'''
- **Method Overloading**:
  - Allows multiple methods with the same name but different parameter lists.
  - Python does not support traditional method overloading; instead, it uses default
     arguments and variable-length argument lists to achieve similar results.

- **Method Overriding**:
  - Occurs when a subclass provides a specific implementation of a method that is already
     defined in its superclass.
  - Used to modify or extend the behavior of inherited methods.
  - The subclass method has the same name and parameters as the superclass method.
'''