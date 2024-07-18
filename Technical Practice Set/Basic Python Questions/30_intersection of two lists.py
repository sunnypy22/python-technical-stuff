# Using List Comprehension

def intersection(list1, list2):
    return [element for element in list1 if element in list2]

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = intersection(list1, list2)
print("Intersection of list1 and list2:", result)  # Output: Intersection of list1 and list2: [3, 4, 5]

# Using set and intersection

def intersection_using_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = intersection_using_set(list1, list2)
print("Intersection of list1 and list2:", result)  # Output: Intersection of list1 and list2: [3, 4, 5]
