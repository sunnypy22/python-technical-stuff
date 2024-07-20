# Basic Dictionary Comprehension

# Example: Creating a dictionary with squares of numbers
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Dictionary Comprehension with Condition

# Example: Filtering dictionary to keep only even squares
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
