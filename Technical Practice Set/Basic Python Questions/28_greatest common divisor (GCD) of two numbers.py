# 1. Using the Euclidean Algorithm (Iterative Approach)

def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage
num1 = 24
num2 = 36
result = gcd_euclidean(num1, num2)
print(f"GCD of {num1} and {num2} is:", result)  # Output: GCD of 24 and 36 is: 12

# 2. Using Python's math Module

import math

def gcd_math(a, b):
    return math.gcd(a, b)

# Example usage
num1 = 24
num2 = 36
result = gcd_math(num1, num2)
print(f"GCD of {num1} and {num2} is:", result)  # Output: GCD of 24 and 36 is: 12
