### 1. Using the `+` Operator
def concatenate_plus(list1, list2):
    return list1 + list2

print(concatenate_plus([1, 2, 3], [4, 5, 6]))

### 2. Using `extend()` Method
def concatenate_extend(list1, list2):
    list1_copy = list1.copy()
    list1_copy.extend(list2)
    return list1_copy

print(concatenate_extend([1, 2, 3], [4, 5, 6])) 

### 3. Using List Comprehension
def concatenate_comprehension(list1, list2):
    return [item for item in list1] + [item for item in list2]

print(concatenate_comprehension([1, 2, 3], [4, 5, 6])) 

### 4. Using `itertools.chain()`
import itertools

def concatenate_itertools(list1, list2):
    return list(itertools.chain(list1, list2))

print(concatenate_itertools([1, 2, 3], [4, 5, 6])) 

### 5. Using `*` Operator (Unpacking)
def concatenate_unpacking(list1, list2):
    return [*list1, *list2]

print(concatenate_unpacking([1, 2, 3], [4, 5, 6]))  

### 6. Using `reduce()` from `functools`
from functools import reduce

def concatenate_reduce(list1, list2):
    return reduce(lambda x, y: x + y, [list1, list2])

print(concatenate_reduce([1, 2, 3], [4, 5, 6])) 

### 7. Using `numpy.concatenate()`
import numpy as np

def concatenate_numpy(list1, list2):
    return np.concatenate((list1, list2)).tolist()

print(concatenate_numpy([1, 2, 3], [4, 5, 6]))  

### 8. Using `collections.deque`

from collections import deque

def concatenate_deque(list1, list2):
    return list(deque(list1) + deque(list2))

print(concatenate_deque([1, 2, 3], [4, 5, 6])) 

### 9. Using a For Loop
def concatenate_loop(list1, list2):
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result

print(concatenate_loop([1, 2, 3], [4, 5, 6]))  

### 10. Using `append()` Method in a Loop
def concatenate_append(list1, list2):
    result = list1.copy()
    for item in list2:
        result.append(item)
    return result

print(concatenate_append([1, 2, 3], [4, 5, 6])) 