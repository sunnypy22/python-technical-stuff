# Method 1: Iterative Multiplication

def power_iterative(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage
base = 2
exponent = 10
print(power_iterative(base, exponent))  # Output: 1024

# Method 2: Recursive Approach

def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)

# Example usage
base = 2
exponent = 10
print(power_recursive(base, exponent))  # Output: 1024

# Method 3: Recursive Approach with Memoization

def power_recursive_memo(base, exponent, memo=None):
    if memo is None:
        memo = {}
    if exponent in memo:
        return memo[exponent]
    if exponent == 0:
        return 1
    memo[exponent] = base * power_recursive_memo(base, exponent - 1, memo)
    return memo[exponent]

# Example usage
base = 2
exponent = 10
print(power_recursive_memo(base, exponent))  # Output: 1024

# Method 4: Binary Exponentiation (Exponentiation by Squaring)

def power_binary_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

# Example usage
base = 2
exponent = 10
print(power_binary_exponentiation(base, exponent))  # Output: 1024

# Method 5: Using a Lambda Function with Reduce (Functional Programming Approach)

from functools import reduce

def power_lambda_reduce(base, exponent):
    return reduce(lambda x, y: x * y, [base] * exponent, 1)

# Example usage
base = 2
exponent = 10
print(power_lambda_reduce(base, exponent))  # Output: 1024
