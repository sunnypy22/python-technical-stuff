### 1. Using a For Loop

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(5)) 

### 2. Using Recursion

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  

### 3. Using the `math` Library

import math

def factorial_math(n):
    return math.factorial(n)

print(factorial_math(5)) 

### 4. Using `reduce()` from `functools`

from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(factorial_reduce(5)) 

### 5. Using `numpy` Library

import numpy as np

def factorial_numpy(n):
    return np.prod(np.arange(1, n + 1))
print(factorial_numpy(5)) 

### 6. Using a While Loop

def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print(factorial_while(5)) 

### 7. Using Memoization (to optimize recursion)

def factorial_memoization(n, memo={0: 1, 1: 1}):
    if n not in memo:
        memo[n] = n * factorial_memoization(n - 1, memo)
    return memo[n]

print(factorial_memoization(5)) 

### 8. Using Itertools (Product)


import itertools

def factorial_itertools(n):
    if n == 0:
        return 1
    return itertools.accumulate(range(1, n + 1), lambda x, y: x * y).__reduce__()[-1]

print(factorial_itertools(5))