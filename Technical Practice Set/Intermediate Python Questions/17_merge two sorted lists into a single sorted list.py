# Method 1: Using the Two-Pointer Technique

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Method 2: Using the heapq Module

import heapq

def merge_sorted_lists_heapq(list1, list2):
    return list(heapq.merge(list1, list2))

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists_heapq(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Method 3: Using Sorting after Concatenation

def merge_sorted_lists_sort(list1, list2):
    return sorted(list1 + list2)

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists_sort(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Method 4: Using List Comprehension with zip

def merge_sorted_lists_zip(list1, list2):
    merged_list = []
    i, j = 0, 0
    n, m = len(list1), len(list2)

    while i < n and j < m:
        merged_list.append(list1[i] if list1[i] < list2[j] else list2[j])
        i, j = (i + 1, j) if list1[i] < list2[j] else (i, j + 1)
    
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists_zip(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
