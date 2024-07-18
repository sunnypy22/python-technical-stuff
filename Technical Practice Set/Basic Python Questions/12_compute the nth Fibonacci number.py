# 1. Recursive Approach

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(10))  # Output: 55


# 2. Iterative Approach

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_iterative(10))  # Output: 55

# 3. Dynamic Programming with Memoization (Top-Down)


def fibonacci_memoization(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

print(fibonacci_memoization(10))  # Output: 55

# 4. Dynamic Programming with Tabulation (Bottom-Up)

def fibonacci_tabulation(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print(fibonacci_tabulation(10))  # Output: 55


# 5. Using Matrix Exponentiation

import numpy as np

def fibonacci_matrix(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    F = np.matrix([[1, 1], [1, 0]], dtype=object)
    result = np.linalg.matrix_power(F, n-1)
    return result[0, 0]

print(fibonacci_matrix(10))  # Output: 55
