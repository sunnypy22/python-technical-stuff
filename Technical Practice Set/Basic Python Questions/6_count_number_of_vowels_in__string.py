### 1. Using a For Loop

def count_vowels_loop(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels_loop("Hello World")) 

### 2. Using a List Comprehension

def count_vowels_comprehension(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels_comprehension("Hello World"))  

### 3. Using `filter()` and `lambda`

def count_vowels_filter(s):
    return len(list(filter(lambda char: char.lower() in 'aeiou', s)))

print(count_vowels_filter("Hello World")) 

### 4. Using `str.count()`

def count_vowels_count(s):
    return sum(s.lower().count(vowel) for vowel in 'aeiou')

print(count_vowels_count("Hello World")) 

### 5. Using Regular Expressions

import re

def count_vowels_regex(s):
    return len(re.findall(r'[aeiouAEIOU]', s))

print(count_vowels_regex("Hello World")) 

### 6. Using `collections.Counter`

from collections import Counter

def count_vowels_counter(s):
    count = Counter(s.lower())
    return sum(count[vowel] for vowel in 'aeiou')

print(count_vowels_counter("Hello World")) 

### 7. Using `reduce()` from `functools`

from functools import reduce

def count_vowels_reduce(s):
    return reduce(lambda acc, char: acc + (char.lower() in 'aeiou'), s, 0)

print(count_vowels_reduce("Hello World")) 

### 8. Using `map()`

def count_vowels_map(s):
    return sum(map(s.lower().count, 'aeiou'))

print(count_vowels_map("Hello World")) 

### 9. Using Numpy
import numpy as np

def count_vowels_numpy(s):
    return np.sum([char in 'aeiouAEIOU' for char in s])

print(count_vowels_numpy("Hello World")) 

### 10. Using Generator Expression

def count_vowels_generator(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels_generator("Hello World")) 