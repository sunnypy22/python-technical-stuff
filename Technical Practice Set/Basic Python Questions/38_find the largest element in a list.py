# 1. Using the max() Function

def find_largest(lst):
    return max(lst)

# Example usage
my_list = [10, 5, 20, 8, 15]
largest = find_largest(my_list)
print(f"The largest element in the list {my_list} is: {largest}")

# 2. Using a for Loop

def find_largest_loop(lst):
    if not lst:
        return None  # Handle empty list case
    largest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
    return largest

# Example usage
my_list = [10, 5, 20, 8, 15]
largest = find_largest_loop(my_list)
print(f"The largest element in the list {my_list} is: {largest}")

# 3. Using numpy.max() (for numeric lists)

import numpy as np

def find_largest_numpy(lst):
    return np.max(lst)

# Example usage
my_list = [10, 5, 20, 8, 15]
largest = find_largest_numpy(my_list)
print(f"The largest element in the list {my_list} is: {largest}")
