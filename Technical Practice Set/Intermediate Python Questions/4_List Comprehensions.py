# Basic List Comprehension

# Example: Squaring numbers in a list
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List Comprehension with Condition

# Example: Filtering even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Nested List Comprehension

# Example: Creating a multiplication table
table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(table)
# Output: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
