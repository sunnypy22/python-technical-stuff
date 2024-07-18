### 1. Using Sorting

def second_largest_sort(lst):
    sorted_list = sorted(set(lst), reverse=True)
    if len(sorted_list) < 2:
        return None  # Edge case: list has less than 2 unique elements
    return sorted_list[1]

print(second_largest_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 2. Using Max() and Removing the Maximum Element

def second_largest_max(lst):
    max_value = max(lst)
    lst.remove(max_value)
    return max(lst) if lst else None

print(second_largest_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 3. Using Heapq Module

import heapq

def second_largest_heapq(lst):
    unique_list = list(set(lst))
    if len(unique_list) < 2:
        return None  # Edge case: list has less than 2 unique elements
    return heapq.nlargest(2, unique_list)[-1]

print(second_largest_heapq([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 4. Using a Single Pass

def second_largest_single_pass(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

print(second_largest_single_pass([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 5. Using List Comprehension and Max()

def second_largest_comprehension(lst):
    unique_list = list(set(lst))
    if len(unique_list) < 2:
        return None  # Edge case: list has less than 2 unique elements
    return max([x for x in unique_list if x != max(unique_list)])

print(second_largest_comprehension([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 6. Using Sort() and Negative Indexing

def second_largest_sort_index(lst):
    unique_list = sorted(set(lst))
    if len(unique_list) < 2:
        return None  # Edge case: list has less than 2 unique elements
    return unique_list[-2]

print(second_largest_sort_index([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 


### 8. Using `numpy.partition()`

import numpy as np

def second_largest_numpy(lst):
    if len(set(lst)) < 2:
        return None  # Edge case: list has less than 2 unique elements
    return np.partition(np.array(lst), -2)[-2]

print(second_largest_numpy([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

### 9. Using `collections.Counter`
from collections import Counter

def second_largest_counter(lst):
    count = Counter(lst)
    unique_values = sorted(count.keys(), reverse=True)
    if len(unique_values) < 2:
        return None  # Edge case: list has less than 2 unique elements
    return unique_values[1]

print(second_largest_counter([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

### 10. Using `reduce()` from `functools`
from functools import reduce

def second_largest_reduce(lst):
    first, second = reduce(lambda x, y: (y, x[0]) if y > x[0] else (x[0], x[1]) if x[0] > y > x[1] else (x[0], y), lst, (float('-inf'), float('-inf')))
    return second if second != float('-inf') else None

print(second_largest_reduce([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 