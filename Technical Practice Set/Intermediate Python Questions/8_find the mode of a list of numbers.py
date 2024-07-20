# Method 1: Using collections.Counter

'''The collections.Counter class is a straightforward 
way to count the frequency of elements.'''

from collections import Counter

def mode_using_counter(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())
    return [num for num, count in counts.items() if count == max_count]

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Mode using Counter:", mode_using_counter(numbers))  # Output: [3]

# Method 2: Using a Dictionary

'''A dictionary can be used to count the frequency of each element manually.'''

def mode_using_dict(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = max(frequency.values())
    return [num for num, count in frequency.items() if count == max_count]

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Mode using Dictionary:", mode_using_dict(numbers))  # Output: [3]

# Method 3: Using statistics module

'''The statistics module provides a built-in mode function.'''

import statistics

def mode_using_statistics(numbers):
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        # Handle the case with multiple modes or no mode
        return "No unique mode found or input list is empty."

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Mode using statistics:", mode_using_statistics(numbers))  # Output: 3

# Method 4: Using scipy module

'''The scipy library provides a mode function that returns both the mode and its count.'''

from scipy import stats

def mode_using_scipy(numbers):
    mode_result = stats.mode(numbers)
    return mode_result.mode[0]

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Mode using scipy:", mode_using_scipy(numbers))  # Output: 3

# Method 5: Using Pandas

'''The pandas library offers the mode function that can return multiple modes if they exist.'''

import pandas as pd

def mode_using_pandas(numbers):
    return pd.Series(numbers).mode().tolist()

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Mode using pandas:", mode_using_pandas(numbers))  # Output: [3]


# Method 6: Brute Force Approach

'''Manually iterate through the list to count frequencies and determine the mode.'''

def mode_brute_force(numbers):
    max_count = 0
    mode = None
    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            mode = num
    return mode

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Mode using brute force:", mode_brute_force(numbers))  # Output: 3
