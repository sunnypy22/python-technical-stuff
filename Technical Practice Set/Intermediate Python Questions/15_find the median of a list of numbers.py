# Method 1: Using Built-in Functions

'''1. Using statistics.median()
'''

import statistics

def find_median_statistics(numbers):
    return statistics.median(numbers)

# Example usage
numbers = [1, 3, 3, 6, 7, 8, 9]
print(find_median_statistics(numbers))  # Output: 6

# Method 2: Sorting and Manual Calculation

'''1. Manual Calculation after Sorting
'''

def find_median_sorted(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

# Example usage
numbers = [1, 3, 3, 6, 7, 8, 9]
print(find_median_sorted(numbers))  # Output: 6

# Method 3: Using Numpy

'''1. Using numpy.median()
'''

import numpy as np

def find_median_numpy(numbers):
    return np.median(numbers)

# Example usage
numbers = [1, 3, 3, 6, 7, 8, 9]
print(find_median_numpy(numbers))  # Output: 6.0


# Method 4: Using Heap Data Structures

'''1. Using Two Heaps
'''

import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []  # Min-heap for the larger half
        self.max_heap = []  # Max-heap for the smaller half
    
    def add_num(self, num):
        # Add to max_heap (invert value to use min-heap as max-heap)
        heapq.heappush(self.max_heap, -num)
        
        # Balance heaps
        if (self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Balance size: max

                # Balance size: max_heap can have at most one more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

# Example usage
finder = MedianFinder()
numbers = [1, 3, 3, 6, 7, 8, 9]
for number in numbers:
    finder.add_num(number)
print(finder.find_median())  # Output: 6

# Method 5: Using Manual Calculation with List Comprehension

'''1. Manual Calculation with List Comprehension
'''

def find_median_list_comprehension(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    return (sorted_numbers[mid] if n % 2 != 0 else (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2)

# Example usage
numbers = [1, 3, 3, 6, 7, 8, 9]
print(find_median_list_comprehension(numbers))  # Output: 6


# Method 6: Using QuickSelect Algorithm

'''1. QuickSelect for Median
'''

import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def find_median_quickselect(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return quickselect(numbers, n // 2)
    else:
        return (quickselect(numbers, n // 2 - 1) + quickselect(numbers, n // 2)) / 2

# Example usage
numbers = [1, 3, 3, 6, 7, 8, 9]
print(find_median_quickselect(numbers))  # Output: 6
