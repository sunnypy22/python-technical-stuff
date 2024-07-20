'''In Python, variables and constants are used to store data that can be used
 and manipulated throughout a program. 
'''

### Variables
'''
A variable in Python is a symbolic name that refers to a value. 
This value can be changed during the execution of a program. 
Variables are created by assigning a value to a name using the `=` operator.
'''

#### Characteristics of Variables:
'''
- They can store different types of data (integers, floats, strings, lists, etc.).
- They can change value throughout the program.
- Variable names are case-sensitive.
'''

#### Example:

# Creating variables
x = 10        # Integer
y = 3.14      # Float
name = "Alice"  # String

# Printing variables
print(x)       # Output: 10
print(y)       # Output: 3.14
print(name)    # Output: Alice

# Changing the value of a variable
x = 20
print(x)       # Output: 20


### Constants
'''
A constant is a type of variable whose value cannot be changed. 
In Python, there is no built-in constant type, but by convention, 
constants are usually defined using all uppercase letters. 
This is a convention and not enforced by the Python interpreter.
'''

#### Characteristics of Constants:
'''
- They are meant to remain unchanged throughout the program.
- They are typically declared at the beginning of the script or module.
'''

#### Example:

# Defining constants
PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458

# Printing constants
print(PI)              # Output: 3.14159
print(GRAVITY)         # Output: 9.8
print(SPEED_OF_LIGHT)  # Output: 299792458

### Differences Between Variables and Constants

'''
- **Mutability**: The value of a variable can change, 
        while a constant’s value should remain the same.
- **Naming Convention**: Variables typically use lowercase letters 
        and may use underscores (e.g., `variable_name`), while constants 
        use uppercase letters with underscores (e.g., `CONSTANT_NAME`).
'''

### Best Practices

'''
1. **Naming Variables and Constants**:
   - Use meaningful names that describe the data they hold.
   - Follow the naming conventions (snake_case for variables and UPPERCASE for constants).

2. **Scope**:
   - Variables and constants defined within a function are local to that function.
   - Variables and constants defined outside any function are global.

3. **Documentation**:
   - Add comments to explain the purpose of variables and constants, especially if they hold complex or important data.
'''
### Example: Using Variables and Constants in a Program

'''
Here’s an example of how variables and constants can be used together in a program:
'''
# Constants
PI = 3.14159
EARTH_RADIUS_KM = 6371.0

# Variables
radius = 5
height = 10

# Calculate the volume of a cylinder
volume = PI * radius ** 2 * height

# Calculate the circumference of the Earth
earth_circumference = 2 * PI * EARTH_RADIUS_KM

# Print results
print("Volume of the cylinder:", volume)  # Output: Volume of the cylinder: 785.3975
print("Circumference of the Earth:", earth_circumference, "km")  # Output: Circumference of the Earth: 40030.173592 km
