# 1. Using collections.Counter

from collections import Counter

def most_frequent_element_counter(lst):
    # Create a Counter object to count occurrences of each element
    counter = Counter(lst)
    
    # Use most_common(1) to get the most frequent element and its count
    most_common_element = counter.most_common(1)
    
    # Return the most frequent element
    return most_common_element[0][0]

# Example usage
numbers = [1, 2, 3, 1, 2, 2, 3, 1, 2, 2, 2]
result = most_frequent_element_counter(numbers)
print(f"The most frequent element is: {result}")  # Output: 2

# 2. Using max() with lst.count

def most_frequent_element_max_count(lst):
    # Use max() with a custom key function to find the element with maximum count
    return max(lst, key=lst.count)

# Example usage
numbers = [1, 2, 3, 1, 2, 2, 3, 1, 2, 2, 2]
result = most_frequent_element_max_count(numbers)
print(f"The most frequent element is: {result}")  # Output: 2

# 3. Using a dictionary for manual counting

def most_frequent_element_dict(lst):
    # Initialize an empty dictionary to count occurrences
    count_dict = {}
    
    # Count occurrences of each element
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    
    # Find the element with the maximum count
    most_frequent_element = max(count_dict, key=count_dict.get)
    
    return most_frequent_element

# Example usage
numbers = [1, 2, 3, 1, 2, 2, 3, 1, 2, 2, 2]
result = most_frequent_element_dict(numbers)
print(f"The most frequent element is: {result}")  # Output: 2
