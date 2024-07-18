# Using index() Method

def find_index_using_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return None  # Return None if element is not found in the list

# Example usage
my_list = [10, 20, 30, 40, 50]
element_to_find = 30
index = find_index_using_index(my_list, element_to_find)
print(f"Index of {element_to_find} in list:", index)  # Output: Index of 30 in list: 2

# Using List Comprehension

def find_indices_using_list_comprehension(lst, element):
    return [index for index, value in enumerate(lst) if value == element]

# Example usage
my_list = [10, 20, 30, 40, 30, 50, 30]
element_to_find = 30
indices = find_indices_using_list_comprehension(my_list, element_to_find)
print(f"Indices of {element_to_find} in list:", indices)  # Output: Indices of 30 in list: [2, 4, 6]
