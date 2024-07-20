# Basic Set Comprehension

# Example: Creating a set of squares
squares_set = {x**2 for x in range(10)}
print(squares_set)
# Output: {0, 1, 64, 4, 36, 9, 16, 81, 49, 25}

# Set Comprehension with Condition

# Example: Filtering set to keep only even squares
even_squares_set = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares_set)
# Output: {0, 64, 4, 36, 16}
