# 1. Using List Comprehension (Recursive)

def flatten_recursive(nested_list):
    flattened_list = []
    for i in nested_list:
        if isinstance(i, list):
            flattened_list.extend(flatten_recursive(i))
        else:
            flattened_list.append(i)
    return flattened_list

# Example usage
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9]]]
result = flatten_recursive(nested_list)
print("Flattened list:", result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Using itertools.chain.from_iterable()

from itertools import chain

def flatten_iter_tools(nested_list):
    return list(chain.from_iterable(map(flatten_iter_tools, nested_list))) if isinstance(nested_list, list) else [nested_list]

# Example usage
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9]]]
result = flatten_iter_tools(nested_list)
print("Flattened list:", result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Using reduce() and operator.concat

from functools import reduce
import operator

def flatten_reduce(nested_list):
    return reduce(operator.concat, nested_list)

# Example usage
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9]]]
result = flatten_reduce(nested_list)
print("Flattened list:", result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
