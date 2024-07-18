# 1. Using the sum() Function

def sum_of_elements(lst):
    return sum(lst)

# Example usage
my_list = [1, 2, 3, 4, 5]
total_sum = sum_of_elements(my_list)
print(f"The sum of all elements in the list {my_list} is: {total_sum}")

# 2. Using a for Loop

def sum_of_elements_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
total_sum = sum_of_elements_loop(my_list)
print(f"The sum of all elements in the list {my_list} is: {total_sum}")

# 3. Using numpy.sum() (for numeric lists)

import numpy as np

def sum_of_elements_numpy(lst):
    return np.sum(lst)

# Example usage
my_list = [1, 2, 3, 4, 5]
total_sum = sum_of_elements_numpy(my_list)
print(f"The sum of all elements in the list {my_list} is: {total_sum}")
