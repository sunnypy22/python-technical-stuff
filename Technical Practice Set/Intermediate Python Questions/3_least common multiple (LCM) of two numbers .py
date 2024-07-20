# Method 1: Using the Greatest Common Divisor (GCD)

'''
The relationship between GCD and LCM can be used:
LCM(a,b)= |a*b|/GCD(a,b)
'''

import math

def lcm_using_gcd(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage
a = 12
b = 18
print("LCM using GCD:", lcm_using_gcd(a, b))

# Method 2: Using a loop to find the LCM

def lcm_using_loop(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

# Example usage
a = 12
b = 18
print("LCM using loop:", lcm_using_loop(a, b))

# Method 3: Using the Least Common Multiple formula with prime factorization

from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def lcm_using_prime_factors(a, b):
    a_factors = Counter(prime_factors(a))
    b_factors = Counter(prime_factors(b))
    lcm_factors = a_factors | b_factors

    lcm = 1
    for factor, power in lcm_factors.items():
        lcm *= factor ** power

    return lcm

# Example usage
a = 12
b = 18
print("LCM using prime factors:", lcm_using_prime_factors(a, b))

# Method 4: Using numpy (External Library)

import numpy as np

def lcm_using_numpy(a, b):
    return np.lcm(a, b)

# Example usage
a = 12
b = 18
print("LCM using numpy:", lcm_using_numpy(a, b))
