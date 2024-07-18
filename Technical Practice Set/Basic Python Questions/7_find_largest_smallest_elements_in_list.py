### 1. Using Built-in `max()` and `min()` Functions
def find_max_min_builtin(lst):
    return max(lst), min(lst)

print(find_max_min_builtin([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

### 2. Using a For Loop
def find_max_min_loop(lst):
    max_element = lst[0]
    min_element = lst[0]
    for num in lst[1:]:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num
    return max_element, min_element

print(find_max_min_loop([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  

### 3. Using Sorting (Not Efficient for Large Lists)
def find_max_min_sort(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-1], sorted_lst[0]

print(find_max_min_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 4. Using List Comprehension
def find_max_min_comprehension(lst):
    return max([num for num in lst]), min([num for num in lst])

print(find_max_min_comprehension([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  

### 5. Using `reduce()` from `functools`
from functools import reduce

def find_max_min_reduce(lst):
    max_element = reduce(lambda a, b: a if a > b else b, lst)
    min_element = reduce(lambda a, b: a if a < b else b, lst)
    return max_element, min_element

print(find_max_min_reduce([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  

### 6. Using `heapq` for Finding N Largest and N Smallest Elements
import heapq

def find_max_min_heapq(lst):
    max_element = heapq.nlargest(1, lst)[0]
    min_element = heapq.nsmallest(1, lst)[0]
    return max_element, min_element

print(find_max_min_heapq([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 7. Using Numpy
import numpy as np

def find_max_min_numpy(lst):
    np_lst = np.array(lst)
    return np_lst.max(), np_lst.min()

print(find_max_min_numpy([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  

### 8. Using `operator` Module

import operator

def find_max_min_operator(lst):
    max_element = reduce(operator.gt, lst)
    min_element = reduce(operator.lt, lst)
    return max_element, min_element

print(find_max_min_operator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  

### 9. Using `collections.Counter` (Not Typical but Interesting)
from collections import Counter

def find_max_min_counter(lst):
    counter = Counter(lst)
    max_element = max(counter.elements(), key=lambda x: x)
    min_element = min(counter.elements(), key=lambda x: x)
    return max_element, min_element

print(find_max_min_counter([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  

### 10. Using a Recursive Function
def find_max_min_recursive(lst, max_element=None, min_element=None):
    if not lst:
        return max_element, min_element
    current = lst[0]
    if max_element is None or current > max_element:
        max_element = current
    if min_element is None or current < min_element:
        min_element = current
    return find_max_min_recursive(lst[1:], max_element, min_element)

print(find_max_min_recursive([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 