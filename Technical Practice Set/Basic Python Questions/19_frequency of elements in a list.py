# 1. Using collections.Counter and Dictionary Comprehension

from collections import Counter

def element_frequency_counter(input_list):
    # Use Counter to count occurrences of each element
    counter = Counter(input_list)
    
    # Convert Counter object to a dictionary comprehension
    frequency_dict = {key: value for key, value in counter.items()}
    
    return frequency_dict

# Example usage
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
output = element_frequency_counter(input_list)
print(output)  # Output: {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 3, 7: 1}

# 2. Using collections.Counter Only

from collections import Counter

def element_frequency_counter_only(input_list):
    # Use Counter to count occurrences of each element
    counter = Counter(input_list)
    
    return dict(counter)

# Example usage
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
output = element_frequency_counter_only(input_list)
print(output)  # Output: {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 3, 7: 1}

# 3. Using dict and Loop

def element_frequency_dict(input_list):
    frequency_dict = {}
    
    # Count occurrences of each element using a loop
    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
            
    return frequency_dict

# Example usage
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
output = element_frequency_dict(input_list)
print(output)  # Output: {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 3, 7: 1}
