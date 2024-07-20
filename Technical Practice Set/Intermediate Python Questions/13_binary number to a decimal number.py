# Method 1: Using Python's Built-in Functions

'''1. Using int() Function
'''

binary_str = '1010'
decimal_number = int(binary_str, 2)
print(decimal_number)  # Output: 10

# Method 2: Manual Conversion Using a Loop

'''1. Manual Calculation
'''

def binary_to_decimal(binary_str):
    decimal_number = 0
    length = len(binary_str)
    for i, digit in enumerate(binary_str):
        if digit == '1':
            decimal_number += 2 ** (length - i - 1)
    return decimal_number

# Example usage
binary_str = '1010'
print(binary_to_decimal(binary_str))  # Output: 10

# Method 3: Using bin() and int() with Base Conversion

'''1. Using Binary Conversion
'''

decimal_number = 10
binary_str = bin(decimal_number)[2:]  # '1010'
print(binary_str)  # Output: '1010'

# Convert back to decimal
converted_decimal = int(binary_str, 2)
print(converted_decimal)  # Output: 10

# Method 4: Using Recursion

'''1. Recursive Approach
'''

def binary_to_decimal_recursive(binary_str):
    if len(binary_str) == 0:
        return 0
    else:
        return (int(binary_str[0]) * 2 ** (len(binary_str) - 1) +
                binary_to_decimal_recursive(binary_str[1:]))

# Example usage
binary_str = '1010'
print(binary_to_decimal_recursive(binary_str))  # Output: 10

# Method 5: Using numpy Library

'''1. Using numpy's binary_repr
'''
import numpy as np

binary_str = '1010'
decimal_number = int(binary_str, 2)
print(decimal_number)  # Output: 10


# Method 6: Using List Comprehension

'''1. List Comprehension Approach
'''

def binary_to_decimal_list_comprehension(binary_str):
    return sum([int(bit) * 2 ** idx for idx, bit in enumerate(reversed(binary_str))])

# Example usage
binary_str = '1010'
print(binary_to_decimal_list_comprehension(binary_str))  # Output: 10
