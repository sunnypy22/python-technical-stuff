### 1. Using a For Loop
def is_prime_loop(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime_loop(29))  

### 2. Using a Recursive Function
def is_prime_recursive(n, divisor=None):
    if divisor is None:
        divisor = int(n**0.5)
    if n <= 1:
        return False
    if divisor < 2:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

print(is_prime_recursive(29)) 

### 3. Using List Comprehension

def is_prime_comprehension(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

print(is_prime_comprehension(29)) 
### 4. Using `filter()` and `lambda`
def is_prime_filter(n):
    if n <= 1:
        return False
    return not any(filter(lambda x: n % x == 0, range(2, int(n**0.5) + 1)))

print(is_prime_filter(29)) 

### 5. Using Sieve of Eratosthenes (to generate primes up to n)
def sieve_of_eratosthenes(n):
    if n <= 1:
        return False
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve[n]

print(sieve_of_eratosthenes(29))  

### 6. Using Numpy (Not common for prime checking but possible)
import numpy as np

def is_prime_numpy(n):
    if n <= 1:
        return False
    return np.all(n % np.arange(2, int(np.sqrt(n)) + 1))

print(is_prime_numpy(29))

### 7. Using a While Loop
def is_prime_while(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime_while(29))  

### 8. Using `sympy` Library
from sympy import isprime

def is_prime_sympy(n):
    return isprime(n)

print(is_prime_sympy(29))  

### 9. Using `all()` with a generator expression
def is_prime_all(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_prime_all(29)) 

### 10. Using `reduce()` from `functools`
from functools import reduce

def is_prime_reduce(n):
    if n <= 1:
        return False
    return reduce(lambda x, y: x and n % y != 0, range(2, int(n**0.5) + 1), True)

print(is_prime_reduce(29)) 