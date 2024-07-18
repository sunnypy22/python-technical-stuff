# 1. Using List Comprehension and set()

def common_elements_list_comprehension(list1, list2):
    return [element for element in list1 if element in list2]

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = common_elements_list_comprehension(list1, list2)
print("Common elements:", result)  # Output: Common elements: [3, 4, 5]

# 2. Using set.intersection()

def common_elements_set_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = common_elements_set_intersection(list1, list2)
print("Common elements:", result)  # Output: Common elements: [3, 4, 5]

# 3. Using filter() with lambda function

def common_elements_filter(list1, list2):
    return list(filter(lambda x: x in list1, list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = common_elements_filter(list1, list2)
print("Common elements:", result)  # Output: Common elements: [3, 4, 5]
