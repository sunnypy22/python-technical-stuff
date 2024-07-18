# 1. Using Built-in max() Function

def max_of_three(a, b, c):
    return max(a, b, c)

# Example usage
result = max_of_three(5, 9, 3)
print("Maximum of the three numbers is:", result)  # Output: Maximum of the three numbers is: 9

# 2. Using Conditional Statements

def max_of_three_conditional(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
result = max_of_three_conditional(5, 9, 3)
print("Maximum of the three numbers is:", result)  # Output: Maximum of the three numbers is: 9

# 3. Using the sorted() Function

def max_of_three_sorted(a, b, c):
    return sorted([a, b, c])[-1]

# Example usage
result = max_of_three_sorted(5, 9, 3)
print("Maximum of the three numbers is:", result)  # Output: Maximum of the three numbers is: 9
