# 1. Using List Comprehension

def remove_element_list_comprehension(lst, element):
    return [x for x in lst if x != element]

# Example usage
input_list = [1, 2, 3, 4, 2, 2, 5]
element_to_remove = 2
result = remove_element_list_comprehension(input_list, element_to_remove)
print("List after removing element:", result)  # Output: List after removing element: [1, 3, 4, 5]

# 2. Using filter() with Lambda Function

def remove_element_filter(lst, element):
    return list(filter(lambda x: x != element, lst))

# Example usage
input_list = [1, 2, 3, 4, 2, 2, 5]
element_to_remove = 2
result = remove_element_filter(input_list, element_to_remove)
print("List after removing element:", result)  # Output: List after removing element: [1, 3, 4, 5]

# 3. Using while Loop (in-place modification)

def remove_element_while_loop(lst, element):
    while element in lst:
        lst.remove(element)
    return lst

# Example usage
input_list = [1, 2, 3, 4, 2, 2, 5]
element_to_remove = 2
result = remove_element_while_loop(input_list, element_to_remove)
print("List after removing element:", result)  # Output: List after removing element: [1, 3, 4, 5]
