# 1. Using Integer Square Root Comparison

import math

def is_perfect_square(num):
    if num < 0:
        return False
    root = math.isqrt(num)  # Integer square root
    return root * root == num

# Example usage
number1 = 16
number2 = 18

print(f"Is {number1} a perfect square? {is_perfect_square(number1)}")  # True (4*4 = 16)
print(f"Is {number2} a perfect square? {is_perfect_square(number2)}")  # False

# 2. Using Math Module Functions

import math

def is_perfect_square(num):
    if num < 0:
        return False
    root = math.sqrt(num)
    return root.is_integer()  # Check if the square root is an integer

# Example usage
number1 = 16
number2 = 18

print(f"Is {number1} a perfect square? {is_perfect_square(number1)}")  # True (4*4 = 16)
print(f"Is {number2} a perfect square? {is_perfect_square(number2)}")  # False
