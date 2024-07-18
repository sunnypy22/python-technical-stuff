# 1. Using dict() Constructor

def list_to_dict_using_dict_constructor(list_of_tuples):
    return dict(list_of_tuples)

# Example usage
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
result = list_to_dict_using_dict_constructor(list_of_tuples)
print("Dictionary:", result)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 2. Using Dictionary Comprehension

def list_to_dict_using_comprehension(list_of_tuples):
    return {key: value for key, value in list_of_tuples}

# Example usage
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
result = list_to_dict_using_comprehension(list_of_tuples)
print("Dictionary:", result)  # Output: {'a': 1, 'b': 2, 'c': 3}
