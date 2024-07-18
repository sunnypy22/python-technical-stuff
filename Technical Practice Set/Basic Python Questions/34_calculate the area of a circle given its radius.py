# 1. Using Python's Math Module

'''You can calculate the area of a circle directly using Python's math module,
 which provides the pi constant and basic mathematical operations'''


import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

# Example usage
radius = 5
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {area}")

# 2. Using a Custom Constant for Pi

'''If you prefer to define the value of pi explicitly without importing from math,
 you can define it as a constant in your code.'''

PI = 3.14159  # Define your own constant for pi

def area_of_circle(radius):
    return PI * (radius ** 2)

# Example usage
radius = 5
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {area}")

# 3. Using a Lambda Function

'''For a more concise approach, you can use a lambda function to 
calculate the area of a circle.'''

area_of_circle = lambda radius: math.pi * (radius ** 2)

# Example usage
radius = 5
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {area}")
